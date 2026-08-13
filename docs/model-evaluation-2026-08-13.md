# Model Evaluation — 2026-08-13

This record repeats the six-discipline activation review on a GPT runtime. It
uses the stronger installed-catalog method requested by issue #215: each prompt
ran in a fresh Codex session, and a skill counted as invoked only when the JSONL
trace showed its full `SKILL.md` being read.

## Runtime and Method

- Runtime: Codex CLI 0.147.0, `gpt-5.6-sol`, provider-default sampling.
- Base revision: `b6a53285f50038500736aa47fecc8a6eb4ad3b89` (`main`).
- Prompt set: the 49 `prompt` values in
  [`activation-matrix.json`](activation-matrix.json), unchanged and in the
  seeded order produced by `scripts/build-routing-review-input.py`.
  The matrix SHA-256 was
  `f56e78d537d9eb18cb76617145026b62c01207ecb9c8cdc1a2acfc3778bdb222`;
  the answer-key SHA-256 was
  `eadeb4c2752292ab7f9acae1abc958de35571f1e80b871765965269b194253d4`.
- Catalog: the six current disciplines and all 33 deprecation stubs were
  symlinked from that revision into an isolated `.agents/skills` directory.
  Normal user skills were disabled by exact path; apps and plugins were
  disabled. Five bundled Codex system skills remained visible.
- Isolation: one fresh `--ephemeral`, `--ignore-user-config`,
  `--ignore-rules`, read-only session per prompt, with approvals disabled. The
  prompt was passed exactly as stored; it did not name a candidate skill or
  expose the answer key.
- Telemetry: raw JSONL and stderr were retained below the repository-ignored
  `reports/issue-215/` directory for the PR review. Started/completed command
  events were deduplicated. The first current discipline whose full
  instructions were read is the pick; later discipline reads are recorded as
  co-activation. A stub followed by its named successor is a successful
  deprecation handoff, not a competing old owner.
- Safety: sessions could read the isolated public catalog but could not write.
  Some tried repository or GitHub discovery because the fixture intentionally
  supplied no project artifact; those attempts failed in the read-only,
  network-restricted environment and did not affect activation grading.

The original stub-inclusive blind input was 34,766 bytes over 180 lines, with
SHA-256
`68083fde2d27152d4095a616392d3d69a6a513657ae79ebdbc23a592805bce83`.
It is a reproducible catalog snapshot; installed-catalog sessions received its
skill metadata naturally and one unchanged matrix prompt at a time rather than
receiving the whole classifier document.

## Results

Round 1 passed 47 of 49 cases. Both misses were clarification-only turns where
the request referred to missing source material:

1. `humanize-team-update` immediately asked for the absent German status note
   without reading any skill.
2. `draft-article-from-notes` immediately asked for the absent workshop notes
   without reading any skill.

Effective Writing's description already covered both artifacts, but the
runtime exposed only the first 448 characters. A narrow change moved the rule
that missing source text is still an activation into that visible prefix.
Round 2 then activated `effective-writing` for `draft-article-from-notes`, but
`humanize-team-update` still clarified without reading a skill. A third round
put its Slack/team-message terms into the visible prefix; Codex explicitly said
it would use the Metro English and German typography rules, yet still read no
`SKILL.md`. That experimental reorder was reverted because it did not change
activation.

Final result: **48/49 (98.0%)**. The retained source change is the one supported
by the successful article rerun: missing source text or notes did not prevent
Effective Writing activation in that repeated case. The remaining mismatch is
recorded rather than papered over. Its trace is consistent with a host shortcut
for a trivial clarifying question: catalog wording made the correct capability
legible, but the runtime answered before invoking instructions. No further
source copy change has evidence that it can deterministically override that
behavior.

An initial automated parse reported 43/49 because its path expression did not
recognize relative `.agents/skills/.../SKILL.md` reads followed by newlines or
semicolons. Manual trace review found the four missing discipline reads and the
parser was corrected before any routing conclusion was drawn. That was a
telemetry-parser defect, not four model mismatches.

## Final Picks and Invocation Evidence

