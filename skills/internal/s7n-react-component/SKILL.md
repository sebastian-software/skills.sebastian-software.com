---
name: s7n-react-component
description: |
  This skill should be used when the user asks to "build a React component", "design a React component API", "refactor React components", "review component composition", "implement controlled or uncontrolled state", "wire React forms", "integrate React Aria or Radix", "support custom elements in React", or "harden reusable React UI". It covers component APIs, composition, state surfaces, refs, form state, interop, accessibility pass-through, and resilient UI states.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N React Component

Use this skill for reusable React component work. Keep React-specific API decisions connected to semantic HTML, accessibility, forms UX, responsive layout, and motion rules from `s7n-ui-design`.

## Workflow

1. Inspect the existing component conventions: prop naming, state ownership, styling API, accessibility patterns, form library, refs, portals, and test setup.
2. Choose the component boundary: primitive, composed widget, app-specific component, or thin adapter around a headless library.
3. Define state ownership: controlled, uncontrolled, externally managed, form-managed, or derived.
4. Preserve semantic DOM and accessible names. Load `s7n-ui-design` references for HTML/accessibility, forms, component development, responsive design, and motion when the component renders UI.
5. Expose stable extension points: slots/children, `as`/polymorphism only when justified, data attributes, CSS custom properties, refs, and event callbacks.
6. Harden states: loading, empty, error, disabled, success, focus, hover, reduced motion, translated text, SSR/hydration, and async transitions.

## Reference Files

- [references/component-api-design.md](references/component-api-design.md) - Composition, polymorphism, slots, and reusable APIs.
- [references/forms-and-state.md](references/forms-and-state.md) - React forms, data binding, controlled state, and state ownership.
- [references/interop-and-accessibility.md](references/interop-and-accessibility.md) - React Aria, Radix, custom elements, refs, and accessibility pass-through.

## Boundaries

Use `s7n-react-architecture` for React Server Components, hydration, rendering boundaries, and app-level performance architecture. Use `s7n-ui-design` for visual design and framework-agnostic UI quality rules.
