# Smart Dependency Update Workflow

Use this reference when executing the full dependency-update process or when the package graph is large enough that the grouping decision needs explicit reasoning.

## 1. Repository Orientation

Start by establishing the local rules and dependency topology.

- Read local agent/contribution instructions before package metadata.
- Identify package managers and lockfile ownership. Never mix package managers unless the repository already does.
- Check workspace boundaries. A monorepo may need one lockfile update but several package-level validation commands.
- Read CI workflow files to understand the checks maintainers expect.
- Inspect release, deployment, or engine constraints such as Node, Python, Rust, Java, browser targets, OS support, or Docker base images.

Suggested inventory output:

```markdown
## Dependency context
- Ecosystems:
- Package manager and lockfiles:
- Workspaces/packages:
- Runtime constraints:
- Test/build/lint commands:
- CI checks:
```

## 2. Candidate Update Discovery

Use official package-manager commands where possible, then registry or upstream sources for extra context.

- JavaScript: `npm outdated`, `pnpm outdated`, `yarn outdated` (Yarn 1), or
  `yarn upgrade-interactive` / the outdated plugin (Yarn 2+), plus
  package-manager-specific lockfile updates.
- Rust: `cargo update --dry-run` where available, `cargo tree`, `cargo outdated` if installed.
- Python: inspect `pyproject.toml`, lockfiles, `pip list --outdated`, `uv lock --upgrade-package`, `poetry show --outdated`.
- Go: `go list -m -u all`.
- Ruby: `bundle outdated`.
- Java: use Maven/Gradle version plugins if present.
- .NET: `dotnet list package --outdated`.

When tools are unavailable, read manifests and lockfiles directly, then use registry metadata or upstream release pages. Record tool gaps in the plan.

## 2a. Security Advisory Discovery and Triage

Run the repository's available ecosystem audit during discovery, not only after
an update was already selected. Examples include `npm audit --json`, `pnpm audit
--json`, `cargo audit`, `pip-audit`, `govulncheck`, or `osv-scanner scan source
-r .`. Prefer the project's existing scanner and lockfile owner; do not install
or run a remediation tool merely to manufacture a result.

For every finding that motivates an update, record the advisory ID (GHSA, CVE,
or OSV ID), source, severity, affected package and dependency path, affected
range, and fixed range. Verify from the advisory that the proposed direct or
transitive version is outside the affected range before grouping or publishing.
An audit result is evidence to investigate, not permission to apply a broad
upgrade or a forced major version.

For a transitive-only finding, prefer updating the direct parent that brings in
a fixed transitive version. When no safe parent update exists, use a narrowly
scoped `overrides` entry for npm or pnpm, or `resolutions` for Yarn, and explain
the compatibility tradeoff, advisory, affected path, and removal condition in
the PR. Regenerate the lockfile with its owning package manager, rescan, and do
not leave a broad or unverified override behind.

## 3. Grouping Decision

Group updates by the review question they answer. A reviewer should be able to understand why every package in a PR belongs there. The grouping decision should carry through implementation, commits, and PRs. Do not treat grouping as a planning artifact and then publish everything in one branch.

Good grouping reasons:

- Shared peer dependency constraints.
- Same framework or vendor family.
- One package is an adapter/plugin for another package.
- Type package tracks runtime package.
- Linter/parser/config packages need compatible versions.
- Test runner packages share snapshot, environment, transform, or coverage behavior.
- Security fix requires updating a parent package and a transitive dependency together.

Reasons to split:

- Multiple unrelated major upgrades.
- Different validation surfaces, such as runtime tests versus docs build output.
- Tooling updates that change source code through stricter linting or type analysis.
- Any migration guide with broad local code impact.
- Runtime dependency unrelated to tooling changes.
- Generated output changes that require snapshot review.
- Package lacks release notes and has non-trivial local usage.
- Update touches deployment, auth, payment, database, or security-sensitive code.

Default multi-PR portfolio groups:

