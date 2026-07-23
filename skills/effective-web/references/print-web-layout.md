# Printable Web Layout

Use this module when a responsive screen layout needs a paper-specific reading
order. Treat print as a separate medium with a stable page, not as a narrow
desktop viewport.

## Linearize Intentionally

- Reduce multi-column, dashboard, and side-by-side layouts to the reading order
  that makes sense on paper. Keep a side panel only when it supplies required
  context or is itself the artifact.
- Remove fixed heights, fragile viewport sizing, sticky offsets, and overflow
  clipping that can hide content in a paged medium.
- Make content use the printable width without forcing every table or image to
  scale beyond readable proportions. Break a complex artifact into a different
  printable view when a single CSS treatment cannot preserve meaning.

## Fragmentation Rules

- Use `break-before`, `break-after`, and `break-inside` for intentional
  pagination; retain legacy aliases only when the project's support policy needs
  them.
- Keep headings with their following material, but do not apply `avoid` so
  broadly that blank pages become likely. Inspect actual output.
- Use named pages, orientation, and margin boxes only when a known target engine
  supports the feature and the artifact warrants the complexity.

For page-rule examples, browser limitations, and the full print-layout
catalog, consult the [deep web print appendix](print-web-styles.md).
