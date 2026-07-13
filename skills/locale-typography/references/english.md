# English

Support `en-US`, `en-GB`, and `en-CA`. English publishing styles differ more
than the language tag alone suggests, so preserve an established house style.

## Quotation marks

| Locale | Default when no house style exists | Nested |
| --- | --- | --- |
| `en-US` | `“Example”` | `‘Example’` |
| `en-GB` | `‘Example’` | `“Example”` |
| `en-CA` | `“Example”` | `‘Example’` |

- In general US editorial prose, place periods and commas inside the closing
  quotation mark. Place question marks and exclamation points according to
  whether they belong to the quotation.
- In British-oriented and logical-punctuation styles, place punctuation inside
  only when it belongs to the quoted material.
- Do not silently repunctuate an exact quotation. A code, linguistics, or
  technical house style may deliberately prefer logical punctuation.

## Dashes, spaces, and apostrophes

- Use a closed em dash in common US style: `The result—after two retries—passed.`
- Use a spaced en dash in common British style: `The result – after two retries – passed.`
- Follow the product's established dash style in Canadian English.
- Put no space before `, . : ; ? !`.
- Use curly apostrophes in contractions and possessives: `don’t`, `the team’s`.
- Do not add an apostrophe to ordinary plurals such as `APIs`, `1990s`, or
  `URLs`.
- Keep a number and abbreviated unit together when a break would be confusing.

## Locale-sensitive data

Never encode ambiguous numeric dates such as `03/04/2026` in shared content.
Use `Intl.DateTimeFormat` or spell the month. Use the complete locale for
currency, grouping, decimal punctuation, measurement conventions, and time.

Treat the serial comma, title capitalization, abbreviation periods, and the
spelling of words such as `color/colour` as house-style or language-editing
questions rather than automatic typography corrections.

## Sources

- [GOV.UK style guide](https://www.gov.uk/guidance/style-guide)
- [Government of Canada: English and French punctuation spacing](https://www.noslangues-ourlanguages.gc.ca/writing-tips-plus/spacing)
- [Unicode CLDR: delimiters](https://cldr.unicode.org/translation/core-data/characters)
