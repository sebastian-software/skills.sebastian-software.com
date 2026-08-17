# Route: Focused Non-Frontend Testing

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
   [Select test evidence](select-test-evidence.md) for a behavior and risk
   model, properties, snapshots, replays, negative proof, and verification of
   the test itself.
4. Make the decision-carrying mechanism directly testable before considering a
   double. Read [Modularity and testability](modularity-and-testability.md) when
   policy, transformation, validation, calculation, state transition, or
   protocol choice is entangled with I/O or framework wiring.
5. Load the focused boundary guidance when it applies:
   - API, service, database, migration, isolation, asynchronous, retry, queue,
     callback, failure-path, or focused performance-regression work: read
     [Services, data, and async](services-data-and-async.md).
   - Command invocation, configuration, stdout or stderr, exit behavior, or
     filesystem side effects: read [CLI contracts](cli-contracts.md).
   - Rust-native test placement, public-API coverage, doctests, feature and
     `cfg` coverage, or opt-in live smoke evidence: read
     [Rust quality, review, and test evidence](rust-quality-and-review.md).
   - Microbenchmark, comparative benchmark, bounded end-to-end performance
     workflow, benchmark interpretation, or publishable performance claim: take
     the Benchmarks route.
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
  brittle. Do not claim load, soak, stress, or capacity methodology.
- TypeScript and Rust are the primary ecosystems here. Follow local conventions
  in other languages; do not use their presence to prescribe a
  language-specific stack.

## Cross-links

- Testing-strategy design — the test-pyramid shape, coverage goals, and which
  risks get which test types — plus contract design, system quality scenarios,
  performance targets, workload scenarios, and capacity planning are the
  Architecture route. This route implements focused tests against an agreed
  strategy or contract, including consumer-driven contract tests.
- Data models, datastore selection, transaction and consistency guarantees,
  replication, partitioning, stream semantics, and data-evolution strategy are
  the Data route. This route owns focused executable evidence for the agreed
  invariant, concurrent behavior, migration, retry, or failure contract.
- Rust and TypeScript implementation decisions beyond the minimal testability
  extraction are the Rust and TypeScript routes; this route owns the test design
  and any small testability refactor.
- Browser, component, visual, accessibility, browser E2E, browser performance,
  and overall frontend testing strategy belong to `effective-web`. Route by
  primary mission, not artifact type: a browser feature belongs there even when
  it contains pure logic; an independent shared library or a server-side domain
  contract belongs here. For server actions and API routes, `effective-web` owns
  the UX and browser workflow while this route owns the domain rule and service
  contract.
- Repository-wide coverage audits, risk prioritization, broad test improvement
  planning, PR-scoped adequacy and merge judgment, migration parity and
  differential evidence, and execution of an existing repository test,
  typecheck, lint, build, or documentation command belong to
  `effective-delivery`. Return here when new or repaired test evidence is the
  requested outcome.
- No first-party discipline currently claims new load, soak, or stress
  execution methodology; state that boundary instead of inventing a tool or
  traffic model.
- Leave orchestration, worktrees, commits, approvals, and delivery flow to the
  calling workflow.
