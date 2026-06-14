---
name: s7n-i18n-ux
description: |
  Internationalized UX, localization, RTL interfaces, text expansion, locale-aware layout, number/date formatting, translation-safe copy, and multilingual frontend checks. Use when building or reviewing UI for multiple languages, German/English switching, RTL support, or locale-specific formatting.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N I18n UX

Use this skill when UI must survive translation, locale changes, longer strings, bidirectional text, or different formatting conventions.

## Workflow

1. Identify supported locales, scripts, directionality, and formatting requirements.
2. Replace layout assumptions based on English string length.
3. Use locale-aware formatting for dates, numbers, currency, addresses, and names.
4. Check RTL mirroring for layout, icons, navigation, and directional language.
5. Verify truncation, wrapping, pluralization, sorting, and search behavior.

## Rules

- Do not concatenate translated strings from fragments with fixed order.
- Avoid text embedded in images or icons when it must be localized.
- Use logical CSS properties where direction can vary.
- Let translated strings wrap; containers must not depend on exact wording.
- Keep source copy clear enough for translators to preserve intent.

## References

- [references/17-i18n-rtl.md](references/17-i18n-rtl.md) - RTL and international layout concerns.
- [references/30-i18n-ux.md](references/30-i18n-ux.md) - localization, formatting, and translation-safe UX rules.
