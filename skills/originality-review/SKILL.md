---
name: originality-review
description: >-
  Audit a website, interface, campaign, document, media artifact, or
  code-backed experience against supplied references for originality risk,
  source overlap, and asset provenance. Use when asked whether work copies its
  inspiration; to compare text, brands, numbers, images, video, layout, motion,
  code, fonts, icons, or other assets; inspect current and historical files;
  check credits or licenses; recommend replacements; or make a release verdict.
  Produces evidence-backed risk findings, not a legal conclusion.
---

# Originality Review

Compare the delivered work with the complete supplied reference corpus. Treat
the audit as an evidence exercise: exact overlap, distinctive combination,
common grammar, and missing provenance are different findings.

## Workflow

1. Lock the audit boundary:
   - audit only, or audit plus authorized fixes;
   - current output, history, or both;
   - references and categories promised by the brief;
   - release decision and risk tolerance owner.
2. Build a source registry. Record every supplied reference, role, path or URL,
   date or version when known, ownership or license evidence supplied by the
   user, and which categories it can prove. Prefer contemporaneous local
   evidence when a live source may have changed.
3. Inventory the current work:
   - rendered and hidden text, metadata, labels, names, claims, and numbers;
   - images, video, audio, fonts, icons, textures, screenshots, and downloads;
   - layout order, distinctive compositions, interaction, motion, and timing;
   - source files, built output, asset records, credits, and relevant history.
4. Read [Audit rubric](references/audit-rubric.md). Compare category by category
   rather than using one overall visual impression.
5. Read [Provenance and history](references/provenance-and-history.md) when
   exact files, transformed media, licenses, deleted material, or repository
   history are in scope.
6. Triangulate every finding:
   - identify the current artifact and exact location;
   - identify the reference artifact and exact location;
   - describe the observable overlap and meaningful differences;
   - state whether evidence is exact, strongly distinctive, common, inferred,
     or blocked;
   - assign severity and the smallest credible correction.
7. Review combinations. Ordinary patterns can become distinctive when unusual
   copy, media, order, motif, and motion are reproduced together. Do not
   escalate a generic dark theme, card grid, fade-in, or pricing table alone.
8. Return a scoped verdict, ordered findings, category passes, provenance and
   history results, missing evidence, and prioritized fixes. Never turn an
   unchecked category into a pass.

## Operating Rules

- Use “originality risk,” “source overlap,” or “red flag.” Do not declare
  plagiarism, infringement, fair use, or legal safety from similarity alone.
- Pair every consequential finding with both current-work and reference
  evidence. A source filename or visual vibe is not sufficient proof.
- Separate copied identity or content from shared conventions, necessary
  functional behavior, independently sourced assets, and documented licensed
  reuse.
- Inspect the visible bytes and behavior, not only filenames. A renamed,
  recolored, cropped, regenerated, hidden, or deleted artifact can remain
  relevant to current publication or release history.
- Treat hashes, text similarity, image matching, and automated inventories as
  leads. Human review decides whether the matched material is meaningful in
  context.
- Do not clear a complete experience after checking only its homepage, hero,
  cover frame, source code, or current working tree.
- Do not remove history, rewrite credits, replace assets, or alter published
  work unless the user separately authorizes those changes.

## Verdicts

Use one:

- `Clear in checked scope`
- `Clear with low-risk similarities`
- `Changes recommended`
- `Block release`
- `Blocked by missing evidence`

State the checked scope directly beside the verdict. “Clear” never means legal
clearance or categories that were unavailable.

## Default Deliverable

1. Verdict and checked scope
2. Source registry and access gaps
3. Findings ordered by severity
4. Category pass and unknown matrix
5. Provenance, license, and history findings
6. Prioritized replacement or redesign plan
7. Areas requiring qualified legal, licensing, or brand review

## Routing Boundaries

- Use `reference-analysis` to extract layout, motion, interaction, and visual
  grammar into a specification before implementation. This skill compares a
  produced work against its sources.
- Route product direction, visual exploration, and prototype choices to
  `product-design`; return here only for the evidence-backed comparison.
- Route browser implementation of accepted fixes to `effective-web` and market
  claims or campaign corrections to `product-marketing`.
- Route product and company name generation or preliminary trademark screening
  to `product-naming`; similarity of names and marks may require qualified
  trademark counsel.
- `web-legal-compliance` does not provide copyright, plagiarism, trademark, or
  license clearance. Keep legal conclusions and specialist clearance outside
  this skill.
- Use `decision-records` only for durable project rules about reference use,
  provenance, or release thresholds—not for storing an audit's temporary status.
