# Routing and Selective Installation

Read this reference only when the task needs a specialist route, spans several
owners, or the preferred owner may not be installed.

## Ownership Map

| Primary need | Authoritative first-party owner | Handoff focus |
| --- | --- | --- |
| Repository investigation, audit, prioritization, or implementation plan | the audit route | Evidence, leverage, scope, and executable next move |
| Browser-facing product work | `effective-web` | UX, implementation, accessibility, performance, and browser evidence |
| Non-frontend test design or regression evidence | `effective-engineering` | Observable risk, suitable test boundary, and discrimination |
| Existing repository-native check execution | the validation route | Exact commands, scope, states, generated changes, and evidence gaps |
| Technical documentation | the docs route | Audience, repository-native surface, examples, and verification |
| Dependency selection, introduction, or update | the dependencies route | Current upstream evidence, compatibility, native package-manager changes, and validation |
| Pull-request review or review follow-through | the review route | Impact-led findings, thread state, CI, and merge judgment |
| System boundary or evolutionary architecture | `effective-engineering` | Drivers, quality scenarios, tradeoffs, operability, and migration |
| Durable cross-functional decision | `effective-product` | Repository-native ADR lifecycle and drift control |
| Port or compatibility migration | the porting route | Behavior contract, parity evidence, execution profile, and handoff |
| Product, design, legal, locale, or communication concern | `effective-product`, `effective-product`, `effective-web`, `effective-writing`, or the matching communication owner | Domain outcome and evidence without expanding orchestration |

The orchestrator selects and sequences owners. Each owner controls its own
analysis, implementation guidance, evidence standard, and domain boundaries.

## Route Mixed Repositories by Owned Surface

1. Classify each affected file or coherent domain independently. Do not infer
   one route for the repository from its first manifest or language.
2. Exclude generated, vendored, cached, and build output from direct editing by
   default. Change the owning source, generator, or documented update mechanism.
3. Treat CI, release, container, manifest, lockfile, formatter, and repository
   metadata as tooling even when they use a product language. Do not treat
   unmatched product code as tooling merely because no specialist is installed.
4. Partition a mixed change across its real owners. Preserve recognized web,
   documentation, dependency, test, architecture, port, and review boundaries;
   use a repository-led fallback for clearly identified unsupported product
   code and disclose materially reduced language-specific depth.
5. Parallelize only owner scopes with cleanly separable files, state, and
   validation surfaces. Otherwise sequence them explicitly.

## Design the Work Graph Before Assigning Owners

1. Represent consequential decisions, investigations, implementation units,
   integration, and evidence as work items. Add prerequisite, ambiguity, and
   shared-state edges instead of treating a checklist as automatically parallel.
2. Identify the critical path and current parallel front: items whose inputs
   are ready and whose state, authority, and evidence surfaces do not conflict.
3. Classify each item by ambiguity, impact, context breadth, repetition,
   objective verifiability, cost, and latency. Keep synthesis with one integrator.
4. When choices exist, assign the strongest suitable model to consequential
   judgment and the least costly sufficient model to bounded, reversible,
   objectively checked execution. Never weaken evidence or safety for price.
5. Bound parallelism by ready independent items, enforceable isolation,
   integration and review capacity, runtime slots, and budget. More workers are
   harmful when their output cannot be judged or merged safely.
6. After each front, integrate evidence, resolve contradictions, and update the
   graph before launching dependent work.

## Give Delegation a Compact Return Contract

Delegate only when a bounded owner can work independently and the returned
evidence is worth the coordination cost. Keep a one-line lookup, a tightly
coupled decision, or work that needs continuous shared judgment in the caller.

Every delegated task should state:

- the result or question, authorized scope, and important exclusions;
- the minimum repository evidence or context needed to work safely;
- whether the task may read, edit, validate, or only recommend;
- the expected return shape and terminal states; and
- what uncertainty must stop the task rather than invite improvisation.

Prefer compact, task-specific receipts:

- location work: `path:line`, exact symbol, and relevance;
- implementation work: changed paths, behavior, focused verification, blocker;
- review work: impact, location, evidence, and smallest credible correction;
- research work: conclusion, primary source, revision or date, and uncertainty.

Use one owner for one bounded result. Bound fan-out, recursion, turns, and
returned context to the smallest shape that shortens the critical path without
overloading integration.

Preserve the complete receipt or artifact when the parent summary omits detail.
Treat declared read-only access, worktree isolation, and tool limits as
contracts. If the runtime cannot enforce one, stop or disclose the downgrade
and request a decision rather than silently continuing with broader authority.

Return the outcome, decisive evidence, and blocker rather than a diary of tool
calls or discarded searches. Keep identifiers, commands, errors, counts, and
paths exact; do not invent abbreviations merely to look terse. Use complete,
unambiguous prose for security, destructive actions, ordering constraints,
conflicting evidence, or any result a human must act on directly. The caller
owns synthesis into a readable user-facing answer.

## Selective-Install Contract

When an optional owner is unavailable:

1. Continue to honor repository instructions, user authority, evidence, and
   handoff requirements; these belong to the orchestrator.
2. Disclose the missing owner when its absence materially reduces confidence or
   depth. Do not turn every missing optional skill into noise.
3. Use a narrow, repository-led fallback when the work is low-risk and normal
   engineering reasoning is sufficient. Reuse local commands, patterns, tests,
   and documentation.
4. Ask for installation, a domain decision, or a focused handoff when the
   missing expertise is necessary for a high-risk or specialist claim.
5. Never recreate a condensed specialist handbook, invent unavailable tool
   behavior, or install a skill without authority.

Describe reduced depth in the final handoff, including what evidence still
supports the result and which domain-specific review remains useful.
