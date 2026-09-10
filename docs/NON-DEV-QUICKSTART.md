# Non-Developer Quickstart

You are not here to write code. You are here to make five decisions, in
order, and let the AI agents handle the implementation. The system is
designed so that nothing ships without your explicit approval at each
stage — and it enforces that mechanically, not on the honour system.

Here are the five steps, what each one actually does, and why it matters.

## Step 1: Define what "done" looks like — in a way a machine can test

Open the file `sprints/<id>/stopping-condition.md` and replace the
placeholder with a single command that the system can run to check whether
your goal has been achieved.

This is the most important thing you will do in the entire sprint.

The command needs to do one thing: succeed (return a result code of zero)
when the goal is met, and fail (return anything other than zero) when it
is not. The system runs this command automatically during the Live Test
checkpoint, and the result code is the verdict. There is no room for
interpretation.

Two examples of what this looks like:

- `npm test` — runs the project's test suite. Succeeds if all tests pass.
- `curl -sf http://localhost:3000/health` — hits the application's health
  endpoint. Succeeds if the server responds, fails if it doesn't.

If you cannot write this command, that is not a problem with the tool — it
is a signal that you do not yet know what you are building. Stop and
clarify the goal before you do anything else.

## Step 2: Review and approve the work plan

Run `/sprint-plan <id>`.

The Architect agent reads your stopping condition and proposes three
different work plans. Each plan is a structured set of tasks with
dependencies between them — what needs to happen first, what can happen in
parallel, and how each piece connects to the next. The Architect explains
the trade-offs between the three plans and recommends one.

Read the recommendation. Think about whether the tasks cover everything
your goal requires, and whether anything is missing or unnecessary.
Nothing executes until you say "go." If the plan is wrong and you approved
it, that is on you, not the agents.

## Step 3: Let the system execute — and watch it verify itself

Run `/sprint-execute <id>`.

The system now takes over. The Master Controller drives the work through
three stages automatically:

1. **Execution.** The development agents build what the plan says. The
   version-control agent (Pipeman) manages the file history. When the
   agents finish, they hand off their work — they never claim it is done,
   only that it is ready for review.

2. **QA Audit.** An auditor agent checks the work against the plan: is
   every task covered? Are there tests for everything? Are there any
   security problems (like passwords left in the code)? If anything fails,
   the work goes back to the development agents automatically. You do not
   need to intervene.

3. **Live Test.** The system runs your stopping condition — the command
   you wrote in Step 1 — for real. If it succeeds, the sprint moves to
   your review. If it fails, the work goes back to the development agents,
   and the loop repeats until the test passes.

This loop can run multiple times without you doing anything. The system
only stops and waits for you when both quality checkpoints have passed.

## Step 4: Read the evidence

Two short files will be waiting for you:

- `evidence/qa1-report.md` — the auditor's checklist, showing what passed
  and what failed.
- `evidence/live-qa-report.md` — the exact command that ran, what it
  returned, and whether it succeeded.

Look for two things: the verdict says "PASS" in both reports, and the
result code in the Live Test report is 0 (which means the command
succeeded). The reports are deliberately kept short so you will actually
read them.

## Step 5: Close the sprint with your signature

Run `/sprint-complete <id> --user-said "I reviewed both reports and accept
the result."`

This is the only way to close a sprint, and only you can do it. The
`--user-said` part is your signature — a real sentence, in your own words,
stating that you reviewed the evidence and are authorizing this work to
ship. The system will refuse to close if either quality report is missing,
if either shows a failure, or if your quote is empty.

This is not a formality. If you rubber-stamp this step, the entire system
is pointless. Read the evidence, then sign.

## What you never do

- **Never write or edit code.** The development agents do that. Your job
  is to define the goal, approve the plan, and verify the result.

- **Never run file-history commands** (git). Pipeman owns that, and the
  separation exists so that no single agent — or person — can both write
  code and publish it.

- **Never skip a checkpoint or close a sprint without evidence.** The
  system will refuse, and that refusal is the product working exactly as
  designed.

- **Never put passwords, API keys, or secrets in files or prompts.** They
  go in environment variables (settings that live outside the code and are
  never saved to file history). The guardrail scanner will catch it if you
  slip.

- **Never let an agent run `/sprint-complete`.** That command is yours
  alone. It exists specifically to make sure a human being — you — has
  reviewed and accepted the result before anything ships.
