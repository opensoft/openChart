# Screening-Driven Lab Order Suggestions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents reviewable laboratory order suggestions from versioned ACOG-, USPSTF-, and locally approved screening guidance.
Topics: openchart-feature-catalog, laboratory, frappe, screening-guidance
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-027 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Screening-Driven Lab Order Suggestions assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates screening suggestion evaluation and disposition as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies patient age and sex context, pregnancy context, risk factors, prior results, due dates, guideline version, and local policy.
- The system produces an explainable suggestion that can be accepted into a draft or dismissed with context and exposes its current state to permitted users.
- The governed lifecycle is Eligible → Presented → Accepted, Dismissed, Deferred, or Expired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Missing or conflicting eligibility data shows uncertainty; no suggestion signs or transmits an order autonomously.

## Frappe realization

- **DocTypes:** `OC Lab Screening Suggestion` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Eligible → Presented → Accepted, Dismissed, Deferred, or Expired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.screening_driven_lab_suggestions` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Screening%20Suggestion` reads and a Desk worklist or report.

## Boundaries

Owns: screening suggestion evaluation and disposition. Consumes: governed guideline rules, patient context, and prior laboratory history. Emits: an explainable suggestion that can be accepted into a draft or dismissed with context. Does not own: diagnosis, guideline authorship, or autonomous ordering.

## Open questions

- Which organization-level policy values and exception thresholds for screening-driven lab order suggestions must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
