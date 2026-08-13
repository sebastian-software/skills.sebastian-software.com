# Provenance and History

Load this reference when exact assets, transformed media, license evidence,
deleted material, generated output, or repository history matter.

## Build the Asset Ledger

For each consequential asset record:

```text
Current path or public location:
Visible role:
Reference candidate:
Exact or transformed match evidence:
Creator or supplier:
Source URL or record:
License or authorization:
Acquisition or generation date:
Required attribution or restriction:
Unknowns and follow-up:
```

Do not infer ownership from possession, a filename, a public URL, an AI tool,
or the absence of a watermark.

## Use Deterministic Leads Carefully

- Cryptographic hashes prove identical bytes, not legal permission or visible
  importance.
- Normalized text comparison can reveal casing, whitespace, punctuation, or
  markup changes; inspect the surrounding meaning before escalating.
- Image dimensions, metadata, and perceptual matching can locate crops or
  derivatives. Re-encoding and generation make automated distance uncertain.
- Frame extraction and matched timestamps can reveal reused video segments,
  shot order, posters, or motion sequences; distinguish page motion from edited
  camera motion.
- Font names, bundle strings, source maps, comments, and embedded URLs are
  investigation leads, not verdicts by themselves.

Keep tool output reproducible and cite the exact artifact it inspected. Do not
write an automatic “plagiarism percentage.”

## Inspect Repository History

When authorized local history is available, use narrow read-only queries:

```bash
git log --all --name-status -- <path>
git log -S'<distinctive text>' --all --oneline
git log -G'<relevant pattern>' --all --oneline
git show <commit>:<path>
```

Search renamed, deleted, and replaced files when the release history is in
scope. Do not rewrite or purge history during an audit. History removal is a
separate destructive action with collaboration, legal, and operational
consequences.

Distinguish:

- material that exists in the current published artifact;
- material present only in an unreleased branch;
- material removed from current output but retained in history;
- third-party assets legitimately retained with complete provenance.

## Review Licenses and Credits

- Read the actual license, purchase record, attribution requirement, and scope;
  do not rely on a platform's generic marketing summary.
- Check whether redistribution, modification, commercial use, model training,
  sublicensing, or embedding is relevant to the actual use.
- Preserve existing notices while their requirement is unresolved.
- Treat missing records as unknown. Recommend the smallest evidence request:
  invoice, download record, license text, creator permission, generation log, or
  replacement asset.
- Escalate interpretation of disputed ownership, substantial similarity,
  license compatibility, or infringement to qualified counsel.

## Report Provenance Separately From Originality

A work can be visually original while containing an unlicensed asset. It can
also resemble a reference while every asset is independently licensed.
Maintain separate findings for:

1. similarity or copying risk;
2. asset authorization and attribution;
3. source-history exposure;
4. legal interpretation still required.
