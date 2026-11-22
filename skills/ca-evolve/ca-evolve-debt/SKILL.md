---
name: ca-evolve-debt
description: Keeps a register of technical debt and its repayment. Use when debt is taken on, discovered or competing for capacity.
metadata:
  kind: procedure
  parent: ca-evolve
---
# Debt register

**Purpose:** Make debt visible, deliberate and repaid.

## Steps
1. Record what and where.
2. Classify: deliberate or inadvertent, prudent or reckless.
3. Estimate interest (cost per change) and principal (fix effort).
4. Name a repayment trigger and an owner.
5. Prioritise by interest times how often the area changes.
6. Repay from the roadmap's reserved capacity.
7. Link ADRs; close entries with evidence.

## Output
An updated `docs/debt.md` entry using these fields.
