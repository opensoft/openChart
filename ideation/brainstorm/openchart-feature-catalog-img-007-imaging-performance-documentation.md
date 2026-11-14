# Imaging Performance Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records what imaging study was actually performed, by whom, with deviations, exposures, contrast, specimens, and technologist notes.
Topics: openchart-feature-catalog, imaging, frappe, performance-documentation
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-007 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Device event ingestion** — Reconcile modality-provided exposure and acquisition metadata with human documentation.

## Focus

This feature isolates the authoritative clinical-operational record of imaging performance.

## Behavior

- The technologist confirms patient, order, protocol, modality, site, laterality, start time, and completion time.
- The record captures performed series summary, contrast administration, exposure details, medications, devices, specimens, and free-text notes as applicable.
- Deviations from the approved protocol require a structured reason and responsible actor.
- Unable-to-complete and partially completed studies preserve attempted work and disposition.
- Submission closes technologist editing; corrections create a successor linked to the accepted record.
- Completion emits report-readiness and downstream integration events only after server validation.

## Frappe realization

- **DocTypes:** submittable `OC Imaging Performance` with child tables for exposures, contrast administrations, series summaries, deviations, and participants.
- **Workflow:** Draft → In Progress → Completed → Accepted, with Partial and Unable to Complete dispositions.
- **Roles/permissions:** technologists create and submit; radiologists read; imaging managers approve corrections; permlevel 1 protects device metadata.
- **Hooks/API/surfaces:** `validate` reconciles order and protocol; guarded performance API accepts idempotency keys; Print Format provides a performance worksheet.

## Boundaries

Owns: performed-study facts and technologist attestation. Consumes: order, protocol, device metadata, and safety checks. Emits: completion and report-readiness events. Does not own: pixel data or diagnostic interpretation.

## Open questions

- Which modality-generated fields may replace manual entry only after explicit reconciliation?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
