---
name: ca-campaign-execute
description: Delivers the plan in small verified increments under the charter. Use when a plan exists and the person said make it so or carry on.
metadata:
  kind: procedure
  parent: ca-campaign
---
# Execute

**Purpose:** Steady, reversible progress without supervision.

## Steps
1. Take the next ready ticket from the plan.
2. Branch, implement, test; one writer per area.
3. An independent check verifies on the combined revision.
4. Merge as `CHARTER.md` allows, as one revertable merge commit; else open a pull request.
5. One-way door? Queue it for the report; continue independent tickets.
6. Record significant choices as ADRs; update state and progress.
7. Repeat until shipshape, the budget or only gated work remains.
8. Milestone done? Refresh guardrails via `../ca-campaign-guardrails/SKILL.md`.

## Output
Merged or proposed changes, updated `docs/daneel/STATE.md`, and a progress line per ticket.
