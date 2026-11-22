---
# MADR 4 front matter (all optional)
status: proposed   # proposed | rejected | accepted | deprecated | superseded by NNNN
date: YYYY-MM-DD
decision-makers: <named people>
consulted: <people or teams>
informed: <people or teams>
review-by: YYYY-MM-DD   # Daneel addition
confidence: medium      # low | medium | high (Daneel addition, after Microsoft guidance)
revisit-when: <event or threshold that warrants a new decision>
accepted-by: <attributable decision reference, once accepted>
---

# NNNN <short title of the problem and solution>

**Y-statement:** In the context of <situation>, facing <concern>, we decided for <option> and against <alternatives>, to achieve <quality>, accepting <downside>.

## Context and Problem Statement
Two or three sentences, or a question. Use the seven Ws briefly. Separate proven cause from inference.

## Decision Drivers
- <driver, for example reversibility, blast radius, cost, risk, maintainability>

## Considered Options
- Do nothing
- <option A>
- <option B>

## Decision Outcome
While Proposed: state what the decision owner is being asked to decide and the recommended option. Once Accepted: chosen option "<option>", its exact scope, and the justification against the drivers. Keep the recommendation and the recorded outcome distinct.

### Consequences
- Good, because ...
- Bad, because ... (accepted cost)

### Confirmation
How compliance will be checked: a test, fitness function, review rule or metric.

## Pros and Cons of the Options
### <option A>
- Good, because ...
- Bad, because ...

## More Information
Links to superseded or related ADRs, specs, incidents. Notes for agents working in this scope (one or two lines).

---

## Before accepting: definition of done (after Zimmermann's ecADR)
- **Evidence:** the design will work (spike, test, precedent).
- **Criteria:** at least two genuine alternatives compared against explicit drivers.
- **Agreement:** decision-makers and consulted people agree, or disagreement is recorded.
- **Documentation:** this record is complete and short.
- **Realisation and review:** implementation is planned and a review date is set.

## Anti-patterns to avoid
Fairy tale (only pros), sales pitch (marketing language), free lunch (no costs stated), dummy alternative (a straw option), tunnel vision (one context only), mega-ADR (a design document in disguise), and silently editing an accepted record instead of superseding it.
