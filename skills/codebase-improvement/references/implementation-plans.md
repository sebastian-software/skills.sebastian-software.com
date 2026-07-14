# Implementation Plans

Use this reference to create, review, save, or reconcile plans that another
human or agent can execute without relying on the planning conversation.

## Contents

- [Plan Ownership](#plan-ownership)
- [Plan Contract](#plan-contract)
- [Drift and Working State](#drift-and-working-state)
- [Plan Template](#plan-template)
- [Review and Reconciliation](#review-and-reconciliation)

## Plan Ownership

Discover the repository's existing planning surface before writing:

- Use the established issue tracker when delivery work already lives there.
- Use an existing `docs/plans/`, `plans/`, roadmap, RFC, or project convention
  when present.
- Use an ADR only for the durable decision and rationale, never as a task-status
  ledger.
- Return the plan in chat when the user did not ask to persist it.

When the user asks to save a plan and no convention exists, use plain Markdown
under `docs/plans/`. Add an index only when several plans require dependency or
status tracking. Do not introduce a hidden directory or tool-specific schema.

## Plan Contract

A useful plan is:

- **Self-contained:** include intent, current evidence, relevant decisions,
  exact paths and symbols, and repository conventions needed for judgment.
- **Scoped:** name files or areas in scope and tempting adjacent work that is
  explicitly out of scope.
- **Ordered:** make prerequisites and safe migration order visible.
- **Verifiable:** pair each step with an actual repository command and expected
  result where feasible.
- **Drift-aware:** record the code state used for planning and explain how to
  detect invalidated assumptions before execution.
- **Bounded under uncertainty:** add specific stop conditions where improvising
  would materially change risk, behavior, public API, data, or scope.
- **Maintainable:** identify the enduring contract and what reviewers should
  scrutinize after the immediate change.

Do not assume the executor is cheaper, less capable, or a subagent. Write for a
competent collaborator who lacks the planning session's hidden context.

## Drift and Working State

For a Git repository, record the short HEAD SHA and planning date. Check whether
in-scope files have uncommitted changes; do not describe HEAD as the complete
current state when the plan was based on a dirty worktree.

At execution time:

1. Compare current in-scope files with the recorded state.
2. Re-read excerpts and assumptions when those files changed.
3. Continue when changes are compatible and the plan still describes reality.
4. Stop or revise the plan when public contracts, chosen architecture, required
   scope, or verification commands no longer match.

Drift detection protects intent; it should not reject harmless line movement or
force a new plan for every unrelated commit.

## Plan Template

Adapt this to the project's format rather than copying empty sections.

```md
# <Outcome-oriented plan title>

## Status

- Priority: P1 / P2 / P3
- Effort: S / M / L
- Risk: LOW / MEDIUM / HIGH
- Depends on: <items or none>
- Planned at: <short SHA>, <date>
- Working state: <clean or relevant uncommitted paths>

## Why this matters

Describe the verified problem, concrete cost, intended outcome, and relevant
ADR or product constraint.

## Current state

- `path/file.ext:line`: role and verified behavior
- Existing convention to follow, with a representative location
- Relevant decision, interface, data, or compatibility constraint

## Scope

In scope:
- Exact files, packages, public contracts, or behaviors

Out of scope:
- Adjacent work that must not be folded into this change

## Verification commands

| Purpose | Command | Expected result |
| --- | --- | --- |
| Focused tests | `<real command>` | exit 0 and named cases pass |
| Type or build check | `<real command>` | exit 0 |

## Steps

### 1. <Safe first outcome>

Describe exact files, symbols, behavior, migration order, and test additions.

Verify: `<command>` -> <expected result>

### 2. <Next outcome>

Continue with the smallest independently verifiable step.

## Done criteria

- [ ] Observable behavior or invariant
- [ ] Named regression cases pass
- [ ] Required repository checks pass
- [ ] No unintended scope changes
- [ ] Related decision, issue, docs, or generated artifacts are consistent

## Stop conditions

- Stop when a named assumption is false.
- Stop when the change requires a public API, schema, security boundary, or
  out-of-scope file not covered by the plan.
- Stop when the verification baseline is already failing in a way that prevents
  attributing results to this work.

## Maintenance and review focus

Name future interactions, deliberately deferred work, and the riskiest review
questions.
```

Use excerpts only when they anchor a fragile contract or help detect drift. Do
not duplicate large source files inside the plan.

## Review and Reconciliation

When reviewing a plan, check:

- Does the current code still contain the claimed problem?
- Does the plan respect accepted ADRs and project terminology?
- Are scope and exclusions sufficient to prevent attractive side quests?
- Do commands exist, run from the stated directory, and test the intended
  behavior rather than merely exit successfully?
- Do new tests prove the regression and meaningful edge cases?
- Are stop conditions specific to actual uncertainty?
- Are secrets omitted and external requirements current?

When reconciling a backlog:

- **Done:** verify cheap, decisive criteria and link the implementation.
- **Blocked:** investigate the blocker; revise, split, or reject the plan.
- **In progress:** confirm ownership and current branch or worktree state.
- **Todo:** rerun drift checks and verify the finding still exists.
- **Superseded or duplicate:** preserve a short rationale and point to the
  successor.
- **No longer valuable:** reject explicitly instead of leaving permanent stale
  work.

Finish with the next executable item and its prerequisites. Do not confuse a
large backlog with progress.
