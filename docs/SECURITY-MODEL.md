# Security Model

## What can go wrong with AI agents, and how this system prevents it

AI agents are powerful but untrustworthy in specific, predictable ways.
The security model in this repo is designed around five known threats —
the ways agents can silently undermine the work if the system does not
actively prevent them. These threats are drawn from the OWASP Agentic AI
Top 10, an industry-standard catalogue of risks specific to AI-driven
systems.

### Threat 1: Goal hijacking — the agent redefines "done"

**The risk.** An agent fails to achieve the actual goal, but produces
something plausible and declares victory. Since the agent wrote the work
and is evaluating the work, it can make failure look like success.

**How this system prevents it.** The stopping condition — the test that
defines "done" — is written by you, the human, before any planning starts.
The Architect agent refuses to proceed if the stopping condition is not
something a machine can test. Only you can close a sprint. The agent's
opinion of whether the work is done is irrelevant; the test's result code
is the verdict.

### Threat 2: Tool misuse — agents use capabilities they shouldn't have

**The risk.** A development agent modifies the project's configuration
files, or pushes code to the shared repository, or reads passwords. Any
of these can cause damage that is hard to detect after the fact.

**How this system prevents it.** Every agent has an explicit list of what
it is allowed to do and what it is forbidden from doing, defined in the
guardrails file (`.staff-engineer/guardrails.yaml`). Only Pipeman touches
file history. No development agent can access file history or
configuration. The guardrail scanner checks for violations automatically.

### Threat 3: Privilege escalation — one agent borrows another's powers

**The risk.** Agent A cannot push code, but Agent B can. If Agent A can
instruct Agent B, it effectively gains the ability to push code through a
back door.

**How this system prevents it.** Strict role separation. The Master
Controller orchestrates the workflow but cannot write code or manage file
history. The development agents write code but cannot publish it. No
single agent holds both the power to create and the power to deploy. The
only path from "code written" to "code shipped" passes through two
independent quality checkpoints and your explicit sign-off.

### Threat 4: Identity confusion — actions attributed to the wrong actor

**The risk.** Without clear attribution, it becomes impossible to know
which agent did what. If something goes wrong, there is no trail to
follow, and accountability is impossible.

**How this system prevents it.** Every stage change is recorded in the
sprint's state file with the actor's name and an ISO timestamp (a
standardised date-and-time format). Sprint closure requires an explicit,
attributable quote from you. The trail is always there.

### Threat 5: Secrets leakage — passwords or keys exposed in code

**The risk.** An agent writes a password, API key, or other secret
directly into a source file. That secret is then saved permanently in
file history, where anyone with access can find it — even if the file is
later edited to remove it.

**How this system prevents it.** All secrets must be stored as environment
variables — settings that live outside the code and are never written to
files. The guardrail scanner runs a set of pattern-matching rules against
every source file, looking for anything that resembles a key or password.
It runs automatically on every check-in and can also be run manually at
any time. Agents are forbidden from reading secrets under any
circumstances.

## The five rules that cannot be broken

These are the structural rules that make the security model work. They are
not guidelines or best practices — they are hard constraints enforced by
the system. If any of them could be bypassed, the system would not be
trustworthy.

1. **Only you can close a sprint.** No agent may run `/sprint-complete`.
   Closure requires both quality reports showing PASS and a non-empty
   quote from you — your explicit authorization. The code being ready and
   you deciding to ship it are treated as two separate conditions, and
   both must be met.

2. **No agent can edit the rules.** The configuration files in
   `.staff-engineer/` define the rules of the system — the state machine,
   the guardrails, the gate requirements. No agent is allowed to modify
   them. The players cannot change the rules of the game.

3. **No long-lived secrets.** Environment variables only. The Live Test
   uses a short-lived token (a temporary credential) that is replaced
   after each sprint, so even if it were exposed, it would be useless
   shortly afterward.

4. **Every stage change is recorded.** Who did it, what the previous stage
   was, what the new stage is, and when it happened. This trail is stored
   in the sprint's state file and is always available for review.

5. **Evidence is fingerprinted and stored in file history.** Each quality
   report gets a sha256 hash — a unique fingerprint derived from its
   contents. If anyone modifies a report after the fact, the fingerprint
   will no longer match, and the tampering is detectable. These
   fingerprints are stored in file history alongside the reports.
