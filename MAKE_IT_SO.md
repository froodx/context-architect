# Make it so

One command to start, two to keep it going. Everything else is Daneel's job.

## Once: set up (about ten minutes)
1. Install the suite into `.daneel/` and the skills into `.claude/skills/` or `.agents/skills/` (see `README.md`). Do not replace your project's own `AGENTS.md`.
2. Copy `CHARTER.md` into the root of the repository and fill in the lines marked **edit**. The defaults are sensible; the goal and the out-of-bounds list matter most.
3. Make sure the agent can run the project's tests in its environment.

## Start: the command
Paste this, as it is, into your agent from inside the repository:

> **Daneel, make it so.** Take charge of this repository under CHARTER.md. Survey it, check it against current best practice, and write a simple, doable plan with a realistic timeframe. Then deliver it in small, verified steps until it is shipshape, recording ADRs only for decisions that matter. Keep it proportionate: fix what hurts, put about a quarter of the effort into structure that makes future changes cheaper, no gold-plating. Stop only at a gate, a blocker or the budget, and leave me a one-page report.

What happens: `ca-campaign` scores the codebase against the ten-line shipshape scorecard, runs survey, alignment (with options compared), proportion and plan, writes `docs/daneel/PLAN.md` with milestones and a time range, then starts delivering the first milestone within the charter's budget. It ends every run with `docs/daneel/REPORT.md`.

## Keep going
- **"Daneel, carry on."** First checks what anyone else changed since his last verified revision (drift), then resumes from `docs/daneel/STATE.md` in a fresh session. Use it at the start of each working session, or schedule it (for example with Claude Code's `/loop` or a scheduled task) so it runs without you.
- **"Daneel, report."** A one-page status without doing more work.
- **"Daneel, replan: <what changed>."** Adjusts the plan, the cut line and the timeframe.
- **"Daneel, stop."** Finishes the current step safely, records state and stops.

More phrases (engage, steady as she goes, shields up, phasers on stun, drop anchor and the rest) are in `COMMANDS.md`.

## What stops drift between runs
Daneel keeps a short managed section of your project's `AGENTS.md` current: test commands, conventions, decisions in force and a finish checklist. Every agent that reads `AGENTS.md` (or `CLAUDE.md`, which imports it) sees these, with or without Daneel. Mistakes that recur become tests or CI checks, which hold even for an agent that ignores instructions. Whatever still slips through is caught by the drift check on the next "carry on".

## What you still do
- Read the one-page report when it arrives (about five minutes).
- Answer the queued decisions in the report, all at once, when it suits you. Daneel does not interrupt you mid-run.
- Glance at new ADRs when you feel like it; only one-way ones wait for you.

## Honest expectations
- **Timeframes are estimates in working sessions, with a range.** Calendar time depends mostly on how often a session runs and how quickly gated items are approved.
- **AGENTS.md is advice too.** Agents usually follow it, but nothing forces them. Only checks that run in CI, with branch protection requiring them, actually block a bad change. Turn on branch protection if you can.
- **A skill is advice; the host enforces.** Give the agent only the permissions the charter needs: branch protection, CI checks and the host's permission settings are what actually stop mistakes.
- **Tested end to end on two small, messy repositories**, a shop service and a multi-agent system, including another agent's follow-up work and a drift check (`docs/TRIAL.md`). **Your first run on a real repository is still a trial.** If the codebase is critical, start at the Advise level ("shields up"), read the first plan, then switch to Deliver.
