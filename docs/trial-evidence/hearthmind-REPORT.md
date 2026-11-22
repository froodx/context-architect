# Report: run 1, update 2026-11-22 (carry on)

## Since the last report
Another agent added two features. **The Writer agent is fine.** **The Coder's new `pip` tool was a security hole:** it ran model text through a shell even with shell turned off, so any web page the Researcher read could run commands on the host and read the admin token. I proved it, then fixed it without removing the feature. `pip` now follows ADR 0001: it is off unless `HEARTHMIND_ALLOW_SHELL=1`, takes one checked package name, runs without a shell and ignores pip config files. I also stopped the Writer's email shortcut catching coding tasks such as "write an email validator". Two new guard tests stop this kind of thing coming back: no `noqa` comments that switch off lint rules, and no test may start pip. Tests: 51 to 70. The independent check took three rounds (it found 5 fixes, then 2 more); all are fixed. Scorecard unchanged; 2 of 5 sessions used.

- Merge: acc84ac drift fix: `git revert -m 1 acc84ac`
- ADR 0001: one dated clarification (any tool that runs code counts as shell; Writer has no tools; opted-in commands can read secrets via `/proc`).
- Declined as unnecessary: wider version syntax for `pip`, guarding `Popen`/`os.system` in tests (not used).

# Report: run 1 (2026-11-22), first part

## What changed
- **Safe to run.** Model output is parsed as JSON, never `eval`'d. The Researcher can only fetch web pages. The Coder writes only inside a workspace, and shell commands are off unless you set `HEARTHMIND_ALLOW_SHELL=1` (ADR 0001). Other websites can no longer drive the agents through your browser, and the UI no longer renders model output as HTML.
- **Starts.** The API container crashed on start (`ModuleNotFoundError`); fixed and covered by a test. Images are pinned, with health checks, ports on localhost only and a data volume. `.env` is no longer committed or copied into the image. Two unused, vulnerable dependencies are gone; runtime is standard library only.
- **Changeable.** One LLM client, one agent loop, one config module. Steps, memory and tool output are bounded. Tests went from 3 (1 failing, needed a live model, wrote to the real `memory.json`) to 45, all run without a model in about 6 seconds.
- **Guarded.** CI workflow (ruff, pytest, compose check); ruff fails on `eval`, `exec` and `shell=True`. `AGENTS.md` managed block and `CLAUDE.md`, so every agent sees the same rules. README now gets a newcomer running.

## Scorecard
| # | Line | Before | Now |
|---|---|---|---|
| 1 | Runs | Red | Amber: tests and entrypoint verified; full `docker compose up` not run (no Docker daemon here) |
| 2 | Trustworthy tests | Red | Green: 45 pass on three runs in a row, fake LLM |
| 3 | Checked on every change | Red | Waiting on you (G2) |
| 4 | Safe | Red | Waiting on you (G1); code fixes done |
| 5 | Sound dependencies | Red | Green |
| 6 | Changeable hotspots | Red | Green |
| 7 | One way to do things | Red | Green |
| 8 | Efficient enough | Red | Green: bounded; per-run token use not measured (no pain yet) |
| 9 | Explained | Amber | Green |
| 10 | Guarded for every agent | Red | Green |

Timeframe: planned 1.5 to 2.5 sessions; used 1 of 5. On track, no replan.

## Decisions for you (nothing else is blocked)
- **G1 Rotate the admin token and API key** that were committed in a724c5a. Recommend: rotate both; do not rewrite git history.
- **G2 Require CI on `main`** once the repo has a GitHub remote. Recommend: yes.
- **G3 Research findings trigger the Coder automatically** on every research task. Recommend: make it opt-in; a one-line change I will make on "carry on" if you agree.
- **Heads-up:** `.env` is now untracked, so `git pull` deletes it from other clones. Copy it aside first, then put it back (it is ignored now). It happened here too and was restored.
- **Quick check (2 minutes):** run the README's three commands on a machine with Docker to turn line 1 green.

## ADRs
- 0001 Agent tools treat model output as untrusted. Accepted under the charter (two-way door).

## Dropped as unnecessary
Auth on `/task` (localhost plus CORS suffices for now), per-call container sandbox, prompts in files, SSRF filter, image digests, any framework.

## Independent checks
Two verifiers. They found 3 should-fix issues (crashes on odd model output, cross-site requests, secrets visible to shell) and doc gaps; all fixed and re-verified before merge.

## Merges (undo with the command shown)
- 49242cd Milestone 1, safe and starts: `git revert -m 1 49242cd`
- e8851b5 Milestone 2, guarded: `git revert -m 1 e8851b5`
- acc84ac Drift fix, pip tool: `git revert -m 1 acc84ac` (reverting reopens the hole)
