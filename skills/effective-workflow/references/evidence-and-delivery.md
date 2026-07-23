# Evidence and Delivery

Read this reference only when selecting a before baseline, verification scope,
review depth, or authorized delivery action.

## Match Evidence to the Change

| Change type | Before or negative proof | Completion evidence |
| --- | --- | --- |
| Bug fix | Reproduce the symptom or demonstrate the broken invariant | Regression guard fails for the old behavior and passes with the fix, plus relevant checks |
| Behavior-preserving refactor | Record focused tests, lint, types, build, output, or performance baseline | Compare the same evidence after the change and explain intentional deviations |
| Feature | Establish the previous absence and acceptance criteria | Exercise the smallest user-visible or contract path that proves the outcome |
| Documentation | Identify the stale, missing, or misleading contract | Validate links, commands, examples, generated output, or implementation agreement as applicable |
| Dependency update | Record current versions and relevant green or already-red checks | Verify upstream compatibility, adapted call sites, lock state, and affected checks |
| Port or migration | Define the source behavior and compatibility envelope | Compare representative outputs, edge cases, performance targets, and integration behavior |

Do not manufacture a failing test when an equivalent observable reproduction is
safer or clearer. Do not delete sound implementation merely to reenact test-first
ordering.

## Choose Validation and Review Depth

1. Run the narrowest discriminating check first.
2. Run the repository's relevant lint, type, test, build, documentation, or
   packaging checks for the touched surface.
3. Increase review depth for authentication, authorization, secrets, payments,
   personal or destructive data, migrations, concurrency, public compatibility,
   deployment, and hard-to-reverse behavior.
4. Inspect the final diff for accidental files, debug output, generated churn,
   missing docs, and unrelated user work.
5. Separate failures introduced by the change from baseline failures and
   environmental limitations.

## Apply Delivery Authority Literally

Treat these as distinct mutations: stage, commit, create or switch a branch,
push, open or edit a pull request, comment or resolve review threads, update an
issue, deploy, release, and merge. Permission for one does not imply all later
actions unless the requested workflow clearly includes them.

Before a remote action, resolve the exact repository, branch, base, pull request,
tracker item, environment, or release target with a read-only check. Use the
host's recovery and approval mechanisms for destructive or privileged actions.

## Write an Intentional Commit Message

Before committing, inspect the repository's documented contribution rules and
recent accepted history. Follow that established syntax and language when it is
coherent. Use Conventional Commits as the fallback when the repository has no
clear convention:

```text
type(optional-scope): imperative outcome
```

Choose a recognized type such as `feat`, `fix`, `docs`, `refactor`, `test`,
`build`, `ci`, or `chore` from the actual change. Keep the subject specific
enough to distinguish the commit in a log. If the subject needs “and” to join
two independently reversible outcomes, reconsider the staging boundary instead
of hiding multiple changes in one message.

Add a body when the reason, constraint, migration, security consequence, or
behavior change is not recoverable from the subject and diff. Mark breaking
changes and reverts using the repository's convention, and name relevant issue
or migration context when it will remain useful. Do not add AI attribution,
generated-by trailers, emojis, or release tokens unless the repository, host
platform, or user explicitly requires them.

Derive the message from the staged diff, not from the original request or the
whole worktree. Do not use `chore` as a generic escape hatch for a user-visible
fix, feature, or documentation change.

## Produce a Review-Ready Handoff

Report:

- the achieved outcome and meaningful behavior change;
- the important files, decisions, or boundaries touched;
- the focused and broader checks run, with their results;
- skipped checks, pre-existing failures, missing credentials, and uncertainty;
- the branch, commit, pull request, tracker, deployment, or merge state when an
  authorized delivery action occurred;
- the smallest remaining next step, or state clearly that none remains.
