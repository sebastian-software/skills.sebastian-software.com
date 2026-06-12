# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation over anecdotal support guesses.
- Separate feature-radar sources from implementation-rule sources.
- Add `@supports`, progressive enhancement, fallback behavior, or project-specific support constraints when using newly available features.
- Connect support policy to Browserslist, linting, CI, and design-system defaults where possible.

## Source-Backed Guidance

### Adactio: Journal-CSS snippets

- Things ID(s): `4m11kz8ZUfiaRXQosiPdmx`
- Source: <https://adactio.com/journal/21896>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for baseline/design-system practice: practitioner default snippets around logical properties, reduced-motion guarded View Transitions, custom properties, OKLCH, focus-visible, text-wrap, hanging punctuation, low-specificity :where(), cascade layers, and line-height units; useful as habit/radar source, not a normative rule source.

### The Coyier CSS starter - Piccalilli

- Things ID(s): `7ajo7EGH54gSpHF6dSemLW`
- Source: <https://piccalil.li/links/the-coyier-css-starter/?utm_source=the-index&utm_medium=newsletter>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for baseline/design-system practice: useful commentary on global CSS starters/resets, cascade layers, fluid root type, text wrapping, form/table defaults, motion preference guards, and team-specific foot-guns; not a normative starter to copy verbatim.

### The Coyier CSS starter - Piccalilli

- Things ID(s): `C3jrBjqmfgTRorm6wJX8hk`
- Source: <https://piccalil.li/links/the-coyier-css-starter/?ref=main-rss-feed>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for baseline/design-system practice: duplicate/tracking variant of the Coyier CSS starter commentary; decide together with 7ajo7EGH54gSpHF6dSemLW.

### What's new in web | Blog | web.dev

- Things ID(s): `Jzu6xaaoRM45KJAzgnJzgx`
- Source: <https://web.dev/blog/whats-new-in-web-io2025?hl=en>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for baseline: official web.dev platform-radar source for Baseline, Web Platform Dashboard, support-policy tooling through Browserslist/ESLint/Stylelint/IDE integrations, and prioritization of newly available APIs such as Anchor Positioning, View Transitions, details enhancements, hidden=until-found, @scope, scrollend, and Core Web Vitals APIs; use as support-policy/radar source, not as detailed pattern guidance.
### What You Need to Know about Modern CSS (Spring 2024 Edition) - Front

- Things ID(s): `SQWBqhYz2wvBeHMtqFK8xz`
- Source: <https://frontendmasters.com/blog/what-you-need-to-know-about-modern-css-spring-2024-edition/?ref=labnotes.org>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Duplicate/supporting modern CSS radar source.

