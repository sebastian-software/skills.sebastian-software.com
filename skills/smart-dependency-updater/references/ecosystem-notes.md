# Ecosystem Notes

Use this reference for ecosystem-specific commands and update checks. Prefer repository-local scripts and lockfile ownership over generic commands when they conflict.

## JavaScript and TypeScript

Detection:

- `package.json`, `package-lock.json`, `npm-shrinkwrap.json` -> npm
- `pnpm-lock.yaml`, `pnpm-workspace.yaml` -> pnpm
- `yarn.lock`, `.yarnrc.yml` -> Yarn
- `bun.lock`, `bun.lockb` -> Bun

Useful commands:

- `npm outdated`, `npm install <pkg>@<version>`
- `pnpm outdated`, `pnpm update <pkg>@<version>`, `pnpm why <pkg>`
- `yarn outdated` (Yarn 1), `yarn upgrade-interactive` or the outdated plugin
  (Yarn 2+), `yarn npm info <pkg>`, `yarn up <pkg>@<version>`, `yarn why <pkg>`
- `npm view <pkg> versions --json`, `npm view <pkg> peerDependencies --json`

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

Useful commands:

- `cargo tree -i <crate>`
- `cargo update -p <crate>`
- `cargo check`, `cargo test`
- `cargo metadata --format-version 1`

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

Useful commands:

- `python -m pip list --outdated`
- `uv lock --upgrade-package <pkg>`
- `poetry show --outdated`, `poetry update <pkg>`
- `pip-compile --upgrade-package <pkg>` when pip-tools is used

Checks:

- Inspect Python version classifiers and tool config.
- Search imports, entry points, mypy/ruff/pytest configuration, and dependency extras.
- Run test and type/lint commands declared by the project.

Adoption opportunities:

- Replace compatibility imports after minimum Python or package versions move.
- Remove warning filters tied to bugs fixed upstream.
- Adopt typed APIs or safer defaults when local code already touches them.

## Go

Detection:

- `go.mod`, `go.sum`, workspace files.

Useful commands:

- `go list -m -u all`
- `go get module@version`
- `go mod tidy`
- `go test ./...`

Checks:

- Inspect module path changes, minimum Go version, and indirect dependency churn.
- Search public API usage and generated code.
- Run `go test ./...`; add targeted integration checks for networking/database/auth libraries.

## Ruby

Detection:

- `Gemfile`, `Gemfile.lock`, gemspecs.

Useful commands:

- `bundle outdated`
- `bundle update <gem>`
- `bundle exec rake test` or project-specific commands.

Checks:

- Inspect Ruby and Rails version constraints.
- Search initializers, config files, monkey patches, and deprecation suppressions.
- Run focused tests for gems that affect Rails, database, background jobs, or auth.

## Java and JVM

Detection:

- `pom.xml`, `build.gradle`, `build.gradle.kts`, `gradle.lockfile`.

Useful commands:

- Maven Versions Plugin if configured.
- Gradle dependency updates plugin if configured.
- `mvn test`, `./gradlew test`, project-specific check tasks.

Checks:

- Inspect Java version, plugin versions, annotation processors, BOMs, and dependency management blocks.
- Group BOM-managed packages together.
- Search config and generated sources for annotation processor or framework changes.

## .NET

Detection:

- `.csproj`, `.fsproj`, `packages.lock.json`, `Directory.Packages.props`, `global.json`.

Useful commands:

- `dotnet list package --outdated`
- `dotnet add package <pkg> --version <version>`
- `dotnet restore`, `dotnet test`

Checks:

- Inspect target frameworks and central package management.
- Group packages managed through shared props files.
- Search startup/config code for framework or SDK behavior changes.
