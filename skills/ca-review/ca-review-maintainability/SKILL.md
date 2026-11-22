---
name: ca-review-maintainability
description: Prices the next likely change through the current and proposed designs. Use when judging long-term cost to readers, agents and future work.
metadata:
  kind: procedure
  parent: ca-review
---
# Price the next change

**Purpose:** Protect the environment the next agent will work in.

## Steps
1. Pick a likely follow-on change from a ticket, incident or roadmap; label hypotheticals.
2. Walk it through both designs: which modules, schemas, tests and teams must change together?
3. Check dependency direction, hidden coupling, duplicated rules and ownership.
4. Could an existing interface hide the volatile decision?
5. Compare keeping, local repair and redesign by actual change cost.
6. Docs, glossary and ADRs updated alongside.

## Output
The edit path, trade-off and smallest justified intervention; deferred debt gets a revisit signal.
