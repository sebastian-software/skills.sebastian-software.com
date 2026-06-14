# Forms and State

Use React state and form libraries in ways that preserve browser semantics, data integrity, and user recovery.

## Working Rules

- Decide whether a component is controlled, uncontrolled, form-managed, or derived before implementing.
- Keep form state close to the data flow that owns validation and submission.
- Avoid hiding native input behavior behind custom abstractions unless the replacement preserves labels, autocomplete, focus, and browser cooperation.
- Handle async, optimistic, loading, error, and reset states without losing user input unexpectedly.

## Additional Rules

- Use as React Hook Form conditional-field guidance; keep conditional fields aligned with validation, unregistering, and user-visible state.
- Use data-binding guidance to decide controlled, uncontrolled, and derived form state boundaries.
- Use as hooks-depth context; apply only when hook abstractions clarify ownership and effects rather than hiding state flow.
- Use as practical React Hook Form + Zod implementation context. Keep schema validation, field registration, error presentation, default values, reset behavior, and submission state aligned with native form semantics and user recovery.
