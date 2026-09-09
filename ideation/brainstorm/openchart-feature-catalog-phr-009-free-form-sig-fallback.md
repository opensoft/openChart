# Free-Form SIG Fallback — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Allows prescribers to enter exceptional directions as free text with explicit provenance, safety checks, and structured limitations.
Topics: openchart-feature-catalog, eprescribing, frappe, free-form-sig
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-009 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Structure-recovery assistant** — A non-autonomous suggestion could propose coded components from free text for prescriber confirmation.

## Focus

This feature isolates the escape hatch for directions that the structured builder cannot faithfully represent. It preserves the fact that text was authored directly and never silently converts suggestions into accepted directions.

## Behavior

- A prescriber may switch to free-form mode after acknowledging loss of structured computability.
- The editor preserves original text, detects prohibited abbreviations, and enforces configured length and character constraints.
- High-risk ambiguity warnings require review and a reasoned override where organization policy permits.
- Any structure-recovery suggestion is visibly machine-generated and requires field-by-field human confirmation.
- Switching back to structured mode never discards free text without explicit confirmation and version evidence.
- The signed prescription identifies the SIG mode and exact rendered text sent to the pharmacy.

## Frappe realization

- **DocTypes:** `OC Prescription SIG` includes `mode`, `free_text`, warning child rows, override reason, and immutable signed rendering.
- **Permissions:** Only `OC Prescriber` may finalize free-form directions; support staff can draft but not clear warnings or sign.
- **Hooks:** Client scripts warn on mode changes; server `validate` applies abbreviation and policy rules consistently across API and Desk.
- **Surfaces:** Composer preview and audit view display author, mode, warnings, overrides, and transmission rendering.

## Boundaries

Owns: exceptional free-text directions and their review evidence. Consumes: site abbreviation policy and medication context. Emits: exact signed SIG text and warnings. Does not own: natural-language clinical interpretation or automatic conversion.

## Open questions

- Which ambiguity checks must block signing and which may allow documented override?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Structured SIG Builder](openchart-feature-catalog-phr-008-structured-sig-builder.md)
