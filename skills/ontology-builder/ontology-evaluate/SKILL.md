---
name: ontology-evaluate
description: Tests whether a suite actually helps agents on real tasks. Use when building a suite, after significant changes, or when switching models.
metadata:
  kind: procedure
  parent: ontology-builder
---
# Evaluate

**Purpose:** Prove the skills help; structure alone proves nothing.

## Steps
1. Before writing, collect at least three realistic tasks per domain, with expected behaviour.
2. Run each without the suite to set a baseline.
3. Run with the suite; check the right skill triggered and was followed.
4. Note misfires: wrong trigger, ignored step, missing context.
5. Fix descriptions first, then bodies.
6. Repeat on each model you use, small and large.
7. Keep the tasks as a regression set; start from `../../../docs/EVALUATION.md`.

## Output
A results table per task: baseline, with suite, notes.
