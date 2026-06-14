# Responsive Design

Design responsive behavior from content, container, input mode, device constraints, and task density. Mobile is not the only responsive case; large screens, print, hybrid pointers, dynamic viewport units, tables, and responsive media need explicit decisions.

## Working Rules

- Use content and task requirements to choose breakpoints and layout changes.
- Prefer container-aware adaptation for reusable components.
- Treat responsive images, tables, navigation, forms, print, safe areas, and large-screen layouts as first-class responsive concerns.
- Avoid relying on viewport width to infer touch, hover, or pointer precision.
- Coordinate responsive media decisions with performance rules when bytes, LCP, or source discovery are affected.
- Design up and down. Large screens need better packaging of the same important content, not filler added because space exists.
- Preserve meaning when transforming dense content. Tables, comparison views, and dashboards need semantics, headers, alignment, scan paths, and keyboard access after responsive changes.
- Treat print as a responsive medium: remove navigation chrome, expose URLs where useful, control page breaks, avoid overflow clipping, and test print preview.
- Use `svh`, `lvh`, and `dvh` deliberately for full-height surfaces, drawers, dialogs, and sticky layouts; account for browser UI, soft keyboards, scrollbars, and update-rate behavior.
- Use responsive images with explicit dimensions/aspect ratios and performance-aware `srcset`/`sizes`; do not let visual layout decisions create avoidable LCP or CLS problems.

## Responsive Decision Checklist

- What is the user trying to compare, scan, enter, read, or act on at each size?
- Is the component responding to viewport size, container size, content count, text length, input mode, or media type?
- Does the large-screen version improve overview, density, sticky controls, or side-by-side comparison without hiding primary content?
- Does the small-screen version preserve table/list semantics or provide an equivalent comparison path?
- Are hover-revealed controls still visible or reachable on touch, keyboard, and hybrid devices?
- Are fixed/sticky elements safe-area aware and tested with browser UI, zoom, and virtual keyboards?

## Breakpoint Strategy

Breakpoints should come from content and task needs, not device names.

- Use container queries for reusable components whose layout depends on their available inline size.
- Use media queries for page-level layout, global navigation, viewport constraints, print, and input capability checks.
- Keep component breakpoints close to the component when they describe component behavior.
- Avoid "mobile/tablet/desktop" assumptions in rule names. Prefer intent names such as `compact`, `comfortable`, `wide`, `dense`, or `comparison`.
- Test at awkward widths, not only common device presets.

## Input Capability

Viewport width is not an input-mode proxy.

- Use `(hover: hover)` and `(pointer: fine)` before adding hover-only refinements.
- Use `(any-hover: hover)` and `(any-pointer: coarse)` when hybrid devices matter.
- Never hide required controls behind hover. Hover can reveal convenience actions only when a keyboard/touch path remains visible or discoverable.
- Increase target size and spacing for coarse pointers, but do not remove keyboard support from pointer-focused layouts.

## Viewport Units and Safe Areas

Use viewport units deliberately:

- `svh` for stable minimum-height surfaces that should not jump when browser UI appears.
- `dvh` for panels that should track the visible viewport, such as drawers or command surfaces, after testing resize behavior.
- `lvh` only when the largest possible viewport is explicitly desired and clipped content is acceptable.
- `env(safe-area-inset-*)` for fixed/sticky controls near device edges.
- `scrollbar-gutter: stable` when scrollbar appearance would shift a centered or fixed-width layout.

Test full-height layouts with mobile browser chrome, virtual keyboards, zoom, landscape orientation, and long translated labels.

## Responsive Content Preservation

Do not solve small screens by deleting meaning.

- Tables need headers, captions, comparison paths, keyboard-accessible overflow, and scroll cues after transformation.
- Dashboards need prioritized scan paths, not random card stacking.
- Navigation needs a reachable semantic baseline before disclosure or burger behavior.
- Forms need grouped labels, hints, errors, and submit controls that remain visible and associated.
- Images and media need explicit dimensions/aspect ratios, `sizes`, and LCP-aware source discovery.

## Additional Rules

- Responsive tables have no universal solution; choose layout pattern from data comparison/scanning needs, preserve table semantics, headers, alignment, spacing, visual scanning, and accessibility when transforming tables for small screens.
- Responsive work should include large screens, not only mobile; adapt the same important content into better large-screen packaging, avoid adding low-value content just because space exists, and balance larger imagery, columns, sticky controls, and overview.
- Do not infer touch/hover/input precision from viewport size; use pointer, hover, any-pointer, and any-hover to adapt hit areas, visible controls, hover-dependent UI, and card/menu/form component behavior; account for hybrid devices and multiple input mechanisms; connect to ux-patterns and html-accessibility.
- Responsive design includes print and other media; define print styles, test print preview, handle page size/breaks, visible links, forms, overflow, navigation removal, grayscale contrast, ink use, and print-color-adjust restraint.
- Modern table styling starts with semantic table markup, captions/headers, readable alignment, and accessible overflow wrappers with focus styles and scroll cues rather than destroying table semantics.
- Use svh/lvh/dvh and logical viewport units intentionally for mobile browser UI, full-height sections, dialogs, and stable vs dynamic viewport behavior; note scrollbar, keyboard, and update-rate caveats.
- Srcset/resolution-switching concept guidance, but pair with newer image sources such as web.dev Learn Images and LCP image guidance for current browser behavior and delivery rules.
- Utopia guidance for fluid layout grids, min/max design states, spacing/type token handoff, line length, and device-agnostic design-tool setup; keep as design process support rather than normative implementation guidance.
- Responsive design guidance should shape layout adaptation, not React architecture.
