# Performance Engineering für Rust

Nutze diese Referenz für messgetriebene Laufzeitoptimierung, Profiling,
Compiler-/Build-Optimierung und die Auswahl geeigneter Messwerkzeuge. Lies für
konkrete Speicherlayouts, Container und Binary-Size-Details zusätzlich
[Memory and data layout](memory-and-data-layout.md).

## Inhaltsverzeichnis

- [Arbeitsvertrag und Messworkflow](#arbeitsvertrag-und-messworkflow)
- [Benchmark-Design mit Criterion](#benchmark-design-mit-criterion)
- [Profiling und Flamegraphs](#profiling-und-flamegraphs)
- [Heap- und Allokationsprofiling](#heap--und-allokationsprofiling)
- [Build-Profile und Codegen](#build-profile-und-codegen)
- [LTO, Linker und Debug-Informationen](#lto-linker-und-debug-informationen)
- [Profile-Guided Optimization](#profile-guided-optimization)
- [Hot-Path-Optimierung](#hot-path-optimierung)
- [I/O, Iteratoren und Bounds Checks](#io-iteratoren-und-bounds-checks)
- [Portabilität und Safety-Grenzen](#portabilität-und-safety-grenzen)
- [Diagnose-Checkliste](#diagnose-checkliste)
- [Quellen und Aktualität](#quellen-und-aktualität)

## Arbeitsvertrag und Messworkflow

1. **Definiere die Zielmetrik.** Entscheide, ob du Wall-Time, CPU-Zyklen,
   Instruktionen, Peak-Bytes, Allokationsrate, Binary-Größe oder Compile-Zeit
   verbessern musst. Vermeide ein unpräzises Ziel wie „schneller“.
   [Rust Performance Book – Benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html)
2. **Sichere eine Baseline.** Baue mit derselben Toolchain, denselben Features,
   demselben Target und realistischen Eingabedaten. Speichere Benchmark-,
   Profiler- und Binary-Size-Artefakte, bevor du Code änderst.
   [Rust Performance Book – Benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html)
3. **Profiliere zuerst.** Nutze Sampling/Flamegraphs, um Hotspots zu finden;
   behandle die Flamegraph-Breite nur als relative CPU-On-CPU-Auslastung und
   bestätige jeden Kandidaten mit einer fokussierten Messung.
   [flamegraph – Flamegraphs Are the Beginning, Not the End](https://github.com/flamegraph-rs/flamegraph#flamegraphs-are-the-beginning-not-the-end)
4. **Ändere eine Ursache.** Trenne Algorithmus-, Datenlayout-, Allokator-,
   Compiler- und CPU-Feature-Änderungen. So bleibt erkennbar, welche Änderung
   den Effekt verursacht.
5. **Wiederhole die Baseline-Messung.** Akzeptiere eine Optimierung nur, wenn
   Effektgröße, Konfidenzintervall und Kosten (Komplexität, Portabilität,
   Debuggability, Compile-Zeit) zum Vertrag passen.
6. **Dokumentiere die Begründung.** Vermerke Workload, Hardware, Toolchain,
   Messkommando und beobachtete Metrik direkt am Optimierungscode.

Verwende realistische Workloads und mehrere Größenklassen. Microbenchmarks sind
für enge Hotspots sinnvoll, dürfen aber keine Produktionsmessung ersetzen.
[Rust Performance Book – Benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html)

Halte den Rechner für Messungen ruhig und warm, aber nicht thermisch gedrosselt.
Kontrolliere CPU-Power-Modus, Hintergrundprozesse, VM-/CI-Last und
Speicheraktivität. [Criterion – A Note of Caution](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_output.html#a-note-of-caution),
[flamegraph – Performance Theory 101](https://github.com/flamegraph-rs/flamegraph#performance-theory-101-quantitative-engineering)

## Benchmark-Design mit Criterion

Richte Criterion als eigenes Benchmark-Crate ein:

```toml
[dev-dependencies]
criterion = "..."

[[bench]]
name = "hot_path"
harness = false
```

```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_hot_path(c: &mut Criterion) {
    c.bench_function("hot path", |b| {
        b.iter(|| hot_path(black_box(input())))
    });
}

criterion_group!(benches, bench_hot_path);
criterion_main!(benches);
```

Halte Setup außerhalb des gemessenen Closures, wenn du nur den Hot Path
bewerten willst. Verwende `black_box`, damit Eingaben und Ergebnisse nicht
konstant gefaltet oder als unbenutzt entfernt werden.
[Criterion – Getting Started](https://bheisler.github.io/criterion.rs/book/getting_started.html)

Berücksichtige das Criterion-Messmodell:

- Lass die Warmup-Phase CPU-/OS-Caches und gegebenenfalls JIT aufwärmen.
- Messe mehrere Samples mit mehreren Iterationen; Criterion schätzt Zeit pro
  Iteration aus dem gesamten Sample.
- Nutze die Bootstrap-Konfidenzintervalle und die gespeicherten Vergleichsdaten.
- Untersuche viele Ausreißer und niedriges R², statt nur den Mittelwert zu lesen.

[Criterion – Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html),
[Criterion – Command-Line Output](https://criterion-rs.github.io/book/user_guide/command_line_output.html)

Verwende diese Befehle für fokussierte Läufe und reproduzierbare Baselines:

```sh
cargo bench
cargo bench -- --verbose
cargo bench -- hot_path
cargo bench -- --profile-time 10
cargo bench -- --save-baseline before
cargo bench -- --baseline before
cargo test --benches
```

`--profile-time` unterdrückt die reguläre Analyse und Plot-Erzeugung und eignet
sich dadurch für externe Profiler. [Criterion – Command-Line Options](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html)

Verwende `BenchmarkGroup::throughput` nur, wenn du die pro Iteration
verarbeiteten Bytes/Elemente korrekt kennst. Nutze
`bench_with_input`/`BenchmarkId` für Eingabegrößen und implementiere bei eigenen
Iteratoren `size_hint` oder `ExactSizeIterator::len`, wenn die Länge bekannt ist.
[Criterion – Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html),
[Criterion – Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html)

Beachte, dass externe Criterion-Benchmarks aus einem separaten Crate auf
`pub`-Funktionen angewiesen sind. Lege rechenintensive Logik in eine Library
und halte eine Binärdatei als dünnen Adapter.
[Criterion – Known Limitations](https://bheisler.github.io/criterion.rs/book/user_guide/known_limitations.html)

## Profiling und Flamegraphs

Baue für lesbare Release-Stacks mindestens Zeilen-Debug-Informationen ein:

```toml
[profile.release]
debug = "line-tables-only"
```

Für `cargo-flamegraph` kann `debug = true` sinnvoll sein; setze für Benchmarks
gegebenenfalls `[profile.bench] debug = true`. [Rust Performance Book – Profiling](https://nnethercote.github.io/perf-book/profiling.html),
[flamegraph – Improving output](https://github.com/flamegraph-rs/flamegraph#improving-output-when-running-with---release)

Installiere und starte Flamegraphs so:

```sh
cargo install flamegraph
cargo flamegraph --bin app -- --input workload.dat
cargo flamegraph --bench hot_path -- --bench
flamegraph --pid 1337
```

Unter Linux verwendet das Tool `perf`, unter macOS `xctrace` und unter Windows
standardmäßig Blondie. Bei aktuellem lld/mold unter Linux kann
`-Wl,--no-rosegment` für genaue Stacks erforderlich sein.
[flamegraph – Quick Start](https://github.com/flamegraph-rs/flamegraph#quick-start),
[flamegraph – Linux](https://github.com/flamegraph-rs/flamegraph#linux)

Interpretiere ein Flamegraph-Element als Anteil der Samples, in denen die
Funktion aktiv oder im Call-Stack war. Die x-Achse ist keine Zeitachse; eine
schmalere Box beweist keine absolute Beschleunigung. Bestätige den Effekt mit
Criterion oder Instruktionszählung. [flamegraph – Systems Performance](https://github.com/flamegraph-rs/flamegraph#systems-performance-work-guided-by-flamegraphs),
[flamegraph – Flamegraphs Are the Beginning, Not the End](https://github.com/flamegraph-rs/flamegraph#flamegraphs-are-the-beginning-not-the-end)

Erweitere Sampling bei Bedarf mit Cachegrind/Callgrind für Instruktionen,
Cache- und Branch-Daten; verwende `perf`, Instruments, VTune, uProf oder samply
je nach Plattform. Erwarte von CPU-On-CPU-Sampling keine vollständige I/O- oder
Off-CPU-Latenzanalyse. [Rust Performance Book – Profiling](https://nnethercote.github.io/perf-book/profiling.html)

Nutze Criterion-Profiling-Hooks, wenn du einen In-Process-Profiler brauchst.
Implementiere `criterion::profiler::Profiler` und aktiviere ihn über
`with_profiler`; die Hooks laufen nur mit `--profile-time`.
[Criterion – Profiling](https://bheisler.github.io/criterion.rs/book/user_guide/profiling.html)

## Heap- und Allokationsprofiling

Wähle DHAT oder `dhat-rs`, wenn `malloc`/`free`, Peak-Heap, `memcpy` oder
Allokationsraten im Profil heiß erscheinen. [Rust Performance Book – Heap Allocations](https://nnethercote.github.io/perf-book/heap-allocations.html#profiling)

Für Rust-Heap-Tests feature-gate den Allocator und nutze Release-Builds:

```toml
[profile.release]
debug = 1

[features]
dhat-heap = []
```

```rust
#[cfg(feature = "dhat-heap")]
#[global_allocator]
static ALLOC: dhat::Alloc = dhat::Alloc;

fn main() {
    #[cfg(feature = "dhat-heap")]
    let _profiler = dhat::Profiler::new_heap();
}
```

```sh
cargo run --release --features dhat-heap
```

Aktiviere `dhat::Alloc` ausschließlich während Profiling; der Wrapper kann
deutlich verlangsamen und ist laut Crate-Dokumentation experimentell.
[DHAT-rs – Configuration and setup](https://docs.rs/dhat/latest/dhat/#configuration-profiling-and-testing),
[DHAT-rs – crate warning](https://docs.rs/dhat/latest/dhat/)

Nutze `Profiler::builder().testing().build()` und `HeapStats::get()`, um
`total_*`, `max_*` und `curr_*`-Bytes/Blocks als Regressionen zu prüfen.
[DHAT-rs – Heap usage testing](https://docs.rs/dhat/latest/dhat/#heap-usage-testing)

Für Ad-hoc-Häufigkeiten markiere Codepunkte mit
`dhat::ad_hoc_event(weight)`. Halte die Profiler-Lifetime möglichst über den
gesamten `main`-Bereich, weil Allokationen außerhalb der Lifetime ignoriert oder
als neue Allokationen behandelt werden können. [DHAT-rs – Ad hoc profiling](https://docs.rs/dhat/latest/dhat/#setup-ad-hoc-profiling),
[DHAT-rs – Running](https://docs.rs/dhat/latest/dhat/#running)

Verwende die detaillierten Container-/Layout-Regeln in
[Memory and data layout](memory-and-data-layout.md), bevor du wegen eines
Allokationsprofils `Box`, `SmallVec`, `Cow`, `clone_from` oder einen alternativen
Allocator einführst.

## Build-Profile und Codegen

Verwende für Laufzeitmessungen ein explizites Release-Profil. Passe
`codegen-units` nur mit Messung an: `1` verbessert oft Cross-Unit-Optimierung,
erhöht aber Compile-Zeit. [rustc Codegen – codegen-units](https://doc.rust-lang.org/rustc/codegen-options.html#codegen-units)

Setze `opt-level` bewusst:

- `3` optimiert auf Laufzeit;
- `s` optimiert auf Größe mit etwas mehr Inlining/Vektorisierung;
- `z` optimiert aggressiver auf Größe, ist aber nicht garantiert kleiner als `s`.

[rustc Codegen – opt-level](https://doc.rust-lang.org/rustc/codegen-options.html#opt-level),
[min-sized-rust – Optimize For Size](https://github.com/johnthagen/min-sized-rust#optimize-for-size)

Verwende `target-cpu=native` oder einzelne `target-feature` nur, wenn du den
CPU-Vertrag der Distribution kennst. Prüfe verfügbare Werte mit
`rustc --print target-cpus` und `rustc --print target-features`; ein falsches
Target kann Laufzeitfehler oder fehlende Portabilität verursachen.
[rustc Codegen – target-cpu](https://doc.rust-lang.org/rustc/codegen-options.html#target-cpu),
[rustc Codegen – target-feature](https://doc.rust-lang.org/rustc/codegen-options.html#target-feature)

Deaktiviere LLVM-Vektorisierung (`no-vectorize-loops`, `no-vectorize-slp`) nur
für Diagnosen oder A/B-Vergleiche. Verwende sie nicht als pauschale
Optimierungseinstellung. [rustc Codegen – vectorization flags](https://doc.rust-lang.org/rustc/codegen-options.html#no-vectorize-loops)

## LTO, Linker und Debug-Informationen

Vergleiche `lto = "thin"` und `lto = "fat"` mit derselben Workload. Thin LTO
reduziert die Linkzeit und erreicht oft ähnliche Laufzeitgewinne; fat LTO kann
zusätzliche Cross-Crate-Optimierung liefern, kostet aber mehr Zeit und ist nicht
immer besser. [rustc Codegen – lto](https://doc.rust-lang.org/rustc/codegen-options.html#lto)

Verwende `embed-bitcode=no`, wenn kein LTO benötigt wird; kombiniere es nicht mit
`-C lto`. Nutze `linker-plugin-lto` nur mit einem kompatiblen nativen Linker.
[rustc Codegen – embed-bitcode](https://doc.rust-lang.org/rustc/codegen-options.html#embed-bitcode),
[rustc Codegen – linker-plugin-lto](https://doc.rust-lang.org/rustc/codegen-options.html#linker-plugin-lto)

Wähle lld/mold/wild zur Compile-Zeitverkürzung nur nach einem erfolgreichen
Link-/CI-Lauf für alle unterstützten Targets. [Rust Performance Book – Linking](https://nnethercote.github.io/perf-book/build-configuration.html#linking)

Halte Debug-Zeilen für Profiler, auch wenn du Symbole im ausgelieferten Binary
strippst. `strip=debuginfo` oder `strip=symbols` reduziert Größe, kann aber
Backtraces und Debugger/Profiler schwächen. [rustc Codegen – strip](https://doc.rust-lang.org/rustc/codegen-options.html#strip)

## Profile-Guided Optimization

Führe PGO als reproduzierbaren Vier-Schritt-Prozess aus:

1. Instrumentiere mit `-Cprofile-generate=/absolute/path`.
2. Führe das instrumentierte Binary mit typischen Workloads mehrfach aus.
3. Führe `llvm-profdata merge` auf alle `.profraw`-Dateien aus.
4. Baue mit `-Cprofile-use=/absolute/path/merged.profdata` und identischen
   Compiler-Flags erneut.

```sh
rustup component add llvm-tools-preview
rm -rf /tmp/pgo-data
RUSTFLAGS="-Cprofile-generate=/tmp/pgo-data" \
  cargo build --release --target=x86_64-unknown-linux-gnu
./target/x86_64-unknown-linux-gnu/release/app typical-input
llvm-profdata merge -o /tmp/pgo-data/merged.profdata /tmp/pgo-data
RUSTFLAGS="-Cprofile-use=/tmp/pgo-data/merged.profdata" \
  cargo build --release --target=x86_64-unknown-linux-gnu
```

Gib `RUSTFLAGS` über Cargo an alle Crates weiter, verwende `--target`, damit
Build-Scripts keine Profile erzeugen, und lösche alte Profildaten vor dem
Training. Nutze `-Cllvm-args=-pgo-warn-missing-function`, um fehlende Profile zu
melden. [rustc PGO – Complete Cargo Workflow](https://doc.rust-lang.org/nightly/rustc/profile-guided-optimization.html#a-complete-cargo-workflow),
[rustc PGO – Troubleshooting](https://doc.rust-lang.org/nightly/rustc/profile-guided-optimization.html#troubleshooting)

Verwende `cargo-pgo`, wenn die manuelle Profilsequenz in eurem Build-System zu
fehleranfällig ist; prüfe trotzdem Trainingsdaten, Toolchain-Bindung und
Distribution. [rustc PGO – Community Maintained Tools](https://doc.rust-lang.org/nightly/rustc/profile-guided-optimization.html#community-maintained-tools)

## Hot-Path-Optimierung

Profiliere vor `#[inline]`, `#[inline(always)]` oder `#[inline(never)]`.
Inlining kann Call-Overhead und zusätzliche Optimierung ermöglichen, aber auch
Codegröße, Compile-Zeit und Instruction-Cache-Druck erhöhen. Inlining ist nicht
transitiv; messe nach jeder Annotation. [Rust Performance Book – Inlining](https://nnethercote.github.io/perf-book/inlining.html)

Verlagere seltene Fehler-/Sonderpfade in eine separate `#[cold]`-Funktion, wenn
das Profil zeigt, dass der Hot Path durch sie aufgebläht wird. [Rust Performance Book – Outlining](https://nnethercote.github.io/perf-book/inlining.html#outlining)

Untersuche generierten Code nur für kleine, wirklich heiße Funktionen mit
Compiler Explorer oder `cargo-show-asm`; überprüfe Bounds Checks, Unrolling,
Inlining und SIMD im Assembly, statt deren Vorhandensein zu vermuten.
[Rust Performance Book – Machine Code](https://nnethercote.github.io/perf-book/machine-code.html)

Verwende für Datenparallelität Rayon/Crossbeam oder SIMD getrennt voneinander;
Thread-Parallelität und Vektorisierung lösen unterschiedliche Engpässe.
[Rust Performance Book – Parallelism](https://nnethercote.github.io/perf-book/parallelism.html)

## I/O, Iteratoren und Bounds Checks

Locke stdout/stderr bei vielen Ausgaben einmal manuell und puffere Datei-/Socket-
I/O mit `BufReader`/`BufWriter`, um Syscalls zu reduzieren. Verwende bei
Byte-orientierten Protokollen `read_until`, wenn UTF-8-Validierung unnötig ist.
[Rust Performance Book – I/O](https://nnethercote.github.io/perf-book/io.html)

Vermeide `collect`, wenn du das Ergebnis sofort wieder iterierst. Gib möglichst
`impl Iterator` zurück, nutze `extend` für bestehende Collections und liefere
`size_hint`, wenn die Ausgabelänge bekannt ist. [Rust Performance Book – Iterators](https://nnethercote.github.io/perf-book/iterators.html)

Verwende in Hot Loops `chunks_exact`, wenn die Blockgröße passt, und prüfe, ob
`iter().copied()` besseren LLVM-Code erzeugt. [Rust Performance Book – Iterators](https://nnethercote.github.io/perf-book/iterators.html#chunks)

Reduziere Bounds Checks zunächst sicher durch Iteration, vorher gebildete Slices
oder explizite Bereichsassertions. Verwende `get_unchecked` nur mit einem
lokalen, dokumentierten Safety-Beweis und erst nach gemessener Relevanz.
[Rust Performance Book – Bounds Checks](https://nnethercote.github.io/perf-book/bounds-checks.html),
[Rustonomicon – Working with Unsafe](https://doc.rust-lang.org/stable/nomicon/working-with-unsafe.html)

## Portabilität und Safety-Grenzen

- **CPU-Vertrag:** Liefere keinen `target-cpu=native`-Code aus, wenn ältere oder
  heterogene CPUs unterstützt werden müssen. Nutze Feature Detection oder
  mehrere Implementierungen.
- **Layout:** Verlasse dich nur auf dokumentierte `repr(C)`-/Alignment-Garantien;
  `repr(Rust)`-Feldreihenfolge und konkrete DST-Größen sind keine stabilen
  Optimierungsverträge. [Rust Reference – Type layout](https://doc.rust-lang.org/stable/reference/type-layout.html)
- **Unsafe:** Behandle `get_unchecked`, `repr(packed)`, Transmute und eigene
  Container als Proof Obligations, nicht als Performance-Labels. Dokumentiere
  Provenance, Bounds, Alignment, Aliasing, Lifetimes, Drop und Unwind-Verhalten.
  [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/),
  [Rust Engineering – Unsafe and FFI](unsafe-and-ffi.md)
- **Panic-Semantik:** `panic = "abort"` spart Unwind-Code, verändert aber das
  Verhalten und kann Bibliotheks-/FFI-Verträge brechen. [rustc Codegen – panic](https://doc.rust-lang.org/rustc/codegen-options.html#panic)
- **Profiling-Overhead:** DHAT-Allocator, Instrumentierungs-PGO und Debug-Info
  beeinflussen die Messung. Verwende sie nur für den diagnostischen Lauf und
  miss den finalen Build separat.
- **Experimental:** `dhat` und mehrere Nightly-Flags können abstürzen, hängen,
  ABI-/Toolchain-Änderungen unterliegen oder unvollständige Ergebnisse liefern.
  Markiere diese Abhängigkeiten in CI und prüfe sie bei Toolchain-Upgrades.

## Diagnose-Checkliste

### Laufzeit

- Messe ich tatsächlich den Release-Build mit dem Produktions-Target?
- Sind CPU-Power, Temperatur, VM/CI und Hintergrundlast kontrolliert?
- Ist der Hotspot CPU-on-CPU, Off-CPU/I/O, Allocation, Cache/Branch oder Dispatch?
- Habe ich eine Flamegraph-Zielauswahl mit Criterion/Instruktionszählung bestätigt?

### Speicher

- Welche Callsite erzeugt wie viele Bytes/Blocks, mit welcher Lifetime und Peak-
  Nutzung?
- Ist `Vec` unter-reserviert, überdimensioniert oder durch `SmallVec`/`Cow`/Reuse
  besser repräsentiert?
- Sind `clone`, `to_owned`, `format!`, `lines()` oder Reallocations im Hot Path?
- Welche Hot Types enthalten Padding, große Enum-Varianten oder unnötige Pointer?

### Codegen/Distribution

- Sind `codegen-units`, LTO, Allocator, Linker und `target-cpu` einzeln gemessen?
- Sind PGO-Workloads repräsentativ, Profile aktuell und Flags identisch?
- Werden Debug-Informationen für Profiling erhalten und erst im Artefakt-Schritt
  gestripped?
- Haben `panic=abort`, `no_std`, `no_main`, `repr(packed)` oder Nightly-Flags den
  Sicherheits-/Portabilitätsvertrag verändert?

## Quellen und Aktualität

Verwende für Garantien die [Rust Reference](https://doc.rust-lang.org/stable/reference/type-layout.html)
und die aktuelle [rustc-Codegen-Referenz](https://doc.rust-lang.org/rustc/codegen-options/index.html).
Behandle das [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/) als
fortgeschrittene, ausdrücklich unvollständige Ergänzung; bei Widersprüchen hat
die Reference Vorrang.

Prüfe Version, Plattform und Toolchain vor jeder Übernahme von Zahlen oder
Flags. Das [Criterion-Book](https://bheisler.github.io/criterion.rs/book/),
[cargo-flamegraph](https://github.com/flamegraph-rs/flamegraph),
[`dhat`](https://docs.rs/dhat/latest/dhat/) und
[min-sized-rust](https://github.com/johnthagen/min-sized-rust) entwickeln sich
weiter; aktuelle CLI-/Nightly-Details können von den Beispielen abweichen.
