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

