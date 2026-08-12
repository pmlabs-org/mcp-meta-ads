# mcp-meta-ads — Orientation

This is a Pathfinder-maintained fork of the open-source [Pipeboard Meta Ads MCP](https://github.com/pipeboard-co/meta-ads-mcp), deployed as a self-hosted remote MCP server (`PM_Facebook_Ads` / `meta-ads.mcp.pathfindermarketing.com.au`) rather than the upstream Pipeboard-hosted option. Registered in `pmtools/data/repos.json` as `mcp-meta-ads` (type `mcp`).

## Deploy model — image-based via GHCR, no droplet git clone

Unlike most Pathfinder MCPs, this one does **not** have a git clone on the droplet. CI (`.github/workflows/ci.yml`) builds and pushes the image to `ghcr.io/pmlabs-org/mcp-meta-ads:latest` on every push to `main`, then SSHes to the droplet and runs `docker compose pull meta-ads && docker compose up -d --force-recreate meta-ads`. Manual update if ever needed: `docker pull ghcr.io/pmlabs-org/mcp-meta-ads:latest && docker compose up -d --force-recreate meta-ads` on the droplet.

**Do not use the standard `pm.sub.ops.redeploy.mcp` git-clone-based flow for this repo** — it assumes `/opt/pmin-mcpinfrastructure/repos/mcp-<name>` exists, which it doesn't here. Verify a deploy landed by checking the specific GHA run's `deploy` job logs (see gotcha below), not just overall workflow status, and independently confirm via a direct `tools/list` JSON-RPC call against the live endpoint rather than trusting a green checkmark alone.

## Two tool-registration sites — both must be updated for a new module to actually work

This is the gotcha that caused a real incident (2026-08-12): 15 fully-built, CI-tested, merged tool modules sat completely invisible as MCP tools for ~4.5 months because they were merged (commits `a6f557a`, `0d42bf2`, `e2ddfc6`, 2026-03-31) but never wired into either registration site.

Adding a new file to `meta_ads_mcp/core/` with `@mcp_server.tool()`-decorated functions is **not enough on its own**. Both of these must be updated:

1. **`meta_ads_mcp/core/__init__.py`** — module-level imports (`from . import <module>`, following the existing pattern used by `ads_library`, `reports`, `duplication`, `authentication`). This registers the tools for stdio/package-level use and `pip install -e .` smoke tests.
2. **`meta_ads_mcp/core/server.py`** — inside the `streamable-http` transport startup block (search for `"Ensuring all tools are registered for HTTP transport"`), there's a **separate, explicit** `from . import <module1>, <module2>, ...` list. **This is the one that actually matters for the deployed remote MCP** — `PM_Facebook_Ads` is served over `streamable-http`, and FastMCP only registers what gets imported in that code path at server startup.

A module can be present in the repo, pass CI, and ship in every built Docker image while being 100% invisible as a callable tool — because CI/tests only import the module directly, they don't exercise the `server.py` HTTP-transport startup path the same way the deployed server does. **Always verify via a live `tools/list` call after registering a new module, not just a passing test suite.**

## GHCR permissions can silently break on a GitHub org transfer

See `pmin-brain/context/tool-gotchas.md` § GitHub for the full incident writeup. Short version: this repo (and others) transferred from the `PM-Labs` org to `pmlabs-org`. The git remote still resolves (`git push` to the old `PM-Labs/...` URL succeeds via GitHub's redirect), but the GHCR container package's own "Manage Actions access" grant did not carry over — CI's `docker push` step 403'd on every run for about a week (2026-08-05 to 2026-08-11) despite correct `permissions: packages: write` in the workflow YAML. A separate `Test and Build` workflow (tests only, no push) kept reporting green the whole time, so the failure went unnoticed until someone checked the `deploy` job's logs specifically.

If a future push seems to succeed but the live server doesn't reflect the change, check the `deploy` job's actual `docker push` step output before assuming the code is wrong.

## Local clone convention

`$HOME/mcp-meta-ads` is a reference clone only — never edit it directly. All edits go through `pm.sub.ops.repo.edit`, which creates a fresh worktree rooted at `origin/main` for every edit, so this local clone's own branch state can drift without affecting anything (it is not kept in sync automatically the way `pmin-claude`'s dev clone is).
