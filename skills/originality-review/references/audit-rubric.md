# Audit Rubric

Load this reference before assigning severity or a release verdict.

## Compare Every Relevant Category

1. **Text** — headlines, body copy, labels, calls to action, captions, metadata,
   legal text, alt text, and hidden accessible wording.
2. **Identity** — names, wordmarks, logos, proprietary icons, people, company
   references, URLs, slogans, and distinctive verbal systems.
3. **Numbers and claims** — metrics, percentages, prices, dates, counts, plan
   structures, durations, and product-interface values.
4. **Images and visual assets** — exact files, derivatives, crops, screenshots,
   subjects, poses, objects, signature compositions, fonts, textures, and icons.
5. **Video and audio** — files, frames, shot order, timing, camera movement,
   transitions, overlays, posters, voice, music, and effects.
6. **Structure and interaction** — section order, unusual layout devices,
   journeys, data presentation, cursor behavior, shaders, gestures, and motion
   sequences.
7. **Code and implementation artifacts** — copied bundles, distinctive shader
   or algorithm code, comments, identifiers, embedded source assets, and license
   notices. Similar output alone does not prove copied code.
8. **History and provenance** — renamed, hidden, replaced, or deleted material;
   credits, source records, licenses, and generation or purchase evidence.

Include a category row even when it is out of scope or blocked.

## Distinguish the Evidence

- **Exact:** identical bytes, text, mark, frame, or code with a verified match.
- **Near-exact:** transformed but clearly traceable material such as a crop,
  recolor, light edit, normalized copy, or consecutive matching frames.
- **Distinctive overlap:** an unusual motif, composition, sequence, wording, or
  combination appears in both with meaningful correspondence.
- **Common grammar:** ordinary convention, functional pattern, broad genre, or
  independently likely design choice.
- **Inference:** plausible relationship without enough evidence to classify.
- **Blocked:** promised material or provenance cannot be inspected.

## Assign Severity

### Critical

Direct source identity, proprietary media, substantial copy, code, or an
unlicensed exact asset is present in released or release-bound work; or missing
evidence prevents review of a category the release explicitly depends on.

Default action: block release and replace, remove, document authorization, or
obtain specialist review.

### High

Near-exact or strongly distinctive overlap creates a credible source confusion
or copying risk even without an exact-file match.

Default action: materially rewrite or redesign before release.

### Medium

Several source-specific elements combine too closely, provenance is incomplete,
or a replaceable asset has uncertain rights.

Default action: correct before broad publication or obtain missing evidence.

### Low

Similarity is common grammar, incidental, or already supported by credible
independent provenance, but a small change or documentation improvement would
reduce doubt.

Default action: document or improve opportunistically; do not inflate it into a
release blocker.

## Write Findings That Can Be Reviewed

Use:

| Severity | Current evidence | Reference evidence | Observable overlap | Meaningful differences | Confidence | Correction |
| --- | --- | --- | --- | --- | --- | --- |

Describe observable facts before judgment. A correction must break the actual
overlap: rewriting copied content, replacing identity and media, changing the
distinctive composition or sequence, or documenting valid authorization.
Cosmetic recoloring does not resolve copied content, identity, or assets.

## Choose the Verdict

- `Clear in checked scope`: every in-scope category was inspectable and no
  meaningful red flag remains.
- `Clear with low-risk similarities`: only common or documented low-risk
  similarities remain.
- `Changes recommended`: medium or bounded high findings require correction.
- `Block release`: a critical or unresolved high finding affects release.
- `Blocked by missing evidence`: the promised review cannot support a verdict.

The verdict follows the most consequential supported finding and the defined
scope; it is not an average score.
