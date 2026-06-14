# CSS Build Tooling

Use this reference when CSS tooling, utility frameworks, CSS-in-TypeScript, generated CSS, or build-time styling decisions affect component APIs, design tokens, runtime cost, or maintainability.

## Working Rules

- Treat CSS tooling as an implementation layer for design-system and component rules, not as a substitute for them.
- Prefer build-time or zero-runtime styling when it improves type safety and removes runtime work without hiding plain CSS behavior.
- Use utility composition escape hatches sparingly, especially when they can duplicate output or obscure component boundaries.
- Check generated CSS size, cascade behavior, token consistency, and framework upgrade paths before codifying tooling patterns.

## Additional Rules

- Tailwind @apply can be an escape hatch for third-party markup or token reuse, but should not become a default abstraction; pair with Tailwind guidance on utility-first reuse and CSS output duplication caveats.
- Vanilla-extract-specific architecture example for zero-runtime CSS, TypeScript theme contracts, createTheme, style/styleVariants, Sprinkles, Recipes, tokens, dark mode, and variant APIs; keep as tool-specific example rather than general styling rule.
- Type-safe Tailwind-style utilities and vanilla-extract belong to styling architecture, not motion.
- Use frontend terminal guide as developer workflow support; keep out of UI rules.
- Use default-export guidance as build/tooling policy context.
