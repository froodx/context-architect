---
name: ca-review-correctness
description: Verifies a claim, slice or integrated change with checks that could fail. Use when confirming behaviour, invariants or tests, or accepting delivered work.
metadata:
  kind: procedure
  parent: ca-review
---
# Verify the guarantee

**Purpose:** Trust results for good reasons, not hopeful ones.

## Steps
1. Choose the smallest check that would fail if the claim were false.
2. Exercise the public boundary; compare failing baseline with the change.
3. Cover old data, retries, concurrency, timeouts and partial failure.
4. Inspect assertions, not just exit status.
5. Rerun integration checks on the combined revision.
6. Nothing fabricated, skipped or disabled to get green.

## Output
Per claim: revision, check, expected, actual, verdict (passed, failed or unverified). Separate checks run from checks proposed.
