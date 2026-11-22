---
name: ca-adr-options
description: Compares decision options against explicit drivers before recommending one. Use when weighing alternatives for an architectural decision.
metadata:
  kind: procedure
  parent: ca-adr
---
# Weigh options

**Purpose:** Choose with evidence and criteria, not momentum.

## Steps
1. Name drivers: reversibility, blast radius, cost, risk, maintainability.
2. List genuine options, including keeping current behaviour.
3. Name the criterion that truly distinguishes them.
4. Say what each costs users, maintainers and operators.
5. Mark guesses; state confidence and what would change your mind.
6. Recommend one, kept apart from the recorded outcome.
7. One-way doors go to `../../ca-human/ca-human-gates/SKILL.md`.

## Output
Drivers, options table and recommendation, ready for the ADR.
