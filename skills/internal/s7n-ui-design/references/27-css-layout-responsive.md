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

### Subgrid

- Things ID(s): `GeEhJHNGGvhjeJuMrZajg8`
- Source: <https://www.joshwcomeau.com/css/subgrid/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: current detailed subgrid guide covering semantic nested markup, extending parent grids through lists/figures, row/column inheritance, gotchas, fallback thinking, and when subgrid enables layouts that would otherwise require flattened DOM or brittle hacks.

### The Basics of Anchor Positioning

- Things ID(s): `ghrCNzohgAzsd9zeZo3cf`
- Source: <https://ishadeed.com/article/anchor-positioning/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with component-development/baseline cross-references: strong Anchor Positioning basics source for positioning elements relative to non-parent anchors, anchor(), position-area, span areas, and position-try fallbacks; pair support blocks with current Baseline data.

### Understanding Layout Algorithms

- Things ID(s): `6mSaX9UbSoaLKzpVpCNPHs`
- Source: <https://www.joshwcomeau.com/css/understanding-layout-algorithms/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive: foundational mental-model source that CSS properties only make sense within layout algorithms such as Flow, Flexbox, Grid, Positioned, and Table; use to teach why width, z-index, sizing, and alignment behave differently by layout mode.

### www.joshwcomeau.com/css/full-bleed/

- Things ID(s): `MgYtYmXmAoBUknE4HT95Z8`
- Source: <https://www.joshwcomeau.com/css/full-bleed/>
- Decision: `primary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for css-layout-responsive with editorial-ux cross-reference: strong updated full-bleed layout source for constraining readable text columns while allowing media/widgets to break out via CSS Grid, clear wrapper rules, padding tradeoffs, and line-length reasoning.

### 6 CSS snippets every front-end developer should know in 2023

- Things ID(s): `KgRaFQXYaM27sqK6Amk67w`
- Source: <https://web.dev/6-css-snippets-every-front-end-developer-should-know-in-2023/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23139%3A+React.dev%2C+Remix%2C+next+export%2C+Server+Components%2C+i18n%2C+Error+Boundary%2C+Wakuwork%2C+Astro%2C+React-Native%2C+Bottom+Sheet%2C+TypeScript%2C+TC39...+%20-%2010351123>
- Decision: `secondary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://web.dev/articles/6-css-snippets-every-front-end-developer-should-know-in-2023?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23139%3A+React.dev%2C+Remix%2C+next+export%2C+Server+Components%2C+i18n%2C+Error+Boundary%2C+Wakuwork%2C+Astro%2C+React-Native%2C+Bottom+Sheet%2C+TypeScript%2C+TC39...++-+10351123
- Guidance: Secondary for css-layout-responsive with baseline/design-system/component-development cross-references: official web.dev roundup of useful modern CSS primitives including container queries, scroll snap, grid pile, aspect-ratio, cascade layers, and logical properties; useful support/radar and checklist source, but detailed rules should come from focused sources.

### Auto filling Grid. Good solution for Dashboards

- Things ID(s): `NJQxicZE8mBsnyMGzqgqXb`
- Source: <https://css-tricks.com/an-auto-filling-css-grid-with-max-columns/?>
- Decision: `secondary`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for css-layout-responsive: practical auto-filling CSS Grid pattern for card/dashboard layouts with max column counts; useful recipe, but narrower than core Grid mental-model sources.

