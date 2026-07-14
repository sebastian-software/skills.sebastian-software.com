# Print Locale Integration

Use this reference to integrate reviewed locale typography into print CSS and
web-to-print pipelines. `locale-typography` owns language-level choices for
quotation marks, punctuation spacing, dashes, numbers, and non-breaking
spaces; do not duplicate or infer those rules here.

## Choose the Locale Before Styling

Set the document language on the printed HTML and route visible prose to
`locale-typography` for the matching profile. Preserve an established,
reviewed house style when it intentionally differs from a locale default.

```html
<html lang="de-DE">
```

For dynamic numbers, currencies, dates, units, and lists, use locale-aware
formatting APIs before print layout rather than assembling localized strings in
CSS or a template.

## CSS Quotation Integration

Use the CSS `quotes` property only after selecting the quotation system from
the matching `locale-typography` profile. Keep the locale values in the source
of truth instead of copying per-locale tables into print styles.

```css
/* Values must come from the reviewed locale profile for the document's lang. */
html[lang="de"] {
  quotes: "„" "“" "‚" "‘";
}

q::before { content: open-quote; }
q::after  { content: close-quote; }
```

Use `quotes: auto` only when the target rendering environment and the document
language produce the reviewed result. Test nested quotations in the generated
print output; do not add visual thin spaces merely to prevent marks from
appearing close together.

## Preprocessing Safely

Never run blind SmartyPants-style substitutions over Markdown, HTML, JSX,
templates, structured data, or quoted source material. They can alter code,
attribute values, and locale-specific punctuation incorrectly.

When preprocessing is necessary, use a locale-aware tool with an explicit
locale, limit it to rendered prose, and review the output before publishing.
Keep transformations such as quote direction, dash style, and spacing in the
`locale-typography` profile or an explicit project house-style rule.

## Locale Profiles Not Yet Covered

`locale-typography` does not yet contain profiles for `pt-PT`, `pt-BR`, or
`es-ES`. For those locales, obtain a reviewed locale or house-style decision
before encoding quotation, dash, number, or spacing rules; add the durable rule
to `locale-typography` rather than creating another table here.

## Print Verification

- Confirm the printed document has the intended `lang` attribute.
- Check nested quotations, punctuation adjacency, and line-break behavior in
  the generated PDF or printed page.
- Verify that numbers, currencies, units, dates, and lists use the exact
  target locale.
- Re-check the output after a preprocessor or font change.
