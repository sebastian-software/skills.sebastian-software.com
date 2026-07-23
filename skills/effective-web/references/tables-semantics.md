# Table Semantics

Use this module when people must compare values across a shared row-and-column
structure. If the primary task is browsing cards, performing one action, or
reading a narrative, choose a different pattern before styling a table.

## Build the Accessible Structure

- Use native `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, and
  `<td>` elements. Do not recreate a data table with generic `div` roles unless
  a native table is genuinely impossible.
- Give every table a visible or visually-hidden `<caption>` that states what is
  being compared and any unit or time period that applies to the whole table.
- Use `scope="col"` and `scope="row"` for ordinary headers. For multi-level or
  irregular headers, connect cells with explicit `id` and `headers` values.
- Keep source order aligned with the comparison task. Do not rely on visual
  positioning to make row or column labels meaningful.

## Make Values Scannable

- Right-align numbers and dates where it improves comparison; use tabular
  numerals for dense numeric columns. Left-align prose and keep headers aligned
  with their data.
- Set density with padding, grouping, and clear headings before reaching for
  zebra stripes or many borders. Never convey status with color alone.
- Keep row actions visible or reveal them through an explicit, keyboard-reachable
  control; hover-only actions strand touch and keyboard users.

## Verify

Check a screen reader's header announcement, keyboard reachability, zoom, long
values, empty and loading states, and whether the chosen presentation remains a
table at the smallest supported width.

For complex headers, CSS implementation recipes, or print details, use the
[deep table appendix](tables-data.md) after the semantic model is settled.
