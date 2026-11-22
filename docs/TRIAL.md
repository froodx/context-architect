# Trials of version 5 (22 November 2026)

All runs were headless Claude Code sessions in throwaway repositories, with the suite installed as `README.md` describes (suite in `.daneel/`, skills in `.claude/skills/`, both kept out of git) and `CHARTER.md` at the default Deliver level. Nobody answered anything mid-run. Daneel committed as "Daneel"; other agents committed as "Other Agent". Reports, the managed `AGENTS.md` block and an ADR from the trials are in `docs/trial-evidence/`.

## Trial A: a messy shop service ("tillhub", about 370 lines)
**Planted problems:** SQL built from strings (injectable from a URL), float money with VAT computed in three places, config returning strings (two tests always failed), a live payment key and SMTP password in source, three unused dependencies with known advisories, dead code, tests that wiped the real database, a slow N+1 report, refunds that ignored promos and could repeat, a stale README, and no CI.

**Command:** the exact "Daneel, make it so" text from `MAKE_IT_SO.md`.

**Result:** about 12 minutes and $3.93. Two milestones were merged, each as one revertable merge commit after an independent check.
- The scorecard went from 0 to 8 of 10 green. The other two lines wait on the owner: rotating the leaked secrets, and requiring CI once there is a remote.
- Tests went from 8 (2 failing) to 39, green three runs in a row.
- About 30 per cent of the effort was strategic: one pricing module (ADR 0001, accepted citing the charter), a README that runs, CI and lint, and the managed `AGENTS.md` block with two enforcing checks (a lint rule against string-built SQL, and a test for secrets in source).
- The report lists what was not done and why: no ORM, no framework, no further splitting of `app.py`, no integer-pence migration.
- **The verifier earned its cost.** It failed milestone 1 because SQLite reuses a deleted row id, so a refunded order's lines attached to the next order. Daneel fixed this before merging.
- **One mistake.** The survey ran the old tests once against the real local database. Daneel had backed it up first, and restored it byte for byte. Version 5's survey now checks what tests touch before running them.

## Trial B: a multi-agent system ("hearthmind")
**Shape:** an orchestrator routing to a Researcher and a Coder on a local Ollama model, shell, file and web tools, shared JSON memory, `docker-compose.yml` (Ollama, API, nginx web UI), and a JavaScript front end.

**Planted problems:** `eval()` on model output, an unrestricted `shell=True` tool, web content flowing into a shell-capable agent, a committed `.env` and admin token, `innerHTML` on model output, CORS `*`, no timeouts or step limits, an unbounded memory file, three copies of the model client with different model names, unpinned images and no health checks, tests that needed a live model, unused vulnerable dependencies, and a stale README.

**Result:** about 14 minutes and $3.70. Two milestones were merged.
- The scorecard went from 0 to 7 of 10 green, with 1 amber: there was no Docker daemon to run `docker compose up`, so the compose file was only validated.
- Tests went from 3 (1 failing, live model needed) to 45 in 6 seconds, on a fake model.
- One ADR (tool safety), accepted citing the charter.
- Three decisions were batched into the report: rotate the leaked secrets, require CI, and make the research-to-Coder hand-off opt-in.
- Two independent reviewers found three real problems before merging, including CORS still letting other sites drive the agents.

## Trial C: another agent, then drift
1. **An ordinary feature by a non-Daneel agent.** Claude Haiku, with no Daneel skills, was asked to "add a Writer agent that drafts emails from research findings".
   - On a clone with the managed `AGENTS.md` block, it used the shared client, loop and tool allowlist, added tests, and ran lint (clean).
   - On a clone with the block removed, the code was nearly as good, because the cleaned-up structure guides it. It skipped lint, though, and left a lint error. CI would have caught it.
   - **Finding:** once a codebase is shipshape, its structure and checks do most of the guarding; the block makes agents run the checks.
2. **Deliberate slop.** A second "Other Agent" commit added a `pip install` tool using `shell=True` and silenced the linter with `# noqa`.
3. **"Daneel, carry on"** (about 7 minutes, $2.27). The drift check ran first and handled both commits.
   - It found that the pip tool let any web page run commands and read the admin token, proved this with a harmless test, and fixed it rather than reverting the other agent's work.
   - It turned the lesson into two checks: a test that fails on any `noqa` in the app code, and one stopping tests from starting pip.
   - It also fixed a routing bug in the Writer change ("write an email validator" went to the Writer).
   - The independent reviewer needed three rounds to pass the fix. Each round found real gaps.

## What this does and does not show
- It does show the full loop working unaided on two small but realistic codebases: survey, research with options, plan, delivery with real strategic work, guardrails, and drift caught and fixed.
- It does not show behaviour on a large codebase. Expect more sessions, and read the first plan.
- Costs are per run on the most capable model and scale with codebase size.
- Verification roughly doubles the cost of a run, and was worth it in every trial.
- Side effect: in this environment, one trial run also saved a lesson to the shared project memory.

---

# Trial run of v4 (22 November 2026)

**Setup.** A deliberately messy 30-line Python repository ("shopcalc"): 4 tests, one always failing (a coupon could make a bill negative), one flaky (random), duplicated pricing logic, a swallowed exception, and an unused `requests==2.19.0` pin with known advisories. The v4 skills were installed in `.claude/skills/`, `CHARTER.md` was copied in at the default Deliver level with the goal "tests pass reliably and pricing is correct and safe", and Claude Code was run headless with the exact command from `MAKE_IT_SO.md`. No human input during the run.

**What Daneel did, unaided**
- Wrote SURVEY, ALIGNMENT, PLAN (2 milestones, estimated 1 to 2 sessions plus about 15 minutes of review), STATE and a one-page REPORT under `docs/daneel/`, and one ADR (`0001-money-in-decimal`).
- Delivered 5 tickets in 5 commits on milestone branches, merged to `main` per the charter: deterministic test, coupon clamped at zero, unused vulnerable pin removed, penny-exact Decimal arithmetic kept behind the existing float API, input validation.
- An independent verifier rejected the first two attempts for real bugs (NaN slipping through; Decimal inputs returning floats); the third passed. Tests went from 4 (2 failing) to 18 (all passing).
- Stopped at a genuine gate: changing the public return type to Decimal is a public API change, so it asked the decision owner, with a recommendation.
- Proportion worked: CI, linting, type checking, packaging, configurable VAT and cosmetic renames were listed as "not doing" with reasons. It used 1 of 3 budgeted sessions.

**What we changed after the trial**
- The paperwork (about 1,600 words of docs for a 30-line module) was heavier than the code deserved, so `ca-campaign-proportion` now says paperwork scales with the codebase.

**Limits of this evidence.** One small repository, one run, one model and host. It shows the loop works end to end; it does not show how it behaves on a large or critical codebase. Start such a codebase at the Advise level for the first run.
