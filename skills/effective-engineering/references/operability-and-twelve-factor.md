# Operability and Twelve-Factor Practices

The [Twelve-Factor App](https://12factor.net/) is a methodology for portable,
cloud-friendly services. Use the factors as questions for long-running APIs,
workers, and scheduled processes. They do not prescribe microservices,
containers, a particular cloud, or a replacement for domain and security
architecture.

## Start with the Application-Platform Contract

Treat operability as a contract between an application and its execution
platform. Keep application-owned behavior explicit, then delegate generic
lifecycle, routing, configuration delivery, and telemetry transport to the
platform where doing so removes repeated application responsibility without
hiding the contract.

Use three ideals when shaping that contract:

- **Reduce application responsibility deliberately.** Trade unnecessary
  application-level control for a smaller operational surface and predictable
  platform behavior. Do not delegate domain invariants, data ownership, or
  security decisions the platform cannot own.
- **Make the paved path carry the practice.** Prefer frameworks, build systems,
  and platform conventions that provide correct lifecycle and operability
  behavior by default instead of requiring every feature team to recreate it.
- **Address day-two concerns on day one.** Make configuration, observability,
  replacement, update, recovery, and one-off operations part of the initial
  service contract rather than post-launch repair work.

## Apply the Factors to the Actual Service

| Practice | Architectural question | Evidence or guardrail |
| --- | --- | --- |
| Codebase | Is each deployable application traceable to one revision-controlled source lineage, with many deploys possible? | Source revision, build provenance, release version |
| Dependencies | Are runtime, build, and invoked system tools declared, versioned, and isolated rather than assumed from a host? | Manifest, lockfile, toolchain or image declaration, reproducible build |
| Configuration | Is deploy-varying configuration separate from code, independently adjustable, and safe to deliver without committing secrets? | Typed granular config contract, secret references, startup validation |
| Backing services | Can a database, cache, broker, or API be attached or replaced through configuration while its explicit application contract remains stable? | Resource handle, compatibility contract, timeout and failure tests |
| Build, release, run | Are build output, deploy configuration, and execution distinct, with every release immutable and the run stage minimal? | Artifact digest, release record, deployment history, mutation controls |
| Processes | Can work be safely retried or resumed without relying on mutable process-local state? | Durable state, idempotency, session strategy |
| Port binding | Does the service expose its listener or invocation contract without depending on an undeclared application server? | Listener or function configuration, readiness behavior |
| Concurrency | Are workload types explicit and independently managed by the execution environment rather than daemonized inside the app? | Process formation, queue depth, saturation, capacity evidence |
| Disposability | Do processes start promptly and stop gracefully without dropping or duplicating important work? | Startup, readiness, drain, shutdown, retry tests |
| Dev/prod parity | Do local, test, staging, and production differ only where intentionally necessary, especially at backing-service contracts? | Compatible service types and versions, representative fixtures, documented differences |
| Logs | Does the app emit an unbuffered event stream while the platform owns collection, routing, storage, and retention? | Structured stdout or platform event contract, correlation IDs, redaction, centralized collection |
| Admin processes | Do migrations, repairs, and one-off operations use the same release, configuration, and dependency discipline as regular processes? | Versioned task command, release identity, audit trail, recovery plan |

## Design the Operational Contract

For a consequential deployable unit, make these behaviors explicit:

- **Configuration:** validate required values at startup; distinguish defaults
  that are safe from required secrets; keep deploy controls granular rather
  than hiding them in one named environment bundle; log neither secrets nor
  sensitive input.
- **Dependency closure:** declare every library, runtime component, and external
  executable the app needs. Do not let a developer laptop or long-lived host
  supply an undeclared compatible version by accident.
- **Lifecycle:** define liveness, readiness, startup dependencies, graceful
  shutdown duration, connection draining, and what happens to in-flight work.
- **Failure handling:** set timeouts and bounded retries; use idempotency keys
  or durable work records where a retry can cause a business side effect;
  expose a clear exhausted-retry or compensation path.
- **Observability:** provide structured logs, metrics, traces, correlation
  identifiers, health signals, alert ownership, and a way to distinguish user,
  dependency, capacity, and application failures.
- **Data protection and recovery:** determine backup, restore, retention,
  encryption, access, and recovery requirements from the actual data and risk.
  Do not claim recovery without exercising the restore path.
- **Release safety:** keep artifacts identifiable, migrations compatible where
  possible, releases immutable, and runtime startup simple. Run migrations and
  repairs from the same release contract. A database migration may require
  forward repair rather than binary rollback; say so before deploying it.

## Avoid Mechanical Compliance

Do not force statelessness onto a system that has justified durable state;
place that state in an explicit, recoverable owner. Interpret “one codebase” as
traceable ownership of a deployable unit, not a ban on monorepos. Do not split a
codebase into services merely to satisfy codebase or concurrency language.

Environment variables are one portable delivery mechanism, not a requirement
to expose every setting or secret as plain process text. A typed runtime-config
API, mounted secret, or platform binding can satisfy the same separation when
its ownership, rotation, and startup behavior are explicit. Likewise, a
serverless function can have a clear invocation contract without visibly
binding its own port.

Do not make staging a literal production clone when scale, data sensitivity, or
budget make that impossible. Preserve the consequential contracts, document
material differences, and create focused verification for them. Apply the
process and log rules to long-running services; do not erase legitimate file or
terminal output contracts in desktop applications and command-line tools.

Use production evidence to tighten the operational contract. A factor is
useful only when it reduces a concrete delivery or operating risk in this
system.

This guidance distills the [Twelve-Factor App
project](https://github.com/twelve-factor/twelve-factor), licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), and adapts its
application-platform contract to the evidence and boundaries of this skill.
