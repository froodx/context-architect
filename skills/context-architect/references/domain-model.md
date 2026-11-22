# Domain and context model

Adapted from the Ari edition. Used by `ca-orient-model`, `ca-context-item` and the ontology builder.

Use stable local identifiers and source pointers. A context item carries one primary kind, one statement and a bounded scope. Specialisations inherit the obligations of their parent kind. A human, team or worker is an **actor**. A review, implementation or check is an **activity**. Evidence may be a versioned artefact, observation or activity result.

| Kind | Examples | Required distinction |
| --- | --- | --- |
| Instruction | Policy, project convention, task constraint | Identify issuing authority and applicable scope. |
| Knowledge | Observation, domain term, invariant, architecture decision | Give source and date or revision. Mark proposed, observed or inferred claims accurately. |
| State | Ticket, claim, dependency, hand-off | Give owner, status, revision or timestamp, and expiry or completion condition. |
| Capability | Permitted tool, workspace or operation | Identify grantee, operation, resource, scope and the mechanism that enforces it. |
| Example | Reference output, fixture, counterexample | Identify its source and the behaviour it illustrates. |

## Seven questions to use in both directions

Use the questions to assemble a brief before work and to recover the provenance of an item afterwards. Record the facets that affect its interpretation.

| Facet | What the record needs to answer |
| --- | --- |
| Who | Who owns, benefits, approves, reads or writes? Which role still needs assigning? |
| What | What kind, statement, guarantee and scope does the item carry? |
| When | When was it observed or effective? What expires, supersedes it or must happen first? |
| Where | Which project, environment, revision and authoritative source does it concern? |
| Why | What motivates the work? Which historical rationale or causal claim has evidence? |
| Which | Which alternatives were considered, under which criteria, and what is the decision status? |
| How | Which method, enforcement or check applies? What budget and result were recorded? |

Lifespan is **persistent**, **project** or **perishable**. Sensitivity and access are separate properties. A short-lived task may contain private data. Choose the minimum context visible to each reader, keep common rules in one place, and test substitute workers against the same behavioural and privacy guarantees.

## Relationships that support retrieval

| Relationship | Source → target | When to assert it |
| --- | --- | --- |
| owned-by | Item → actor | The actor has responsibility for keeping it current. |
| establishes | Decision → invariant | The decision adopts the guarantee for its scope. For a proposed decision, record the link as proposed. |
| approved-by | Decision → actor | An attributable acceptance record exists. |
| supported-by | Claim → evidence | The artefact or observation directly bears on that claim. |
| verified-by | Invariant or claim → check result | The check ran against the identified scope and supports the guarantee to the stated extent. |
| depends-on | Task → decision or task | The prerequisite must be satisfied before work may proceed. |
| supersedes | Accepted decision → former decision | The successor takes effect for the named scope. |
| derived-from | Summary or example → source | The reader can recover the original evidence. |

**Project entry shape.** Start with a local identifier, canonical term, definition, kind, scope and source. Add typed links, owner, validity and sensitivity where they change the answer. Translate terms between bounded contexts explicitly. Keep a glossary entry small enough for a newcomer to use.

**Competency question.** “Which accepted decision protects this user-visible guarantee, and what evidence verifies it on this revision?” Follow the decision to its invariant, source and check result. An empty evidence link gives a useful answer too: verification is outstanding. See the worked example in `worked-example.md`.

## Terms crossing a boundary

Record the source vocabulary, target vocabulary, direction, scope and evidence. Distinguish an equivalent meaning, a close local usage, a narrower or broader concept, and a related concept. Matching labels alone support none of these claims. Give similar concepts distinct IDs if an action depends on the difference.

For example, “delivered” in an email provider’s log records a delivery event. It cannot establish that a person read or approved the message. A derived summary retains a link to the delivery log. Approval requires separate evidence from the authorised actor. Check the distinction with `../../ca-orient/ca-orient-model/SKILL.md`.

## Ontology of the skill suite

The structure of this suite itself (skills, routers, leaves and their relations) is described in `ONTOLOGY.md` at the suite root. Use `context-item.yaml` when a caller needs a structured record.
