# Things Action Format

Cluster briefs should end with a machine-readable action table so decisions can
be applied back to Things consistently.

## Required Table

```markdown
## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `abc123` | candidate | `Skill Archive Candidate` | yes | Primary source for visual regression workflow. |
| `def456` | rejected | `Skill Archive Rejected` | yes | Personal shopping link; no archive relevance. |
```

## Decision Values

Use one of:

- `candidate` -- capture into a skill/reference proposal.
- `deferred` -- keep for later, but not this pass.
- `rejected` -- archive-irrelevant, stale, duplicate, unreachable, or too weak.

## Applying To Things

For each final action:

1. Add `Skill Archive Reviewed`.
2. Add the final tag from the table.
3. Remove `Skill Archive Intake` if possible.
4. Mark complete when `Complete?` is `yes`.

Keep broad category tags such as `Skill: Testing`; they are useful audit trail.
