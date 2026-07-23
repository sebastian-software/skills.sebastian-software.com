# Ownership and API Design

## Choose Ownership Deliberately

- Accept `&T` when the callee only needs to observe a value and the borrow keeps
  the caller's ownership clear.
- Accept `&mut T` when in-place mutation is the contract. Do not hide mutation
  behind interior mutability merely to make a signature look shared.
- Accept `T` when the operation consumes, stores, transforms, or transfers
  ownership. Use `into_*` only when that transfer is meaningful to callers.
- Return an owned value when it must outlive the input or cross a task, thread,
  cache, or persistence boundary. Do not add `clone()` solely to silence a
  borrow-checker error; first determine which component should own the data and
  for how long.

Prefer the simplest lifetime relationship the API requires. Avoid explicit
lifetime parameters when elision expresses the same contract, but do not use
leaks, global storage, reference counting, or unsafe extension to evade a
misplaced ownership boundary.

## Model Domain Distinctions

Use a newtype, enum, or validated constructor when it prevents a real mix-up:
different identifiers with the same representation, units, lifecycle states,
validated input, or security-sensitive capabilities. Keep construction paths
small and make invalid values unavailable or explicit.

Parse into the valid type instead of validating a string and continuing to pass
the raw string. Preserve the original input only when callers genuinely need
it. Avoid stringly typed states, error categories, feature names, or units when
the set is owned and stable.

Do not wrap primitives by reflex. A type that adds no invariant, meaning, trait
behavior, or future-compatible boundary is ceremony rather than safety.

## Keep Interfaces Deep and Concrete

Start with the concrete function or type that solves the demonstrated need.
Introduce a trait when callers require substitution, multiple implementations
exist or are planned with evidence, or the trait is the stable public contract.
Do not create one-method traits only to mock an internal helper.

Keep public types and trait bounds focused on caller needs:

- hide implementation-only generics and storage choices;
- avoid exposing third-party types unless that coupling is intentional;
- preserve object safety only when dynamic dispatch is an actual requirement;
- use associated types when one implementation determines one related type;
- use generic parameters when callers must choose among types.

Changing a public enum, trait, error type, feature, or auto-trait behavior may be
breaking even when the code still compiles locally. Inspect downstream use,
semver policy, `#[non_exhaustive]`, feature gates, and MSRV before changing it.

## Make Conversions Honest

Use `From`/`Into` for infallible, unsurprising conversions and
`TryFrom`/`TryInto` for range, validation, or representation failures. Avoid
lossy `as` casts where truncation, sign changes, precision loss, or platform
width affects behavior. Name a deliberately lossy conversion so callers can see
the policy.
