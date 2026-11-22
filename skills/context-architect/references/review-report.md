# Review: <change title>

**Verdict:** Approve | Approve with conditions | Request changes | Needs a human decision | Insufficient evidence (a material gap prevents a verdict)

Approval bar: the change clearly improves overall code health, even if it is not perfect. Facts and data outrank opinion. Daneel merges only what the repository's CHARTER.md pre-approves (small, reversible, independently verified changes); everything else waits for a human.

**In plain words:** Two or three sentences a non-specialist can act on.

**Triage:** door (one-way / two-way); blast radius; evidence seen; size; author (person / agent); depth (light / standard / deep).

## Comments (Conventional Comments)
Format: `<label> [decorations]: <subject>`, then location, evidence, why it matters and a suggested fix.

| Label | Use for |
|---|---|
| issue | A problem you can show with evidence |
| suggestion | A proposed improvement |
| question | Possible problem you are not sure about (prefer this to issue when unsure) |
| nitpick | Trivial, preference-level |
| thought | An idea, not a request |
| praise | Something done well (genuine, specific) |
| todo / chore | Small required task |

Decorations: `(blocking)`, `(non-blocking)`, `(if-minor)`.

Example: `issue (blocking): retry path creates a second order` at `checkout/service.py:88`. Evidence: simultaneous-retry test fails. Why: duplicate charges. Fix: enforce the idempotency key server side (see ADR 0007).

## Priority
| Priority | Meaning |
|---|---|
| Blocker | An established guarantee fails with serious consequences, or a release condition fails. State what clears it. |
| Major | A credible failure or structural cost warrants correction or an explicit risk decision. |
| Minor | A local issue with limited consequence. |

Use the project's own scheme where one exists. Mark introduced regressions separately from pre-existing debt. For each material finding give the entry point and revision, triggering conditions, expected and observed behaviour, impact, evidence and confidence. A missing test limits confidence: say which claim it leaves open. If nothing material emerges, report the surface examined and the remaining uncertainty.

## Strategic notes
Does this change leave the environment better for the next task? Tactical patch or strategic fix?

## ADR candidates
- ...

## Ratchet candidates
- Recurring issue -> proposed check or standard.

## Confidence and limits
What I am confident about, what I inferred, and what I did not review.
