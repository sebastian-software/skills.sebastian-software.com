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

### Building Low Level Components the Radix Way | Alex Kondov - Software

- Things ID(s): `96XkrXULWNjnRvUThPRtxW`
- Source: <https://alexkondov.com/building-low-level-components-the-radix-way/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23160%3A+Remix%2C+Next.js%2C+Expo+API+Routes%2C+Ladle%2C+MDXEditor%2C+Sonner%2C+Docusaurus%2C+AbortController%2C+Query+String%2C+Menubar%2C+VisionCamera%2C+Victory+Native+XL%2C+Bun%2C+ESLint%2C+TC39...%20-%2011844219>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for framework-agnostic component-development: low-level primitives, composable APIs, unstyled accessible components, DOM/data-attribute state, controlled/uncontrolled state, and maintainable layering; not React-specific.

