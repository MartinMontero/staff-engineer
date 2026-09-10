# Security Model

## Threat model

Aligned with the OWASP Agentic AI Top 10.

| Threat | OWASP ref | Mitigation in this repo |
| --- | --- | --- |
| Goal Hijacking — an agent redefines "done" to whatever it achieved | ASI01 | The stopping condition is written by the human before planning; the Architect refuses non-machine-checkable goals; only the human can close a sprint. |
| Tool Misuse — agents use tools beyond their mandate | AAI01 | Per-role capability matrices in `.staff-engineer/guardrails.yaml` (can/cannot per role); only Pipeman touches git; no dev agent touches git or config. |
| Multi-Agent Privilege Escalation — one agent leverages another's powers | AAI05 | Strict role separation: Master Controller orchestrates but cannot write code or run git; dev teams write code but cannot merge; no single agent holds both write and publish powers. |
| Identity Confusion — actions attributed to the wrong actor | AAI06 | Every state transition records the actor and an ISO timestamp in `state.json`; sprint closure requires an attributable `--user-said` quote. |
| Secrets leakage — credentials committed or exposed to agents | — | Env-only secrets policy; `guardrail_check.py` regex-scans `src/**` for key patterns on every CI run; agents are forbidden from reading secrets. |

## Non-negotiable rules

1. **Human-only `/sprint-complete`.** No agent may close a sprint. Closure
   requires both QA reports at PASS plus a non-empty user quote.
2. **No agent edits `.staff-engineer/**`.** The rules of the game are not
   writable by the players.
3. **No long-lived secrets.** Environment variables only; Live QA uses a
   short-lived runner token rotated per sprint.
4. **Every transition is recorded.** Actor, from, to, timestamp — in
   `state.json`, always.
5. **Evidence is hashed and stored in git.** sha256 hashes per
   `.staff-engineer/config.yaml`; tampering is detectable.
