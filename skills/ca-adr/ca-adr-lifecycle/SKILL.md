---
name: ca-adr-lifecycle
description: Manages ADR status, supersession, review and indexing. Use when an ADR is accepted, rejected, challenged, outdated or contradicted by code.
metadata:
  kind: procedure
  parent: ca-adr
---
# ADR lifecycle

**Purpose:** Keep decisions current without losing history.

## Steps
1. Status: proposed, accepted, rejected, deprecated, superseded.
2. Record acceptance only against an attributable decision, owner and date.
3. Accepted records are immutable; supersede and link both ways.
4. Review when the revisit trigger fires or the date arrives.
5. Lint the index for stale, conflicting or orphaned records.
6. Code contradicts an Accepted ADR? Raise it; never silently choose.
7. Reviews check changes against Accepted ADRs.

## Output
An index of decisions in force, at `docs/decisions/index.md`.
