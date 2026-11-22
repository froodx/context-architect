---
name: ontology-model
description: Designs a skill tree from source material before any node is written. Use when starting a new suite or a new domain.
metadata:
  kind: procedure
  parent: ontology-builder
---
# Model the tree

**Purpose:** One node, one job, one trigger.

## Steps
1. List the jobs (verbs) and concepts (nouns) in the material.
2. Group jobs into domains of three to seven; domains become top-level routers in `skills/`.
3. Harnesses discover only top-level skills; leaves nest one level down and load by path.
4. Each leaf is a procedure or checklist with one clear trigger.
5. No two nodes share a trigger.
6. Specialise concepts; compose instructions.
7. Tables, templates and examples become references.

## Output
A tree sketch with name, kind and trigger per node.
