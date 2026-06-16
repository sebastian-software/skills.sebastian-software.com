# HTML and Accessibility

Use semantic HTML, native behavior, visible focus, keyboard access, and assistive-technology expectations as the foundation for every interface. Prefer browser-provided semantics and controls before custom ARIA patterns.

## Working Rules

- Start with the native element that already has the right role, name, state, keyboard model, and form behavior.
- Treat ARIA as a repair layer for gaps, not as a replacement for semantic HTML.
- Keep focus visible, predictable, and returned to a logical place after dialogs, popovers, disclosures, and route changes.
- Make interactive targets large enough for touch and pointer use, and do not infer input mode from viewport width alone.
- Test keyboard and screen-reader behavior for every custom or composite widget.
- Let HTML carry meaning before adding JavaScript: use landmarks, headings, labels, captions, explicit link purposes, and native form controls as the baseline.
- Preserve browser assistance. Use accurate `type`, `name`, `autocomplete`, `inputmode`, and `enterkeyhint`; avoid disabling autocomplete or paste unless the value is genuinely temporary or sensitive.
- Delay validation until the user has had a fair chance to answer. Prefer `:user-valid` / `:user-invalid`, clear recovery copy, and submit-time validation over premature red error states.
- Keep visible focus as a design token, not an afterthought: standardize outline color, width, offset, dark-mode behavior, and forced-colors behavior across links, buttons, inputs, `summary`, and custom triggers.

## Application Checklist

- Native first: can a `button`, `a`, `label`, `input`, `select`, `details`, `dialog`, `table`, or landmark solve the job without a custom role?
- Name and purpose: does every control have a stable accessible name, and does every link/button text explain the action or destination?
- Focus path: can keyboard users enter, operate, dismiss, and leave the pattern without losing context?
- Form help: do fields expose input purpose to the browser and allow password managers, autofill, paste, and mobile keyboard optimization?
- Feedback: are validation, async save, toast, and route-change updates announced only when announcement helps the user?
- Input mode: are touch, hover, pointer precision, and target sizes based on actual input capabilities rather than viewport assumptions?

## Additional Rules

- Use as broader semantic state/parent-context pattern guidance, not only a11y: parent styling from child/content/focus/error/state conditions; a11y is one use case.
- Live/inline validation timing, copy-paste tolerance, late validation, recovery paths, and avoiding premature error states.
- Custom/native control anatomy, semantic input preservation, focus/state styling, configurable component CSS; not React-specific and not only a11y.
- Correct input type, inputmode, enterkeyhint, autocomplete/name hints, browser cooperation, mobile keyboard UX, and progressive enhancement.
- focus-visible snippet/reminder: useful for visible focus styling, outline offset/width/currentColor caveats, but too small to be a focus guidance.
- Use explicit `tel:` links for call-to-action phone numbers, preserve international phone formatting in visible text, and disable iOS telephone auto-detection only when custom markup/styling provides an equivalent intentional link.
