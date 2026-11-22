# Brief: <title>

Seven Ws brief. Keep it to one page. Supply supporting sources on demand, not all up front.

| W | Content |
|---|---|
| Who | Requester; implementer (agent or person); reviewer and approver; who must not see the result. |
| What | The outcome in one sentence; how success is tested; out of scope. |
| When | Deadline; required sequence; how current each fact must be. |
| Where | Authoritative sources; permitted environments; forbidden systems and data. |
| Why | Motivation; relevant history (link ADRs); known or suspected cause (mark which). |
| Which | Options considered; criteria for choosing; preferred option and why. |
| How, and how much | Method; budget of time, tokens and money; evidence required to call it done. |

**Permitted actions:** ...

**Non-goals:** ...

**Escalate if:** ...

## Worked example (from the guide's checkout case)

- Who: a maintainer requests; a worker agent implements; a reviewer approves.
- What: repeated requests with the same idempotency key create exactly one Order. Out of scope: changing the payment provider.
- When: before tomorrow's release, including simultaneous-retry scenarios.
- Where: the checkout service and an isolated test database; no access to live systems.
- Why: prevent duplicate charges and orders.
- Which: enforce the guarantee on the server; record rejected alternatives in an ADR.
- How: implement the agreed interface, run simultaneous-request tests, report evidence including failures; one working session.
