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
### What's new in CSS and UI: I/O 2023 Edition - Chrome Developers

- Things ID(s): `NNV8cwLuZa577Rwiyu51TY`
- Source: <https://developer.chrome.com/blog/whats-new-css-ui-2023/?utm_source=CSS-Weekly&utm_campaign=Issue-550&utm_medium=email>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Chrome CSS/UI I/O 2023 as platform radar, not concrete implementation rules.
### The (Frontend||UI||UX) Developer/Engineer Handbook 2024

- Things ID(s): `YPjE7QDNrmiqjNwqKMzcKX`
- Source: <https://frontendmasters.com/guides/front-end-handbook/2024/?utm_source=CSS-Weekly&utm_medium=newsletter&utm_campaign=issue-585-april-25-2024>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use frontend handbook as broad background/radar source only.
### web.dev

- Things ID(s): `BezGoFfMZr5zFxDLrSfRjh`
- Source: <https://web.dev/baseline?hl=de>
- Decision: `primary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use official web.dev Baseline reference for browser feature availability policy.
### What You Need to Know about Modern CSS (2025 Edition) - Frontend Mas

- Things ID(s): `GE57sYjLMCe7H5RESLcnsV`
- Source: <https://frontendmasters.com/blog/what-you-need-to-know-about-modern-css-2025-edition/?utm_source=the-index&utm_medium=newsletter>
- Decision: `secondary`
- Target: `baseline`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Modern CSS 2025 as platform radar and currentness source.

