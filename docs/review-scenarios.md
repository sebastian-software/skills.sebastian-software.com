# Reviewing Unrun Scenarios

`skills/<name>/evals/evals.json` contains manual review scenarios. They are
useful prompts and expectations for consequential behavior, but neither local
checks nor CI runs a model, grades a response, or establishes behavioral
correctness from them. CI validates only their static JSON shape, non-empty
fields, and unique names through `python3 scripts/validate-readmes.py`.

Use this workflow when a PR needs recorded behavioral evidence without claiming
that the repository has a reproducible automated model-evaluation harness.

## Prepare a Review

Generate a template for the affected skill:

```sh
python3 scripts/validate-scenario-review.py --skill effective-web --template \
  > /tmp/effective-web-review.json
```

Select the changed skill and the scenarios that exercise its consequential
behavior. Keep the relevant skill loaded in the agent under review, provide each
stored prompt unchanged, and record the actual response. Fill in the agent,
model/version, and sampling/runtime settings that materially affect the result.

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

## Validate the Record

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

This workflow is a transparent manual quality record. It does not make reports
comparable across models, replace a model-provider evaluation harness, or turn a
schema-valid report into proof that an agent will behave correctly in production.
If the collection later adds a reproducible provider-backed runner, it must
define the provider, model/version, sampling, rubric or grader, artifacts,
baseline, cost and flake policy, and its CI or scheduled execution boundary.
