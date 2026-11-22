# Glossary: <bounded context>

One meaning per term within this bounded context. Start with ten terms; add only when confusion costs something.

| Term | Meaning here | Kind | Aliases to retire | Source / owner | Updated |
|---|---|---|---|---|---|
| Order | A confirmed purchase created from exactly one checkout attempt. | Knowledge: concept | purchase, sale | payments team | 2026-11-22 |
| Checkout attempt | One customer intent to pay, identified by an idempotency key. | Knowledge: concept | - | payments team | 2026-11-22 |

## Translations at boundaries

| This context | Other context | Their term | Rule |
|---|---|---|---|
| Checkout | Customer email | "pending charge" | Map to Order with status Unpaid. |

## Suite vocabulary (Daneel's own terms)

| Term | Meaning |
|---|---|
| One-way door | A change that is hard or costly to reverse. Needs a human gate. |
| Two-way door | A change that is easy to reverse. |
| Blast radius | How much a mistake can damage before someone notices. |
| Deep module | Much functionality behind a small, simple interface. |
| Bounded context | A part of the system where one vocabulary holds. |
| Invariant | A rule that must always hold, such as one checkout attempt creating at most one order. |
| Ratchet | Turning a recurring review comment into a written standard or automated check. |
| Context item | Any unit of context: instruction, knowledge, state, capability or example. |
| Lifespan | Persistent, project or perishable. |
| Lethal trifecta | Private data plus untrusted content plus outbound communication in one agent. |
| Smart zone | The early part of a context window where the model reasons best. |
| Fitness function | An automated check for an architectural property. |
