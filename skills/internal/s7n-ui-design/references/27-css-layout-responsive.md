# CSS Layout and Responsive Primitives

Use CSS layout algorithms deliberately. Grid, Flexbox, Subgrid, container queries, anchor positioning, viewport units, and intrinsic sizing solve different layout problems; choose from the content and layout algorithm rather than from habit.

## Working Rules

- Use Flexbox for one-dimensional, content-driven distribution.
- Use Grid for two-dimensional placement, track control, and page or card composition.
- Use Subgrid when nested children need to align with ancestor tracks without flattening semantic markup.
- Use container queries for reusable components that must respond to actual container size.
- Use anchor positioning for suitable floating UI, while keeping semantics, collision behavior, and fallback behavior separate.

## Source-Backed Guidance

