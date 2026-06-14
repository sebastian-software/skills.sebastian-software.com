# Skill Sync Monorepo Specification

## Purpose

This repository will become the canonical source for Sebastian Software agent
skills. It must keep skills reproducible across machines and team members while
still making skill updates easy to review.

The implementation must use the existing TypeScript-oriented stack. Core
automation must be written in TypeScript and executed through `tsx` during
development. Do not implement the workflow as shell scripts.

The first implementation phase is a pnpm monorepo with a publishable
`skill-sync` CLI package.

## Goals

- Keep local Codex and Agents skill installations in sync with this repository.
- Treat internal Sebastian Software skills as first-party source after import.
- Treat external skills like dependencies: explicitly sourced, locked,
  reviewable, and reproducible.
- Preserve unmanaged local skills by default.
- Provide a DX-oriented CLI and documentation so developers can install,
  validate, update, and review skills without knowing the repo internals.
- Prepare the `skill-sync` CLI for npm publication.

## Non-Goals

- No automatic archiving of old GitHub repositories in the default workflow.
- No direct production updates from external skill sources on developer
  machines.
- No shell-script implementation for install, sync, import, validation, or
  update behavior.
- No destructive exact mirroring of local skill folders by default.

## Repository Layout

```txt
sebastian-software-skills/
  README.md
  spec.md
  package.json
  pnpm-workspace.yaml
  tsconfig.json
  tsconfig.root.json
  eslint.config.ts
  oxlint.config.ts

  packages/
    skill-sync/
      package.json
      tsdown.config.ts
      src/
        cli.ts
        index.ts
      test/

  skills/
    internal/
      s7n-ui-design/
        SKILL.md
        references/

    vendor/
      example-external-skill/
        SKILL.md
        SOURCE.md
        references/

  manifests/
    skills.sources.json
    skills.lock.json

  docs/
    authoring-skills.md
    reviewing-external-skills.md
    sync-workflow.md
    publishing-skill-sync.md

  dist/
    skills/
```

### `packages/skill-sync`

Publishable TypeScript CLI and library package.

Package defaults:

- Package name: `skill-sync`.
- Runtime module format: ESM.
- Node engine: `>=24`.
- Build tool: `tsdown`.
- Dev execution: `tsx`.
- CLI binary: `skill-sync`.
- Test runner: Vitest.

Registry status as of June 9, 2026:

- `npm whoami` succeeds as `swernerx`.
- `npm view skill-sync` returns 404, so the unscoped package name appears
  available.

### `skills/internal`

First-party skills maintained in this repository.

Internal skill install names should use the `s7n-*` prefix. `s7n` is the compact
Sebastian Software namespace and keeps first-party skills distinct from generic
or external skills after installation.

Internal skills may originate from existing Sebastian Software skill
repositories. After import, this repository becomes the source of truth and
future changes happen here through normal pull requests.

Initial internal import candidates:

- `sebastian-software/effective-ui-design-skill`
- `sebastian-software/effective-german-typography-skill`
- `sebastian-software/effective-linkedin-posts`

Old internal skill repositories may be archived only after:

1. the skill was imported,
2. the generated skill output was validated,
3. the first `skill-sync` release is available,
4. consumers were migrated, and
5. the archive action was manually reviewed.

Archiving is not part of the default `skill-sync` command set.

### `skills/vendor`

Approved snapshots of external skills.

External skills are not considered first-party source. They remain dependency
style inputs that are reviewed, locked, and updated intentionally. A vendor
snapshot is allowed when the team wants the external content committed for
reviewability or local patching.

Every vendored external skill must include `SOURCE.md` with:

- original source URL,
- source type,
- imported ref,
- resolved commit or version,
- import date,
- license,
- reviewer,
- local modification status.

### `manifests/skills.sources.json`

Declarative source list for internal imports and external dependencies.

The file should distinguish internal and external sources explicitly:

```json
{
  "internal": [
    {
      "id": "s7n-ui-design",
      "repo": "https://github.com/sebastian-software/effective-ui-design-skill",
      "ref": "main",
      "path": "."
    }
  ],
  "external": [
    {
      "id": "openai-spreadsheets",
      "type": "git",
      "repo": "https://github.com/example/agent-skills",
      "ref": "v1.2.0",
      "include": ["spreadsheets"]
    }
  ]
}
```

### `manifests/skills.lock.json`

Resolved source state used for reproducible imports and updates.

The lockfile must record at least:

- source id,
- source kind (`internal` or `external`),
- source URL,
- requested ref,
- resolved commit or version,
- included skill ids,
- content integrity hash,
- imported or updated timestamp,
- tool version that wrote the entry.

## CLI Requirements

The CLI must be implemented in TypeScript. Commands should be available through
the published `skill-sync` binary and through workspace scripts during
development.

### `skill-sync validate`

Validate repository state.

Checks:

- manifest schema is valid,
- lockfile schema is valid,
- every skill has a `SKILL.md`,
- `SKILL.md` frontmatter contains at least `name` and `description`,
- skill names are unique after flattening,
- referenced files and directories exist,
- paths do not escape the repository root,
- vendor skills include `SOURCE.md`,
- generated dist output is consistent when requested.

### `skill-sync build`

Generate a flat installable skill tree under `dist/skills`.

The output must flatten `skills/internal/*` and approved `skills/vendor/*` into a
single skill directory namespace because local agent runtimes commonly expect a
flat skill folder.

The command must fail on duplicate skill names.

### `skill-sync sync`

Install managed skills into local agent targets.

Required options:

- `--target codex|agents|all`
- `--target-dir <path>` for test and custom installs
- `--dry-run`
- `--verbose`

Default target paths:

- Codex: `~/.codex/skills`
- Agents: `~/.agents/skills`

