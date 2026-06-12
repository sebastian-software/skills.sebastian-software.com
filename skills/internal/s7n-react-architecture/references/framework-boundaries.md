# Framework Boundaries

Use framework features deliberately. Rendering mode, routing, data fetching, CSS delivery, Server-Timing, and build constraints shape React architecture.

## Working Rules

- Check what the framework does at build time, request time, stream time, and hydration time.
- Keep CSS and styling choices compatible with server/client boundaries.
- Use observability such as Server-Timing when architecture decisions need production feedback.
- Avoid treating one framework's RSC or routing behavior as universal React behavior.

## Source-Backed Guidance

