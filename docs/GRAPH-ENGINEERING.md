# Graph Engineering

## A shopping list is not a recipe

"Build auth, add a dashboard, fix the bugs" is a shopping list. It says what
to buy, not how to cook. It has no order, no dependencies, and no way to
know when dinner is ready. LLM agents handed a shopping list will improvise
the recipe — and they will confidently serve you something raw.

A **task graph** is the recipe. It is a **directed acyclic graph (DAG)**:
each node is a unit of work, each edge is a dependency, and cycles are
forbidden. The DAG forces three questions a prompt never does:

1. **What must exist before this node starts?** (edges)
2. **What does "this node works" mean?** (per-node verification)
3. **How do we know the whole thing is done?** (the terminal node reaches
   the stopping condition)

## Why graphs beat prompts

Prompts are vibes; graphs are contracts. A prompt lets an agent declare
victory. A graph gives the QA1 Auditor a checklist — every node covered,
every node tested — and gives the Live QA runner a single executable
stopping condition. When a node fails, the graph tells you exactly what is
blocked and what can still proceed. When an agent drifts, the graph is the
diff you review.

## The stiff peaks metaphor

Baking instructions say "whip egg whites to stiff peaks" — not "whip for a
while." Stiff peaks is a *testable state*: lift the whisk and the peak
stands. Your stopping condition is the stiff-peaks test for the sprint. If
the peak droops, you keep whipping (back to EXECUTION). You never argue the
meringue into being done. **Done is a verifiable state, not a judgment
call.**
