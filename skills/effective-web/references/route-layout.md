# Layout and Spacing

Use this skill for the structural geometry of an interface: where things sit, how they align, how relationships are expressed through space, and how the layout adapts across containers and viewports.

## Workflow

1. Identify the content groups and rank them by relationship, frequency, and importance.
2. State each region's layout behavior before naming a component: flow,
   wrapping group, bounded column, narrow-plus-flexible pair, equal peers,
   repeated cells, overflow sequence, or deliberate overlay.
3. Choose and compose the smallest intrinsic primitives that express those
   behaviors. Prefer content- and container-driven reconfiguration before
   queries.
4. Establish a spacing scale and apply it by relationship: closer means more related, farther means separated.
5. Define stable dimensions only for genuinely fixed-format UI such as boards, toolbars, tiles, counters, and grids.
6. Add a container query for an explicit component mode only after intrinsic
   sizing cannot express it; reserve media queries for viewport-owned changes.
7. Check continuous container widths, child-count extremes, zoom, long content,
   keyboard reachability, and supported writing directions before shipping.

## Rules

- Avoid layout shifts caused by hover states, labels, loading text, or dynamic content.
- Preserve readable line lengths; do not let wide screens stretch dense content indefinitely.
- Use full-width bands or unframed layouts for page structure. Reserve cards for repeated items, modals, and genuinely framed tools.
- Account for safe-area insets on fixed and sticky UI.
- Keep touch targets large enough and spacing generous enough for coarse pointers.

## References

- [intrinsic-layouts.md](intrinsic-layouts.md) - algorithmic layout mental model,
  primitive selection, composition contracts, implementation, and verification.
- [layout-spacing.md](layout-spacing.md) - spacing systems, grids, white space, and visual grouping.
- [responsive-design.md](responsive-design.md) - responsive design decisions and breakpoints.
- [css-layout-responsive.md](css-layout-responsive.md) - CSS layout primitives and responsive implementation.
