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

### Printing the web: making webpages look good on paper - Piccalilli

- Things ID(s): `3zNQbsyz9k2bM4nzFdLggX`
- Source: <https://piccalil.li/blog/printing-the-web-making-webpages-look-good-on-paper/?utm_source=the-index&utm_medium=newsletter>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for responsive-design with html-accessibility/editorial-ux cross-references: responsive design includes print and other media; define print styles, test print preview, handle page size/breaks, visible links, forms, overflow, navigation removal, grayscale contrast, ink use, and print-color-adjust restraint.

### Styling Tables the Modern CSS Way - Piccalilli

- Things ID(s): `D8RHkqvhUFYNUdYB5iKKKt`
- Source: <https://piccalil.li/blog/styling-tables-the-modern-css-way/?utm_source=the-index&utm_medium=newsletter>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for responsive-design with html-accessibility/component-development cross-references: modern table styling starts with semantic table markup, captions/headers, readable alignment, and accessible overflow wrappers with focus styles and scroll cues rather than destroying table semantics.

### The large, small, and dynamic viewport units

- Things ID(s): `sawtsQjn1r5XtVkh28FqG`
- Source: <https://web.dev/viewport-units/>
- Decision: `primary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://web.dev/blog/viewport-units
- Guidance: Primary for responsive-design with css-layout-responsive/baseline cross-references: use svh/lvh/dvh and logical viewport units intentionally for mobile browser UI, full-height sections, dialogs, and stable vs dynamic viewport behavior; note scrollbar, keyboard, and update-rate caveats.

### "srcset" ist eine gute Wahl für Responsive Images

- Things ID(s): `A2qYFTpTNwJ87VF9JZu7wH`
- Source: <https://css-tricks.com/responsive-images-youre-just-changing-resolutions-use-srcset/>
- Decision: `secondary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Related URLs: <http://caniuse.com/#search=srcset>
- Guidance: Secondary for responsive-design with network-performance cross-reference: durable srcset/resolution-switching concept source, but pair with newer primary image sources such as web.dev Learn Images and LCP image guidance for current browser behavior and delivery rules.

### Designing a Utopian layout grid: Working with fluid responsive value

- Things ID(s): `SJwvvggnGGiv4DFzt7ighv`
- Source: <https://utopia.fyi/blog/designing-a-utopian-layout-grid/>
- Decision: `secondary`
- Target: `responsive-design`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for responsive-design with design-system cross-reference: useful Utopia source for fluid layout grids, min/max design states, spacing/type token handoff, line length, and device-agnostic design-tool setup; keep as design process support rather than normative implementation source.
### The Guide To Responsive Design In 2023 and Beyond - Ahmad Shadeed

- Things ID(s): `3un8g64C5Lurw8yoHFARJX`
- Source: <https://ishadeed.com/article/responsive-design/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23134%3A+Gatsby+%E2%9E%A1%EF%B8%8F+Netlify%2C+React+DOM+for+Native%2C+XState%2C+Flashlight%2C+re-renders%2C+Custom+Hooks%2C+Ignite+Cookbook...%20-%2010021836>
- Decision: `primary`
- Target: `responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Retarget to responsive design: detailed responsive design source should shape layout adaptation, not React architecture.

