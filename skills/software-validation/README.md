[← Sebastian Software Skills](../../README.md)

# Software Validation

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Run the checks a repository actually trusts and show exactly what evidence is
still missing.**

Software Validation discovers and executes established repository-native
typecheck, static-analysis, lint, format, test, benchmark, load, soak, stress,
build, package, and documentation checks. It preserves package scope and
working state, handles timeouts and shared workspace risks explicitly, and
reports every applicable category as passed, failed, skipped, or timed out.

## What It Can Deliver

- a deduplicated validation plan grounded in repository instructions, CI, task
  runners, manifests, and contributor documentation
- narrow package checks and required dependent checks for monorepos without
  competing top-level orchestrators
- safe sequential or conditionally parallel execution with bounded timeouts and
  verified process-tree cleanup
- exact commands, scopes, diagnostics, warnings, skipped prerequisites, and
  remaining evidence gaps
- detection and preservation of unrelated working changes and
  validation-generated output

## Example Prompts

```text
Validate this package change using the repository's established checks. Tell me
what ran, what was skipped, and what evidence is still missing.

Discover the canonical quality gate for this monorepo and run the smallest scope
that still covers the changed package and its affected dependents.

Run the existing docs build, doctests, link checks, and generated-reference
verification without installing any missing tools.

Run this repository's established benchmark and soak commands exactly once,
preserve their result artifacts, and report any missing prerequisites.
```

See [SKILL.md](SKILL.md) for command discovery, execution safety, result states,
and ownership boundaries.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill software-validation
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian software-validation
dalo approve skill sebastian:software-validation
dalo sync
```

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) coordinates wider
  implementation and hands established-check execution to this skill.
- [Software Testing](../software-testing/README.md) designs, authors, repairs,
  and interprets focused non-frontend test and benchmark evidence; this skill
  runs existing test, benchmark, load, soak, and stress commands.
- [Effective Web](../effective-web/README.md) owns frontend and browser test
  design; this skill executes already-established repository checks.
- [Codebase Improvement](../codebase-improvement/README.md) diagnoses and
  prioritizes repository risk; this skill reports current validation evidence.
- [Tech Docs](../tech-docs/README.md) authors and verifies documentation content;
  this skill runs existing documentation gates.
- [PR Review](../pr-review/README.md) owns PR-scoped review, CI interpretation,
  and merge judgment; this skill supplies local repository-native check results.
- [Software Architecture](../software-architecture/README.md) chooses system
  quality targets; this skill executes checks against established targets.

## Scope

This skill executes and interprets checks the repository already defines. It
does not invent commands, install missing tools, design tests, set coverage or
quality targets, prioritize improvements, author documentation, or own commits,
pull requests, CI infrastructure, approvals, and delivery orchestration. A green
run is evidence for the checks that ran, not proof of untested correctness.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
