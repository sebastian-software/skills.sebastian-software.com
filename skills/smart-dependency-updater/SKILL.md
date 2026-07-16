---
name: smart-dependency-updater
description: This skill should be used when the user asks to "update dependencies", "upgrade packages", "replace Dependabot", "make Renovate smarter", "group dependency updates", "create dependency update PRs", "create multiple dependency PRs", "run dependency updates in worktrees", "bump packages with changelog impact", "modernize dependencies and code", or wants dependency PRs that explain upstream changes, validate behavior, and adopt useful new APIs in the local codebase. Default to producing pushed, ready-for-review pull requests for all viable dependency groups unless the user explicitly asks for planning only, draft PRs, local-only branches, or a single group.
---

# Smart Dependency Updater

Use this skill to perform dependency updates as engineering work, not as mechanical version bumps. The default outcome is a portfolio of focused, pushed, ready-for-review pull requests. Each PR groups related packages, explains what changed upstream, assesses local impact, runs the repository's validation suite, and adopts newly useful dependency capabilities when they improve the local code.

Treat every update as a small migration and delivery unit. Do not stop after creating a local branch, updating one easy package, or writing a chat summary unless the user explicitly asked for that narrower outcome. A good outcome is a set of ready-for-review PRs where reviewers and automation can see why the versions belong together, what changed in those dependencies, what local risk was checked, which tests were run, and whether the project now benefits from new APIs, fixed limitations, or changed defaults.

## Default Delivery Contract

When the user invokes this skill for dependency updates without narrowing the scope, execute the full dependency-update portfolio:

1. Discover all direct dependency candidates.
2. Group them into coherent PR units.
3. Create one branch or worktree per viable group.
4. Research, update, validate, commit, push, and open a ready-for-review PR for each viable group.
5. Put the reviewer-grade explanation in the PR title and body, not primarily in the chat response.
6. Defer only groups that are blocked, require human product/security decisions, are too risky for the current run, or conflict with already-open PR sequencing. Record the reason.

Final chat responses should be operational: list PR links, validation status, deferred groups, and any blockers. Avoid pasting full PR bodies into chat unless the user asks for them.

## Operating Model

1. **Load repository context first.**
   - Read local instructions such as `AGENTS.md`, `CLAUDE.md`, contribution docs, PR templates, CI workflows, package manifests, lockfiles, and release notes.
   - Run [the dependency-context helper](scripts/discover_dependency_context.py)
     when a quick dependency map is useful.
   - Identify package managers, workspaces, generated lockfiles, supported runtime versions, and test/build commands before changing versions.
2. **Build an update inventory.**
   - List currently used dependency versions from manifests and lockfiles.
   - Find candidate latest versions using the project's package manager commands, registry metadata, or official release sources.
   - Run the repository's available security audit or a source scan such as
     `osv-scanner scan source -r .`; record advisory IDs, severity, affected and
     fixed ranges, and dependency paths before grouping security work.
   - Separate runtime, dev/tooling, test, type, lint, framework, adapter/plugin, and transitive-only updates.
3. **Group dependencies by real coupling.**
   - Group packages that should be reviewed and validated together: framework core plus adapters, type packages plus runtime packages, plugin ecosystems, compiler/linter/parser families, test runner plus coverage adapters, SDK modules from the same vendor, and packages that share peer dependency constraints.
   - Keep unrelated packages separate even when they are individually small. Smaller coherent PRs are easier to review than a large "everything update" PR.
   - Split a package into its own PR when it has a major version change, migration guide, broad API surface, runtime behavior changes, security implications, or unclear compatibility.
4. **Plan the PR portfolio before editing, then execute it.**
   - Treat a dependency inventory as a portfolio of possible PRs, not as a single backlog item.
   - Produce one row per proposed PR group with package names, old/new versions, grouping reason, risk, validation surface, and worktree/branch name.
   - Merge multiple package families into one PR only when they answer the same reviewer question and share the same validation surface. Split them when they require different expertise or tests.
   - Do not finish at the portfolio table when the user asked for dependency updates. Use the table as the execution plan for the PRs.
5. **Plan publish units before editing.**
   - Treat each dependency group as a default branch, commit, and PR unit, not just as an analysis bucket.
   - If two groups answer different review questions, prepare separate PRs even when the code changes are small.
   - Keep a required migration or tightly coupled cleanup in the same PR as the dependency that caused it, but consider a separate commit when it improves review.
   - Use Conventional Commits for each commit unless the repository has a stricter convention.
