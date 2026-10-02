#!/usr/bin/env python3
"""
Regression tests: successful tool responses must never carry the access token.

Graph API list responses include `paging.next` / `paging.previous` URLs with
`access_token=<live token>` (and `appsecret_proof`) embedded in the query
string. Error responses were already scrubbed via _redact_url; successful
responses were passed straight through, so any tool that returned a paged
Graph response (real case: get_pixel_events) echoed the operator's
never-expiring system-user token into the caller's transcript.

Two layers are covered:
  1. make_api_request drops paging.next / paging.previous at any depth
     (cursors stay, so callers can still paginate with `after`).
  2. meta_api_tool redacts any leftover access_token= / appsecret_proof=
     query values in the final output, whatever field they sit in.
"""

import json

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from meta_ads_mcp.core.api import (
    _redact_secret_params,
    _strip_paging_links,
    make_api_request,
    meta_api_tool,
)

TOKEN = "EAAFAKETOKEN0123456789abcdefXYZ"
PROOF = "deadbeefcafe0123456789"
LEAKY_NEXT = f"https://graph.facebook.com/v25.0/123/stats?access_token={TOKEN}&limit=25&after=abc"
LEAKY_PREV = f"https://graph.facebook.com/v25.0/123/stats?access_token={TOKEN}&appsecret_proof={PROOF}&before=xyz"


def _paged_payload():
    return {
        "data": [{"value": "PageView", "count": 14}],
        "paging": {
            "cursors": {"before": "B", "after": "A"},
            "next": LEAKY_NEXT,
            "previous": LEAKY_PREV,
        },
    }


# --- Layer 1: _strip_paging_links ------------------------------------------

def test_strip_removes_next_and_previous_keeps_cursors():
    cleaned = _strip_paging_links(_paged_payload())
    assert cleaned["paging"] == {"cursors": {"before": "B", "after": "A"}}
    assert cleaned["data"] == [{"value": "PageView", "count": 14}]


def test_strip_works_at_any_depth():
    """Field-expansion responses nest paging inside objects and lists."""
    payload = {
        "id": "act_1",
        "adspixels": _paged_payload(),
        "list": [{"inner": _paged_payload()}],
    }
    text = json.dumps(_strip_paging_links(payload))
    assert TOKEN not in text
    assert PROOF not in text
    assert text.count('"after": "A"') == 2  # cursors survive in both nested spots


def test_strip_leaves_non_paging_next_keys_alone():
    """Only `next`/`previous` inside a `paging` object are links; a field that
    merely happens to be called `next` elsewhere is real data."""
    payload = {"next": "keep-me", "data": [{"previous": "keep-me-too"}]}
    assert _strip_paging_links(payload) == payload


def test_strip_handles_scalars_and_empty_paging():
    assert _strip_paging_links("text") == "text"
    assert _strip_paging_links(None) is None
    assert _strip_paging_links({"paging": {}}) == {"paging": {}}
    assert _strip_paging_links({"paging": "not-a-dict"}) == {"paging": "not-a-dict"}


# --- Layer 1 end-to-end: make_api_request ----------------------------------

@pytest.fixture
def mock_httpx_client():
    with patch("meta_ads_mcp.core.api.httpx.AsyncClient") as mock_client_cls:
        client = MagicMock()
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json.return_value = _paged_payload()
        response.raise_for_status.return_value = None
        client.get = AsyncMock(return_value=response)
        mock_client_cls.return_value.__aenter__ = AsyncMock(return_value=client)
        mock_client_cls.return_value.__aexit__ = AsyncMock(return_value=False)
        yield client


@pytest.mark.asyncio
async def test_make_api_request_strips_paging_links(mock_httpx_client):
    result = await make_api_request("123/stats", "SECRET_TOKEN", {})
    assert "next" not in result["paging"]
    assert "previous" not in result["paging"]
    assert result["paging"]["cursors"]["after"] == "A"
    assert TOKEN not in json.dumps(result)


# --- Layer 2: _redact_secret_params ----------------------------------------

def test_redact_masks_token_and_proof_values():
    text = f'{{"u": "https://x/y?access_token={TOKEN}&limit=5&appsecret_proof={PROOF}"}}'
    out = _redact_secret_params(text)
    assert TOKEN not in out and PROOF not in out
    assert "access_token=REDACTED" in out
    assert "appsecret_proof=REDACTED" in out
    assert "limit=5" in out  # unrelated params untouched


def test_redact_handles_value_at_end_and_escaped_json():
    assert _redact_secret_params(f"?access_token={TOKEN}") == "?access_token=REDACTED"
    escaped = json.dumps(f"https://x/y?a=1&access_token={TOKEN}")
    assert TOKEN not in _redact_secret_params(escaped)


def test_redact_leaves_clean_text_unchanged():
    clean = '{"data": [{"name": "access_token_rotation_policy"}], "limit": 25}'
    assert _redact_secret_params(clean) == clean


# --- Layer 2 end-to-end: meta_api_tool wrapper -----------------------------

@pytest.mark.asyncio
async def test_wrapper_redacts_token_in_any_string_field():
    @meta_api_tool
    async def fake_tool(access_token=None):
        # A leak in a field the paging-strip layer knows nothing about.
        return json.dumps({"preview_url": f"https://x/y?access_token={TOKEN}"})

    out = await fake_tool(access_token="SECRET_TOKEN")
    assert TOKEN not in out
    assert "access_token=REDACTED" in out


@pytest.mark.asyncio
async def test_wrapper_redacts_token_in_dict_results():
    @meta_api_tool
    async def fake_tool(access_token=None):
        return {"link": f"https://x/y?access_token={TOKEN}"}

    out = await fake_tool(access_token="SECRET_TOKEN")
    assert TOKEN not in out


@pytest.mark.asyncio
async def test_wrapper_passes_clean_output_through_unchanged():
    payload = json.dumps({"data": [1, 2, 3]}, indent=2)

    @meta_api_tool
    async def fake_tool(access_token=None):
        return payload

    assert await fake_tool(access_token="SECRET_TOKEN") == payload


# --- get_login_link must not show any part of the cached token --------------

@pytest.mark.asyncio
async def test_login_link_never_shows_token_prefix(monkeypatch):
    """It used to return `Token preview: <first 10 chars>...` — a partial
    disclosure of the live token. Now it only says that a token is cached."""
    from meta_ads_mcp.core import authentication

    monkeypatch.delenv("META_ADS_DISABLE_CALLBACK_SERVER", raising=False)
    token_info = MagicMock(created_at=1, expires_in=2)
    with patch.object(authentication.auth_manager, "get_access_token", return_value=TOKEN), \
         patch.object(authentication.auth_manager, "token_info", token_info, create=True):
        out = await authentication.get_login_link()

    assert "Already Authenticated" in out
    assert TOKEN[:10] not in out
    assert "Token preview" not in out


# --- Removed tool -----------------------------------------------------------

def test_get_capi_diagnostics_is_gone():
    """Meta no longer serves /server_events_diagnostic (Graph v25 returns
    400 code 2500 'Unknown path components'), so the tool was removed."""
    from meta_ads_mcp.core import conversions

    assert not hasattr(conversions, "get_capi_diagnostics")
    assert hasattr(conversions, "send_conversion_events")  # sibling untouched
