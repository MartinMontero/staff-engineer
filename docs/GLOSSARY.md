# Glossary

## Staff Engineer

The human in this system — you. Not a coder. An accountable
decision-maker who defines what "done" looks like, approves work plans,
reviews evidence that the work succeeded, and is the only person allowed
to declare work complete. The role exists to enforce accountability, not
to write code. The AI agents report to you; the checkpoints protect you
from them.

## Sprint

A single piece of work — one goal, from start to finish. Each sprint has
its own folder under `sprints/`, containing its stopping condition, its
work plan, its state file, and its evidence reports. A sprint moves
through a fixed sequence of stages and cannot skip any mandatory
checkpoint.

## Stopping condition

The machine-testable definition of "done." It is a single command, stored
in `sprints/<id>/stopping-condition.md`, that the system runs
automatically during the Live Test checkpoint. The command returns a
result code: zero means success (PASS), anything else means failure
(FAIL). The result code is the verdict — there is no interpretation,
no partial credit, and no judgment call.

If you cannot write the command, you do not yet know what you are
building. That is the system telling you to clarify the goal before
proceeding.

## Task graph

A structured work plan where each task is a node and the connections
between nodes show dependencies — what must be completed before the next
task can start. Stored in `sprints/<id>/graph.yaml`. The technical term
is a directed acyclic graph (DAG): "directed" because dependencies go one
way (A before B), and "acyclic" because the plan cannot contain circular
dependencies (B cannot also be required before A).

The task graph is the contract between planning and execution. Every node
must be verifiable — there must be a way to check that it worked. Every
path through the graph terminates at the stopping condition, so if the
stopping condition passes, every task in the plan has succeeded.

A shopping list is not a recipe. The task graph is the recipe.

## Gate

A mandatory checkpoint in the sprint's progression that cannot be
skipped. There are three gates: QA Audit, Live Test, and Your Review.
Each gate converts an agent's claim ("I finished the work") into verified
evidence ("here is proof that it passed a specific test") before the
sprint is allowed to move to the next stage. The setting `allow_skip:
false` is enforced mechanically — it is not a policy, it is a constraint
built into the system.

## Evidence bundle

The proof produced at each gate. It includes the QA Audit report (a
checklist of what passed and failed), the Live Test report (the exact
command that ran, its output, and its result code), and a sha256 hash for
each report — a unique fingerprint derived from the report's contents
that makes any after-the-fact tampering detectable. The evidence bundle
is stored in file history so it can be audited at any time.

## Result code (exit code)

A number that every command returns when it finishes. Zero means success.
Any other number means failure. This is a universal convention in
software — the system does not invent it, it relies on it. When the
stopping condition runs, its result code is the final verdict on whether
the sprint's goal has been achieved.

## State file

The file `sprints/<id>/state.json` that records which stage the sprint is
currently in and the full history of every stage change: who triggered it,
what the previous stage was, what the new stage is, and the exact date
and time. The state file is what makes the sprint's progression auditable.

## Guardrails

The rules that define what each agent is and is not allowed to do, stored
in `.staff-engineer/guardrails.yaml`. The guardrail scanner
(`scripts/guardrail_check.py`) checks the codebase for violations —
primarily looking for secrets accidentally written into source files. It
can run automatically on every check-in or manually at any time.

## Pipeman

The agent responsible for file history (git operations — branching,
committing, merging). Pipeman is the only agent allowed to touch file
history, and file history is all Pipeman touches. This separation exists
so that no single agent can both write code and publish it. If Pipeman
encounters a conflict it cannot resolve mechanically, it stops and
escalates — it never rewrites code to fix a merge problem.

## Master Controller

The agent that drives the sprint's progression through the state machine.
It reads the current stage, checks what transitions are allowed, invokes
the appropriate agents, and records every stage change. The Master
Controller orchestrates but does not do the work itself — it cannot write
code, manage file history, or read secrets.

## Environment variable

A setting stored outside the codebase — in the operating system's
configuration rather than in any file that gets saved to file history.
This is where secrets (passwords, API keys, tokens) must live. The
guardrail scanner checks source files for anything that looks like a
secret and flags it as a violation.