6. **Research upstream changes before editing code.**
   - Read changelogs, release notes, migration guides, GitHub releases, compare views, and issue links for the exact old-to-new version range.
   - Prefer primary sources. If release notes are incomplete, inspect git tags, commits, package diff, type definitions, docs, and tests.
   - Capture gaps explicitly instead of pretending the upstream history is complete.
7. **Assess local impact.**
   - Search the codebase for imported APIs, config keys, CLI usage, environment variables, generated code, peer dependency assumptions, and documented workarounds tied to the packages.
   - Classify each upstream change as `irrelevant`, `covered-by-existing-usage`, `requires-local-change`, `enables-local-improvement`, or `needs-human-decision`.
   - Update local code when the new version provides a clearly better API, fixes a workaround, removes a local shim, improves types, closes a bug, or changes recommended configuration.
8. **Implement, validate, and publish one PR group at a time.**
   - Update manifests and lockfiles with the package manager that owns them.
   - Make local code migrations in the same PR only when they directly benefit from or are required by the grouped dependency update.
   - Run the repository's narrow checks first, then broader suites that match the changed dependency surface.
   - If a check cannot be run, record the reason and the most relevant substitute validation.
   - Commit, push, and open a ready-for-review PR before moving to the next unrelated group, unless the user explicitly asked for draft or local-only work.
9. **Write the reviewer-grade explanation into the PR.**
   - Explain the dependency group, old and new versions, upstream behavior changes, local impact, code changes made to benefit from the update, validation results, and known gaps.
   - Use principles from `copywriting` and `humanizer`, both from the separately
     managed DALO `marketingskills` catalog, when drafting PR titles and bodies:
     write for a busy reviewer, lead with the review question, and remove stiff
     AI phrasing.
   - Avoid raw changelog dumps. Summarize only the changes that matter to this project and link to sources.
   - Keep the chat summary short; the PR body is the review artifact.
   - For advisory-motivated changes, include the advisory ID, severity, affected
     dependency path, fixed range, and verification that the selected version is
     outside the affected range.

## Update Grouping Heuristics

Use the smallest group that preserves meaning and compatibility.

| Group type | Typical examples | Default PR shape |
| --- | --- | --- |
| Framework runtime | `next`, `react`, `react-dom`, `@next/*`, framework adapters | One PR per framework family and major line |
| Build tooling | `vite`, `@vitejs/*`, Rollup plugins, bundler adapters | One PR per build surface; split from runtime frameworks unless the migration guide couples them |
| Lint/format/type tooling | `typescript`, `eslint`, parsers, plugins, `biome`, `ultracite` | One PR when configs and peer ranges are coupled; split TypeScript majors when repo-wide fallout is likely |
| Test stack | runner, environment, coverage, snapshot serializers | One PR with focused test validation |
| UI primitive family | `@radix-ui/*`, `cmdk`, `react-day-picker`, related shadcn primitives | One PR when components share the same app/UI validation surface |
| SDK/vendor modules | `@aws-sdk/*`, `@sentry/*`, `firebase` packages | One PR per vendor feature area when large |
| Types and runtime | `foo` plus `@types/foo` | Same PR unless types update is independent |
| Security patch | vulnerable package, required direct parents, or a scoped override | Separate PR when urgency or blast radius differs |

Read [the detailed workflow](references/workflow.md) for a deeper grouping,
research, and impact-analysis procedure.

## PR and Commit Shaping

Default to one branch and one PR per dependency group. A group should be easy to name as a single reviewer question, such as "Does the Vitest coverage update still satisfy test and coverage checks?" or "Does the docs framework stack still build after the Ardo/Vite migration?"

Split groups when they have different validation surfaces. For example, root test/build tooling and docs framework dependencies should usually be separate PRs, because one is reviewed through package checks and tests while the other is reviewed through docs build output and framework migration notes.

Combine packages into one PR when the coupling is real: shared peer constraints, one adapter for another package, one vendor SDK surface, one UI primitive family, one test runner stack, or one migration guide that requires coordinated code changes. Do not combine packages only because they are all "tooling"; Next.js runtime, Vite build config, ESLint rules, and TypeScript compiler changes often deserve separate PRs.

Use Conventional Commits. Small groups can use one commit, for example `chore(deps): update vitest coverage tooling`. If the update forces local code migration, a second commit can make review easier, for example `refactor(docs): adapt ardo ui imports`. Keep both commits in the same PR only when the migration is caused by that dependency group.

For dependency-update requests, continue the grouping through the full delivery flow by default: create the branch, stage only that group's files, commit, push, and open a ready-for-review PR for that group before moving to the next unrelated group. Do not collapse unrelated update groups into one PR just because they were discovered in the same inventory pass. Only open draft PRs, skip publishing, or keep local-only branches when the user explicitly asks for that narrower mode.

