# ONTOLOGY.md

The structure of this suite, written down so people and agents share one map. The project-domain model that Daneel builds for other codebases (typed relations, boundary mappings, competency questions) is in `skills/context-architect/references/domain-model.md`. The generated list of every node is in `ONTOLOGY-INDEX.md`.

## 1. Classes

| Class | Is a kind of | Meaning | Obligations |
|---|---|---|---|
| Skill node | context item (instruction) | One `SKILL.md`, 150 words or fewer | name, description, kind, parent, Purpose, Output |
| Top-level skill | skill node | Lives at `skills/<name>/SKILL.md`; discoverable by harnesses | Description that triggers well |
| Leaf skill | skill node | Lives one level down, `skills/<domain>/<leaf>/SKILL.md`; loaded by path from its parent | Routed from exactly one parent |
| Router | skill node | Chooses between children; holds no long procedure | `## Routes` listing exactly its child folders |
| Procedure | skill node | Ordered steps that produce an output | Numbered steps; a named output |
| Checklist | skill node | Checks applied to existing work | Numbered checks; a named output |
| Reference | context item (example) | Template or table loaded on demand | Named by at least one node; no word cap |
| Root file | context item | AGENTS, SOUL, USER, MEMORY, SYSTEM_PROMPT | See AGENTS.md file map |

Obligations flow downwards: every skill node inherits the skill node obligations; routers and leaves add their own.

## 2. Node schema

```yaml
---
name: ca-review-triage          # equals folder name; unique
description: Does X. Use when Y.  # third person; trigger words early; no ': ' or '#'
metadata:
  kind: checklist               # router | procedure | checklist
  parent: ca-review             # parent node name; 'none' for the root
---
# Title
**Purpose:** one sentence.
## Steps | Checks | Routes
## Output
```

## 3. Relations

| Relation | Expressed as | Checked by script |
|---|---|---|
| child of | `metadata.parent` (and folder nesting for leaves) | yes, must agree |
| routes to | backticked `child/SKILL.md` in a router | yes, must equal child folders |
| uses | backticked relative path to another node or reference | yes, must resolve |
| applies to | prose (for example ca-human applies to every route) | no |

## 4. Domains (Daneel)

| Domain | Answers | Main W |
|---|---|---|
| ca-campaign | How do we sort out this whole codebase, proportionately, with little supervision, and keep it from drifting back? | All seven |
| ca-orient | What is wanted, by whom, why, and what do our terms mean? | Who, What, Why |
| ca-review | Is this change correct, safe, humane and good for the long term? | How |
| ca-adr | Why is it like this, and what did we reject? | Why, Which |
| ca-steer | What should happen next, in what order, and how do we roll it out safely? | When, Which |
| ca-swarm | Who does the work, with what limits? | Who, Where |
| ca-context | What should each agent know, and what does the next worker need? | Where, When |
| ca-human | Is this understandable, gated and safe? | Who |
| ca-evolve | Is the codebase getting healthier? | How, When |

## 5. Design rules
- One node, one job, one trigger.
- Specialise concepts; compose instructions.
- Long material lives in references, loaded on demand.
- Layout: root router, then top-level skills in `skills/`, then leaves one level down. Never deeper: harnesses discover only top-level skills and the spec keeps references one level deep.
- Prefer breadth of three to seven children per router.
- Only the six spec frontmatter keys: name, description, license, compatibility, metadata, allowed-tools.
