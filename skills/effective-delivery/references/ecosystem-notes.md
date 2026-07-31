# Ecosystem Notes

Use this reference for the non-obvious ecosystem-specific commands and update
checks. Prefer repository-local scripts and lockfile ownership over generic
commands when they conflict. Baseline package-manager usage (`npm outdated`,
`bundle outdated`, `go list -m -u all`, `dotnet list package --outdated`, and
similar) is assumed; only the deltas worth remembering are listed here.

## JavaScript and TypeScript

Detection:

- `package.json`, `package-lock.json`, `npm-shrinkwrap.json` -> npm
- `pnpm-lock.yaml`, `pnpm-workspace.yaml` -> pnpm
- `yarn.lock`, `.yarnrc.yml` -> Yarn
- `bun.lock`, `bun.lockb` -> Bun

Non-obvious deltas:

- Yarn 2+ ships no built-in `outdated`; use a third-party plugin such as
  `yarn-plugin-outdated`, or `yarn npm info <pkg>` per package. Yarn 1's
  `yarn outdated` still exists.
- `pnpm why <pkg>` / `yarn why <pkg>` explain transitive pulls before you
  decide where to update.
- `npm view <pkg> peerDependencies --json` catches peer-range breaks before
  install does.
- For transitive-only security fixes, use narrowly scoped `overrides` (npm,
  pnpm) or `resolutions` (Yarn); regenerate the lockfile with its owner,
  rescan, and record the removal condition (see the workflow reference, §2a).

Checks:

- Read `engines`, `packageManager`, workspace config, and CI Node version.
- Inspect `peerDependencies` for React, Next, Vite, ESLint, Jest/Vitest, TypeScript, Rollup/Webpack, Babel/SWC, and framework plugins.
- Search scripts and CI for CLI flags that may have changed.
- For type-related updates, run typecheck and inspect changed generated type output.
- For build tools, run build plus a focused runtime or browser check where available.

Adoption opportunities:

- Remove polyfills or plugin workarounds fixed by the new framework/tool version.
- Switch deprecated config keys to current names.
- Use stricter or safer TypeScript/ESLint options only when the repo can absorb the resulting changes.
- Replace manual type shims after packages ship better definitions.

## Rust

Detection:

- `Cargo.toml`, `Cargo.lock`, workspace table.

Non-obvious deltas:

- `cargo update <crate>` takes the crate positionally; `-p <crate>` is a
  documented alias for the same selection.
- `cargo tree -i <crate>` inverts the tree to show who pulls a crate in.
- `cargo outdated` is a third-party install, not built in.

Checks:

- Inspect MSRV policy before updating crates that changed edition or rust-version.
- Read feature flags and default-feature changes.
- Search for trait implementations, derive macros, builder APIs, and error types from updated crates.
- For proc macros or serialization crates, run tests that exercise generated code.

Adoption opportunities:

- Remove local wrappers after crates add stable helpers.
- Use improved error/context APIs when it simplifies code without broad churn.
- Update feature flags to avoid deprecated optional dependencies.

## Python

Detection:

- `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`, `setup.cfg`, `setup.py`.

Non-obvious deltas:

- The lockfile decides the tool: `uv lock --upgrade-package <pkg>`,
  `poetry update <pkg>`, or `pip-compile --upgrade-package <pkg>` (pip-tools).
  Do not mix them against the same lock state.

Checks:

- Inspect Python version classifiers and tool config.
- Search imports, entry points, mypy/ruff/pytest configuration, and dependency extras.
- Run test and type/lint commands declared by the project.

Adoption opportunities:

- Replace compatibility imports after minimum Python or package versions move.
- Remove warning filters tied to bugs fixed upstream.
- Adopt typed APIs or safer defaults when local code already touches them.

## Go

Detection: `go.mod`, `go.sum`, workspace files.

Checks:

- Watch for module path changes on majors (`/v2` suffixes), minimum Go version
  bumps, and indirect dependency churn; run `go mod tidy` after edits.
- Search public API usage and generated code; add targeted integration checks
  for networking/database/auth libraries.

## Ruby

Detection: `Gemfile`, `Gemfile.lock`, gemspecs.

Checks:

- Inspect Ruby and Rails version constraints.
- Search initializers, config files, monkey patches, and deprecation
  suppressions; run focused tests for gems that affect Rails, database,
  background jobs, or auth.

## Java and JVM

Detection:

- `pom.xml`, `build.gradle`, `build.gradle.kts`, `gradle.lockfile`.

Non-obvious deltas:

- Version discovery needs the Maven Versions Plugin or a Gradle
  dependency-updates plugin; use them only when the repository already
  configures one.
- Group BOM-managed packages together: a BOM or `dependencyManagement` block
  owns the versions, so update the BOM, not each member.

Checks:

- Inspect Java version, plugin versions, annotation processors, BOMs, and dependency management blocks.
- Search config and generated sources for annotation processor or framework changes.

## .NET

Detection:

- `.csproj`, `.fsproj`, `packages.lock.json`, `Directory.Packages.props`, `global.json`.

Non-obvious deltas:

- With central package management, `Directory.Packages.props` owns the
  versions; update it and group the packages it manages together.

Checks:

- Inspect target frameworks and `global.json` SDK pinning.
- Search startup/config code for framework or SDK behavior changes.
