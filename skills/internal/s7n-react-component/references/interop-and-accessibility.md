# Interop and Accessibility

Use React libraries and platform interop as implementation tools, not as permission to skip semantic DOM and accessibility checks.

## Working Rules

- Treat Radix, React Aria, and similar libraries as accessibility infrastructure that still needs product-specific labels, states, and layout.
- Use refs and imperative handles only for real imperative integration points such as focus, measurement, animation, and third-party APIs.
- Test custom elements and framework interop for attributes, properties, events, refs, SSR, and hydration behavior.
- Keep accessibility pass-through visible in component APIs.

## Source-Backed Guidance
### Upcoming custom element support in React

- Things ID(s): `F2b8oMKPck9CBqQooEqZc7`, `TyY59H1w8RYcdG3nVsS6VQ`, `677keroerttLyiagzAjjL3`
- Source: <https://piccalil.li/blog/upcoming-custom-element-support-in-react/?ref=main-rss-feed>
- Decision: `primary`
- Target: `react-interop`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use React custom-element support as current interop guidance for attributes, properties, events, refs, and framework support.

