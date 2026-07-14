# CSS Architecture

Use this skill for making CSS maintainable, predictable, and compatible with the project's browser-support promise.

## Workflow

1. Identify styling ownership: global reset, tokens, layout primitives, components, utilities, overrides.
2. Define cascade order explicitly with layers or local conventions.
3. Use custom properties for semantic tokens and runtime theming.
4. Choose progressive enhancement boundaries based on the supported baseline.
   Check the dated feature radar when the model may not know the current
   platform, and promote useful Newly available features with an honest fallback.
5. Keep build tooling simple enough that generated CSS remains debuggable.

## Rules

- Avoid specificity arms races; solve ordering and scope instead.
- Do not encode semantic state only in class names when native state or attributes fit better.
- Gate modern CSS with feature queries when unsupported behavior would break the UI.
- Prefer readable source CSS over clever generated output.
- Document exceptions in the local component or token contract, not as global folklore.

## References

- [css-architecture.md](css-architecture.md) - cascade, layers, scoping, and maintainable CSS.
- [baseline-support.md](baseline-support.md) - browser baseline and support decisions.
- [platform-feature-radar.md](platform-feature-radar.md) - dated leads for recent
  Baseline features that older model knowledge may miss.
- [css-build-tooling.md](css-build-tooling.md) - CSS build tooling and generated output rules.
- [css-layout-responsive.md](css-layout-responsive.md) - intrinsic layout,
  configurable compositions, container behavior, and responsive CSS algorithms.
- [typography-rules.md](typography-rules.md) - fluid type, text metrics, wrapping,
  and authored-content resilience.
- [component-development.md](component-development.md) - semantic component
  state, custom-property contracts, focus, clipping, and local layout ownership.
- [ui-quality-gates.md](ui-quality-gates.md) - semantic fixtures, feature erasure,
  continuous resize, and core-to-enhancement verification.
