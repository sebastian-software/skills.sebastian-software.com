# Model Evaluation — 2026-07-29

This record checks natural skill activation and fresh with/without-skill behavior
after the current-model guidance review. It is a representative sample, not a
claim that every scenario has been executed on every model.

## Runtime and Method

- GPT runtime: Codex CLI 0.146.0, `gpt-5.6-sol`, provider-default sampling.
- Activation: one fresh `--ephemeral`, read-only session per prompt. User config
  was ignored, while the installed skill catalog remained available for natural
  discovery. The structured response named only skills whose full instructions
  were actually invoked.
- Comparison: one fresh read-only baseline session instructed not to load skills
  and one fresh session pointed explicitly at the candidate worktree
  `SKILL.md`. Responses were manually checked against the scenario expectation.
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

## Catalog Observation

Codex reported that the installed catalog exceeded its 2% skill-description
context budget and shortened descriptions while keeping every skill visible.
This runtime contains this repository plus separately installed marketing and
system skills, so the warning cannot be attributed to this repository alone.
The sampled activation decisions remained correct; description changes should
therefore be driven by broader activation evidence rather than a blind rewrite.

## Claude Opus 5 Status

The local Claude Code 2.1.207 installation is present, but `claude auth status`
reports no authenticated account or API key. No Opus result is recorded until
the runtime can execute real fresh sessions.
