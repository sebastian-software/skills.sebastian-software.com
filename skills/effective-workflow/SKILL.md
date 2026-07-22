---
name: effective-workflow
description: >-
  Coordinate multi-stage or mixed-domain software work from an unclear request
  through an authorized change, focused verification, and a review-ready
  handoff. Use when a task spans diagnosis, implementation, validation, review,
  or delivery and needs sequencing across repository-native workflows and
  first-party specialist skills. Prefer the matching specialist directly for
  an already narrow documentation, dependency, test, review, architecture,
  port, or frontend request.
---

# Effective Workflow

Coordinate the path from intent to evidence. Let repository instructions and
specialist skills own how the work is done; own what should happen next, which
authority applies, and what must be true before completion.

## Start from the Host and Repository

1. Inspect the repository instructions, current state, relevant artifacts, and
   available skills or tools before choosing a workflow.
2. Restate the requested outcome, material constraints, and authorized scope.
   Infer routine details from local evidence; ask only when a missing choice
   would materially change the result or authority.
3. Preserve unrelated work and repository-native conventions. Do not create an
   Effective Workflow config, hidden directory, plan store, label system, role
   registry, or status marker.
4. Keep analysis-only requests read-only. Treat diagnosis, implementation, and
   delivery as separate authority levels even when the likely fix is obvious.

## Select the Smallest Route

Classify the immediate need before acting:

- answer or explain: inspect enough evidence and report without mutation;
- diagnose: reproduce or trace the cause, then stop unless a fix is authorized;
- plan: use the repository's existing issue, plan, or decision conventions;
- build or fix: implement the narrowest authorized behavior change;
- refactor: establish a before baseline, preserve behavior, and compare after;
- documentation, dependency update, port, architecture, test, or review: hand
  specialist judgment to the matching owner;
- deliver: commit, push, open a pull request, update a tracker, deploy, or merge
  only when the user already authorized that external mutation.

When ownership spans more than one domain or an optional skill may be missing,
read [Routing and selective installation](references/routing-and-fallbacks.md).
Load only the owners needed for the current stage; do not preload the catalog.

## Work from Understand to Deliver

### 1. Understand

- Identify the observable outcome and acceptance evidence, not merely the
  requested file edit.
- Inspect before proposing. For a defect, separate symptom, reproduction,
  likely cause, and confidence. For an unclear feature, resolve only the choices
  that block a safe implementation.
- Decide whether a saved plan is useful. Use one for multi-step or risky work
  when the repository or user calls for it; skip it for a small, clear change.
- Establish a relevant before baseline for behavior-preserving work. Record an
  already-red baseline instead of attributing old failures to the new change.

### 2. Change

- Invoke the appropriate first-party owner when available and treat its domain
  rules as authoritative. Pass it the outcome, scope, repository evidence,
  constraints, and expected handoff.
- Implement only the agreed surface. Do not expand a fix into cleanup, a docs
  task into product behavior, or a dependency update into unrelated migration.
- Follow repository-native files, commands, branches, issues, tests, and docs.
  Never require a project to adopt this skill's internal mechanics.
- If an owner is unavailable, use the selective-install contract rather than
  recreating that owner's handbook inside this workflow.

### 3. Verify

- Match evidence to the claim: reproduce and guard a bug, compare a refactor
  baseline, exercise a feature's acceptance path, validate documentation
  examples and links, or check dependency and port compatibility.
- Use `software-validation` when available to discover, deduplicate, execute,
  and report the repository's established check surface; keep specialist owners
  responsible for designing any new evidence the change requires.
- Run the narrow check first, then the relevant established repository checks.
  Review the changed surface in proportion to user impact, reversibility,
  security, data, concurrency, and release risk.
- Distinguish new failures from pre-existing failures. Report skipped checks,
  missing credentials, unavailable services, and remaining uncertainty.

Read [Evidence and delivery](references/evidence-and-delivery.md) when choosing a
baseline, review depth, or completion proof.

### 4. Deliver

- Leave the working state understandable and review-ready even when no external
  delivery action was authorized.
- Before any commit or remote mutation, recheck the diff, unrelated work, target
  repository, branch, and requested completion action.
- When a specialist creates or adopts a worktree, require that independently
  installed owner to apply its local repository, location, staging, resume, and
  cleanup safety contract. Do not substitute an orchestrator-owned ledger.
- Use the host's available Git, forge, CI, and review capabilities. Do not assume
  every harness can push, comment, resolve threads, merge, or deploy.
- Finish with a concise handoff: outcome, important files or behavior, evidence
  run, skipped or failing checks, delivery state, and remaining risk.

## Keep the Orchestrator Lean

- Keep this `SKILL.md` below 200 lines and the runtime surface to at most two
  directly linked references, each below 120 lines. Treat exceeding a cap as a
  design-review trigger, not permission to add another manual.
- Keep a specialist route to a short selection rule and handoff contract. Move
  no frontend, testing, documentation, dependency, architecture, port, product,
  legal, language, or PR-review checklist into this skill.
- Add no setup scripts, generated distribution, fixed commands, internal memory,
  caches, counters, locks, or automatic tracker mutations.
- Prefer normal-language intent over a separate command vocabulary.

## Completion Standard

Call the work complete only when the authorized outcome is present, relevant
evidence supports it, the changed surface has been reviewed at the right depth,
and the handoff says what was done, skipped, or remains. Do not equate a clean
diff, a passing narrow test, a created pull request, or an available delivery
tool with completion by itself.
