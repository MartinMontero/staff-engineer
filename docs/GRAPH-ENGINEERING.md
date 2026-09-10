# Graph Engineering

## A shopping list is not a recipe

"Build login, add a dashboard, fix the bugs" is a shopping list. It tells
you what to buy but not how to cook. There is no order, no dependency
between the items, and no way to know when dinner is ready. Hand that list
to an AI agent and it will improvise the recipe — and it will confidently
serve you something half-cooked.

A **task graph** is the recipe.

It is a structured plan where each piece of work is a node, and the
connections between nodes show what depends on what. "Build the database
before building the login page" is a dependency — one thing must exist
before the next can start. The structure is called a directed acyclic
graph, or DAG: "directed" because each connection has a direction (A must
happen before B), and "acyclic" because the plan cannot loop back on
itself (B cannot also be required before A — that would be a
contradiction).

The power of a task graph is that it forces three questions that a flat
list of instructions never asks:

1. **What must already exist before this task can start?** The connections
   between nodes answer this. If the database is not built, the login page
   has no place to store users, and the graph makes that explicit.

2. **How do we know this specific task worked?** Each node has its own
   verification step. This means problems are caught at the task level,
   not at the end of the entire project.

3. **How do we know the whole thing is done?** The final node in the graph
   reaches the stopping condition — the test you wrote at the start. If
   that test passes, every path through the graph has succeeded. If it
   fails, the graph tells you exactly where the problem is.

## Why task graphs beat flat instructions

When you give an AI agent a flat instruction — "build me a login system"
— the agent decides what that means, builds something, and declares
victory. You have no way to audit what it did or verify that it matches
what you wanted.

A task graph changes that relationship in three ways:

**It gives the auditor a checklist.** The QA Audit agent walks the graph
node by node: is every task covered by an implementation? Is every task
covered by a test? Were any tasks skipped? This is mechanical — the
auditor is not judging quality, it is checking coverage against a known
plan.

**It gives the live test a single, definitive answer.** The stopping
condition runs at the end, and its result code is the verdict. Pass or
fail, no interpretation required.

**It makes failure informative.** When a flat instruction fails, you know
something went wrong but not where. When a node in a graph fails, you
know exactly which task broke, what it depended on, and what other tasks
are blocked by the failure. That specificity is the difference between
"try again" and "fix this one thing."

## The stiff-peaks test

This idea comes from baking. A recipe says "whip egg whites to stiff
peaks" — not "whip for a while" or "whip until it looks about right."
Stiff peaks is a testable condition: lift the whisk and either the peak
holds its shape or it droops. If it droops, you keep whipping. You do not
argue the meringue into being done.

Your stopping condition is the stiff-peaks test for the sprint.

You define it before any work begins. The system runs it automatically.
If it passes, the work is done. If it fails, the work goes back for
another round — back to Execution — until the test passes. Nobody gets
to declare it done by opinion or by exhaustion.

**"Done" is a verifiable state, not a judgment call.**
