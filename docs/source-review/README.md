# Source Review Principle

Things links are an input channel, not durable project content.

When a source is useful, fold the reusable rule, checklist item, caveat, or
implementation guidance into the relevant skill under `skills/`. Keep only a
small source metadata block next to the rule when provenance matters.

When a source is not useful enough to change a skill, leave it out of the
repository. The repository should not preserve intake queues, copied link
archives, generated Things reports, or bulk triage notes.

## Current Rule

Process links one at a time:

1. Verify the source.
2. Read the target skill/reference.
3. Update the skill only if the source improves repeatable agent behavior.
4. Commit the source-specific change.
5. Keep operational state in Things, not in this repository.

## Commit Metadata

For source-processing commits, include:

```text
Things-ID: <id, or not provided>
Source: <url>
Decision: primary|secondary|ignored|deferred|rejected
Target: <skill/reference>
URL-Recheck: <date and result>
```
