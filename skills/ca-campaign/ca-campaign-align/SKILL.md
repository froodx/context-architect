---
name: ca-campaign-align
description: Checks surveyed problems against current best practice for this stack. Use when a survey is done, before planning, or when options need researching.
metadata:
  kind: procedure
  parent: ca-campaign
---
# Align

**Purpose:** Fix real problems the standard way, not the fashionable way.

## Steps
1. For each top pain, find the official guidance for this language, framework and version.
2. Prefer primary sources: official docs, release notes, security advisories.
3. Note the project's own conventions; they win unless they cause the pain.
4. Significant items: compare two or three options, including the smallest fix, with costs.
5. No trend adoption, rewrite or new framework without evidence it pays.
6. Cite sources with dates; mark uncertainty.

## Output
`docs/daneel/ALIGNMENT.md`: pain, options, recommendation, source, confidence.
