# Campaign files

Daneel keeps a campaign's memory in the target repository, so any fresh session can resume. Keep each file short; link rather than copy.

| File | Written by | Holds |
|---|---|---|
| `docs/daneel/SURVEY.md` | `ca-campaign-survey` | One-page map; top ten pains with evidence; working build, test and lint commands; baseline shipshape scorecard; date and revision |
| `docs/daneel/ALIGNMENT.md` | `ca-campaign-align` | Pain, options compared (always including the smallest fix), recommendation, primary source, confidence |
| `docs/daneel/PLAN.md` | `ca-campaign-plan` | Milestones, tickets, cut line, not-doing list, timeframe range, gates |
| `docs/daneel/STATE.md` | `ca-campaign-execute` | Current milestone and ticket, branch, last verified revision, budget used, open gates, next step |
| `docs/daneel/REPORT.md` | `ca-campaign-report` | Latest one-page report with the scorecard before and now (older ones live in git history) |
| `docs/decisions/` | `ca-adr` | ADRs in MADR 4 form (one decision each, about 200 words), plus `index.md` |
| `AGENTS.md` (managed block only) | `ca-campaign-guardrails` | Commands, conventions, decisions in force and a finish checklist for every agent; see `agents-block.md` |
| `CLAUDE.md` | `ca-campaign-guardrails` | `@AGENTS.md`, created only if missing |

## PLAN.md shape

```markdown
# Plan (revision abc123, 2026-11-22)
Goal: <from CHARTER.md>
Timeframe: 3 milestones, 6 to 10 working sessions, plus about 1 hour of your review.

## Milestone 1: Make the tests trustworthy (2 to 3 sessions; scorecard lines 1, 2)
- [ ] T1 Fix the 4 flaky tests in checkout (two-way door)
- [ ] T2 Add the missing test for refunds (two-way door)
- [ ] T3 Strategic: one price function instead of three copies; makes the next promo and the VAT change one-file edits (two-way door)
Gate: none

## Not doing (and why)
- Migrating to a new framework: no surveyed pain it would fix.
```

## STATE.md shape

```markdown
Milestone: 1, ticket T2, branch daneel/t2-refund-test
Last verified revision: def456
Shipshape: 6 of 10 green (was 2), 1 N/A, 3 to go
Budget: 2 of 5 sessions used this run
Waiting on you: nothing
Drift since last check: 2 commits by others; 1 fix ticket (T7), 0 blocking
Next: finish T2, run independent check, merge per charter
```
