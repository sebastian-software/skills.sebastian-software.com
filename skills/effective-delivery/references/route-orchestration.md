# Route: Workflow Orchestration

Use this route when a request spans diagnosis, implementation, verification,
and delivery. Go directly to the specialist for an already narrow task.
Coordinate the next step and handoff; let the selected owner supply its methods.

## Establish the Outcome and Authority

Read scoped repository instructions, current working state, and the artifacts
needed to identify the outcome and acceptance evidence. Preserve unrelated work
and repository conventions. Keep answer-only requests read-only; a combined
request to diagnose and fix already authorizes both stages. Commit, publish,
message, merge, or deploy only within the user's granted authority and target.

Infer routine reversible choices from repository evidence. Ask only when a
missing decision materially changes outcome, scope, data, security, cost,
reversibility, or authority. For consequential alternatives, present the small
set of viable paths and a recommendation. Produce a reviewable plan before
high-impact or ambiguous implementation when it resolves those choices; save it
only under the user or repository's planning convention.

## Choose the Next Owner

| Immediate need | Owner or reference |
| --- | --- |
| Diagnose, audit, simplify, prioritize, or plan an improvement | [Audit route](route-audit.md) |
| Documentation, dependency work, or a port | The matching delivery route |
| Domain implementation, new test evidence, or a durable decision | Matching specialist discipline |
| Baseline, proof, review depth, or commit/handoff conventions | [Evidence and delivery](evidence-and-delivery.md) |
| Execute established checks | [Validation route](route-validation.md) |
| PR judgment or upkeep | [Review route](route-review.md) |

Load references only for the current decision. When ownership overlaps, a
specialist is unavailable, or delegation is useful, read
[Routing and selective installation](routing-and-fallbacks.md). Do not preload
the catalog or reproduce a missing specialist's handbook. Disclose material
loss of depth and use a bounded repository-led fallback when sufficient.

For delegation, keep one owner per mutable scope and pass the outcome,
authority, constraints, acceptance evidence, and return boundary. Use available
capabilities according to judgment difficulty and verifiable scope; keep work
local when context loss or coordination cost dominates. Never silently weaken
isolation, authority, tool limits, or required review to use another worker.

## Implement, Verify, and Deliver

1. Establish the relevant before evidence. For a refactor, compare the same
   behavior afterward; for a defect, reproduce or trace its broken invariant.
   Keep pre-existing failures distinct from introduced ones.
2. Implement the authorized outcome at its owning seam. Preserve trust-boundary
   checks, data protection, accessibility, compatibility, and required recovery.
   Keep consequential problem, architecture, and acceptance choices with the
   accountable human or team; agent generation does not settle them.
3. Run the narrowest decisive check and relevant repository gates. Generated
   code, agent confidence, and plan conformance are not behavioral proof. Add an
   independent reviewer or a separate cold pass for a named risk or demonstrated
   gap. Reconcile findings by evidence and accept zero findings.
4. Inspect the final diff and subtract speculative wrappers, options,
   dependencies, duplicated behavior, and unrelated files. Preserve requirements
   and safeguards. Report skipped checks and unresolved evidence honestly.
5. Before a commit or remote mutation, recheck the diff, unrelated work, target,
   branch, and authorized action. When adopting, writing in, staging from, or
   cleaning a worktree, apply [Worktree safety](worktree-safety.md).
6. Complete every requested deliverable. Report outcome, decisive evidence,
   delivery state, and exact blockers or remaining risk. A blocked item does
   not cancel independent work; no extra phase or artifact is needed when the
   authorized outcome is already verified.

Use repository-native plans, issues, commands, and files. Add no orchestration
configuration, hidden state, private ledger, role registry, or tracker scheme.
