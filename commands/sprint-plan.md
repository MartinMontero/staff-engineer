---
command: /sprint-plan
args: <sprint-id>
---

# /sprint-plan <sprint-id>

Plan the sprint.

1. Verify the sprint is in BACKLOG and that `stopping-condition.md` contains
   a machine-checkable bash block (the Architect will refuse otherwise).
2. Invoke the **Architect** agent: read `stopping-condition.md`, propose 3
   candidate task graphs with tradeoffs, and recommend one.
3. Write the recommended graph to `sprints/<sprint-id>/graph.yaml`.
4. Transition **BACKLOG → PLANNING → DESIGN_REVIEW** via
   `scripts/sprint_lifecycle.py`, recording each hop.
5. **Stop for human approval.** Do not begin execution without the human
   approving the graph (see `docs/STAFF-ENGINEER-PLAYBOOK.md`, duty 2).
