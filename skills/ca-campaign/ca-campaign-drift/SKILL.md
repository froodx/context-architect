---
name: ca-campaign-drift
description: Checks changes other people or agents made since Daneel last verified the repository. Use when told "carry on", before more planned work.
metadata:
  kind: procedure
  parent: ca-campaign
---
# Drift check
**Purpose:** Catch slop early.
## Steps
1. No managed block in `AGENTS.md`? Run `../ca-campaign-guardrails/SKILL.md` first.
2. Read the last verified revision in `docs/daneel/STATE.md`.
3. List commits since then not made by Daneel. None? Stop.
4. Run the checks the block names.
5. Compare the diff with its conventions and Accepted ADRs; new `d_` uses count.
6. Rate findings blocking, fix or nit; ignore taste.
7. Small clear fixes become tickets; repeats become guardrail checks.
8. Never revert others' work unasked.
9. Remove `d_` items proven unused (`../../context-architect/references/deprecation.md`); record the revision.
## Output
A short drift note in `docs/daneel/STATE.md`, plus any tickets.
