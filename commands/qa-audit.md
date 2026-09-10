---
command: /qa-audit
args: <sprint-id>
---

# /qa-audit <sprint-id>

Run the static QA1 audit.

1. Verify the sprint is in EXECUTION (handoffs emitted, branches merged).
2. Transition **EXECUTION → QA1**.
3. Invoke the **QA1 Auditor** agent with its full checklist:
   every node covered, tests present, no forbidden patterns, no hardcoded
   secrets, stopping condition referenced by a test, deps match
   `package.json`.
4. Write the result to `sprints/<sprint-id>/evidence/qa1-report.md`.
5. Transition on verdict:
   - PASS → **QA1 → LIVE_QA**
   - FAIL → **QA1 → EXECUTION** (send failing items back to the dev teams)

A partial pass is a FAIL. The auditor must refuse PASS on any failed item.
