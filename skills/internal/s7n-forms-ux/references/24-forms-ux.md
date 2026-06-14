# Forms UX

Design forms around user recovery: clear labels, browser-supported input attributes, tolerant validation, meaningful error messages, and submission flows that preserve native behavior.

## Working Rules

- Choose `type`, `name`, `autocomplete`, `inputmode`, and `enterkeyhint` intentionally.
- Validate after useful interaction, not at first keystroke.
- Preserve paste, autofill, password managers, native validation, and submitter semantics unless there is a specific risk.
- Pair custom widgets with precise keyboard, focus, error, and fallback behavior.
- Provide text input fallbacks for controls such as sliders when precision matters.

## Additional Rules

- Do not disable autocomplete globally; use autocomplete tokens intentionally, preserve input-purpose identification, allow password managers, and disable autocomplete only for temporary or sensitive values such as OTPs, unique identifiers, or CVV-like fields; connect to html-accessibility and security/privacy.
- Mobile forms should minimize taps, prefer visible segmented controls for small option sets, avoid dropdown-heavy flows, use appropriate binary/range/numeric controls, keep forms single-column on small screens, show inline errors, mark optional fields instead of repeating required markers, group related fields, provide comfortable touch areas, and respect platform conventions; connect to component-development and ux-patterns.
- Sliders are false simplicity unless implemented carefully; use only for exploratory range/filter interaction, account for non-linear value distributions, make dual handles visually unambiguous, define safe click behavior, always provide text input fallbacks for precise values and degraded motor control, and keep live updates low-latency; connect to component-development, ux-patterns, and network-performance.
- 2022 forms API radar covering requestSubmit() vs submit(), SubmitEvent.submitter, formdata event, showPicker(), and inert; use to preserve native validation/submission flows and form semantics, but pair individual API rules with current MDN/Baseline docs.
