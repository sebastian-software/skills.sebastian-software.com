# Command Discovery

Build the validation plan from repository evidence. Do not guess a command
because it is common in the ecosystem.

## Evidence Order

Inspect in this order and record the source for every selected command:

1. Scoped `AGENTS.md`, `CLAUDE.md`, and explicit repository instructions.
2. CI workflows and established task-runner configuration.
3. Manifests, lockfiles, workspace definitions, and declared scripts or tasks.
4. Contribution, development, release, and package documentation.
5. Nearby package conventions and recent successful CI usage.

Resolve conflicts in favor of the more scoped authoritative instruction and the
current executable repository state. A stale README command is evidence to
investigate, not permission to repair documentation during validation.

## Map the Applicable Surface

Consider only categories relevant to the changed or requested contract:

- type checking and static analysis;
- linting and formatting verification;
- existing focused and broader tests;
- build, compile, bundle, package, or publish-dry-run validation;
- documentation build, doctest, links, generated references, and examples;
- repository-defined combined quality or verification gates.

For each category, record:

| Field | Required evidence |
| --- | --- |
| Command | Exact established invocation, without invented flags |
| Root | Explicit repository, workspace, or package working directory |
| Scope | Files, package, workspace, target, or full repository observed |
| Source | Instruction, CI job, task definition, manifest, or current docs |
| Coverage | Other categories or subcommands already included |
| Prerequisites | Installed tools, generated inputs, network, credentials, services |
| Writes | Caches, coverage, build output, generated docs, lockfiles, snapshots |

## Deduplicate Instead of Expanding

- Prefer an established combined quality command when repository evidence says
  it is the canonical gate. Do not additionally run each covered lint, test,
  typecheck, or build command.
- Report the combined gate once, then map category states only from subchecks the
  task proves actually ran. If the gate stops early, later covered categories
  are `SKIPPED (combined gate stopped before this subcheck)`, not fabricated
  failures or passes.
- If a failed combined gate does not expose which subchecks ran, keep the gate
  `FAILED` and mark each unobservable category `SKIPPED (combined gate did not
  expose subcheck execution)`. Do not infer category failure or success from the
  aggregate exit alone.
- When a combined command is too broad for the requested scope, use a narrower
  established package task only when it still observes the changed contract.
- Do not translate a CI matrix into simultaneous local top-level orchestrators.
  Preserve the task runner's dependency graph and concurrency controls.
- Do not run the same command at root and package level unless repository
  evidence establishes that they observe different required contracts.

## Monorepos and Workspaces

Identify the owning package and affected dependents from workspace definitions,
task graphs, import or dependency edges, and repository instructions. Prefer:

1. the package's established focused check;
2. required dependent or integration checks;
3. the canonical top-level gate when repository policy requires it.

Use the repository's filter, selector, project, target, or package syntax
exactly as declared. Do not invent workspace flags. Never launch multiple root
orchestrators that compete over the same task graph, cache, daemon, generated
directory, or lockfile.

## Missing Commands and Prerequisites

When the evidence does not establish a safe command, report the category as
`SKIPPED` with the concrete gap, such as:

- no declared lint task or CI job;
- documented command references a missing script;
- required runtime or tool is absent;
- command requires unavailable credentials, service, device, or network;
- requested package is outside the discovered workspace;
- only a write-mode formatter exists and formatting changes were not authorized.

Do not install, initialize, authenticate, start external infrastructure, or
invent a replacement command to turn a visible gap into a synthetic pass.
