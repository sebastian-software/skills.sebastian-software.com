[← Sebastian Software Skills](../../README.md)

# Locale Typography

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Make visible prose look as though it belongs to the reader's locale, not as
though punctuation and spacing survived a generic translation pass.**

Locale Typography helps agents write, edit, localize, proofread, and implement
locale-appropriate visible text in Markdown, HTML, JSX, templates, interfaces,
documents, and print layouts. It provides focused guidance for 26 European and
North American locale profiles.

## What It Covers

- quotation marks and nested quotations
- punctuation and non-breaking spacing
- hyphens, en dashes, em dashes, and ranges
- apostrophes and elision
- numbers, dates, times, units, and currencies
- line-breaking hazards and hyphenation
- implementation with locale-aware platform APIs
- mixed-language content and intentional house-style exceptions

Supported language families include German, English, French, Dutch,
Luxembourgish, Spanish, Italian, Danish, Norwegian, Swedish, Polish, Czech, and
Croatian, with regional distinctions where they matter.

## Example Prompts

```text
Proofread this German landing page for quotation marks, dashes, non-breaking
spaces, dates, prices, and line-breaking problems.

Localize the visible typography in this JSX from US English to Canadian French
without changing identifiers, URLs, props, or code literals.

Review this multilingual report for locale-specific number, currency, and date
formatting, then replace hardcoded formatting with the appropriate APIs.

Apply the existing house style where it is intentional and report only the
places where locale correctness still breaks.
```

See [SKILL.md](SKILL.md) for locale detection, shared rules, language profiles,
implementation guidance, and editing boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill locale-typography
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian locale-typography
dalo approve skill sebastian:locale-typography
dalo sync
```

## Related Skills

- [Effective Web](../effective-web/README.md) handles internationalization UX,
  RTL, responsive text expansion, webfonts, and frontend implementation.
- [Web Legal Compliance](../web-legal-compliance/README.md) establishes required
  legal wording before locale typography is applied.
- [Metro English](../metro-english/README.md) changes professional voice and
  register; this skill handles locale correctness after the wording is stable.
- [Consultant Profile](../consultant-profile/README.md) creates and localizes the
  underlying professional profile content.

## Scope

This is not a general grammar, translation, or house-style rewrite. It changes
visible prose only and preserves code, identifiers, URLs, paths, commands, data
keys, attribute values, and copy-paste literals unless the user explicitly asks
otherwise.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).
