# Shipshape scorecard

The finish line for a campaign. The survey scores it as a baseline, each milestone moves lines to green, and every report shows before and now. A campaign is done when every line is green, marked not applicable with a reason, or waiting at a named gate. Scale it to the codebase: a 300-line library needs less than a 300,000-line service, so mark lines N/A rather than invent work.

| # | Line | Green means (evidence) |
|---|---|---|
| 1 | Runs | One documented command builds and tests from a clean checkout (the command and its output) |
| 2 | Trustworthy tests | Suite passes three runs in a row; critical paths have tests (run log, list of paths) |
| 3 | Checked on every change | CI runs tests and lint; branch protection requires them where the host allows (CI file, settings or a gate asking for them) |
| 4 | Safe | No known high or critical vulnerabilities; no secrets in the repository; inputs validated where untrusted data enters (audit output, grep, review) |
| 5 | Sound dependencies | Pinned, supported, none unused (lock file, audit) |
| 6 | Changeable hotspots | The few files that change most can be changed safely: tests around them, no tangle a newcomer cannot follow (churn list, before and after) |
| 7 | One way to do things | One approach each for config, errors, logging and data access; duplicates removed (search results) |
| 8 | Efficient enough | No evidenced performance or cost problem left untriaged; tests run in minutes, not hours (timings) |
| 9 | Explained | README gets a newcomer running; significant decisions are Accepted ADRs that the code does not contradict (README, index) |
| 10 | Guarded for every agent | Managed block in `AGENTS.md` current and short; `CLAUDE.md` imports it; recurring mistakes have checks (the block, the checks) |

## Agent systems (orchestrators, tool-using agents, local or hosted LLMs)
Read these into the lines above; they are where agent codebases usually rot.
- **Line 2:** tests run without a live model, using a fake or recorded responses; a few golden-task evals cover the main flows.
- **Line 4:** tools that run commands, write files or call out are allowlisted and sandboxed; no session mixes untrusted input, secrets and outbound actions without a gate (Rule of Two); model output is never executed or trusted as instruction.
- **Line 7:** one model client with timeouts, retries and token limits; prompts live in files, not scattered strings; one memory store with a size cap.
- **Line 8:** token use and latency per run are measured; context is bounded, not grown each turn.
- **Line 1:** `docker compose up` (or the documented command) starts the stack with pinned images and a health check.

Tactical lines (1, 2, 4, 5) usually go green first. Strategic lines (6, 7, 9, 10) take the reserved strategic share of each milestone, so structure improves alongside fixes instead of never.
