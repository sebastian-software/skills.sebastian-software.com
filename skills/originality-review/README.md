[← Sebastian Software Skills](../../README.md)

# Originality Review

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Compare a produced experience with its references using paired evidence,
provenance, and history—not a vague similarity score.**

Originality Review audits websites, interfaces, campaigns, documents, media,
and code-backed experiences for exact reuse, distinctive combinations, common
visual grammar, uncertain asset rights, and historical exposure. It produces a
scoped release verdict while keeping legal conclusions with qualified counsel.

## What It Can Deliver

- a complete source and current-work registry
- category-by-category text, identity, media, structure, motion, code, and
  history comparison
- paired current/reference evidence for every consequential finding
- an asset provenance, license, and attribution ledger
- a severity-ordered originality-risk report
- a prioritized replacement or redesign plan
- a scoped `clear`, `changes recommended`, `block`, or `blocked` verdict

## Use It When

Use this skill before releasing work derived from references, when a customer
or reviewer suspects copying, when assets have unclear origins, or when renamed,
cropped, regenerated, deleted, or historical material must be checked. It
distinguishes ordinary genre conventions from exact or distinctively combined
source material.

## Example Prompts

```text
Audit this website against the supplied reference pack. Check copy, brand names,
numbers, images, video, layout, motion, assets, and Git history.

These two interfaces feel similar. Pair exact evidence from both sides, separate
common patterns from distinctive overlap, and recommend the smallest credible
fixes.

Build a provenance ledger for every published image, font, icon, video, and
download. Mark missing licenses and attribution requirements as unknown.

Review the current release and historical commits, but do not modify files or
declare legal infringement.
```

See [SKILL.md](SKILL.md) for the complete audit, evidence, severity, verdict, and
handoff workflow.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill originality-review
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian originality-review
dalo approve skill sebastian:originality-review
dalo sync
```

## Related Skills

- [Reference Analysis](../reference-analysis/README.md) turns source material
  into a traceable specification before implementation.
- [Product Design](../product-design/README.md) owns the experience direction
  and visual exploration that an originality audit may later review.
- [Effective Web](../effective-web/README.md) implements and verifies accepted
  browser-facing fixes.
- [Product Marketing](../product-marketing/README.md) corrects market claims,
  campaign language, proof, and positioning exposed by the audit.
- [Product Naming](../product-naming/README.md) owns name generation and
  preliminary trademark screening; qualified counsel owns clearance.
- [Web Legal Compliance](../web-legal-compliance/README.md) covers web
  disclosures and consent requirements, not copyright or license clearance.

## Scope

The skill reports evidence-backed originality and provenance risk. It does not
declare plagiarism, copyright or trademark infringement, fair use, license
compatibility, or legal safety. It does not rewrite history, remove published
assets, or implement fixes without separate authorization.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
