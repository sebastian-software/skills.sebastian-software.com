# Ready-to-merge state

Treat `ready-to-merge` as a derived, reversible flag—not an approval and never an
instruction to merge.

## Add the flag only when all conditions hold

- The PR is open and non-draft.
- The latest remote head is the intended final implementation commit.
- The branch is conflict-free and satisfies the repository's base/update policy.
- Every required check for that head is complete and accepted by branch
  protection. No required check is pending, queued, failing, canceled, timed out,
  or awaiting action.
- Required preview/deployment and documentation gates are satisfied.
- Review bots have completed their expected pass, or the repository's bounded
  watcher has completed with no actionable finding.
- No unresolved substantive review thread or requested change remains.
- No linked issue comment, reopened issue, or newly linked defect reports a
  reproducible problem in this implementation.
- All fixes have been pushed and proportionate local validation has passed.

## Remove the flag immediately when any condition stops holding

Remove it on:

- any new push until required checks and reviews cover the new head;
- red/canceled/timed-out/action-required required CI;
- a substantive new review finding or reproducible linked problem;
- a merge conflict, draft transition, missing required preview, or invalidated
  documentation gate;
- a reopened requirement that means more code is expected.

Remove first, then diagnose. Even an apparently flaky or infrastructure-only red
check makes the flag temporarily false; such a failure may be documented and
escalated rather than “fixed” in product code.

Do not remove the flag merely because an unrelated issue entered the project.
Only feedback or defects linked to the PR's behavior invalidate its readiness.

## Restore the flag

After a fix or rerun, refresh the PR rather than relying on cached state. Restore
the flag only when every condition above holds for the current head. Never carry a
prior human approval across an expected code change when repository policy
requires approval of the final commit.
