# Execution and Reporting

Run the discovered plan without losing working state, process ownership, or
evidence about what did not run.

## Preflight

Before the first command:

- capture the repository root, relevant package roots, current branch or commit,
  and `git status --short`, including staged and untracked paths;
- classify known user changes and pre-existing generated output without
  modifying them;
- record the exact command, explicit working directory, timeout rationale,
  prerequisites, likely writes, and expected process-tree controls;
- verify required executables are already available without installing them.

If the baseline is too dirty to attribute validation-generated changes safely,
run only checks whose output is isolated or mark the affected categories
`SKIPPED (dirty baseline prevents safe output attribution)`.

## Execute Proportionately

1. Run narrow established checks before broader ones when failure attribution
   improves and repository policy does not require one combined gate.
2. Execute each planned command exactly once with captured stdout, stderr, exit
   status, duration, and scope. Avoid shell wrappers that hide the real exit
   status or spawn unmanaged background work.
3. Select a bounded timeout from repository history, CI limits, task size, cold
   versus warm execution, and harness constraints. Do not prescribe one global
   duration.
4. Parallelize only commands with independent process trees and no shared cache,
   daemon, output directory, generated file, database, port, lock, or task
   orchestrator. Otherwise serialize and record the safety reason.

## Races, Timeouts, and Cancellation

If parallel checks race through shared state:

1. Stop the affected commands and their descendants using harness-supported
   process-group or tree controls.
2. Confirm every affected process has exited and inspect workspace changes.
3. Preserve and report generated or ambiguous output; do not clean it blindly.
4. Retry the commands sequentially at most once only when cleanup and ownership
   are confirmed. Report the initial race and recovery attempt separately.

On deadline or cancellation, terminate and reap the relevant process tree. Use
`TIMEOUT` only after confirming descendants are stopped. If termination cannot
be verified, emit an interim `TERMINATION_UNCONFIRMED` diagnostic, stop dependent
checks, and continue monitoring or escalate process control. Do not assign a
final result state or present the run as terminally clean while descendants may
still be active. After user or harness cancellation is confirmed clean, use
`SKIPPED (cancelled before completion)` because no validation result completed;
reserve `TIMEOUT` for an exceeded bound.

## Attribute Workspace Changes

After every write-producing command and at the end:

- compare current status with the baseline;
- distinguish pre-existing paths from newly changed or untracked paths;
- identify the command most likely to have produced each new path, without
  claiming certainty when parallel work made attribution ambiguous;
- preserve all changes. Do not reset, restore, stash, clean, commit, or delete
  them as part of validation.

An unexpected source, lockfile, snapshot, generated reference, or config diff is
validation evidence even when the command exits zero.

## Result Shape

Start with a compact matrix:

| Category | State | Command and scope | Evidence source | Duration | Key result |
| --- | --- | --- | --- | --- | --- |
| Typecheck, lint, tests, build, docs, or repository gate | `PASSED`, `FAILED`, `SKIPPED (...)`, or `TIMEOUT` | Exact invocation and root/package | CI, task, manifest, or instruction | Observed or not run | Diagnostic, warning, or gap |

If process termination is unconfirmed, return an interim process-control alert
instead of this final matrix for affected or dependent categories.

Then report:

1. decisive diagnostics with file, line, package, target, or task when available;
2. warnings that do not change the command state;
3. skipped prerequisites and why they were not installed or activated;
4. validation-generated files or diffs and preserved unrelated dirty state;
5. process cleanup evidence for timeouts, cancellations, or race recovery;
6. remaining evidence gaps and the limits of the green checks.

Do not collapse skipped categories, warnings, generated diffs, or cleanup
uncertainty into a single green summary.
