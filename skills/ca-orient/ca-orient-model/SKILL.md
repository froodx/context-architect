---
name: ca-orient-model
description: Builds and tests a project's domain model with competency questions. Use when people, code or agents disagree about meaning, authority or how concepts relate.
metadata:
  kind: procedure
  parent: ca-orient
---
# Model shared meaning

**Purpose:** A small model that answers real questions.

## Steps
1. Start from a question people need answered.
2. Give each term an id, kind, definition, scope and source.
3. Add typed relations only where they change an answer.
4. At boundaries, mark terms equivalent, narrower, broader or related; labels alone prove nothing.
5. Test with a case and a near miss that should answer differently.
6. Missing link? Answer unknown and name the evidence needed.
7. Check new terms keep earlier answers valid.

## Output
Entries per `../../context-architect/references/domain-model.md`, plus test results.
