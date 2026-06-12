# Source Review Workflow

Use Things as the operational queue and this repository as the durable record of
what actually changed in the skills.

The current rule is: **process one canonical Things link at a time and update
the relevant skill or decision log directly**. Do not create new source cards or
cluster briefs for routine intake work.

## Current Workflow

1. Open the Things link and verify what is behind it.
2. Read the existing target skill/reference before deciding.
3. Choose one outcome:
   - `Candidate`: update or create the relevant skill/reference.
   - `Deferred`: record only a compact decision if the source may matter later.
   - `Rejected`: record only a compact decision when auditability is useful.
4. Commit the source-specific change.
5. Mark the Things item reviewed and complete only after the commit exists.

Prefer one commit per canonical Things link. Exact duplicate Things items should
be handled in the canonical source commit rather than receiving empty commits.

## Commit Metadata

Every source-processing commit should include:

```text
Things-ID: <id or comma-separated ids>
Source: <url>
Decision: primary|secondary|ignored|deferred|rejected
Target: <skill/reference or decision log>
URL-Recheck: <date and result>
```

## Decision Bar

Interesting is not enough. A source should affect a skill only when it improves
a repeatable agent workflow, rule, checklist, caveat, or implementation
decision.

Prefer:

- official documentation and standards-facing references,
- durable explanatory articles,
- high-quality implementation guides,
- sources that explain tradeoffs, failure modes, or decision criteria.

Treat package-shopping links, GitHub repositories, product homepages, release
announcements, stale news, and social posts conservatively. Route them to
`processed-decisions.md` as deferred or rejected unless they contain durable
workflow guidance.

## Things Tags

When applying the final Things decision:

- add `Skill Archive Reviewed`,
- remove `Skill Archive Intake`,
- add exactly one final tag: `Skill Archive Candidate`,
  `Skill Archive Deferred`, or `Skill Archive Rejected`,
- keep broad category tags such as `Skill: Frontend UI` for auditability,
- complete the Things item after the matching commit exists.

## Files

- `processed-decisions.md` -- compact log for handled links that should not
  become skill/reference content.
- `archive/2026-06-things-import/` -- preserved historical intake, queue,
  cluster, second-pass, and candidate-map artifacts from the June 2026 import.
- `things-actions.md` and `scripts/apply_things_actions.py` -- optional helper
  format and script for bulk-retagging Things after reviewed decisions exist.
