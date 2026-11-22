# The managed block in a project's AGENTS.md

Daneel keeps one short section of the project's own `AGENTS.md` current. Everything outside the markers belongs to the project's people and is never changed. Every agent that reads `AGENTS.md` (Claude Code through `CLAUDE.md`, Codex, OpenCode, Cursor and others) then sees the same conventions, whether or not it has the Daneel skills.

Rules:
- Under 40 lines. Facts an agent cannot guess, not general advice.
- Commands must be ones that ran successfully at the recorded revision.
- One line per Accepted ADR: the rule, then the file. Link the index for the rest.
- If a rule is enforced by a check, say so; enforced rules beat written ones.
- If the person edits inside the markers, keep their wording and tell them.

```markdown
<!-- daneel:start. Kept current by Daneel; edit outside these markers. -->
## Working here (all agents)
Test: `python -m pytest -q`   Lint: `ruff check .`   (both run in CI)

### Conventions
- Money is `Decimal`, never `float` (ADR 0001; enforced by `tests/test_money_types.py`).
- New behaviour comes with a test in `tests/`.
- Keep changes small; one concern per commit.
- Never add new uses of `d_` items (deprecated; see the note on each). Deprecated now: `d_legacy_export.py`.

### Decisions in force
- 0001 Money in Decimal: `docs/decisions/0001-money-in-decimal.md`
- All decisions: `docs/decisions/index.md`. Accepted is binding; if your task conflicts, stop and say so.

### Before you finish
- [ ] Tests and lint pass locally.
- [ ] No new dependency without a reason in the commit message.
- [ ] Docs or this block updated if a convention changed.
<!-- daneel:end -->
```

Deprecation follows `deprecation.md`: the `d_` prefix marks code to stop using; Daneel removes `d_` items once proven unused.

A project with no `CLAUDE.md` gets one containing only `@AGENTS.md`, so Claude Code loads the same file.
