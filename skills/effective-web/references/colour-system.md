# Color System and Theming

Use this module to create a palette and token system that can serve brand,
interaction, dark mode, and future components without turning values into
untraceable folklore.

## Build from Roles

1. Define the semantic roles and the contrast relationships they must preserve.
2. Create primitive steps in a perceptually useful space such as OKLCH when the
   browser-support policy permits it.
3. Map semantic tokens to those primitives, then expose only narrow component
   tokens where a consumer needs a real contract.
4. Design dark mode as its own contrast and elevation system; do not simply
   invert the light palette.

- Use relative color syntax, wide-gamut values, and `light-dark()` as progressive
  enhancements with a tested fallback. Keep a stable sRGB path when it is part
  of the product baseline.
- Use translucency and shadows to express elevation sparingly. A surface should
  remain distinguishable when transparency, backdrop effects, or color features
  are unavailable.
- Document semantic ownership and migrate hard-coded values deliberately rather
  than adding another near-duplicate token.

For tonal-gradient math, palette recipes, and specialized elevation patterns,
consult the [deep color appendix](colour.md).
