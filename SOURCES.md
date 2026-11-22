# Sources behind versions 2 and 3

Consulted 22 November 2026. Figures marked (vendor) are self-reported. Full analysis in `docs/research-report.md`.

## Agent Skills, entry files and memory
- Agent Skills specification: https://agentskills.io/specification (frontmatter fields, name rules, description up to 1,024 characters, references one level deep)
- Anthropic, Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (third-person descriptions, no time-sensitive content, evaluations first, test across models)
- Claude Code skills: https://code.claude.com/docs/en/skills ; memory: https://code.claude.com/docs/en/memory (CLAUDE.md under 200 lines; AGENTS.md via @import)
- OpenCode skills: https://opencode.ai/docs/skills/ (no nested skill discovery)
- AGENTS.md: https://agents.md/ (closest file wins)
- Hermes Agent memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory (USER.md 1,375 and MEMORY.md 2,200 character caps; consolidate at 80 per cent)

## Context engineering
- Anthropic, Effective context engineering for AI agents (29 Sep 2025): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Chroma, Context Rot (14 Jul 2025): https://www.trychroma.com/research/context-rot

## Architecture Decision Records
- Nygard, Documenting Architecture Decisions (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR 4.0.0: https://adr.github.io/madr
- AWS Prescriptive Guidance, ADR process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- Microsoft Azure Well-Architected, ADR: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- GOV.UK ADR framework: https://www.gov.uk/government/publications/architectural-decision-record-framework/architectural-decision-record-framework
- Zimmermann, ecADR definition of done: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
- O'Reilly Radar, coding agents and decision records (Oct 2026): https://oreilly.com/radar/coding-agents-love-decision-records/

## Code review
- Google Engineering Practices, the standard of code review: https://google.github.io/eng-practices/review/reviewer/standard.html ; small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html
- Conventional Comments: https://conventionalcomments.org/
- DORA 2025 State of AI-assisted Software Development: https://dora.dev/
- GitClear, AI code quality (vendor): https://gitclear.com/the_ai_code_quality_maintainability_gap
- GitHub, responsible use of Copilot code review: https://docs.github.com/en/copilot/responsible-use/code-review
- Anthropic Code Review (vendor): https://claude.com/resources/articles/code-review
- Notion, ESLint ratchet: https://www.notion.com/blog/how-we-evolved-our-code-notions-ratcheting-system-using-custom-eslint-rules
- Fowler, Technical Debt Quadrant: https://martinfowler.com/bliki/TechnicalDebtQuadrant.html

## Multi-agent systems and loops
- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, How we built our multi-agent research system (about 15x tokens; 90.2 per cent gain on research): https://www.anthropic.com/engineering/multi-agent-research-system
- Cognition, Multi-Agents: What's Actually Working (Apr 2026; single-threaded writes): https://cognition.com/blog/multi-agents-working
- Google Research, Towards a science of scaling agent systems (Jan 2026; 17.2x vs 4.4x error amplification; 39 to 70 per cent loss on sequential planning): https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
- MAST, Why do multi-agent LLM systems fail?: https://arxiv.org/html/2503.13657v3
- Anthropic, Effective harnesses for long-running agents: https://anthropic.com/engineering/effective-harnesses-for-long-running-agents ; Harness design: https://anthropic.com/engineering/harness-design-long-running-apps
- OpenAI, A practical guide to building agents: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Claude Code subagents: https://code.claude.com/docs/en/subagents

## Agent security
- OWASP Top 10 for LLM Applications (2026 edition): https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md
- OWASP Top 10 for Agentic Applications (2026): https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/
- Willison, The lethal trifecta: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Meta, Agents Rule of Two: https://ai.meta.com/blog/practical-ai-agent-security/
- Beurer-Kellner et al., Design patterns for securing LLM agents: https://arxiv.org/abs/2506.08837v3
- UK NCSC, Prompt injection is not SQL injection: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
- Anthropic, Claude Code sandboxing: https://www.anthropic.com/engineering/claude-code-sandboxing ; auto mode: https://www.anthropic.com/engineering/claude-code-auto-mode
- Skill marketplace studies: https://arxiv.org/html/2601.10338v1 and https://arxiv.org/html/2602.06547v1
- Invariant Labs, MCP tool poisoning: https://invariantlabs.ai/blog/mcp-security-notification

## Added in version 3 (from the Ari edition's research notes)
- Noy and McGuinness, Ontology Development 101 (competency questions): https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html
- W3C SKOS Reference, mapping properties: https://www.w3.org/TR/skos-reference/
- W3C PROV-DM (entities, activities, agents, derivation): https://www.w3.org/TR/prov-dm/
- Google Engineering Practices, what to look for in a review: https://google.github.io/eng-practices/review/reviewer/looking-for.html
- NIST SP 800-218 Secure Software Development Framework v1.1 (PW.7): https://doi.org/10.6028/NIST.SP.800-218
- W3C Understanding WCAG 2.2 SC 3.3.4, error prevention: https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html
- Fowler, Parallel Change (expand, migrate, contract): https://martinfowler.com/bliki/ParallelChange.html
- Google SRE Workbook, canarying releases: https://sre.google/workbook/canarying-releases/
- Geoff Fane, A Guide to Context Architecture (design source): https://www.froodx.net/blog/ai-adventures/guide-to-context-architecture
