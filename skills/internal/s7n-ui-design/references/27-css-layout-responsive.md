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

### Building a breakout element with container units - Piccalilli

- Things ID(s): `LTn1R5dr77ATW9cwGHeHSR`
- Source: <https://piccalil.li//blog/building-a-breakout-element-with-container-units/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with responsive-design cross-reference: container units and container queries can solve breakout/content-width layouts relative to parent containers rather than viewport, preserve flexible sidebar/content layouts, and degrade as minimum viable experience when unsupported.

### CSS Anchor Positioning Guide

- Things ID(s): `BFDCMcS6STYvcRNbXtE1AN`
- Source: <https://css-tricks.com/css-anchor-positioning-guide/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with component-development and baseline cross-references: general CSS Anchor Positioning guide for placing floating UI relative to anchors, reducing custom JS positioning, and defining fallback/collision strategy; pair with component-specific tooltip/popover semantics.

### CSS Container Queries

- Things ID(s): `X4W31kjNukNLBo1dAWmCgc`
- Source: <https://css-tricks.com/css-container-queries/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with component-development/responsive-design cross-references: container queries let components and layout regions adapt to their actual container rather than global viewport; use for reusable components, nested layout, and content-aware responsive behavior with progressive support checks.

### Learn CSS Subgrid - Ahmad Shadeed

- Things ID(s): `EQmx9Zw92dUPULMadKjBTR`
- Source: <https://ishadeed.com/article/learn-css-subgrid/?utm_source=newsletter&utm_medium=email&utm_campaign=WDRL+300>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: subgrid solves nested alignment when child components need to inherit parent tracks for titles, descriptions, media, cards, forms, and editorial/list layouts; pair old support notes with current Baseline checks.

### Learn CSS Subgrid - Ahmad Shadeed

- Things ID(s): `Sz9LXzmqASdQXgfQ2K8na`
- Source: <https://ishadeed.com/article/learn-css-subgrid/?utm_source=CSS-Weekly&utm_campaign=Issue-504&utm_medium=email>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: duplicate/tracking variant of the Ahmad Shadeed subgrid source; decide together with EQmx9Zw92dUPULMadKjBTR and pair old support notes with current Baseline checks.

### Solved By Modern CSS: Section Layout

- Things ID(s): `JD5mWxmHNyBPhviZWeLCBG`
- Source: <https://ishadeed.com/article/modern-css-section-layout/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with component-development cross-reference: modern section/card layout source combining Grid, :has(), quantity queries, clamp(), container query units, size/style queries, min-width fixes, and defensive handling of variable content counts.

