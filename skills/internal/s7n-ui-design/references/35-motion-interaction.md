# Motion Interaction

Use motion to explain state change, spatial continuity, feedback, and progress. Avoid decorative motion that delays task completion or makes layout harder to understand.

## Working Rules

- Respect `prefers-reduced-motion` and provide a useful non-motion baseline.
- Keep product UI transitions short and tied to user intent.
- Use View Transitions, scroll-driven animations, keyframes, and entry/exit animations only after support and fallback behavior are clear.
- Preserve focus, scroll position, URL state, and semantic navigation when adding page or component transitions.

## Source-Backed Guidance

### Reibungslose Übergänge mit der View Transition API | View Transition

- Things ID(s): `WnRXZj2vu69LuHodEyqL8n`
- Source: <https://developer.chrome.com/docs/web-platform/view-transitions?hl=de>
- Decision: `primary`
- Target: `motion-interaction`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for motion-interaction with ux-patterns cross-reference: official View Transition API overview for same-document SPA transitions via document.startViewTransition() and cross-document MPA transitions via @view-transition navigation:auto; use for spatial continuity in navigation, filtering/reordering, list-to-detail, and persistent UI, while enforcing prefers-reduced-motion, performance, focus/scroll context, and semantic navigation checks.

