---
name: ca-adr-detect
description: Decides whether a choice deserves an Architecture Decision Record. Use when unsure if a decision is significant enough to record.
metadata:
  kind: checklist
  parent: ca-adr
---
# Detect

**Purpose:** Record significant choices; skip cheap ones.

## Write an ADR when
1. It is hard or costly to reverse.
2. It shapes structure, quality attributes, dependencies, interfaces or construction techniques.
3. Two or more credible options exist, or there is no precedent.
4. It sets an invariant, policy or contract.
5. Agents keep repeating a mistake here.
6. It deviates from a standard or an Accepted ADR.
7. A legacy system lacks one for a key choice: write it retroactively.

## Skip when
- Local, reversible and obvious from the code.

## Output
One line: "ADR needed: yes or no, because..."
