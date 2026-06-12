# Forms UX

Design forms around user recovery: clear labels, browser-supported input attributes, tolerant validation, meaningful error messages, and submission flows that preserve native behavior.

## Working Rules

- Choose `type`, `name`, `autocomplete`, `inputmode`, and `enterkeyhint` intentionally.
- Validate after useful interaction, not at first keystroke.
- Preserve paste, autofill, password managers, native validation, and submitter semantics unless there is a specific risk.
- Pair custom widgets with precise keyboard, focus, error, and fallback behavior.
- Provide text input fallbacks for controls such as sliders when precision matters.

## Source-Backed Guidance

### Disable Auto Complete (DOM)

- Things ID(s): `JDbStG1Z3KoGW3jhnejquP`
- Source: <https://developer.mozilla.org/en-US/docs/Web/Security/Securing_your_site/Turning_off_form_autocompletion>
- Decision: `primary`
- Target: `forms-ux`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Turning_off_form_autocompletion
- Guidance: Primary for forms-ux: do not disable autocomplete globally; use autocomplete tokens intentionally, preserve input-purpose identification, allow password managers, and disable autocomplete only for temporary or sensitive values such as OTPs, unique identifiers, or CVV-like fields; cross-reference html-accessibility and security/privacy.

