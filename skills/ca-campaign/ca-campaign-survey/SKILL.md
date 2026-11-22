---
name: ca-campaign-survey
description: Maps a whole codebase and its health before any plan. Use when a campaign starts or the survey is older than the charter allows.
metadata:
  kind: procedure
  parent: ca-campaign
---
# Survey

**Purpose:** Know what exists and what actually hurts.

## Steps
1. Find build, test and lint commands. Check what tests touch; protect real data. Run them; record results.
2. Map modules, entry points, dependencies and data stores.
3. Find hotspots: files changed often in git history and hard to read.
4. Collect pain: failing tests, open issues, incident notes, TODOs.
5. Audit dependencies for known vulnerabilities and unsupported versions.
6. List existing ADRs, docs and conventions.
7. Score `../../context-architect/references/shipshape.md` as the baseline.

## Output
`docs/daneel/SURVEY.md`: map, top ten pains with evidence, working commands, baseline scorecard.
