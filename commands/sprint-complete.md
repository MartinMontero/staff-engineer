---
command: /sprint-complete
args: <sprint-id> --user-said "<quote>"
---

# /sprint-complete <sprint-id> --user-said "<quote>"

The **only** way to close a sprint. Human-only. No agent may invoke this.

## Preconditions (ALL required — refuse if any is missing)

1. Sprint is in USER_REVIEW.
2. `sprints/<sprint-id>/evidence/qa1-report.md` exists with verdict PASS.
3. `sprints/<sprint-id>/evidence/live-qa-report.md` exists with verdict PASS.
4. `--user-said "<quote>"` is present and **non-empty** — an explicit,
   attributable statement of authorization from the human.

## On refusal

Print exactly which condition failed. Do not suggest workarounds. The gates
are the product.

## On success

1. Record the user quote in `sprints/<sprint-id>/state.json` alongside the
   evidence hashes.
2. Transition **USER_REVIEW → COMPLETE**.
3. Print a closure summary: stopping condition, evidence hashes, user quote.
