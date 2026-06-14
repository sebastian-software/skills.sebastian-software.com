# Framework Boundaries

Use framework features deliberately. Rendering mode, routing, data fetching, CSS delivery, Server-Timing, and build constraints shape React architecture.

## Working Rules

- Check what the framework does at build time, request time, stream time, and hydration time.
- Keep CSS and styling choices compatible with server/client boundaries.
- Use observability such as Server-Timing when architecture decisions need production feedback.
- Avoid treating one framework's RSC or routing behavior as universal React behavior.

## Source-Backed Guidance
### Crafting the Next.js Website

- Things ID(s): `55GsQdEtimywvuTdzNMR8H`
- Source: <https://rauno.me/craft/nextjs?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23143%3A+RSC+Quiz%2C+useFormStatus%2C+Next.js+Website%2C+Panda+CSS%2C+useLayoutEffect%2C+Million.js%2C+Immer%2C+Super+Apps%2C+React-Three-Fiber%2C+Vite...%20-%2010625518>
- Decision: `secondary`
- Target: `framework`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as framework-site architecture case study, not as universal Next.js guidance.
### CSS in React Server Components

- Things ID(s): `p5XfqJB3Kpx4ATxfrtbSt`
- Source: <https://www.joshwcomeau.com/react/css-in-rsc/>
- Decision: `secondary`
- Target: `framework`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use CSS-in-RSC source for styling constraints across server/client boundaries.
### Modern CSS For Dynamic Component-Based Architecture | Modern CSS Sol

- Things ID(s): `KedFFWf1rEpPGYsxhMXKDB`
- Source: <https://moderncss.dev/modern-css-for-dynamic-component-based-architecture/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23148%3A+Remix+Routing%2C+Hydration%2C+React.FC%2C+Vite+%2B+RSC%2C+Zedux%2C+Astro%2C+Tremor%2C+Valhalla%2C+Reanimated%2C+Expo-Apple-Targets%2C+XCode+15...%20-%2011002426>
- Decision: `secondary`
- Target: `framework`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as dynamic component/CSS architecture source, with framework and browser-support caveats.
### How Next.js breaks React Fundamentals (Examples) | Ondrej Velisek

- Things ID(s): `AFU1R3G9xzTNbnepRCd6Y3`
- Source: <https://ondrejvelisek.github.io/how-nextjs-breaks-react-fundamentals/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#178:%20Remix%20and%20Vite,%20Type-safe%20Children,%20Astro%20DB,%20React%20Compiler,%20Firebolt,%20Vitest,%20Composition,%20Remix%20Nitro,%20RSC%20in%20React%20Native,%20TenTap,%20Expo%20Atlas,%20TypeScript,%20Elysia...%20-%2013399704>
- Decision: `secondary`
- Target: `react-architecture`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Retarget to React architecture: use as framework-boundary caveat source for Next.js vs React fundamentals.

### Asset loading in React

- Things ID(s): `KXorttcJMbTTaaaM6KnXog`
- Source: <https://m.youtube.com/watch?v=dxWLp-8mXes>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 2,120 words
- Guidance: Use as React asset-loading radar/context. Keep asset priority, preload, discovery, and render timing coordinated with browser-performance rules rather than treating asset loading as only a component concern.

### I Didn't Know Next.js Server Actions Could Do This!

- Things ID(s): `FVdnJMA2yW4QgrYhfmhxf`
- Source: <https://m.youtube.com/watch?v=ZZCXnNAOqqU>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 1,543 words
- Guidance: Use as Next.js Server Actions capability context. Before adopting patterns, verify current framework behavior around validation, auth, redirects, cache invalidation, error handling, progressive enhancement, and form semantics.

### Nextjs Server Actions Just Got Better

- Things ID(s): `XA6tVGijwpAMV7H8kdGfHq`
- Source: <https://m.youtube.com/watch?v=ahB3DgUMs1A>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 2,522 words
- Guidance: Use as Server Actions update/radar source. Treat API changes as framework-version-specific and pair with official Next.js docs before encoding rules.

### I Was Wrong About React Router

- Things ID(s): `7otzbFZ55ksUFhpP7S9gS5`
- Source: <https://m.youtube.com/watch?v=m86HssTKExU>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 4,377 words
- Guidance: Use as React Router architecture tradeoff context: routing, data loading, server rendering, and framework features should be evaluated as a coherent app architecture, not as isolated library preferences.

### React Router 7.2 Just Added This GAME-CHANGING Feature!

- Things ID(s): `tpWThWDAcdaAzGGr1v2G7`
- Source: <https://m.youtube.com/watch?v=6zwi5O3CST8>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 1,668 words
- Guidance: Use as React Router feature-radar context. Verify current React Router docs before relying on specific APIs in skill guidance.

### An Honest Review of TanStack vs Next.js

- Things ID(s): `KDKoKoAJEHSufpuCMXtszp`, `RQ2ueLwCSfzGtQY2YVAm9D`
- Source: <https://m.youtube.com/watch?v=D27AfH0pSp8>
- Decision: `secondary`
- Target: `framework`
- Transcript extraction: 2026-06-14, 5,195 words
- Guidance: Use as framework comparison context. Capture tradeoffs around routing, data loading, server rendering, deployment model, ecosystem maturity, and team familiarity instead of turning one framework into a default.
