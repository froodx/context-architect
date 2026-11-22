---
status: accepted
date: 2026-11-22
decision-makers: Daneel, under CHARTER.md section 2 (Deliver) and section 4
review-by: 2027-05-22
confidence: high
revisit-when: shell use becomes routine, or the API is exposed beyond one machine
accepted-by: CHARTER.md sections 2 and 4 (two-way door: one setting restores shell)
---

# 0001 Agent tools treat model output as untrusted

**Y-statement:** In the context of agents that read web pages and act on the results, facing prompt injection turning into code execution, we decided for parse-only JSON replies, per-agent tool allowlists, shell off by default and file writes confined to a workspace, and against a per-call container sandbox or removing the tools, to keep the agents useful and safe to run, accepting that the Coder cannot run commands unless an operator opts in.

## Context and Problem Statement
The Researcher ran `eval()` on model output, could reach `shell` and `write_file`, and its web findings were passed to the Coder, whose `shell` tool used `shell=True`. Any fetched page could run commands on the host (Rule of Two broken: untrusted input, private data, outbound action).

## Considered Options
- Do nothing.
- Parse-only replies, allowlists, shell opt-in without `shell=True`, writes in a workspace (chosen).
- Run every tool call in a throwaway container: stronger, but new infrastructure with no current need.

## Decision Outcome
Chosen: option 2. Replies go through `llm.parse_reply` (JSON object or nothing). `tools.call` enforces each agent's allowlist: Researcher `fetch`; Writer none; Coder `write_file` (inside the workspace, symlinks resolved), plus `shell` only when `HEARTHMIND_ALLOW_SHELL=1`, run with `shlex.split` rather than `shell=True`, a 30 s timeout, the workspace as working directory and a minimal environment (secrets are not passed on, though a command can still read the API process environment through `/proc`). `fetch` accepts `http(s)` only. Any later tool that runs code counts as shell and follows the same rules (clarified 2026-11-22: the Coder's `pip` tool).

### Consequences
- Good: injection cannot reach the host shell by default; tests prove each rule.
- Bad: with shell enabled, the model can still start an interpreter (`sh -c`, `python3 -c`) and reach any path the API user can, inside its container; enabling shell means trusting everything the agents read. `fetch` can reach internal addresses (no SSRF filter).

### Confirmation
`tests/test_tools.py`, `tests/test_agents.py`, `tests/test_server.py`; ruff rules S102, S307, S602, S604, S605 fail on `exec`, `eval` and shell use; `test_no_security_rule_is_silenced_in_app_code` fails on inline `noqa: S` suppressions.
