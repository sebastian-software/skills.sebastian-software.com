[← Sebastian Software Skills](../../README.md)

# Effective Web

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Give your agent one coherent standard for designing, building, reviewing, and
improving production web experiences.**

Effective Web turns broad requests like “make this interface better” into a
routed workflow with explicit guidance for design, implementation,
accessibility, performance, and verification. It covers marketing sites,
content pages, web applications, dashboards, React components, and browser-based
print output without forcing every task through one oversized prompt.

## Why Effective Web

Frontend quality rarely fails in only one discipline. A visually polished page
can still have weak semantics, broken focus order, expensive loading, unclear
states, fragile responsive behavior, or an API that makes future changes harder.

Effective Web treats those concerns as one system. Its 24 intent routes and 91
focused references let an agent load the smallest useful guidance set, then
check the result across the boundaries that matter before calling it done.

## What It Covers

| Area | Capabilities |
| --- | --- |
| Product experience | UI/UX direction, design critique, redesign preservation, attention, mental models, learnability, hierarchy, responsive layout, typography, color, and theming |
| Components and flows | Buttons, navigation, dialogs, forms, tables, reusable primitives, loading states, errors, empty states, and auth UX |
| Inclusive design | Semantic HTML, accessible names, keyboard and focus behavior, screen-reader support, reduced motion, internationalization, RTL, and text expansion |
| Frontend engineering | CSS architecture, browser support, React architecture, component APIs, rendering boundaries, interoperability, and frontend testing |
| Discovery and speed | Frontend SEO, structured data, AI search visibility, Core Web Vitals, resource loading, images, caching, and perceived performance |
| Visual systems | SVG icons, illustrations, paths, animation, noise, grain, organic textures, print stylesheets, paged media, and web-to-print |

## Use It For

- shaping a new interface before implementation
- reducing distraction and bridging unfamiliar product concepts without hiding
  useful capability
- auditing or modernizing an existing site without losing its important
  contracts
- building accessible, responsive components and flows
- making React and CSS architecture decisions in product context
- diagnosing performance, SEO, testing, or browser-support problems
- hardening edge cases, interaction states, internationalization, and auth UX
- producing printable documents with HTML and CSS

## Example Prompts

```text
Audit this dashboard across hierarchy, accessibility, responsive behavior, and
loading cost, then fix the highest-impact problems.

Redesign this marketing page without losing its brand, content, analytics,
routes, SEO metadata, or keyboard behavior.

Build this multi-step form in React with clear validation, resilient loading
and error states, and a component API we can maintain.

Investigate our Core Web Vitals regression and verify the improvement in the
browser.

Turn this HTML report into reliable paged-media output with print typography
and locale-aware page rules.
```

## How It Works

The agent first identifies the primary intent, such as design review, forms,
accessibility, React architecture, performance, SVG, or print. It reads that
route, loads only the supporting references needed for the current problem, and
works against the product's existing language and architecture. Verification
then covers the affected visual states, responsive behavior, keyboard and
screen-reader use, loading cost, and relevant project checks.

See [SKILL.md](SKILL.md) for the complete route table and agent workflow.

## Install This Skill

With the skills CLI:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-web
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian effective-web
dalo approve skill sebastian:effective-web
dalo sync
```

See the collection's [installation guide](../../README.md#installation) for the
complete setup and the difference between selective catalogs and team sources.

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) coordinates wider
  repository work and hands browser-facing design, implementation, and
  verification to this skill.
- [Product Management](../product-management/README.md) establishes the product
  outcome, scope, and quality bar before interface implementation.
- [Product Design](../product-design/README.md) shapes evidence into a problem
  model, interaction system, structure, and prototype before implementation.
- [Locale Typography](../locale-typography/README.md) handles locale-specific
  punctuation, spacing, quotations, numbers, dates, and visible prose.
- [Web Legal Compliance](../web-legal-compliance/README.md) establishes legal,
  privacy, disclosure, and consent requirements before frontend implementation.
- [Decision Records](../decision-records/README.md) preserves durable design and
  architecture choices that should survive future sessions and contributors.
- [Software Validation](../software-validation/README.md) runs existing
  repository-native quality gates when execution and reporting, rather than
  frontend evidence design, is the requested outcome.

## Scope

Effective Web is for browser-facing product work. It does not replace product
discovery, jurisdiction-specific legal analysis, locale-level editorial rules,
backend-only architecture, infrastructure and deployment work, penetration
testing, or non-web print production.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
