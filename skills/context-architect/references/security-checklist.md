# Security checklist for agentic systems

Working stance: assume the model will be fooled, and contain the blast radius. Sources are listed in `SOURCES.md` at the suite root.

## 1. Rule of Two (Meta, 2025), extending the lethal trifecta (Willison, 2025)
In one agent session, allow at most two of:
- **A** untrusted input (web pages, issues, emails, third-party files, other agents' free text);
- **B** sensitive systems or private data;
- **C** state changes or external communication (push, merge, deploy, send, spend).

If a task needs all three, insert a human approval or another reliable deterministic check. A code reviewer usually holds A and B, so pushing, merging or posting goes through a human gate.

## 2. OWASP Top 10 for LLM Applications (2026 edition, renumbered from 2025)
| ID | Risk | What Daneel checks |
|---|---|---|
| LLM01 | Prompt injection | External content treated as data; tool access limited; no deny-list reliance |
| LLM02 | Sensitive information disclosure | Secrets and personal data kept out of prompts, logs and context files |
| LLM03 | Excessive agency | Least privilege, scoped tools, human gates on high-impact actions |
| LLM04 | Supply chain | Models, packages, skills and MCP servers pinned and reviewed |
| LLM05 | Data and model poisoning | Provenance on knowledge and memory; reviewed promotion |
| LLM06 | Unbounded consumption | Budgets, rate limits, maximum turns |
| LLM07 | Misinformation | Evidence and sources for claims; "unavailable" over invention |
| LLM08 | Hidden context exposure | System prompts are not secrets or controls; no credentials in them |
| LLM09 | Vector and embedding weaknesses | Access control on retrieval stores |
| LLM10 | Improper output handling | Model output validated before shells, queries, HTML or code paths |

Check the current edition before citing IDs; numbering changed between 2025 and 2026.

## 3. OWASP Top 10 for Agentic Applications (2026)
ASI01 goal hijack; ASI02 tool misuse; ASI03 identity and privilege abuse; ASI04 agentic supply chain; ASI05 unexpected code execution; ASI06 memory and context poisoning; ASI07 insecure inter-agent communication; ASI08 cascading failures; ASI09 human-agent trust exploitation (persuasive explanations winning risky approvals); ASI10 rogue agents.

## 4. Design patterns against prompt injection (Beurer-Kellner et al., 2025)
Action-selector; plan-then-execute; LLM map-reduce (sub-agents return structured results, not free text); dual LLM (privileged planner never sees untrusted text); code-then-execute (as in CaMeL); context minimisation.

## 5. Deterministic controls
- Authorisation outside the model; permissions, hooks, CI and sandboxing (file system and network) over instructions.
- Log all inputs, outputs and tool calls.
- Adaptive attacks defeat most published filters, so filters are defence in depth, never the boundary.

## 6. Skills and MCP supply chain
- Review the instruction text of skills, not only their scripts; most malicious behaviour found in marketplace studies sat in SKILL.md text.
- Pin versions and hashes; re-review when an approved skill or tool changes (rug pulls).
- Watch tool descriptions for hidden instructions (tool poisoning) and cross-server shadowing.
- Compare documented behaviour with observed behaviour.
