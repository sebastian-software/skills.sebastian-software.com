# Interfaces and Migrations

## Document the observable contract

Derive reference facts from the implemented interface, schema, generated help,
tests, and supported configuration. For each relevant operation, make the
reader able to determine:

- what the operation does and when to use it;
- authentication, permissions, prerequisites, and version constraints;
- inputs, required and optional values, defaults, validation, and precedence;
- successful output and observable side effects;
- errors, exit behavior, retry or idempotency semantics, and recovery; and
- compatibility, deprecation, pagination, limits, or stability guarantees that
  the implementation actually provides.

Do not promise undocumented behavior merely because it would make a nicer API.
Surface a code or product gap separately when the desired contract does not
exist.

## API documentation

Use the repository's established schema and generator where available. Keep
generated reference content generated, and add authored explanation around it
instead of editing output that will be overwritten.

Choose examples that show a realistic request and response, including required
headers or setup and one decision-relevant failure when useful. Keep field
descriptions semantic: explain meaning, constraints, units, ownership, and
relationships rather than restating the field name or type.

## CLI and configuration documentation

Capture the actual invocation, subcommands, arguments, options, defaults,
environment variables, configuration files, and precedence rules. Distinguish
stdout from stderr and document meaningful exit codes, interactive behavior,
destructive operations, and automation-safe modes when the CLI supports them.

Prefer generated `--help` for exhaustive option listings when it is reliable.
Use authored guides for task sequences, decisions, examples, and failure
recovery. Verify examples against the built or local CLI rather than memory.

## Migration documentation

A migration guide should state:

1. who is affected and what changed;
2. the supported source and target versions or states;
3. prerequisites, backups, compatibility windows, and rollout constraints;
4. ordered changes with checkpoints;
5. validation after each consequential step;
6. rollback or recovery behavior; and
7. deprecation or removal timing only when it is actually committed.

Separate automatic transformations from manual work. Mark irreversible steps
before the reader performs them. If rollback is unavailable, say so plainly and
give the supported recovery path instead of inventing reversibility.
