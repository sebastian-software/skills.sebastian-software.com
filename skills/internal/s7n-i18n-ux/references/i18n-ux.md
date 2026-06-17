# I18n UX

Design global interfaces so language, country, currency, units, timezone, direction, and shipping/payment context can differ. Inferred locale is a starting point, not a command.

## Working Rules

- Separate language choice from country, region, currency, units, timezone, and fulfilment context.
- Treat an inferred locale (from `Accept-Language` or IP geolocation) as a default, never a lock. Never force a redirect based on it, and always expose an override the user can set and that persists.
- Make locale controls discoverable, reversible, keyboard-accessible, and screen-reader-friendly. Label languages in their own endonym (`Deutsch`, not `German`) and set `lang` plus `dir` on the option so each name renders in its own script.
- Support translated text expansion, RTL, and changed reading order; test forms, navigation, tables, and component labels with long translated strings.
- Render quotation marks and other locale-specific punctuation with CSS rather than literal characters in copy: declare `quotes` per language with `:lang()` and emit `<q>` or `quotes`-aware content so the browser inserts the correct marks (`«»`, `„“`, `“”`) for each locale.
