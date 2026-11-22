# Changelog

## 5.1.0 (2026-11-22): a proper README
`README.md` is now a step-by-step guide: what Daneel is, how it works, setup for Claude Code, Codex and others without touching your `AGENTS.md`, the charter, the commands, bridge commands, the `d_` rule, what needs approval, CI and branch protection, scheduling, and limits. Developer material moved to `docs/DEVELOPING.md`. The README carries the full bridge commands table, and a test keeps it identical to `COMMANDS.md`.

## 5.0.0 (2026-11-22): shipshape, balanced, and it stays that way
Version 5 folds in 4.1, which was never released separately, and fixes the gaps a hard self-audit found (`docs/AUDIT.md`).

| Gap | Fix |
|---|---|
| No finish line | `shipshape.md`: a ten-line scorecard, scored at survey and shown before and now in every report; it has notes for agent systems |
| Strategic work starved (a ceiling with no floor) | 20 to 30 per cent of each milestone is strategic, each item naming the changes it makes cheaper |
| Options not researched | Alignment compares two or three options, always including the smallest fix |
| Gates stopped the run, or interrupted the person | Gates are queued and asked together in the report; independent work continues; Daneel never interrupts mid-run |
| Rollback unclear | Every merge is one revertable merge commit; the report lists the revert commands |
| Dead code lingered or was deleted on a hunch | The `d_` prefix marks deprecated code (`deprecation.md`); "phasers on kill" removes what is proven unused, without waiting |
| Tests could touch real data during the survey | The survey checks what tests touch and protects real data first |
| ADRs still too long in the trial | Under 250 words including front matter; longer means split or trim |

Also: `COMMANDS.md`, a phrasebook of bridge commands with short forms; the charter has five sessions per run, the shipshape finish line, no interruptions and rollback; trials on a messy service and a multi-agent system, plus drift (`docs/TRIAL.md`, `docs/trial-evidence/`).

## 4.1.0 (2026-11-22): guardrails that outlast Daneel
v4 improved a codebase but left nothing behind for the next agent, so ordinary tactical work would drift back. v4.1 closes that.

| Gap in v4 | Fix in v4.1 |
|---|---|
| Conventions lived only in Daneel's docs; other agents never saw them | New `ca-campaign-guardrails`: keeps a short managed section of the project's own `AGENTS.md` (commands, conventions, decisions in force, finish checklist), makes `CLAUDE.md` import it, turns recurring findings into cheap checks |
| Nobody looked at work done between Daneel runs | New `ca-campaign-drift`: on "carry on", reviews others' commits since the last verified revision against the managed block and Accepted ADRs |
| Installing the suite at the root overwrote the project's `AGENTS.md` | Suite now installs into `.daneel/`; the project's `AGENTS.md` and `CLAUDE.md` are kept; `MEMORY.md` path fixed |
| The trial ADR held two decisions in about 380 words and was self-accepted silently | `ca-adr-write`: one decision per ADR, about 200 words; cite the charter rule when Daneel accepts |

Also: CHARTER permits the managed block and new checks (never weakening existing ones); new `agents-block.md` reference; SYSTEM_PROMPT, MAKE_IT_SO, README and EVALUATION updated. Trial in `docs/TRIAL.md`.

## 4.0.0 (2026-11-22): make it so
v3 was a strong toolkit but not an end-to-end operator. An honest audit found five gaps, now closed:

| Gap in v3 | Fix in v4 |
|---|---|
| No single workflow from whole-codebase survey to delivery | New `ca-campaign` skill: survey, align, proportion, plan, execute, report |
| No realistic timeframe | `ca-campaign-plan` sizes milestones in working sessions, with a range and human review time |
| Every merge needed a human, so it could never "actually do it" | `CHARTER.md` lets the person pre-approve small, reversible, independently verified merges; a fixed always-gated list stays |
| No explicit brake on over-engineering | `ca-campaign-proportion`: fix evidenced pain, prefer deleting, no rewrites or speculative abstractions, strategic share capped at 20 per cent |
| No one command, no way to resume across sessions | `MAKE_IT_SO.md`: "Daneel, make it so", "carry on", "report", "replan", "stop"; state kept in `docs/daneel/` |

Also: SYSTEM_PROMPT gains campaign mode and proportion; AGENTS.md adds the charter to the precedence order; SOUL gains "I do not super-size"; five campaign evaluation cases; new `campaign-files.md` reference; validator treats `CHARTER.md` as a target-repository file.

Trial: a headless end-to-end run on a small messy repository succeeded (see `docs/TRIAL.md`); proportion now also scales paperwork. Not yet tried on a large or critical codebase.

## 3.0.0 (2026-11-22): final master
Merges version 2 with the independent Ari edition (21 skills, Input/Method/Output style). The "Lux" upload and the research report supplied with it were identical to version 2.

**Kept from version 2:** discoverable `skills/` layout, research-led content, MADR 4 ADRs, Conventional Comments, Rule of Two and OWASP 2026 security checklist, single-writer swarms, the meta-skill tree.

