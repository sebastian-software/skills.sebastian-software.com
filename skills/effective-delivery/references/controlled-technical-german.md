# Controlled Technical German

Use this reference for German technical documentation when the user or project
asks for tekom-style rule-based writing, controlled or standardized German,
translation-oriented German, or a durable editorial profile. Optimize for
precise, natural Standard German that proficient readers can read comfortably.
Do not make Einfache Sprache or Leichte Sprache the default.

## Contents

- [Select the language profile](#select-the-language-profile)
- [Establish the editorial contract](#establish-the-editorial-contract)
- [Use the default technical-German profile](#use-the-default-technical-german-profile)
- [Apply German-specific rules](#apply-german-specific-rules)
- [Write by information type](#write-by-information-type)
- [Author and review in passes](#author-and-review-in-passes)
- [Report assurance honestly](#report-assurance-honestly)
- [Typical references](#typical-references)

## Select the language profile

Use the narrowest profile that meets the audience need:

| Profile | Use |
| --- | --- |
| Natural technical German | Improve clarity while preserving the repository's established voice and terminology. |
| Rule-based technical German | Apply an adopted tekom-based editorial guide, terminology database, and repeatable sentence and structure rules. |
| Einfache Sprache | Apply DIN 8581-1 or ISO 24495-1 only when the audience, contract, or accessibility goal requires this profile. |
| Leichte Sprache | Treat as a separate accessibility and audience requirement. Do not infer it from a general request for clear technical text. |

For experienced technicians, engineers, administrators, and software users,
prefer rule-based technical German. Permit necessary Fachbegriffe, useful
subordinate clauses, cohesive paragraphs, and normal sentence variation.

## Establish the editorial contract

Determine:

1. audience knowledge, task, reading environment, and translation needs;
2. the implemented product behavior or approved engineering source;
3. the selected tekom guide edition and the rules the project adopted;
4. the approved terminology database, abbreviations, and product names;
5. applicable information, safety, regulatory, and house-style standards; and
6. the required technical, editorial, terminology, and usability reviews.

Treat the tekom publication as a practice guide from which a project establishes
its editorial rules. Do not imply a universal tekom conformity label. If no
project profile exists, apply the default below, mark it as a proposed profile,
and keep project-specific decisions visible.

Apply sources in this order:

1. Engineering sources own meaning, values, conditions, sequence, and hazards.
2. Product terminology owns preferred designations and literal interface text.
3. The adopted editorial guide owns language and structure rules.
4. Product-information and safety standards own required content and
   presentation.
5. General language and typography rules control only the remaining choices.

## Use the default technical-German profile

### Require precision and consistency

- Use one preferred designation for each concept. Do not rotate synonyms for
  stylistic variety.
- Preserve necessary technical terms. Define an unfamiliar term at its first
  useful occurrence instead of replacing it with an inaccurate everyday word.
- Preserve commands, code, API names, configuration keys, UI labels, part
  numbers, quoted output, legal text, and approved safety wording exactly.
- Define abbreviations before use unless the audience and project approve them
  as common knowledge.
- Keep units, numbers, identifiers, capitalization, and spelling consistent
  with the project convention.

### Make actions and logic explicit

- Use the imperative for direct instructions: `Schließen Sie Ventil V1.`
- Put a condition or prerequisite before the action when readers must know it
  first: `Wenn der Druck unter 2 bar liegt, schließen Sie Ventil V1.`
- Give one primary action per numbered step. Keep actions together only when
  they must occur simultaneously or form one indivisible operation.
- Name the actor in descriptive text when responsibility matters.
- Put the main statement early. Split a sentence when readers must retain
  several nested conditions before reaching the action.
- Use references such as `dies`, `diese`, `dabei`, or `hierzu` only when their
  antecedent is unmistakable.

### Keep the prose natural

- Permit subordinate clauses when they express cause, condition, purpose,
  sequence, or contrast more clearly than separate fragments.
- Vary sentence length in descriptive passages. Use short sentences for
  critical actions, not as a mechanical rhythm for every paragraph.
- Use connectors to show the relationship between statements.
- Permit passive voice in descriptions when the actor is unknown or irrelevant.
  Prefer active voice when responsibility or sequence matters.
- Keep a coherent paragraph for one topic. Do not turn every proposition into a
  separate heading, bullet, or one-line paragraph.
- Use lists when order, alternatives, prerequisites, or comparison become
  clearer, not merely to avoid prose.

### Remove avoidable difficulty

- Replace heavy nominal constructions with direct verbs when meaning stays the
  same.
- Reduce stacked premodifiers and long noun groups. Introduce the main noun and
  express relationships with a preposition or a separate clause.
- Remove filler, redundant doublets, vague intensifiers, idioms, and internal
  jargon that the audience does not need.
- Avoid parentheses inside parentheses and qualifications that interrupt the
  main action.
- Do not impose a universal word limit. Treat length and clause depth as review
  signals; rewrite when the reader must hold too many relations at once.

## Apply German-specific rules

### Control modality

Use modal language consistently with the product contract:

- `muss` identifies a requirement;
- `darf nicht` identifies a prohibition;
- `sollte` identifies a recommendation only when the project uses it that way;
- `kann` identifies capability or possibility, not permission by default.

Do not weaken a requirement into a recommendation during editing. Avoid
ambiguous combinations such as `sollte möglichst` when a precise requirement or
an explicit option is intended.

### Control compounds and hyphens

Use the approved German compound when it is a recognized technical term. Add a
hyphen when it makes the relationship or a mixed alphanumeric expression
clearer, but do not invent changing spellings for the same concept. Break up a
long compound only when the result remains terminologically correct.

### Control sentence brackets

Keep the finite verb and its important complement close enough that readers can
recognize the action without retaining a long middle field. Prefer a direct
verb over `Die Durchführung der Prüfung erfolgt ...` constructions.

### Apply inclusive language deliberately

Follow the project's audience, legal, accessibility, and house-style policy.
Prefer clear role names and consistent formulations. Do not trade technical
precision or scanability for ad hoc variation.

## Write by information type

### Procedures

State the goal and prerequisites before the steps. Use ordered steps for
sequence, imperatives for actions, explicit conditions, observable results, and
real recovery paths. Keep explanatory background outside the action sequence
unless the reader needs it to act safely.

### Descriptions

Introduce the system or concept before details. Give each paragraph one topic,
use stable terminology, and show causal or functional relationships explicitly.
Do not force descriptions into imperative fragments.

### Safety information

Derive severity, signal word, hazard, consequence, avoidance action, and
placement from the approved risk assessment and applicable product standard.
Language simplification must not change or hide the risk.

### Software and interface documentation

Keep literal interface strings and executable examples unchanged. Apply the
German profile to surrounding prose. Verify commands, configuration, outputs,
links, and examples independently from the language review.

## Author and review in passes

1. Extract actor, action, object, condition, limit, sequence, result, and hazard
   from the authoritative source.
2. Classify content as procedure, description, reference, note, or safety
   information.
3. Resolve terminology before polishing sentences. Record unresolved concepts.
4. Rewrite for explicit logic, controlled modality, and natural reading flow.
5. Compare the result with the source so that no technical proposition changes.
6. Search for terminology variants, undefined abbreviations, ambiguous
   references, nominal constructions, deep nesting, and altered literals.
7. Run repository-native example, schema, link, build, and documentation checks.
8. Obtain the required technical and editorial review. Use representative
   audience testing when comprehension or safe task completion is consequential.

Read the text aloud as a final naturalness check. A rule-based result can still
fail if every sentence has the same clipped rhythm.

## Report assurance honestly

Report the selected tekom edition or house guide, adopted rule profile, term-base
version, content scope, manual and automated checks, deviations, unresolved
terms, and reviewer status.

Use `tekom-informed` when only the practice guide shaped the edit. Claim review
against a project profile only when that profile and the reviewed scope are
identified. Do not equate a spelling, terminology, or readability checker with
a complete editorial review.

## Typical references

- [tekom: Deutsch für die Technische Kommunikation — Regelbasiertes Schreiben, 3. Auflage (2026)](https://www.tekom.de/services-unsere-angebote/publikationen/fachbuecher/detail/deutsch-fuer-technische-kommunikation-regeln-und-ihre-anwendung)
- [DIN EN IEC/IEEE 82079-1:2021-09 — Erstellung von Nutzungsinformationen](https://www.dinmedia.de/de/norm/din-en-iec-ieee-82079-1/342226844),
  the German adoption of IEC/IEEE 82079-1
- [DIN 8581-1:2024-05 — Einfache Sprache, Anwendung für das Deutsche](https://www.dinmedia.de/de/norm/din-8581-1/377238273)
- [ISO 24495-1:2023 — plain-language principles and guidelines](https://www.iso.org/standard/78907.html)
- [ISO 704:2022 — terminology work principles and methods](https://www.iso.org/standard/79077.html)
- [ISO 1087:2019 — terminology work and terminology science vocabulary](https://www.iso.org/standard/62330.html)
- [ISO 20607:2019 — machinery instruction-handbook principles](https://www.iso.org/standard/68519.html)

Verify the applicable edition, license, product-specific standards, and project
adoption before claiming that the text satisfies a named requirement.
