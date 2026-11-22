---
name: ca-evolve-modules
description: Deepens modules and redraws boundaries through small refactors. Use when modules are shallow, tangled or blocking parallel work.
metadata:
  kind: procedure
  parent: ca-evolve
---
# Modules

**Purpose:** Deep modules with narrow, tested interfaces.

## Steps
1. Map bounded contexts and the modules within them.
2. Flag shallow modules, god modules and tangles.
3. Find where agents collide or need the whole codebase in view.
4. Propose one small, reversible refactor at a time.
5. Test through the interface so internals can change freely.
6. Align module names with the glossary.
7. Sample-review steady streams of small changes.

## Output
A module map and a queue of refactor tickets.
