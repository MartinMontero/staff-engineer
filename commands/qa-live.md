---
command: /qa-live
args: <sprint-id>
---

# /qa-live <sprint-id>

Run the live QA gate — execute the stopping condition for real.

1. Verify the sprint is in QA1 with a PASS verdict in
   `evidence/qa1-report.md`, then transition **QA1 → LIVE_QA**.
2. Invoke the **Live QA** agent:
   - Run the test suite.
   - Execute the stopping condition via
     `python3 scripts/verify_stopping_condition.py --sprint <sprint-id>`.
   - Record command, exit code, and stdout/stderr.
3. Write results to `sprints/<sprint-id>/evidence/live-qa-report.md` and
   emit a signed evidence bundle.
4. Transition on verdict:
   - Exit 0 (PASS) → **LIVE_QA → USER_REVIEW**
   - Nonzero exit (FAIL) → **LIVE_QA → EXECUTION**

The exit code is the verdict. There is no partial credit.
