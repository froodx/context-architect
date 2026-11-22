---
name: ca-review-design
description: Reviews structure, interfaces, dependencies and module boundaries. Use when a change alters how the code is organised.
metadata:
  kind: checklist
  parent: ca-review
---
# Design lens

**Purpose:** Keep modules deep and boundaries honest.

## Checks
1. Deep modules: small interface, much behind it.
2. Volatile decisions hidden behind stable interfaces.
3. Dependencies point towards stable, general code.
4. Bounded contexts respected; names match the glossary.
5. Composition preferred to deep inheritance.
6. Tactical patch or strategic fix? Disabling a retry button hides a bug; an idempotency key fixes the class of bug.
7. Could several agents work here in parallel without colliding?

## Output
Design findings with location, evidence and a suggested strategic alternative.
