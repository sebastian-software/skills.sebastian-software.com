# Responsive Design

Design responsive behavior from content, container, input mode, device constraints, and task density. Mobile is not the only responsive case; large screens, print, hybrid pointers, dynamic viewport units, tables, and responsive media need explicit decisions.

## Working Rules

- Use content and task requirements to choose breakpoints and layout changes.
- Prefer container-aware adaptation for reusable components.
- Treat responsive images, tables, navigation, forms, print, safe areas, and large-screen layouts as first-class responsive concerns.
- Avoid relying on viewport width to infer touch, hover, or pointer precision.
- Coordinate responsive media decisions with performance rules when bytes, LCP, or source discovery are affected.

## Source-Backed Guidance

### Accessible Front-End Patterns For Responsive Tables (Part 1) - Smash

- Things ID(s): `YNbLiP3ydejFvtxQDKKxAK`
- Source: <https://www.smashingmagazine.com/2022/12/accessible-front-end-patterns-responsive-tables-part1/>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for responsive-design with component-development and html-accessibility cross-references: responsive tables have no universal solution; choose layout pattern from data comparison/scanning needs, preserve table semantics, headers, alignment, spacing, visual scanning, and accessibility when transforming tables for small screens.

### Größer und mehr wenn viel Platz da ist

- Things ID(s): `UwB5V42Y9HiqNWqSvz4YBA`
- Source: <http://baymard.com/blog/responsive-upscaling>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://baymard.com/blog/responsive-upscaling
- Guidance: Primary for responsive-design with UX patterns cross-reference: responsive work should include large screens, not only mobile; adapt the same important content into better large-screen packaging, avoid adding low-value content just because space exists, and balance larger imagery, columns, sticky controls, and overview.

### Neue Variante Touch Erkennung

- Things ID(s): `17HCnUvGaMKyxXZVkzLKWY`
- Source: <https://css-tricks.com/touch-devices-not-judged-size/?utm_source=mobilewebweekly&utm_medium=email>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for responsive-design plus component-development: do not infer touch/hover/input precision from viewport size; use pointer, hover, any-pointer, and any-hover to adapt hit areas, visible controls, hover-dependent UI, and card/menu/form component behavior; account for hybrid devices and multiple input mechanisms; cross-reference ux-patterns and html-accessibility.

