# ASD-STE100 Simplified Technical English

Use this reference to author or review English technical documentation when the
user, project, contract, or governing publication standard requires
ASD-STE100. STE controls language. It does not establish technical correctness,
document structure, hazard severity, or product behavior.

## Contents

- [Select the English profile](#select-the-english-profile)
- [Establish the STE contract](#establish-the-ste-contract)
- [State the level of assurance](#state-the-level-of-assurance)
- [Apply sources in the correct order](#apply-sources-in-the-correct-order)
- [Author in passes](#author-in-passes)
- [Do not conflate adjacent standards](#do-not-conflate-adjacent-standards)
- [Typical references](#typical-references)

## Select the English profile

- Use `effective-writing` for relaxed Slack, GitHub, Linear, PR, and internal team
  communication.
- Use the Technical Documentation route workflow for clear technical English
  when no controlled-language standard applies.
- Use this reference when ASD-STE100 or another explicit controlled-English
  contract applies.

Do not import Metro-English contractions, casual rhythm, or conversational
alternatives into STE text. A team message about an STE document can use
`effective-writing`; the controlled document itself cannot.

## Establish the STE contract

Determine these inputs before making a conformance claim:

1. the required ASD-STE100 issue and release date;
2. the exact document, sections, and text types in scope;
3. the implemented product behavior or approved engineering source;
4. the project glossary or terminology database for technical nouns and
   technical verbs;
5. the governing publication, safety, regulatory, and house-style directives;
   and
6. the required review and acceptance process.

Issue 9, dated 2025-01-15, is the baseline for this reference. Verify the
current issue on the official STEMG site before new compliance work. Preserve a
project's mandated older issue when compatibility or a contract requires it,
and report the difference.

Do not store or redistribute an unofficial copy of the standard or its
dictionary. Use the official distribution channel. If the selected standard,
dictionary, or project term base is unavailable, make an STE-informed edit and
state which conformance checks remain open.

## State the level of assurance

Use a claim that matches the evidence:

| Claim | Required evidence |
| --- | --- |
| STE-informed | Apply selected STE clarity patterns without asserting compliance. |
| Authored for a named STE issue | Use that issue's writing rules and dictionary plus the approved project terminology. Record unresolved terms and deviations. |
| Reviewed against a named STE issue | Check all in-scope prose against the named rules, dictionary, terminology, and project directives. Record the review scope and results. |

Do not call a text, checker, AI system, trainer, or workflow ASD-certified or
ASD-endorsed without direct authorization from ASD. A checker is an aid, not
evidence that replaces the standard, technical knowledge, or human review.

## Apply sources in the correct order

Keep these concerns separate:

1. Product and engineering sources own technical meaning, values, sequence, and
   behavior.
2. The project contract identifies the applicable STE issue and any approved
   deviations.
3. The official STE writing rules and dictionary control the English prose.
4. The project term base controls subject-field technical nouns and verbs.
5. Publication and safety standards control information models, signal words,
   layout, and hazard classifications.
6. House style controls only choices that the higher-priority sources leave
   open.

Do not use STE to repair uncertain engineering content. Resolve the technical
uncertainty first. Do not silently lower or invent a hazard classification to
make a sentence easier to write.

## Author in passes

### 1. Preserve the technical proposition

Extract the actor, action, object, conditions, limits, sequence, result, and
hazard consequence from the authoritative source. Keep a comparison copy so
that language editing cannot remove a requirement or change causality.

Classify each passage as procedural, descriptive, a note, or a safety
instruction. Apply the matching rules instead of forcing all content into
imperative steps.

### 2. Normalize terminology

- Use one approved technical noun for one item or concept throughout the
  document.
- Use an approved general word when it expresses the meaning accurately.
- Classify a subject-field word as a technical noun or technical verb only when
  it fits the applicable STE category and the project approves it.
- Prefer short, recognizable terms. Reject slang, regional language, and
  unexplained internal jargon.
- Do not treat every unknown or unapproved word as a technical term merely to
  bypass the dictionary.
- Use American English spelling unless an official project directive requires
  a different spelling.

Record term, concept, part of speech, approved form, source, and status for each
project-specific decision. Reuse an existing terminology database instead of
creating a parallel glossary.

### 3. Apply the rule groups

Use this map as a working checklist, not as a substitute for the full rules:

| Issue 9 section | Working decisions |
| --- | --- |
| 1 — Words | Use dictionary words only with their approved meaning, part of speech, and form. Control technical nouns and verbs through the project term base. Keep terminology consistent. |
| 2 — Multi-word nouns | Prefer groups of no more than three words. For a longer official technical noun, write it in full first and use the clarification methods permitted by the standard. |
| 3 — Verbs | Use permitted simple forms and tenses. Prefer active voice; use passive voice in descriptive text only when the agent is unknown. Use `-ing` forms only in the permitted technical-noun roles. Describe actions with verbs and avoid complex auxiliary constructions. |
| 4 — Sentences | Write complete, short sentences. Do not use contractions or omit necessary words. Use vertical lists for complex information, clear connectors for related ideas, and articles or demonstratives where they prevent ambiguity. |
| 5 — Procedures | Keep a sentence to 20 words or fewer. Put one instruction in each sentence unless actions occur at the same time. Use the imperative. Put a condition the reader must know first before the command. Keep instructions out of notes. |
| 6 — Descriptions | Give information gradually and keep a sentence to 25 words or fewer. Give each paragraph one topic and no more than six sentences. Use key terms and phrases to expose the logical structure. |
| 7 — Safety instructions | Use the signal word or symbol required by the applicable domain. Start with a clear command or condition, then state the risk or possible result. Preserve the approved hazard analysis and severity. |
| 8 — Punctuation and word count | Do not use semicolons. Use hyphens and parentheses only for their permitted purposes. Count words with the STE rules, including the special treatment of list colons, parenthetical text, numbers with units, identifiers, quoted text, proper nouns, and hyphenated groups. |
| 9 — Writing practices | Restructure a sentence when a word-for-word substitution changes or obscures the meaning. Use approved words in valid combinations, avoid phrasal verbs, keep wording consistent, and make pronoun references unambiguous. |

Check the official issue when applying any exception or edge case. A normal
token counter does not implement the STE word-count rules.

### 4. Preserve literal technical text

Do not rewrite commands, code, API names, configuration keys, filenames, part
numbers, UI labels, quoted output, or legally fixed text. Mark literal content
with the repository's established code or quotation format and apply STE to the
surrounding prose.

Keep examples executable. A linguistically simpler command that the product
does not support is incorrect documentation.

### 5. Verify in separate passes

Perform and report these checks:

1. **Meaning:** Compare the result with the engineering source. Confirm actors,
   conditions, values, sequence, results, and hazards.
2. **Vocabulary:** Check every in-scope prose word against the selected issue's
   dictionary for meaning, part of speech, and form. Resolve unknown words
   through the approved terminology process.
3. **Rules:** Review each sentence against the applicable procedural,
   descriptive, safety, punctuation, and word-count rules.
4. **Consistency:** Search for alternate terms, spelling variants, ambiguous
   pronouns, and changed interface literals.
5. **Document behavior:** Run the repository's example, link, build, schema,
   doctest, or interface checks independently of the language review.
6. **Acceptance:** Obtain the project-required technical and language review
   for safety-critical or contractually conforming content.

When a checker is available, configure it with the selected STE issue and
approved project terminology. Review each finding in context and record
material false positives, false negatives, and ignored text classes.

Report the selected issue, scope, term-base version, manual checks, automated
checks, deviations, unresolved findings, and final assurance level. If the
evidence is incomplete, use wording such as `STE-aligned draft; full
ASD-STE100 Issue 9 conformance was not verified`.

## Do not conflate adjacent standards

- Plain language can improve audience fit and document design, but plain
  language alone is not ASD-STE100 compliance.
- S1000D and ATA iSpec 2200 can control publication structure and data
  exchange. They do not replace the STE writing rules and dictionary.
- A safety-sign or machinery standard can control signal words, symbols, and
  hazard presentation. STE controls how the related English text is written.
- Readability scores and sentence-length checks do not verify vocabulary,
  approved meanings, terminology, or the full writing rules.

## Typical references

Start with the official ASD sources:

- [ASD-STE100 downloads and current issue](https://www.asd-ste100.org/STE_downloads.html)
- [STEMG overview of STE and Issue 9](https://www.asd-ste100.org/about_STE.html)
- [Official STE frequently asked questions](https://www.asd-ste100.org/STE_faq.html)
- [Official guidance on STE checking tools](https://www.asd-ste100.org/STEsoftware.html)

Add only the companion standards required by the document contract:

- [ISO 1087:2019 — terminology work and terminology science vocabulary](https://www.iso.org/standard/62330.html)
- [ISO 704:2022 — terminology work principles and methods](https://www.iso.org/standard/79077.html)
- [IEC/IEEE 82079-1:2019 — preparation of information for use](https://www.iso.org/standard/71620.html)
- [ISO 24495-1:2023 — plain-language principles and guidelines](https://www.iso.org/standard/78907.html)
- [S1000D — international specification for technical publications](https://s1000d.org/)
- [ATA iSpec 2200 — aviation maintenance information standards](https://ataebiz.org/standards/)
- [ISO 3864-1 — design principles for safety signs and markings](https://www.iso.org/standard/51021.html)
- [ANSI Z535 safety signs and labels](https://webstore.ansi.org/industry/safety-standards/safety-signs-labels)
- [ISO 20607:2019 — machinery instruction-handbook principles](https://www.iso.org/standard/68519.html)

Confirm the applicable edition and access rights for each project. A citation
to a companion standard is not evidence that its requirements were reviewed.
