---
name: locale-typography
description: >-
  Apply and review locale-appropriate typography in visible prose for German,
  English, French, Dutch, Luxembourgish, Spanish, Italian, Danish, Norwegian,
  Swedish, Polish, Czech, and Croatian. Use when writing, editing, localizing,
  proofreading, or implementing text in Markdown, HTML, JSX, templates, UI
  copy, documents, or print layouts where quotation marks, punctuation spacing,
  dashes, apostrophes, non-breaking spaces, numbers, dates, currency, or
  hyphenation must match a supported language and region.
---

# Locale Typography

Produce typography that belongs to the reader's locale without turning the
task into a grammar, translation, or house-style rewrite.

## Workflow

1. Determine the locale from an explicit locale tag, the document's `lang`,
   product configuration, or the stated audience. Never infer one language from
   a multilingual country alone.
2. Preserve an established house style when it intentionally differs from the
   locale default. Preserve punctuation inside verbatim quotations unless the
   user asks to normalize it.
3. Read [Shared rules](references/shared-rules.md) and the relevant row in the
   [locale matrix](references/locale-matrix.md).
4. Read only the matching language profile listed below. Load more than one
   profile only for mixed-language content.
5. For web or application code, also read
   [implementation](references/implementation.md). Delegate dynamic numbers,
   units, currency, dates, times, lists, and plurals to locale-aware APIs.
6. Apply changes only to visible prose. Do not alter code, identifiers, URLs,
   file paths, commands, data keys, attribute values, or copy-paste literals.
7. Review nested quotations, punctuation adjacency, line-breaking hazards, and
   locale tags before finishing.

If the locale remains ambiguous and the choice would visibly change the
result, ask for it. For low-risk work, state the assumed locale briefly and
continue.

## Language profiles

- [German](references/german.md): `de-DE`, `de-AT`, `de-CH`, `de-BE`, `de-LU`
- [English](references/english.md): `en-US`, `en-GB`, `en-CA`
- [French](references/french.md): `fr-FR`, `fr-CA`, `fr-CH`, `fr-BE`, `fr-LU`
- [Dutch](references/dutch.md): `nl-NL`, `nl-BE`
- [Luxembourgish](references/luxembourgish.md): `lb-LU`
- [Spanish](references/spanish.md): `es-ES`
- [Italian](references/italian.md): `it-IT`, `it-CH`
- [Danish](references/danish.md): `da-DK`
- [Norwegian](references/norwegian.md): `nb-NO`, `nn-NO`
- [Swedish](references/swedish.md): `sv-SE`
- [Polish](references/polish.md): `pl-PL`
- [Czech](references/czech.md): `cs-CZ`
- [Croatian](references/croatian.md): `hr-HR`

## Boundaries

- Correct typography and locale-sensitive presentation, not spelling,
  grammar, translation, tone, or general content style unless requested.
- Encode durable rules and frequent error cases, not a complete national style
  manual.
- Treat locale defaults as defaults, not universal law. Product terminology,
  legal requirements, quoted source material, and an explicit house style win.
- Do not hand-format dynamic locale data. Use `Intl`, ICU, CLDR-backed
  libraries, or the platform equivalent and test the exact runtime.
- Do not insert manual soft hyphens throughout prose. Prefer correct language
  metadata and automatic hyphenation; add discretionary breaks only for known,
  reviewed exceptions.
