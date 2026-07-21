# Modularity and Testability

Testability is primarily a property of responsibilities and boundaries, not of
how many collaborators a mocking library can intercept. When a test needs a
large mock graph, first find the mechanism that actually decides the result.

## Extract the Mechanism, Not a Mocking Surface

Identify the rule, transformation, calculation, validation, state transition,
or protocol decision that carries the behavior. Give it the smallest cohesive
function or module with explicit inputs and observable outputs.

- Use a pure function when the behavior is naturally pure.
- Use a small explicit stateful module when state is intrinsic; expose the
  transition, result, and next state rather than hiding them in callbacks.
- Keep network, database, filesystem, clock, randomness, process, framework,
  and notification wiring in thin outer adapters.
- Extract a production concept with a real responsibility. Do not create a
  one-method interface solely so a mocking framework can intercept it.

Then test the mechanism directly with ordinary values and normal construction.
At the adapter, preserve the nearest real boundary that still has behavior to
prove. An adapter that only forwards an already-protected result may have no
meaningful direct unit test.

## A Small Example of the Decision Boundary

If a service method mixes eligibility, state updates, persistence, and
notification, do not immediately program four collaborators to return a
scripted sequence. First separate the eligibility and transition:

1. represent the relevant account state and requested action explicitly;
2. calculate accept, reject, and next state in a cohesive mechanism;
3. test permitted, denied, and boundary cases directly with real values;
4. let the adapter persist an accepted transition and send the resulting
   notification; and
5. verify the persistence or delivery boundary where its real semantics matter.

This preserves a clear policy test and makes the integration evidence smaller.
It does not justify extracting a new service, changing ownership, or redesigning
the runtime merely to make one test convenient.

## Refactor Legacy, Untested Code Safely

An entangled module can be too risky to reshape blind. Before extraction:

1. locate an existing seam that can observe only the behavior relevant to the
   planned change;
2. add a temporary characterization test at that seam with representative
   inputs and outputs;
3. mark any observed defect as known-wrong behavior rather than silently
   treating it as a permanent contract;
4. extract the decision mechanism beneath that protection;
5. add direct mechanism tests and a meaningful boundary test; and
6. remove the temporary pin only when the new evidence makes it genuinely
   redundant.

Do not use characterization coverage to preserve unrelated accidental behavior,
and do not let it become a reason to keep the code entangled.

## Use Doubles in Order

Use this ladder for the remaining outer boundary:

1. **Direct mechanism:** real inputs and outputs after modularization.
2. **Real local boundary:** a local database, filesystem, transport fixture,
   fixture, replay, or focused integration environment when it is sensibly
   executable.
3. **Contract-faithful fake:** only when that boundary cannot sensibly run. A
   fake provides the same relevant contract, contains no invented convenience
   semantics, and, when reused, should ideally share contract tests with the
   real implementation.
4. **Mock:** only for an irreducible unavailable, destructive, credentialed,
   nondeterministic, or prohibitively slow boundary. Keep it outermost and
   explain the exception in the test or change description.

Value injection for a clock, configuration, seed, UUID source, or random value
is normal API design. It makes the mechanism explicit; it is not a behavior
simulation that needs mock-style interaction expectations.

## Stop Signals

Pause and reassess when a test requires nested mocks, ordered calls that are not
externally observable, hand-written imitation of a real datastore, a fake that
adds shortcuts the production contract lacks, or setup larger than the behavior
under test. These signs usually mean the decision boundary remains hidden or
the chosen layer is wrong. Improve the seam, use a real local boundary, or state
why an exceptional double is unavoidable.
