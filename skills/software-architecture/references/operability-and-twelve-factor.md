# Operability and Twelve-Factor Practices

The [Twelve-Factor App](https://12factor.net/) is a methodology for portable,
cloud-friendly services. Use the factors as questions for long-running APIs,
workers, and scheduled processes. They do not prescribe microservices,
containers, a particular cloud, or a replacement for domain and security
architecture.

## Apply the Factors to the Actual Service

| Practice | Architectural question | Evidence or guardrail |
| --- | --- | --- |
| Codebase | Is one deployable application traceable to one revision-controlled codebase, with many deploys possible? | Source, build provenance, release version |
| Dependencies | Are runtime and build dependencies declared and isolated rather than assumed from a host? | Manifest, lockfile, reproducible build |
| Configuration | Can deploy-specific configuration vary without changing code or committing secrets? | Typed config contract, secret references, startup validation |
| Backing services | Can a database, cache, broker, or API be treated as an attached dependency with an explicit contract? | Connection configuration, timeout and failure tests |
| Build, release, run | Are immutable build output, deploy configuration, and the running process distinguishable? | Artifact digest, release record, deployment history |
| Processes | Can work be safely retried or resumed without relying on mutable process-local state? | Durable state, idempotency, session strategy |
| Port binding | Does the service declare how it accepts traffic rather than depend on a preconfigured application server? | Listener configuration, readiness behavior |
| Concurrency | Is workload scaling based on independently managed process types or workers? | Queue depth, saturation, autoscaling or capacity evidence |
| Disposability | Do processes start promptly and stop gracefully without dropping or duplicating important work? | Startup, readiness, drain, shutdown, retry tests |
| Dev/prod parity | Do local, test, staging, and production environments differ only where intentionally necessary? | Same service contracts, representative fixtures, documented differences |
| Logs | Are logs emitted as structured event streams rather than managed as application-owned files? | Correlation IDs, redaction, centralized collection |
| Admin processes | Do migrations, repairs, and one-off operations run with the same release and configuration discipline? | Versioned task command, audit trail, rollback plan |

## Design the Operational Contract

For a consequential deployable unit, make these behaviors explicit:

- **Configuration:** validate required values at startup; distinguish defaults
  that are safe from required secrets; log neither secrets nor sensitive input.
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
  possible, and rollback conditions explicit. A database migration may require
  forward repair rather than binary rollback; say so before deploying it.

## Avoid Mechanical Compliance

Do not force statelessness onto a system that has justified durable state;
place that state in an explicit, recoverable owner. Do not split a codebase
into services merely to satisfy “one codebase” or concurrency language. Do not
make staging a production clone when scale, data sensitivity, or budget make
that impossible; document the material difference and create focused
verification for it.

Use production evidence to tighten the operational contract. A factor is
useful only when it reduces a concrete delivery or operating risk in this
system.
