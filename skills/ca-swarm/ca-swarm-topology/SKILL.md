---
name: ca-swarm-topology
description: Chooses between one agent and a multi-agent shape using published evidence. Use when deciding how many agents a task needs and how they coordinate.
metadata:
  kind: procedure
  parent: ca-swarm
---
# Topology

**Purpose:** The simplest shape that works.

## Steps
1. Default to one agent; strengthen its tools and prompts first.
2. Split only for overflowing context, truly parallel subtasks, or roles needing different tools, models or permissions.
3. Keep writes single-threaded: parallel readers, searchers and reviewers; one writer per area.
4. Avoid splitting sequential planning; studies show multi-agent setups degrade it.
5. Never run unchecked independent agents; central verification limits error amplification.
6. Scale agent count to complexity, and budget for many times the tokens.

## Output
Chosen shape, the reason, and a dependency sketch.
