# Staff Engineer

A system that lets a non-developer manage a team of AI agents the way a
senior engineer manages a team of developers — by defining what "done"
looks like, approving the work plan, reviewing proof that it worked, and
signing off on the result. The system enforces these steps mechanically:
it will refuse to skip any of them, and that refusal is the point.

## The core rule

**"Done" is something the machine can verify, not something anyone gets
to claim.** Every piece of work ends with a test that runs automatically,
produces evidence, and requires your explicit sign-off. No evidence, no
closure.

## How a sprint moves through the system

A sprint is a single piece of work — one goal, from start to finish. It
moves through a fixed sequence of stages, and several of those stages are
mandatory checkpoints (called gates) that cannot be skipped:

```
BACKLOG → PLANNING → DESIGN REVIEW → EXECUTION → QA AUDIT → LIVE TEST → YOUR REVIEW → COMPLETE
                         ↑____________|____________|__________|____________|
                         (any gate can send the work back for fixes;
                          your review can also send it back to planning)
```

Three things are always true:

- The checkpoints (QA Audit, Live Test, Your Review) cannot be skipped or
  bypassed. The system enforces this.
- Only the version-control agent (Pipeman) touches file history. Only you
  can close a sprint.
- Every stage change is recorded with who did it and when, so there is
  always a trail.

## Getting started

```bash
pip install pyyaml

# 1. Create a new sprint
/sprint-init my-sprint

# 2. Write your definition of done (what the machine will test for)
$EDITOR sprints/my-sprint/stopping-condition.md

# 3. Plan it, run it, review the evidence, close it
/sprint-plan my-sprint
/sprint-execute my-sprint
/sprint-complete my-sprint --user-said "I reviewed both reports and accept the result."

# Anytime: check that the rules are intact and a sprint's test passes
npm run guardrail
python3 scripts/verify_stopping_condition.py --sprint my-sprint
```

Step 2 is the hard one, and everything downstream depends on getting it
right. If you can't yet write that command, the
[Sprint Setup Bench](https://martinmontero.github.io/staff-engineer/sprint-setup-bench.html)
walks you to it in plain language — no code, nothing to install.

## Documentation

- [**Sprint Setup Bench**](https://martinmontero.github.io/staff-engineer/sprint-setup-bench.html)
  — an interactive worksheet, open it in a browser. Turns a vague goal
  into a machine-checkable stopping condition, a task graph it checks
  for loops, and the exact words to hand your agent. Use it before
  `/sprint-init`. Source: [docs/sprint-setup-bench.html](docs/sprint-setup-bench.html)
- [docs/NON-DEV-QUICKSTART.md](docs/NON-DEV-QUICKSTART.md) — start here
  if you don't code
- [docs/STAFF-ENGINEER-PLAYBOOK.md](docs/STAFF-ENGINEER-PLAYBOOK.md) —
  your four responsibilities
- [docs/GRAPH-ENGINEERING.md](docs/GRAPH-ENGINEERING.md) — why a work
  plan with dependencies beats a list of instructions
- [docs/SECURITY-MODEL.md](docs/SECURITY-MODEL.md) — what the system
  protects you from, and the rules that make it work
- [docs/GLOSSARY.md](docs/GLOSSARY.md) — terms used in this repo

## License

MIT — see [LICENSE](LICENSE).

---

## Acknowledgements

This repo is a synthesis of two pieces of work that deserve credit in full:

- **Sam Chan** —
  [*Stop cooking. Start writing recipes.*](https://samchan.ca/musings/graph-engineering-for-non-engineers)
  — supplied the graph-engineering frame and the "stiff peaks" stopping
  condition.
- **Chris Hobbs** —
  [`fully-completely`](https://github.com/chrishobbsrocks/fully-completely)
  — supplied the state machine, role separation, and the `--user-said`
  authorization gate.

See [CREDITS.md](CREDITS.md) for the full lineage.
