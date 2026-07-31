# Unsafe and FFI

Unsafe Rust is a proof obligation, not an optimization label. Keep the unsafe
surface smaller than the safe contract it supports and reject unsafe code when
the invariant cannot be stated and checked.

## Establish the Safety Proof

For every unsafe operation, verify the relevant facts:

- **provenance and ownership:** where each pointer or handle came from, who may
  read, write, move, free, or retain it, and whether the allocation still lives;
- **validity and initialization:** which bit patterns and states are valid,
  which fields are initialized, and whether reads can observe uninitialized
  memory;
- **alignment, bounds, and layout:** required alignment, allocation extent,
  offset arithmetic, representation, ABI, and target assumptions;
- **aliasing and mutation:** which references or raw pointers coexist and which
  exclusive-access guarantee makes mutation sound;
- **lifetimes and pinning:** what prevents use after free, relocation, or a
  reference outliving its backing storage;
- **drop and unwind:** exactly-once cleanup, partial initialization, panic or
  unwind behavior, and ownership transfer on every return path;
- **thread safety:** why shared state satisfies `Send` and `Sync`, including
  callbacks, thread affinity, and foreign-library guarantees.

Write a `SAFETY:` comment next to the unsafe operation that connects the code to
these facts. Avoid comments that merely say the operation was reviewed.

## Contain the Boundary

Expose a small safe API that validates preconditions before entering unsafe
code. Keep raw pointers and foreign representations inside the owning module.
Use the smallest unsafe block that still leaves the invariant understandable;
do not mark an entire function unsafe to avoid identifying individual
operations.

An `unsafe fn` must document the caller's obligations in `# Safety`. Inside it,
keep unsafe operations explicit according to the repository's edition and lint
policy. Review Rust 2024 unsafe attributes and extern-block requirements when
the crate uses or migrates to that edition; do not backport syntax blindly to a
different MSRV.

## Review FFI as a Protocol

Verify ABI, calling convention, integer widths, layout, nullability,
NUL-termination, encoding, allocation owner, callback lifetime, thread
affinity, and error transfer against the foreign declaration or specification.
Never let a Rust panic unwind through a boundary that does not explicitly
support it. Represent foreign handles with one clear owner and make close/free
idempotency or exactly-once behavior explicit.

## Validate Proportionately

Add a focused safe-boundary test for the contract. Use Miri, sanitizers,
fuzzing, loom-like concurrency exploration, or target-specific CI only when the
repository supports the tool and the risk warrants it. Passing dynamic checks
does not replace the written safety proof; an unexercised invalid path can still
be unsound.
