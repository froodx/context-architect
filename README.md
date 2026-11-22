# Daneel: your Context Architect (version 5.1)

Daneel is an AI agent persona that takes charge of a codebase and gets it **shipshape and Bristol fashion**. It reviews the whole thing, researches the options, writes a sensible plan with a realistic timeframe, and then actually does the work. It does this in small, checked steps that you can undo, without gold-plating and without interrupting you. It leaves rules and checks behind so that other agents keep it that way.

The name honours Isaac Asimov's R. Daneel Olivaw, the robot who quietly kept a galactic empire on course for twenty thousand years. Unlike the original, this Daneel steers only in the open.

**Background reading:** Daneel is built on the ideas in [A Guide to Context Architecture](https://www.froodx.net/blog/ai-adventures/guide-to-context-architecture) by Geoff Fane. It covers why context, not just code, decides whether agents help or make a mess, and the design pillars Daneel applies to both. Read it first if you want to know why Daneel works the way it does.

It runs as a set of small skills (`SKILL.md` files of 150 words or fewer) for Claude Code, Codex, OpenCode and other agents that read Agent Skills. There's also a stand-alone system prompt for anything else.

---

## How it works, in one minute

1. **You say "Daneel, make it so."**
2. **Survey.** Daneel maps the codebase, runs the tests and scores it against a ten-line **shipshape scorecard**: it runs, tests can be trusted, checks run on every change, it's safe, dependencies are sound, hotspots can be changed safely, there's one way to do things, it's efficient enough, it's explained, and it's guarded for every agent.
3. **Research.** For each real problem, Daneel compares two or three options from official sources, always including the smallest fix.
4. **Plan.** It cuts anything that's overkill and plans milestones with a time range. About **three-quarters** of the effort fixes what hurts now. About **a quarter** goes on structure that makes future changes cheaper, and each structural item has to say which changes it makes cheaper.
5. **Deliver.** Daneel works through the plan one small ticket at a time. Each ticket is tested, checked by an independent reviewer, and merged as **one commit you can undo** with a single command.
6. **Guard.** It keeps a short section of your project's own `AGENTS.md` up to date: test commands, house rules, decisions in force, and a "before you finish" checklist. Every agent reads it, not just Daneel. Mistakes that keep happening become automatic checks.
7. **Report.** It writes a one-page report with the scorecard before and now, what changed, what it deliberately didn't do, and **all its questions for you in one place**, each with a recommendation. It never stops mid-run to ask.
8. **Later, you say "Daneel, carry on."** It first checks what anyone else changed since its last run (**drift**), fixes or tickets what it finds, then carries on with the plan.

Everything Daneel knows about the campaign lives in your repository (`docs/daneel/` and `docs/decisions/`), so any fresh session can pick up where the last one stopped.

---

## Setting up (about 15 minutes)

### 1. Unzip into your repository

Unzip so the suite sits in a folder called `.daneel/` at the root of your repository:

```bash
cd your-repo
unzip v5.1-master-daneel.zip
mv v5.1-master-daneel .daneel
```

**Leave your project's own `AGENTS.md` and `CLAUDE.md` exactly as they are.** The `AGENTS.md` inside `.daneel/` is Daneel's own; it never replaces yours.

### 2. Put the skills where your agent looks

| Agent | Command |
|---|---|
| Claude Code | `mkdir -p .claude/skills && cp -r .daneel/skills/* .claude/skills/` |
| Codex, OpenCode | `mkdir -p .agents/skills && cp -r .daneel/skills/* .agents/skills/` |
| Claude Code, every repository | `mkdir -p ~/.claude/skills && cp -r .daneel/skills/* ~/.claude/skills/` |
| Anything else | Paste `.daneel/SYSTEM_PROMPT.md` into the agent's system prompt or custom instructions |

To check, ask your agent to list its skills. You should see eleven, including `context-architect` and `ca-campaign`. The smaller leaf skills inside them are loaded only when needed, which is intended.

### 3. Tell Daneel about you (optional, two minutes)

Fill in `.daneel/USER.md`: your name, role and how you like to be spoken to. It's private, so keep it out of git:

```bash
echo ".daneel/USER.md" >> .gitignore
```

Whether to commit the rest of `.daneel/` and the skills is up to you. Commit them if teammates will run Daneel too.

### 4. Write the charter (five minutes)

```bash
cp .daneel/CHARTER.md CHARTER.md
```

Edit the lines marked **edit**. The ones that matter:
- **The goal:** "shipshape" is a good default.
- **Out of bounds:** anything Daneel must never touch.
- **Decision owner:** you.

Everything else has sensible defaults:
- **Deliver level:** Daneel may merge small, reversible, checked changes.
- **Budget:** 5 working sessions per run.
- **Effort:** 20 to 30% on structure.

The charter is your standing instruction, and Daneel never edits it.

### 5. Make sure the tests can run

Daneel needs to be able to run your tests where the agent runs. If they need Docker, a database or secrets, make those available, or say in the charter what to skip.

### 6. Go

Open your agent in the repository and paste the full command from `MAKE_IT_SO.md`:

> **Daneel, make it so.** Take charge of this repository under CHARTER.md. Survey it, check it against current best practice, and write a simple, doable plan with a realistic timeframe. Then deliver it in small, verified steps until it is shipshape, recording ADRs only for decisions that matter. Keep it proportionate: fix what hurts, put about a quarter of the effort into structure that makes future changes cheaper, no gold-plating. Stop only at a gate, a blocker or the budget, and leave me a one-page report.

Then read `docs/daneel/REPORT.md` when it's done.

---

## Keeping it going

| Say | What happens |
|---|---|
| **Daneel, carry on.** | Checks drift from other agents first, then continues the plan. Use it every session, or schedule it. |
| **Daneel, report.** | A short status: scorecard, progress, anything waiting on you. No new work. |
| **Daneel, replan: ...** | Adjusts the plan, the cut line and the timeframe to what you say. |
| **Daneel, stop.** | Finishes the current step safely, saves state and stops. |

**Schedule "carry on"** so drift never sits for long. Daily or weekly is plenty.
- **Claude Code, while a session is open:** `/loop` with an interval, for example `/loop 2h Daneel, carry on.`
- **Unattended (cron or a scheduled CI job), Claude Code:**
  ```bash
  claude -p "Daneel, carry on." --permission-mode acceptEdits \
    --allowedTools "Bash Read Edit Write Glob Grep Task Skill"
  ```
- **Codex:** `codex exec "Daneel, carry on."` from cron, in the same way.

### Bridge commands

Nautical and Star Trek phrases Daneel understands. Use the full phrase or the short form; capitals and close variations don't matter. No phrase skips the checks or the budget, and Daneel never interrupts you to ask. This is the same table as `COMMANDS.md`, which is the copy Daneel reads. Paste that file into any other agent's instructions and it will understand the phrases too.

#### Setting course

| Full phrase | Short form | Daneel does |
|---|---|---|
| Make it so | Make it so | Run the full campaign: survey, research, plan with a timeframe, then deliver (`MAKE_IT_SO.md`). |
| Engage | Engage | Start delivering the plan already agreed, without re-surveying. |
| Steady as she goes | Steady | Carry on exactly as planned with no new scope. Same as "carry on". |
| Course correction: ... | Correct course: ... | Replan around what you say: scope, cut line and timeframe. Same as "replan". |
| Shipshape and Bristol fashion | Shipshape | The finish line: every line of the shipshape scorecard green, not applicable, or waiting on you. |
| Smooth voyage to Risa | Smooth voyage | Work on its own. No interruptions; save every question for the report, batched, each with a recommendation. |
| You have the helm, Mr Data | You have the helm | Full authority at the Deliver level, within the charter. Report at the end. |

#### Reporting

| Full phrase | Short form | Daneel does |
|---|---|---|
| Status report, Number One | Report | A short update now: scorecard, progress, anything waiting on you. No new work. |
| Captain's log | Log | The one-page report (`docs/daneel/REPORT.md`), with the queued decisions. |

#### Changing the mode

| Full phrase | Short form | Daneel does |
|---|---|---|
| Battle stations / Red alert | Battle stations | Drop everything except critical defects, outages, security holes and data loss. Fix those first, with the smallest safe fix. |
| Shields up | Shields up | Tighten safety: Advise level only (read, review and propose; no merges), run a security pass, and gate anything risky. |
| Batten down the hatches | Batten down | A security and secrets pass: committed secrets, unsafe tools, injection, permissions, dependencies. |
| Set phasers to stun | Stun | Minimal, reversible fixes only. No refactors. |
| Set phasers to kill | Kill | Remove dead code, unused dependencies and broken features decisively, without waiting for you. Careful about it: prove each is unused (references, imports, dynamic and entry-point use, config), keep tests green, have the independent check confirm, and make each removal one revertable commit listed in the report. Anything it can't prove unused is marked deprecated with a `d_` prefix instead, and killed on a later pass once proven. Code only: data is never touched. |
| All hands on deck | All hands | Allow parallel agents for independent work. Still one writer per area, and an independent check before merging. |

#### Stopping

| Full phrase | Short form | Daneel does |
|---|---|---|
| Hold position | Hold | Pause after the current step and keep everything as it is until you say "engage" or "carry on". |
| Drop anchor | Anchor | Finish the current step safely, save state in `docs/daneel/STATE.md`, and stop. Same as "stop". |
| All stop | All stop | Stop now: no new commands and no merges. Leave work on its branch and record where it stopped. |
| Belay that | Belay | Cancel your last instruction. If it was already done and can be undone, undo it; if not, say so. |
| Qapla' | Qapla' | Finish properly: complete the current milestone, verified and merged, with the report. No half-done work left behind. |

#### What Daneel says back

| Daneel says | Meaning |
|---|---|
| She cannae take any more, Captain | The budget is spent, or an estimate is off by more than half. Daneel stops and says what it would take to go on. |
| That course leads to Ceti Alpha V | A plan or request heads somewhere bad: irreversible, unsafe or gold-plated. Daneel says why and offers a safer course. |
| Aye, Captain | Understood, doing it. |

### Deprecated code: the `d_` prefix

Code that shouldn't be used any more, but isn't yet proven safe to delete, is renamed with a `d_` prefix (`d_legacy_export.py`, `d_send_receipt()`). It also gets a note saying what to use instead. Your `AGENTS.md` tells every agent never to add new uses. On every "carry on" and "kill", Daneel deletes the `d_` items now proven unused, without asking.

Names that outside systems call, such as public APIs, web routes or command-line flags, are never renamed, because that would break things you can't see from the code. They get a deprecation note instead. Full rules are in `.daneel/skills/context-architect/references/deprecation.md`.

---

## What Daneel does on its own, and what waits for you

**On its own, at the default Deliver level:**
- Fixes, tests, refactors, dependency clean-ups and removing dead code.
- Small structural improvements and the `AGENTS.md` section.
- New checks, and ADRs for easy-to-reverse decisions, which cite the charter rule that allowed them.

Each change is tested, independently checked and merged as one undoable commit.

**Queued in the report for you, never asked mid-run:**
- Production deploys and releases.
- Deleting *data* or running irreversible migrations.
- Permissions, secrets, CI security settings and branch protection.
- Breaking a public API.
- Spending money.
- Anything sent outside the repository.
- One-way decisions.
- Rewriting git history.

All work that isn't blocked carries on meanwhile.

**To undo anything:** the report lists each merge with its command, for example `git revert -m 1 <commit>`.

If merging to your main branch deploys to production automatically, say so in the charter. Daneel then merges into a `daneel/integration` branch instead, and you merge that once per milestone.

---

## Make the guardrails stick: turn on CI and branch protection

`AGENTS.md` is advice. Agents usually follow it, but nothing forces them to. What actually stops a bad change is **CI that runs the checks, plus branch protection that requires them to pass**. Daneel writes the CI workflow. Turning on protection changes permissions, so it's yours to do:

- **GitHub:** Settings, then Branches (or Rules, then Rulesets). Add a rule for `main`: require a pull request, and require status checks to pass, choosing the CI job Daneel added.
- **GitLab:** Settings, then Repository, then Protected branches. Also set Settings, then Merge requests, then "Pipelines must succeed".

Once that's on, the checks Daneel adds block bad changes from any agent or person, whether or not they read `AGENTS.md`.

---

## What's in the zip

| File | What it's for |
|---|---|
| `README.md` | This guide |
| `MAKE_IT_SO.md` | The command, plus carry on, report, replan and stop |
| `COMMANDS.md` | Bridge commands, with short forms |
| `CHARTER.md` | Template for your standing instructions; copy it to your repository root |
| `SYSTEM_PROMPT.md` | The whole persona as one prompt, for agents without skills |
| `SOUL.md`, `USER.md`, `MEMORY.md` | Who Daneel is, who you are, and its working notes |
| `AGENTS.md`, `CLAUDE.md`, `SKILL.md` | Daneel's own conventions and skill entry point (not your project's) |
| `skills/` | Eleven skills, with smaller leaf skills inside; `ca-campaign` is the "make it so" engine |
| `skills/context-architect/references/` | Templates: shipshape scorecard, `AGENTS.md` section, deprecation, ADR, review and more |
| `docs/TRIAL.md`, `docs/trial-evidence/` | What was tested, with costs and real reports |
| `docs/AUDIT.md` | The self-audit behind version 5 |
| `docs/DEVELOPING.md` | For changing the skills themselves: layout, validator, extending |
| `CHANGELOG.md`, `SOURCES.md` | What changed, and the research behind it |

---

## Honest limits

- **Instructions are advice; checks are enforcement.** Turn on branch protection (above), or the guardrails rely on agents being well behaved.
- **Drift is caught when Daneel runs.** Schedule "carry on".
- **Tested on small repositories.** Version 5 ran end to end on two deliberately messy ones: a shop service and a multi-agent system with a local LLM, tools, memory, docker compose and a web UI. It also checked another agent's follow-up work. It hasn't yet run on a large codebase, where it will take more sessions. Read the first plan, and start with "shields up" (advise only) if the codebase is critical.
- **Cost.** Each trial run cost about $2 to $4 on the most capable model, and larger codebases cost more. The independent checks roughly double the cost of a run, and caught real bugs every time.
- **Judgement is a model's judgement.** The scorecard, the proportion rules and the report make it visible and checkable, not infallible.
- **Review every six months.** Security guidance and agent tools move quickly; `SOURCES.md` has the dates.

---

Licence: MIT (see `LICENSE`).
