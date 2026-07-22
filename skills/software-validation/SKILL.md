---
name: software-validation
description: >-
  Discover, execute, and report existing repository-native software checks.
  Use when asked to validate a change, verify repository or package health, run
  the applicable typecheck, static analysis, lint, format, test, build, package,
  documentation, doctest, link, generated-reference, or example checks, or
  explain what validation evidence is still missing. Do not use to invent or
  install tooling, design new tests, choose architecture quality targets,
  prioritize repository improvements, or orchestrate delivery.
---

# Software Validation

Establish what the repository already treats as valid, run the smallest
applicable check surface safely, and report both evidence and gaps. A green
command proves only what that command observes.

## Core Contract

- Discover commands from repository evidence; never substitute ecosystem habit
  for an established command.
- Do not silently install or upgrade a runtime, SDK, compiler, dependency,
  linter, formatter, test runner, documentation generator, or package manager.
- Preserve unrelated working state. Treat every check as potentially
  write-producing and report validation-generated files or diffs.
- Execute each planned command once. A single transparent sequential recovery
  attempt is allowed only after a parallel workspace race is stopped and cleanup
  is confirmed; report both attempts.
- Give every applicable category an explicit terminal state only after its
  process tree has ended; keep skipped, still-running, or missing evidence
  visible.

## Workflow

1. Read scoped `AGENTS.md`, `CLAUDE.md`, repository instructions, and the user's
   requested validation boundary. Resolve the canonical repository root,
   relevant package or workspace, changed contract, and current dirty and staged
   state before running anything.
2. Read [Command discovery](references/command-discovery.md). Build a deduplicated
   plan from instructions, CI, task runners, manifests, contributor docs,
   package conventions, and recent successful CI usage, in that order.
3. For every applicable category, record the exact command, working directory,
   package or workspace scope, evidence source, covered subchecks, prerequisites,
   timeout rationale, and shared caches or generated outputs. Mark a category
   `SKIPPED (<reason>)` when no safe established command exists.
4. Choose the smallest scope that observes the changed contract. Prefer focused
   checks before broader checks, but preserve a repository-mandated combined or
   top-level command. Do not run covered subcommands again merely to make the
   report look complete.
5. Read [Execution and reporting](references/execution-and-reporting.md). Run
   independent commands in parallel only when the harness, process isolation,
   caches, generated files, and repository guidance make that safe; otherwise
   run sequentially and state why.
6. Recheck working state after execution. Preserve and identify unrelated
   changes, validation-generated changes, remaining processes, skipped
   prerequisites, and evidence gaps.
7. Return exact commands, scopes, states, decisive diagnostics, warnings, and
   one honest summary. Do not equate all-green established checks with proof of
   an untested behavior.

## Result States

Use exactly one state for each applicable category:

- `PASSED` — the established command completed successfully.
- `FAILED` — the established command and its descendants ended with an
  unsuccessful exit status. Report actionable diagnostics when available and
  say explicitly when the command exposed none.
- `SKIPPED (<reason>)` — no safe command or prerequisite was available, or the
  authorized mode excluded or cancelled the category before evidence completed.
- `TIMEOUT` — the bound was exceeded and the relevant process tree was
  confirmed stopped and reaped.

A skip does not automatically fail the whole validation, but it remains an
explicit evidence gap. A command can pass while producing warnings or workspace
changes; report both. When termination is unconfirmed, report the interim marker
`TERMINATION_UNCONFIRMED`, keep monitoring or escalate process control, and do
not finalize the affected category or dependent checks.

## Safety and Boundaries

- Use explicit working directories for every command. In monorepos, preserve
  package or workspace scope and do not launch competing top-level orchestrators.
- Do not expose secrets in commands or output. Treat network, service,
  credential, device, and production prerequisites as unavailable unless the
  repository establishes the check and the user and harness authorize access.
- Do not stash, reset, clean, discard, commit, or absorb user changes. Never
  delete generated output merely to make the post-validation diff clean.
- Do not claim timeout cleanup while descendants may still be running. Stop the
  affected validation flow when process-tree state is uncertain.
- Route new, missing, or restructured non-frontend test evidence and test
  discovery, collection, runner, or framework diagnosis and repair to
  `software-testing`; route browser test design to `effective-web`.
- Route system quality targets and broader verification strategy to
  `software-architecture`; repository audit prioritization to
  `codebase-improvement`; documentation authoring to `tech-docs`; and
  orchestration, commits, pull requests, approvals, and merge judgment to the
  calling delivery skill or `pr-review`.

This skill owns discovery and execution of checks the repository already has.
It does not become the build system, CI service, package manager, test designer,
or delivery orchestrator.