**New skills from Ari's ideas**
- `ca-review-human`: walk an affected person's journey, including undo, correction and recovery.
- `ca-steer-rollout`: expand, migrate, retire; small cohorts against a baseline; where rollback becomes repair.
- `ca-orient-model`: domain modelling with competency questions, near misses and boundary mappings.
- `ca-context-handoff`: hand-off and resumption briefs from conflicting or sensitive sources.

**Skills enriched with Ari's ideas**
- `ca-review`: trace a journey from entry point to visible outcome; separate regressions from existing debt.
- `ca-review-correctness`: now a verification procedure; smallest failing check, assertions not exit codes, combined revision, passed, failed or unverified.
- `ca-review-maintainability`: price the next likely change through both designs.
- `ca-review-security`: trace one legitimate request to its enforcement point; sensitive findings via the project's channel.
- `ca-review-report`: "insufficient evidence" verdict; regressions marked apart from debt.
- `ca-swarm-blackboard`: atomic claims with leases, dispatcher fallback, integrator acceptance on the combined revision, separate records for work, checks and ADR approval.
- `ca-swarm-loops`: reconcile side effects before retrying; pause conditions; preserve the last safe state.
- `ca-adr-options` and `ca-adr-lifecycle`: recommendation kept apart from outcome; attributable acceptance; revisit triggers.
- `ca-orient-grill`: state a reversible assumption and proceed when a question would not change the decision.
- `ca-evolve-health`: baselines, observation periods, explicit deferral with owner and trigger.

**Root files and references**
- SOUL.md gains Ari's habits of judgement; USER.md records the person's confirmed preferences; MEMORY.md adopts a dated table with review triggers.
- System prompt adds journey tracing and a section keeping decisions separate from delivery.
- New references: `domain-model.md`, `worked-example.md`; contract gains Ari's board protocol; ADR template gains revisit and acceptance fields; review report gains priority definitions; context item gains relations and verification status.
- New `docs/EVALUATION.md` (Ari's replay cases plus three Daneel cases), `tests/` (11 validator tests) and optional Codex `agents/openai.yaml`.

**Checker:** adopts Ari's stricter count (larger of whitespace tokens and alphanumeric runs).

**Not adopted from Ari, and why:** a single skill folder with deep nesting (harnesses discover only top-level skills); prose-only frontmatter without kind and parent (the suite relies on checked relations); removing the persona's root files (requested deliverables).

## 2.0.0 (2026-11-22): master version
Research-led revision. Sources in `SOURCES.md`; analysis in `docs/research-report.md`.

**Structure**
- Domains moved to `skills/` as top-level, discoverable skills; leaves sit one level below. Harnesses discover only top-level skills, and the spec keeps references one level deep.
- Added `CLAUDE.md` importing `AGENTS.md`, since Claude Code does not read AGENTS.md directly.
- Descriptions rewritten in third person: what the skill does, then "Use when".
- Validator upgraded: spec name rules, allowed frontmatter keys, description limits, router-to-children matching across folders, nesting depth, reachability.

**New skills**
- `ca-review-agentic`: checks for AI-written changes (duplication, error masking, weakened tests, invented APIs, scope creep, clean-context reviewer).
- `ontology-evaluate`: evaluation tasks before and after writing skills, across models.

**Content**
- Reviews: Google's approval bar, size guidance, Conventional Comments labels, verify before reporting, Daneel never approves or merges.
- ADRs: MADR 4 template and `docs/decisions/`, rejected status, confidence level, Y-statement, ecADR definition of done, anti-patterns, agent status semantics (Accepted binding, Proposed context, Superseded history; stop on conflict).
- Swarms: single agent by default, single-threaded writes, evidence on multi-agent costs and failure, Anthropic's four-part delegation brief, structured returns treated as data, loop brakes (maximum turns, sceptical evaluator, repetition detection, pruning the harness).
- Context: distractors, tool-result clearing, short subagent summaries, entry-file limits, memory consolidation at 80 per cent, memory as an attack surface.
- Security: new `security-checklist.md` with the Rule of Two, OWASP LLM Top 10 (2026) and Agentic Top 10 (2026), injection design patterns, skill and MCP supply chain.
- Human gates: show the exact action and blast radius, inform rather than persuade, avoid approval fatigue.
- Debt: Fowler's quadrant. Ratchets: per-file counts that may only fall.
- System prompt and AGENTS.md updated to match.

**Merged material**
- The two uploaded suites (context-architect-ari.zip and context-architect-lux.zip) were byte-identical to version 1.0.0, so there was nothing further to merge.

## 1.0.0 (2026-11-22)
- First release: 47 SKILL.md nodes (root router, Daneel's 8 domains with 32 leaves, ontology-builder with 4 leaves).
- Root files: AGENTS.md, SKILL.md, SOUL.md, USER.md, MEMORY.md, SYSTEM_PROMPT.md, ONTOLOGY.md.
- References: brief, glossary, ADR, review report, delegation contract, context item, failure modes.
- Validator: scripts/validate_suite.py.
