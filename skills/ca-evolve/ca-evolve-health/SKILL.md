---
name: ca-evolve-health
description: Measures whether the codebase and its context are improving, then prunes. Use when reviewing outcomes, failure modes or rules that no longer pay.
metadata:
  kind: procedure
  parent: ca-evolve
---
# Health

**Purpose:** Judge architecture by outcomes, then prune.

## Steps
1. Track escaped defects, repeated corrections, lead time, review burden, context size, cost and provenance coverage.
2. Keep a handful of real tasks as a benchmark; rerun when context changes.
3. Start from a real change or incident; separate trends from anecdotes.
4. Give each measure a baseline and an observation period.
5. Diagnose with `../../context-architect/references/failure-modes.md`.
6. Remove rules that cost more attention than they save.
7. Simplify before adding anything.

## Output
A health note: trend, top failure mode, one intervention or explicit deferral, its owner and next trigger.
