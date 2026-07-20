# Effective Flow capability inventory

- Audit date: 2026-07-20
- Status: Complete for the audited revision
- Source: [`sebastian-software/effective-flow`](https://github.com/sebastian-software/effective-flow)
  (private; access required)
- Audited revision: [`origin/develop@1cdd053`](https://github.com/sebastian-software/effective-flow/tree/1cdd0533c13ddcd9b2bf4205e2ddfecf152dc923), tagged `effective-flow-v1.48.0`
- Related issue: [#104](https://github.com/sebastian-software/skills.sebastian-software.com/issues/104)
- Decision: [ADR-0001](../adr/0001-distill-effective-flow-and-retire-the-standalone-system.md)

## Purpose

This audit treats Effective Flow as source material, not as a package that must
be preserved. It inventories the actual revision rather than relying on issue
prose, identifies independently useful capabilities, and records what should
happen to each part before any migration work starts.

The evaluation bar is deliberately asymmetric:

- A capability belongs in this collection only when it is useful independently
  of Effective Flow and has a clear owner, trigger, boundary, and verification
  story.
- Normal agent behavior such as editing code, running project checks, creating
  a commit, or using a worktree does not become a skill merely because Effective
  Flow wrapped it in a named workflow.
- New public skills must be directly installable from the repository through a
  standard skill manager. Platform-specific builds, generated delivery branches,
  custom installers, and fixed worker fleets need separate evidence of value.
- An existing first-party skill is preferred over a second copy of its domain
  guidance.
- Historical names do not determine future names. Any retained capability gets
  a descriptive collection-level name.

## Verified shape

At the audited revision, Effective Flow contains:

- one thin router and **17 public tools**;
- **6 internal tools**, including a three-way `apply` router and two
  `apply-review` support files;
- **13 custom workers** with separate Claude and Codex model, tool, and sandbox
  declarations;
- **27 shared instruction fragments**;
- 4,941 lines of tool instructions, 1,216 lines of worker instructions, and
  1,566 lines of shared fragments;
- a source-to-distribution compiler, transform library, generated Claude and
  Codex layouts, build guards, release automation, a generated default branch,
  release archives, and custom copy/symlink installers;
- a target-project configuration and runtime model spanning a living setup ADR,
  an `AGENTS.md` marker, `.effective-flow/` state, plan archives, review reports,
  remote tracker labels, and worktrees.

The source is already trying to delegate reusable expertise to this collection.
Its ownership document names `effective-web`, `smart-dependency-updater`,
`codebase-improvement`, `port-codebases`, `software-architecture`,
`decision-records`, `product-management`, and `product-design`. That is useful
evidence for distillation, but it also means much of the remaining system is
adapter and lifecycle machinery rather than unique domain expertise.

## Evidence boundary

This audit verifies what the source implements, where it already delegates to a
first-party owner, and whether a capability recurs outside its Effective Flow
wrapper. The tables record those signals through the current-implementation,
ownership, and rationale columns.

The source does not contain usage telemetry or a complete inventory of active
installations. Presence in the repository is therefore evidence that a behavior
exists, not that users independently value it. A row is marked
`merge into existing` when an existing first-party owner supplies that
independent context, `evaluate as new capability` when the source suggests a
plausible gap but usage evidence is still missing, and `temporary adapter` when
value is limited to protecting existing consumers or artifacts. Nothing is kept
as orchestration on source presence alone.

## Disposition vocabulary

| Disposition | Meaning |
| --- | --- |
| `keep as orchestration` | Preserve the behavior only if a small, independently justified orchestration layer remains after distillation. |
| `merge into existing` | Move the useful rule or workflow into an existing first-party owner; do not preserve the Effective Flow wrapper. |
| `evaluate as new capability` | There is a plausible collection-wide gap, but a separate capability still needs evidence and scope design. |
| `temporary adapter` | Keep only long enough to migrate consumers or recover valuable state, then remove. |
| `remove` | No first-party capability should preserve this part. |

## Public tools

The public catalog is verified from `TOOL_GROUPS` in `build.mjs`, not inferred
from the README.

| Tool | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| `investigate` | Explains a bug or surprising behavior without changing code and recommends one next action. | Writes a local diagnosis under `.effective-flow/investigation/`, carries temporary wisdom state, and routes to another Effective Flow tool. | `codebase-improvement` already owns repository reconnaissance, evidence, root-cause reasoning, and selected fixes. | Depends on private runtime paths and Effective Flow tool names. | `merge into existing` | Keep diagnosis-first behavior and the no-fix boundary in `codebase-improvement`; do not retain a branded report format. |
| `plan` | Clarifies work and writes an actionable implementation plan. | Creates status-bearing files under a configurable plan directory, invokes an internal interactive review, and recommends `build`, `fix`, `refactor`, or `docs`. | `codebase-improvement` owns executable engineering plans; `product-management`, `product-design`, `software-architecture`, and `effective-web` own specialist decisions. | Prescribes custom numbering migration, status markers, archive rules, and tool handoffs. | `merge into existing` | Preserve evidence-led planning and specialist routing, not the custom plan lifecycle. |
| `open-plans` | Lists plans that have not been implemented. | Parses Effective Flow status markers across active and archived plan directories. | No domain gap; repository search and normal task tracking cover it. | Only works with the custom plan schema. | `remove` | It is a convenience command created by the bespoke lifecycle, not a reusable skill. |
| `plan-issue` | Clarifies an underspecified GitHub or Forgejo issue in place. | Finds `effective-flow-needs-planning` issues, runs the planning method, comments on the issue, and removes the label. | Engineering clarification fits `codebase-improvement`; product clarification fits `product-management`. Issue mutation remains caller-owned. | Assumes specific tracker CLIs, labels, and a two-step Effective Flow queue. | `evaluate as new capability` | The clarification pattern is valuable, but only if a generic issue-oriented workflow proves useful without Effective Flow labels. |
| `apply` | Starts implementation from a plan, review report, or issue. | Detects a custom source type and loads one of three internal tools. It implements nothing itself. | Host skill discovery plus existing narrow skills. | Requires the Effective Flow router, report schema, plan schema, and tracker labels. | `remove` | A second router duplicates the host's selection responsibility and mainly connects Effective Flow-owned formats. |
| `build` | Implements a feature end to end, including tests, docs, review, and delivery. | A 444-line orchestrator that selects custom workers, tracks goals, uses optional worktrees, and performs delivery. | Normal agent execution, supplemented by domain skills such as `effective-web`, `software-architecture`, and `codebase-improvement`. | Couples model-specific workers, mutable state, custom includes, commits, branches, and PR completion. | `remove` | End-to-end execution is expected agent behavior; no evidence yet justifies an umbrella skill or fixed worker fleet. |
| `fix` | Diagnoses and fixes a bug with regression coverage. | Runs investigation, implementation worker selection, tests, validation, review, goal tracking, and delivery. | `codebase-improvement` owns diagnosis and focused improvements; frontend depth belongs to `effective-web`. | Same orchestration, worker, state, and delivery coupling as `build`. | `merge into existing` | Retain minimal-fix and regression-test judgment in the existing improvement owner. |
| `refactor` | Improves structure without changing behavior. | Runs gap analysis, baselines, custom implementers and reviewers, validation, before/after comparison, and delivery. | `codebase-improvement`; `port-codebases` for cross-runtime or cross-language work. | Couples a general refactor to Effective Flow's state, workers, plan schema, and delivery process. | `merge into existing` | This is already an explicit `codebase-improvement` use case. |
| `docs` | Creates or updates documentation without changing product behavior. | Clarifies scope, optionally plans, and delegates to `docs-writer` or `code-documenter` before validation and delivery. | Genuine general technical-documentation gap; tracked separately by [#106](https://github.com/sebastian-software/skills.sebastian-software.com/issues/106). | The useful writing guidance is packaged as workers behind the router. | `evaluate as new capability` | Evaluate a direct, descriptive technical-documentation skill; do not carry over the orchestration wrapper. |
| `maintain` | Updates dependencies and security fixes in grouped commits. | Thin adapter around `smart-dependency-updater`, adding baseline, commit grouping, worktree, report, and delivery rules. | `smart-dependency-updater`. | Adds a second delivery loop and Effective Flow state around an existing owner. | `merge into existing` | The source itself declares the central skill authoritative. |
| `iterate` | Applies human or bot feedback to an existing PR and updates it with new commits. | Reads PR threads and free-text instructions, classifies each item, dispatches to implementation tools, replies, resolves threads, validates, and pushes. | `pr-review` owns feedback resolution, CI recovery, and branch maintenance; caller-owned handoff is tracked by [#105](https://github.com/sebastian-software/skills.sebastian-software.com/issues/105). | Assumes GitHub/Forgejo APIs, Effective Flow routing, and authority to reply, resolve, commit, and push. | `temporary adapter` | Retain only until the generic `pr-review` handoff and migration path cover actual consumers. |
| `review` | Reviews code or, when passed a plan, reviews a plan. | A 507-line multimodal orchestrator with profiles, worker fan-out, decision filtering, finding IDs, local reports or remote issue epics, caches, and memory. | PR scope belongs to `pr-review`; repository and plan review to `codebase-improvement`; domain review routes to specialist skills. | Depends on custom workers, confidence schema, mutable counters, runtime cache, labels, and report formats. | `merge into existing` | Split by intent and let existing owners retain useful evidence and prioritization rules. |
| `commit` | Commits already staged changes using Conventional Commits. | Inspects the staged diff, proposes a message, and runs `git commit` without a co-author trailer. | No skill gap; normal repository-aware agent behavior. | Assumes a particular message convention and direct Git authority. | `remove` | Too small and generic to justify a public skill. Repository conventions should decide the message. |
| `pr` | Opens a GitHub or Forgejo pull request and restores the checkout. | Detects the host, uses `gh` or `tea`, pushes a branch, derives title/body, and manages branch restoration. | Normal delivery behavior; ongoing PR work belongs to `pr-review`. | Hard-wires two hosts, CLIs, checkout behavior, and mutation authority. | `remove` | Keep provider operations in the active workflow rather than a distributable skill. |
| `setup` | Configures Effective Flow in a target repository. | Writes a living setup ADR, adds an `AGENTS.md` marker, ignores `.effective-flow/`, and migrates old JSON configuration. | No collection-wide capability gap. | Entirely specific to Effective Flow configuration and runtime state. | `temporary adapter` | Useful only to migrate an existing installation away from the standalone system. |
| `cleanup` | Removes legacy Effective Flow, Firmo, and sf-plugin remnants after confirmation. | Reconciles old runtime/config state, `.gitignore` entries, installed files, and tracker labels before deletion. | No permanent owner. | Product-name-specific and intentionally destructive after confirmation. | `temporary adapter` | Keep as a bounded retirement aid, then remove with the last supported migration window. |
| `version` | Shows the installed Effective Flow version and source hash. | Reads a compiler-injected version string. | No skill gap. | Exists only because generated releases need independent version identity. | `remove` | Standard Git or package-manager pins already provide provenance for direct skills. |

## Internal tools

| Tool | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| `apply-plan` | Implements a finished plan through the recommended workflow. | Resolves custom plan references and status, applies the clarity gate, then dispatches to four public tools. | `codebase-improvement` planning and normal agent execution. | Requires Effective Flow plan metadata and tool names. | `remove` | The useful clarity check belongs with planning; the dispatch layer adds no domain value. |
| `apply-issues` | Implements one or more issues, one PR per sufficiently specified issue. | Classifies issue lists and container checklists, comments status, labels unclear work, and dispatches each issue. | Potential generic issue-execution gap; planning belongs to `codebase-improvement` or `product-management`. | Depends on `gh`/`tea`, special labels, sub-issue syntax, and the Effective Flow delivery loop. | `evaluate as new capability` | Evaluate only from real multi-issue usage and with caller-owned authority; do not smuggle it in as part of an umbrella skill. |
| `apply-review` | Resolves findings from a local report or remote review epic. | Parses custom finding states, may create ADRs, chooses commit strategy, runs fixes in parallel worktrees, validates, and updates report/issues. | `pr-review`, `decision-records`, and `codebase-improvement`; the remaining handoff gap is #105. | Tightly bound to Effective Flow finding IDs, reports, labels, state, worktrees, and commits. | `temporary adapter` | Needed only while old review artifacts remain; new work should flow through existing owners. |
| `apply-review-commit-mechanics` | Safely combines parallel review fixes. | Implements a commit mutex, per-finding worktrees, and cherry-pick conflict assessment. | No durable skill gap; this is execution mechanics. | Assumes a fixed parallel-worker and commit strategy. | `remove` | Keep such mechanics local to an implementation when actually needed. |
| `apply-review-remote` | Keeps remote finding issues and their epic synchronized. | Implements tracker labels, issue states, comments, and completion updates. | `pr-review` for PR feedback; generic issue orchestration remains unproven. | Coupled to the Effective Flow issue schema and GitHub/Forgejo CLIs. | `temporary adapter` | Retain only to close or migrate existing Effective Flow tracker artifacts. |
| `plan-review` | Interactively improves a plan before implementation. | Checks logic, security, feasibility, UI/UX, scorecard, and open points and edits the referenced plan. | `codebase-improvement`, routing to `product-management`, `product-design`, `software-architecture`, `effective-web`, or `web-legal-compliance`. | Bound to the custom plan schema and parent `plan` tool. | `merge into existing` | Plan review is already within the declared scope of `codebase-improvement`. |

## Custom workers

The 13 workers are build inputs, not portable skills. Every worker declares a
Claude model and tool list plus a Codex model, reasoning effort, and sandbox
mode. The compiler emits Claude workers as globally registered
`effective-flow-*` Markdown files and Codex workers as nested TOML agents. That
packaging choice is the main reason a single direct skill cannot currently be
installed unchanged.

| Worker | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| `code-documenter` | Adds JSDoc, TSDoc, rustdoc, inline comments, type docs, handler docs, and CLI help. | Writable specialist worker with language, task, discovery, and documentation rules. | Technical-documentation gap, #106. | Fixed model/tools/sandbox and generated agent registration. | `evaluate as new capability` | Distill its independently useful guidance together with `docs-writer`; do not keep a worker merely to make orchestration possible. |
| `docs-writer` | Produces README, user/developer, API/CLI, component, Rust, and migration documentation. | Writable specialist worker with documentation categories and central typography delegation. | Technical-documentation gap, #106. | Same worker packaging plus Effective Flow document-category rules. | `evaluate as new capability` | Strongest candidate for a direct first-party skill after scope and eval design. |
| `marketing-writer` | Turns the root README into a short user-value entry page with two documentation links. | Writable README-only worker with a rigid ending and optional copywriting skills. | Partly #106; no current first-party general marketing-documentation owner. | Hard-coded repository structure and worker runtime. | `evaluate as new capability` | Preserve the value-first README heuristic only if it fits a broader documentation capability; a standalone worker is too narrow. |
| `test-writer` | Writes unit, integration, component, API, CLI, database, and Rust tests. | Writable testing worker; delegates frontend depth to `effective-web` and keeps a broad fallback checklist. | Frontend testing is owned by `effective-web`; non-frontend ownership is under evaluation in #107. | Fixed worker runtime; overly broad JS/TS/Rust domain bundle. | `evaluate as new capability` | Use #107 to decide whether the non-frontend remainder is cohesive enough for a skill. |
| `e2e-tester` | Writes and runs browser E2E, API integration, CLI smoke, and visual regression tests. | Full-access worker with Playwright/page-object guidance and central frontend delegation. | Browser E2E belongs to `effective-web`; API/CLI testing remains part of #107. | Full-access worker declaration and mixed browser/non-browser scope. | `merge into existing` | Move browser depth to `effective-web`; evaluate any remaining test ownership with `test-writer`, not as a separate worker. |
| `ui-implementer` | Implements frontend code and components. | Full-access worker with a minimal fallback and authoritative delegation to `effective-web`. | `effective-web`. | Generated worker registration and model/sandbox selection. | `merge into existing` | The source already says the central skill owns the substantive domain. |
| `frontend-reviewer` | Reviews accessibility, performance, UI patterns, design systems, CSS, and state. | Read-only worker whose depth comes from `effective-web`, plus Effective Flow finding format. | `effective-web`; PR lifecycle belongs to `pr-review`. | Fixed worker runtime and custom finding schema. | `merge into existing` | Use the domain skill during normal review rather than retaining a separate reviewer identity. |
| `nodejs-implementer` | Implements Node.js APIs, CLIs, services, database access, security, logging, and shutdown. | Full-access worker containing a broad Node.js backend checklist. | `software-architecture` covers system-level reasoning, not implementation depth; possible backend-engineering gap. | Fixed worker runtime and one large stack-specific handbook. | `evaluate as new capability` | Evaluate the durable Node/CLI/runtime judgment jointly with the Rust material and #107 boundaries. |
| `nodejs-reviewer` | Reviews Node.js APIs, security, event-loop performance, errors, CLIs, configuration, and logging. | Read-only worker with confidence and finding-schema constraints. | Architecture routes to `software-architecture`; line-level backend review has no owner. | Worker runtime and Effective Flow report contract. | `evaluate as new capability` | Candidate evidence for a descriptive backend-engineering capability, not a reason to preserve Effective Flow. |
| `rust-implementer` | Implements idiomatic Rust libraries, services, CLIs, async code, database access, and safe abstractions. | Full-access worker containing Rust-specific implementation guidance. | `software-architecture` covers cross-cutting architecture; Rust implementation depth has no owner. | Fixed worker runtime and language-specific packaging. | `evaluate as new capability` | Test whether Node and Rust share a coherent backend/runtime capability or need narrower ownership; do not assume either. |
| `rust-reviewer` | Reviews Rust safety, errors, idioms, concurrency, APIs, security, and CLI behavior. | Read-only worker with confidence and report-format constraints. | Same gap as `rust-implementer`. | Worker runtime and Effective Flow finding schema. | `evaluate as new capability` | Useful source material, pending evidence-led capability boundaries. |
| `generic-implementer` | Changes CI, tooling, configuration, manifests, containers, and repository metadata. | Full-access catch-all worker with generic structure, version, and validation rules. | Normal agent behavior; dependency work routes to `smart-dependency-updater`. | Broad authority and generated worker registration with no distinctive domain. | `remove` | A catch-all worker is orchestration scaffolding, not a first-party skill. |
| `code-validator` | Runs lint, type, format, build, Cargo, and related validation and explains failures. | Writable worker that detects and runs existing project commands. | Normal implementation behavior; verification is already required by `codebase-improvement`, `pr-review`, `effective-web`, and other skills. | Fixed worker runtime; risks separating validation from the agent that owns the change. | `merge into existing` | Keep the principle “use repository-native checks and distinguish baseline failures” in each owning workflow, not as a worker. |

## Shared instruction fragments

Every shared source file is accounted for below. Closely related fragments are
grouped because their value and retirement path are the same.

| Shared source(s) | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| `adr-convention.md` | Rejected findings can become durable decisions. | Declares living, numberless ADRs and provides a fallback template. | `decision-records`. | Overrides target conventions unless carefully delegated; embedded through compiler includes. | `merge into existing` | Let `decision-records` discover the target convention. Do not retain an Effective Flow ADR dialect. |
| `apply-clarity-gate.md` | Prevents implementation from guessing through open points or unverifiable acceptance criteria. | Shared gate across direct and `apply` entry points. | `codebase-improvement` planning; product ambiguity routes to `product-management`. | References custom plan/report/tool types. | `merge into existing` | The judgment is valuable and portable once detached from Effective Flow routing. |
| `apply-source-detection.md` | Distinguishes plans, review reports, review issues, container issues, and plain issues. | Two-stage filesystem/tracker classifier. | No current owner for generic issue execution; plan/review ownership already exists. | Almost every type is defined by Effective Flow paths, labels, or markers. | `temporary adapter` | Use only to migrate old sources; evaluate a much smaller issue-input contract if real demand remains. |
| `audit-reasoning-delegation.md`, `central-reasoning-delegation.md` | Gives tools better audit and plan judgment. | Adapter contracts that call `codebase-improvement` and normalize results into Effective Flow schemas. | `codebase-improvement`. | Exist only because Effective Flow wraps another skill. | `remove` | Direct use of the owner eliminates both adapters. |
| `commit-message-rules.md`, `pre-commit-gate.md`, `completion-protocol.md`, `goal-completion.md`, `task-tracking.md` | Keeps implementation progressing, validated, and committed coherently. | Repeated lifecycle gates and temporary task state embedded in tools and workers. | Normal agent/repository workflow; owning skills already require proportionate verification. | Coupled to custom `/goal`, worker handoffs, commit authority, and compiler includes. | `remove` | These are execution conventions, not independently installable expertise. Retain only specific proven rules in their natural owner. |
| `config-migration.md`, `effective-flow-dir-migration.md` | Moves old Firmo/sf-plugin config and state to Effective Flow paths. | Reads legacy JSON/runtime locations, writes setup ADR markers, and tracks migration state. | No permanent owner. | Product- and history-specific. | `temporary adapter` | Invert the migration toward retirement, preserve only valuable user artifacts, and remove after the support window. |
| `dependency-version-policy.md` | Avoids casual version changes and uses repository lockfiles. | Small shared rule embedded in implementers and test/documentation workers. | `smart-dependency-updater` for update work; repository conventions otherwise. | Compiler include for a rule already owned elsewhere. | `merge into existing` | Keep update research in the dependency skill and normal lockfile respect in execution. |
| `doc-categories.md` | Separates root marketing README, user guide, developer guide, API/reference, and plans. | Prescribes documentation directories and landing pages. | Technical-documentation gap, #106. | Hard-coded information architecture may not fit every repository. | `evaluate as new capability` | Retain as evidence, but the future skill must discover and preserve repository conventions. |
| `investigation-method.md`, `wisdom-accumulation.md` | Carries hypotheses, reproduction evidence, and lessons between workflow phases. | Investigation checklist plus per-session hidden temporary Markdown. | `codebase-improvement`. | Uses hidden Effective Flow state to compensate for a multi-worker workflow. | `merge into existing` | Keep hypothesis/evidence discipline; remove hidden wisdom files and worker-transfer ceremony. |
| `issue-tracker.md` | Stores review findings remotely and supports GitHub/Forgejo issue execution. | Host detection, CLI checks, labels, issue schemas, deduplication, and migration among three prefixes. | `pr-review` for PR feedback; generic issue-batch execution remains an evaluated gap. | Provider CLI, auth, mutation authority, labels, and Effective Flow schemas are inseparable. | `temporary adapter` | Needed to discover and retire existing remote artifacts; no permanent branded tracker layer. |
| `language-rules.md` | Keeps code/commits in English and visible prose locale-correct. | Minimal policy plus delegation to central language skills. | `locale-typography`; `metro-english` for team communication; repository instructions for code language. | One global language policy does not fit every repository. | `merge into existing` | Preserve locale expertise centrally and honor each repository's language convention. |
| `plan-numbering.md`, `plan-reference-routing.md`, `plan-status.md` | Makes plans addressable, resumable, and archivable. | Date-slug naming, legacy-number migration, status markers, lookup, and archive behavior. | `codebase-improvement` owns plan quality, but no need exists for a universal plan database. | Custom schema and backward-compatibility burden. | `remove` | Plain repository-native plans are enough; existing Effective Flow plans can be migrated by a temporary adapter. |
| `pr-review-comments.md` | Classifies, replies to, and resolves PR feedback safely. | Shared GitHub/Forgejo thread logic used by `iterate`. | `pr-review`, with caller-owned handoff evaluated in #105. | Assumes provider APIs and mutation authority. | `merge into existing` | Distill provider-neutral classification and authority boundaries into `pr-review`. |
| `review-report-backlinks.md`, `unresolved-review-report.md` | Keeps unresolved findings traceable after implementation and links fixes back to reports. | Generates Effective Flow report paths, IDs, statuses, and backlinks. | `pr-review` or `codebase-improvement`, depending on scope. | Depends on `.effective-flow/review/`, global counters, and a German-token report schema. | `temporary adapter` | Preserve links while old reports remain; new work should use owner-native artifacts. |
| `reviewer-design-decisions.md` | Avoids reporting an intentional design choice as a defect. | Requires reviewers to inspect relevant ADRs and mark filtered findings. | `decision-records` plus the active review owner. | Embedded in custom worker output contracts. | `merge into existing` | This is a sound review rule and belongs in normal review guidance. |
| `skill-discovery.md` | Loads installed domain skills only when relevant and honors include/exclude preferences. | Custom discovery contract plus Effective Flow configuration and fallback chains. | Native host skill discovery and each skill's trigger. | Reimplements platform behavior and adds another configuration layer. | `remove` | Directly installable skills should rely on the host contract; dependencies can be documented without a private router. |
| `worktree-integration.md` | Isolates implementation and completes it as a branch, merge, or PR. | A 285-line branch/worktree/delivery protocol with setup detection, partial-diff transfer, plan archiving, commits, handback, and PR creation. | Normal agent delivery behavior; `pr-review` owns existing-PR maintenance. | Imposes branch, setup, commit, and merge policy across repositories. | `remove` | Useful individual safeguards should remain in agent/repository workflow, not in a mandatory skill-owned delivery subsystem. |

## Target-project state, configuration, and artifacts

| Component | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| Project setup ADR and marker | Makes one project-wide Effective Flow configuration discoverable. | A living `docs/adr/effective-flow-project-setup.md` is referenced by `**Effective Flow project setup:**` in `AGENTS.md` or `CLAUDE.md`. | `decision-records` owns real decisions; repository config should stay in its executable owner. | Pollutes repository instructions with a product-specific marker and stores operational settings in prose. | `temporary adapter` | Read it during migration, preserve genuine decisions, then remove the marker and product configuration. |
| Configuration schema | Controls review profiles, apply-review strategy, plan paths, worktrees, delivery, tracker, and skill discovery. | Markdown key/value table with defaults and legacy JSON fallbacks. | Settings belong to the concrete workflow or repository, not a collection-wide runtime. | Large cross-cutting schema must be interpreted consistently by every tool. | `remove` | It creates a second agent runtime. Direct skills should need little or no shared configuration. |
| `.effective-flow/memory.json` and `cache.json` | Keeps global finding numbers, migration markers, and review cache. | Hidden, gitignored mutable JSON read and written by review and migration flows. | No permanent owner. | State is invisible to standard skill managers and unsafe to assume across agents or machines. | `temporary adapter` | Recover links and migration status if needed, then remove; new findings need no global branded counter. |
| `.effective-flow/review/` and `.effective-flow/investigation/` | Persists local review and diagnosis reports. | Hidden, untracked Markdown with custom names, schemas, and status tokens. | `codebase-improvement` and `pr-review`. | Valuable evidence is intentionally outside normal repository history. | `temporary adapter` | Offer a deliberate migration to normal docs/issues when worth keeping; otherwise delete after user review. |
| `.effective-flow/.worktrees/` and wisdom files | Isolates work and passes temporary reasoning among workers. | Gitignored worktrees and `.wisdom-accumulation-<SESSION>.tmp.md`. | Normal execution environment. | Local paths and session files are not portable skill state. | `remove` | Worktrees may still be used by agents, but must not be owned by a skill installation. |
| `docs/plan/` status and archive model | Makes implementation plans resumable and records completed work. | Configurable directory, canonical bilingual status marker, date slugs, legacy numbering, and archive moves at delivery. | Plan quality belongs to `codebase-improvement`; repositories own storage conventions. | Requires all readers and writers to understand Effective Flow metadata. | `temporary adapter` | Preserve human-useful plan content, normalize only when a repository chooses to, and retire the mandatory schema. |
| Remote tracker artifacts | Shares review/issue progress with a team. | `effective-flow-*` labels, review-finding issues, epic checklists, comments, and predecessor-prefix compatibility. | `pr-review` for PR threads; normal project management for issues. | Mutates external systems and leaves branded state after uninstall. | `temporary adapter` | Inventory and close/relabel existing artifacts with explicit authority; do not create new branded queues. |

The audited revision also contains documentation drift: developer guidance and
the current `setup` source say configuration moved into a living setup ADR and
`.effective-flow/` is fully ignored, while several user-guide pages still
describe `.effective-flow/config.json` as the active tracked source. This is a
concrete maintenance cost of the duplicated lifecycle and documentation layers,
not merely a theoretical portability concern.

## Build, distribution, installation, and release

| Component | User-visible outcome | Current implementation | Current first-party owner or gap | Portability constraint | Disposition | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| Thin router and lazy tool loading | Exposes one memorable command without loading all tool instructions. | `src/SKILL.md` receives a generated catalog; public tools are loaded by name and may load internal or lazy shared files. | Native skill discovery plus focused first-party skills. | Requires users to know a second command grammar and requires generated references. | `remove` | Progressive disclosure is good, but direct skills already provide it without an umbrella router. |
| Source-to-dist compiler | Produces matching Claude and Codex packages from one source. | `build.mjs` and `build-lib.mjs` parse frontmatter, resolve eager/lazy includes, expand skill/agent/version placeholders, render `ask` blocks, normalize sandboxes, and atomically swap `dist/`. | No collection gap. | Exists to support platform-specific worker registration, commands, and metadata chosen by Effective Flow. | `remove` | Publish plain `skills/<name>/SKILL.md` sources directly. Add deterministic helpers only for behavior that genuinely requires code. |
| Compiler guards and tests | Prevents invalid references, frontmatter, duplicated groups, stale standards, broken docs, and Claude/Codex version drift. | `test/build-lib.test.mjs` plus build-time content, budget, reference, and output guards. | Collection validators cover direct skill structure and site metadata. | Most invariants protect generated artifacts that will no longer exist. | `remove` | Port any generally useful validation to collection validators only when a direct skill demonstrates the need. |
| Platform-specific worker output | Gives both harnesses approximately equivalent custom workers. | Claude gets global `effective-flow-*.md` agents; Codex gets nested `agents/*.toml`; model, tools, color, reasoning, and sandbox fields are transformed. | No proven capability gap. | This is the central non-portable requirement and the reason for separate distributions. | `remove` | Do not promise internal worker parity. Use native delegation opportunistically when available. |
| `develop` source and generated `main` delivery branch | Lets standard installers consume built artifacts from the default branch. | Releases append generated `claude/`, `codex/`, README, user docs, and Renovate config to `main`; source stays on `develop`. | Standard direct GitHub installation from this collection. | Default branch is not reviewable source and must be synchronized by release automation. | `remove` | Each future skill should live directly under `skills/` on the normal default branch. |
| Release Please, version stamp, and archive | Publishes versioned standalone bundles and displays an installed version/hash. | Release Please on `develop`, changelog/tag/release, tarball of both distributions, compiler-injected version, and drift guard. | Git commit pins and skill-manager source state. | Adds a separate release identity and asset flow for Markdown instructions. | `remove` | Reintroduce release packaging only if a future deterministic runtime artifact needs it. |
| Custom installer | Installs both builds and globally registered Claude workers from the latest release. | `install-skill.sh` downloads with `gh`; `local-common.sh` copies into Claude/Codex paths and deletes retired installs; `local-link.sh` symlinks local builds. | DALO and the skills CLI. | Writes several global directories, assumes `gh`, handles three historical names, and bypasses standard selection/provenance. | `temporary adapter` | Keep an uninstall/migration path for existing users, then direct all new installation to standard GitHub URLs. |
| CI and documentation delivery | Verifies and publishes the standalone distribution. | Node 24/pnpm format, unit/build, shellcheck, docs link rewriting, worktree delivery, and Renovate redirection. | This collection's existing validators and normal CI. | Maintains two audiences on two branches and rewrites links during delivery. | `remove` | Direct source eliminates delivery rewriting; retain only tests belonging to distilled capabilities. |

## Capability map

The audit supports the following narrow, successive work. It does **not**
authorize implementing the linked issues in parallel.

| Candidate outcome | Evidence from Effective Flow | Next owner or decision |
| --- | --- | --- |
| Caller-owned PR feedback analysis | `iterate`, `apply-review`, `pr-review-comments` | Extend `pr-review` only if #105's generic handoff contract remains independently useful. |
| Technical documentation guidance | `docs`, `docs-writer`, `code-documenter`, selected `marketing-writer` and `doc-categories` rules | Evaluate the descriptive capability in #106 with repository-convention discovery and behavioral evals. |
| Non-frontend test judgment | `test-writer`, non-browser parts of `e2e-tester`, validation handoffs | Complete the ownership analysis in #107 before creating a skill. |
| Backend/runtime engineering judgment | Node.js and Rust implementer/reviewer material | Compare against `software-architecture`, #107, and real recurring work; create no issue or skill from this audit alone. |
| Issue clarification or issue-batch execution | `plan-issue`, `apply-issues`, tracker abstractions | Collect real use cases first; separate analysis from mutation authority and avoid Effective Flow labels. |
| Umbrella software-delivery orchestration | Router, `build`, `apply`, custom workers, state, and delivery | **Not justified now.** Reconsider only after the narrow capabilities are proven and an unmet cross-skill orchestration problem remains. |

## Successive retirement sequence

1. **Freeze and observe.** Treat the audited revision as source material. Avoid
   expanding the compiler, worker fleet, configuration schema, or installer
   while the narrow capability decisions are pending.
2. **Distill one capability at a time.** Start with the smallest independently
   valuable candidate, implement it under a descriptive name, validate it with
   its own evals, and verify direct installation through standard skill
   managers. #105–#107 remain separate decisions and are not bundled into this
   audit.
3. **Redirect real consumers.** Replace one Effective Flow dependency at a time
   with an existing or newly accepted first-party owner. Keep temporary adapters
   only for existing plans, review artifacts, issue labels, or setup state that
   users still need.
4. **Deprecate the standalone entry point.** Once the needed outcomes are
   reachable without it, stop recommending `/effective-flow`, stop publishing
   new generated packages, and provide an explicit migration/uninstall guide.
5. **Clean up after an announced support window.** Remove custom agents,
   compiler and generated branch, release archives, installer, branded target
   state, and temporary adapters. Archive the external repository only after
   active consumers and valuable artifacts have been checked.

Each phase has an exit gate: the next phase starts only after the previous
replacement is usable and its affected consumers are known. The intended result
may be **no umbrella successor at all**.

## Source coverage manifest

This manifest makes the count and classification reproducible without copying
the private source contents into this repository.

### Public tools (17)

`src/tools/investigate.md`, `src/tools/plan.md`,
`src/tools/open-plans.md`, `src/tools/plan-issue.md`,
`src/tools/apply.md`, `src/tools/build.md`, `src/tools/fix.md`,
`src/tools/refactor.md`, `src/tools/docs.md`, `src/tools/maintain.md`,
`src/tools/iterate.md`, `src/tools/review.md`, `src/tools/commit.md`,
`src/tools/pr.md`, `src/tools/setup.md`, `src/tools/cleanup.md`, and
`src/tools/version.md`.

### Internal tools (6)

`src/tools/apply-plan.md`, `src/tools/apply-issues.md`,
`src/tools/apply-review.md`, `src/tools/apply-review-commit-mechanics.md`,
`src/tools/apply-review-remote.md`, and `src/tools/plan-review.md`.

### Custom workers (13)

`src/agents/code-documenter.md`, `src/agents/code-validator.md`,
`src/agents/docs-writer.md`, `src/agents/e2e-tester.md`,
`src/agents/frontend-reviewer.md`, `src/agents/generic-implementer.md`,
`src/agents/marketing-writer.md`, `src/agents/nodejs-implementer.md`,
`src/agents/nodejs-reviewer.md`, `src/agents/rust-implementer.md`,
`src/agents/rust-reviewer.md`, `src/agents/test-writer.md`, and
`src/agents/ui-implementer.md`.

### Shared fragments (27)

`src/shared/adr-convention.md`, `src/shared/apply-clarity-gate.md`,
`src/shared/apply-source-detection.md`,
`src/shared/audit-reasoning-delegation.md`,
`src/shared/central-reasoning-delegation.md`,
`src/shared/commit-message-rules.md`, `src/shared/completion-protocol.md`,
`src/shared/config-migration.md`, `src/shared/dependency-version-policy.md`,
`src/shared/doc-categories.md`,
`src/shared/effective-flow-dir-migration.md`,
`src/shared/goal-completion.md`, `src/shared/investigation-method.md`,
`src/shared/issue-tracker.md`, `src/shared/language-rules.md`,
`src/shared/plan-numbering.md`, `src/shared/plan-reference-routing.md`,
`src/shared/plan-status.md`, `src/shared/pr-review-comments.md`,
`src/shared/pre-commit-gate.md`, `src/shared/review-report-backlinks.md`,
`src/shared/reviewer-design-decisions.md`, `src/shared/skill-discovery.md`,
`src/shared/task-tracking.md`, `src/shared/unresolved-review-report.md`,
`src/shared/wisdom-accumulation.md`, and
`src/shared/worktree-integration.md`.

### Standalone-system machinery

The build and transform surface is `src/SKILL.md`, `build.mjs`,
`build-lib.mjs`, and `test/build-lib.test.mjs`. Installation and local
development use `install-skill.sh`, `local-common.sh`, and `local-link.sh`.
Release and delivery use `.github/workflows/ci.yml`,
`.github/workflows/release.yml`, `.release-please-manifest.json`,
`release-please-config.json`, `scripts/deliver-docs.mjs`, and
`scripts/delivery-renovate.json`.
