# CSS Build Tooling

Use this reference when CSS tooling, utility frameworks, CSS-in-TypeScript, generated CSS, or build-time styling decisions affect component APIs, design tokens, runtime cost, or maintainability.

## Working Rules

- Treat CSS tooling as an implementation layer for design-system and component rules, not as a substitute for them.
- Prefer build-time or zero-runtime styling when it improves type safety and removes runtime work without hiding plain CSS behavior.
- Use utility composition escape hatches sparingly, especially when they can duplicate output or obscure component boundaries.
- Check generated CSS size, cascade behavior, token consistency, and framework upgrade paths before codifying tooling patterns.
- Reserve Tailwind `@apply` for narrow cases such as styling third-party markup or reusing a token set; do not let it become a default abstraction, since it duplicates output and hides component boundaries that utility-first markup would make explicit.
- When using a zero-runtime CSS-in-TypeScript tool (such as vanilla-extract), express tokens through a typed theme contract (`createTheme`) and model variants with the tool's own primitives (`styleVariants`, recipes, sprinkles) so the type system enforces token usage and dark mode at build time.
- Wire the project's browser-support target into tooling: Browserslist, Baseline-aware linting, Stylelint/ESLint rules, IDE warnings, and CI should all reflect the same support policy rather than scattered assumptions.
- Keep generated CSS inspectable; if a styling tool hides cascade order, specificity, duplication, or runtime injection cost, treat that as architecture risk.
- Keep `@supports` blocks and progressive-enhancement fallbacks next to the feature they guard, and re-review the support target when the project drops old browsers, enters an enterprise/WebView environment, or adopts a newly available platform feature.

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
