# Route: TypeScript Engineering

Write TypeScript that makes types, module boundaries, failure, and async
ownership honest to the next maintainer. Prefer repository evidence and the
type system over ambient strictness fashions, defensive `any`, or speculative
abstraction. The compiler is a contract, not a lint to be silenced.

Scope: server-side, shared-library, and general TypeScript. Browser-facing
TypeScript belongs to `effective-web`.

## Establish the Contract

1. Read scoped instructions and the affected code and tests. Inspect compiler
   settings, package/runtime contracts, CI, accepted decisions, and public
   consumers when they constrain the change. Use repository-native commands.
2. State the changed behavior and boundaries: inputs, outputs, nullability,
   ownership of promises and resources, expected errors, cancellation,
   concurrency, and which values cross an untyped runtime boundary. Do not
   invent a stricter compiler flag set, a validation library, a bundler, or a
   runtime target the repository has not adopted.
3. Read [Types and boundaries](typescript-types-and-boundaries.md) when changing
   types, narrowing, generics, assertions, or runtime validation boundaries.
4. Read [Module and API design](typescript-module-and-api-design.md) when
   changing exports, module boundaries, ESM/CJS interop, or a public type.
5. Read [Async and errors](typescript-async-and-errors.md) when the change
   returns a promise, spawns background work, can be cancelled, or fails.
6. Read [Tooling and config](typescript-tooling-and-config.md) when compiler,
   build/runtime targets, lint, or formatting configuration is in scope.
7. Read [Quality and review](typescript-quality-and-review.md) when TypeScript
   review or verification choices need guidance.
8. Read [Source-verified external contracts](source-verified-external-contracts.md)
   when a framework, runtime, dependency, or platform behavior materially
   affects a consequential implementation or public contract.

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
