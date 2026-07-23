# CSS Layout and Responsive Primitives

Use CSS layout algorithms deliberately. Grid, Flexbox, Subgrid, container queries, anchor positioning, viewport units, and intrinsic sizing solve different layout problems; choose from the content and layout algorithm rather than from habit.

## Working Rules

- Use Flexbox for one-dimensional, content-driven distribution.
- Use Grid for two-dimensional placement, track control, and page or card composition.
- Use Subgrid when nested children need to align with ancestor tracks without flattening semantic markup.
- Use container queries and container query units for reusable components that must respond to actual container size, not the viewport; design the no-support path as the minimum viable layout so components degrade gracefully when containment is unavailable. Prefer a small-container baseline with `min-width` enhancements when practical, because erasing the query then leaves a stacked but usable component rather than a wide layout forced into a narrow container.
- Use anchor positioning for suitable floating UI: tie placement to an `anchor()` reference, prefer `position-area` for common edge/corner placements, and declare `position-try` fallbacks for collision handling — while keeping trigger semantics separate from positioning. Keep it support-gated and provide a positioning fallback when the floating UI is critical.
- Start from the layout algorithm. `width`, `min-width`, `z-index`, alignment, and intrinsic sizing behave differently in Flow, Flexbox, Grid, Positioned, and Table layout.
- Trace percentage block sizes to a definite ancestor size. A child's
  `height: 100%` cannot resolve when the parent's height is content-sized from
  that same child; break the circular dependency with a genuinely definite size
  only when the product needs one, or use `min-height`, flex/grid stretch, or
  viewport/container sizing that preserves content growth.
- Distinguish `width: auto` from `width: 100%` in normal flow. `auto` consumes
  available space after margins and constraints; `100%` copies the containing
  block's width and can overflow once margins are added. Keep `auto` unless an
  explicit percentage is part of the intended sizing relationship.
- Make the parent context own ordinary layout spacing. Use `gap` when the
  parent is already Flex/Grid or wrapping/alignment behavior needs that
  formatting context. Use a direct-child adjacent-sibling rule (`> * + *`, the
  Owl) for parent-owned vertical rhythm when normal block flow should remain
  intact; scope recursion deliberately. Use nested groups for different regular
  rhythms and an explicit, token-backed spacer only for a one-off discontinuity
  that neither adjacent child should own. Reserve component-authored margin for
  `auto` alignment or documented optical correction; keep prose margins owned
  by the reading context and use `margin-trim` only as a support-gated edge
  refinement.
- Prefer logical properties (`inline-size`, `block-size`, `margin-inline`, `padding-block`, `inset-inline`) over physical ones so layouts adapt to writing mode and RTL without rework.
- Size fluidly with `min()`, `max()`, and `clamp()` for content width, gutters, type, and gaps so layout flexes between sensible bounds without a breakpoint for every step; cap line length (for example `min(100%, 65ch)`) so fluid widths never break readable measure.
- Prefer a page Grid or Subgrid full-bleed pattern when readable text and
  breakout media must coexist and the page wrapper is under your control. When
  a bounded-column utility must escape instead, do not assume `100vw` equals
  the usable page width: classic scrollbars can make viewport units wider than
  the initial containing block. Use a stable page-width query container and
  logical `cqi` breakout math, then audit nested query containers.
- Drive content-aware sections from the content itself — `:has()`, quantity queries (`:nth-child` / `:nth-last-child` of-type counts), container query units, and `clamp()` — with `@supports` fallbacks, so layouts adapt to variable item counts and text lengths instead of relying on brittle breakpoint-only rules.
- Scope `:has()` to the smallest stable component or region that owns the
  derived state. Prefer a specific relative selector over a broad descendant
  search, avoid root-wide and deeply chained conditions, and profile selector
  cost on large or frequently mutating trees. Do not mirror the same DOM state
  into a JavaScript class merely to style it, but keep business and product
  state explicit in the component model instead of inferring it from incidental
  markup.
- Use `min-width: 0`, intrinsic sizing constraints, and explicit `aspect-ratio` defensively in cards, grids, media, and overflow-prone components to prevent blowouts and reserve space against layout shift (CLS).
- Prevent icons, markers, and fixed control affordances from becoming squishy in
  flex layouts with `flex: none` or an intentional `flex-shrink: 0`; do not apply
  it to text-bearing regions that need to yield and wrap.
- Express local layout math through clearly named semantic custom properties; avoid clever cascading custom properties that hide which element owns a value.
- Treat shared compositions as small CSS APIs: give every configurable custom
  property a sensible fallback, keep the primitive useful with no local setup,
  and let components configure the relationship instead of duplicating its
  implementation.
