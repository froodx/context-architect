---
name: ca-steer-spec
description: Turns an agreed brief into a testable specification. Use when work must be written down before agents implement it.
metadata:
  kind: procedure
  parent: ca-steer
---
# Specify

**Purpose:** Write intent down once, testably.

## Steps
1. Problem and the people affected.
2. Goals and explicit non-goals.
3. Invariants that must always hold.
4. Interfaces and contracts, named in glossary terms.
5. Acceptance criteria, each testable.
6. Risks, door type and rollback plan.
7. Links to the brief and relevant ADRs.
8. For one-way doors, get human sign-off before decomposing.

## Output
A spec in `specs/`, short enough to read in five minutes.
