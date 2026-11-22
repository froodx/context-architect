---
name: ca-adr-write
description: Drafts an Architecture Decision Record in MADR 4 form. Use when a new decision needs recording.
metadata:
  kind: procedure
  parent: ca-adr
---
# Write the ADR

**Purpose:** A short record a future stranger can trust.

## Steps
1. Copy `../../context-architect/references/adr-template.md` to `docs/decisions/NNNN-title-with-dashes.md`. Never reuse numbers.
2. Front matter: status Proposed, date, decision-makers, consulted, informed.
3. Context and problem statement, using the seven Ws.
4. Drivers, considered options, outcome with justification.
5. Consequences, then confirmation: the test or check proving it holds.
6. Add a one-line Y-statement summary and a confidence level.
7. One decision, under 250 words with front matter; longer means split or trim.
8. Open it as a pull request. If `CHARTER.md` lets Daneel accept it, cite that rule.

## Output
A Proposed ADR and its index line.
