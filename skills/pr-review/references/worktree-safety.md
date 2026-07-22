# PR Maintenance Worktree Safety

Read this reference before Mode B creates, adopts, writes in, stages from,
commits in, pushes from, or removes a worktree.

## Establish a Run-Local Receipt

Use Git metadata rather than similar-looking paths. Record in the current run:

- canonical repository identity from `git rev-parse --path-format=absolute
  --git-common-dir`;
- absolute worktree root from `git rev-parse --path-format=absolute
  --show-toplevel`;
- expected detached commit or branch, PR head, and base reference;
- whether the checkout is the primary checkout, a pre-existing user worktree, a
  harness-managed worktree, or a worktree created for this PR maintenance run;
- cleanup ownership. Only the last class is workflow-owned.

Treat a pre-existing linked checkout as foreign unless the host identifies it
as harness-managed for this task. Keep the receipt in run context; do not create
a private ledger or hidden runtime directory.

## Preflight and Revalidation

1. Inspect `git worktree list --porcelain`, local and remote branch refs, the
   proposed absolute path, and `git status --short` before creating or adopting
   a worktree. Refuse branch or path collisions.
2. Preserve dirty and staged state. Never stash, reset, overwrite, or absorb it.
   Use a clean isolated worktree when possible; stop when foreign state cannot
   be separated safely.
3. Reuse a suitable linked or harness-managed worktree instead of nesting a new
   one. Never claim cleanup ownership for a checkout the workflow did not
   create.
4. Immediately before the first write and after any resume or handoff, compare
   the repository identity, absolute root, registered worktree entry, and
   expected branch or detached commit with the receipt. Stop on any mismatch.
5. Run Git commands with `git -C <absolute-root>` and every other command with
   an explicit tool working directory. Do not rely on a previous `cd` or on
   shell variables surviving another tool call; carry the recorded absolute
   values into each command.

## Stage and Deliver One PR Unit

- Scope the worktree to the one PR head named in the receipt.
- Stage explicit paths with `git -C <root> add -- <paths>`. Avoid `git add .`,
  `git add -A`, and `git commit -a` whenever other changes could exist.
- Inspect both `git -C <root> diff --cached --name-only` and `git -C <root>
  diff --cached` before committing. Stop if staged state contains foreign work.
- Treat a shared lockfile or generated file as owned only when the current PR's
  repository-native command produced it and the complete diff belongs to the
  PR's declared purpose.
- Immediately before a run-owned commit, revalidate that `HEAD` still equals
  the receipt's expected commit and that detached-versus-branch state still
  matches. Record the full staged tree ID after inspecting the staged diff.
  After the commit succeeds, advance the receipt to the new commit only when its
  parent is that expected commit and its complete tree equals the recorded
  staged tree. This explicit transition is the only way the workflow may change
  the receipt's expected commit; an arbitrary HEAD move remains foreign and
  blocks push or cleanup.
- Do not rewrite remote history except for the skill's explicitly allowed,
  user-authorized rebase flow on the user's own PR branch. Revalidate review and
  branch state after the push.

## Clean Up Conservatively

Remove a worktree automatically only when the receipt says this run created it
for this PR. Immediately before removal, verify the same repository, registered
absolute path, latest run-owned expected branch or detached commit, and a clean
status. For a detached receipt, also prove that `HEAD` has not become attached
to a branch even when the commit OID is unchanged.

Never use force removal for automatic cleanup. Leave a dirty, moved,
mismatched, user-created, or harness-managed worktree and its branch intact;
report the exact path, observed state, expected state, and safest next action.
Require separate user authority for destructive cleanup or branch deletion.
