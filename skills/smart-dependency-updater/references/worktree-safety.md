# Dependency Worktree Safety

Read this reference before creating, adopting, writing in, staging from,
committing in, pushing from, or removing a dependency-update worktree.

## Identify the Checkout

For each PR group, record run-locally:

- repository identity from `git rev-parse --path-format=absolute
  --git-common-dir` and absolute root from `git rev-parse --path-format=absolute
  --show-toplevel`;
- expected branch or detached commit, refreshed base reference, dependency group,
  and proposed worktree path;
- classification as primary checkout, user-created worktree, harness-managed
  worktree, or worktree created by this update run;
- cleanup ownership. Only a worktree created by this run is owned for cleanup.

Do not persist a private receipt. Treat any pre-existing linked worktree as
foreign unless the host identifies it as the task's managed checkout.

## Preflight Every Group

1. Inspect `git worktree list --porcelain`, relevant local and remote refs, the
   proposed absolute path, and staged and unstaged status. Refuse path or branch
   collisions; never overwrite or reuse by name resemblance.
2. Do not stash, reset, discard, or commit foreign changes. Reuse a clean,
   suitable harness-managed worktree instead of nesting another worktree. Stop
   when unrelated state cannot be isolated.
3. Before the first manifest or lockfile write and after resume or handoff,
   compare repository identity, absolute root, registered worktree entry, and
   expected branch or commit with the receipt. Stop on mismatch before editing,
   install commands, validation that writes, staging, commit, push, or cleanup.
4. Use `git -C <absolute-root>` for Git and set an explicit working directory for
   package-manager, validation, generation, and research commands. Carry the
   recorded absolute values into every tool call; do not assume `cd` or shell
   variables persist.

## Preserve the PR Group Boundary

- Keep one branch and worktree per declared dependency group.
- Stage explicit group paths and inspect the staged filename list and staged
  diff before every commit. Do not use `git add .`, `git add -A`, or
  `git commit -a` around mixed state.
- Own a shared lockfile or generated file only when a repository-native command
  run in this group's verified root produced it and the whole diff tells this
  group's dependency story.
- If another group appears in the lockfile diff, narrow and rerun the owning
  package-manager command. If unavoidable, serialize after the earlier group,
  regenerate from the new base, or split coherent lockfile/tooling work. Never
  hand-delete unrelated lock entries.
- Never rewrite remote history unless the exact operation is documented by this
  skill and authorized for the current group.

## Clean Up Conservatively

Automatically remove only a clean, registered worktree that this run created
for the recorded dependency group. Immediately recheck repository identity,
absolute path, expected branch or commit, and status before removal.

Never force-remove a dirty, moved, mismatched, user-created, or harness-managed
worktree. Leave its worktree and branch intact and report the expected and
observed state plus the narrow manual action that would be required. Require
separate user authority for destructive cleanup or branch deletion.
