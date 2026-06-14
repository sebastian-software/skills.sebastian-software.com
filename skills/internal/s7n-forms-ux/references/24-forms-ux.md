# Forms UX

Design forms around user recovery: clear labels, browser-supported input attributes, tolerant validation, meaningful error messages, and submission flows that preserve native behavior.

## Working Rules

- Choose `type`, `name`, `autocomplete`, `inputmode`, and `enterkeyhint` intentionally.
- Validate after useful interaction, not at first keystroke.
- Preserve paste, autofill, password managers, native validation, and submitter semantics unless there is a specific risk.
- Pair custom widgets with precise keyboard, focus, error, and fallback behavior.
- Provide text input fallbacks for controls such as sliders when precision matters.

## Native Form Behavior

Preserve the browser's form model unless replacing it solves a real product problem.

- Use real `<form>`, `<label>`, `<input>`, `<select>`, `<textarea>`, `<button>`, `<fieldset>`, and `<legend>` elements where they fit.
- Use `requestSubmit()` instead of `.submit()` when triggering form submission from script, because it preserves validation and submitter behavior.
- Use submitter-aware flows for multiple submit buttons. The clicked button may change intent, validation, destination, or confirmation copy.
- Use the `formdata` event or framework equivalent when augmenting submission data without disconnecting controls from native form semantics.
- Avoid global `novalidate` or custom validation layers that hide browser input purpose, mobile keyboards, password managers, or autofill.

## Validation Timing

Validation should help recovery, not punish exploration.

- Do not show red error states on first render.
- Do not validate every keystroke unless the feedback is genuinely useful and non-disruptive, such as password strength or username availability with debounce.
- Prefer `:user-invalid` / `:user-valid` when supported, with submit-time fallback for older browsers.
- Keep error text adjacent to the field, programmatically associated, and specific enough to fix the issue.
- Preserve user input after failed submit, navigation errors, server validation, and auth timeouts.

## Mobile and Touch Forms

- Keep narrow-screen forms single-column unless a grouped multi-field pattern is easier to scan.
- Prefer segmented controls, radios, steppers, or text inputs over dropdowns for small option sets.
- Keep targets comfortable for coarse pointers: 44-48 CSS px for common controls, with adequate spacing.
- Do not infer touch from viewport width. Use pointer/hover capabilities and test hybrid devices.
- Use `autocomplete` tokens for names, email, addresses, one-time codes, and payment fields where appropriate.
- Use `inputmode` to tune keyboard layout without changing validation semantics.

## Custom Controls

Before building a custom select, combobox, date picker, slider, or file picker:

1. Try the native control first.
2. Define the keyboard model, focus movement, escape behavior, labels, errors, and form submission behavior.
3. Test mobile OS picker behavior and fallback parsing.
4. Keep a text input fallback when exact values matter.
5. Avoid custom controls for visual styling alone.

## Additional Rules

- Do not disable autocomplete globally; use autocomplete tokens intentionally, preserve input-purpose identification, allow password managers, and disable autocomplete only for temporary or sensitive values such as OTPs, unique identifiers, or CVV-like fields; connect to html-accessibility and security/privacy.
- Mobile forms should minimize taps, prefer visible segmented controls for small option sets, avoid dropdown-heavy flows, use appropriate binary/range/numeric controls, keep forms single-column on small screens, show inline errors, mark optional fields instead of repeating required markers, group related fields, provide comfortable touch areas, and respect platform conventions; connect to component-development and ux-patterns.
- Sliders are false simplicity unless implemented carefully; use only for exploratory range/filter interaction, account for non-linear value distributions, make dual handles visually unambiguous, define safe click behavior, always provide text input fallbacks for precise values and degraded motor control, and keep live updates low-latency; connect to component-development, ux-patterns, and network-performance.
- 2022 forms API radar covering requestSubmit() vs submit(), SubmitEvent.submitter, formdata event, showPicker(), and inert; use to preserve native validation/submission flows and form semantics, but pair individual API rules with current MDN/Baseline docs.
