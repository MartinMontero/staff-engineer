# Glossary

## Staff Engineer

The human in this system. Not a coder — an accountable decision-maker who
defines verifiable goals, approves plans, reviews evidence, and is the only
entity allowed to declare work complete. The role exists to enforce
accountability, not to write code.

## Stopping condition

A machine-checkable definition of done: a single command, stored in
`sprints/<id>/stopping-condition.md`, that exits 0 when the sprint's goal is
met and nonzero otherwise. If you cannot write the command, you do not yet
know what you are building.

## Task graph

A directed acyclic graph (DAG) of work nodes with explicit dependencies,
stored in `sprints/<id>/graph.yaml`. It is the contract between planning and
execution: every node is verifiable and every path terminates at the
stopping condition. A shopping list is not a recipe.

## Gate

A required checkpoint in the sprint state machine (QA1, Live QA, User
Review) that cannot be skipped. Gates convert agent claims into verified
evidence before the next state is entered. `allow_skip: false` — always.

## Evidence bundle

A signed, hashed record produced at each gate: the QA1 report, the Live QA
report (command, exit code, output), and their sha256 hashes stored in git.
Evidence bundles make "done" auditable after the fact.
