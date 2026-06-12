# Forms and State

Use React state and form libraries in ways that preserve browser semantics, data integrity, and user recovery.

## Working Rules

- Decide whether a component is controlled, uncontrolled, form-managed, or derived before implementing.
- Keep form state close to the data flow that owns validation and submission.
- Avoid hiding native input behavior behind custom abstractions unless the replacement preserves labels, autocomplete, focus, and browser cooperation.
- Handle async, optimistic, loading, error, and reset states without losing user input unexpectedly.

## Source-Backed Guidance

