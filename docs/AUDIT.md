# Self-audit for version 5

The goal, in the person's words: steer a codebase into something efficient, sustainable and manageable; fully review it, research options, and actually get it shipshape; a real balance of tactical and strategic work, never gold-plated; and keep it that way after Daneel leaves.

Each row is a gap found in version 4 (by reading the skills and by the version 4 trial), and what version 5 does about it.

| # | Gap in version 4 | Evidence | Fix in version 5 |
|---|---|---|---|
| 1 | No finish line. "Better" was whatever the plan said, so a campaign could stop early or never stop. | Trial 1 stopped with "nothing planned" once its two milestones were done. | `shipshape.md`: a ten-line scorecard with evidence for each line. Surveyed as a baseline, shown before and now in every report. The campaign ends when every line is green, N/A or gated. |
| 2 | Strategic work was a ceiling (at most 20 per cent) with no floor, and proportion dropped anything that did not fix a current pain, so structure work could be starved for ever. | Trial 1 did no structural work at all. | Proportion now cuts both ways: 20 to 30 per cent of each milestone is reserved for strategic work, and each item must name the future changes it makes cheaper. Plan milestones target scorecard lines. |
| 3 | "Research" meant finding one recommended practice per pain; options were not compared. | `ca-campaign-align` steps. | Significant items compare two or three options, always including the smallest fix, with costs. |
| 4 | A gate stopped the whole run. | `ca-campaign-execute` step 5. | A gated ticket waits; independent tickets continue. |
| 5 | Conventions lived in Daneel's own files, so any other agent's ordinary work could drift back. | Trial 1 left the project's `AGENTS.md` and `CLAUDE.md` untouched. | `ca-campaign-guardrails` keeps a short managed block in the project's own `AGENTS.md` and ratchets recurring mistakes into checks. |
| 6 | Nobody looked at work done between Daneel's runs. | No step for it. | `ca-campaign-drift` runs first on "carry on". |
| 7 | Installing the suite at the root replaced the project's `AGENTS.md`. | README install step 2. | The suite installs in `.daneel/`; the project's files are kept. |
| 8 | The trial's ADR held two decisions in about 380 words and was accepted silently. | `docs/decisions/0001` in trial 1. | One decision per ADR, about 200 words; cite the charter rule on self-acceptance. |

Later additions, from the person's feedback during the build:

| # | Gap | Fix |
|---|---|---|
| 9 | Gate questions could interrupt the person | Queued and asked together in the report; unblocked work continues |
| 10 | Rollback relied on reading git history | One revertable merge commit per change, listed with its revert command |
| 11 | Trials used toy repositories | Trial B is a multi-agent system with a local LLM, tools, memory, docker compose and a web UI; the scorecard gained agent-system notes |
| 12 | Dead code needed approval or lingered | "Phasers on kill" removes code proven unused, without waiting; the `d_` prefix marks code on its way out |

## What version 5 still cannot do

- **Instructions are advice.** `AGENTS.md` is read by most agents and usually followed, but nothing forces it. Only CI checks with branch protection actually stop a bad change. Daneel adds the checks; switching on branch protection is a gated permission change, so it waits for you.
- **Drift is caught when Daneel runs.** Schedule "Daneel, carry on" (daily or weekly) or slop can sit unnoticed until the next run.
- **Judgement is a model's judgement.** The scorecard and proportion rules make it visible and checkable, not infallible. Read the first plan on any codebase that matters.
- **Trial scale.** Tested on two small repositories. A large codebase will take many sessions; the plan says how many, with a range.
