---
name: ca-review-agentic
description: Adds checks for risks typical of AI-generated code. Use when an agent wrote or substantially edited the change under review.
metadata:
  kind: checklist
  parent: ca-review
---
# Agent-written changes

**Purpose:** Counter automation bias; plausible is not proven.

## Checks
1. Duplication: copied blocks instead of reuse.
2. Error masking: broad catches, silent fallbacks, defaults hiding failure.
3. Tests weakened, skipped or rewritten to match the code.
4. Invented APIs, packages, flags or file paths.
5. Scope creep beyond the ticket; unrelated rewrites.
6. Reasoning that does not match the actions taken.
7. Size: large agent changes get split, not skimmed.
8. A clean-context reviewer, not the author's session, checks it.

## Output
Agentic findings added to the report, with evidence for each.
