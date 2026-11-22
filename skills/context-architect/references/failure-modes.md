# Failure modes

| Failure | What you notice | Likely cause | Fix |
|---|---|---|---|
| The kitchen sink | Important rules ignored late in long sessions | An overloaded window | Retrieve narrowly; compact; start fresh |
| The stale fact | Last year's figure used with total confidence | A perishable fact stored as persistent, undated | Date facts; set expiry; lint regularly |
| The two dialects | One word, different meanings | No shared glossary or ontology | Define once; align code, docs and prompts |
| The prompt as lock | Private data turns up where it should not | A boundary that exists only in instructions | Permissions, scoped credentials, hooks |
| The confident summary | A sound decision gets reversed | The summary lost the reason | Keep ADRs; link summaries to sources |
| The echo chamber | Reviewers agree and the bug ships | Reviewers shared the implementer's context | Independent, evidence-based review and tests |
| The runaway loop | Changes pile up faster than anyone understands | No brakes, budgets or gates | Stop conditions, budgets, human review at one-way doors |
| Silent promotion | The agent "knows" a preference you never had | Inferred preference stored without approval | Propose; never promote silently |
| Governance theatre | Everything is slow and nobody reads the rules | Ceremony out of proportion to risk | Scale process to reversibility and blast radius; delete rules that do not pay |
| The tactical spiral (Daneel addition) | Each task is slightly harder than the last | Only tactical fixes, nobody tending the environment | Reserve capacity; ratchet; roadmap fitness functions |
