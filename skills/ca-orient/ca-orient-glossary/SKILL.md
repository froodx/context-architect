---
name: ca-orient-glossary
description: Fixes one meaning per term in each bounded context. Use when terms differ between code, docs, interface and people, or no glossary exists.
metadata:
  kind: procedure
  parent: ca-orient
---
# Ubiquitous language

**Purpose:** One meaning per term within each bounded context.

## Steps
1. Spot drift, such as reversal, chargeback and refund naming one thing.
2. Define each term once: meaning, kind, bounded context, aliases to retire.
3. Start with ten terms. Add more only when confusion costs something.
4. Propose renames in code as small tickets.
5. Translate explicitly where bounded contexts meet.

## Output
Entries in `../../context-architect/references/glossary.md` form, plus rename tickets.
