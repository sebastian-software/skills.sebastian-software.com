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
### Migrating from Radix to React Aria: Improving Accessibility and UX

- Things ID(s): `EWLPEibbrFkiZbw1RYjbG8`
- Source: <https://argos-ci.com/blog/react-aria-migration?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#187:%20Next.js,%20Expo,%20Popover,%20rethrow,%20SWR,%20React-Query,%20Astro,%20PPR,%20tRPC,%20zsa,%20Memory%20leaks,%20INP,%20RN%20IDE,%20Skia,%20WebGPU,%20RNSC,%20Atlas,%20Re.Pack,%20Prisma,%20SwiftUI,%20Flutter,%20Angular...%20-%2014027931>
- Decision: `secondary`
- Target: `react-interop`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use migration guidance as a comparison lens for Radix and React Aria accessibility and UX tradeoffs.
### React Aria Components - React Aria

- Things ID(s): `F4SxcNqNzc6eTRioiBpS1x`
- Source: <https://react-spectrum.adobe.com/react-aria/react-aria-components.html?ck_subscriber_id=1697729046>
- Decision: `primary`
- Target: `react-interop`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://react-aria.adobe.com/
- Guidance: Use React Aria Components as primary interop/accessibility infrastructure reference, while still requiring product-specific labels and states.

### Goodbye, forwardRef

- Things ID(s): `DDiUYHKpVPG5Za3Zx8EpnC`
- Source: <https://m.youtube.com/watch?v=m4QbeS9BTNU>
- Decision: `secondary`
- Target: `react-interop`
- Transcript extraction: 2026-06-14, 3,059 words
- Guidance: Use as React ref API change/radar context. Keep refs as explicit imperative escape hatches for focus, measurement, animation, and third-party interop; verify the current React version before changing public component APIs.
