# CSS Layout and Responsive Primitives

Use CSS layout algorithms deliberately. Grid, Flexbox, Subgrid, container queries, anchor positioning, viewport units, and intrinsic sizing solve different layout problems; choose from the content and layout algorithm rather than from habit.

## Working Rules

- Use Flexbox for one-dimensional, content-driven distribution.
- Use Grid for two-dimensional placement, track control, and page or card composition.
- Use Subgrid when nested children need to align with ancestor tracks without flattening semantic markup.
- Use container queries for reusable components that must respond to actual container size.
- Use anchor positioning for suitable floating UI when project support allows it, while keeping semantics, collision behavior, and fallback behavior separate.
- Start from the layout algorithm. `width`, `min-width`, `z-index`, alignment, and intrinsic sizing behave differently in Flow, Flexbox, Grid, Positioned, and Table layout.
- Use `gap` for component and layout rhythm when the parent owns spacing; use margin intentionally for document/content flow and optically special cases.
- Use full-bleed/grid wrapper patterns when readable text and breakout media must coexist without wrapper sprawl.
- Use quantity queries, `:has()`, container query units, and `@supports` fallbacks for content-aware sections instead of brittle breakpoint-only layouts.
- Use `min-width: 0`, intrinsic sizing constraints, and explicit aspect ratios defensively in cards, grids, media, and overflow-prone components.
- Treat new primitives such as `round()`, multi-column wrapping features, `@scope`, and style queries as support-gated enhancements until the target browser baseline is verified.

## Layout Selection Guide

- **Flow:** best for documents, editorial content, natural vertical rhythm, and text-first pages.
- **Flexbox:** best for one axis, unknown item sizes, toolbar/button rows, inline clusters, and content-driven wrapping.
- **Grid:** best for two-dimensional control, dashboards, page sections, card mosaics, full-bleed wrappers, and explicit alignment.
- **Subgrid:** best when nested markup must inherit card/list/form/editorial tracks while keeping semantic structure intact.
- **Container queries:** best for reusable components embedded in sidebars, cards, split panes, and CMS regions where viewport breakpoints are misleading.
- **Anchor positioning:** best for tooltips, callouts, popovers, onboarding highlights, and floating UI that should be tied to a trigger without custom JS geometry; keep it support-gated for critical behavior.
- **Multi-column:** best for continuous editorial content, not interactive card grids; verify fragmentation, reading order, and support before using newer wrapping controls.

## Additional Rules

- High-quality interactive CSS Grid mental-model guidance for tracks, placement, alignment, intrinsic sizing, responsive composition, and choosing Grid when layout requires two-dimensional control; pair with specific pattern sources for production recipes.
- High-quality interactive Flexbox mental-model guidance for one-dimensional layout, intrinsic sizing, wrapping, alignment, distribution, and choosing Flexbox when content-driven rows/columns are more appropriate than Grid.
- Container units and container queries can solve breakout/content-width layouts relative to parent containers rather than viewport, preserve flexible sidebar/content layouts, and degrade as minimum viable experience when unsupported.
- General CSS Anchor Positioning guide for placing floating UI relative to anchors, reducing custom JS positioning, and defining fallback/collision strategy; pair with component-specific tooltip/popover semantics.
- Container queries let components and layout regions adapt to their actual container rather than global viewport; use for reusable components, nested layout, and content-aware responsive behavior with progressive support checks.
- Subgrid solves nested alignment when child components need to inherit parent tracks for titles, descriptions, media, cards, forms, and editorial/list layouts; pair old support notes with current Baseline checks.
- Duplicate/tracking variant of the Ahmad Shadeed subgrid guidance; decide together with EQmx9Zw92dUPULMadKjBTR and pair old support notes with current Baseline checks.
- Modern section/card layout guidance combining Grid, :has(), quantity queries, clamp(), container query units, size/style queries, min-width fixes, and defensive handling of variable content counts.
- Detailed subgrid guide covering semantic nested markup, extending parent grids through lists/figures, row/column inheritance, gotchas, fallback thinking, and when subgrid enables layouts that would otherwise require flattened DOM or brittle hacks.
- Strong Anchor Positioning basics guidance for positioning elements relative to non-parent anchors, anchor(), position-area, span areas, and position-try fallbacks; pair support blocks with current Baseline data.
- Foundational mental-model guidance that CSS properties only make sense within layout algorithms such as Flow, Flexbox, Grid, Positioned, and Table; use to teach why width, z-index, sizing, and alignment behave differently by layout mode.
- Strong updated full-bleed layout guidance for constraining readable text columns while allowing media/widgets to break out via CSS Grid, clear wrapper rules, padding tradeoffs, and line-length reasoning.
- Roundup of useful modern CSS primitives including container queries, scroll snap, grid pile, aspect-ratio, cascade layers, and logical properties; useful support/radar and checklist guidance, but detailed rules should come from focused sources.
- Auto-filling CSS Grid pattern for card/dashboard layouts with max column counts; useful recipe, but narrower than core Grid mental-model sources.
- CSS round() fluid sizing/grid math guidance, but feature support and exact syntax should be checked before codifying production rules.
- Strong modern CSS layout example useful for examples and implementation inspiration, but case-study-specific rather than a direct rule.
- 2026 multi-column feature radar for column-wrap/column-height and continuous-content fragmentation, but support is still narrow and concrete production rules should wait for Baseline/current compatibility checks.
- Clamp() wrapper utility for fluid content width, gutters, line length, and progressive fallback; narrow quick-tip guidance rather than broad responsive-layout guidance.
- Strong modern CSS layout example using Grid, gap, aspect-ratio, text wrapping, :has(), fluid sizing, and container queries, but case-study-specific rather than a direct reusable rule.
- Duplicate/tracking variant of the Vox modern CSS layout example; decide together with 3XJAUQjYcWgpUKURQC6caV.
- Clever sticky-header text-obscuring/layering trick and scroll-driven-animation note, but it depends on specific hero/header design constraints and should remain an example/caveat, not a baseline pattern.
- Concise practical subgrid example for aligning headings/summaries across responsive cards and understanding gap inheritance; useful companion to broader subgrid sources.
- Use as `margin-trim` feature radar and spacing-model context: it can simplify first/last-child edge trimming in stacks and sections, but keep it support-gated and subordinate to the broader parent-owned spacing rule.
- Use as platform-radar context for current CSS/web platform progress, not as narrow implementation guidance. When it changes a rule, verify against Baseline/current browser docs first.
- Use as practical CSS property radar. Treat individual properties as prompts for support checks and focused docs before adding production rules.
- Use as implementation context for progressively enhancing native `details`/`summary` interactions with CSS. Preserve native disclosure semantics, focus behavior, reduced-motion handling, and support fallbacks.
- Use as examples of deriving directional/hover effects from CSS state and geometry. Keep effects decorative, pointer-gated, keyboard-safe, and nonessential to understanding or operating the component.
- Use as practical image-default context: image display, sizing, aspect-ratio, and overflow defaults should support stable layout and responsive media without fighting semantic `img` behavior.
- Use as advanced custom-property context for theming, local layout math, state-derived values, and API design. Prefer clear semantic custom properties over clever cascading that hides ownership.
- Use as decorative section-shape implementation context only. Do not promote slanted containers as a default pattern; require content readability, hit-target stability, and responsive overflow checks.
- Use as explanatory support for CSS mental models and layout-algorithm thinking. The rule remains: identify the layout algorithm before interpreting sizing, positioning, stacking, or alignment behavior.
