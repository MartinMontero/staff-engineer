---
command: /sprint-execute
args: <sprint-id>
---

# /sprint-execute <sprint-id>

Drive the sprint through execution and both QA gates.

1. Verify the human approved the graph in DESIGN_REVIEW.
2. The **Master Controller** drives the pipeline:
   - **DESIGN_REVIEW → EXECUTION**: Pipeman creates `sprint/<id>` and feature
     branches; Dev Team 1 (and Dev Team 2 in its worktree) implement assigned
     graph nodes and emit handoffs; Pipeman merges.
   - **EXECUTION → QA1**: run `/qa-audit <sprint-id>`.
   - **QA1 → LIVE_QA** (on PASS) or **QA1 → EXECUTION** (on FAIL): loop until
     QA1 passes, then run `/qa-live <sprint-id>`.
   - **LIVE_QA → USER_REVIEW** (on PASS) or **LIVE_QA → EXECUTION** (on FAIL).
3. **Stop at USER_REVIEW.** Present both evidence reports to the human.
   Only the human can close the sprint with `/sprint-complete`.
