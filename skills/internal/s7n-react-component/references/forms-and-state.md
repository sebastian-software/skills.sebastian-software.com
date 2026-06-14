# Forms and State

Use React state and form libraries in ways that preserve browser semantics, data integrity, and user recovery.

## Working Rules

- Decide whether a component is controlled, uncontrolled, form-managed, or derived before implementing.
- Keep form state close to the data flow that owns validation and submission.
- Avoid hiding native input behavior behind custom abstractions unless the replacement preserves labels, autocomplete, focus, and browser cooperation.
- Handle async, optimistic, loading, error, and reset states without losing user input unexpectedly.

## Source-Backed Guidance
### Conditionally Render Fields Using React Hook Form

- Things ID(s): `Jy7y4NBbS9Vxf8Ri6E9QbE`
- Source: <https://echobind.com/post/conditionally-render-fields-using-react-hook-form?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23125%3A+tRPC%2C+T3%2C+Remix%2C+Zustand%2C+Server+Components%2C+Drag+%26+Drop%2C+Forms%2C+Gatsby%2C+Remotion%2C+React-Native%2C+Skia...%20-%209471615>
- Decision: `secondary`
- Target: `react-state`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as React Hook Form conditional-field guidance; keep conditional fields aligned with validation, unregistering, and user-visible state.
### Data Binding in React

- Things ID(s): `Tb378Xb9Q4P6En1cQMtC7h`
- Source: <https://www.joshwcomeau.com/react/data-binding/>
- Decision: `secondary`
- Target: `react-state`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use data-binding guidance to decide controlled, uncontrolled, and derived form state boundaries.
### React Hooks: The Deep Cuts

- Things ID(s): `bjSgb8q93XCZg6yU6BGtg`
- Source: <https://css-tricks.com/react-hooks-the-deep-cuts/>
- Decision: `secondary`
- Target: `react-state`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as hooks-depth context; apply only when hook abstractions clarify ownership and effects rather than hiding state flow.

### Building Great Forms with React Hook Form & Zod

- Things ID(s): `E8u8Sr7ycgD6XPaL3WknM8`
- Source: <https://m.youtube.com/watch?v=FXWD_etMJWA>
- Decision: `secondary`
- Target: `react-state`
- Transcript extraction: 2026-06-14, 13,185 words
- Guidance: Use as practical React Hook Form + Zod implementation context. Keep schema validation, field registration, error presentation, default values, reset behavior, and submission state aligned with native form semantics and user recovery.
