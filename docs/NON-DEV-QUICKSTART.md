# Non-Developer Quickstart

You don't need to write code. You need to make five decisions and let the
agents do the typing.

## The 5 steps

1. **Write the stopping condition.** Edit
   `sprints/<id>/stopping-condition.md` and replace the placeholder with one
   command that exits 0 when your goal is achieved. Example: `npm test`, or
   `curl -sf http://localhost:3000/health`. If you can't write it, you don't
   yet know what you're building.

2. **`/sprint-plan <id>`.** The Architect proposes 3 plans (task graphs)
   with tradeoffs and recommends one. Read it. Approve it. Nothing executes
   until you do.

3. **`/sprint-execute <id>`.** The Master Controller drives the dev teams,
   then runs both quality gates automatically: QA1 (static audit) and Live
   QA (your stopping condition, executed for real). Failures loop back to
   the dev teams without you lifting a finger.

4. **Read the evidence.** Two short files: `evidence/qa1-report.md` and
   `evidence/live-qa-report.md`. Look for "Verdict: PASS" and an exit code
   of 0. That's it.

5. **`/sprint-complete <id> --user-said "I reviewed both reports and accept
   the result."`** This is your signature. The sprint cannot close without
   it.

## What you never do

- Never write or edit code in `src/` — that's what the dev teams are for.
- Never run git commands — Pipeman owns git.
- Never skip a gate or close a sprint without evidence — the system will
  refuse, and that refusal is the product working.
- Never put secrets in files or prompts — environment variables only.
- Never let an agent run `/sprint-complete` — that command is yours alone.