## Multi-PR Worktree Orchestration

Use worktrees when the user asks for multiple dependency PRs, when several groups can proceed independently, when the default dependency portfolio contains more than one viable group, or when the repo has a branch guard that blocks edits on the main branch.

1. Start from a clean base branch and fetch the current default branch.
2. Create one worktree per proposed PR group, named by the group and branch, for example `codex/deps-radix-primitives` or `codex/deps-vite-build`.
3. Apply only that group's manifest, lockfile, generated output, migrations, and local adoption changes in that worktree.
4. Run validation matching that group's surface. Prefer narrow checks first, then the repo's broad quality gate when the group affects shared tooling or lockfiles.
5. Commit, push, and open a ready-for-review PR for that group before starting the next unrelated group, unless the user explicitly wants draft PRs or only local branches.
6. Record deferred groups and reasons, especially major upgrades split out because they need migration research or human decisions.

When a shared lockfile makes multiple worktrees conflict, keep the PR group boundaries anyway. Rebase each worktree on the latest default branch after the prior dependency PR lands, or regenerate the lockfile in the active PR group and document that it intentionally contains only that group's dependency story.

## Source Research Requirements

For each grouped update, collect enough evidence to answer these questions:

- What exact version range is changing?
- Which upstream changes can affect this repository's runtime behavior, generated output, public API, build/test pipeline, or deployment?
- Which changes are irrelevant because the project does not use that feature?
- Which migration notes, deprecations, peer dependency changes, or changed defaults require local action?
- Which new fixes or features make an existing local workaround unnecessary?
- Where are the gaps in upstream documentation or changelogs?

Use [ecosystem notes](references/ecosystem-notes.md) for package-manager
commands and ecosystem-specific checks.

## Local Code Adoption

Prefer adopting new dependency capabilities when the improvement is directly supported by the update research and local usage evidence.

Good adoption candidates:

- Replace local compatibility code after the upstream package gained first-class support.
- Remove comments or workarounds tied to a bug fixed in the new version.
- Use improved types, safer options, or stricter defaults when they reduce local risk.
- Update configuration to recommended names or defaults before old forms become deprecated.
- Simplify code paths made unnecessary by new APIs.

Avoid opportunistic refactors that are merely adjacent. If an improvement is appealing but not clearly part of the dependency update, mention it as a follow-up rather than expanding the PR.

## PR Body Format

Use this structure unless the repository has a stricter PR template:

```markdown
## Dependency group
- Packages: `name` old -> new, `name` old -> new
- Why grouped: shared peer constraints / same framework family / same toolchain surface

## Upstream changes that matter here
- [Package]: concise local-impact summary with source link
- [Package]: note relevant breaking changes, changed defaults, fixes, or new APIs
- Gaps: release notes missing for X; checked tags/commits/package diff instead

## Local impact and code changes
- Existing usage checked: imports/config/CLI/tests affected
- Required migrations:
- Beneficial adoption:
- Deferred follow-ups:

## Validation
- `command`: result
- `command`: result

## Risk
- Runtime/build/test/config risk and remaining uncertainty
```

Write this full review package into the pull request body. Do not substitute a long chat response for the PR body. In chat, report the PR URL, validation result, and any deferred groups or blockers.

## PR Writing Style

Make PRs accessible and concrete. Apply the same discipline used for good product copy, but keep the tone engineering-focused:

- Lead with what the reviewer needs to decide.
- Use short paragraphs and specific package/version ranges.
- Translate upstream changes into local consequences.
- Say what was checked, what changed locally, and what remains deferred.
- Avoid vague claims like "modernizes the stack", "improves stability", or "keeps everything up to date" unless you can tie them to a concrete local effect.
- Avoid AI-sounding filler such as "This update serves as", "It is important to note", "seamless", "robust", "pivotal", and generic upbeat conclusions.
- Prefer plain language: "Docs build required new Ardo component names" is better than "The documentation surface was migrated to align with the updated Ardo API".

## Additional Resources

- **[Dependency-context helper](scripts/discover_dependency_context.py)** - Inspect common manifests, lockfiles, package-manager hints, and JS test/build scripts.
- **[Detailed workflow](references/workflow.md)** - End-to-end workflow for inventory, grouping, research, impact classification, implementation, and PR writing.
- **[Ecosystem notes](references/ecosystem-notes.md)** - Commands and checks for JavaScript, Rust, Python, Go, Ruby, Java, and .NET projects.
- **[Evaluation prompts](evals/evals.json)** - Test whether this skill produces better dependency-update plans and PR descriptions than a baseline.
