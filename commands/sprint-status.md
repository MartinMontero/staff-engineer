---
command: /sprint-status
args: <sprint-id>
---

# /sprint-status <sprint-id>

Print a read-only status report for the sprint.

1. Load `sprints/<sprint-id>/state.json`.
2. Print:
   - Current state (from the state machine in
     `.staff-engineer/state-machine.yaml`, also list the legal next states).
   - Full transition history: actor, from → to, ISO timestamp.
   - Evidence hashes recorded for `evidence/qa1-report.md` and
     `evidence/live-qa-report.md`, if present.
3. If `state.json` does not exist, say so — never create it here. Status
   checks must not mutate state.
