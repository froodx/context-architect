---
name: daneel-suite
description: Routes a session to the Daneel role or the skill-suite builder. Use when starting any session with this suite.
metadata:
  kind: router
  parent: none
---
# Daneel suite

**Purpose:** Route to the right skill tree, loading as little as possible.

## Load order
1. `AGENTS.md` for conventions and precedence.
2. `SOUL.md`, then `USER.md`, then `MEMORY.md`.
3. One route below; descend only as the task needs.

## Routes
- `skills/context-architect/SKILL.md`: review, decide, plan, steer or maintain code as Daneel.
- `skills/ontology-builder/SKILL.md`: create, extend or validate a suite of 150-word skills.

## Rules
- Read a description before loading its file.
- Load references only when a step names them.
- Return to the parent when a leaf is done.

## Output
The chosen route, stated in one line.
