# CSS Layout and Responsive Primitives

Use CSS layout algorithms deliberately. Grid, Flexbox, Subgrid, container queries, anchor positioning, viewport units, and intrinsic sizing solve different layout problems; choose from the content and layout algorithm rather than from habit.

## Working Rules

- Use Flexbox for one-dimensional, content-driven distribution.
- Use Grid for two-dimensional placement, track control, and page or card composition.
- Use Subgrid when nested children need to align with ancestor tracks without flattening semantic markup.
- Use container queries and container query units for reusable components that must respond to actual container size, not the viewport; design the no-support path as the minimum viable layout so components degrade gracefully when containment is unavailable.
- Use anchor positioning for suitable floating UI: tie placement to an `anchor()` reference, prefer `position-area` for common edge/corner placements, and declare `position-try` fallbacks for collision handling — while keeping trigger semantics separate from positioning.
- Start from the layout algorithm. `width`, `min-width`, `z-index`, alignment, and intrinsic sizing behave differently in Flow, Flexbox, Grid, Positioned, and Table layout.
- Use `gap` for component and layout rhythm when the parent owns spacing; use margin intentionally for document/content flow and optically special cases. Reach for `margin-trim` (support-gated) to drop unwanted first/last-child edge margins instead of override hacks, keeping it subordinate to parent-owned `gap` spacing.
- Prefer logical properties (`inline-size`, `block-size`, `margin-inline`, `padding-block`, `inset-inline`) over physical ones so layouts adapt to writing mode and RTL without rework.
- Size fluidly with `min()`, `max()`, and `clamp()` for content width, gutters, type, and gaps so layout flexes between sensible bounds without a breakpoint for every step; cap line length (for example `min(100%, 65ch)`) so fluid widths never break readable measure.
- Use full-bleed/grid wrapper patterns when readable text and breakout media must coexist without wrapper sprawl.
- Drive content-aware sections from the content itself — `:has()`, quantity queries (`:nth-child` / `:nth-last-child` of-type counts), container query units, and `clamp()` — with `@supports` fallbacks, so layouts adapt to variable item counts and text lengths instead of relying on brittle breakpoint-only rules.
- Use `min-width: 0`, intrinsic sizing constraints, and explicit `aspect-ratio` defensively in cards, grids, media, and overflow-prone components to prevent blowouts and reserve space against layout shift (CLS).
- Express local layout math through clearly named semantic custom properties; avoid clever cascading custom properties that hide which element owns a value.
- Treat new primitives such as `round()`, multi-column wrapping features, `@scope`, and style queries as support-gated enhancements until the target browser baseline is verified.

## Layout Selection Guide

- **Flow:** best for documents, editorial content, natural vertical rhythm, and text-first pages.
- **Flexbox:** best for one axis, unknown item sizes, toolbar/button rows, inline clusters, and content-driven wrapping.
- **Grid:** best for two-dimensional control, dashboards, page sections, card mosaics, full-bleed wrappers, and explicit alignment.
- **Subgrid:** best when nested markup must inherit card/list/form/editorial tracks while keeping semantic structure intact.
- **Container queries:** best for reusable components embedded in sidebars, cards, split panes, and CMS regions where viewport breakpoints are misleading.
- **Anchor positioning:** best for tooltips, callouts, popovers, onboarding highlights, and floating UI that should be tied to a trigger without custom JS geometry.
- **Multi-column:** best for continuous editorial content, not interactive card grids; verify fragmentation, reading order, and support before using newer wrapping controls.
