# Module and API Design

## Design the Public Surface Deliberately

Export the smallest set of types and functions that solves the demonstrated
need. What a module exports is a contract: a consumer can depend on any exported
type, so hide implementation-only types, internal helpers, and storage shapes.
Prefer named exports over a default export for discoverability and refactoring,
unless the repository or ecosystem convention (or a framework's module contract)
requires a default.

Keep the type surface concrete first. Introduce an interface, generic, or
overload when callers require substitution or type relation, not to look
extensible. Prefer `interface` for object contracts meant to be implemented or
extended, and `type` for unions, tuples, mapped, and conditional shapes; follow
the repository's existing choice when it is consistent.

## Weigh Barrel Files Against Their Cost

A barrel (`index.ts` re-exporting a directory) can give a clean public entry
point, but re-exporting everything couples unrelated modules, defeats tree
shaking for CJS and some bundler configurations, and creates import cycles that
surface as `undefined` at runtime. The rule that changes decisions: use a barrel
as a curated public API for a package or a stable boundary, not as an automatic
re-export of every internal file. Import deep paths internally to avoid cycles
and keep the dependency graph honest.

## Respect ESM/CJS and `package.json` Reality

Module format is a runtime contract, not a stylistic choice. Before changing
imports or output:

- check `"type"` in `package.json`, the `tsconfig` `module` and
  `moduleResolution` settings, and whether consumers are ESM, CJS, or both;
- in ESM, relative imports need explicit extensions in the emitted form; a
  default import of a CJS module goes through interop and may not behave like a
  named import;
- when a package ships both formats, the `exports` map — not the legacy `main`
  or `module` — decides what each condition (`import`, `require`, `types`)
  resolves to. A missing or wrong `types` condition breaks consumers silently;
- do not switch a package's module system, drop the `exports` map, or change the
  emitted target as incidental cleanup; it is a breaking change for consumers.

## Treat Exported Types as Semver Surface

A change to an exported type can break downstream compilation even when the local
build passes. Narrowing a parameter type, widening a return type, adding a
required field, removing a union member, or making an optional field required is
a breaking change. Adding an optional field or a new union member can also break
exhaustive consumers. Inspect downstream use, the package's stability promise,
and whether the type is genuinely public before changing it, and describe the
compatibility impact rather than assuming a green local build means safe.
