# CSS Build Tooling

Use this reference when CSS tooling, utility frameworks, CSS-in-TypeScript, generated CSS, or build-time styling decisions affect component APIs, design tokens, runtime cost, or maintainability.

## Working Rules

- Treat CSS tooling as an implementation layer for design-system and component rules, not as a substitute for them.
- Prefer build-time or zero-runtime styling when it improves type safety and removes runtime work without hiding plain CSS behavior.
- Use utility composition escape hatches sparingly, especially when they can duplicate output or obscure component boundaries.
- Check generated CSS size, cascade behavior, token consistency, and framework upgrade paths before codifying tooling patterns.
- Connect browser-support policy to tooling: Browserslist, Baseline-aware linting, Stylelint/ESLint rules, IDE warnings, and CI should reflect the project's actual support target.
- Make generated CSS inspectable. If a styling tool hides cascade order, specificity, duplication, or runtime injection cost, treat that as architecture risk.

## Baseline Tooling

- Prefer one declared support target rather than scattered assumptions in comments and docs.
- Use Browserslist or equivalent project policy when build tools, transpilers, prefixers, or linters need a browser target.
- Add Baseline-aware linting where available for CSS features that the project should not use yet.
- Keep `@supports` blocks and progressive-enhancement fallbacks close to the feature they guard.
- Review support targets when the project drops old browsers, enters an enterprise/WebView environment, or adopts a newly available platform feature.

## Generated CSS Review

Before adopting or expanding a styling tool, inspect:

- final CSS size and duplication,
- cascade layer order,
- selector specificity,
- critical CSS and code-splitting behavior,
- runtime style injection or hydration requirements,
- token consistency,
- source maps and debug output,
- dark mode and forced-colors behavior,
- upgrade and migration path.

## Additional Rules

- Tailwind @apply can be an escape hatch for third-party markup or token reuse, but should not become a default abstraction; pair with Tailwind guidance on utility-first reuse and CSS output duplication caveats.
- Vanilla-extract-specific architecture example for zero-runtime CSS, TypeScript theme contracts, createTheme, style/styleVariants, Sprinkles, Recipes, tokens, dark mode, and variant APIs; keep as tool-specific example rather than general styling rule.
- Type-safe Tailwind-style utilities and vanilla-extract belong to styling architecture, not motion.
- Use frontend terminal guide as developer workflow support; keep out of UI rules.
- Use default-export guidance as build/tooling policy context.
