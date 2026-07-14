# Complexity Lens

Use this lens when choosing an implementation or reviewing overengineering.
Reduce owned complexity without reducing understanding, safety, or required
capability.

## The Ladder

Stop at the first option that satisfies the real requirement:

1. **Need:** Is the capability required now, or is it speculative? Do not argue
   away something the user explicitly requested; clarify the smallest useful
   outcome when scope is ambiguous.
2. **Existing path:** Search for an existing helper, component, type, policy,
   query, or pattern and reuse it when it still fits.
3. **Platform primitive:** Prefer the language standard library, browser or OS
   capability, database constraint, protocol, or framework primitive when it
   covers the semantics and support target.
4. **Installed dependency:** Reuse an appropriate maintained dependency already
   owned by the project before adding another overlapping tool.
5. **Small clear implementation:** Write the minimum explicit code that handles
   the required states and edge cases.
6. **New dependency or abstraction:** Add one only when it reduces net ownership
   across real callers, not for a hypothetical future variation.

Inspect the affected flow before climbing the ladder. A small edit in the wrong
place creates more work than a slightly larger root-cause fix.

## Root-Cause Placement

Before patching a reported symptom:

- Trace callers, siblings, state ownership, and the boundary where the invalid
  behavior first becomes possible.
- Prefer one correction at the shared invariant over repeated guards in every
  consumer.
- Avoid centralizing behavior whose callers intentionally have different
  semantics.
- Add a regression check at the narrowest layer that proves the real failure.

## Quality Guardrails

Never simplify away:

- validation and authorization at trust boundaries;
- accessibility semantics, keyboard paths, or user recovery;
- error handling needed to prevent data loss or silent corruption;
- observability required to diagnose consequential failures;
- explicit compatibility, regulatory, or user requirements;
- calibration or tolerance required by physical systems;
- meaningful tests for risky logic.

Line count is not the quality metric. Compare cognitive load, public surface,
failure modes, blast radius, dependencies, runtime cost, and maintenance
ownership. Boring and readable beats both ceremony and clever compression.

## Deliberate Simplifications

When accepting a bounded shortcut, record:

- what was simplified;
- the known ceiling or lost capability;
- the measurable trigger for revisiting it;
- where the follow-up is owned.

Use an ADR for a durable cross-cutting tradeoff, the project's issue or backlog
for delivery debt, and a normal nearby code comment only when future maintainers
need the constraint at that exact line. Do not invent a proprietary comment
prefix or ledger.

Test in proportion to risk and repository convention. A trivial expression may
need no new test; parsers, money, auth, migrations, concurrency, and shared
policy usually require focused regression coverage.
