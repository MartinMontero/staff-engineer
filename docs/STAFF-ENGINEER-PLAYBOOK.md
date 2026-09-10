# Staff Engineer Playbook

You are the Staff Engineer. The agents work for you; the gates protect you
from them. You have exactly four duties. Do them well and the system cannot
ship garbage without your signature.

## Duty 1: Define the stopping condition

Before any planning, write a machine-checkable command that exits 0 when the
sprint's goal is met. This is the hardest and most important thing you will
do. If you cannot write the command, you do not yet know what you are
building.

## Duty 2: Approve the graph

At DESIGN_REVIEW, read the Architect's recommended DAG. Ask: does every node
matter? Is anything missing? Is anything unverifiable? Execution does not
start until you approve. An approved bad graph is your fault, not the
agents'.

## Duty 3: Review the evidence

At USER_REVIEW, read both reports: `evidence/qa1-report.md` (static audit)
and `evidence/live-qa-report.md` (the stopping condition actually executed).
Check the exit code, skim the output, and verify the hashes. The reports are
short on purpose — read them.

## Duty 4: Authorize closure explicitly

Close with `/sprint-complete <id> --user-said "..."` and a real sentence
stating that you reviewed the evidence and accept the result. Empty or
rubber-stamp quotes defeat the entire system.

## Anti-patterns

- **"It looks done, just close it."** Done is a verifiable state, not a
  judgment call. No evidence, no closure.
- **Skipping the stopping condition** ("we'll know it when we see it"). You
  won't. Write the command.
- **Approving graphs unread.** The graph is the contract; read it.
- **Letting an agent run `/sprint-complete`.** Human-only. Always.
- **Treating a QA failure as a nuisance** instead of a signal. The gate
  caught something. Send it back to EXECUTION and fix the graph if failures
  repeat.
