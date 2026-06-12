# CSS Layout and Responsive Primitives

Use CSS layout algorithms deliberately. Grid, Flexbox, Subgrid, container queries, anchor positioning, viewport units, and intrinsic sizing solve different layout problems; choose from the content and layout algorithm rather than from habit.

## Working Rules

- Use Flexbox for one-dimensional, content-driven distribution.
- Use Grid for two-dimensional placement, track control, and page or card composition.
- Use Subgrid when nested children need to align with ancestor tracks without flattening semantic markup.
- Use container queries for reusable components that must respond to actual container size.
- Use anchor positioning for suitable floating UI, while keeping semantics, collision behavior, and fallback behavior separate.

## Source-Backed Guidance

### An Interactive Guide to CSS Grid

- Things ID(s): `DW2EfCKvCaz6HFc4ACAsa8`
- Source: <https://www.joshwcomeau.com/css/interactive-guide-to-grid/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: high-quality interactive CSS Grid mental-model source for tracks, placement, alignment, intrinsic sizing, responsive composition, and choosing Grid when layout requires two-dimensional control; pair with specific pattern sources for production recipes.

### An Interactive Guide to Flexbox in CSS

- Things ID(s): `a4H5PfTLUEE7rFztJmTjB`
- Source: <https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: high-quality interactive Flexbox mental-model source for one-dimensional layout, intrinsic sizing, wrapping, alignment, distribution, and choosing Flexbox when content-driven rows/columns are more appropriate than Grid.

