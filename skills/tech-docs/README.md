[← Sebastian Software Skills](../../README.md)

# Tech Docs

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Design, write, and verify technical documentation that fits the software, its
repository, and its readers.**

Tech Docs helps agents create and maintain READMEs, task and contributor guides,
API and CLI documentation, migration notes, code documentation, and executable
examples. It starts from the implemented contract and the repository's existing
language, structure, tooling, and conventions instead of imposing one universal
documentation system.

## What It Can Deliver

- focused READMEs and guides organized around reader tasks
- API, CLI, configuration, and migration documentation grounded in code
- useful JSDoc, TSDoc, rustdoc, docstrings, and explanatory comments
- copyable examples with explicit prerequisites and observable results
- documentation updates synchronized with changed interfaces
- repository-native docs builds, doctests, example checks, and link validation

## Use It When

Use this skill when software users or contributors need a reliable path through
an interface or workflow: onboarding to a repository, completing a setup task,
using an API or CLI, migrating between versions, understanding a public code
contract, or verifying that existing documentation still matches the product.

It preserves the project's established documentation language and architecture
unless changing them is the task. It does not turn a documentation request into
a repository-wide audit or a new orchestration system.

## Example Prompts

```text
Rewrite this README around the first successful contributor workflow and verify
every command against the repository.

Document the new CLI subcommand, including configuration precedence, exit
behavior, a copyable example, and the repository-native checks.

Add TSDoc to this public TypeScript API. Explain the behavioral contract and
errors without restating types already present in the signature.

Write a migration guide for this breaking configuration change with version
constraints, checkpoints, verification, and the supported recovery path.
```

See [SKILL.md](SKILL.md) for the workflow, documentation routes, verification
rules, and ownership boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill tech-docs
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian tech-docs
dalo approve skill sebastian:tech-docs
dalo sync
```

## Related Skills

- [Codebase Improvement](../codebase-improvement/README.md) diagnoses
  documentation or expectation drift and prioritizes repository-wide
  documentation opportunities; this skill owns the correction and verification.
- [Software Validation](../software-validation/README.md) executes existing docs
  builds, doctests, link checks, examples, and combined repository gates without
  taking ownership of documentation craft.
- [Decision Records](../decision-records/README.md) preserves durable accepted
  choices before this skill documents their consequences.
- [Effective Web](../effective-web/README.md) owns browser-interface copy and
  frontend implementation concerns.
- [Locale Typography](../locale-typography/README.md) applies locale-specific
  punctuation and formatting.
- [Metro English](../metro-english/README.md) supplies a natural professional
  English voice when requested.
- [Software Architecture](../software-architecture/README.md) resolves the
  system direction that architecture documentation describes.

## Scope

This skill owns technical-documentation craft and verification. It does not own
marketing positioning, repository-wide audit prioritization, unresolved system
design, legal documentation, or an approval, commit, worktree, and delivery
lifecycle.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
