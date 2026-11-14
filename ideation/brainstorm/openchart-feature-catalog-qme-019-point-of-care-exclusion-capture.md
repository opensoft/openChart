# Point Of Care Measure Exclusion Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians document measure-specific exclusion evidence during care with coded reasons, supporting facts, and bounded applicability.
Topics: openchart-feature-catalog, quality-reporting, frappe, exclusion-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-019 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Contextual candidate prompt** — Present a non-blocking exclusion form only when current evidence suggests a permitted criterion.

## Focus

Clinician-authored exclusion evidence captured in workflow without letting reporting incentives create unsupported clinical facts.

## Behavior

- A clinician opens an eligible measure context and chooses an approved exclusion reason from the active measure release.
- The form requires supporting clinical fact, encounter, onset/effective date, applicability period, and author attestation.
- Free-text alone cannot satisfy a coded criterion when the specification requires structured evidence.
- The clinician may save not-applicable, uncertain, or declined-to-document states without forcing an exclusion.
- Accepted evidence remains a clinical assertion with provenance and follows succession-based amendment rules.
- Measure calculation determines whether the evidence satisfies the active criterion; capture does not guarantee exclusion.
- Expired, contradicted, or superseded evidence is visible and prompts review rather than silent reuse.

## Frappe realization

- **DocTypes:** Add `OC Measure Exclusion Evidence` with patient, encounter, measure criterion, coded reason, source links, effective dates, status, and succession fields.
- **Workflow:** Use draft, clinician-signed, review-required, accepted, rejected, and superseded states where policy requires review.
- **Permissions and client:** Restrict signing to `OC Clinician`; provide a non-blocking encounter client dialog filtered to active criteria.
- **API and hooks:** Guard writes under `open_chart.api.v1.quality.record_exclusion_evidence` and queue recalculation after acceptance or succession.

## Boundaries

Owns: measure-context exclusion evidence capture. Consumes: active criteria, encounters, accepted clinical facts, and clinician authority. Emits: provenance-bearing evidence and recalculation events. Does not own: final measure classification or autonomous clinical prompting.

## Open questions

- Which exclusion assertions should become reusable clinical records beyond the originating measure context?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
