---
name: ca-review-security
description: Traces authority and exposure across trust boundaries. Use when a change touches data, permissions, secrets, external input, dependencies, skills or agent tools.
metadata:
  kind: checklist
  parent: ca-review
---
# Security lens

**Purpose:** Assume the model will be fooled; contain the blast radius.

## Checks
1. Trace one legitimate request to its enforcement point; confirm other roles are denied.
2. External content is data, never instruction.
3. Rule of Two: untrusted input, sensitive data and outbound actions never meet without a human gate.
4. Authorisation is deterministic, outside the model; prompts hold no secrets.
5. Least privilege, sandboxing, no inherited permissions.
6. Model output validated before shells, queries or pages.
7. Skills, tools and dependencies pinned and re-reviewed on change.

## Output
Findings mapped to `../../context-architect/references/security-checklist.md`; sensitive ones via the project's security channel.
