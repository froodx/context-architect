---
name: ontology-write
description: Writes one SKILL.md node within the spec and a 150-word budget. Use when writing or rewriting a single node.
metadata:
  kind: procedure
  parent: ontology-builder
---
# Write a node

**Purpose:** One job in 150 words, frontmatter included.

## Steps
1. Name: lowercase, digits, single hyphens, up to 64 characters, equal to the folder, unique.
2. Description: third person, what it does, then "Use when" plus trigger keywords. No colons or XML.
3. Metadata: kind (router, procedure, checklist) and parent.
4. Body: Purpose, then Steps or Checks, then Output. Routers add Routes.
5. Imperative voice; one idea per line; consistent glossary terms.
6. No dates or time-sensitive claims in nodes.
7. Point to references by relative path.

## Output
A node passing `../ontology-validate/SKILL.md`.
