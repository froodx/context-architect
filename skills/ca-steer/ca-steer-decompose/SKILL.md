---
name: ca-steer-decompose
description: Splits a specification into tickets sized for one fresh context window. Use when planning work for one or many agents.
metadata:
  kind: procedure
  parent: ca-steer
---
# Decompose

**Purpose:** Each ticket fits one fresh context window.

## Steps
1. Prefer thin vertical slices that deliver testable value.
2. Give each ticket: goal, files in scope, acceptance test, dependencies, door type.
3. Put unknowns and risky work first, as spikes if needed.
4. Sketch the dependency graph.
5. A line suggests one agent; a fan allows parallel agents.
6. Keep tickets that touch the same module sequential.

## Output
Ordered tickets plus the dependency sketch, ready for `../../ca-swarm/SKILL.md`.
