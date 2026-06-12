# CSS Build Tooling

Use this reference when CSS tooling, utility frameworks, CSS-in-TypeScript, generated CSS, or build-time styling decisions affect component APIs, design tokens, runtime cost, or maintainability.

## Working Rules

- Treat CSS tooling as an implementation layer for design-system and component rules, not as a substitute for them.
- Prefer build-time or zero-runtime styling when it improves type safety and removes runtime work without hiding plain CSS behavior.
- Use utility composition escape hatches sparingly, especially when they can duplicate output or obscure component boundaries.
- Check generated CSS size, cascade behavior, token consistency, and framework upgrade paths before codifying tooling patterns.

## Source-Backed Guidance

### Tailwind's @apply Feature is Better Than it Sounds | CSS-Tricks

- Things ID(s): `3Yiw2X5Df8N3SW6c2rbGjD`, `BUcVr8BFyK5GE9jZy33PUv`
- Source: <https://css-tricks.com/tailwinds-apply-feature-is-better-than-it-sounds/>
- Decision: `secondary`
- Target: `build-tooling`
- URL recheck: 2026-06-13, HTTP 200
- Duplicate handling: canonical entry for 2 Things items.
- Guidance: Secondary for build-tooling with design-system/component-development cross-references: Tailwind @apply can be an escape hatch for third-party markup or token reuse, but should not become a default abstraction; pair with Tailwind official guidance on utility-first reuse and CSS output duplication caveats.

### Writing Performant CSS with vanilla-extract | Lennart Jörgens

- Things ID(s): `KGe4g1QciSLNCwL6LCH8eU`
- Source: <https://www.lekoarts.de/javascript/writing-performant-css-with-vanilla-extract?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23124%3A+FLIP%2C+Lifecycle%2C+Next.js%2C+TypeScript%2C+Vanilla-Extract%2C+LiveView%2C+Remix%2C+GitHub%2C+Race+Conditions%2C+Fontpie%2C+Remotion...%20-%209416696>
- Decision: `secondary`
- Target: `build-tooling`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://www.lekoarts.de/writing-performant-css-with-vanilla-extract/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23124%3A+FLIP%2C+Lifecycle%2C+Next.js%2C+TypeScript%2C+Vanilla-Extract%2C+LiveView%2C+Remix%2C+GitHub%2C+Race+Conditions%2C+Fontpie%2C+Remotion...%20-%209416696
- Guidance: Secondary for build-tooling with design-system and component-development cross-references: useful vanilla-extract-specific architecture example for zero-runtime CSS, TypeScript theme contracts, createTheme, style/styleVariants, Sprinkles, Recipes, tokens, dark mode, and variant APIs; keep as tool-specific example rather than general styling rule source.

