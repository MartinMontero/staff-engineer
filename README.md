# Staff Engineer

A guardrail-enforced state machine that turns a non-developer into a Staff
Engineer — by refusing to let LLM agents skip verification, and refusing to
let the human skip accountability.

## Core rule

**Done is a verifiable state, not a judgment call.** Every sprint ends with
a machine-checkable stopping condition, executed for real, with hashed
evidence and explicit human authorization. No evidence, no closure.

## Sprint lifecycle

```
BACKLOG → PLANNING → DESIGN_REVIEW → EXECUTION → QA1 → LIVE_QA → USER_REVIEW → COMPLETE
                         ↑____________|___________|_____|__________|
                         (any gate may send the sprint back to EXECUTION;
                          USER_REVIEW may also send it back to PLANNING)
```

- **Gates** (QA1, Live QA, User Review) cannot be skipped. `allow_skip: false`.
- Only **Pipeman** touches git; only the **human** runs `/sprint-complete`.
- Every transition is recorded in `sprints/<id>/state.json` with actor and
  timestamp.

## Quickstart

```bash
pip install pyyaml

# 1. Initialize a sprint
/sprint-init my-sprint

# 2. Write your machine-checkable stopping condition
$EDITOR sprints/my-sprint/stopping-condition.md

# 3. Plan, approve the graph, execute, review evidence, close
/sprint-plan my-sprint
/sprint-execute my-sprint
/sprint-complete my-sprint --user-said "I reviewed both reports and accept the result."

# Anytime: check the guardrails and a sprint's stopping condition
npm run guardrail
python3 scripts/verify_stopping_condition.py --sprint my-sprint
```

## Docs

- [docs/NON-DEV-QUICKSTART.md](docs/NON-DEV-QUICKSTART.md) — start here if you don't code
- [docs/STAFF-ENGINEER-PLAYBOOK.md](docs/STAFF-ENGINEER-PLAYBOOK.md) — your four duties
- [docs/GRAPH-ENGINEERING.md](docs/GRAPH-ENGINEERING.md) — why task graphs beat prompts
- [docs/SECURITY-MODEL.md](docs/SECURITY-MODEL.md) — threat model and non-negotiable rules
- [docs/GLOSSARY.md](docs/GLOSSARY.md) — terms

## License

MIT — see [LICENSE](LICENSE).

---

## Acknowledgements

This repo is a synthesis of two pieces of work that deserve credit in full:

- **Sam Chan** — [*Stop cooking. Start writing recipes.*](https://samchan.ca/musings/graph-engineering-for-non-engineers) — supplied the graph-engineering frame and the "stiff peaks" stopping condition.
- **Chris Hobbs** — [`fully-completely`](https://github.com/chrishobbsrocks/fully-completely) — supplied the state machine, role separation, and the `--user-said` authorization gate.

See [CREDITS.md](CREDITS.md) for the full lineage.
