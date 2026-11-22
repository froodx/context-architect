# Developing the suite

For people changing Daneel's skills rather than using them. Users start with `README.md`.

## Layout

```
SKILL.md                 root router (suite entry)
MAKE_IT_SO.md            the one command, plus carry on, report, replan, stop
COMMANDS.md              bridge commands: engage, shields up, phasers on stun, drop anchor...
CHARTER.md               template: copy into the target repository and edit
AGENTS.md  CLAUDE.md     conventions; CLAUDE.md imports AGENTS.md
SOUL.md USER.md MEMORY.md
SYSTEM_PROMPT.md         master system prompt, works on its own
ONTOLOGY.md ONTOLOGY-INDEX.md
SOURCES.md CHANGELOG.md
docs/research-report.md  the full research report behind version 2
docs/EVALUATION.md       replay cases for behavioural testing
docs/AUDIT.md            the self-audit behind version 5
docs/TRIAL.md            what was tested, with costs; evidence in docs/trial-evidence/
tests/                   regression tests for the validator
skills/
  context-architect/     Daneel's entry skill (+ references/ templates)
  ca-campaign/           make it so: survey, align, proportion, plan, execute, report
  ca-orient/ ca-review/ ca-adr/ ca-steer/
  ca-swarm/ ca-context/ ca-human/ ca-evolve/
      <leaf>/SKILL.md    leaf skills, one level down
  ontology-builder/      meta-skill for building suites like this
scripts/validate_suite.py
```

Every folder in `skills/` is a real, discoverable skill. Leaf skills sit one level below their domain and load by path when the domain routes to them. This follows the finding that Claude Code, Codex and OpenCode discover skills only at `<skills-root>/<name>/SKILL.md`; OpenCode states that it does not look inside a skill for more skills.

## Install (detail)

Your project's own `AGENTS.md` and `CLAUDE.md` belong to the project and every agent that works on it. **Never overwrite them with the suite's files.** Daneel lives in a folder of his own:

1. **Prompt only:** paste `SYSTEM_PROMPT.md` into your harness's system prompt or custom instructions. Fill in `USER.md`.
2. **Into a repository (any harness):** copy this whole suite into `.daneel/` at the repository root. Then copy the folders inside `skills/` into `.claude/skills/` (Claude Code) or `.agents/skills/` (Codex, OpenCode). Copy `CHARTER.md` to the root and edit it. Leave the project's `AGENTS.md` and `CLAUDE.md` as they are; Daneel adds his short managed section to the project's `AGENTS.md` on the first run, and creates `CLAUDE.md` with `@AGENTS.md` only if it is missing.
3. **Personal (Claude Code):** copy the skill folders into `~/.claude/skills/` and the suite into `~/.daneel/`, if you want Daneel available in every repository.
4. Check after installing: ask the agent to list its skills. The eleven top-level skills should appear; leaves should not, which is intended.
5. Codex users get display metadata from `skills/context-architect/agents/openai.yaml`; other harnesses ignore it.

## Rules the validator enforces

- Every `SKILL.md` is **150 words or fewer over the whole file including frontmatter**, counting the larger of whitespace tokens and alphanumeric runs, so hyphenated names and paths cannot hide words. This is a house rule; the spec allows up to about 5,000 tokens.
- Spec frontmatter only: `name` (lowercase, digits, single hyphens, up to 64 characters, equal to the folder, no "claude" or "anthropic"), `description` (third person, contains "Use when", under 1,024 characters, no XML), plus `metadata.kind` and `metadata.parent`.
- Routers route to exactly their children; nesting is at most one level below a top-level skill; every node reaches the root; references resolve.
- House style: no em dashes, common US spellings flagged, `USER.md` and `MEMORY.md` within their caps.

```
python3 scripts/validate_suite.py . --tree
python3 scripts/validate_suite.py . --index ONTOLOGY-INDEX.md
python3 -m unittest discover -s tests
```

Optionally also run the reference validator from the Agent Skills project (`skills-ref validate`) on each folder in `skills/`.

## Extending it
Load `skills/ontology-builder/SKILL.md`: model, write, evaluate, validate, then record the change in `CHANGELOG.md`.


## Background

Version 3 merges the research-led version 2 with the strongest parts of the independent Ari edition (journey-based review, verification with explicit verdicts, recoverable rollouts, domain modelling with competency questions, hand-off briefs, board leases and integration, and its stricter word count). Version 2 kept the ideas of *A Guide to Context Architecture* and aligns the suite with current published practice: the Agent Skills specification, MADR 4, Google's review standard and Conventional Comments, Anthropic, Cognition, OpenAI and Google Research on multi-agent systems, and the OWASP 2026 lists. See `CHANGELOG.md` for what changed and `SOURCES.md` for why.

