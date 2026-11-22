---
name: ontology-validate
description: Runs the deterministic suite checks and a stranger test. Use when any node changes, and before packaging or sharing a suite.
metadata:
  kind: procedure
  parent: ontology-builder
---
# Validate

**Purpose:** Let a deterministic check hold the structure.

## Steps
1. Run `python3 scripts/validate_suite.py . --tree` from the suite root.
2. It checks word limits, frontmatter, names, parents, routes, references, reachability and house style.
3. Fix every error; never raise the limit to pass.
4. Regenerate the index with `--index ONTOLOGY-INDEX.md`.
5. Then the stranger test: read three random nodes cold. Can you act on each?

## Output
Zero errors, a fresh index and notes from the stranger test.
