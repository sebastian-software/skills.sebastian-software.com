---
name: software-testing
description: >-
  Design, implement, diagnose, and verify focused non-frontend software tests
  for services, APIs, databases, async work, CLIs, and Rust. Use when asked
  to protect a behavior, invariant, regression, failure path, retry,
  authorization rule, migration, command-line contract, or flaky test; to
  diagnose test discovery, collection, runner, or framework configuration; to
  make a rule or state transition directly testable; or to add a focused
  performance-regression guard. Prefer repository-native test conventions and
  real behavior over mock choreography. Do not use for browser, component,
  visual, accessibility, or browser E2E testing; repository-wide coverage
  audits; broad system-quality design; or load and capacity methodology.
---

# Software Testing

Turn a concrete behavior, invariant, failure mode, or regression risk into the
smallest reliable evidence the repository can support. Test the mechanism that
decides the behavior directly, then preserve every real boundary that matters
to the claim.

## Workflow

1. Read scoped instructions and discover the repository's test layout,
   commands, frameworks, fixtures, helpers, environments, and nearby examples.
   Follow those conventions unless they cannot observe the risk. Do not add a
   test runner, assertion library, crate, or coverage target merely because a
   generic recipe prefers one.
2. State the claim before selecting a test: the behavior or invariant to
   protect, the input or state that exercises it, the observable result, and
   the failure it must distinguish. Separate a known fact from an assumption
   about a dependency, race, authorization model, or production environment.
3. Choose the narrowest evidence layer that can observe the real risk. Read
   [Select test evidence](references/select-test-evidence.md) for a behavior
   and risk model, properties, snapshots, replays, negative proof, and
   verification of the test itself.
4. Make the decision-carrying mechanism directly testable before considering a
   double. Read [Modularity and testability](references/modularity-and-testability.md)
   when policy, transformation, validation, calculation, state transition, or
   protocol choice is entangled with I/O or framework wiring.
5. Load the focused boundary guidance when it applies:
   - API, service, database, migration, isolation, asynchronous, retry,
     queue, callback, failure-path, or focused performance work: read
     [Services, data, and async](references/services-data-and-async.md).
   - Command invocation, configuration, stdout or stderr, exit behavior, or
     filesystem side effects: read [CLI contracts](references/cli-contracts.md).
   - Rust-native test placement, public-API coverage, doctests, or opt-in live
     smoke evidence: read [Rust testing](references/rust-testing.md).
6. Use the test-double ladder deliberately:
   1. Extract and test the cohesive mechanism directly with real values.
   2. At the remaining outer boundary, prefer the real local implementation,
      fixture, replay, or focused integration environment.
   3. Use a contract-faithful fake only when the real boundary is not sensibly
      executable. A reusable fake should ideally run through the same relevant
      contract tests as the real implementation; it must not invent convenient
      behavior. Supplying a clock, configuration, seed, or random value is
      ordinary input design, not mocking.
   4. Use an interaction-verifying or behavior-simulating mock only as a last
      exception for a genuinely unavailable, destructive, credentialed,
      nondeterministic, or prohibitively slow boundary. State why a direct
      test, real component, fixture, replay, or focused integration test could
      not preserve the contract. Keep it at the outermost boundary and assert
      interactions only when the interaction is itself the contract.

   A growing mock graph is a stop signal: improve the production seam instead
   of simulating another collaborator.
7. Make state explicit. Reuse repository-native fixtures and helpers; control
   identity, time, randomness, concurrency, external data, credentials, and
   cleanup whenever they could change the result. Exercise meaningful failure
   paths, not just the happy path.
8. Prove discrimination when practical. For new behavior, observe the focused
   failure before implementing it when that fits the repository. For an
   existing fix, reproduce the regression, temporarily reverse or mutate the
   relevant behavior, or use equivalent targeted negative proof. Do not delete
   sound implementation work merely to reenact a test-first ritual.
9. Run the narrow test first, then the relevant broader repository check.
   Report what ran, skipped credentials or live dependencies, and any remaining
   evidence gap honestly.

## Operating Rules

- Prefer a test of observable behavior over coverage percentage, assertion
  count, mock call choreography, or a generic test-pyramid label. One behavior
  can need several related assertions; one assertion can be insufficient.
- Preserve each boundary whose actual behavior makes the claim true: real
  authorization, serialization, schema, transaction, process, timeout, or
  protocol semantics should not disappear behind a unit mock.
- Keep side-effecting orchestration thin. If an adapter adds no decision or
  invariant, protect it through the nearest meaningful integration or smoke
  boundary rather than adding a ceremonial mock-heavy unit test.
- A scoped extraction that exposes a cohesive rule, transformation, or state
  transition is in scope. Do not turn a focused test request into a broad
  redesign that changes runtime responsibilities or major system boundaries;
  identify and route that design problem instead.
- Diagnose flakes by locating the uncontrolled time, ordering, shared state,
  cleanup, external dependency, or hidden retry. Do not hide the cause behind
  sleeps, retries, loosened assertions, or an arbitrary timeout.
- A focused performance-regression guard for a concrete function or service
  path is in scope when the environment and target are explicit. Prefer a
  trend or relative threshold on shared CI when an absolute number would be
  brittle. Do not claim load, soak, capacity, or comprehensive benchmark
  methodology.
- TypeScript and Rust are the primary ecosystems for this skill. Follow local
  conventions in other languages; do not use their presence to prescribe a
  language-specific stack.

## Routing Boundaries

- Route browser, component, visual, accessibility, browser E2E, browser
  performance, and an overall frontend testing strategy to `effective-web`.
  Route by primary mission, not artifact type: a browser feature belongs there
  even when it contains pure logic. An independent shared library or a
  server-side domain contract belongs here. For server actions and API routes,
  `effective-web` owns the UX and browser workflow while this skill owns the
  domain rule and service contract.
- Route repository-wide coverage audits, risk prioritization, and broad test
  improvement planning to `codebase-improvement`.
- Route PR-scoped adequacy and merge judgment to `pr-review`.
- Route contract design, system quality scenarios, performance targets,
  capacity planning, and broader architectural redesign to
  `software-architecture`. This skill implements contract tests against an
  agreed contract, including consumer-driven contract tests, and produces
  focused evidence against a given or locally agreed target. Load, soak, and
  comprehensive benchmark methodology are not claimed by a skill yet; their
  ownership is under evaluation in #112.
- Route migration parity, differential evidence, and compatibility work to
  `port-codebases`.
- Route substantive runtime or service implementation decisions to the
  appropriate engineering capability. This skill owns the test design and any
  small testability refactor, not the surrounding delivery workflow.
- Leave orchestration, worktrees, commits, approvals, and delivery flow to the
  calling workflow.