| # | Case | Expected | Full instructions invoked | Pick | Result |
| ---: | --- | --- | --- | --- | --- |
| 1 | `audit-page-against-references` | `effective-web` | `originality-review` → `effective-web` | `effective-web` | Pass |
| 2 | `run-established-checks` | `effective-delivery` | `software-validation` → `effective-delivery` | `effective-delivery` | Pass |
| 3 | `operate-unspecified-issue-queue` | `effective-delivery` | `issue-autopilot` → `effective-delivery` → `effective-writing` | `effective-delivery` | Pass |
| 4 | `audit-formulaic-prose` | `effective-writing` | `effective-writing` | `effective-writing` | Pass |
| 5 | `control-scheduling` | `none` | none | `none` | Pass |
| 6 | `replace-gamed-seat-pricing` | `effective-product` | `pricing-and-packaging` → `effective-product` | `effective-product` | Pass |
| 7 | `model-onboarding-experience` | `effective-product` | `product-design` → `effective-product` | `effective-product` | Pass |
| 8 | `scope-marketing-endorsement-disclosures` | `effective-web` | `web-legal-compliance` → `effective-web` | `effective-web` | Pass |
| 9 | `choose-strategic-control-boundary` | `effective-engineering` | `software-architecture` → `effective-engineering` | `effective-engineering` | Pass |
| 10 | `write-homepage-hero` | `effective-marketing` | `marketing-writing` → `locale-typography` → `effective-marketing` → `effective-writing` | `effective-marketing` | Pass |
| 11 | `correct-german-typography` | `effective-writing` | `locale-typography` → `effective-writing` | `effective-writing` | Pass |
| 12 | `fix-conflicting-status-writes` | `effective-engineering` | `data-systems` → `decision-records` → `effective-engineering` → `effective-product` | `effective-engineering` | Pass |
| 13 | `prioritize-release-scope` | `effective-product` | `product-management` → `effective-product` | `effective-product` | Pass |
| 14 | `boundary-research-versus-messaging` | `effective-product` | `market-research` → `effective-product` | `effective-product` | Pass |
| 15 | `humanize-team-update` | `effective-writing` | none | `none` | **Mismatch** |
| 16 | `select-generated-design-direction` | `effective-product` | `product-design` → `effective-product` | `effective-product` | Pass |
| 17 | `diagnose-checkout-dropoff` | `effective-marketing` | `conversion-optimization` → `effective-marketing` | `effective-marketing` | Pass |
| 18 | `write-migration-notes` | `effective-delivery` | `tech-docs` → `effective-delivery` | `effective-delivery` | Pass |
| 19 | `boundary-editorial-versus-commercial-prose` | `effective-writing` | `nonfiction-writing` → `effective-writing` | `effective-writing` | Pass |
| 20 | `select-distribution-motion` | `effective-marketing` | `product-marketing` → `effective-marketing` | `effective-marketing` | Pass |
| 21 | `adapt-writeup-for-social` | `effective-marketing` | `create-social-content` → `locale-typography` → `effective-marketing` → `effective-writing` | `effective-marketing` | Pass |
| 22 | `control-spreadsheet-task` | `none` | none | `none` | Pass |
| 23 | `name-a-feature-bilingually` | `effective-product` | `product-naming` → `effective-product` | `effective-product` | Pass |
| 24 | `rank-repository-improvements` | `effective-delivery` | `codebase-improvement` → `effective-delivery` | `effective-delivery` | Pass |
| 25 | `design-churn-interview-program` | `effective-product` | `market-research` → `effective-product` | `effective-product` | Pass |
| 26 | `review-rust-public-api` | `effective-engineering` | `rust-engineering` → `effective-engineering` | `effective-engineering` | Pass |
| 27 | `coordinate-ai-generated-production-code` | `effective-delivery` | `effective-workflow` → `effective-delivery` | `effective-delivery` | Pass |
| 28 | `build-linkedin-pipeline` | `effective-marketing` | `linkedin-social-selling` → `effective-marketing` | `effective-marketing` | Pass |
| 29 | `diagnose-repeated-agent-divergence` | `effective-delivery` | `codebase-improvement` → `effective-delivery` | `effective-delivery` | Pass |
| 30 | `port-library-preserving-behavior` | `effective-delivery` | `port-codebases` → `rust-engineering` → `effective-delivery` → `effective-engineering` | `effective-delivery` | Pass |
| 31 | `scope-jurisdiction-disclosures` | `effective-web` | `web-legal-compliance` → `effective-web` | `effective-web` | Pass |
| 32 | `diagnose-deploy-ownership` | `effective-delivery` | `engineering-management` → `effective-delivery` | `effective-delivery` | Pass |
| 33 | `boundary-pr-review-versus-api-review` | `effective-delivery` | `pr-review` → `effective-delivery` | `effective-delivery` | Pass |
| 34 | `control-general-knowledge` | `none` | none | `none` | Pass |
| 35 | `specify-reference-motion` | `effective-web` | `reference-analysis` → `effective-web` | `effective-web` | Pass |
| 36 | `record-durable-decision` | `effective-product` | `decision-records` → `pricing-and-packaging` → `effective-product` | `effective-product` | Pass |
| 37 | `fix-dashboard-accessibility` | `effective-web` | `effective-web` | `effective-web` | Pass |
| 38 | `write-single-linkedin-post` | `effective-marketing` | `linkedin-posts` → `effective-marketing` | `effective-marketing` | Pass |
| 39 | `record-intuition-without-promoting-it` | `effective-product` | `decision-records` → `effective-product` | `effective-product` | Pass |
| 40 | `draft-article-from-notes` | `effective-writing` | `effective-writing` | `effective-writing` | Pass |
| 41 | `choose-segment-and-position` | `effective-marketing` | `product-marketing` → `effective-marketing` | `effective-marketing` | Pass |
| 42 | `prepare-dependency-portfolio` | `effective-delivery` | `smart-dependency-updater` → `effective-delivery` | `effective-delivery` | Pass |
| 43 | `boundary-test-design-versus-check-execution` | `effective-engineering` | `software-testing` → `effective-engineering` | `effective-engineering` | Pass |
| 44 | `write-discriminating-regression-test` | `effective-engineering` | `software-testing` → `effective-engineering` | `effective-engineering` | Pass |
| 45 | `replace-unsound-type-cast` | `effective-engineering` | `typescript-engineering` → `effective-engineering` | `effective-engineering` | Pass |
| 46 | `coordinate-vague-bug-report` | `effective-delivery` | `effective-workflow` → `effective-delivery` | `effective-delivery` | Pass |
| 47 | `work-the-review-queue` | `effective-delivery` | `pr-review` → `effective-delivery` | `effective-delivery` | Pass |
| 48 | `decide-service-boundary` | `effective-engineering` | `software-architecture` → `effective-engineering` | `effective-engineering` | Pass |
| 49 | `audit-consultant-profile` | `effective-marketing` | `consultant-profile` → `effective-marketing` | `effective-marketing` | Pass |

