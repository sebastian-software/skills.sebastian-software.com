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

## WCAG 2.2 Priorities

Use WCAG 2.2 AA as the stable minimum target for new work. WCAG is a floor, not a complete product-quality definition.

Pay special attention to the criteria that frequently affect modern application UI:

- **2.4.11 Focus Not Obscured (Minimum):** sticky headers, drawers, floating toolbars, cookie banners, and overlays must not cover focused controls. Use `scroll-padding`, `scroll-margin`, layout offsets, and overlay tests.
- **2.5.7 Dragging Movements:** any drag-only reordering, slider, map, cropper, or canvas interaction needs a single-pointer alternative unless dragging is essential.
- **2.5.8 Target Size (Minimum):** pointer targets must be at least 24 x 24 CSS px, or satisfy the spacing/equivalent/inline/user-agent/essential exceptions. Prefer 44-48 CSS px for frequent touch controls.
- **3.2.6 Consistent Help:** repeated help mechanisms such as chat, contact, docs, or support links should appear in a consistent relative location.
- **3.3.7 Redundant Entry:** avoid asking users to re-enter information already provided in the same process unless there is a real security or confirmation need.
- **3.3.8 Accessible Authentication (Minimum):** do not require cognitive-function tests such as memorization, transcription, or puzzles unless an accessible alternative exists. Support password managers, paste, passkeys, magic links, and recovery flows.

WCAG 2.2 removed 4.1.1 Parsing as a success criterion. Still write valid HTML because invalid structure can break semantics, focus, forms, and browser repair behavior.

## ARIA and Assistive Technology

Use ARIA only when native HTML cannot express the required role, state, or relationship.

- Prefer native controls over ARIA replicas. A native `button`, `select`, `details`, `dialog`, `table`, or form field usually brings keyboard behavior, names, states, and browser integration for free.
- Use ARIA Authoring Practices patterns as implementation references, not as proof that a pattern is accessible in every screen-reader/browser pair.
- Treat `aria-controls`, `aria-describedby`, live regions, comboboxes, grids, treeviews, and application-style menus as test-required. Support varies by assistive technology and browser.
- Do not add ARIA attributes that duplicate or contradict native semantics.
- Do not use `role="button"` on non-buttons unless a native button is impossible; if used, implement keyboard activation, focus, disabled semantics, and accessible name behavior.

## Accessibility Test Loop

For every custom or composite widget:

1. Navigate with keyboard only.
2. Verify visible focus, focus order, focus return, Escape behavior, and no keyboard trap.
3. Test at 200% zoom and a narrow viewport.
4. Test forced-colors/high-contrast mode when the UI has custom borders, icons, or focus styling.
5. Test reduced motion when transitions affect state or spatial orientation.
6. Test with at least one screen reader/browser pair when the component has custom roles, live updates, dialogs, menus, comboboxes, grids, or non-trivial focus management.
7. Confirm automated accessibility checks pass, then manually verify behavior that automation cannot infer.

## Additional Rules

- User prefers explanatory practice articles as when they explain why and how better than specs/MDN.
- Use as broader semantic state/parent-context pattern guidance, not only a11y: parent styling from child/content/focus/error/state conditions; a11y is one use case.
- Live/inline validation timing, copy-paste tolerance, late validation, recovery paths, and avoiding premature error states.
- Custom/native control anatomy, semantic input preservation, focus/state styling, configurable component CSS; not React-specific and not only a11y.
- Correct input type, inputmode, enterkeyhint, autocomplete/name hints, browser cooperation, mobile keyboard UX, and progressive enhancement.
- focus-visible snippet/reminder: useful for visible focus styling, outline offset/width/currentColor caveats, but too small to be a focus guidance.
- Small semantic HTML pattern for explicit tel: links as call-to-action phone numbers, international phone formatting, not relying on auto-detection, and only disabling iOS telephone auto-detection intentionally when custom markup/styling is provided; old/narrow guidance, not .
