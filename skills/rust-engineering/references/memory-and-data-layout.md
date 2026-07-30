# Memory and Data Layout

Use this reference when a profile points at allocations, heap peaks, copy
costs, object size, padding, cache misses, or binary size. Never optimize from
a blanket byte or container rule: measure the concrete workload and record the
layout and portability contract. For measurement design, flamegraphs, and
compiler profiles see [Performance and profiling](performance-and-memory.md).

## Contents

- [Working contract: measure, then lay out](#working-contract-measure-then-lay-out)
- [Allocations and lifetime](#allocations-and-lifetime)
- [Vec, String, and reallocation](#vec-string-and-reallocation)
- [HashMap, HashSet, and hashing](#hashmap-hashset-and-hashing)
- [Box, Rc, Arc, Cow, and copying](#box-rc-arc-cow-and-copying)
- [Type sizes, alignment, and padding](#type-sizes-alignment-and-padding)
- [Layout guarantees and repr](#layout-guarantees-and-repr)
- [Cache locality: AoS, SoA, and pointers](#cache-locality-aos-soa-and-pointers)
- [Dispatch, monomorphization, and code size](#dispatch-monomorphization-and-code-size)
- [DHAT for heap regressions](#dhat-for-heap-regressions)
- [Binary size and build artifacts](#binary-size-and-build-artifacts)
- [Safety, portability, and review](#safety-portability-and-review)
- [Diagnostic checklist](#diagnostic-checklist)
- [Sources and currency](#sources-and-currency)

## Working contract: measure, then lay out

1. Define the affected metric first: peak bytes, live bytes, allocation count,
   CPU time, cache misses, or artifact size. A smaller struct is not a goal
   when it does not improve the relevant metric.
2. Capture a baseline with the identical toolchain, target, feature selection,
   input distribution, and allocator. Store benchmark, heap, and binary-size
   artifacts.
3. Find allocation call sites with a profiler and connect them to lifetime and
   peak usage. Do not count only the total: many small short-lived blocks and
   few large long-lived blocks need different solutions.
4. Change data structure, ownership, and layout as isolated hypotheses.
   Re-confirm runtime, memory, code size, and maintainability afterwards.

The [Rust Performance Book – Benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html)
and the [Heap allocations](https://nnethercote.github.io/perf-book/heap-allocations.html)
chapter set the measurement frame. For the tooling steps see
[Performance and profiling](performance-and-memory.md).

## Allocations and lifetime

First examine whether a heap allocation is necessary at all:

- Keep values on the stack when size and lifetime are local and small.
- Pass borrowed slices and strings (`&[T]`, `&str`) when the caller owns the
  memory; this avoids `to_owned`/`clone` at API boundaries.
- Use `Vec::with_capacity` or `String::with_capacity` when the expected size
  can be derived from the protocol, `size_hint`, or a previous measurement. Do
  not reserve unrealistic maxima that raise peak RSS.
- Reuse mutable buffers (`clear` plus `extend_from_slice`/`read_to_end`)
  instead of creating new vectors in a loop. Measure whether the extended
  lifetime worsens the peak heap.
- Avoid implicit allocations from `format!`, `collect`, `lines`, `to_string`,
  `serde_json::to_string`, and temporary adapter chains in the hot path.

Use heap profiling to check whether a clone is actually needed for ownership.
`clone_from` can reuse the target buffer; compare it with a plain `clone` when
the target size varies strongly.
[Perf Book – Heap allocations](https://nnethercote.github.io/perf-book/heap-allocations.html)

Group allocations by lifetime. Short-lived scratch data can be bundled in an
explicit arena or bump allocator; long-lived objects must not be forced into an
arena lifetime. Introduce an arena allocator only when the profile confirms the
free/allocate cost and the lifetime structure. Document drop semantics, thread
compatibility, and fragmentation.

Treat the global allocator as a system boundary. An alternative allocator
changes fragmentation, thread contention, RSS, and FFI behavior; measure it
against the default allocator on every supported platform and version the
choice. Do not use an allocator swap as a substitute for removing unnecessary
clones.

## Vec, String, and reallocation

Use `Vec<T>` as the default for contiguous sequences. Its elements are stored
contiguously, so sequential iteration and prefetching work well. A `Vec` holds
pointer, length, and capacity; `len` is not the reserved capacity. Check
`capacity()` in the profile to distinguish over-reservation from reallocation.

- Use `with_capacity(n)` when `n` is well founded.
- Use `reserve`/`reserve_exact` deliberately: `reserve` may grow geometrically
  and amortizes reallocation; `reserve_exact` saves potentially unused space
  but can cause more allocations under incremental growth.
- Use `shrink_to`/`shrink_to_fit` only outside critical loops and only when
  returning the memory justifies the cost.
- Trim with `truncate` or `clear` at the end when the buffer is reused.
  `clear` keeps the capacity.
- Communicate known sizes through `Iterator::size_hint` or
  `ExactSizeIterator` so `collect`/`extend` can reserve sensibly.

The same rules apply to `String` for text; avoid repeated `format!`/`push_str`
without capacity planning. For UTF-8 protocols you may use `Vec<u8>` and
`read_until` when validation is only needed later.
[Perf Book – I/O](https://nnethercote.github.io/perf-book/io.html)

Use `SmallVec` or an inline array only for a measured small-size-dominant
workload. Inline storage enlarges every value and can pressure the cache with
large elements or nested structures. Document the inline-capacity contract and
compare heap allocations, `size_of::<T>()`, and iteration separately.
[Perf Book – Standard library types](https://nnethercote.github.io/perf-book/standard-library-types.html)

## HashMap, HashSet, and hashing

Use `HashMap`/`HashSet` for fast average lookup cost, not for stable iteration
order or automatically minimal memory. Check in the profile:

- Reserve capacity from a well-founded estimate (`with_capacity`), but avoid
  blanket reservation on every request.
- Remove entries with `retain`/`drain` when the table is reused as a buffer;
  decide deliberately whether the capacity should remain.
- Use a faster hasher only with a known threat model. Many hashing
  alternatives are vulnerable to hash flooding with untrusted keys.
- For integer or enum keys a specialized, collision-resistant hasher can be
  faster; prove the effect with both adversarial and normal data.
- Check whether a dense ID set permits a `Vec<Option<T>>`, `Vec<T>` plus
  bitset, or a sorted sequence instead of hashing.

Compare hash function, load factor, key size, and cache behavior together; a
faster hash function does not automatically make pointer or bucket misses
cheaper. [Perf Book – Hashing](https://nnethercote.github.io/perf-book/hashing.html)

## Box, Rc, Arc, Cow, and copying

Choose pointer containers by ownership contract:

- Use `Box<T>` when a value deliberately belongs on the heap (for example
  recursive types or large rare variants). Measure whether the extra
  indirection hurts the cache-hot path.
- Use `Rc<T>` only single-threaded and `Arc<T>` only for genuine cross-thread
  sharing. Both store reference counts and add indirection; `Arc::clone` is
  cheap but not free.
- Use `Cow<'a, [T]>`/`Cow<'a, str>` when the common path can stay borrowed and
  mutation is rare. Verify that the clone fallback is rare enough in the real
  workload.
- Use `clone_from` for reused target values; check the implementation and
  measure the capacity reuse.
- Use `mem::take`/`mem::replace` when ownership can be moved instead of
  forcing a deep copy.

Do not remove a pointer solely because of its size: it may enable recursion,
unsized values (`dyn Trait`, DSTs), or stable addresses. Always evaluate
indirection, allocation count, and access pattern together.

## Type sizes, alignment, and padding

Measure layout on the concrete deployment targets:

```rust
use std::mem::{align_of, size_of};

const _: () = {
    let _ = size_of::<MyType>();
    let _ = align_of::<MyType>();
};
```

Use `std::mem::size_of::<T>()` and `align_of::<T>()` in a small tool or test
for diagnosis. For a field overview use nightly `rustc -Zprint-type-sizes`
diagnostically only; the output format is not a stable build contract.
[Perf Book – Type sizes](https://nnethercote.github.io/perf-book/type-sizes.html)

Expect padding when a field has a higher alignment requirement than the
previous field. Do not reorder fields manually without a contract and a
measurement: with `repr(Rust)` the concrete field order is not guaranteed as an
ABI. Use `repr(C)` for FFI or an external layout contract and verify the
resulting size on all targets. [Rust Reference – Type layout](https://doc.rust-lang.org/stable/reference/type-layout.html)

Treat "large types" as a workload and target question. A threshold such as
128 bytes can prompt a copy-cost measurement, but it is not a Rust guarantee.
Measure `memcpy`/move cost, register pressure, stack usage, and cache effect
before boxing or splitting fields.

Reduce size with demonstrable measures:

- Replace wide state fields only when value range, overflow contract, and
  FFI/serialization allow it.
- Pack bool or enum state into a representation-stable bitset only when the
  extra mask operations do not hurt the hot path.
- Check large enum variants: `Box` can shrink the enum but adds an allocation
  and indirection.
- Measure `size_of` of container elements and total heap usage; a smaller
  header can lose through more external allocations.

## Layout guarantees and repr

Follow the [Rust Reference – Type layout](https://doc.rust-lang.org/stable/reference/type-layout.html):

- `repr(Rust)` guarantees field alignment, that fields do not overlap, and
  that the type is suitably aligned; concrete order, padding, and niche
  optimizations are not a general ABI contract.
- `repr(C)` fixes the C-compatible order and alignment rules. Use it for FFI,
  shared-memory formats, and explicit layout tests; it does not make a type
  FFI-safe as a whole (`String`/`Vec` remain Rust ownership types).
- Primitive `repr(u8)`/`repr(u16)` and similar stabilize the enum
  discriminant, not automatically all padding or variant payloads.
- Combine `repr(C, u8)`/`repr(C, u16)` only with a documented external format
  and test size, alignment, and offsets against the counterpart.
- Use `repr(transparent)` for the documented single-field wrapper contract,
  such as FFI newtypes.
- Avoid `repr(packed)` as a size optimization. Unaligned references are
  undefined behavior; access through `addr_of!` plus
  `read_unaligned`/`write_unaligned`, or copy into an aligned temporary. See
  [Rustonomicon – Working with unsafe](https://doc.rust-lang.org/stable/nomicon/working-with-unsafe.html).

For every layout dependency document: target architecture, `repr`, alignment,
field offsets, endianness, serialization format, and upgrade plan. Use
compile-time assertions only for deliberately stabilized contracts; avoid
assertions on incidental `repr(Rust)` details.

For pointer and DST layout: thin pointers (`&T`, `Box<T>`) and fat pointers
(`&[T]`, `&dyn Trait`) carry different metadata. Do not derive their size from
an incidental implementation; `size_of_val` measures the concrete value, not a
durable ABI. [Rust Reference – Dynamically Sized Types](https://doc.rust-lang.org/stable/reference/dynamically-sized-types.html)

## Cache locality: AoS, SoA, and pointers

Arrange data by access pattern, not by aesthetic field grouping:

- **AoS (array of structs):** choose it when each step needs nearly all fields
  of one object or when stable object boundaries matter.
- **SoA (struct of arrays):** choose it when a hot loop processes few fields
  across many objects. The active columns stay dense and reduce cache
  traffic; keep lengths and indices synchronized.
- **AoSoA/chunking:** evaluate it at SIMD or cache tile sizes when pure SoA or
  AoS layouts are impractical.
- **Pointer-rich graphs:** do not blindly replace `Box`/`Rc` chains. Check
  whether an arena plus indices or a `Vec<Node>` improves access locality and
  how stable-address and deletion requirements change.

Measure LLC/L1 misses, branch misses, and wall time with realistic data sets.
An SoA layout can add index arithmetic, scatter/gather, or synchronization
cost; accept it only with a positive overall balance.
[Data-Oriented Design in Rust](https://jamesmcm.github.io/blog/intro-dod/)

Avoid `LinkedList` for ordinary sequences: every step can cost a pointer
indirection and cache miss. Prefer `Vec`, `VecDeque`, or an index structure and
justify exceptions with measured insert/remove requirements.
[Perf Book – Standard library types](https://nnethercote.github.io/perf-book/standard-library-types.html)

## Dispatch, monomorphization, and code size

Use static generics (`impl Trait`, generic functions) when hot-path dispatch
and inlining matter and the code duplication is acceptable. Use `dyn Trait`
when many implementations are called rarely, binary size or compile time
matters more, or plugin boundaries are needed. Measure both variants; a vtable
indirection can cost branches and cache, while monomorphization can bloat the
instruction cache.
[Data-Oriented Design – Static vs dynamic dispatch](https://jamesmcm.github.io/blog/intro-dod/)

Split generic hot code paths into small reusable functions when Compiler
Explorer or `cargo asm` shows a relevant code explosion. Use
`cargo bloat`/`cargo llvm-lines` to attribute monomorphization and inlining
drivers; do not remove an abstraction without a size and runtime measurement.

## DHAT for heap regressions

Gate `dhat-rs` behind a feature so production builds contain no profiling
allocator:

```toml
[features]
dhat-heap = ["dhat"]

[dependencies]
dhat = { version = "...", optional = true }
```

```rust
#[cfg(feature = "dhat-heap")]
#[global_allocator]
static ALLOC: dhat::Alloc = dhat::Alloc;

fn main() {
    #[cfg(feature = "dhat-heap")]
    let _profiler = dhat::Profiler::new_heap();
    run_workload();
}
```

Run the diagnostic build in release configuration with a representative input.
For automatable limits use `Profiler::builder().testing().build()` and check
`HeapStats` values such as `total_bytes`, `total_blocks`, `max_bytes`, and
`max_blocks`.
[DHAT-rs – Configuration and setup](https://docs.rs/dhat/latest/dhat/#configuration-profiling-and-testing),
[DHAT-rs – Heap usage testing](https://docs.rs/dhat/latest/dhat/#heap-usage-testing)

Mark rare, semantic events with `dhat::ad_hoc_event(weight)` when the
allocation itself is not informative. Keep the profiler alive across the whole
relevant scope; a too-short lifetime skews the interpretation. DHAT is
experimental per its crate documentation and can change performance and timing
substantially. [DHAT-rs](https://docs.rs/dhat/latest/dhat/)

## Binary size and build artifacts

Define a size budget and measure the final, strippable artifact (`ls -lh`,
`size`, platform tool) separately from the debug or profiling build. Use
[`cargo bloat`](https://github.com/RazrFalcon/cargo-bloat) or
[`cargo llvm-lines`](https://github.com/dtolnay/cargo-llvm-lines) to attribute
large functions and generic duplication.

Start from a reproducible release profile:

```toml
[profile.release]
opt-level = "z"       # alternatively "s" or 3; measure
lto = true            # compare thin/fat
codegen-units = 1
panic = "abort"      # only when the API/FFI contract allows it
strip = "symbols"    # after profiler/debug runs
```

Choose `opt-level = "s"` or `"z"` by measurement; `"z"` is not guaranteed
smaller or faster than `"s"`. `lto = "thin"` can offer a better size and
link-time compromise than fat LTO. `codegen-units = 1` can improve
optimization and size but raises compile time. [rustc Codegen options](https://doc.rust-lang.org/rustc/codegen-options/index.html),
[min-sized-rust](https://github.com/johnthagen/min-sized-rust#optimize-for-size)

Keep a separate build with `debug = "line-tables-only"` or `debug = true` for
profiling; strip only the release artifact. Check whether panic strings,
backtraces, formatting and logging code, unused features, and monomorphization
form the largest share.

Consider `no_std`/`no_main` only for matching embedded or runtime contracts.
`panic = "abort"`, removing unwind or backtrace code, and aggressive linker
garbage collection change failure diagnostics and library boundaries. Verify
with cross-target CI that every artifact still starts and exports FFI symbols
correctly.

Use UPX or compression only when startup time, platform rules, signatures, and
deployment allow it; measure the packed and unpacked artifact sizes and
document the release step. [min-sized-rust – Compressing](https://github.com/johnthagen/min-sized-rust#compressing)

## Safety, portability, and review

- Treat `repr(packed)`, `read_unaligned`, `get_unchecked`, transmute, raw
  pointers, and custom allocators as unsafe proof obligations. Document
  provenance, initialization, alignment, bounds, aliasing, lifetimes, drop,
  unwind, and thread safety; see the
  [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/).
- Ship `target-cpu=native`/`target-feature` builds only when every user meets
  the CPU requirements. For portable SIMD use feature detection or multiple
  implementations; see [rustc target features](https://doc.rust-lang.org/rustc/codegen-options/index.html#target-feature).
- Couple layout assertions to an explicit `repr` and target. Test endianness,
  pointer width, alignment, and external serialization on all deployment
  platforms.
- Separate diagnostic flags (DHAT, PGO instrumentation, nightly
  `-Zprint-type-sizes`) from production profiles. Re-check toolchain and crate
  versions on every upgrade.

## Diagnostic checklist

- Which allocation call site causes peak bytes, and what lifetime does it have?
- Is the `Vec`/`String` capacity too small, too large, or reusable?
- Does the cost come from `clone`, `to_owned`, `collect`, `format!`,
  `Box`/`Arc` indirection, or hashing?
- Are `size_of`, `align_of`, and field padding known on all targets?
- Does AoS/SoA/chunking match the actual field access and cache profile?
- Is static dispatch a measured code and cache improvement or only an
  assumption?
- Which change actually reduces the measured binary-size component?
- Are unsafe, FFI, and CPU-feature contracts and fallbacks documented and
  tested?

## Sources and currency

Use the [Rust Reference](https://doc.rust-lang.org/stable/reference/type-layout.html)
for layout guarantees and the [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/)
for unsafe foundations. The [Rust Performance Book](https://nnethercote.github.io/perf-book/)
provides practice-oriented heuristics on allocations, type sizes, standard
containers, and hashing. Complement it with
[Data-Oriented Design in Rust](https://jamesmcm.github.io/blog/intro-dod/) for
data-layout questions, [DHAT-rs](https://docs.rs/dhat/latest/dhat/) for heap
regressions, and [min-sized-rust](https://github.com/johnthagen/min-sized-rust)
for binary-size questions.

Verify all CLI flags, crate versions, and platform assumptions against the
current toolchain. Numbers and thresholds from blog posts are starting points
for measurements, not stable Rust guarantees.
