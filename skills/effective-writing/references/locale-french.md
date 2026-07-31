# French

Support `fr-FR`, `fr-CA`, `fr-CH`, `fr-BE`, and `fr-LU`. Apply the complete
locale: French punctuation spacing is not identical across these regions.

## Quotation marks

Use guillemets for the outer quotation: `« Exemple »`. Keep the text and each
guillemet together with a non-breaking space. A narrow no-break space is common
in high-quality French typesetting when the production system supports it.

For nested quotations, preserve the publisher's convention. Common choices are
curly double quotes, repeated guillemets, and—in Swiss publishing—single
guillemets. Avoid improvising a third nesting level; restructure the sentence
or use a block quotation.

## Punctuation spacing

| Locale | Before `:` | Before `; ? !` |
| --- | --- | --- |
| `fr-FR` | non-breaking space | narrow or regular non-breaking space |
| `fr-CA` | non-breaking space | no space in Canadian government style |
| `fr-CH`, `fr-BE`, `fr-LU` | follow the established regional or publisher style | follow the established regional or publisher style |

All locales use no space before a comma or period and one normal space after
ordinary punctuation. Never leave a breakable line end before a punctuation
mark that requires preceding space.

## Other high-value rules

- Use curly apostrophes in elisions: `l’équipe`, `aujourd’hui`.
- Preserve accents on uppercase letters: `É`, `À`, `Ç`.
- Use a spaced dash for an interruption when the house style permits it; do not
  import a closed US em dash.
- Keep numbers with units, currency, and percent signs according to the exact
  locale's formatted output.
- Do not hand-build dates, decimals, prices, or translated unit phrases.

## Sources

- [Government of Canada: English and French punctuation spacing](https://our-languages.canada.ca/en/writing-tips-plus/spacing)
- [Office québécois de la langue française: Banque de dépannage linguistique](https://vitrinelinguistique.oqlf.gouv.qc.ca/)
- [Unicode CLDR: delimiters](https://cldr.unicode.org/translation/core-data/characters)
