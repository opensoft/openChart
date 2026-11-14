# Telehealth-Specific Intake Forms — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Collects versioned clinical and operational telehealth intake before join and routes concerning answers for human review.
Topics: openchart-feature-catalog, telehealth, frappe, telehealth-intake
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-034 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Service-specific intake packs** — Compose reviewed forms for primary care, dermatology, therapy, urgent care, or follow-up visits.

## Focus

This feature isolates pre-join telehealth intake content and completion state without duplicating the longitudinal chart.

## Behavior

- The patient receives the effective intake pack for service, modality, age, language, and appointment context.
- Forms may collect reason for visit, symptom updates, medications, allergies, location, callback, accessibility, and technology needs.
- Drafts save securely and show completeness, required fields, and a clear distinction between reported facts and clinician findings.
- Submission freezes the response version and routes configured concern flags to qualified staff for human review.
- A flagged answer may block admission only when an explicit reviewed policy and authorized decision require it.
- Accepted clinical statements enter the chart only through the supported intake API with provenance and succession controls.

## Frappe realization

- **DocTypes:** `OC Telehealth Intake Pack`, child `OC Intake Form Assignment`, and `OC Telehealth Intake Submission` store template versions, answers, completion, flags, and chart-ingestion references.
- **Portal/API:** Web Forms save and submit through `open_chart.api.v1.telehealth`; mapped clinical statements call the guarded intake write surface rather than direct DocType inserts.
- **Workflow/permissions:** Patient authors own submission, Telehealth Intake Reviewer resolves flags, Clinician sees accepted encounter context, and template changes require Clinical Content Reviewer.

## Boundaries

Owns: telehealth pre-join form assignment and submission. Consumes: appointment and governed templates. Emits: readiness state and provenance-bound patient reports. Does not own: longitudinal reconciliation or autonomous triage.

## Open questions

- Which answers should remain encounter-local versus entering longitudinal statement records after clinician reconciliation?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
