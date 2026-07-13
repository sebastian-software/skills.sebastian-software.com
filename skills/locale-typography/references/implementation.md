# Implementation

Use locale data and semantic markup as the source of truth. Treat visible
punctuation replacement as a narrow finishing step.

## HTML and CSS

Set the language on the document and override it on mixed-language passages:

```html
<html lang="fr-CA">
  <p>Elle a répondu <q>Oui</q>.</p>
  <p lang="pl-PL">To jest tekst po polsku.</p>
</html>
```

Prefer semantic quotation markup for actual quotations. Test browser output
for every supported locale before relying on `quotes: auto`; CLDR defaults and
an editorial house style can legitimately differ.

```css
q {
  quotes: auto;
}

[lang] {
  hyphens: auto;
}

code,
kbd,
pre,
samp {
  hyphens: none;
}
```

Do not encode language-specific syllable rules in CSS or rewrite spelling to
simulate a line break. Use `lang`, `hyphens: auto`, and reviewed soft hyphens
for exceptional product names or compounds only.

## JavaScript and TypeScript

Use the full BCP 47 locale:

```js
const locale = "fr-CH";

new Intl.NumberFormat(locale).format(1234567.89);
new Intl.NumberFormat(locale, {
  style: "currency",
  currency: "CHF",
}).format(1234.5);
new Intl.DateTimeFormat(locale, { dateStyle: "long" }).format(date);
new Intl.ListFormat(locale, { style: "long", type: "conjunction" }).format(items);
new Intl.RelativeTimeFormat(locale, { numeric: "auto" }).format(-1, "day");
```

Use `Intl.PluralRules` for message selection and `Intl.Collator` for user-facing
sorting. Prefer a mature message-format layer for plural and grammatical
variants rather than concatenating localized fragments.

## Spaces in source formats

- In prose files, insert the intended Unicode space when the publishing chain
  preserves it.
- In HTML, `&nbsp;` is acceptable when entity style is already used; otherwise
  use Unicode consistently.
- In JavaScript strings, use `\u00A0` or `\u202F` when an invisible literal
  would be hard to review.
- In JSX text nodes, prefer ordinary rendered text plus a clearly named helper
  or explicit escape for generated bindings.

## Verification

Test representative values instead of snapshots copied from another locale:

- positive, negative, zero, decimal, and five-digit numbers;
- currency before and after the value;
- dates where day and month are both at most 12;
- quotations nested one level;
- punctuation at a quotation boundary;
- narrow layouts with number-unit pairs and one-letter function words;
- mixed-language spans and assistive-technology pronunciation.

Record any deliberate deviation as a house-style rule close to the product,
not as a silent override of platform locale data.

## Sources

- [ECMA-402: ECMAScript Internationalization API](https://tc39.es/ecma402/)
- [Unicode Locale Data Markup Language](https://unicode.org/reports/tr35/)
- [MDN: `lang` global attribute](https://developer.mozilla.org/docs/Web/HTML/Reference/Global_attributes/lang)