- Distinguish `auto-fit` from `auto-fill` in responsive grids. Collapse empty
  tracks with `auto-fit` when present items should consume the available row;
  preserve the track scaffold with `auto-fill` only when empty tracks are part
  of the intended placement behavior.
- Stop generalizing a layout primitive when one consumer needs compound
  viewport/container conditions, repeated resets, or markup inserted only to
  make a query possible. Find a stable behavioral invariant or move the
  exceptional layout into the owning pattern.
- Prefer Subgrid or semantic markup changes over `display: contents` when the
  only goal is to flatten a wrapper into an ancestor Grid. If flattening is
  still justified, verify the element's semantics in representative
  accessibility trees because some implementations can omit the element itself.
- Bound viewport-relative block spacing and sizing with root-relative minima and
  maxima. Prefer logical viewport units (`vi`/`vb`, or the appropriate dynamic
  viewport unit) when the relationship follows writing-mode axes, and test
  shallow landscape viewports, browser chrome, and zoom.
- Treat new primitives such as `round()`, multi-column wrapping features, `@scope`, and style queries as support-gated enhancements until the target browser baseline is verified.

## Route Responsive Signals by Owner

Choose the query from the condition's owner, not from the visual result it
happens to produce:

| Condition | Owner and mechanism |
| --- | --- |
| Page shell, navigation, or other viewport-owned structure | Viewport or device environment; use a media query. |
| A reusable component's available inline or block space | Nearest intentional query container; use a size container query. |
| Real descendant presence, count, checked state, or another local DOM fact | Owning component or region; use `:has()` or a quantity selector. |
| Theme, density, feature treatment, or presentation intent supplied by an ancestor | Cascade context; use a semantic custom property and, when verified, a style query. |
| Browser capability or user preference | User agent or user setting; use `@supports` or the relevant preference media query. |
| Business state, authorization, fetched data, or application workflow | Component/application model; expose it explicitly rather than asking CSS to infer it. |

Start with intrinsic behavior and add a query only for a meaningful mode change.
Keep every condition local and explainable. If a layout requires the cross
product of media, size, style, and relational queries to select one mode,
restate the zones and ownership, simplify the composition, or move explicit
product state back into the component model. Preserve a coherent baseline when
any enhancement query is erased.

