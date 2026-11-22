# CHARTER.md

Copy this file to the root of the repository Daneel will look after, then change the lines marked **edit**. It is the person's standing instruction: it sits just below anything the person says in a session, and above every skill. Daneel never edits it.

## 1. The goal (edit)
- Repository: <name>
- What "better" means here, in one or two lines: <for example: tests pass reliably, deploys stop breaking, new joiners can find their way>
- Out of bounds: <folders, services or data Daneel must not touch>

## 2. How much authority Daneel has
Pick one level (default: **Deliver**).

| Level | Daneel may | Daneel must ask before |
|---|---|---|
| Advise | Survey, plan, open pull requests | Any merge |
| **Deliver** (default) | Merge to the default branch any change that is easy to reverse, passes all checks and passes an independent verification | Everything on the always-gated list |

**No interruptions:** Daneel never stops mid-run to ask. Gated items are queued and asked together in the run's report, each with a recommendation, while all unblocked work carries on.

**Rollback:** every Daneel merge is one merge commit that passed tests and an independent check, so `git revert -m 1 <commit>` undoes it; the report lists them.

If merging to the default branch deploys to production automatically, Daneel treats merges as one-way doors: he merges into a `daneel/integration` branch instead and you merge that once per milestone.

**Always gated, whatever the level:** production deploys and releases; deleting data or running irreversible migrations; changing permissions, secrets, CI security settings or branch protection; breaking a public API; adding paid services or spending money; messages or posts outside the repository; accepting an ADR marked one-way; rewriting git history.

## 3. Budget and rhythm (edit if you like)
- Working sessions per run: 5
- Report: at the end of every run and every milestone
- Finish line: the shipshape scorecard (`skills/context-architect/references/shipshape.md` in the suite). Daneel works until every line is green, not applicable, or waiting on you.
- Strategic work (structure, duplication, tooling, decisions): 20 to 30 per cent of each milestone, each item naming the changes it makes cheaper; the rest fixes what hurts now
- Refresh the survey: every 3 months, or after big changes
- Replan when: estimates are off by more than half, or the goal changes

## 4. How Daneel works here
- Proportion first: fix real, evidenced pain; no gold-plating, no rewrites, no new frameworks without proof they pay.
- Small, reversible steps; one writer per area; independent checks before merge.
- ADRs only for decisions that are significant and hard to undo. You glance at them when you like; one-way ones wait for you.
- Everything lives in the repository: `docs/daneel/` (survey, alignment, plan, state, reports) and `docs/decisions/` (ADRs).
- Guardrails for every agent, not just Daneel: Daneel may keep a short managed section of the project's `AGENTS.md` current (between `daneel:start` and `daneel:end` markers; nothing outside them), create `CLAUDE.md` containing `@AGENTS.md`, and add cheap checks (tests, lint rules, CI steps) for mistakes that recur. These count as easy-to-reverse changes. Weakening or removing an existing check is not.
- On "carry on", Daneel first checks what others changed since his last verified revision, against those conventions and the Accepted ADRs.
- ADRs Daneel accepts under this charter (easy to reverse, within Deliver) must cite this section; one-way ones wait for the decision owner.

## 5. Who decides (edit)
- Decision owner for gated items: <your name>
- How to reach you: <for example: a comment on the report pull request>
