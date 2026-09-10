---
command: /sprint-init
args: <sprint-id>
---

# /sprint-init <sprint-id>

Initialize a new sprint.

1. Create `sprints/<sprint-id>/` by copying `templates/sprint/` (including
   `sprint.md`, `graph.yaml`, `stopping-condition.md`, and the `evidence/`
   placeholders).
2. Replace `<SPRINT-ID>` placeholders in the copied files.
3. Create `sprints/<sprint-id>/state.json` and transition the sprint to
   **BACKLOG** via `scripts/sprint_lifecycle.py`.
4. Report the created paths to the user.

The human must now write a machine-checkable stopping condition before any
planning can begin.