| Proposed PR family | Typical packages | Why together | Default validation |
| --- | --- | --- | --- |
| Framework runtime | `next`, `react`, `react-dom`, `@next/*`, framework adapters | Shared runtime/SSR/client rendering behavior and peer constraints | app build, typecheck, focused browser smoke |
| Build tooling | `vite`, `@vitejs/*`, Rollup/esbuild plugins, bundler adapters | Shared build pipeline, output shape, and config semantics | package build, typecheck, build-related tests |
| Lint/format/type tooling | `typescript`, `eslint`, `typescript-eslint`, `biome`, `ultracite`, formatters | Shared static-analysis config and rule fallout | lint, typecheck, formatter check, generated cleanup review |
| Test stack | `vitest`, `jest`, `jsdom`, Testing Library, coverage adapters | Shared runner/environment/snapshot behavior | affected package tests, coverage/snapshot review |
| UI primitives | `@radix-ui/*`, `cmdk`, `react-day-picker`, shadcn-adjacent primitives | Shared component interaction/accessibility surface | UI package tests, app typecheck, browser spot checks when visible |
| Vendor SDK | `@ai-sdk/*`, Supabase, Stripe, PostHog, Sentry, AWS SDK | Shared vendor API surface, auth, telemetry, or billing semantics | focused service tests plus integration checks for touched paths |
| App/runtime island | Cloudflare Worker, docs app, mobile app, separate package manager island | Separate lockfile/deploy target/CI job | that island's install, typecheck, test, deploy dry-run when available |

Do not let the word "tooling" collapse unrelated review questions. For example, Next.js, Vite, ESLint, and TypeScript may all look like tooling in an outdated report, but they often affect different contracts: runtime rendering, bundle output, lint rules, and type analysis. Combine them only when a migration guide or peer dependency constraint makes the coupling real.

Document grouping in a short table:

```markdown
| Proposed PR | Packages | Why together | Risk | Validation |
| --- | --- | --- | --- | --- |
```

Good proposed PRs are named by the thing a reviewer is actually checking:

- `chore(deps): update vitest coverage tooling` for a test runner plus coverage adapter.
- `chore(deps): update docs framework stack` for Ardo, React Router, Vite, React, and docs-only UI migration.
- `chore(deps): update eslint toolchain` for ESLint core, parser, plugins, and the lint cleanup it causes.

If two rows in the table would use different validation commands or require different reviewer knowledge, make them separate PRs by default.

## 4. PR Portfolio and Worktree Plan

For more than one coherent dependency group, produce a PR portfolio before editing:

```markdown
| PR group | Branch/worktree | Packages | Why together | Split from | Risk | Validation |
| --- | --- | --- | --- | --- | --- | --- |
```

Use this table as the execution contract. Each row is normally one branch, one worktree, one commit series, and one ready-for-review PR. Keep the rows small enough that a reviewer can approve or reject the group without reviewing unrelated ecosystem changes.

Worktree workflow:

1. Refresh the default branch before creating worktrees.
2. Create one worktree per PR group from the same refreshed base unless repository policy requires serial rebases.
3. Name branches by the group, for example `codex/deps-next-runtime`, `codex/deps-radix-primitives`, or `codex/deps-vite-build`.
4. Apply only the group's manifests, lockfile changes, generated output, local migrations, and directly-caused code changes inside that worktree.
5. Validate, commit, push, and open a ready-for-review PR for that worktree before moving to an unrelated group. Use draft PRs or keep worktrees local only when the user explicitly asks for planning only, draft PRs, local-only branches, or analysis without PRs.
6. Rebase or regenerate later worktrees after earlier dependency PRs land if they share a lockfile.

Shared lockfiles do not justify a mixed PR by themselves. A pnpm workspace may produce one root lockfile, but each PR still needs a coherent dependency story. If regenerating a lockfile for one group also updates unrelated packages, narrow the package-manager command and regenerate; if the churn remains unavoidable, split it into its own lockfile/tooling PR. Do not hand-delete lockfile entries.

Parallel worktrees are useful for independent groups such as Radix primitives, Cloudflare Worker tooling, and Stripe SDK updates. Prefer serial worktrees for groups that are likely to conflict in the same lockfile or source files, such as Next/React and Testing Library.

## 5. Upstream Research

Research the exact old-to-new range. Prefer primary sources:

- Official changelog or migration guide.
- GitHub releases.
- Git tag compare view.
- Package diff or published tarball diff.
- Docs for changed config/API names.
- Issues and PRs linked from release notes.
- Type definition or generated API diffs.

Capture findings in three layers:

1. **Global upstream summary**: broad themes across the update range.
2. **Local relevance filter**: whether the repository uses the affected APIs/configs.
3. **Action decision**: no action, required migration, beneficial adoption, follow-up, or human decision.

When changelog coverage is missing, state what was checked instead. Examples:

- "No release notes for 2.4.0-2.4.2; checked tag compare and package diff."
- "Migration guide covers only framework apps; local package uses only the CLI, so CLI flags were checked separately."

## 6. Local Impact Analysis

Search for:

