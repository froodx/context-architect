---
name: ca-steer-roadmap
description: Sets technical direction over months with fitness functions and reserved capacity. Use when many changes pull a codebase in different directions.
metadata:
  kind: procedure
  parent: ca-steer
---
# Roadmap

**Purpose:** Make the long view explicit and checkable.

## Steps
1. Sketch the target architecture: bounded contexts and deep modules.
2. Define fitness functions: automated checks for key properties.
3. Reserve a share of capacity for debt and environment work.
4. Sequence by value, risk and dependency.
5. Prefer incremental, strangler-style moves over big-bang rewrites.
6. Record major choices as ADRs.
7. Revisit after each retrospective.

## Output
A one-page roadmap with milestones, fitness functions and linked ADRs.
