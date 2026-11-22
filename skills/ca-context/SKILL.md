---
name: ca-context
description: Routes decisions about what agents know, see and remember. Use when shaping agent context, or when an agent errs for lack of it.
metadata:
  kind: router
  parent: context-architect
---
# Context architecture

**Purpose:** The right knowledge for the right agent, at the right moment, with the right authority, and a way to check it.

## First question
When an agent errs, ask what was in its window before blaming the model.

## Routes
- `ca-context-layers/SKILL.md`: persistent, project, perishable.
- `ca-context-window/SKILL.md`: protect the attention budget.
- `ca-context-item/SKILL.md`: describe items with the seven Ws.
- `ca-context-handoff/SKILL.md`: brief the next worker.
- `ca-context-learning/SKILL.md`: promote, expire, forget.

## Output
Context files that are short, typed, dated and sourced.
