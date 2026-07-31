# Route: Review Provider Access and Caller Handoff

How the Review route reaches a pull request, and what it returns when the caller
keeps authority. Read this alongside the Review route, not instead of it.

## Select one coherent access path

1. Read [Provider access](provider-access.md). Choose exactly one: connected
   provider tools, a capable CLI or API, or complete caller-supplied Mode A
   context with caller-owned publication. Do not mix adapters mid-run.
2. Resolve review identity once from caller input or that adapter; never require
   a logged-in user when an app or bot is the delivery actor.
3. Read [GitHub CLI fallback recipes](gh-recipes.md) only when `gh` is the
   selected adapter. Do not translate those commands to another provider by
   analogy — GitLab, Forgejo, and Gitea differ in ways that silently change
   meaning.

Caller-supplied full PR context runs the Review route's normal ladder and
returns `pr-review-result/v1`; unlike Mode C, it produces an actual review.

## Mode C — caller-owned analysis handoff

Use Mode C only when a caller supplies review items for classification while
retaining approval, implementation, and delivery. It is provider-neutral: do not
assume a provider. Analyze only the supplied material — no repository, Git,
provider, CI, deployment, or thread discovery, and no mutations. Caller
constraints override every autonomous Mode B default.

Follow the [Mode C contract](mode-c-contract.md) exactly: the supplied inputs,
the prohibited actions, and the single-JSON-object response (schema
`pr-review-handoff/v1`, preserved item IDs and constraints, the fixed
classification and recommended-action vocabularies, and explicit
`missing_inputs` / `missing_evidence` instead of invented facts). The caller
decides whether and how to act on every recommendation.

## Cross-links

- The review ladder, decision thresholds, voice, and Mode A and Mode B
  workflows are the Review route.
- Orchestration, delivery authority, and completion standards are the
  Orchestration route.
