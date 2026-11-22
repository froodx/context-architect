# AGENTS.md

<!-- daneel:start. Kept current by Daneel; edit outside these markers. -->
## Working here (all agents)
Setup: `pip install -r requirements-dev.txt`
Test: `python -m pytest -q`   Lint: `ruff check .`   Compose: `docker compose config -q`   (all three run in CI)

### Conventions
- Runtime is the Python standard library only; a new dependency needs a reason in the commit message.
- Every model call goes through `hearthmind/llm.py`; agents loop via `hearthmind/agents/loop.py`.
- Model output is untrusted: parse with `llm.parse_reply`, never `eval`/`exec`, never `shell=True` (ADR 0001; enforced by ruff S rules in `pyproject.toml`).
- New tools go in `hearthmind/tools.py` and are reached only through `tools.call` with an allowlist.
- A tool that runs code (commands, package installs) is shell-equivalent: off unless `config.ALLOW_SHELL`, no `shell=True`, minimal environment, timeout. No `noqa` comments in `hearthmind/` (a test fails).
- Settings live in `hearthmind/config.py`, read from the environment; use `config.NAME` at call time.
- Tests never need a live model or real data: use the `fake_llm` fixture in `tests/conftest.py`.
- Web UI: render model text with `textContent`, never `innerHTML`.
- Document new settings in `.env.example` and the README.

### Decisions in force
- 0001 Agent tools treat model output as untrusted: `docs/decisions/0001-agent-tool-safety.md`
- All decisions: `docs/decisions/index.md`. Accepted is binding; if your task conflicts, stop and say so.

### Before you finish
- [ ] Tests, lint and compose check pass locally.
- [ ] New behaviour has a test in `tests/`.
- [ ] `.env.example`, README or this block updated if a setting or convention changed.
<!-- daneel:end -->
