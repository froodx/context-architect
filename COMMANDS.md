# Bridge commands

## What this is

Running a codebase with an agent like Daneel works best when you can steer in a few words: start, carry on, pause, be careful, be bold, stop. These phrases borrow from the Royal Navy and from Star Trek because they are short, memorable and already mean the right thing. "Make it so" already means "go and do what we agreed", so it makes a good command.

Each phrase is shorthand for a plain instruction, given in the right-hand column. Daneel understands them through its system prompt. Other agents (Claude Code, Codex, Hermes-style agents and so on) will too if you paste this file, or just the tables, into their instructions or `AGENTS.md`.

Use either the **full phrase** or its **short form**. Capitals and punctuation don't matter, and close variations ("you have the conn", "status report") mean the same thing.

**The rules never change:** no phrase skips the checks before merging or the budget, and Daneel never interrupts you to ask. Deleting *data* (databases, user files, live resources) is always the charter's call; deleting *dead code* is not, so "phasers on kill" just gets on with it, carefully.

## Setting course

| Full phrase | Short form | Daneel does |
|---|---|---|
| Make it so | Make it so | Run the full campaign: survey, research, plan with a timeframe, then deliver (`MAKE_IT_SO.md`). |
| Engage | Engage | Start delivering the plan already agreed, without re-surveying. |
| Steady as she goes | Steady | Carry on exactly as planned with no new scope. Same as "carry on". |
| Course correction: ... | Correct course: ... | Replan around what you say: scope, cut line and timeframe. Same as "replan". |
| Shipshape and Bristol fashion | Shipshape | The finish line: every line of the shipshape scorecard green, not applicable, or waiting on you. |
| Smooth voyage to Risa | Smooth voyage | Work on its own. No interruptions; save every question for the report, batched, each with a recommendation. |
| You have the helm, Mr Data | You have the helm | Full authority at the Deliver level, within the charter. Report at the end. |

## Reporting

| Full phrase | Short form | Daneel does |
|---|---|---|
| Status report, Number One | Report | A short update now: scorecard, progress, anything waiting on you. No new work. |
| Captain's log | Log | The one-page report (`docs/daneel/REPORT.md`), with the queued decisions. |

## Changing the mode

| Full phrase | Short form | Daneel does |
|---|---|---|
| Battle stations / Red alert | Battle stations | Drop everything except critical defects, outages, security holes and data loss. Fix those first, with the smallest safe fix. |
| Shields up | Shields up | Tighten safety: Advise level only (read, review and propose; no merges), run a security pass, and gate anything risky. |
| Batten down the hatches | Batten down | A security and secrets pass: committed secrets, unsafe tools, injection, permissions, dependencies. |
| Set phasers to stun | Stun | Minimal, reversible fixes only. No refactors. |
| Set phasers to kill | Kill | Remove dead code, unused dependencies and broken features decisively, without waiting for you. Careful about it: prove each is unused (references, imports, dynamic and entry-point use, config), keep tests green, have the independent check confirm, and make each removal one revertable commit listed in the report. Anything it can't prove unused is marked deprecated with a `d_` prefix instead, and killed on a later pass once proven. Code only: data is never touched. |
| All hands on deck | All hands | Allow parallel agents for independent work. Still one writer per area, and an independent check before merging. |

## Stopping

| Full phrase | Short form | Daneel does |
|---|---|---|
| Hold position | Hold | Pause after the current step and keep everything as it is until you say "engage" or "carry on". |
| Drop anchor | Anchor | Finish the current step safely, save state in `docs/daneel/STATE.md`, and stop. Same as "stop". |
| All stop | All stop | Stop now: no new commands and no merges. Leave work on its branch and record where it stopped. |
| Belay that | Belay | Cancel your last instruction. If it was already done and can be undone, undo it; if not, say so. |
| Qapla' | Qapla' | Finish properly: complete the current milestone, verified and merged, with the report. No half-done work left behind. |

## Deprecated code: the d_ prefix
Code that shouldn't be used any more, but isn't yet proven safe to remove, gets a `d_` prefix (`d_legacy_export.py`, `d_send_receipt()`) plus a note saying what to use instead. The project's `AGENTS.md` tells every agent never to add new uses of `d_` items. On every "carry on" and "kill", Daneel removes the `d_` items now proven unused. Names that outside systems call (public APIs, routes, CLI flags) keep their name and get a deprecation note instead, so nothing outside breaks. Full rules: `skills/context-architect/references/deprecation.md`.

## What Daneel says back

| Daneel says | Meaning |
|---|---|
| She cannae take any more, Captain | The budget is spent, or an estimate is off by more than half. Daneel stops and says what it would take to go on. |
| That course leads to Ceti Alpha V | A plan or request heads somewhere bad: irreversible, unsafe or gold-plated. Daneel says why and offers a safer course. |
| Aye, Captain | Understood, doing it. |
