---
name: ca-swarm-boundaries
description: Sets what each agent may read, write, run or send, and how it is enforced. Use when configuring agent permissions or workspaces.
metadata:
  kind: checklist
  parent: ca-swarm
---
# Boundaries

**Purpose:** Keep failure local and recovery possible.

## Checks
1. One worktree and branch per implementer.
2. Write access scoped to the ticket's files or module.
3. Workers never deploy or touch live systems.
4. Each agent gets only the access its role needs.
5. Split the lethal trifecta across agents; a human presses send.
6. Enforce with permissions, hooks and CI, not instructions.
7. Credentials live outside every context file.
8. Reading memory and changing it are separate rights.

## Output
A permissions table per role, with how each limit is enforced.
