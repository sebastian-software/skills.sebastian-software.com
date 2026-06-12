# HTML and Accessibility

Use semantic HTML, native behavior, visible focus, keyboard access, and assistive-technology expectations as the foundation for every interface. Prefer browser-provided semantics and controls before custom ARIA patterns.

## Working Rules

- Start with the native element that already has the right role, name, state, keyboard model, and form behavior.
- Treat ARIA as a repair layer for gaps, not as a replacement for semantic HTML.
- Keep focus visible, predictable, and returned to a logical place after dialogs, popovers, disclosures, and route changes.
- Make interactive targets large enough for touch and pointer use, and do not infer input mode from viewport width alone.
- Test keyboard and screen-reader behavior for every custom or composite widget.

## Source-Backed Guidance

