# CSS Tokens and Theming

Use this module when several components need stable visual roles, theming, or
consumer overrides. Name tokens by their contract, not their current color or
pixel value.

## Build Three Levels

```css
:root {
  --blue-600: oklch(52% 0.18 255);      /* raw value */
  --color-action: var(--blue-600);      /* semantic role */
  --button-background: var(--color-action); /* local contract */
}
```

- Raw values express the available palette, scale, or duration. Semantic tokens
  express product meaning such as surface, text, danger, focus, or action.
  Component tokens expose only a narrow local customization contract.
- Do not make consumers depend on a primitive value when they mean a semantic
  role. Do not create a component token for every declaration with no consumer
  or state boundary.
- Theme through semantic tokens and verify light, dark, forced-colors, focus,
  and disabled states. `light-dark()` can be useful where the support policy and
  explicit color-scheme behavior are understood.
- Record a token's owner and migration path when replacing an established value.
  A visual one-off may need consolidation; it is not automatically a new global
  primitive.

For methodology comparisons, color derivation, and complete architecture
examples, consult the [deep CSS architecture appendix](css-architecture.md).
