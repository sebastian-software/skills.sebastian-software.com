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

### Form Design für Mobile

- Things ID(s): `5P9g7ariJhS7vPPw9GKFaa`
- Source: <https://uxplanet.org/building-great-mobile-forms-2fa8e9a258cc#.k5gdyvljy>
- Decision: `primary`
- Target: `forms-ux`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://uxplanet.org/building-great-mobile-forms-2fa8e9a258cc?gi=548f1be0be62
- Guidance: Primary for forms-ux: mobile forms should minimize taps, prefer visible segmented controls for small option sets, avoid dropdown-heavy flows, use appropriate binary/range/numeric controls, keep forms single-column on small screens, show inline errors, mark optional fields instead of repeating required markers, group related fields, provide comfortable touch areas, and respect platform conventions; cross-reference component-development and ux-patterns.

### Form Usability

- Things ID(s): `TKAxWsA8VEbzoFkewYJ1H8`
- Source: <http://baymard.com/blog/slider-interfaces>
- Decision: `primary`
- Target: `forms-ux`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://baymard.com/blog/slider-interfaces
- Guidance: Primary for forms-ux: sliders are false simplicity unless implemented carefully; use only for exploratory range/filter interaction, account for non-linear value distributions, make dual handles visually unambiguous, define safe click behavior, always provide text input fallbacks for precise values and degraded motor control, and keep live updates low-latency; cross-reference component-development, ux-patterns, and network-performance.

### What’s New With Forms in 2022?

- Things ID(s): `JJZHKZrJk5i4FzRFbfk4HQ`
- Source: <https://css-tricks.com/whats-new-with-forms-in-2022/>
- Decision: `secondary`
- Target: `forms-ux`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for forms-ux with component-development, html-accessibility, and baseline cross-references: useful 2022 forms API radar covering requestSubmit() vs submit(), SubmitEvent.submitter, formdata event, showPicker(), and inert; use to preserve native validation/submission flows and form semantics, but pair individual API rules with current MDN/Baseline docs.

