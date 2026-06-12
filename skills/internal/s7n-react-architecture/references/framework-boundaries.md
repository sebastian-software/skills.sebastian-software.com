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

