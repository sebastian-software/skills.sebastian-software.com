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
### Color Shifting in CSS • Josh W. Comeau

- Things ID(s): `NwAFPEuYCCySvUqkKHLUQ7`
- Source: <https://www.joshwcomeau.com/animation/color-shifting/>
- Decision: `secondary`
- Target: `motion-interaction`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use color-shifting animation as a motion/effects example; require reduced-motion and readability checks.
### CSS Stärkung Style

- Things ID(s): `PKAn2UtGhMZx833zTDuwRD`
- Source: <https://www.joshwcomeau.com/css/starting-style/>
- Decision: `primary`
- Target: `motion-interaction`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use CSS `@starting-style` as entry-transition guidance with support and fallback checks.
### Introducing "Unleash the power of Scroll-Driven Animations" | Blog |

- Things ID(s): `PefC88bAi4AggCxR6R8tnR`
- Source: <https://developer.chrome.com/blog/scroll-driven-animations-video-course?hl=en>
- Decision: `primary`
- Target: `motion-interaction`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use official scroll-driven animation material as primary reference for scroll-linked motion with progressive enhancement.

