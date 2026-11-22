---
name: ca-context-window
description: Protects the attention budget of a working agent. Use when sessions grow long, agents drift, or context is preloaded wholesale.
metadata:
  kind: checklist
  parent: ca-context
---
# Attention budget

**Purpose:** The smallest set of high-signal tokens.

## Checks
1. Retrieve narrowly, just in time; hold paths and queries, not payloads.
2. Remove distractors: plausible but irrelevant text harms most.
3. Keep state in files so sessions can be cleared.
4. Clear old tool results first; compact at natural boundaries, keeping decisions, open problems and next steps.
5. Start fresh with a good brief rather than push on.
6. Subagents explore and return summaries of one to two thousand tokens.
7. Grow wary as windows fill; instinct matters more than any number.

## Output
A leaner window and a hand-over note.
