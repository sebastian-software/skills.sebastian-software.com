# Route: TypeScript Engineering

Write TypeScript that makes types, module boundaries, failure, and async
ownership honest to the next maintainer. Prefer repository evidence and the
type system over ambient strictness fashions, defensive `any`, or speculative
abstraction. The compiler is a contract, not a lint to be silenced.

Scope: server-side, shared-library, and general TypeScript. Browser-facing
TypeScript belongs to `effective-web`.

## Establish the Contract

1. Read scoped instructions, `tsconfig.json` (and any extended base or project
   references), `package.json`, lockfile, CI, lint and format policy, relevant
   ADRs, public entry points, nearby types, and representative call sites.
   Discover the compiler strictness, module and target settings, runtime
   (Node LTS, edge, worker, browser), module system (ESM/CJS), package manager,
   and repository-native commands.
2. State the changed behavior and boundaries: inputs, outputs, nullability,
   ownership of promises and resources, expected errors, cancellation,
   concurrency, and which values cross an untyped runtime boundary. Do not
   invent a stricter compiler flag set, a validation library, a bundler, or a
   runtime target the repository has not adopted.
3. Read [Types and boundaries](typescript-types-and-boundaries.md) for
   strictness contracts, honest narrowing and assertions, discriminated unions
   versus enums, generics restraint, the `any`/`unknown` policy, and where
   runtime validation replaces compile-time trust.
4. Read [Module and API design](typescript-module-and-api-design.md) for
   exports, barrel-file tradeoffs, ESM/CJS interop, `package.json` `exports`,
   and the semver surface of a public type.
5. Read [Async and errors](typescript-async-and-errors.md) when the change
   returns a promise, spawns background work, can be cancelled, or fails.
6. Read [Tooling and config](typescript-tooling-and-config.md) for the
   meaning-bearing `tsconfig` options, build and runtime targets, and lint and
   format conventions the repository already owns.
7. Read [Quality and review](typescript-quality-and-review.md) before declaring
   the change ready.

## Implementation Rules

- Make invalid states unrepresentable when the domain distinction is stable and
  valuable: discriminated unions for closed variant sets, branded types for
  identifiers that share a primitive, `readonly` where mutation is not the
  contract. Do not wrap every primitive in a nominal type by reflex.
- Trust the compiler inside the type boundary and validate at the untyped edge.
  Parse external input (network, filesystem, environment, `JSON.parse`, `any`
  from an untyped dependency) into a known type once; do not re-validate values
  the type system already guarantees.
- Keep narrowing honest. Prefer control-flow narrowing, `in`, `typeof`, and
  user-defined type guards whose runtime check actually proves the type. A type
  assertion or `as` cast claims knowledge the compiler lacks — justify it or
  replace it with a checked narrowing.
- Reserve `any` for a deliberate, documented escape; prefer `unknown` at
  boundaries and narrow before use. Do not repair a type error with `as any`,
  `as unknown as T`, `@ts-ignore`, or `@ts-expect-error` without stating why
  the suppression is sound and when it can be removed.
- Own every promise: await it, return it, or attach a deliberate handler.
  Propagate cancellation through `AbortSignal` rather than orphaning work.
  Model expected failure as a typed result or a typed error with a `cause`
  chain; reserve thrown exceptions for genuinely exceptional paths.
- Design the public surface smaller than the implementation. Add a generic
  parameter, overload, or conditional type only for demonstrated variation;
  hide implementation-only types, and treat a change to an exported type as
  potentially breaking even when local code still compiles.
- Follow the repository's `tsconfig`, lint, and format contract. Do not
  blanket-enable every strict flag, migrate module resolution, or add a
  formatter against the established convention as incidental cleanup.

## Review Output

For a review, report only findings that can affect correctness, type soundness,
compatibility, performance, or maintainability. Tie each finding to a concrete
path and contract, distinguish a verified defect from a risk or preference, and
propose the smallest correction consistent with repository conventions.

For an implementation, summarize the type, module, and failure decisions, name
the focused evidence run, and state unverified runtime, platform, or
compatibility claims explicitly.

## Cross-links

- Module and service boundary decisions for a TypeScript system are the
  Architecture route; this route implements quality within an agreed boundary.
- Test selection and implementation are the Testing route; this route owns the
  TypeScript contracts the tests must protect.
- Frontend, React, browser, DOM, CSS, accessibility, and browser-facing
  TypeScript belong to `effective-web`.
- Pull-request lifecycle, approval, CI recovery, merge judgment, ports, TSDoc
  and contributor documentation, package selection and version updates,
  repository-wide audits and implementation plans, and execution of existing
  format, lint, typecheck, build, or test commands belong to
  `effective-delivery`. This route supplies TypeScript-depth findings inside a
  review and a post-parity idiom pass on ported code.

Do not turn this route into a parallel test, documentation, dependency, or
delivery system.
