---
name: effective-workflow
description: >-
  Coordinate multi-stage, mixed-domain, or multi-agent software work from an
  unclear request through an authorized change, focused verification, and a
  review-ready handoff. Use when a task spans diagnosis, implementation,
  validation, review, or delivery and needs proactive decomposition,
  ambiguity reduction, capability- and cost-aware delegation, or sequencing
  across repository-native workflows and first-party specialist skills. Prefer
  the matching specialist directly for an already narrow documentation,
  dependency, test, review, architecture, port, or frontend request.
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

## Prefer the Smallest Sufficient Change

Minimize only after understanding the requested behavior and tracing the owning
flow. Before adding new code, configuration, abstraction, or dependencies,
check in this order:

1. the work is necessary for the accepted outcome;
2. an established repository pattern or implementation already owns it;
3. the language standard library or native platform covers it;
4. an already-installed dependency covers it without distorting the design;
5. otherwise, add the smallest cohesive implementation at the owning seam.

The shortest diff is not the goal when it patches a symptom, hides risk, or
pushes complexity into callers. Never simplify away trust-boundary validation,
data-loss protection, security, accessibility, required compatibility, useful
error handling, or evidence proportionate to the change.

When plausible paths materially differ in public behavior, data, authority,
operational cost, reversibility, or scope, present the smallest useful set of
options with tradeoffs and a recommendation. Ask for the decision only when it
changes the authorized outcome. For ordinary reversible choices, follow the
repository's conventional path and proceed.

If a deliberate shortcut has a real ceiling, record the ceiling and the
observable trigger for revisiting it in the repository's normal comment,
issue, or decision convention. Do not add a skill-specific debt marker.

## Work from Understand to Deliver

### 1. Understand

- Identify the observable outcome and acceptance evidence, not merely the
  requested file edit.
- Inspect before proposing. For a defect, separate symptom, reproduction,
  likely cause, and confidence. For an unclear feature, resolve only the choices
  that block a safe implementation.
- Decide whether a saved plan is useful. Use one for multi-step or risky work
  when the repository or user calls for it; skip it for a small, clear change.
- Before delegation or mutation, challenge ambiguity that could change
  behavior, data, security, compatibility, scope, or acceptance. Resolve routine
  details from repository evidence; when credible interpretations materially
  diverge, present them with consequences and obtain the owning decision.
- For nontrivial work, identify decisions that unblock later work, independent
  investigations, shared-state collisions, objective evidence, and the critical
  path. Do not wait for the caller to partition work agents can organize.
- Establish a relevant before baseline for behavior-preserving work. Record an
  already-red baseline instead of attributing old failures to the new change.

### 2. Change

- Invoke the appropriate first-party owner when available and treat its domain
  rules as authoritative. Pass it the outcome, scope, repository evidence,
  constraints, and expected handoff.
- When an agent will produce production code, keep the accountable human or
  owning team responsible for the problem, material architecture, data,
  security, compatibility, and acceptance choices. Resolve consequential
  choices before generation.
- For ambiguity-heavy or high-impact work, require a reviewable implementation
  plan before mutation and compare it with the accepted outcome, exclusions,
  repository constraints, and evidence plan. Keep this gate proportionate.
- Shape nontrivial work into a dependency graph and active parallel front. Read
  [Routing and selective installation](references/routing-and-fallbacks.md)
  for work-graph, model-selection, and delegation contracts.
- When model or agent selection exists, match each item to ambiguity, impact,
  context breadth, repetition, objective verifiability, cost, and latency. Use
  the strongest suitable capability for consequential judgment and the least
  costly sufficient worker for bounded execution. Never invent tiers.
- Limit parallel work by independence, state isolation, integration and review
  capacity, slots, and budget. Integrate each completed front, then update the
  graph; keep tightly coupled judgment in one context.
- Give delegated work a compact outcome, authority, evidence, and return
  contract. Prefer result and blocker over process narration.
- Treat delegated authority, isolation, and tool limits as enforceable
  contracts. Stop or disclose the downgrade and request a decision when the
  runtime cannot honor them; never continue silently with broader capability.
- Do not let delegation volume, speed, or price weaken authority, evidence,
  safety, or the integrator's ability to judge the combined work.
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
- Treat generated code, agent confidence, and plan conformance as inputs, not
  completion evidence. Verify behavior, failure modes, and repository
  integration independently of who or what wrote the change.
- Use `software-validation` when available to discover, deduplicate, execute,
  and report the repository's established check surface; keep specialist owners
  responsible for designing any new evidence the change requires.
- Run the narrow check first, then the relevant established repository checks.
  Review the changed surface in proportion to user impact, reversibility,
  security, data, concurrency, and release risk.
- Run a subtraction pass over the final diff: remove speculative files,
  dependencies, configuration, wrappers, duplicated behavior, and options that
  do not serve the accepted outcome. Preserve every requirement and safeguard.
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

## Routing Boundaries

- Route domain-specific implementation, evidence design, and durable decisions
  to the selected specialist skill; this skill only coordinates the handoff.
- Do not use this skill to invent repository workflow, delivery authority, or
  project-specific policy absent from the host repository or user request.
