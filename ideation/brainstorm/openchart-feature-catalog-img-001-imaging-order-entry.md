# Imaging Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a complete imaging request with modality, study, protocol intent, contrast, anatomy, laterality, urgency, and clinical context.
Topics: openchart-feature-catalog, imaging, frappe, imaging-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-001 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Order favorites** — Let clinicians reuse governed study defaults without copying patient-specific answers.

## Focus

This feature isolates the accepted clinical request that starts an imaging workflow.

## Behavior

- Authorized ordering clinicians choose a study from a governed imaging catalog.
- The order records modality, anatomy, laterality, contrast intent, priority, requested date, and diagnosis or indication.
- Study-specific fields appear before signature and reject invalid modality or laterality combinations.
- Drafts may be saved, but only a signed order becomes available to protocoling or scheduling.
- Fulfillment staff may request clarification without editing the accepted clinical intent.
- Material changes create a superseding order; cancellation records actor, time, and reason.

## Frappe realization

- **DocTypes:** submittable `OC Imaging Order` with naming series `IMG-ORD-.YYYY.-` and Links to patient, encounter, study catalog, and ordering practitioner.
- **Workflow:** Draft → Pending Signature → Active → Clarification Requested → Scheduled → In Progress → Completed, with Cancelled and supersession paths.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Imaging Coordinator` advances fulfillment; permlevel 1 protects signed intent and provenance.
- **Hooks/API/surfaces:** `validate` enforces catalog rules; guarded `open_chart.api.v1.imaging.submit_order` is the supported write path; Desk lists expose work by state.

## Boundaries

Owns: imaging clinical intent and lifecycle. Consumes: patient, encounter, terminology, and study catalog data. Emits: protocoling and scheduling demand. Does not own: scanner acquisition, PACS storage, or interpretation.

## Open questions

- Which order changes require a new order rather than a succession amendment?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
