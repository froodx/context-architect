---
name: ontology-extend
description: Adds, splits, merges or retires nodes without blurring the tree. Use when changing the shape of an existing suite.
metadata:
  kind: procedure
  parent: ontology-builder
---
# Extend

**Purpose:** Grow the suite without blurring it.

## Steps
1. Search existing descriptions first; extend before adding.
2. Add: choose the parent, write the node, add its route to the parent.
3. Split a node with two triggers or no room left; its parent becomes a router.
4. Merge nodes whose triggers overlap.
5. Retire by removing the route and folder; note it in CHANGELOG.md.
6. Validate after every change.

## Output
A changed suite, a passing validation and a CHANGELOG entry.
