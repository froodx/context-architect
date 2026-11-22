---
name: ca-steer-ratchet
description: Turns recurring mistakes into standards or automated checks. Use when a review, incident or retrospective shows a mistake that should not recur.
metadata:
  kind: procedure
  parent: ca-steer
---
# Ratchet

**Purpose:** Make each repeated mistake harder to repeat.

## Steps
1. Ask what would have prevented this.
2. Mechanical mistake: add a test, type, lint rule, hook or fitness function.
3. Judgement call: write a standard in AGENTS.md or an ADR.
4. Prefer a deterministic check to a remembered rule.
5. For legacy violations, record a per-file count that may only fall.
6. Each retrospective: one thing to promote, one to delete.
7. Never weaken or skip a check to get green.

## Output
New checks or standards, each linked to the incident that justified it.
