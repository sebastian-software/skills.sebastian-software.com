# Code Documentation

## Document semantics, not syntax

Use in-code documentation for a public or reused contract, an invariant,
non-obvious rationale, side effect, failure mode, concurrency rule, ownership
boundary, safety condition, or example that a maintainer or caller needs.

Do not add comments that merely translate the next line into prose. Prefer a
clearer name or smaller function when the code itself can carry the meaning.
Remove or update comments that contradict the current implementation.

## JSDoc and TSDoc

Follow the repository's chosen convention and supported toolchain. In
TypeScript, the signature already owns parameter and return types; describe
meaning, units, valid ranges, defaults, mutation, ownership, errors,
deprecation, and usage that the type system cannot express. In JavaScript,
type-bearing JSDoc may also be part of the checked interface.

Use tags only when the project's compiler, linter, documentation generator, or
editor workflow supports them. Keep parameter names synchronized with the
signature. Verify links, overload behavior, inherited documentation, and
generated API output when those surfaces are part of the project.

## rustdoc

Give crates and modules a concise purpose and a realistic first example. For a
public item, start with a useful summary, then explain important semantics and
provide an example when it clarifies correct use.

Add conventional sections such as `# Errors`, `# Panics`, or `# Safety` only
when the contract has that behavior. Explain the triggering conditions rather
than repeating that an error, panic, or unsafe operation exists. Prefer
intra-doc links and executable documentation examples supported by the crate.

Document ownership transfer, borrowing, mutation, cancellation, ordering,
feature gates, units, and platform limits when callers need them. In `# Safety`,
state the caller obligations that make the operation sound; a warning that an
item is unsafe is not a contract. Keep examples Unicode-safe: do not demonstrate
arbitrary byte slicing when the prose promises characters or display width.

## Explanatory comments and docstrings

- Explain why a constraint or unusual approach exists and what would break if
  it changed.
- Place the explanation beside the code or contract it qualifies.
- Reference a stable issue, specification, or decision only when that source
  will help future maintainers recover the rationale.
- Avoid timelines, author narration, and temporary implementation notes unless
  the repository has an explicit convention for them.
- Turn enforceable invariants into types, assertions, or tests where possible;
  keep the comment for context the mechanism cannot express.

Review documentation together with the interface it describes. A correct
comment on an obsolete API is still stale documentation.
