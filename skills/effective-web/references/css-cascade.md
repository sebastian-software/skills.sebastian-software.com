# CSS Cascade and Scope

Use this module to make style ownership and override order predictable. Solve a
cascade problem before adding selector weight or `!important`.

## Establish an Order

1. Separate reset, base elements, layout primitives, components, utilities, and
   overrides by the project's actual ownership boundaries.
2. Declare cascade-layer order once, near the entry point. Later layers win at
   equal origin and importance; unlayered normal author styles outrank layered
   normal styles, so use unlayered CSS deliberately rather than accidentally.
3. Keep selectors shallow and local. A component should not need knowledge of a
   page's incidental DOM ancestry to render correctly.

```css
@layer reset, base, layout, components, utilities;
```

- Use nesting to improve local readability, not to generate a long descendant
  chain. Check `:is()`-like specificity behavior when nesting a selector list.
- Use `@scope` only when a real local boundary makes styles easier to reason
  about; preserve a usable fallback where support is not part of the baseline.
- Treat `!important` as an explicit exception. Its layer precedence reverses,
  so it is not a general-purpose escape hatch.

For advanced layer ordering, nesting, scope proximity, and anchor-positioning
details, consult the [deep CSS architecture appendix](css-architecture.md).
