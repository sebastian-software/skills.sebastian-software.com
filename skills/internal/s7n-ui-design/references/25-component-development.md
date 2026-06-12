# Component Development

Build components as durable interface primitives: semantic DOM first, clear state surfaces, predictable layout ownership, resilient focus behavior, and configurable CSS APIs.

## Working Rules

- Preserve native controls and semantics whenever possible.
- Separate component internals from parent layout; component internals may use `gap`, while outer layout owns spacing between components.
- Expose state through real DOM state, attributes, data attributes, and custom properties instead of hidden implementation details.
- Define disabled, loading, empty, error, success, hover, focus, active, reduced-motion, high-contrast, and translated-text behavior.
- Keep component APIs portable across plain HTML/CSS, React, and Web Components unless framework specifics are required.

## Source-Backed Guidance

### Build a fully-responsive, progressively enhanced burger menu - Picca

- Things ID(s): `AXsJMeRBGH82pzPNZYg7ng`
- Source: <https://piccalil.li/blog/build-a-fully-responsive-progressively-enhanced-burger-menu>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://piccalil.li/blog/build-a-fully-responsive-progressively-enhanced-burger-menu/
- Guidance: Primary for framework-agnostic component-development: progressive responsive navigation/disclosure, semantic nav baseline, skip links, focus flow, minimum viable experience, and JS as enhancement rather than replacement.

