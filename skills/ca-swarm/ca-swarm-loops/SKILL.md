---
name: ca-swarm-loops
description: Bounds an automated agent loop with goals, brakes and gates. Use when work repeats without a new human instruction each time.
metadata:
  kind: checklist
  parent: ca-swarm
---
# Loops with brakes

**Purpose:** Let loops compound improvements, not mess.

## Checks
1. Finite goal, finish check, ceilings on turns, time and cost.
2. One task per turn; fresh brief; state in files and commits.
3. Before retrying, inspect side effects and reconcile partial writes.
4. A separate, sceptical evaluator.
5. Deterministic checks every turn.
6. Pause on missing permission, spent budget, repetition, stale contract or a one-way door.
7. Preserve the last safe state; say how to resume.
8. Prune harness parts newer models no longer need.

## Output
A loop design passing every check. Never loop where you would not leave a newcomer unsupervised.
