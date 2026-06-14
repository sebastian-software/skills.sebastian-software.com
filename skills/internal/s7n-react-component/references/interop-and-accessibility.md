# Interop and Accessibility

Use React libraries and platform interop as implementation tools, not as permission to skip semantic DOM and accessibility checks.

## Working Rules

- Treat Radix, React Aria, and similar libraries as accessibility infrastructure that still needs product-specific labels, states, and layout.
- Use refs and imperative handles only for real imperative integration points such as focus, measurement, animation, and third-party APIs.
- Test custom elements and framework interop for attributes, properties, events, refs, SSR, and hydration behavior.
- Keep accessibility pass-through visible in component APIs.

## Additional Rules

- Use React custom-element support as current interop guidance for attributes, properties, events, refs, and framework support.
- Use migration guidance as a comparison lens for Radix and React Aria accessibility and UX tradeoffs.
- Use React Aria Components as interop/accessibility infrastructure rule, while still requiring product-specific labels and states.
- Use as React ref API change/radar context. Keep refs as explicit imperative escape hatches for focus, measurement, animation, and third-party interop; verify the current React version before changing public component APIs.
