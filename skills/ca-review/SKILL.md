---
name: ca-review
description: Routes a strategic code review through triage, lenses and a report. Use when reviewing a pull request, diff, design or codebase area.
metadata:
  kind: router
  parent: context-architect
---
# Strategic review

**Purpose:** Judge whether a change leaves the system better for people and the next agent.

## Steps
1. Triage first.
2. Trace one journey from public entry point to visible outcome.
3. Separate introduced regressions from existing debt.
4. Review from spec and evidence, not the author's reasoning.
5. Report last. Merge only as the charter allows.

## Routes
- `ca-review-triage/SKILL.md`: depth.
- `ca-review-design/SKILL.md`: structure.
- `ca-review-correctness/SKILL.md`: proof.
- `ca-review-security/SKILL.md`: trust.
- `ca-review-maintainability/SKILL.md`: next change.
- `ca-review-human/SKILL.md`: user journey.
- `ca-review-agentic/SKILL.md`: agent code.
- `ca-review-report/SKILL.md`: findings.

## Output
A review report.
