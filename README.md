# Meta Ads MCP

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that lets AI assistants — Claude, ChatGPT, Perplexity, Cursor, or any MCP client — run your Meta Ads end to end: launch campaigns, upload creatives, update budgets, and analyze performance through natural conversation across Facebook, Instagram, and every Meta ad surface. Available as a **hosted remote MCP** — no developer token, no self-hosting required.

This is the **Meta Ads node** of the [Pipeboard](https://pipeboard.co) MCP family — five remote MCP servers (Meta, Google, TikTok, Snap, Reddit) plus a unified [Pipeboard CLI](https://github.com/pipeboard-co/pipeboard-cli), **230+ tools** in total, one auth, one safety model. If you are comparing single-platform MCPs, you are looking at one node of a network — see [The Pipeboard MCP Family](#the-pipeboard-mcp-family) below.

> **Note:** This is an independent open-source project that uses Meta's public APIs. The hosted service behind it — [Pipeboard](https://pipeboard.co) — is a **badged Meta Business Partner** and an officially approved Meta app that manages **Meta, Google, TikTok, Snap & Reddit Ads** from one login (with a free plan) — so it is neither Meta-only nor something you have to self-host. Meta, Facebook, Instagram, and other Meta brand names are trademarks of their respective owners.

[![Meta Ads MCP Server Demo](https://github.com/user-attachments/assets/3e605cee-d289-414b-814c-6299e7f3383e)](https://github.com/user-attachments/assets/3e605cee-d289-414b-814c-6299e7f3383e)

[![MCP Badge](https://lobehub.com/badge/mcp/nictuku-meta-ads-mcp)](https://lobehub.com/mcp/nictuku-meta-ads-mcp)

mcp-name: co.pipeboard/meta-ads-mcp

## Community & Support

- [Discord](https://discord.gg/YzMwQ8zrjr). Join the community.
- [Email Support](mailto:info@pipeboard.co). Email us for support.

## Table of Contents

- [The Pipeboard MCP Family](#the-pipeboard-mcp-family)
- [🚀 Getting started with Remote MCP (Recommended for Marketers)](#getting-started-with-remote-mcp-recommended)
- [Pipeboard CLI (Alternative to MCP)](#pipeboard-cli-alternative-to-mcp)
- [Local Installation (Technical Users Only)](#local-installation-technical-users-only)
- [Features](#features)
- [Configuration](#configuration)
- [Available MCP Tools](#available-mcp-tools)
- [Licensing](#licensing)
- [Privacy and Security](#privacy-and-security)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## The Pipeboard MCP Family

Pipeboard ships a remote [MCP server](https://modelcontextprotocol.io/) for every major ad platform — plus a single-binary [CLI](https://github.com/pipeboard-co/pipeboard-cli) that wraps all of them. **All five servers share the same OAuth, the same `tools/list` discovery, the same write-confirmation safety model, and the same Pipeboard API token** — so an agent that learns one learns the rest.

### Remote MCP servers

| Platform | Remote MCP URL | Surface |
|---|---|---|
| **Meta Ads MCP** (Facebook + Instagram) | `https://meta-ads.mcp.pipeboard.co/` | **42 tools** — campaigns, ad sets, ads, creatives (incl. dynamic creative testing), image upload, insights, interest / behavior / demographic / geo targeting, page management |
| **Google Ads MCP** | `https://google-ads.mcp.pipeboard.co/` | **59 tools** — campaigns, ad groups, responsive search ads, Performance Max, keywords, GAQL queries, extensions (sitelinks, callouts, structured snippets), audiences, asset uploads, generic mutate |
| **TikTok Ads MCP** | `https://tiktok-ads.mcp.pipeboard.co/` | **59 tools** — campaigns, ad groups, ads, identities, image and video upload, audience and creative management, insights |
| **Snap Ads MCP** | `https://snap-ads.mcp.pipeboard.co/` | **37 tools** — ad accounts, campaigns, ad squads, ads, creatives, media upload, insights |
| **Reddit Ads MCP** | `https://reddit-ads.mcp.pipeboard.co/` | **33 tools** — accounts, campaigns, ad groups, ads, performance reports |

**That is 230+ tools across five ad platforms behind one auth.** Plug any of these URLs into Claude, Cursor, ChatGPT, Perplexity, or any MCP-compatible client. Connect your ad accounts once at [pipeboard.co](https://pipeboard.co) and every client gets access.

### Pipeboard CLI — the same tools, in your shell

[**Pipeboard CLI**](https://github.com/pipeboard-co/pipeboard-cli) is a single Go binary that exposes every MCP tool above as a typed shell command — built for AI coding agents (Claude Code, Cline, OpenClaw, Codex) and automation scripts that prefer subprocess calls over JSON-RPC:

```bash
brew install pipeboard-co/tap/pipeboard
export PIPEBOARD_API_TOKEN=<your-token>

pipeboard meta-ads get-campaigns   --account-id act_123
pipeboard google-ads execute-gaql-query   --customer-id 1234567890 --query "..."
pipeboard tiktok-ads get-campaigns --advertiser-id 7605685552884596737
```

Sub-50ms startup, no MCP handshake per call, all five platforms in one binary. Full docs in the [pipeboard-cli repo](https://github.com/pipeboard-co/pipeboard-cli).

### Why a family instead of one MCP per repo?

- **One account, every platform** — auth once at [pipeboard.co](https://pipeboard.co); manage Meta + Google + TikTok + Snap + Reddit from the same agent session
- **Cross-platform questions get cross-platform answers** — "which channel had the cheapest signups last week?" actually works
- **Same safety contract everywhere** — writes are explicit, new campaigns start paused where the platform supports it, and confirmation prompts look identical across all five servers
- **One token, one rate-limit ceiling, one place to revoke** — no juggling separate OAuth flows or per-vendor installs

Single-platform MCP benchmarks miss the point. The value is the network, not the node.

### How Pipeboard compares

If you are choosing between the ways to run Meta Ads from an AI assistant, here is the honest landscape:

| | **Pipeboard** | **Meta's official MCP** | **Open-source / self-hosted servers** |
|---|---|---|---|
| **Platforms** | Meta + Google + TikTok + Snap + Reddit, one login | Meta only | Usually Meta only |
| **Setup** | Hosted remote MCP — no developer token, ~2 minutes | Hosted by Meta (Meta only) | Self-host, manage your own tokens & upgrades |
| **Trust** | Badged Meta Business Partner + approved Meta app | First-party (Meta) | Varies — audit the code yourself |
| **Safety** | Explicit confirmation on every write; new campaigns start paused | Meta-defined | You build the guardrails |
| **Price** | Free plan, then paid tiers | Free (open beta) | Free, but you run the infra |

Meta's official connector is the safest **single-platform** option. Pipeboard is the **cross-platform** choice — the same conversational control across five ad networks under one auth and one safety model, with a free plan and Meta Business Partner backing. Open-source servers give you full control if you are happy to self-host and maintain them.

## Getting started with Remote MCP (Recommended)

The fastest and most reliable way to get started is to **[🚀 Get started with our Meta Ads Remote MCP](https://pipeboard.co)**. Our cloud service uses streamable HTTP transport for reliable, scalable access to your Meta Ads account. No technical setup required — just connect and start launching, updating, and analyzing campaigns with AI!

### For Claude Pro/Max Users

1. Go to [claude.ai/settings/integrations](https://claude.ai/settings/integrations) (requires Claude Pro or Max)
2. Click "Add Integration" and enter:
   - **Name**: "Pipeboard Meta Ads" (or any name you prefer)
   - **Integration URL**: `https://meta-ads.mcp.pipeboard.co/`
3. Click "Connect" next to the integration and follow the prompts to:
   - Login to Pipeboard
   - Connect your Facebook Ads account

That's it! You can now ask Claude to analyze your Meta ad campaigns, get performance insights, and manage your advertising.

#### Advanced: Direct Token Authentication (Claude)

For direct token-based authentication without the interactive flow, use this URL format when adding the integration:

```
https://meta-ads.mcp.pipeboard.co/?token=YOUR_PIPEBOARD_TOKEN
```

Get your token at [pipeboard.co/api-tokens](https://pipeboard.co/api-tokens).

### For Cursor Users

Add the following to your `~/.cursor/mcp.json`. Once you enable the remote MCP, click on "Needs login" to finish the login process.


```json
{
  "mcpServers": {
    "meta-ads-remote": {
      "url": "https://meta-ads.mcp.pipeboard.co/"
    }
  }
}
```

#### Advanced: Direct Token Authentication (Cursor)

If you prefer to authenticate without the interactive login flow, you can include your Pipeboard API token directly in the URL:

```json
{
  "mcpServers": {
    "meta-ads-remote": {
      "url": "https://meta-ads.mcp.pipeboard.co/?token=YOUR_PIPEBOARD_TOKEN"
    }
  }
}
```

Get your token at [pipeboard.co/api-tokens](https://pipeboard.co/api-tokens).

### For Other MCP Clients

Use the Remote MCP URL: `https://meta-ads.mcp.pipeboard.co/`

**[📖 Get detailed setup instructions for your AI client here](https://pipeboard.co)**

#### Advanced: Direct Token Authentication (OpenClaw and other clients)

For MCP clients that support token-based authentication, you can append your Pipeboard API token to the URL:

```
https://meta-ads.mcp.pipeboard.co/?token=YOUR_PIPEBOARD_TOKEN
```

This bypasses the interactive login flow and authenticates immediately. Get your token at [pipeboard.co/api-tokens](https://pipeboard.co/api-tokens).

### Other platforms

Meta Ads is one of five remote MCP servers in the family — see [The Pipeboard MCP Family](#the-pipeboard-mcp-family) for Google Ads, TikTok Ads, Snap Ads, and Reddit Ads, all set up the same way.

## Pipeboard CLI (Alternative to MCP)

If your agent prefers shell commands over JSON-RPC, the [Pipeboard CLI](https://github.com/pipeboard-co/pipeboard-cli) exposes every tool in the family as a typed subcommand — see [the family section above](#pipeboard-cli--the-same-tools-in-your-shell) for the quick install and the [pipeboard-cli repo](https://github.com/pipeboard-co/pipeboard-cli) for full docs.

## Local Installation (Advanced Technical Users Only)

🚀 **We strongly recommend using [Remote MCP](https://pipeboard.co) instead** - it's faster, more reliable, and requires no technical setup.

Meta Ads MCP also supports a local streamable HTTP transport, allowing you to run it as a standalone HTTP API for web applications and custom integrations. See **[Streamable HTTP Setup Guide](STREAMABLE_HTTP_SETUP.md)** for complete instructions.

## Features

- **Campaign Management**: Launch campaigns, ad sets, and ads, update budgets, pause and resume, and apply targeting changes — all from a conversation, with explicit confirmation on every write
- **Creative Operations**: Upload images, build creatives, and update copy, headlines, descriptions, and CTAs without leaving your AI client
- **Dynamic Creative Testing**: One API for both simple ads (single headline/description) and full A/B testing (multiple headlines/descriptions)
- **AI-Powered Campaign Analysis**: Let your favorite LLM analyze performance and surface actionable insights
- **Strategic Recommendations**: Receive data-backed suggestions for optimizing ad spend, targeting, and creative content
- **Budget Optimization**: Get recommendations for reallocating budget to better-performing ad sets
- **Creative Improvement**: Receive feedback on ad copy, imagery, and calls-to-action
- **Automated Monitoring**: Ask any MCP-compatible LLM to track performance metrics and alert you about significant changes
- **Cross-Platform Integration**: Works with Facebook, Instagram, and all Meta ad surfaces
- **Universal LLM Support**: Compatible with any MCP client including Claude Desktop, Cursor, Cherry Studio, and more
- **Partner-Backed, Not Just Open Source**: Built by [Pipeboard](https://pipeboard.co), a badged Meta Business Partner and officially approved Meta app — with a free plan and hosted remote MCP (no self-hosting required)
- **Enhanced Search**: Generic search function includes page searching when queries mention "page" or "pages"
- **Simple Authentication**: Easy setup with secure OAuth authentication
- **Cross-Platform Support**: Works on Windows, macOS, and Linux

## Configuration

### Remote MCP (Recommended)

**[✨ Get started with Remote MCP here](https://pipeboard.co)** - no technical setup required! Just connect your Facebook Ads account and start asking AI to analyze your campaigns.

### Local Installation (Advanced Technical Users)

For advanced users who need to self-host, the package can be installed from source. Local installations require creating your own Meta Developer App. **We recommend using [Remote MCP](https://pipeboard.co) for a simpler experience.**

### Available MCP Tools

**84 tools** across 30 categories. Quick reference:

| Category | Tools |
|---|---|
| [Accounts](#accounts) | `get_ad_accounts`, `get_account_info`, `get_account_pages` |
| [Campaigns](#campaigns) | `get_campaigns`, `get_campaign_details`, `create_campaign`, `update_campaign` |
| [Ad Sets](#ad-sets) | `get_adsets`, `get_adset_details`, `create_adset`, `update_adset` |
| [Ads](#ads) | `get_ads`, `get_ad_details`, `create_ad`, `update_ad` |
| [Creatives](#creatives) | `get_ad_creatives`, `get_creative_details`, `create_ad_creative`, `update_ad_creative` |
| [Images/Video](#imagesvideo) | `upload_ad_image`, `get_ad_image`, `get_image_by_hash`, `compute_image_crops`, `upload_video`, `get_ad_video` |
| [Insights](#insights) | `get_insights` |
| [Targeting](#targeting) | `search_interests`, `get_interest_suggestions`, `estimate_audience_size`, `search_behaviors`, `search_demographics`, `search_geo_locations`, `search_pages_by_name` |
| [Budget](#budget) | `create_budget_schedule` |
| [Ad Library](#ad-library) | `search_ads_archive` |
| [Search](#search) | `search` |
| [Auth](#auth) | `get_login_link` |
| [Other](#other) | `fetch` (record cache lookup, see [Search](#search)) |
| [Custom Audiences](#custom-audiences) | `create_custom_audience`, `get_custom_audiences`, `update_custom_audience`, `delete_custom_audience`, `add_users_to_custom_audience` |
| [Lookalike Audiences](#lookalike-audiences) | `create_lookalike_audience`, `get_lookalike_audience_status` |
| [Conversion API (CAPI)](#conversion-api-capi) | `send_conversion_events`, `get_capi_diagnostics` |
| [Custom Conversions](#custom-conversions) | `create_custom_conversion`, `get_custom_conversions` |
| [Advanced Insights](#advanced-insights) | `get_insights_with_breakdowns`, `create_async_insights_report`, `get_async_insights_report` |
| [Automated Rules](#automated-rules) | `create_automated_rule`, `get_automated_rules`, `get_rule_execution_history` |
| [Pixels](#pixels) | `get_pixels`, `get_pixel_events` |
| [A/B Testing](#ab-testing) | `get_ab_tests`, `create_ab_test` |
| [Product Catalogs](#product-catalogs) | `get_product_catalogs`, `get_catalog_products`, `create_product_catalog`, `get_product_sets` |
| [Lead Forms](#lead-forms) | `get_lead_forms`, `get_leads`, `create_lead_form` |
| [Reach & Frequency](#reach--frequency) | `get_reach_frequency_predictions`, `create_reach_frequency_prediction` |
| [Business Manager](#business-manager) | `get_business_info`, `get_business_ad_accounts`, `get_business_users` |
| [Page Posts](#page-posts) | `get_page_posts`, `get_post_insights`, `create_promoted_post` |
| [Offline Conversions](#offline-conversions) | `create_offline_event_set`, `upload_offline_events` |
| [Advanced Creatives](#advanced-creatives) | `delete_ad_creative`, `get_creative_preview`, `get_dynamic_creative_elements` |
| [Saved Audiences](#saved-audiences) | `create_saved_audience`, `update_saved_audience`, `delete_saved_audience` |
| [Attribution](#attribution) | `get_attribution_report`, `get_attribution_settings` |

All write tools (`create_*`, `update_*`) default new objects to `status: PAUSED` — Meta has no separate publish step, so flipping `status` to `ACTIVE` via `update_campaign` / `update_adset` / `update_ad` is what makes something go live. Every tool accepts an optional `access_token` param; omit it to use the cached/authenticated token.

---

#### Accounts

- **`get_ad_accounts`** — Ad accounts accessible by a user. Inputs: `user_id` (default `"me"`), `limit` (default 200). `amount_spent`/`balance` are returned in currency units (dollars), not cents.
- **`get_account_info`** — Detailed info for one ad account. Inputs: `account_id`, `fields` (optional override of the default field set — use for `funding_source_details`, `spend_cap`, `is_prepay_account`, etc). Adds `dsa_required`/`dsa_compliance_note` for EU accounts.
- **`get_account_pages`** — Facebook Pages associated with an ad account. Input: `account_id`.

#### Campaigns

- **`get_campaigns`** — List campaigns. Inputs: `account_id`, `limit`, `status_filter` (e.g. `ACTIVE`/`PAUSED`), `objective_filter` (single or list), `after` (pagination cursor).
- **`get_campaign_details`** — Full detail for one campaign. Input: `campaign_id`.
- **`create_campaign`** — Create a campaign with an ODAX objective (`OUTCOME_AWARENESS`, `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_SALES`, `OUTCOME_APP_PROMOTION` — legacy objectives like `LINK_CLICKS`/`CONVERSIONS` 400 out). Inputs: `account_id`, `name`, `objective`, `status` (default `PAUSED`), `special_ad_categories`, `daily_budget`/`lifetime_budget` (cents), `buying_type`, `bid_strategy` (default `LOWEST_COST_WITHOUT_CAP`), `bid_cap`, `spend_cap`, `campaign_budget_optimization`, `ab_test_control_setups`, `use_adset_level_budgets`. Campaigns don't support `start_time` — set that on the ad set instead.
- **`update_campaign`** — Update name/status/budget/bid strategy. Inputs: `campaign_id` + any of the create fields, plus `objective` and `adset_budgets` (the correct way to migrate CBO → ABO: pass `[{adset_id, daily_budget}, ...]` — Meta atomically clears the campaign budget and assigns per-ad-set budgets; the older `use_adset_level_budgets=true` flag is silently ignored by Meta).

#### Ad Sets

- **`get_adsets`** — List ad sets. Inputs: `account_id`, `limit`, `campaign_id` (optional filter).
- **`get_adset_details`** — Full detail for one ad set, including `frequency_control_specs`. Input: `adset_id`.
- **`create_adset`** — Create an ad set. Inputs: `account_id`, `campaign_id`, `name`, `optimization_goal` (valid values depend on objective + `destination_type` — see inline docstring for the full matrix), `billing_event`, `status` (default `PAUSED`), `daily_budget`/`lifetime_budget` (omit both if the parent campaign uses CBO), `targeting` (defaults to broad US 18–65 if omitted), `bid_amount`, `bid_strategy`, `bid_constraints` (required for `LOWEST_COST_WITH_MIN_ROAS`), `bid_adjustments`, `start_time`/`end_time`, `dsa_beneficiary`/`dsa_payor` (required for EU targeting), `promoted_object`, `destination_type`, `is_dynamic_creative`, `frequency_control_specs` (immutable after creation), `multi_advertiser_ads`, `regional_regulated_categories`/`regional_regulation_identities` (Taiwan/Australia/India/Singapore/Thailand), `attribution_spec`. Runs a pre-flight check against the parent campaign to catch CBO budget conflicts and missing `bid_amount` before hitting Meta's API.
- **`update_adset`** — Update an existing ad set. Same field set as `create_adset` minus the immutable ones (`is_dynamic_creative` and `attribution_spec` are accepted but Meta silently ignores/rejects changes to them post-creation — recreate the ad set instead).

#### Ads

- **`get_ads`** — List ads. Inputs: `account_id`, `limit`, `campaign_id`/`adset_id` (optional filters).
- **`get_ad_details`** — Full detail for one ad, including `preview_shareable_link`. Input: `ad_id`.
- **`create_ad`** — Create an ad from an existing creative. Inputs: `account_id`, `name`, `adset_id`, `creative_id`, `status` (default `PAUSED`), `bid_amount`, `tracking_specs` (pixel events). Dynamic Creative creatives require `is_dynamic_creative=true` on the parent ad set.
- **`update_ad`** — Update name/status/bid/creative on an ad. Inputs: `ad_id`, `name`, `status`, `bid_amount`, `tracking_specs`, `creative_id` (swaps the ad's creative — FLEX creatives can hit a first-image-mismatch error 3858355; the workaround is a new ad + pause old, since swapping isn't always possible).

#### Creatives

- **`get_ad_creatives`** — Creative(s) attached to an ad, with image hashes resolved to URLs and DPA/catalog creatives resolved to `catalog_id`/`catalog_name`. Input: `ad_id`.
- **`get_creative_details`** — Full detail for one creative by ID, including `asset_feed_spec`, `dynamic_creative_spec` (when applicable), and catalog resolution. Input: `creative_id`.
- **`create_ad_creative`** — Create a creative. Six modes: existing post (`object_story_id`), simple image/video (`image_hash`/`video_id` + `object_story_spec`), multi-variant copy (`messages[]`/`headlines[]`/`descriptions[]`), Placement Asset Customization (`optimization_type="PLACEMENT"` + `videos`/`images` + `asset_customization_rules`), Dynamic Creative (`dynamic_creative_spec`, requires `is_dynamic_creative` on the ad set), FLEX/Advantage+ (`optimization_type="DEGREES_OF_FREEDOM"`). Inputs: `account_id`, `name`, `page_id`, `link_url`, `message`/`messages`, `headline`/`headlines`, `description`/`descriptions`, `image_hash`/`image_hashes`/`images`, `video_id`/`videos`, `call_to_action_type`, `instagram_actor_id`, `dynamic_creative_spec`, `asset_customization_rules`, `creative_features_spec` (Advantage+ enhancement opt-in/out), `lead_gen_form_id`, `image_crops`, and more — see inline docstring.
- **`update_ad_creative`** — Meta's API does **not** allow updating content fields (message, headline, image, URL, etc.) on an existing creative — only `name` and `asset_feed_spec`-level optimization settings. To change content, create a new creative and point the ad at it via `update_ad(creative_id=...)`.

#### Images/Video

- **`upload_ad_image`** — Upload an image for use in creatives. Inputs: `account_id`, `file` (data URL/base64) or `image_url`, `name`. Returns `image_hash` plus a Meta CDN `url` for immediate viewing.
- **`get_ad_image`** — Fetch and view the image an existing ad is serving. Input: `ad_id`.
- **`get_image_by_hash`** — Fetch and view an image by its hash (e.g. from `upload_ad_image` or a creative's `image_hash`), without needing an ad. Inputs: `account_id`, `image_hash`.
- **`compute_image_crops`** — Compute the `image_crops` dict for `create_ad_creative` given a source image's dimensions — largest centered region per Meta's 6 accepted aspect ratios (`100x100`, `100x72`, `400x500`, `400x150`, `600x360`, `90x160`). Inputs: `image_width`, `image_height`, `crop_keys` (optional subset).
- **`upload_video`** — Upload a video to the account's video library. Inputs: `account_id`, `video_url` (preferred — Meta fetches server-side) or `file` (base64, ~100MB practical limit), `name`, `title`, `description`. Returns `video_id`.
- **`get_ad_video`** — Video details + source/thumbnail URLs + processing status for an ad's video creative. Inputs: `ad_id` or `video_id` (provide `account_id` too when possible — it avoids error 100/33 and error #10 on Business Manager tokens). Poll `video_status` ("processing" → "ready") before calling `create_ad_creative` with the video.

#### Insights

- **`get_insights`** — Performance metrics for a campaign/ad set/ad/account. Inputs: `object_id` (or the `account_id`/`campaign_id`/`adset_id`/`ad_id` aliases), `time_range` (preset string or `{since, until}`), `breakdown` (demographic/platform/creative-asset/attribution/SKAN — see inline docstring for the full list; `platform_position` auto-pairs with `publisher_platform`; `media_type` auto-clears `action_breakdowns`), `level`, `limit`, `after`, `action_attribution_windows`, `action_breakdowns`, `compact` (strips redundant `omni_*`/`onsite_web_*`/pixel-duplicate action-type rows, ~60% smaller).

#### Targeting

- **`search_interests`** — Search interest targeting options by keyword. Inputs: `query`, `limit`.
- **`get_interest_suggestions`** — Suggested interests based on existing ones. Inputs: `interest_list`, `limit`.
- **`estimate_audience_size`** — Comprehensive audience estimation via Meta's `reachestimate` API (with a `delivery_estimate` fallback, disabled by default via `META_MCP_DISABLE_DELIVERY_FALLBACK`). Inputs: `account_id`, `targeting` (full spec — demographics/geo/interests/behaviors), `optimization_goal` (default `REACH`). Also retains backwards-compat simple interest validation via `interest_list`/`interest_fbid_list` (no `account_id`/`targeting` needed for that path).
- **`search_behaviors`** — All available behavior targeting options. Input: `limit`.
- **`search_demographics`** — Demographic targeting options. Inputs: `demographic_class` (`demographics`, `life_events`, `industries`, `income`, `family_statuses`, `user_device`, `user_os`), `limit`.
- **`search_geo_locations`** — Search geographic targeting locations. Inputs: `query`, `location_types` (`country`/`region`/`city`/`zip`/`geo_market`/`electoral_district`), `limit`.
- **`search_pages_by_name`** — Search Facebook Pages within an account by name. Inputs: `account_id`, `search_term`.

#### Budget

- **`create_budget_schedule`** — Schedule a temporary budget increase on a campaign for a high-demand period (Unix timestamps). Inputs: `campaign_id`, `budget_value`, `budget_value_type` (`ABSOLUTE` or `MULTIPLIER`), `time_start`, `time_end`.

#### Ad Library

- **`search_ads_archive`** — Search the public Facebook Ads Library archive. Inputs: `search_terms`, `ad_reached_countries` (list of country codes), `ad_type` (default `ALL`, or `POLITICAL_AND_ISSUE_ADS`/`HOUSING_ADS`), `limit`, `fields`.

#### Search

- **`search`** — Generic search across your own ad accounts, campaigns, ads, pages, and businesses (not the public Ads Library — see [Ad Library](#ad-library) for that). Input: `query`. Returns matching record IDs (`account:...`, `campaign:...`, etc.) cached for a subsequent `fetch` call.

#### Auth

- **`get_login_link`** — Clickable login link for the local Meta OAuth flow. Requires your own Meta app (`META_APP_ID`) and the local callback server enabled; disabled entirely via `META_ADS_DISABLE_LOGIN_LINK`. Not needed on the hosted Pipeboard MCP, which authenticates via a Pipeboard API token instead.

#### Other

- **`fetch`** — Look up a record ID previously returned by `search` in the *same session*. Input: `id` (format `"type:id"`, e.g. `"account:act_123456"`). This does **not** hit the Meta API directly — for direct ID lookups use `get_campaign_details`/`get_adset_details`/`get_ads`/`get_adsets` instead.

#### Custom Audiences

- **`create_custom_audience`** — Create a custom audience. Inputs: `ad_account_id`, `name`, `subtype` (`CUSTOM`, `WEBSITE`, `APP`, `OFFLINE_CONVERSION`, `LOOKALIKE`, `ENGAGEMENT`, etc.), `description`, `customer_file_source`, `rule` (for WEBSITE/engagement audiences), `retention_days`.
- **`get_custom_audiences`** — List custom audiences for an account. Inputs: `ad_account_id`, `limit`.
- **`update_custom_audience`** — Update name/description/rule/retention. Input: `audience_id` + fields to change.
- **`delete_custom_audience`** — Permanently delete a custom audience. Input: `audience_id`. **Irreversible.**
- **`add_users_to_custom_audience`** — Add users to an existing audience. Inputs: `audience_id`, `schema` (field names, e.g. `["EMAIL","FN","LN"]`), `data` (rows matching schema order), `is_raw` (when `true`, SHA-256 hashes PII fields client-side before sending — required for raw/unhashed input).

#### Lookalike Audiences

- **`create_lookalike_audience`** — Create a lookalike from an existing custom audience. Inputs: `ad_account_id`, `name`, `origin_audience_id`, `country` (default `AU`), `ratio` (0.01–0.20), `type` (`similarity` or `reach`).
- **`get_lookalike_audience_status`** — Status/detail for a lookalike audience. Input: `audience_id`.

#### Conversion API (CAPI)

- **`send_conversion_events`** — Send server-side conversion events via Meta's Conversions API. Inputs: `pixel_id`, `events` (list — each with `event_name`, `event_time`, `user_data`, optional `custom_data`/`event_source_url`/`action_source`), `test_event_code`. PII fields in `user_data` (`em`, `ph`, `fn`, `ln`, `ct`, `st`, `zp`, `country`, `ge`, `db`, `external_id`) are SHA-256 hashed automatically if not already hashed.
- **`get_capi_diagnostics`** — Event quality/deduplication diagnostics for a pixel's server-side events. Input: `pixel_id`.

#### Custom Conversions

- **`create_custom_conversion`** — Define a custom conversion from a URL/event rule. Inputs: `ad_account_id`, `name`, `event_source_id` (pixel or app ID), `rule` (JSON string, e.g. `{"url":{"i_contains":"thank-you"}}`), `custom_event_type`, `default_conversion_value`.
- **`get_custom_conversions`** — List custom conversions for an account. Input: `ad_account_id`.

#### Advanced Insights

- **`get_insights_with_breakdowns`** — Insights with demographic/placement breakdowns and custom field selection (a lower-level alternative to `get_insights`). Inputs: `object_id`, `fields` (explicit metric list), `date_preset`/`time_range`, `time_increment` (`1`/`7`/`monthly`/`all_days`), `breakdowns`, `level`, `filtering`, `limit`.
- **`create_async_insights_report`** — Start an async insights report job for large result sets. Inputs: same shape as `get_insights_with_breakdowns` minus `time_increment`/`limit`. Returns a `report_run_id` to poll.
- **`get_async_insights_report`** — Poll/fetch results for a report started with `create_async_insights_report`. Inputs: `report_run_id`, `limit`, `after`. Returns job status + percent complete until the job finishes, then the report rows.

#### Automated Rules

- **`create_automated_rule`** — Create a Meta Ads automated rule (e.g. auto-pause on spend threshold). Inputs: `ad_account_id`, `name`, `evaluation_spec` (trigger conditions), `execution_spec` (action to take), `schedule_spec`, `entity_type` (`CAMPAIGN`/`ADSET`/`AD`, default `CAMPAIGN`).
- **`get_automated_rules`** — List automated rules for an account. Input: `ad_account_id`.
- **`get_rule_execution_history`** — Execution history for one rule. Input: `rule_id`.

#### Pixels

- **`get_pixels`** — List Meta Pixels (datasets) for an account. Input: `ad_account_id`.
- **`get_pixel_events`** — Event statistics for a pixel. Inputs: `pixel_id`, `start_time`/`end_time` (Unix timestamps, optional).

#### A/B Testing

- **`get_ab_tests`** — List A/B tests (ad studies) for an account. Inputs: `ad_account_id`, `limit`.
- **`create_ab_test`** — Create a split-test ad study across campaigns. Inputs: `ad_account_id`, `name`, `description`, `start_time`/`end_time` (ISO 8601), `campaign_ids`.

#### Product Catalogs

- **`get_product_catalogs`** — Product catalogs owned by a business. Input: `business_id`.
- **`get_catalog_products`** — Products within a catalog. Inputs: `catalog_id`, `limit`, `filter`.
- **`create_product_catalog`** — Create a new catalog. Inputs: `business_id`, `name`, `vertical` (default `commerce`; also `destinations`, `flights`, `home_listings`, `hotels`, `vehicles`).
- **`get_product_sets`** — Product sets within a catalog. Inputs: `catalog_id`, `limit`.

#### Lead Forms

- **`get_lead_forms`** — Lead gen forms for a Page. Inputs: `page_id`, `limit`.
- **`get_leads`** — Leads collected by a form. Inputs: `form_id`, `limit`.
- **`create_lead_form`** — Create a lead gen form. Inputs: `page_id`, `name`, `questions` (list of `{type, label?}` — `EMAIL`/`FULL_NAME`/`PHONE`/`CUSTOM`), `privacy_policy_url` (required by Meta), `thank_you_page_url`.

#### Reach & Frequency

- **`get_reach_frequency_predictions`** — List reach/frequency prediction jobs for an account. Inputs: `ad_account_id`, `limit`.
- **`create_reach_frequency_prediction`** — Create a reach/frequency prediction. Inputs: `ad_account_id`, `targeting`, `start_time`/`end_time`, `frequency_cap`, `objective` (default `REACH`).

#### Business Manager

- **`get_business_info`** — Business Manager details. Input: `business_id`.
- **`get_business_ad_accounts`** — Ad accounts owned by a Business Manager. Inputs: `business_id`, `limit`.
- **`get_business_users`** — Users with access to a Business Manager, including `email`. Inputs: `business_id`, `limit`.

#### Page Posts

- **`get_page_posts`** — Posts on a Facebook Page. Inputs: `page_id`, `limit`.
- **`get_post_insights`** — Metrics for one post. Inputs: `post_id`, `metrics` (defaults to impressions/engaged users/clicks/reactions).
- **`create_promoted_post`** — One-call boost of an existing Page post: creates a `POST_ENGAGEMENT` campaign → ad set → ad targeting that post in one go. Inputs: `ad_account_id`, `page_id`, `post_id`, `daily_budget` (cents), `targeting` (defaults to broad US 18+), `status` (default `PAUSED`).

#### Offline Conversions

- **`create_offline_event_set`** — Create an offline conversion event set. Inputs: `ad_account_id`, `name`, `description`.
- **`upload_offline_events`** — Upload offline conversion events (e.g. in-store purchases) to a set. Inputs: `event_set_id`, `events` (each with `match_keys` — PII auto-hashed if not already SHA-256 — plus `event_name`, `event_time`, optional `value`/`currency`).

#### Advanced Creatives

- **`delete_ad_creative`** — Permanently delete a creative. Input: `creative_id`. **Irreversible.**
- **`get_creative_preview`** — HTML preview of a creative in a given placement. Inputs: `creative_id`, `ad_format` (default `DESKTOP_FEED_STANDARD`; also `MOBILE_FEED_STANDARD`, `INSTAGRAM_STANDARD`, `RIGHT_COLUMN_STANDARD`, `DESKTOP_FEED_SQUARE`).
- **`get_dynamic_creative_elements`** — `asset_feed_spec`/`object_story_spec` for the creatives on an ad set — the individual components Meta mixes for Dynamic Creative. Input: `adset_id`.

#### Saved Audiences

- **`create_saved_audience`** — Save a targeting spec as a reusable saved audience. Inputs: `ad_account_id`, `name`, `targeting`.
- **`update_saved_audience`** — Update name/targeting on a saved audience. Input: `audience_id` + fields to change.
- **`delete_saved_audience`** — Permanently delete a saved audience. Input: `audience_id`. **Irreversible.**

#### Attribution

- **`get_attribution_report`** — Ad-level performance broken down by attribution window. Inputs: `ad_account_id`, `date_preset` (default `last_30d`), `attribution_windows` (default `["1d_click","7d_click","1d_view"]`).
- **`get_attribution_settings`** — Account-level `attribution_spec`, `default_dsa_beneficiary`, `default_dsa_payor`. Input: `ad_account_id`.


## Licensing

Meta Ads MCP is licensed under the [Business Source License 1.1](LICENSE), which means:

- ✅ **Free to use** for individual and business purposes
- ✅ **Modify and customize** as needed
- ✅ **Redistribute** to others
- ✅ **Becomes fully open source** (Apache 2.0) on January 1, 2029

The only restriction is that you cannot offer this as a competing hosted service. For questions about commercial licensing, please contact us.

## Privacy and Security

Meta Ads MCP follows security best practices with secure token management and automatic authentication handling. 

- **Remote MCP**: All authentication is handled securely in the cloud - no local token storage required
- **Local Installation**: Tokens are cached securely on your local machine

## Testing

### Basic Testing

Test your Meta Ads MCP connection with any MCP client:

1. **Verify Account Access**: Ask your LLM to use `mcp_meta_ads_get_ad_accounts`
2. **Check Account Details**: Use `mcp_meta_ads_get_account_info` with your account ID
3. **List Campaigns**: Try `mcp_meta_ads_get_campaigns` to see your ad campaigns

For detailed local installation testing, see the source repository.

## Troubleshooting

### 💡 Quick Fix: Skip the Technical Setup!

The easiest way to avoid any setup issues is to **[🎯 use our Remote MCP instead](https://pipeboard.co)**. No downloads, no configuration - just connect your ads account and start getting AI insights on your campaigns immediately!

### Local Installation Issues

For local installation issues, refer to the source repository. **For the easiest experience, we recommend using [Remote MCP](https://pipeboard.co) instead.**
