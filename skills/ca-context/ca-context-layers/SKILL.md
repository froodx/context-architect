---
name: ca-context-layers
description: Places rules and facts in the right layer and entry file. Use when deciding where something should live, or setting up AGENTS.md, CLAUDE.md and similar files.
metadata:
  kind: procedure
  parent: ca-context
---
# Three layers

**Purpose:** Each item at the right lifespan, reach and home.

## Steps
1. Persistent: identity, standards, values.
2. Project: glossary, ADRs, specs, AGENTS.md.
3. Perishable: ticket, failing test, deadline.
4. Precedence: platform, person, organisation, project, task. Tasks cannot grant access.
5. Entry files stay short (under about 200 lines) and point to canonical files.
6. The closest AGENTS.md wins. Claude Code needs an @AGENTS.md import line in CLAUDE.md.
7. Compose small policy modules; never duplicate rules across files.
8. Lifespan is not sensitivity; scope private material.

## Output
Each item placed once, in one layer.
