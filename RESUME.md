## 2026-09-21: RESUME HERE — personal AI-engineering portfolio (MonetixPayne)

#learning/ai-engineering #status/active #personal

**Repo (live):** https://github.com/MonetixPayne/AI-Engineering
**Local:** `~/Projects/personal/ai-engineering-proof` (remote `git@github-personal:MonetixPayne/AI-Engineering.git`)
**Plan:** `learning/2026-09-21-ai-engineering-development-plan.md` (mirrored as `PLAN.md` in the repo)

### Identity wiring (done, do not redo)
- SSH key `~/.ssh/id_ed25519_personal`, host alias `github-personal`, key added to the account, auth verified.
- `~/.gitconfig` has `includeIf gitdir:~/Projects/personal/` -> `~/.gitconfig-personal`
  (`Tolga <132578049+MonetixPayne@users.noreply.github.com>`). Work email cannot leak into this repo.
- Separate from `verluna` (consultancy) and the dormant `tolgaoral` / `llrd` accounts.

### Plan shape
24 weeks, 1h/day, 7 phases, 7 gate artifacts. Two-tier portfolio: this repo + standalone gate repos
are pinned; `~/Projects/personal/ai-engineering-lab` (local only, not yet on GitHub) absorbs tutorial
work unpinned. Rule: no eval, no ship; no number, no claim.

### Where we stopped
Phase 0 scaffolded and pushed: `00-foundations/` with `enrich/{config,schemas,cost,calllog,llm,fetch,cli}.py`
as TODO stubs by day, `tests/{test_cost,test_retry}.py`, `urls.csv`, `pyproject.toml`, `uv.lock`,
and a README holding the 10-session day plan plus the empty results table.

- `uv sync` verified, all imports load.
- Personal Anthropic key in `00-foundations/.env` (gitignored), verified: models 200, message 200, 696ms.
  First key failed because it was org-scoped, not workspace-scoped. Current one is personal + workspace-scoped.
- `ENRICH_MODEL=claude-haiku-4-5-20251001` — dated snapshot pinned on purpose, never the alias.
- Account also has `claude-sonnet-5`, `claude-opus-5`, `claude-fable-5-1` for the D9 comparison and the Phase 2 grader.

**Next action: Phase 0 Day 1.** Fill `enrich/config.py` (pydantic-settings) and write
`complete(prompt: str) -> str` in `enrich/llm.py`. Raw text only. No retry, no cost, no schema —
those are D3/D5/D2 deliberately, so each failure is met alone.
Verify: `uv run python -c "from enrich.llm import complete; print(complete('say hi'))"`

### Open items
- `ai-engineering-lab` not created on GitHub yet (create only when the first experiment needs it).
- Profile README drafted at `~/Projects/personal/MonetixPayne` (committed locally, remote set);
  the `MonetixPayne/MonetixPayne` repo does not exist yet, so it is unpushed.
- No contact links in the profile README, and no employer named. Tolga's call.
- `orca open` CLI is broken (symlink resolution); open files with `open -t` instead.
