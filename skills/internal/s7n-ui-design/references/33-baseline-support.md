# Baseline and Browser Support

Use current browser-support evidence before turning modern web-platform features into defaults. Baseline, official documentation, and project support policy should drive adoption, not novelty.

## Working Rules

- Prefer Baseline and official platform documentation over anecdotal support guesses.
- Separate feature-radar sources from implementation-rule sources.
- Add `@supports`, progressive enhancement, fallback behavior, or project-specific support constraints when using newly available features.
- Connect support policy to Browserslist, linting, CI, and design-system defaults where possible.

## Additional Rules

- Practitioner default snippets around logical properties, reduced-motion guarded View Transitions, custom properties, OKLCH, focus-visible, text-wrap, hanging punctuation, low-specificity :where(), cascade layers, and line-height units; useful as habit/radar guidance, not a normative rule.
- Commentary on global CSS starters/resets, cascade layers, fluid root type, text wrapping, form/table defaults, motion preference guards, and team-specific foot-guns; not a normative starter to copy verbatim.
- Duplicate/tracking variant of the Coyier CSS starter commentary; decide together with 7ajo7EGH54gSpHF6dSemLW.
- Platform-radar guidance for Baseline, Web Platform Dashboard, support-policy tooling through Browserslist/ESLint/Stylelint/IDE integrations, and prioritization of newly available APIs such as Anchor Positioning, View Transitions, details enhancements, hidden=until-found, @scope, scrollend, and Core Web Vitals APIs; use as support-policy/radar guidance, not as detailed pattern guidance.
- Duplicate/supporting modern CSS radar guidance.
- Use Chrome CSS/UI I/O 2023 as platform radar, not concrete implementation rules.
- Use frontend handbook as broad background/radar guidance only.
- Use Baseline rule for browser feature availability policy.
- Use Modern CSS 2025 as platform radar and currentness guidance.
- Use Chrome Web UI I/O 2025 as platform radar for native UI capabilities.