- Imports, re-exports, dynamic imports, plugin registrations, config entries, and generated types.
- CLI invocations in package scripts, CI workflows, Dockerfiles, Makefiles, shell scripts, and docs.
- Workarounds, TODOs, comments, issue links, version gates, and local patches.
- Peer dependency assumptions and duplicate transitive versions.
- Snapshot, fixture, schema, generated-code, and lockfile changes.

Classify each relevant upstream item:

| Classification | Meaning | Typical action |
| --- | --- | --- |
| `irrelevant` | Project does not use the feature or code path | Mention only if likely reviewers wonder |
| `covered-by-existing-usage` | Existing usage remains valid | Validate with tests/types |
| `requires-local-change` | Migration needed to keep behavior | Update code/config/docs |
| `enables-local-improvement` | New version removes a limitation or workaround | Adopt when scoped and useful |
| `needs-human-decision` | Product/security/API tradeoff is unclear | Stop or ask before changing behavior |

## 7. Implementation

Use the package manager's normal update path. Avoid hand-editing lockfiles unless the ecosystem expects it.

- Update one proposed PR group at a time.
- Keep generated files and lockfiles in the same commit as their manifest changes.
- Apply required migrations first.
- Apply beneficial local adoption only when the diff remains reviewable and directly connected to the update.
- Update tests or snapshots when behavior intentionally changes.
- Add regression coverage when the dependency update fixes a bug that local code relied on or worked around.

Commit strategy:

- Use one Conventional Commit for small coherent updates.
- Use separate commits for "dependency versions" and "local adoption" when it improves review.
- Keep the commit scope aligned with the PR group, for example `chore(deps): update docs framework stack` or `refactor(docs): adapt ardo ui imports`.
- Avoid mixing unrelated groups in one commit. If the commit message needs "and", split it.
- Use Conventional Commit style when the repository has no stronger convention, for example `chore(deps): update eslint toolchain`.

Publishing strategy:

- Create one branch per proposed PR group by default, usually `codex/update-<group-name>` unless the repository has its own branch convention.
- Prefer separate worktrees for independent PR groups. Check existing worktrees first to avoid branch/path collisions.
- Stage only files that belong to that group. A lockfile can be shared across workspace packages, but the PR should still have a coherent dependency story.
- Push and open a ready-for-review PR for one group before moving to the next unrelated group. Put the researched dependency explanation, validation, risk, and deferred work in the PR body.
- If a repository already has a mixed local diff, either split it into commits/branches carefully or ask before publishing a broad PR.

## 8. Validation

Run checks proportional to the dependency surface:

- Package-manager install/lockfile integrity.
- Typecheck for type or compiler updates.
- Lint/format checks for tooling updates.
- Unit tests for runtime libraries.
- Integration or browser tests for framework/build/runtime changes.
- Snapshot review when generated output changes.
- Security audit or source scan when a security update motivated the change;
  verify the selected version satisfies the advisory's fixed range.

If a full suite is too expensive, run narrow checks first and name the unrun broader checks in the PR. Do not claim safety from a single install command.

## 9. PR Review Package

Prepare reviewers to evaluate the update quickly:

- Explain grouping.
- List old and new versions.
- Summarize upstream changes by local relevance.
- Link primary sources.
- Call out changelog gaps and substitute evidence.
- Explain required migrations and beneficial adoptions.
- Include validation commands and results.
- For advisory-motivated changes, include the advisory ID, severity, dependency
  path, fixed range, and post-update scan result.
- State risk and remaining uncertainty.

Avoid dumping the full changelog. The PR should answer "what does this change for this repository?"

Writing quality:

- Use copywriting discipline: lead with the main review question, then give enough detail to make approval easy.
- Use humanizer discipline: remove stiff AI phrasing, generic praise, empty transitions, and vague claims.
- Prefer concrete local impact over broad upstream summaries.
- Keep bullets readable. One dense bullet that lists every upstream release is worse than two short bullets that explain what changed locally.
- Name deferred work explicitly, especially major upgrades split into follow-up PRs.

Good PR body language:

```markdown
## Why this group
This PR updates the docs framework stack together because Ardo owns the Vite plugin setup and the React Router build path.

## Local migration
- Ardo 3 renamed the UI exports used by the docs app, so `RootLayout`, `Hero`, and `Features` now use their `Ardo*` names.
- Lucide 1 no longer exports the GitHub brand icon from `lucide-react`; the external GitHub link now uses `ExternalLink`.

## Validation
- `pnpm --filter docs build`: passed.
```

Weak PR body language:

```markdown
This update modernizes the docs stack and improves compatibility. It is important to note that the project remains robust and up to date.
```