Sources: [Chrome selector-cost guidance](https://developer.chrome.com/docs/performance/insights/slow-css-selector),
[Chrome `:has()` guidance](https://developer.chrome.com/blog/has-m105), and
[MDN `display: contents` accessibility note](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#display_contents).

## Layout Selection Guide

- **Flow:** best for documents, editorial content, natural vertical rhythm, and text-first pages.
- **Flexbox:** best for one axis, unknown item sizes, toolbar/button rows, inline clusters, and content-driven wrapping.
- **Grid:** best for two-dimensional control, dashboards, page sections, card mosaics, full-bleed wrappers, and explicit alignment.
- **Subgrid:** best when nested markup must inherit card/list/form/editorial tracks while keeping semantic structure intact.
- **Container queries:** best for reusable components embedded in sidebars, cards, split panes, and CMS regions where viewport breakpoints are misleading.
- **Anchor positioning:** best for tooltips, callouts, popovers, onboarding highlights, and floating UI that should be tied to a trigger without custom JS geometry; keep it support-gated for critical behavior.
- **Multi-column:** best for continuous editorial content, not interactive card grids; verify fragmentation, reading order, and support before using newer wrapping controls.

## Debug Flex and Grid From Their Defaults

Diagnose the algorithm before adding a breakpoint or hiding overflow:

1. Identify the formatting context and the item's containing block.
2. For Flexbox, start from `flex: 0 1 auto`, no wrapping, cross-axis stretch,
   and the often content-based automatic minimum size. Determine whether the
   container has positive or negative free space and which items are allowed to
   grow, shrink, wrap, or remain fixed.
3. For Grid, inspect explicit and implicit tracks plus each track's minimum.
   Remember that `1fr` keeps an automatic minimum; use `minmax(0, 1fr)` only
   when that track must yield below its content-based minimum and the content
   has an intentional wrapping or overflow policy.
4. Use fixed tracks only when the content contract has a fixed capacity.
   Otherwise prefer intrinsic tracks, bounded `minmax()`, wrapping, or a
   meaningful component mode.
5. Retest with long localized text, unbreakable identifiers, optional media,
   one and many items, and the exact width where free space changes sign.

Do not use `overflow: hidden` as proof that the layout is fixed. It can conceal
the algorithmic failure, clipped focus, and unreachable content.

## Container Query Failure Modes

- Put size containment on a stable outer region and query its descendants. An
  element cannot select itself from its own size query; add or reuse an owning
  wrapper instead of duplicating the viewport breakpoint.
- Check whether the proposed container depended on its contents for inline
  sizing. Inline-size containment removes that contribution and can collapse or
  distort a shrink-to-fit region. Move containment outward or give the owning
  region an intentional size contract.
- Audit the nearest eligible container for every query and container unit,
  especially inside nested components. Do not assume a distant named container
  retargets container units.
- Choose thresholds in a resizable component fixture with representative
  content. Resize until the relationship becomes cramped or changes meaning,
  then name that component mode and verify both sides continuously.
- Erase the query during review. The baseline must retain semantic content,
  source order, core actions, and a usable small-container composition.

## Percentage-Size Diagnostic

1. Identify the element's layout algorithm and containing block.
2. Determine whether the percentage axis resolves against a definite size.
3. Walk ancestors until the definite size is found; `auto`/content-based heights
   do not establish one for a descendant percentage height.
4. Prefer content-safe layout (`min-height`, stretch, intrinsic sizing) before
   imposing a fixed height merely to make a percentage resolve.
5. Test text zoom, translated content, loading states, and overflow after adding
   any definite block size.

## Build Full-Bleed Breakouts Without Hiding Overflow

Prefer explicit Grid tracks when you own the wrapper. This keeps the content
measure and breakout relationship in one layout algorithm and does not depend
on viewport units:

```css
.page {
  --gutter: clamp(1rem, 4vi, 3rem);
  --measure: 70ch;
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [content-start] minmax(0, var(--measure))
    [content-end] minmax(var(--gutter), 1fr)
    [full-end];
}

.page > * { grid-column: content; }
.page > .full-bleed { grid-column: full; }
```

When you cannot make the wrapper a Grid, establish a full-width inline-size
query container and let a descendant utility escape from its bounded column:

```css
body {
  /* Use the project's normal full-width body margin reset. */
  margin: 0;
  container: page / inline-size;
}

.full-bleed {
  inline-size: 100cqi;
  margin-inline: calc(50% - 50cqi);
}
```

This avoids the classic `100vw` mismatch because `cqi` uses the query
container's content-box inline size. Do not make `overflow-x: hidden` or
`overflow-inline: clip` the primary fix: clipping can conceal unrelated layout
bugs, focus indicators, shadows, and positioned content. Reserve
`scrollbar-gutter: stable` for a deliberate root-level scrollbar policy rather
than adding permanent gutter space only to rescue one utility.

Container units always select the nearest eligible ancestor for their axis;
the name in `container: page / inline-size` cannot target `100cqi` at that named
container. A nested inline-size container can therefore retarget the utility.
Prefer one of these responses, in order:

1. Keep the full-bleed element outside local query containers.
2. Use the page Grid pattern instead of a breakout utility.
3. For a verified browser baseline, capture the page size as the computed value
   of a registered inherited custom property at a stable boundary:

```css
@property --page-inline-size {
  syntax: "<length> | <percentage>";
  inherits: true;
  initial-value: 100%;
}

@property --page-half-inline-size {
  syntax: "<length> | <percentage>";
  inherits: true;
  initial-value: 50%;
}

body {
  container: page / inline-size;
}

.page-shell {
  /* Resolves against body here, before nested query containers intervene. */
  --page-inline-size: 100cqi;
  --page-half-inline-size: 50cqi;
}

.full-bleed {
  inline-size: var(--page-inline-size);
  margin-inline-start: calc(50% - var(--page-half-inline-size));
}
```

Registration matters: an unregistered custom property preserves the `100cqi`
token and resolves it where `var()` is used, while a typed registered property
substitutes its computed length. Do not treat this as invisible magic: document
where the page width is captured, verify `@property` support, and prefer the
Grid version when the ownership is hard to explain.

Test full-bleed layouts with always-visible classic scrollbars, RTL and another
supported writing direction, nested query containers, browser zoom, long
content, borders/shadows that reveal one-pixel clipping, and keyboard focus at
both edges.

Sources: [David Bushell's full-bleed analysis](https://dbushell.com/2026/07/03/fixing-full-bleed-css/),
[CSS Values viewport and scrollbar behavior](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths),
[CSS container-relative units](https://www.w3.org/TR/css-contain-3/#container-lengths),
and the [CSS Properties and Values API](https://drafts.css-houdini.org/css-properties-values-api-1/).
