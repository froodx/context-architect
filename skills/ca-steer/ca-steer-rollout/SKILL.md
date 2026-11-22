---
name: ca-steer-rollout
description: Plans safe evolution of a live interface, schema or workflow. Use when old and new versions overlap in production or recovery would be costly.
metadata:
  kind: procedure
  parent: ca-steer
---
# Recoverable rollout

**Purpose:** Change live systems so people can recover.

## Steps
1. Identify old and new readers, writers, stored data and release authority.
2. Expand compatibly, migrate consumers and data, then retire the old contract once evidence shows it unused.
3. Make partial migrations safely resumable.
4. Start with a small cohort compared against a baseline.
5. Define the stop signal, operator and recovery action before widening.
6. Distinguish code rollback from data restoration or compensation.
7. Flag any point where rollback becomes repair.

## Output
Ordered stages with entry and exit checks and recovery limits.
