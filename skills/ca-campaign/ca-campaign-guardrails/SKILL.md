---
name: ca-campaign-guardrails
description: Keeps the project's AGENTS.md conventions and cheap automated checks current, so every agent follows them. Use when a milestone ends, an ADR is accepted or a finding recurs.
metadata:
  kind: procedure
  parent: ca-campaign
---
# Guardrails
**Purpose:** Conventions that outlast Daneel's session.
## Steps
1. Edit the project's `AGENTS.md` only between its `daneel:start` and `daneel:end` markers. Never touch other text.
2. Fill it per `../../context-architect/references/agents-block.md`, under 40 lines.
3. No `CLAUDE.md`? Create it with `@AGENTS.md`. One without that line? Add it.
4. A finding seen twice becomes a check: a test, lint rule or CI step, not a note.
5. Checks stay fast, removable and in CI where it exists.
6. Record the revision in `docs/daneel/STATE.md`.
## Output
Updated block, any new checks, one progress line.