Default behavior is managed-only:

- Build or read `dist/skills`.
- Copy managed skills into the selected target folders.
- Write `.skill-sync.json` into each managed skill directory.
- Update or remove only directories that contain a valid `.skill-sync.json`
  marker owned by this repo.
- Preserve unmanaged local skill directories.

The marker must include at least:

- source repo path or package identity,
- skill id,
- lockfile digest,
- installed timestamp,
- installed by `skill-sync`.

### `skill-sync import-internal`

Import configured Sebastian Software skill repositories into `skills/internal`.

Behavior:

- Read `manifests/skills.sources.json`.
- Resolve configured refs.
- Clone or fetch into a temporary directory.
- Copy the configured skill root into `skills/internal/<id>`.
- Preserve `SKILL.md`, `references/`, `scripts/`, `assets/`, examples, and
  license files when present.
- Update `manifests/skills.lock.json`.
- Leave the resulting repository diff reviewable.

Internal import does not archive source repositories.

### `skill-sync update-external`

Resolve external source refs and update lock metadata.

Behavior:

- Read external entries from `manifests/skills.sources.json`.
- Resolve the configured ref to an immutable commit or version.
- Update `manifests/skills.lock.json`.
- If the external source is configured for vendoring, copy the selected skill
  snapshot into `skills/vendor/<id>` and update `SOURCE.md`.
- Leave all changes visible in Git for review.

### `skill-sync doctor`

Report local environment and repository health.

The command should check:

- Node version,
- pnpm availability,
- git availability,
- npm authentication state,
- default Codex and Agents target paths,
- whether targets contain managed skills,
- whether manifests and lockfile parse successfully.

## Build And Workspace Scripts

The root workspace should expose developer-friendly scripts:

```json
{
  "scripts": {
    "build": "pnpm -r build",
    "test": "pnpm -r test",
    "typecheck": "pnpm -r typecheck",
    "lint": "pnpm lint:oxlint && pnpm lint:eslint",
    "format": "oxfmt --ignore-path .oxfmtignore --write .",
    "format:check": "oxfmt --ignore-path .oxfmtignore --check .",
    "skill-sync": "tsx packages/skill-sync/src/cli.ts",
    "agent:check": "pnpm lint && pnpm format:check && pnpm typecheck && pnpm build && pnpm test && pnpm skill-sync validate"
  }
}
```

`packages/skill-sync` should use `tsdown` for builds:

```json
{
  "scripts": {
    "build": "tsdown",
    "dev": "tsx src/cli.ts",
    "test": "vitest run",
    "typecheck": "tsc --noEmit"
  }
}
```

## Documentation Requirements

Documentation must be written for developer experience, not only as reference
material.

### `README.md`

Include:

- what this repository is,
- quickstart,
- how to install skills locally,
- how to validate changes,
- how to add or update a skill,
- how internal and external skills differ.

Required quickstart:

```bash
pnpm install
pnpm build
pnpm skill-sync validate
pnpm skill-sync sync --target all
```

### `docs/authoring-skills.md`

Explain:

- required skill structure,
- `SKILL.md` frontmatter expectations,
- naming rules,
- when to use `references/`, `scripts/`, `assets/`, and examples,
- how to keep skills small enough for progressive disclosure.

### `docs/sync-workflow.md`

Explain:

- day-to-day developer sync,
- managed-only behavior,
- target path overrides,
- dry-run usage,
- CI usage.

### `docs/reviewing-external-skills.md`

Include review checklist:

1. source trust,
2. license compatibility,
3. risky or overriding instructions,
4. executable scripts,
5. network access,
6. secret or environment variable access,
7. local filesystem access,
8. relevance to Sebastian Software workflows.

### `docs/publishing-skill-sync.md`

Document first-publish workflow:

```bash
pnpm build
pnpm pack
pnpm publish --dry-run
pnpm publish --tag alpha
```

The real publish must be a reviewed action. The first version should be an
alpha release, for example `0.0.0-alpha.0`.

## Testing Requirements

Use Vitest for unit and integration tests.

Required unit coverage:

- source manifest parsing,
- lockfile parsing and writing,
- path normalization,
- duplicate skill detection,
- marker-file ownership checks,
- target selection logic,
- `SKILL.md` frontmatter validation.

Required integration coverage:

- `skill-sync build` creates a flat `dist/skills` tree,
- duplicate internal/vendor names fail the build,
- managed sync installs into a temporary target directory,
- managed sync preserves unmanaged local skills,
- managed sync updates managed skills,
- Codex and Agents target selection resolves correctly,
- internal import creates reviewable files and lock entries,
- external update writes deterministic lock metadata.

Required package checks:

- built package exposes the `skill-sync` binary,
- `pnpm pack` includes only intended files,
- `pnpm publish --dry-run` succeeds before a real publish.

## Acceptance Criteria

The implementation is complete when:

- `spec.md` has been replaced by this English implementation spec.
- The repo is converted to a pnpm monorepo.
- `packages/skill-sync` exists and can be built with `tsdown`.
- `skill-sync validate`, `build`, `sync`, `import-internal`,
  `update-external`, and `doctor` are implemented.
- Initial internal skill sources are represented in `skills.sources.json`.
- Internal skills can be imported into `skills/internal`.
- Local sync works for both `~/.codex/skills` and `~/.agents/skills`.
- Unmanaged local skills are preserved by default.
- DX documentation exists for authoring, syncing, reviewing, and publishing.
- Tests and package dry-run checks pass.

## First Commit Scope

The first commit must modify only `spec.md`.

Commit message:

```txt
docs: replace skill sync implementation spec
```

No package scaffolding, implementation files, documentation files, manifests, or
imported skills belong in the first commit.
