---
name: s7n-css-architecture
description: |
  CSS architecture, cascade layers, custom properties, scoping, browser baseline support, progressive enhancement, build tooling, CSS nesting, and maintainable styling systems. Use when organizing CSS, reviewing style architecture, choosing browser-support strategy, or fixing cascade/build problems.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N CSS Architecture

Use this skill for making CSS maintainable, predictable, and compatible with the project's browser-support promise.

## Workflow

1. Identify styling ownership: global reset, tokens, layout primitives, components, utilities, overrides.
2. Define cascade order explicitly with layers or local conventions.
3. Use custom properties for semantic tokens and runtime theming.
4. Choose progressive enhancement boundaries based on the supported baseline.
5. Keep build tooling simple enough that generated CSS remains debuggable.

## Rules

- Avoid specificity arms races; solve ordering and scope instead.
- Do not encode semantic state only in class names when native state or attributes fit better.
- Gate modern CSS with feature queries when unsupported behavior would break the UI.
- Prefer readable source CSS over clever generated output.
- Document exceptions in the local component or token contract, not as global folklore.

## References

- [references/css-architecture.md](references/css-architecture.md) - cascade, layers, scoping, and maintainable CSS.
- [references/baseline-support.md](references/baseline-support.md) - browser baseline and support decisions.
- [references/css-build-tooling.md](references/css-build-tooling.md) - CSS build tooling and generated output rules.
