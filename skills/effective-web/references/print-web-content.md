# Printable Content

Use this module when a printed page needs readable links, images, tables, code,
or article content. Preserve information value while avoiding a paper artifact
that is visually noisier than the screen.

## Links and Provenance

- Prefer descriptive labels. Add a short URL, numbered note, printed source
  list, or QR code only when offline provenance, citation, or a fallback path
  matters to the reader.
- Do not append tracking-heavy raw URLs to every link. Expose destinations
  selectively and wrap long paths safely when they are needed.

## Images, Tables, and Code

- Constrain images to the printable area, prevent fragmentation where practical,
  and hide decorative artwork. Use vector for marks, diagrams, and type when it
  remains appropriate to the output.
- Repeat table headers with `thead { display: table-header-group; }`, avoid
  splitting rows where possible, and test wide comparisons rather than forcing
  a desktop grid onto a narrow page.
- Convert dark syntax themes to light paper output. Let code wrap or provide a
  deliberate print representation; never clip the only copy of important text.

## Typography and Fragmentation

- Keep headings with the following content and avoid splitting figures,
  blockquotes, tables, and code where it improves reading continuity.
- Use `orphans` and `widows` as progressive quality hints, then inspect actual
  pagination. Browser support and print engines vary.

For detailed link, image, and table recipes, consult the [deep web print
appendix](print-web-styles.md).
