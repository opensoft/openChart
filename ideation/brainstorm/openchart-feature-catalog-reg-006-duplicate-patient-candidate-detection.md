# Duplicate Patient Candidate Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Scores and explains possible duplicate patients before creation so staff can reuse or review records instead of fragmenting charts.
Topics: openchart-feature-catalog, registration, frappe, duplicate-detection
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-006 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Match-quality tuning dashboard** — Measure false positives and missed matches using resolved cases.

## Focus

Detect candidates and explain matching evidence without performing an autonomous merge.

## Behavior

- Candidate detection runs before patient creation and on material identity changes.
- Deterministic identifiers and configurable fuzzy name, birth-date, address, and contact signals contribute to a score.
- Results show matched and conflicting fields rather than only a percentage.
- Exact conflicts on protected identifiers force review even when other fields match.
- Staff may select an existing patient, continue with documented reason, or send candidates to review.
- The system never merges, suppresses, or rewrites a chart based only on a score.

## Frappe realization

- **DocTypes:** `OC Duplicate Candidate Set` and child `OC Duplicate Candidate` with signals, score, threshold band, and disposition.
- **Workflow:** Open → Existing Patient Selected, New Patient Justified, or Review Required → Resolved.
- **Roles/permissions:** `OC Registration Clerk` views candidates; `OC Identity Reviewer` resolves ambiguous sets; matching configuration is System Manager-only.
- **API/surfaces:** `open_chart.api.v1.registration.find_duplicates`; pre-create modal, identity review worklist, and Script Report for thresholds.

## Boundaries

Owns: candidate generation and disposition. Consumes: normalized identity facts and identifiers. Emits: explained match candidates and review tasks. Does not own: merge execution.

## Open questions

- Which fields may participate in fuzzy matching under each jurisdiction's privacy rules?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
