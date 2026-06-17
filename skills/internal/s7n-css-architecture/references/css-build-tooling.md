# CSS Build Tooling

Use this reference when CSS tooling, utility frameworks, CSS-in-TypeScript, generated CSS, or build-time styling decisions affect component APIs, design tokens, runtime cost, or maintainability.

## Working Rules

- Treat CSS tooling as an implementation layer for design-system and component rules, not as a substitute for them.
- Prefer build-time or zero-runtime styling when it improves type safety and removes runtime work without hiding plain CSS behavior.
- Use utility composition escape hatches sparingly, especially when they can duplicate output or obscure component boundaries.
- Check generated CSS size, cascade behavior, token consistency, and framework upgrade paths before codifying tooling patterns.
- Reserve Tailwind `@apply` for narrow cases such as styling third-party markup or reusing a token set; do not let it become a default abstraction, since it duplicates output and hides component boundaries that utility-first markup would make explicit.
- When using a zero-runtime CSS-in-TypeScript tool (such as vanilla-extract), express tokens through a typed theme contract (`createTheme`) and model variants with the tool's own primitives (`styleVariants`, recipes, sprinkles) so the type system enforces token usage and dark mode at build time.
