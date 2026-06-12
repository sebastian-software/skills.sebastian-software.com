# Component Development

Build components as durable interface primitives: semantic DOM first, clear state surfaces, predictable layout ownership, resilient focus behavior, and configurable CSS APIs.

## Working Rules

- Preserve native controls and semantics whenever possible.
- Separate component internals from parent layout; component internals may use `gap`, while outer layout owns spacing between components.
- Expose state through real DOM state, attributes, data attributes, and custom properties instead of hidden implementation details.
- Define disabled, loading, empty, error, success, hover, focus, active, reduced-motion, high-contrast, and translated-text behavior.
- Keep component APIs portable across plain HTML/CSS, React, and Web Components unless framework specifics are required.

## Source-Backed Guidance

