---
name: s7n-layout-spacing
description: |
  Layout, spacing, responsive CSS layout, Grid, Flexbox, container queries, subgrid, safe areas, and viewport adaptation. Use when the user asks to fix layout, spacing, responsive behavior, grids, full-bleed sections, dashboards, mobile breakpoints, or CSS layout bugs.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Layout & Spacing

Use this skill for the structural geometry of an interface: where things sit, how they align, how relationships are expressed through space, and how the layout adapts across containers and viewports.

## Workflow

1. Identify the content groups and rank them by relationship, frequency, and importance.
2. Choose layout primitives deliberately: flow for documents, grid for two-dimensional alignment, flex for one-dimensional distribution.
3. Establish a spacing scale and apply it by relationship: closer means more related, farther means separated.
4. Define stable dimensions for fixed-format UI such as boards, toolbars, tiles, counters, and grids.
5. Use container queries for component-level adaptation and media queries for page-level changes.
6. Check small, medium, wide, and extreme-width viewports before shipping.

## Rules

- Avoid layout shifts caused by hover states, labels, loading text, or dynamic content.
- Preserve readable line lengths; do not let wide screens stretch dense content indefinitely.
- Use full-width bands or unframed layouts for page structure. Reserve cards for repeated items, modals, and genuinely framed tools.
- Account for safe-area insets on fixed and sticky UI.
- Keep touch targets large enough and spacing generous enough for coarse pointers.

## References

- [references/layout-spacing.md](references/layout-spacing.md) - spacing systems, grids, white space, and visual grouping.
- [references/responsive-design.md](references/responsive-design.md) - responsive design decisions and breakpoints.
- [references/css-layout-responsive.md](references/css-layout-responsive.md) - CSS layout primitives and responsive implementation.
