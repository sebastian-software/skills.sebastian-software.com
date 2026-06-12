# Interop and Accessibility

Use React libraries and platform interop as implementation tools, not as permission to skip semantic DOM and accessibility checks.

## Working Rules

- Treat Radix, React Aria, and similar libraries as accessibility infrastructure that still needs product-specific labels, states, and layout.
- Use refs and imperative handles only for real imperative integration points such as focus, measurement, animation, and third-party APIs.
- Test custom elements and framework interop for attributes, properties, events, refs, SSR, and hydration behavior.
- Keep accessibility pass-through visible in component APIs.

## Source-Backed Guidance

