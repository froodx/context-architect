---
name: ca-swarm-blackboard
description: Defines shared task state, claims and acceptance for several agents. Use when agents coordinate through a board, queue, table or progress file.
metadata:
  kind: procedure
  parent: ca-swarm
---
# Board and integration

**Purpose:** Shared state any agent can judge, with one integrator.

## Steps
1. Entries are context items: id, owner, revision, expiry, evidence, status.
2. Claim atomically, with a lease; otherwise one dispatcher serialises writes.
3. Ready, Active, Review, Accepted or Blocked.
4. Workers store results and return references; they edit only their own fields.
5. Expired lease: reconcile side effects before reassigning.
6. An independent verifier checks; the integrator accepts only on the combined revision.
7. Work acceptance, check results and ADR approval are separate facts.

## Output
A board protocol, set before work starts.
