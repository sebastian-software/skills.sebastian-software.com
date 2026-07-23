[← Sebastian Software Skills](../../README.md)

# TypeScript Engineering

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Write and review server-side and general TypeScript whose type, module,
async, and error contracts stay honest under change.**

TypeScript Engineering gives agents a strict but evidence-led standard for
non-frontend TypeScript implementation and review. It favors honest narrowing
over defensive casts, runtime validation only at the untyped edge,
discriminated unions over loose flags, owned promises and real cancellation,
typed errors with cause chains, and the repository's own `tsconfig`, lint, and
module contract over ambient strictness fashions.

## What It Can Deliver

- TypeScript implementations with honest narrowing, guarded assertions, and a
  deliberate `any`/`unknown` policy
- domain types that make invalid states unrepresentable without nominal-type
  ceremony
- module and package APIs with a controlled export surface, sane barrels, and
  correct ESM/CJS and `package.json` `exports`
- promise-owning, cancellation-aware async code with typed errors and `cause`
  chains
- `tsconfig`, build-target, and lint decisions grounded in the actual runtime
  and repository convention
- TypeScript-depth review findings, grounded in strictness, module, and
  compatibility contracts, for a code review owned by PR Review

## Use It When

Use this skill while implementing, refactoring, or reviewing server-side or
shared-library TypeScript, especially around type-system decisions, public
module and package APIs, ESM/CJS boundaries, async and cancellation, typed
errors, or `tsconfig` and toolchain meaning.

It does not replace the owner skills for pull-request lifecycle and merge
judgment, frontend and React work, test design, TSDoc, dependency updates,
repository-wide audits, behavior-preserving ports, or execution of existing
checks.

## Example Prompts

```text
Review this TypeScript service for null handling, unsafe casts, floating
promises, and public type compatibility.

Refactor this job type into a discriminated union so illegal field
combinations are unrepresentable and handling is exhaustive.

Make this async worker propagate AbortSignal cancellation and represent
expected failures as typed errors with cause chains.

Implement this module's public API without repairing type errors with `as any`,
adding a validation library by default, or blanket-enabling strict flags.
```

See [SKILL.md](SKILL.md) for the workflow, operating rules, and routing
boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill typescript-engineering
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian typescript-engineering
dalo approve skill sebastian:typescript-engineering
dalo sync
```

## Related Skills

- [PR Review](../pr-review/README.md) owns pull-request lifecycle, approval, CI
  recovery, and merge judgment; this skill supplies the TypeScript-depth
  findings inside a review.
- [Effective Web](../effective-web/README.md) owns frontend, React, browser, and
  browser-facing TypeScript; this skill owns non-frontend and shared-library
  TypeScript depth.
- [Software Testing](../software-testing/README.md) owns focused TypeScript test
  design and implementation against the contracts established here.
- [Tech Docs](../tech-docs/README.md) owns TSDoc, examples, and contributor
  documentation.
- [Software Validation](../software-validation/README.md) discovers and runs the
  repository's established typecheck, lint, build, and test checks.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) owns package
  selection and version updates.
- [Port Codebases](../port-codebases/README.md) owns behavior-preserving moves
  into or out of TypeScript.

## Scope

This skill does not impose one validation library, test runner, bundler, lint
set, module system, package manager, or strictness level beyond what the
repository has adopted. It does not authorize unrelated cleanup, dependency
additions, public API breaks, or codebase-wide strict-flag or module-system
migrations bundled into a feature change. Frontend and browser TypeScript stays
with `effective-web`; test evidence stays with `software-testing`.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
