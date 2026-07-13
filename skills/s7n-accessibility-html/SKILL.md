---
name: s7n-accessibility-html
description: |
  Semantic HTML, WCAG-oriented frontend accessibility, keyboard interaction, focus management, landmarks, headings, ARIA, accessible names, forced colors, and inclusive interaction. Use when reviewing HTML structure, fixing accessibility bugs, adding ARIA, or making UI keyboard/screen-reader accessible.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Accessibility & HTML

Use this skill for semantic structure and accessible interaction. Prefer native HTML and robust focus behavior before adding custom abstractions.

## Workflow

1. Check semantic structure: landmarks, headings, lists, buttons, links, forms, tables.
2. Verify keyboard order, focus visibility, escape routes, and focus return.
3. Ensure every interactive control has a role, name, value, and state.
4. Test contrast, reduced motion, forced colors, zoom, and text resizing where relevant.
5. Use ARIA only to supplement missing semantics, never to disguise the wrong element.

## Rules

- Buttons do actions; links navigate. Use the native element instead of recreating its role, keyboard model, and states on a `div`.
- `:focus-visible` must be obvious, must not rely on color alone, and must move into and out of dialogs, popovers, and new SPA views.
- Hidden content must be hidden consistently from visual, keyboard, and accessibility trees; never hide a focusable element with `aria-hidden`.
- Every control needs an accessible name; error messages must be programmatically associated with the field via `aria-describedby` + `aria-invalid`.
- Announce only user-unprompted changes through an appropriate live region; preserve `autocomplete`/`type`/`inputmode` and validate late.
- Accessibility is a design and implementation constraint, not a final audit layer.

## References

- [references/html-accessibility.md](references/html-accessibility.md) - semantic structure, ARIA repair layer, accessible names, forms/labels, focus management, live regions, composite widgets, state-driven styling, contrast/target size/reduced-motion/forced-colors, and a review checklist.
