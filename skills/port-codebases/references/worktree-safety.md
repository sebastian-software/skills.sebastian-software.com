# Port Shard Worktree Safety

Read this reference whenever a port profile creates, adopts, writes in, stages
from, commits in, integrates from, or removes a Git worktree.

## Record Shard Location and Ownership

Keep a run-local receipt for each shard containing:

- canonical repository identity from `git rev-parse --path-format=absolute
  --git-common-dir`, absolute worktree root, and registered worktree entry;
- expected branch or detached commit, integration base, migration-contract
  slice, and exclusively owned files;
- checkout class: primary, user-created, harness-managed, or created by this
  port run;
- cleanup ownership. Only the final class is eligible for automatic removal.

Do not create a hidden state directory or mandatory receipt file. Treat a
pre-existing worktree as foreign unless the host identifies it as managed for
the current shard.

## Verify Before Work

1. Inspect all registered worktrees, relevant branches, the proposed absolute
   path, and dirty and staged state before assigning a shard. Refuse branch,
   path, or file-ownership collisions.
2. Reuse a suitable harness-managed worktree rather than nesting a new one.
   Never stash, reset, overwrite, or absorb unrelated state.
3. Before the first write and after resume, delegation, or handoff, recheck the
   repository identity, absolute root, registered path, expected branch or
   commit, and shard ownership. Stop before editing, writing validation,
   staging, committing, integration, push, or cleanup on any mismatch.
4. Use `git -C <absolute-root>` for Git and an explicit tool working directory
   for compilers, generators, tests, formatters, and other commands. Carry the
   recorded absolute values into every tool call; do not assume `cd` or shell
   variables persist.

## Keep the Shard Isolated

- Stage only the shard's declared files; avoid `git add .`, `git add -A`, and
  `git commit -a` around shared state.
- Inspect staged filenames and the full staged diff before every checkpoint or
  commit. Foreign staged work blocks delivery until isolated.
- Assign shared manifests, lockfiles, generated indexes, or build metadata to
  one integration owner. Own their diff only when the repository-native command
  for the current integration unit produced a coherent result.
- Do not let a shard rewrite remote history or perform destructive shared-state
  operations without explicit workflow and user authority.

## Remove Only What the Run Owns

Immediately before automatic removal, prove that this port run created the
worktree for the recorded shard and that repository identity, registered path,
branch or commit, and clean status still match.

Never force-remove a dirty, moved, mismatched, user-created, or harness-managed
worktree. Leave the worktree and branch intact and report the exact discrepancy
to the integration owner. Require separate user authority for destructive
cleanup or branch deletion.
