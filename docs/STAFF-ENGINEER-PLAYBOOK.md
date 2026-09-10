# Staff Engineer Playbook

You are the Staff Engineer. The AI agents work for you. The checkpoints
protect you from them. You have exactly four responsibilities, and if you
do them well, the system cannot ship anything without your informed
approval.

## Responsibility 1: Define what "done" looks like

Before any planning begins, write a command that the system can run to
test whether the sprint's goal has been achieved. The command succeeds
(returns a result code of zero) when the goal is met and fails (returns
anything else) when it is not.

This is the hardest and most important thing you will do.

A good stopping condition is specific, testable, and leaves no room for
debate. "The application loads" is too vague. "The health endpoint at
localhost:3000/health returns a successful response" is testable — either
it does or it doesn't.

If you cannot write the command, you do not yet know what you are
building. That is useful information. Stop, clarify the goal, and then
come back to this step.

## Responsibility 2: Approve the work plan

At the Design Review stage, the Architect agent presents a structured work
plan — a set of tasks arranged by dependency, showing what must happen
first and what can proceed in parallel. The Architect shows you three
options with trade-offs and recommends one.

Read it. Ask yourself three questions:

1. Does every task in the plan actually matter for the goal?
2. Is anything missing that the goal requires?
3. Can every task be verified — is there a way to check that it worked?

Execution does not start until you approve the plan. If you approve a bad
plan, the resulting problems are yours, not the agents'. The plan is the
contract between you and the system. Take it seriously.

## Responsibility 3: Review the evidence

At the Your Review stage, two short reports are waiting for you:

- `evidence/qa1-report.md` — a checklist audit. Did the agents build what
  the plan said? Are there tests? Are there security violations? Every
  item must pass. A partial pass is a failure.

- `evidence/live-qa-report.md` — the result of actually running your
  stopping condition. Shows the exact command, its output, and the result
  code. Zero means it succeeded. Anything else means it failed.

Check the result code. Skim the output. Verify the integrity hashes (a
unique fingerprint for each report, stored in file history, that proves
the reports have not been altered after the fact).

The reports are short on purpose. Read them.

## Responsibility 4: Close the sprint with an explicit authorization

Close with `/sprint-complete <id> --user-said "..."` and write a real
sentence stating that you reviewed the evidence and accept the result.

The `--user-said` flag is your signature. The system refuses to close
if either quality report is missing, if either shows a failure, or if
your quote is empty. This is not a checkbox — it is the mechanism that
keeps a human being accountable for every piece of work that ships.

An empty or pro-forma quote defeats the entire purpose. If you find
yourself writing "looks good" without having read the reports, the system
is no longer protecting you.

## Patterns that break the system

These are the ways people defeat their own guardrails. Recognise them
and refuse to do them.

- **"It looks done, just close it."** "Done" is a verifiable state, not
  a feeling. The stopping condition exists specifically so that no one —
  including you — has to guess. If it passes, it is done. If it does not,
  it is not.

- **Skipping the stopping condition.** "We'll know it when we see it" is
  a recipe for agents declaring victory on their own terms. Write the
  command. If you cannot write it, the goal is not clear enough yet.

- **Approving the plan without reading it.** The plan is a contract. If
  you approve it unread, you are signing a blank cheque. The agents will
  build exactly what the plan says — and if the plan is wrong, the result
  will be wrong.

- **Letting an agent close the sprint.** The `/sprint-complete` command
  is restricted to humans for a reason. Technical readiness and human
  authorization are separate gates. Both quality checkpoints passing means
  the code works; it does not mean you have decided to ship it.

- **Treating a quality failure as a nuisance.** When a checkpoint catches
  something, that is the system working. Send the work back to Execution.
  If the same failure keeps recurring, the work plan needs revising — send
  it back to Planning.
