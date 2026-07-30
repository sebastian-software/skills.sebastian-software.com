# Speicher und Datenlayout in Rust

Nutze diese Referenz, wenn ein Profil auf Allokationen, Heap-Spitzen,
Kopierkosten, Objektgröße, Padding, Cache-Misses oder Binary Size zeigt.
Optimiere nie nach einer pauschalen Byte- oder Containerregel: Messe den
konkreten Workload und halte den Layout-/Portabilitätsvertrag fest. Für
Messdesign, Flamegraphs und Compiler-Profile siehe
[Performance and profiling](performance-and-memory.md).

## Inhaltsverzeichnis

- [Arbeitsvertrag: messen, dann layouten](#arbeitsvertrag-messen-dann-layouten)
- [Allokationen und Lebensdauer](#allokationen-und-lebensdauer)
- [Vec, String und Reallocation](#vec-string-und-reallocation)
- [HashMap, HashSet und Hashing](#hashmap-hashset-und-hashing)
- [Box, Rc, Arc, Cow und Kopieren](#box-rc-arc-cow-und-kopieren)
- [Typgrößen, Alignment und Padding](#typgrößen-alignment-und-padding)
- [Layout-Garantien und repr](#layout-garantien-und-repr)
- [Cache-Lokalität: AoS, SoA und Pointer](#cache-lokalität-aos-soa-und-pointer)
- [Dispatch, Monomorphisierung und Codegröße](#dispatch-monomorphisierung-und-codegröße)
- [DHAT für Heap-Regressionen](#dhat-für-heap-regressionen)
- [Binary Size und Build-Artefakte](#binary-size-und-build-artefakte)
- [Safety, Portabilität und Review](#safety-portabilität-und-review)
- [Diagnose-Checkliste](#diagnose-checkliste)
- [Quellen und Aktualität](#quellen-und-aktualität)

## Arbeitsvertrag: messen, dann layouten

1. Definiere zuerst die betroffene Metrik: Peak-Bytes, live Bytes,
   Allokationsanzahl, CPU-Zeit, Cache-Misses oder Artefaktgröße. Eine kleinere
   Struktur ist kein Ziel, wenn sie die relevante Metrik nicht verbessert.
2. Sichere eine Baseline mit identischer Toolchain, Target, Feature-Auswahl,
   Eingabeverteilung und Allocator. Speichere Benchmark-, Heap- und
   Binary-Size-Artefakte.
3. Finde Allokations-Callsites mit einem Profiler und verknüpfe sie mit
   Lifetime/Peak. Zähle nicht nur die Summe: viele kleine kurzlebige Blöcke und
   wenige große langlebige Blöcke brauchen unterschiedliche Lösungen.
4. Ändere Datenstruktur, Ownership und Layout jeweils als isolierte Hypothese.
   Bestätige Laufzeit, Speicher, Codegröße und Wartbarkeit danach erneut.

Das [Rust Performance Book – Benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html)
und der Abschnitt [Heap allocations](https://nnethercote.github.io/perf-book/heap-allocations.html)
geben den Messrahmen vor. Für die Werkzeugschritte siehe
[Performance and profiling](performance-and-memory.md).

## Allokationen und Lebensdauer

Untersuche zuerst, ob eine Heap-Allokation überhaupt notwendig ist:

- Halte Werte auf dem Stack, wenn Größe und Lebensdauer lokal und klein sind.
- Übergib geliehene Slices/Strings (`&[T]`, `&str`), wenn der Aufrufer den
  Speicher besitzt; vermeide dadurch `to_owned`/`clone` an API-Grenzen.
- Nutze `Vec::with_capacity` oder `String::with_capacity`, wenn die erwartete
  Größe aus dem Protokoll, `size_hint` oder einer vorherigen Messung ableitbar
  ist. Reserviere keine unrealistischen Maxima, die Peak-RSS erhöhen.
- Reuse mutable Buffers (`clear` + `extend_from_slice`/`read_to_end`), statt im
  Loop neue Vektoren zu erzeugen. Miss, ob die dadurch verlängerte Lifetime den
  Peak-Heap verschlechtert.
- Vermeide implizite Allokationen in `format!`, `collect`, `lines`,
  `to_string`, `serde_json::to_string` und temporären Adapterketten im Hot Path.

Prüfe mit Heap-Profiling, ob ein Clone für Ownership tatsächlich gebraucht
wird. `clone_from` kann den Zielbuffer wiederverwenden; vergleiche es mit einem
gewöhnlichen `clone`, wenn die Zielgröße stark schwankt.
[Perf Book – Heap allocations](https://nnethercote.github.io/perf-book/heap-allocations.html)

Ordne Allokationen nach Lifetime. Kurzlebige Scratch-Daten können in einem
expliziten Arena-/Bump-Allocator gebündelt werden; langlebige Objekte sollten
keine Arena-Lifetime erzwingen. Führe einen Arena-Allocator nur ein, wenn das
Profil die Freigabe-/Allokationskosten und die Lebensdauerstruktur bestätigt.
Dokumentiere Drop-Semantik, Thread-Verträglichkeit und Fragmentierung.

Behandle den globalen Allocator als Systemgrenze. Ein alternativer Allocator
ändert Fragmentierung, Thread-Contention, RSS und FFI-Verhalten; messe ihn
gegen den Standard-Allocator auf jeder unterstützten Plattform und versioniere
die Auswahl. Vermeide einen Allocator-Wechsel als Ersatz für unnötige Clones.

## Vec, String und Reallocation

Verwende `Vec<T>` als Standard für zusammenhängende Sequenzen. Seine Elemente
liegen contiguous, wodurch sequentielle Iteration und Prefetching gut
funktionieren. Eine `Vec` hält pointer/length/capacity; `len` ist nicht die
reservierte Kapazität. Prüfe `capacity()` im Profil, um Überreservierung und
Reallocations zu unterscheiden.

- Nutze `with_capacity(n)`, wenn `n` belastbar ist.
- Nutze `reserve`/`reserve_exact` bewusst: `reserve` darf geometrisch wachsen
  und amortisiert Reallocation; `reserve_exact` spart potenziell ungenutzten
  Platz, kann aber bei schrittweisem Wachstum mehr Allokationen erzeugen.
- Nutze `shrink_to`/`shrink_to_fit` nur außerhalb kritischer Schleifen und nur,
  wenn die Rückgabe des Speichers den Aufwand rechtfertigt.
- Entferne am Ende mit `truncate` oder `clear`, wenn der Buffer wiederverwendet
  wird. `clear` behält die Kapazität.
- Übergib bekannte Größen über `Iterator::size_hint` oder `ExactSizeIterator`,
  damit `collect`/`extend` sinnvoll reservieren können.

Für Text gelten dieselben Regeln für `String`; vermeide wiederholtes
`format!`/`push_str` ohne Kapazitätsplanung. Bei UTF-8-Protokollen darfst du
`Vec<u8>` und `read_until` verwenden, wenn Validierung erst später notwendig
ist. [Perf Book – I/O](https://nnethercote.github.io/perf-book/io.html)

Verwende `SmallVec` oder ein Inline-Array nur bei gemessenem Small-Size-
Dominanzfall. Inline-Speicher vergrößert jeden Wert und kann bei großen
Elementen/verschachtelten Strukturen den Cache belasten. Dokumentiere den
Inline-Capacity-Vertrag und vergleiche Heap-Allokationen, `size_of::<T>()` und
Iteration separat. [Perf Book – Standard library types](https://nnethercote.github.io/perf-book/standard-library-types.html)

## HashMap, HashSet und Hashing

Nutze `HashMap`/`HashSet` für schnelle durchschnittliche Lookup-Kosten, nicht
für stabile Iterationsreihenfolge oder automatisch minimale Speicherbelegung.
Prüfe im Profil:

- Reserviere Kapazität aus einer belastbaren Schätzung (`with_capacity`), aber
  vermeide pauschales Reservieren in jeder Anfrage.
- Entferne Einträge mit `retain`/`drain`, wenn du die Tabelle als Buffer
  wiederverwendest; entscheide bewusst, ob die Kapazität bleiben soll.
- Verwende einen schnelleren Hasher nur mit bekanntem Threat Model. Viele
  Hashing-Alternativen sind für untrusted Keys anfällig für Hash-Flooding.
- Für Integer-/Enum-Keys kann ein spezialisierter, collision-resistenter
  Hasher schneller sein; belege den Effekt mit adversarialen und normalen Daten.
- Prüfe, ob eine dichte ID-Menge ein `Vec<Option<T>>`, `Vec<T>` plus Bitset oder
  eine sortierte Sequenz statt Hashing erlaubt.

Vergleiche Hash-Funktion, Load-Factor, Keygröße und Cache-Verhalten zusammen;
eine schnellere Hashfunktion macht Pointer-/Bucket-Misses nicht automatisch
billiger. [Perf Book – Hashing](https://nnethercote.github.io/perf-book/hashing.html)

## Box, Rc, Arc, Cow und Kopieren

Wähle Pointer-Container nach Ownership-Vertrag:

- Verwende `Box<T>`, wenn ein Wert bewusst auf den Heap soll (z. B. rekursive
  Typen oder große seltene Varianten). Miss, ob zusätzliche Indirektion den
  Cache-Hot-Path verschlechtert.
- Verwende `Rc<T>` nur single-threaded und `Arc<T>` bei echter geteilter
  Thread-Nutzung. Beide speichern Referenzzählungen und verursachen Indirektion;
  `Arc::clone` ist billig, aber nicht kostenlos.
- Verwende `Cow<'a, [T]>`/`Cow<'a, str>`, wenn der häufige Pfad geliehen bleiben
  kann und Mutationen selten sind. Prüfe, ob der Clone-Fallback im realen
  Workload häufig genug ist.
- Verwende `clone_from` für wiederverwendete Zielwerte; prüfe die Implementierung
  und messe die Kapazitätsreuse.
- Nutze `mem::take`/`mem::replace`, wenn Ownership bewegt werden kann, statt
  eine tiefe Kopie zu erzwingen.

Entferne einen Pointer nicht allein wegen seiner Größe: Er kann Rekursion,
Unvollständigkeit (`dyn Trait`, DST) oder stabile Adressen ermöglichen. Bewerte
immer Indirektion, Allokationszahl und Zugriffsmuster gemeinsam.

## Typgrößen, Alignment und Padding

Miss Layout an den konkreten Zieltargets:

```rust
use std::mem::{align_of, size_of};

const _: () = {
    let _ = size_of::<MyType>();
    let _ = align_of::<MyType>();
};
```

Nutze zur Diagnose `std::mem::size_of::<T>()` und `align_of::<T>()` in einem
kleinen Tool oder Test. Für eine Feldübersicht verwende auf Nightly
`rustc -Zprint-type-sizes` nur diagnostisch; das Ausgabeformat ist kein
stabiler Build-Vertrag. [Perf Book – Type sizes](https://nnethercote.github.io/perf-book/type-sizes.html)

Erwarte Padding, wenn ein Feld eine höhere Alignment-Anforderung als das
vorherige Feld hat. Ordne Felder nicht manuell um, solange kein Vertrag und
keine Messung vorliegen: Bei `repr(Rust)` ist die konkrete Feldreihenfolge nicht
als ABI-Garantie zugesichert. Nutze `repr(C)` für FFI/externen Layout-Vertrag
und prüfe die resultierende Größe auf allen Targets. [Rust Reference – Type layout](https://doc.rust-lang.org/stable/reference/type-layout.html)

Behandle „große Typen“ als Workload-/Target-Frage. Eine Schwelle wie 128 Byte
kann ein Anlass sein, Kopierkosten zu messen, ist aber keine Rust-Garantie.
Miss `memcpy`/Move-Kosten, Registerdruck, Stack-Nutzung und Cache-Effekt, bevor
du boxst oder Felder aufteilst.

Reduziere Größe mit belegbaren Maßnahmen:

- Ersetze breite Zustandsfelder nur, wenn Wertebereich, Overflow-Vertrag und
  FFI/Serialization dies erlauben.
- Packe Bool-/Enum-Zustände in einen repräsentationsstabilen Bitset nur, wenn
  zusätzliche Maskenoperationen nicht den Hot Path verschlechtern.
- Prüfe große Enum-Varianten: `Box` kann den Enum verkleinern, fügt aber eine
  Allokation/Indirektion hinzu.
- Miss `size_of` von Container-Elementen und die Gesamt-Heap-Belegung; ein
  kleinerer Header kann durch mehr externe Allokationen verlieren.

## Layout-Garantien und repr

Halte dich an die [Rust Reference – Type layout](https://doc.rust-lang.org/stable/reference/type-layout.html):

- `repr(Rust)` garantiert Feld-Alignment, dass Felder nicht überlappen und der
  Typ passend ausgerichtet ist; konkrete Reihenfolge, Padding und Nischen-
  Optimierungen sind kein allgemeiner ABI-Vertrag.
- `repr(C)` legt die C-kompatible Reihenfolge/Alignment-Regeln fest. Verwende es
  für FFI, Shared-Memory-Formate und explizite Layout-Tests; es macht einen Typ
  nicht automatisch insgesamt FFI-sicher (z. B. `String`/`Vec` bleiben Rust-
  Ownership-Typen).
- Primitive `repr(u8)`/`repr(u16)` usw. stabilisieren die Enum-Diskriminante,
  nicht automatisch jedes Padding oder alle Variantendaten.
- Kombiniere `repr(C, u8)`/`repr(C, u16)` nur mit einem dokumentierten externen
  Format und teste Size/Align/Offset gegen die Gegenstelle.
- Verwende `repr(transparent)` für den dokumentierten Single-Field-Wrapper-
  Vertrag, etwa FFI-Newtypes.
- Vermeide `repr(packed)` als Größenoptimierung. Unaligned-Referenzen sind
  Undefined Behavior; greife über `addr_of!` + `read_unaligned`/`write_unaligned`
  oder kopiere in ein ausgerichtetes temporäres Objekt. Siehe
  [Rustonomicon – Working with unsafe](https://doc.rust-lang.org/stable/nomicon/working-with-unsafe.html).

Dokumentiere bei jeder Layout-Abhängigkeit: Target-Architektur, `repr`,
Alignment, Feld-Offsets, Endianness, Serialisierungsformat und Upgrade-Plan.
Verwende Compile-Time-Assertions nur für absichtlich stabilisierte Verträge;
vermeide Assertions auf zufällige `repr(Rust)`-Details.

Für Pointer-/DST-Layout gilt: Thin Pointer (`&T`, `Box<T>`) und fat Pointer
(`&[T]`, `&dyn Trait`) haben unterschiedliche Metadaten. Leite ihre Größe nicht
aus einer zufälligen Implementierung ab; `size_of_val` misst den konkreten
Wert, nicht ein dauerhaftes ABI. [Rust Reference – Dynamically Sized Types](https://doc.rust-lang.org/stable/reference/dynamically-sized-types.html)

## Cache-Lokalität: AoS, SoA und Pointer

Ordne Daten nach Zugriffsmuster, nicht nach ästhetischer Feldgruppierung:

- **AoS (Array of Structs):** Wähle es, wenn jeder Schritt fast alle Felder
  eines Objekts benötigt oder du stabile Objektgrenzen brauchst.
- **SoA (Structure of Arrays):** Wähle es, wenn ein Hot Loop nur wenige Felder
  über viele Objekte verarbeitet. Die aktiven Spalten bleiben dicht und
  reduzieren Cache-Traffic; halte Längen/Indizes synchron.
- **AoSoA/Chunking:** Prüfe es bei SIMD-/Cache-Kachelgrößen, wenn reine SoA-
  oder AoS-Layouts unpraktisch sind.
- **Pointer-rich Graphen:** Ersetze `Box`/`Rc`-Ketten nicht blind. Prüfe, ob
  Arena + Index oder eine `Vec<Node>` die Zugriffslokalität verbessert und wie
  sich Stable-Address-/Deletion-Anforderungen ändern.

Messe LLC/L1-Misses, Branch-Misses und Wall-Time mit realistischen Datensätzen.
Ein SoA-Layout kann zusätzliche Indexberechnungen, Scatter/Gather oder
Synchronisationskosten erzeugen; akzeptiere es nur bei positiver Gesamtbilanz.
[Data-Oriented Design in Rust](https://jamesmcm.github.io/blog/intro-dod/)

Vermeide `LinkedList` für normale Sequenzen: Jeder Schritt kann eine
Pointer-Indirektion und Cache-Miss kosten. Bevorzuge `Vec`, `VecDeque` oder eine
Indexstruktur und begründe Ausnahmen mit gemessenen Insert/Remove-Anforderungen.
[Perf Book – Standard library types](https://nnethercote.github.io/perf-book/standard-library-types.html)

## Dispatch, Monomorphisierung und Codegröße

Verwende statische Generics (`impl Trait`, generische Funktionen), wenn
Hot-Path-Dispatch und Inlining zählen und die Code-Vervielfachung akzeptabel
ist. Verwende `dyn Trait`, wenn viele Implementierungen selten aufgerufen
werden, Binärgröße/Compile-Zeit wichtiger sind oder Plugin-Grenzen gebraucht
werden. Miss beide Varianten; eine Vtable-Indirektion kann Branch-/Cache-
Kosten verursachen, Monomorphisierung kann den Instruction-Cache aufblasen.
[Data-Oriented Design – Static vs dynamic dispatch](https://jamesmcm.github.io/blog/intro-dod/)

Teile generische Hot-Codepfade in kleine, wiederverwendbare Funktionen, wenn
Compiler-Explorer/`cargo asm` eine relevante Codeexplosion zeigt. Prüfe
`cargo bloat`/`cargo llvm-lines`, um Monomorphisierungs- und Inline-Treiber zu
identifizieren; entferne keine Abstraktion ohne Größen-/Laufzeitmessung.

## DHAT für Heap-Regressionen

Setze `dhat-rs` feature-gated ein, damit Produktionsbuilds keinen Profiling-
Allocator enthalten:

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

Starte den diagnostischen Build in Release-Konfiguration und verwende eine
repräsentative Eingabe. Für automatisierbare Grenzen nutze
`Profiler::builder().testing().build()` und prüfe `HeapStats` wie
`total_bytes`, `total_blocks`, `max_bytes` und `max_blocks`.
[DHAT-rs – Configuration and setup](https://docs.rs/dhat/latest/dhat/#configuration-profiling-and-testing),
[DHAT-rs – Heap usage testing](https://docs.rs/dhat/latest/dhat/#heap-usage-testing)

Markiere seltene, semantische Ereignisse mit `dhat::ad_hoc_event(weight)`,
wenn die Allokation selbst nicht aussagekräftig ist. Halte den Profiler über
den gesamten relevanten Scope; eine zu kurze Lifetime verschiebt die
Interpretation. DHAT ist laut Crate-Dokumentation experimentell und kann
Performance/Timing stark verändern. [DHAT-rs](https://docs.rs/dhat/latest/dhat/)

## Binary Size und Build-Artefakte

Definiere ein Größenbudget und miss das finale, stripbare Artefakt (`ls -lh`,
`size`, Plattformtool) getrennt vom Debug-/Profiling-Build. Nutze
[`cargo bloat`](https://github.com/RazrFalcon/cargo-bloat) oder
[`cargo llvm-lines`](https://github.com/dtolnay/cargo-llvm-lines), um große
Funktionen und generische Vervielfachung zuzuordnen.

Beginne mit einem reproduzierbaren Release-Profil:

```toml
[profile.release]
opt-level = "z"       # alternativ "s" oder 3; messen
lto = true            # thin/fat vergleichen
codegen-units = 1
panic = "abort"      # nur wenn der API-/FFI-Vertrag dies erlaubt
strip = "symbols"    # nach Profiler-/Debug-Läufen
```

Wähle `opt-level = "s"` oder `"z"` nach Messung; `"z"` ist nicht garantiert
kleiner oder schneller als `"s"`. `lto = "thin"` kann einen besseren
Größen-/Linkzeitkompromiss als fat LTO liefern. `codegen-units = 1` kann
Optimierung und Größe verbessern, erhöht aber Compile-Zeit. [rustc Codegen options](https://doc.rust-lang.org/rustc/codegen-options.html),
[min-sized-rust](https://github.com/johnthagen/min-sized-rust#optimize-for-size)

Behalte für Profiling einen separaten Build mit `debug = "line-tables-only"`
oder `debug = true`; strippe erst beim Release-Artefakt. Prüfe, ob Panic-
Strings, Backtraces, Formatierungs-/Logging-Code, ungenutzte Features und
Monomorphisierung den größten Anteil ausmachen.

Erwäge `no_std`/`no_main` nur für passende Embedded-/Runtime-Verträge.
`panic = "abort"`, Entfernen von Unwind-/Backtrace-Code oder aggressive
Linker-Garbage-Collection verändern Fehlerdiagnose und Bibliotheksgrenzen.
Prüfe mit Cross-Target-CI, ob jedes Artefakt weiterhin startet und FFI-Symbole
korrekt exportiert.

Verwende UPX/Kompression nur, wenn Startzeit, Plattformregeln, Signaturen und
Deployment dies erlauben; messe die Größe des verpackten und entpackten
Artefakts und dokumentiere den Release-Schritt. [min-sized-rust – Compressing](https://github.com/johnthagen/min-sized-rust#compressing)

## Safety, Portabilität und Review

- Behandle `repr(packed)`, `read_unaligned`, `get_unchecked`, Transmute,
  rohe Pointer und eigene Allocatoren als Unsafe-Proof-Obligations. Dokumentiere
  Provenienz, Initialisierung, Alignment, Bounds, Aliasing, Lifetimes, Drop,
  Unwind und Thread-Safety; siehe [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/).
- Liefere `target-cpu=native`/`target-feature` nur, wenn alle Nutzer die
  CPU-Anforderungen erfüllen. Für portable SIMD nutze Feature Detection oder
  mehrere Implementierungen; siehe [rustc target features](https://doc.rust-lang.org/rustc/codegen-options.html#target-feature).
- Kopple Layout-Assertions an ein explizites `repr` und Target. Teste
  Endianness, Pointerbreite, Alignment und externe Serialisierung auf allen
  Zielplattformen.
- Trenne diagnostische Flags (DHAT, PGO-Instrumentierung, Nightly-
  `-Zprint-type-sizes`) von Produktionsprofilen. Prüfe Toolchain-/Crate-Versionen
  bei jedem Upgrade.

## Diagnose-Checkliste

- Welche Allokations-Callsite verursacht Peak-Bytes und welche Lifetime hat sie?
- Ist die Kapazität von `Vec`/`String` zu klein, zu groß oder wiederverwendbar?
- Entsteht der Aufwand durch `clone`, `to_owned`, `collect`, `format!`,
  `Box`/`Arc`-Indirektion oder Hashing?
- Sind `size_of`, `align_of` und Feld-Padding auf allen Targets bekannt?
- Passt AoS/SoA/Chunking zum tatsächlichen Feldzugriff und Cache-Profil?
- Ist statischer Dispatch eine gemessene Code-/Cache-Verbesserung oder nur eine
  Annahme?
- Welche Änderung reduziert die gemessene Binary-Size-Komponente tatsächlich?
- Sind Unsafe-/FFI-/CPU-Feature-Verträge und Fallbacks dokumentiert und getestet?

## Quellen und Aktualität

Verwende die [Rust Reference](https://doc.rust-lang.org/stable/reference/type-layout.html)
für Layoutgarantien und die [Rustonomicon](https://doc.rust-lang.org/stable/nomicon/)
für Unsafe-Grundlagen. Die [Rust Performance Book](https://nnethercote.github.io/perf-book/)
liefert praxisnahe Heuristiken zu Allokationen, Typgrößen, Standardcontainern
und Hashing. Ergänze sie bei Datenlayout-Fragen mit
[Data-Oriented Design in Rust](https://jamesmcm.github.io/blog/intro-dod/), bei
Heap-Regressions mit [DHAT-rs](https://docs.rs/dhat/latest/dhat/) und bei
Binary-Size-Fragen mit [min-sized-rust](https://github.com/johnthagen/min-sized-rust).

Prüfe alle CLI-Flags, Crate-Versionen und Plattformannahmen gegen die aktuelle
Toolchain. Zahlen/Schwellenwerte aus Blogposts sind Startpunkte für Messungen,
keine stabilen Rust-Garantien.
