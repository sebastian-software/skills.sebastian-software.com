# Component API Design

Design React component APIs so composition, state, styling, and semantics remain predictable as components are reused.

## Working Rules

- Prefer clear composition over prop surfaces that encode every possible layout.
- Use polymorphic `as` APIs only when the semantic element truly must vary.
- Keep accessible names, roles, focus behavior, and disabled behavior explicit.
- Expose styling hooks without forcing consumers to know private DOM structure.

## Source-Backed Guidance
### Advanced React component composition

- Things ID(s): `ESpokt4xw8RoDmGhedyQer`
- Source: <https://frontendmastery.com/posts/advanced-react-component-composition-guide/>
- Decision: `secondary`
- Target: `react-api`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Advanced composition source for separating layout, behavior, and extension points in reusable React component APIs.
### Behind the ‘as’ prop: polymorphism done well - Kristóf Poduszló

- Things ID(s): `L1pFuPGLJtiFqvUU3i4Kkt`
- Source: <https://www.kripod.dev/blog/behind-the-as-prop-polymorphism-done-well/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#187:%20Next.js,%20Expo,%20Popover,%20rethrow,%20SWR,%20React-Query,%20Astro,%20PPR,%20tRPC,%20zsa,%20Memory%20leaks,%20INP,%20RN%20IDE,%20Skia,%20WebGPU,%20RNSC,%20Atlas,%20Re.Pack,%20Prisma,%20SwiftUI,%20Flutter,%20Angular...%20-%2014027931>
- Decision: `secondary`
- Target: `react-api`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as typed polymorphic component API guidance; require semantic safety before adding an `as` prop.
### Building Swipe Actions component with React and Framer Motion · Oleg

- Things ID(s): `31ji52rMMiXpW5b4URoMgg`
- Source: <https://sinja.io/blog/swipe-actions-react-framer-motion?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#197:%20Waku,%20Effect,%20TanStack,%20Framer%20Motion,%20use(>
- Decision: `secondary`
- Target: `react-api`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Swipe-action implementation is useful as a component interaction example; pair with touch, keyboard, reduced-motion, and destructive-action recovery rules.

