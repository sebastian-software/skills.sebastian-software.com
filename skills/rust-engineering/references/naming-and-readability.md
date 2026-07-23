# Naming and Readability

## Name the Contract

Follow repository terminology and Rust conventions. Prefer names that identify
the domain role rather than the representation:

- predicates read naturally with `is_`, `has_`, `can_`, or another precise verb;
- accessors normally use the noun without a `get_` prefix;
- `as_*` borrows or cheaply views, `to_*` creates a value, and `into_*` consumes;
- fallible operations reveal failure through `Result`, `Option`, or a clear
  domain verb rather than a surprising panic;
- include units in the type or name when the type alone cannot express them.

Do not encode implementation history, author narration, or type names that the
signature already makes obvious. Keep one term for one domain concept across
types, variants, functions, fields, tests, logs, and documentation.

## Keep Values Explainable

Name values that carry policy, protocol meaning, a unit, a compatibility limit,
or repeated business intent. Put the unit in the name or type and place the
constant near its owner. A named constant should answer why the value exists,
not merely repeat the digits in uppercase.

Do not introduce generic thresholds for "small" copies, "large" moves, retry
counts, buffer sizes, task counts, or timeouts. Derive them from a protocol,
measurement, product constraint, or repository configuration and document the
reason and review trigger.

Leave a single obvious structural literal local when extracting it would make
the code harder to read. "No magic numbers" means no unexplained policy, not
that every `0`, `1`, or empty value needs a constant.

## Preserve Text Correctness

Rust strings are UTF-8 bytes, not character arrays. Do not slice at an arbitrary
byte offset, assume one byte per visible character, or use `len()` as a user-
visible character count. Choose the semantic unit first:

- bytes for protocols and binary limits;
- Unicode scalar values for code-point processing;
- grapheme clusters for user-perceived characters;
- display width for terminal layout.

Use the repository's existing Unicode support when grapheme or display-width
semantics are required. Do not add a dependency when byte-safe boundary checks,
`chars()`, or a domain-specific parser is sufficient.

## Explain the Why

Prefer a clearer type, name, or helper over a comment that narrates syntax.
Comment non-obvious invariants, compatibility constraints, ordering, ownership,
performance evidence, unsafe reasoning, or external protocol behavior. Keep the
comment beside the contract and turn enforceable parts into types, assertions,
or tests.

Avoid dense iterator or combinator pipelines when they hide ownership changes,
error context, mutation, or early exits. A small explicit loop or `match` is
often the more maintainable Rust.
