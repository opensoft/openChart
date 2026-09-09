# Structured E-Visit Questionnaire — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Collects condition-specific asynchronous patient answers and routes them to a clinician for a documented response.
Topics: openchart-feature-catalog, telehealth, frappe, structured-e-visit
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-012 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Adaptive question branches** — Show reviewed follow-up questions based on discrete answers without making a clinical decision.

## Focus

This feature isolates the end-to-end asynchronous questionnaire and clinician-response workflow known as an e-visit.

## Behavior

- A patient selects an offered e-visit reason and sees scope, expected response time, fees boundary, and emergency warnings.
- The questionnaire saves drafts, validates required answers, and records the exact effective template version.
- Submission freezes the patient response as an accepted artifact and creates a clinician review assignment.
- A clinician may request clarification, redirect modality, provide a clinical response, or decline with rationale.
- Patient clarification appends a new response segment rather than changing the original submission.
- Completion releases the clinician response and summary according to encounter-release policy with timestamps and provenance.

## Frappe realization

- **DocTypes/workflow:** `OC E Visit`, `OC E Visit Template`, and child `OC E Visit Answer` support Draft, Submitted, In Review, Awaiting Patient, Completed, Redirected, and Declined states.
- **API/surfaces:** portal Web Forms use versioned `open_chart.api.v1.telehealth` methods; a Clinician Kanban, assignments, and Notifications manage asynchronous work.
- **Clinical integrity:** accepted submissions and responses use succession-based amendments; templates define fields and branches but cannot autonomously diagnose, order, or prescribe.

## Boundaries

Owns: asynchronous intake, review dialogue, and response state. Consumes: patient identity, template, and clinician assignment. Emits: an e-visit encounter artifact. Does not own: billing adjudication or autonomous care decisions.

## Open questions

- Which presenting concerns are appropriate for e-visits, and who governs each template's inclusion and exclusion criteria?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
