# HTML and Accessibility

Use semantic HTML, native behavior, visible focus, keyboard access, and assistive-technology expectations as the foundation for every interface. Prefer browser-provided semantics and controls before custom ARIA patterns.

## Working Rules

- Start with the native element that already has the right role, name, state, keyboard model, and form behavior.
- Treat ARIA as a repair layer for gaps, not as a replacement for semantic HTML.
- Keep focus visible, predictable, and returned to a logical place after dialogs, popovers, disclosures, and route changes.
- Make interactive targets large enough for touch and pointer use, and do not infer input mode from viewport width alone.
- Test keyboard and screen-reader behavior for every custom or composite widget.

## Source-Backed Guidance

### 5 Accessibility Quick Wins You Can Implement Today

- Things ID(s): `GrwsAoykPLsoyNE3xaWExr`
- Source: <https://css-tricks.com/5-accessibility-quick-wins-you-can-implement-today/>
- Decision: `primary`
- Target: `core-html-a11y`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: User prefers explanatory practice articles as primary when they explain why and how better than specs/MDN.

### :has(): the family selector - Chrome Developers

- Things ID(s): `S7QdCNaqFMgg6mtMgPUQEz`
- Source: <https://developer.chrome.com/blog/has-m105/?utm_source=CSS-Weekly&utm_campaign=Issue-516&utm_medium=email>
- Decision: `primary`
- Target: `core-html-a11y`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as broader semantic state/parent-context pattern source, not only a11y: parent styling from child/content/focus/error/state conditions; a11y is one use case.

### A Complete Guide To Live Validation UX - Smashing Magazine

- Things ID(s): `WV1CJTgNqUcfKj5TqVkNY`
- Source: <https://www.smashingmagazine.com/2022/09/inline-validation-web-forms-ux/>
- Decision: `primary`
- Target: `core-html-a11y`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for forms and accessibility: live/inline validation timing, copy-paste tolerance, late validation, recovery paths, and avoiding premature error states.

### A highly configurable switch component using modern CSS techniques

- Things ID(s): `DWLbMdqiECL5aXGfG4Rpfx`, `KievRkcUy5BjHimCZm9jFN`
- Source: <https://piccalil.li/blog/a-highly-configurable-switch-component-using-modern-css/>
- Decision: `primary`
- Target: `core-html-a11y`
- URL recheck: 2026-06-13, HTTP 200
- Duplicate handling: canonical entry for 2 Things items.
- Guidance: Primary for framework-agnostic component-development know-how: custom/native control anatomy, semantic input preservation, focus/state styling, configurable component CSS; not React-specific and not only a11y.

### Adactio: Journal-Three attributes for better web forms

- Things ID(s): `Qbn2aNkkGwuJsrin323izj`
- Source: <https://adactio.com/journal/19842?utm_source=newsletter&utm_medium=email&utm_campaign=wdrl-309>
- Decision: `primary`
- Target: `core-html-a11y`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for forms UX and HTML input rules: correct input type, inputmode, enterkeyhint, autocomplete/name hints, browser cooperation, mobile keyboard UX, and progressive enhancement.

