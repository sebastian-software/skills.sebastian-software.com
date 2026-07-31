# Route: Rust Performance and Memory

Use this route when the task makes a runtime, build-time, binary-size,
profiling, or benchmark claim, or when choosing collections, allocation
strategies, representations, alignment, cache layout, boxing, integer widths, or
binary-size techniques.

Start from the Rust entry route for the ownership, naming, error, and review
contract; come here for the measurement and layout decision.

## Read

- [Performance and profiling](rust-performance-and-memory.md) for runtime,
  build-time, binary-size, profiling, and benchmark claims.
- [Memory and data layout](rust-memory-and-data-layout.md) for collections,
  allocation strategies, representations, alignment, cache layout, boxing,
  integer widths, and binary-size techniques.

Load the one the task needs. Both together are appropriate only when a layout
change is the proposed answer to a measured runtime problem.

## Apply

- Profile before optimizing. Do not choose integer widths, collection layouts,
  boxing, inlining, LTO, allocation strategies, or copying thresholds from a
  generic size rule.
- Treat a performance change as a measurement contract: record workload,
  platform, toolchain, build profile, baseline, metric, and the evidence that
  identified the bottleneck.
- State unverified platform or performance claims explicitly rather than
  implying they were measured.

## Cross-links

- Benchmark methodology — how to construct, run, and interpret a
  repository-native microbenchmark, comparative benchmark, or bounded
  end-to-end workflow benchmark — is the Benchmarks route.
- SIMD, target features, atomics, Rayon, and thread pools are the Rust Unsafe
  and SIMD route.
- Executing an existing repository benchmark command belongs to
  `effective-delivery`.
- Performance objectives, workload scenarios, and capacity decisions are the
  Architecture route.
