# Reviewing Skill Behavior

`skills/<name>/evals/evals.json` contains manual review scenarios. They are
useful prompts and expectations for consequential behavior, but neither local
checks nor CI runs a model, grades a response, or establishes behavioral
correctness from them. CI validates only their static JSON shape, non-empty
fields, and unique names through `python3 scripts/validate-readmes.py`.

Use the smallest review mode that answers the current question:

- **Activation:** Does the host load the skill for the right requests and avoid
  adjacent requests?
- **Single run:** Does a response satisfy the scenario criteria?
- **With/without comparison:** Does the skill improve quality enough to justify
  its context, latency, and token cost?

All modes record human-reviewed evidence without claiming automatic semantic
grading.

## Review Activation

Add should-trigger and should-not-trigger cases to the skill's `activation`
array, then generate a report template:

```sh
python3 scripts/validate-scenario-review.py \
  --skill effective-workflow \
  --activation-template \
  > /tmp/effective-workflow-activation.json
```

Run every case in a fresh session with the normal installed skill set. Do not
mention the skill explicitly unless explicit invocation itself is the behavior
under test. Record whether the host exposed or invoked the skill and the trace,
log, or other evidence supporting that observation.

Validate the completed report:

```sh
python3 scripts/validate-scenario-review.py \
  --skill effective-workflow \
  --report /tmp/effective-workflow-activation.json
```

The validator checks that the recorded pass/fail result agrees with the
fixture's expected activation and the observed boolean. It does not establish
that the host trace was interpreted correctly.

## Compare With and Without the Skill

Generate a comparison template:

```sh
python3 scripts/validate-scenario-review.py \
  --skill effective-web \
  --comparison-template \
  > /tmp/effective-web-comparison.json
```

For every selected scenario:

1. Start a fresh session with the skill available.
2. Start another fresh session with only that skill disabled.
3. Keep the model, sampling settings, prompt, repository state, tools, and other
   installed skills the same.
4. Grade each response independently against `expected`.
5. Record duration and input/output tokens when the host exposes them; use
   `null` for unavailable token counts.
6. Choose `with_skill`, `without_skill`, or `tie`, then explain the evidence for
   that comparison.

Validate the completed comparison with the same `--report` command. Compare
pass rate first, then evidence quality, material omissions, duration, and token
cost. A shorter or cheaper result is an improvement only when it still passes
the scenario.

## Review One Run

Generate a single-run template for the affected skill:

```sh
python3 scripts/validate-scenario-review.py --skill effective-web --template \
  > /tmp/effective-web-review.json
```

Select the scenarios that exercise consequential behavior. Keep the relevant
skill loaded, provide each stored prompt unchanged, and record the actual
response. Fill in the agent, model/version, and sampling/runtime settings that
materially affect the result.

Compare each response with that scenario's `expected` criteria. Record `pass`
only when the response addresses the relevant judgment; record `fail` when it
misses a required decision, evidence source, safety boundary, or tradeoff. The
`grading_evidence` field must explain that result in concrete terms.

Reports contain only:

```json
{
  "skill": "effective-web",
  "runtime": {
    "agent": "Codex desktop",
    "model": "gpt-5.6",
    "sampling": "temperature 0"
  },
  "results": [
    {
      "name": "rsc-boundary",
      "response": "Recorded agent response.",
      "result": "pass",
      "grading_evidence": "Concrete comparison with the scenario's expected criteria."
    }
  ]
}
```

Attach the report to the PR or its review record when it informs a merge
decision. Do not commit arbitrary model output or private prompts to the source
tree unless the repository explicitly asks for a durable benchmark artifact.

## Validate a Single-Run Record

The validator confirms that every recorded case belongs to the selected skill,
fields are complete, results are explicitly `pass` or `fail`, and no case is
duplicated. It does not semantically grade the recorded response.

```sh
python3 scripts/validate-scenario-review.py \
  --skill effective-web \
  --report /tmp/effective-web-review.json
```

For a negative-control review, require the record to show at least one failed
scenario:

```sh
python3 scripts/validate-scenario-review.py \
  --skill effective-web \
  --report docs/scenario-review-report.example.json \
  --require-failure
```

The committed example is intentionally bad: its `rsc-boundary` response moves
all rendering and data access to the client, so its recorded result is `fail`
with the missing server/client boundary evidence named explicitly. This proves
that the report workflow can capture a failed scenario without pretending to be
an automatic behavioral grader.

## What This Does Not Claim

This workflow creates transparent manual quality records. It does not make
reports comparable across models, replace a provider-backed evaluation harness,
or turn a schema-valid report into proof that an agent will behave correctly in
production. Comparisons are meaningful only when their recorded conditions are
actually held constant.

If the collection later adds a reproducible provider-backed runner, it must
define the provider, model/version, sampling, rubric or grader, artifacts,
baseline, cost and flake policy, and its CI or scheduled execution boundary.
