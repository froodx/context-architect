---
name: ca-adr
description: Routes the detection, comparison, writing and upkeep of Architecture Decision Records. Use when a significant technical decision is made, challenged or outdated.
metadata:
  kind: router
  parent: context-architect
---
# Architecture Decision Records

**Purpose:** Keep the why. Code shows only the present.

## Status meanings for agents
- Accepted: binding.
- Proposed: context only.
- Superseded, deprecated, rejected: history only.
- Conflict with an Accepted ADR: stop and propose a new one.

## Routes
- `ca-adr-detect/SKILL.md`: is an ADR needed?
- `ca-adr-options/SKILL.md`: weigh the alternatives.
- `ca-adr-write/SKILL.md`: draft the record.
- `ca-adr-lifecycle/SKILL.md`: supersede, review, index.

## Output
An ADR with status, owner and review date.
