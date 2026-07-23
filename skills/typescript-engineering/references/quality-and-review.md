# Quality and Review

## Review the Repository Contract First

Use the repository's `tsconfig` strictness, module and target settings, lint and
format policy, runtime, package manager, and validation commands. Do not add
`strict` flags the repository has not adopted, enable every ESLint rule, switch
module resolution, or install a tool as incidental cleanup. Judge the change
against the contract that exists, not against a maximal-strictness ideal.

Inspect the narrow changed module and its public surface:

- exported type and API compatibility, and whether a change breaks downstream
  compilation even when the local build is green;
- null and undefined handling, narrowing correctness, and every `as`, `!`, and
  `@ts-expect-error`/`@ts-ignore` suppression;
- `any` introductions and `unknown` values used without narrowing;
- promise ownership, floating promises, cancellation, and unhandled rejections;
- error representation, `cause` preservation, and boundary translation;
- module format and `exports`/`types` correctness for a published package;
- index access, optional-property handling, and assumptions about runtime
  globals the target may not provide.

## Do Not Cargo-Cult Strictness

Strictness serves correctness; it is not a score to maximize. A reasonable
`as const`, a well-justified assertion at a validated boundary, or a pragmatic
`unknown`-then-narrow is not a defect. Conversely, a green `tsc` with hidden
`any` or a lying type guard is worse than an honest `unknown`. Flag suppressions
that hide real unsoundness; do not flag a documented, contained escape hatch as
if it were the same thing.

## Avoid Magic Thresholds

Do not invent numeric limits — file length, function length, parameter count,
union-member count, or an arbitrary "too many generics" rule — as review
findings. Derive any limit from a protocol, a measured constraint, a product
requirement, or an established repository configuration, and name the reason.
"No magic numbers" means no unexplained policy value, not that every literal
needs a named constant.

## Keep Suppressions Local and Explained

When a suppression is genuinely needed, scope it to the smallest site, prefer
`@ts-expect-error` (which fails when the underlying error is fixed) over
`@ts-ignore`, state why it is correct, and note when it can be removed. Never
disable a lint rule across a file or blanket-cast to make a changed line pass.

## Produce Decisive Evidence

Start with a typecheck (`tsc --noEmit` or the repository's script) and the
focused lint and tests for the changed module, then the nearest consumer.
Distinguish a passing typecheck from a passing build when the repository
transpiles separately, and exercise the real runtime path when a claim depends
on it. Report exact commands and outcomes through `software-validation`; do not
claim a build, runtime, or compatibility result that was not actually run.
