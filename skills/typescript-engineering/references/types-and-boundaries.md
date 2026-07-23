# Types and Boundaries

## Trust the Type System Inside, Validate at the Edge

The strictness settings define what the compiler already guarantees. Inside that
boundary, trust it: do not re-check for `null` where `strictNullChecks` proves
absence is impossible, and do not add defensive runtime guards for shapes the
type already constrains. The rule that changes decisions: every value that
enters from an untyped source — network payloads, `JSON.parse`, `process.env`,
filesystem reads, an untyped or `any`-returning dependency, `unknown` from a
catch — is unproven until a runtime check narrows it. Parse it into a known type
once at that edge, then let the rest of the code rely on the type.

Do not reach for a schema-validation library by default. When the repository
already uses one, follow it. When it does not, a hand-written type guard, a
discriminant check, or a small parse function is often sufficient; add a
dependency only when the validation surface genuinely warrants shared schemas.

## Keep Narrowing and Assertions Honest

Prefer control-flow narrowing (`typeof`, `in`, `instanceof`, equality, and
truthiness) and user-defined type guards whose runtime predicate actually proves
the claimed type. A type guard that returns `x is Foo` after checking one field
is a lie when other fields decide the type — check what the type requires.

A type assertion (`as T`, `as const` aside) and a non-null assertion (`!`) tell
the compiler to trust you. Each is a claim the type system cannot verify:

- use `as` only when you hold knowledge the compiler cannot (a validated
  boundary, a well-known DOM lookup), and prefer a checked narrowing otherwise;
- never launder an incompatible type through `as unknown as T`;
- treat `!` as an assertion that absence is impossible here, not as a shortcut
  to silence `strictNullChecks`.

## Model Closed Sets as Discriminated Unions

For a closed set of variants with different data, prefer a discriminated union
with a literal discriminant over loosely related optional fields or a class
hierarchy. Exhaustiveness then falls out of a `switch` with a `never` default,
so adding a variant surfaces every unhandled site at compile time.

Prefer union-of-literals or `as const` objects over `enum` for most closed sets:
they need no runtime construct, interoperate with plain data, and avoid the
numeric-enum and `const enum` isolation pitfalls. Use `enum` when the repository
already standardizes on it or when a named runtime object genuinely helps.

## Use Generics for Real Variation Only

Add a type parameter when a caller must relate input and output types or choose
a type the function preserves. Do not add generics, conditional types, or mapped
types to look flexible: an unused or always-inferred-as-`unknown` parameter is
ceremony. Constrain parameters (`extends`) so the body can actually use them,
and keep inference predictable for callers.

## Set an `any`/`unknown` Policy

Prefer `unknown` at every boundary where the type is not yet proven, and narrow
before use. Reserve `any` for a deliberate, local, documented escape from a
genuinely untypable construct; it disables checking for every downstream use, so
contain it behind a typed function. Do not spread `any` to make an error
disappear — that moves the failure to runtime and hides it from the next reader.
