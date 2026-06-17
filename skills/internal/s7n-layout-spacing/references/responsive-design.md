# Responsive Design

Design responsive behavior from content, container, input mode, device constraints, and task density. Mobile is not the only responsive case; large screens, print, hybrid pointers, dynamic viewport units, tables, and responsive media need explicit decisions.

## Working Rules

- Use content and task requirements to choose breakpoints and layout changes; test at awkward in-between widths, not only common device presets.
- Name breakpoints by intent (`compact`, `comfortable`, `wide`, `dense`, `comparison`) rather than by device class so rules describe the layout change instead of an assumed screen.
- Prefer container-aware adaptation for reusable components.
- Treat responsive images, tables, navigation, forms, print, safe areas, and large-screen layouts as first-class responsive concerns.
- Detect input capability with `pointer`, `hover`, `any-pointer`, and `any-hover` rather than inferring touch, hover, or precision from viewport width; size hit areas, gate hover-dependent UI, and adapt card/menu/form behavior from the actual input mode, accounting for hybrid devices with multiple input mechanisms.
- Coordinate responsive media decisions with performance rules when bytes, LCP, or source discovery are affected.
- Design up and down. Large screens need better packaging of the same important content, not filler added because space exists.
- Preserve meaning when transforming dense content. Tables, comparison views, and dashboards need semantics, headers, alignment, scan paths, and keyboard access after responsive changes.
- Treat responsive tables as having no universal solution: pick the transform (horizontal scroll, stacked rows, priority columns, comparison view) from the data's scanning and comparison needs. When a table overflows, wrap it in a focusable, labelled scroll container with a visible scroll cue rather than flattening the markup or dropping headers.
- Treat print as a responsive medium: remove navigation chrome, expose URLs where useful, control page breaks, avoid overflow clipping, verify grayscale contrast, restrain ink-heavy backgrounds, use `print-color-adjust` sparingly, and test print preview.
- Use `svh`, `lvh`, and `dvh` deliberately for full-height surfaces, drawers, dialogs, and sticky layouts; account for browser UI, soft keyboards, scrollbars, and update-rate behavior.
- Apply `scrollbar-gutter: stable` when an appearing scrollbar would otherwise shift a centered or fixed-width layout.
- Use responsive images with explicit dimensions/aspect ratios and performance-aware `srcset`/`sizes`; do not let visual layout decisions create avoidable LCP or CLS problems.

## Responsive Decision Checklist

- What is the user trying to compare, scan, enter, read, or act on at each size?
- Is the component responding to viewport size, container size, content count, text length, input mode, or media type?
- Does the large-screen version improve overview, density, sticky controls, or side-by-side comparison without hiding primary content?
- Does the small-screen version preserve table/list semantics or provide an equivalent comparison path?
- Are hover-revealed controls still visible or reachable on touch, keyboard, and hybrid devices?
- Are fixed/sticky elements safe-area aware and tested with browser UI, zoom, and virtual keyboards?
