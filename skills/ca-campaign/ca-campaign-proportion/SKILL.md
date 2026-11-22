---
name: ca-campaign-proportion
description: Cuts gold-plating from findings, plans and tickets. Use when judging any candidate change in a campaign, or when work grows.
metadata:
  kind: checklist
  parent: ca-campaign
---
# Proportion

**Purpose:** Common sense; no super-sizing, no neglect.

## Checks
1. Does it fix a surveyed pain, a risk or a scorecard gap? If not, drop it.
2. Is there a smaller fix? Prefer config, deletion or a test to new code. Maybe dead? Mark it `d_`.
3. New abstraction, layer or tool? Only with two real current uses.
4. No rewrites; change incrementally.
5. Would a sensible senior engineer call it overkill? Then it is.
6. Strategic work: 20 to 30 per cent, each naming the changes it makes cheaper.
7. Stop polishing once acceptance passes.
8. Paperwork scales too: small codebase, short files.

## Output
Each item marked keep, shrink or drop, with one line why.
