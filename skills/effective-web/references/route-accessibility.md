# Accessibility and HTML

Use this route for semantic structure, accessible interaction, naming,
visibility, announcements, and accessibility evidence. Prefer native HTML and
robust focus behavior before adding custom abstractions.

## Workflow

1. Identify the user outcome and distinguish conformance evidence from usability
   evidence.
2. Check semantic structure: landmarks, headings, lists, buttons, links, forms,
   and tables.
3. Verify keyboard order, focus visibility, escape routes, focus return, and
   consistency between visible, focus, interaction, and accessibility-tree state.
4. Ensure every interactive control has the intended role, name, description,
   value, state, and relationships.
5. Test contrast, reduced motion, forced colors, zoom, text resizing, and
   representative assistive technology where relevant.
6. Use ARIA only to supplement missing semantics, never to disguise the wrong
   element.

## Rules

- Buttons do actions; links navigate. Use the native element instead of recreating its role, keyboard model, and states on a `div`.
- `:focus-visible` must be obvious, must not rely on color alone, and must move into and out of dialogs, popovers, and new SPA views.
- Choose hiding behavior deliberately across visual rendering, layout,
  accessibility-tree exposure, focus, interaction, and find-in-page; never hide
  a focusable element with `aria-hidden`.
- Prefer native or visible naming, then `aria-labelledby`, with `aria-label` as a
  constrained fallback; keep visible label text within the accessible name.
- Associate field errors programmatically, preserve entered values, keep submit
  available for validation, and provide a focusable error-summary recovery path
  when several fields fail.
- Prefer semantic state and focus over live regions. Announce only important
  asynchronous changes that users would otherwise miss, using short, stable,
  non-interactive regions.
- Accessibility is a design and implementation constraint, not a final audit layer.
- WCAG conformance is a baseline, not proof of usability; combine automation
  with task-based keyboard, accessibility-tree, resilience, and representative
  assistive-technology testing.

## References

- [html-accessibility.md](html-accessibility.md) - semantic structure, ARIA repair layer, forms, focus management, composite widgets, resilient styling, and a review checklist.
- [accessible-names.md](accessible-names.md) - name computation, visible labels, descriptions, icon controls, image alternatives, localization, and verification.
- [visibility-and-notifications.md](visibility-and-notifications.md) - hiding and disabled-state decisions, inert/modal surfaces, find-in-page, and live-region boundaries.
- [accessibility-testing.md](accessibility-testing.md) - conformance versus usability, layered evidence, task scripts, accessibility-tree inspection, representative pairings, and triage.
