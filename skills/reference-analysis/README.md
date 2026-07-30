[← Sebastian Software Skills](../../README.md)

# Reference Analysis

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn websites, screenshots, HTML, prototypes, and videos into specifications
that another person or agent can actually implement and verify.**

Reference Analysis captures the relevant evidence, separates observation from
interpretation, and describes portable layout, visual, interaction, motion,
responsive, accessibility, and performance contracts. It supports faithful
reconstruction when reuse is authorized and reference-informed design when the
target must remain original.

## What It Can Deliver

- a dated source and capture registry
- a timestamped motion and interaction breakdown
- an evidence-backed structure and visual-system specification
- a responsive and input-mode contract with explicit unknown ranges
- an asset and implementation-mechanism register
- a portable-grammar versus source-specific-exclusion matrix
- acceptance checks that distinguish observed behavior from hypotheses

## Use It When

Use this skill when a live page, local HTML file, screenshot, screen recording,
video, prototype, or mixed reference pack must become a design or implementation
brief. It is especially useful when the reference is dynamic, long, edited,
partly inaccessible, or easy to imitate superficially without understanding its
states and behavior.

## Example Prompts

```text
Analyze this screen recording and produce a timestamped implementation
specification for its scroll sequence, transitions, responsive assumptions, and
reduced-motion fallback.

Compare these three reference sites. Extract the visual and interaction grammar
we can reuse without copying their brands, copy, assets, or complete layouts.

Turn this exported HTML and the rendered page into a component, state, motion,
and acceptance specification. Mark anything the source does not prove.

Capture this long lazy-loaded page reliably and document which evidence supports
each section of the implementation brief.
```

See [SKILL.md](SKILL.md) for the complete evidence, extraction, specification,
verification, and handoff workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill reference-analysis
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian reference-analysis
dalo approve skill sebastian:reference-analysis
dalo sync
```

## Related Skills

- [Product Design](../product-design/README.md) turns research and product
  evidence into a problem model, experience structure, and chosen direction;
  Reference Analysis supplies inspectable source evidence.
- [Effective Web](../effective-web/README.md) implements and verifies the
  accepted specification in the browser.
- [Originality Review](../originality-review/README.md) compares a produced
  result against its references for source overlap and provenance risk.
- [Product Marketing](../product-marketing/README.md) owns market position,
  campaign claims, audience, and proof rather than inferring them from a
  reference's visible execution.
- [Decision Records](../decision-records/README.md) preserves an accepted
  reference-derived direction when it becomes a durable project decision.

## Scope

The skill is not general internet research, competitor strategy, legal
clearance, product discovery, or frontend implementation. It does not treat
access to a reference as permission to reproduce its identity, content, code,
or assets.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
