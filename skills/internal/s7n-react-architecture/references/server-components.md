# Server Components

React Server Components move data access and non-interactive rendering to the server,
shipping zero JS for that work, while client components own interactivity. Treat the
boundary as the core decision: what crosses it, in which direction, and what is allowed
to cross. Verify current support before copying APIs across Next.js, React Router, Vite,
or a custom RSC setup.

## The server/client mental model

- Server components are the default. A component stays a server component unless it needs
  interactivity (event handlers, state, effects) or browser-only APIs. Reaching for
  `'use client'` is the exception that must be justified, not the starting point.
- Server components run once on the server and never hydrate, so they add no client JS and
  can use server-only resources directly. They cannot use `useState`, `useEffect`,
  `useRef`, event handlers, or browser APIs. Client components can do all of that but ship
  their code to the browser and re-render there.
- `'use client'` marks an entry point into the client graph, not a single component:
  every module it imports becomes part of the client bundle. Place the directive at the
  leaf of interactivity, not high in the tree, so the server portion stays large and the
  client island stays small.

## Drawing the boundary

- Keep data fetching and static, data-heavy rendering on the server. Isolate the
  interactive pieces (filters, toggles, menus, forms) in small client components. For a
  page that fetches products and shows an interactive filter sidebar: fetch and render the
  product list server-side, and make only the filter controls a client component.
- Pass server-rendered content into client components as `children` (or props) rather than
  importing server components into client modules. A client component can render
  server-provided children it received as props, which keeps the static subtree on the
  server even though an interactive shell wraps it. Importing a server component from a
  client module instead pulls it into the client bundle.
- Push the client boundary down and out: a small interactive control wrapping a large
  static tree (passed as children) ships far less JS than making the whole section a
  client component. Optimize the boundary for "smallest client island", then verify with
  the bundle.

## Data fetching

- Fetch directly inside server components with `async`/`await` against the database or
  internal services; there is no need for a client data-fetching layer for server-owned
  data. This removes the request waterfall and the client cache for that data.
- Fetch in parallel: start independent requests together (e.g. `Promise.all`) or render
  sibling server components that each fetch, so they stream concurrently instead of
  serializing. Avoid sequential `await`s that create a server-side waterfall.
- Do not refetch server data on the client to "make it reactive". Mutate via a server
  action and revalidate, or hydrate a client component with the server-fetched data as
  initial props.

## What can cross the boundary (serialization)

- Everything passed from a server component to a client component as props must be
  serializable: primitives, plain objects/arrays, `Date`, `Map`/`Set`, and — critically —
  JSX/`ReactNode` and Promises. Functions (except server actions), class instances,
  Symbols, and closures are not serializable and will error at the boundary.
- Pass server actions, not arbitrary callbacks, when a client component needs to invoke
  server behavior. A function prop crossing server→client is only allowed when it is a
  `'use server'` action reference.
- Send only what the client needs. Select and shape data on the server rather than passing
  whole records; every serialized prop is bytes in the RSC payload and the initial HTML.
  This is the main bundle/payload tradeoff to weigh against keeping work server-side.

## Streaming and Suspense

- Wrap slow server subtrees in `<Suspense>` with a meaningful fallback so the framework
  streams the shell immediately and flushes each boundary as its data resolves. Place
  boundaries around independently-loading regions, not the whole page, so fast content is
  not held back by the slowest query.
- Stream the page shell first and let data-dependent islands fill in; this improves
  perceived performance without a client loading-state machine. Design the fallback as a
  real skeleton matching final layout to avoid shift — coordinate with
  `s7n-error-loading-states`.
- Pass a Promise from a server component into a client component and unwrap it there with
  `use()` when the client needs to render around streamed data while staying interactive.

## Framework caveats

- RSC is a protocol the framework implements; capabilities and APIs differ across Next.js
  App Router, React Router, Vite-based setups, and custom servers. Confirm support for
  server actions, streaming, caching, and the `'use client'`/`'use server'` directives in
  the target framework's current docs before encoding patterns.
- Treat advanced patterns (async server components composing client islands, passing
  Promises across the boundary) as version-specific capabilities to verify, not blanket
  rules, and pair any rule with current React Working Group / framework documentation.

## Review checklist

- Is server the default, with `'use client'` only at interactivity leaves and the client
  island as small as possible?
- Is data fetched on the server, in parallel, without a client refetch for server-owned
  data?
- Are static subtrees passed as `children` into client shells rather than imported into
  client modules?
- Are all props crossing server→client serializable, with callbacks expressed as server
  actions and payloads trimmed to what the client needs?
- Are slow regions wrapped in scoped `<Suspense>` boundaries that stream independently?
- Is the boundary/streaming behavior verified against the target framework's current docs?
