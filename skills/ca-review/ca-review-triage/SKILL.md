---
name: ca-review-triage
description: Sets review depth from reversibility, blast radius, evidence and size. Use when starting any review.
metadata:
  kind: checklist
  parent: ca-review
---
# Triage

**Purpose:** Spend review attention where mistakes cost most.

## Checks
1. Door: two-way (easily reversed) or one-way?
2. Blast radius: function, module, service, external parties or people?
3. Evidence: tests, types, CI, reproduction. Trustworthy?
4. Size: about 100 changed lines reviews well; past roughly 400, ask to split. Refactors go separately.
5. Author: agent-written? Add `../ca-review-agentic/SKILL.md`.

## Depth
- Light: two-way, local, green evidence. Correctness only.
- Standard: add design and maintainability.
- Deep: one-way or wide radius. All lenses, plus `../../ca-human/ca-human-gates/SKILL.md`.

## Output
One line: door, radius, evidence, size, depth.
