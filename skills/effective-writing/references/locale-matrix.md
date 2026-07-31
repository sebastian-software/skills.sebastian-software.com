# Locale matrix

Use the language profile for punctuation and the complete locale for dynamic
data. Rows described as regional-data-only do not invent a separate writing
system; apply the language profile and let `Intl`/CLDR supply regional formats.

| Locale | Language profile | Regional rule or default |
| --- | --- | --- |
| `de-DE` | German | Default German profile. |
| `de-AT` | German | German quote system; preserve Austrian terminology and house style. |
| `de-CH` | German | Swiss quotes and `ss` instead of `ß`. |
| `de-BE` | German | German punctuation; Belgian regional data. |
| `de-LU` | German | German punctuation; Luxembourg regional data. |
| `en-US` | English | US quotation punctuation and US regional data. |
| `en-GB` | English | British editorial defaults and UK regional data. |
| `en-CA` | English | Canadian English house style and Canadian regional data. |
| `fr-FR` | French | Metropolitan French spacing defaults. |
| `fr-CA` | French | Canadian French punctuation spacing. |
| `fr-CH` | French | Swiss regional data; confirm publisher spacing and nested quotes. |
| `fr-BE` | French | Belgian regional data; confirm publisher spacing. |
| `fr-LU` | French | Luxembourg regional data; confirm publisher spacing. |
| `nl-NL` | Dutch | Dutch editorial defaults and Netherlands regional data. |
| `nl-BE` | Dutch | Dutch-language Belgian house style and regional data. |
| `lb-LU` | Luxembourgish | Official Luxembourgish punctuation and Luxembourg regional data. |
| `es-ES` | Spanish | Peninsular Spanish punctuation and regional data. |
| `it-IT` | Italian | Italian editorial defaults. |
| `it-CH` | Italian | Italian punctuation with Swiss regional data. |
| `da-DK` | Danish | Danish punctuation and regional data; `»…«` outer quotes when no house style exists. |
| `nb-NO` | Norwegian | Bokmål text with Norwegian punctuation and regional data. |
| `nn-NO` | Norwegian | Nynorsk text with the same typographic profile; do not change spelling. |
| `sv-SE` | Swedish | Swedish punctuation and regional data. |
| `pl-PL` | Polish | Apply the Polish rules effective from 1 January 2026. |
| `cs-CZ` | Czech | Czech punctuation and regional data. |
| `hr-HR` | Croatian | Croatian punctuation and regional data. |

For a bare language tag, use the project's configured default region. If none
exists, prefer `de-DE`, `en-US`, `fr-FR`, `nl-NL`, `es-ES`, `it-IT`, `da-DK`,
`nb-NO`, `sv-SE`, `pl-PL`, `cs-CZ`, `hr-HR`, or `lb-LU` only for low-risk
drafting. Ask before publication when regional typography differs.
