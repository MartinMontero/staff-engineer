# Credits & Acknowledgements

This project stands directly on the work of two people. Without them, this repo does not exist.

---

## Sam Chan — *Stop cooking. Start writing recipes.*

**Source:** https://samchan.ca/musings/graph-engineering-for-non-engineers

Sam's article is the **conceptual foundation** of this repo. It gave us:

- **The shopping list is not the recipe.** The order and dependencies between tasks — the graph — are the actual work. A list of ingredients is not dinner.
- **"Stiff peaks" as a stopping condition.** A loop only works when the stopping condition is stated up front and is checkable by someone who isn't you. "Whisk until it looks good" puts you back at the bowl. "Whisk until stiff peaks" lets you walk away.
- **Graph engineering for non-engineers.** The framing that makes agentic development legible to people who don't already speak "nodes and loops."

Every `stopping-condition.md`, every `graph.yaml`, and `scripts/verify_stopping_condition.py` in this repo is a direct expression of Sam's thesis.

---

## Chris Hobbs — [`fully-completely`](https://github.com/chrishobbsrocks/fully-completely)

**Source:** https://github.com/chrishobbsrocks/fully-completely

Chris's framework is the **enforcement foundation** of this repo. It gave us:

- **Six agent roles** (Master Controller, Dev Team 1, Dev Team 2, QA1, Pipeman, LiveQA) — mapped directly onto `agents/*.md`.
- **Two mandatory QA gates.** Nothing closes unless QA1's audit and LiveQA's live test have both been recorded as PASS.
- **`/sprint-complete --user-said "..."`.** The insight that technical readiness and human authorization are *separate* gates — and that closing a sprint must require an explicit, non-empty quote from the human. Both gates passing tells you the code is ready; it does not tell you the human has decided to close it.
- **A state file per sprint, slash commands as the only way forward, and a script that refuses to skip steps.** That refusal *is* the product.

`.staff-engineer/state-machine.yaml`, `.staff-engineer/guardrails.yaml`, and `scripts/sprint_lifecycle.py` are adaptations of Chris's enforcement model.

---

## What this repo adds

The synthesis: taking Sam's conceptual frame and Chris's enforcement mechanics and building a single repo where **the human is the Staff Engineer** and the LLM agents are a dev team that reports to them. The additions are:

- A per-role guardrail matrix (`guardrails.yaml`) with explicit `can` / `cannot` lists.
- A reusable Python state machine (`sprint_lifecycle.py`) that refuses illegal transitions and prints the legal ones.
- A guardrail scanner (`guardrail_check.py`) that runs in CI and as a pre-commit hook.
- Documentation written for non-developers (`docs/NON-DEV-QUICKSTART.md`).

If you build on this, credit Sam and Chris. Their work is why this repo exists.
