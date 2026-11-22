---
name: ontology-builder
description: Routes the modelling, writing, evaluation and validation of small-skill suites. Use when creating, extending or checking a suite of SKILL.md files of 150 words or fewer.
metadata:
  kind: router
  parent: daneel-suite
---
# Ontology builder

**Purpose:** Turn source material into a navigable tree of small, typed skills.

## Steps
1. Model, write, evaluate, validate.
2. Extend existing suites through the same steps.
3. Long detail goes in references, never in nodes.

## Routes
- `ontology-model/SKILL.md`: design the tree.
- `ontology-write/SKILL.md`: write a node.
- `ontology-evaluate/SKILL.md`: test it on real tasks.
- `ontology-validate/SKILL.md`: check the structure.
- `ontology-extend/SKILL.md`: add, split, merge or retire.

## Output
A suite that passes `../../scripts/validate_suite.py` and its evaluations.
