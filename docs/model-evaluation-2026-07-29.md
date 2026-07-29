# Model Evaluation — 2026-07-29

This record checks natural skill activation and fresh with/without-skill behavior
after the current-model guidance review. It is a representative sample, not a
claim that every scenario has been executed on every model.

## Runtime and Method

- GPT runtime: Codex CLI 0.146.0, `gpt-5.6-sol`, provider-default sampling.
- Claude runtime: Claude Code 2.1.220, `claude-opus-5`, provider-default
  sampling through a Claude subscription.
- GPT activation: one fresh `--ephemeral`, read-only session per prompt. User
  config was ignored, while the installed skill catalog remained available for
  natural discovery. The structured response named only skills whose full
  instructions were actually invoked.
- Comparison: one fresh read-only baseline session instructed not to load
  skills and one fresh session pointed explicitly at the candidate worktree
  `SKILL.md`. Claude conditions additionally used `--safe-mode` and exposed
  only the read tool. Responses were manually checked against the scenario
  expectation.
- No repository changes or external actions were allowed inside evaluation
  sessions.

## GPT-5.6 Activation Sample

| Skill | Positive case | Result | Adjacent negative case | Correct destination | Result |
| --- | --- | --- | --- | --- | --- |
| `effective-workflow` | Mixed diagnosis-to-delivery work | Triggered with the three relevant specialist skills | Existing-check execution | `software-validation` | Pass |
| `effective-web` | Frontend accessibility fix | Triggered alone | Privacy-notice research | `web-legal-compliance` | Pass |
| `software-validation` | Run repository quality gates | Triggered alone | Design a new regression test | `software-testing` | Pass |
| `linkedin-posts` | Draft one LinkedIn post | Triggered alone | Redesign the LinkedIn acquisition system | `linkedin-social-selling` | Pass |

Result: **8/8 activation decisions passed**. Machine-readable reports were
generated beside the fixtures and passed `validate-scenario-review.py`; the
repository's `reports/` ignore rule keeps those runtime artifacts local, while
this review record preserves the durable result.

## GPT-5.6 With/Without Comparisons

### Port model tiering

Scenario: use a premium architect occasionally, a cheaper continuous builder,
and the cheapest model for routine quick review.

- Baseline: failed the expected behavior by assigning the cheapest model as a
  standard reviewer for every work unit.
- Initial candidate run: also retained a routine cheap-review loop. The model
  interpreted the Solo cold-review instruction as a separate reviewer role,
  exposing a real conflict between the profile and model-tiering guidance.
- Revised candidate: passed. It starts with one builder, deterministic evidence,
  and a cold self-review; rejects routine second-model review; and adds an
  independent reviewer only for a named semantic risk or measured benefit.
- Verdict: **with skill wins** after the evidence-driven revision in commit
  `8393ad3d`.

### PR finding before publication filtering

Scenario: report only blockers when the diff contains a billing-precision defect
and a harmless naming preference.

- Baseline: passed by reporting only the integer-cents billing defect.
- Candidate skill: passed with the same blocker and omitted the naming taste.
- Verdict: **tie** on this case. The skill response was shorter, but the sample
  does not establish a quality win over base-model behavior.

## Claude Opus 5 With/Without Comparisons

The repository is not packaged as a native Claude Code plugin, so this run does
not claim natural Claude skill activation. It tests response quality with the
candidate instructions explicitly loaded under the same fresh-session method
used for the GPT comparisons.

### Port model tiering

- Baseline: passed. It rejected cheap-model judgment review, kept the builder's
  cold pass as the routine review, and limited the cheapest tier to
  deterministic gates and mechanically verifiable plan-conformance checks.
- Candidate skill: passed. It rejected price as evidence of review value,
  assigned deterministic evidence to the cheapest tier, kept the builder's cold
  pass as the routine review, and triggered an independent specialist only for
  named semantic risks or measured benefit.
- Verdict: **tie**. The candidate reinforced the intended boundary but did not
  establish a material quality win over base Opus 5 on this case.

### PR finding before publication filtering

- Baseline: passed by requesting changes only for the floating-point invoice
  total and treating the helper name as non-blocking taste.
- Candidate skill: passed with the same blocker and publication threshold.
- Verdict: **tie**. The skill preserved the correct judgment but did not
  establish a material quality win over the base model on this case.

## Catalog Observation

Codex reported that the installed catalog exceeded its 2% skill-description
context budget and shortened descriptions while keeping every skill visible.
This runtime contains this repository plus separately installed marketing and
system skills, so the warning cannot be attributed to this repository alone.
The sampled activation decisions remained correct; description changes should
therefore be driven by broader activation evidence rather than a blind rewrite.

## Claude Opus 5 Independent Review

In addition, a separate high-effort Opus 5 session reviewed `main...HEAD`
read-only. It found no blocking issue and confirmed the branch's central
direction: find findings before applying a publication threshold, prefer
deterministic evidence over routine second-model verification, keep skill
bodies lean, and route detailed context through focused references.

It reported six pre-merge quality items:

1. stale reference counts caused by four newer `main` commits
2. ambiguous activation-report semantics and one questionable negative fixture
3. a documented-but-rejected nullable duration metric
4. residual per-batch wording that implied higher-capability review
5. one intentionally repeated model-tiering rule
6. a dangling route pointer after the Effective Web split

The branch integrated `main` and corrected items 1, 2, 3, 4, and 6. Item 5
remains deliberate: the initial GPT-5.6 candidate run failed without the
explicit top-level rule, so removing it would trade a measured behavior fix for
an abstract deduplication preference.
