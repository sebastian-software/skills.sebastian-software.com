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

- Buttons do actions; links navigate.
- `:focus-visible` must be obvious and must not rely on color alone.
- Hidden content must be hidden consistently from visual, keyboard, and accessibility trees.
- Error messages must be programmatically associated with the field or region they describe.
- Accessibility is a design and implementation constraint, not a final audit layer.

## References

- [references/23-html-accessibility.md](references/23-html-accessibility.md) - semantic HTML, ARIA, keyboard, and accessibility implementation.