## Catalog and Context-Budget Observation

Before the measured fix, the six discipline descriptions occupied 5,751 UTF-8
bytes; the 39-entry transition catalog occupied 26,761 bytes. The retained
Effective Writing change makes those totals 5,801 and 26,811 bytes.

Every one of the 49 sessions emitted Codex's warning that descriptions had
been shortened to fit the skills context budget. A local
`codex debug prompt-input` inspection against the final isolated catalog showed
all 39 entries still present, but only 17,337 description characters visible:
406–448 characters per entry. Effective Writing exposed 448 of its 1,020 folded
characters. The warning and the measured truncation support ADR 0004's existing
conclusion: during the deprecation window the old descriptions preserve legacy
triggers, but they also materially reduce the successor descriptions available
to selection.

## Reproduction

Generate the exact classifier view and answer key:

```sh
python3 scripts/build-routing-review-input.py --include-deprecated \
  > /tmp/routing-review.md
python3 scripts/build-routing-review-input.py --key \
  > /tmp/routing-key.json
shasum -a 256 docs/activation-matrix.json /tmp/routing-review.md \
  /tmp/routing-key.json
```

For installed-catalog activation, create a temporary directory containing
`.agents/skills/<slug>` symlinks to every current `skills/<slug>` directory.
Run one unchanged matrix prompt per process from that directory:

```sh
codex --ask-for-approval never exec \
  --ephemeral \
  --ignore-user-config \
  --ignore-rules \
  --disable plugins \
  --disable apps \
  --sandbox read-only \
  --model gpt-5.6-sol \
  --json \
  --skip-git-repo-check \
  -c 'skills.config=[{path="<normal-user-skill>/SKILL.md",enabled=false}]' \
  '<one unchanged prompt from docs/activation-matrix.json>' \
  > '<seeded-position>-<case-name>.jsonl
```

Expand `skills.config` to one exact-path exclusion for every normal user skill;
do not disable the temporary worktree-linked copies. Inspect each JSONL command
event for full `SKILL.md` reads, deduplicate started/completed events, and keep
the answer key outside the model session.

## Limitations

- This is one run per prompt on one GPT model and one Codex CLI version. It does
  not establish stability across sampling, versions, providers, or hosts.
- The installed catalog isolates this repository's transition state rather
  than reproducing a user's unrelated third-party skills. Five bundled system
  skills remained visible, so it is not literally a 39-entry global catalog.
- The runtime's description truncation is observed behavior, not a documented
  guarantee that the same character allocation will hold elsewhere.
- Invocation proves that instructions were loaded, not that the resulting task
  response was semantically correct. Many fixtures intentionally lack the
  source artifact needed to complete the requested work.
- The remaining clarification-only miss means this run does not establish
  perfect production activation. Revisit it with host-level selection telemetry
  or a fixture that includes the referenced status note before changing more
  description copy.
