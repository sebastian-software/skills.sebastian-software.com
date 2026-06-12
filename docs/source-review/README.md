# Source Review Workflow

Use this folder as the buffer between Things links and skill changes.

The rule is: **no skill changes from a URL alone**. A source must first become a
reviewed source card or cluster brief. Only then should it update an existing
skill or justify a new one.

## Lifecycle

1. **Intake**
   - Link was found in Things and looks potentially relevant.
   - Things tags: `Skill Archive`, `Skill Archive Intake`, plus one broad
     category tag such as `Skill: Frontend UI`.
   - No claim has been made about quality yet.

2. **Source Card**
   - The link has been opened and read enough to understand what it actually
     contains.
   - Capture stable facts: title, URL, author/source, date if available, topic,
     summary, durable ideas, implementation details, caveats, and archive
     decision.
   - Things tags: add `Skill Archive Reviewed`.

3. **Cluster Brief**
   - Several source cards point to the same repeatable workflow or knowledge
     area.
   - Capture whether the cluster should become a new skill, a reference update,
     a vendor review, or a discard pile.

4. **Skill Proposal**
   - Define the skill boundary before editing:
     trigger phrases, expected tasks, reference files, scripts/assets if any,
     eval prompts, and sources to cite in `SOURCE.md` or reference notes.

5. **Skill Change**
   - Update or create the skill only after the proposal is coherent.
   - Keep source-derived content paraphrased and attributed.
   - Add evals when the skill has behavior that can be tested.

## Things Completion Policy

Things remains the operational queue. Once a link has been fully handled for the
archive, mark the Things task complete so the queue shrinks. The completed item
remains available in Things' Logbook.

Complete a Things task only after one of these final outcomes is recorded in a
source card or cluster brief:

- **Candidate** -- source should inform a skill/reference and has been captured
  in a cluster brief.
- **Deferred** -- source is potentially useful, but not for the current archive
  pass; reason is documented.
- **Rejected** -- source is irrelevant, private/personal, stale news, duplicate,
  unreachable, or too weak for archive use; reason is documented.

Do not complete an `Intake` item merely because it was tagged or exported. The
minimum bar is: link opened or intentionally skipped for a documented reason,
decision recorded, Things retagged, then completed.

## Things Tags

| Tag | Meaning |
| --- | --- |
| `Skill Archive` | Source is part of the archive process. |
| `Skill Archive Intake` | Source is queued but not reviewed. |
| `Skill Archive Reviewed` | Source was opened/read and captured in a source card or review note. |
| `Skill Archive Candidate` | Source should inform a skill/reference. |
| `Skill Archive Deferred` | Source may be useful later, but not for the current pass. |
| `Skill Archive Rejected` | Source was intentionally discarded for archive purposes. |

When applying a final decision in Things, remove `Skill Archive Intake` where
possible and add exactly one final decision tag: `Candidate`, `Deferred`, or
`Rejected`. Keep broad category tags for auditability.

## Review Standard

For each source, answer:

1. What is behind the link?
2. Is it durable enough for a skill, or is it news/tool churn?
3. What specific workflow or decision would improve if an agent had this
   source?
4. Does it belong in an existing skill, a new skill, a vendor review, or a
   discard/defer list?
5. What caveats, version/date limits, or source-quality concerns matter?

## Relevance Bar

Interesting is not enough. A source should become a `Candidate` only when it is
both relevant to a plausible skill/reference and useful for a repeatable agent
workflow.

Prefer:

- explanatory articles with durable concepts,
- official documentation,
- standards/specification references,
- high-quality implementation guides,
- source material that explains tradeoffs, failure modes, or workflow decisions.

Treat GitHub projects and package links conservatively. Most package-shopping
links should be `Rejected` or `Deferred`, especially if the note is only "try
this library", "maybe add this plugin", or old project-specific boilerplate.
GitHub projects are generally **not skill sources**. They can still be
interesting, but route them to the GitHub project matrix instead of promoting
them into skill candidates. Use `Deferred` with a reason such as "captured in
GitHub project matrix" when the repo is potentially interesting but not source
material for a skill. Use `Rejected` for dead, irrelevant, personal, archived,
or weak package-shopping links.

Exceptions are rare and should be justified explicitly: a GitHub URL may be
skill-relevant when it points to an actual skill repository under vendor review,
a formal specification/reference repository, or a PR/discussion that functions
as an explanatory article about a durable architecture/migration pattern.

When in doubt, downgrade from `Candidate` to `Deferred` and explain what
additional sources would be needed before changing a skill.

## GitHub Project Matrix

GitHub projects that are generally interesting should be tracked separately
from skill source review. The matrix captures metadata such as description,
stars, last push/commit, latest release, archived status, license, language,
topics, and the Things items that referenced the repo.

The matrix is an inventory, not a recommendation to add the project to a skill.

## Output Files

- `source-card-template.md` -- copy structure for individual reviewed sources.
- `things-intake-2026-06-10.md` -- current Things intake snapshot and category
  counts.
- `candidate-source-map.csv` -- final candidate source inventory with proposed
  topic, skill/reference area, source role, quality, and second-pass status.
- `skill-taxonomy.md` -- proposed skill/reference architecture for turning
  candidate sources into coherent skill updates.
- `cluster-brief-template.md` -- structure for turning source cards into a
  skill/reference proposal.
- `clusters/` -- reviewed cluster briefs plus Things action tables.
- `github-projects/github-project-matrix.csv` -- GitHub project inventory with
  repository metadata and back-references to Things items.
