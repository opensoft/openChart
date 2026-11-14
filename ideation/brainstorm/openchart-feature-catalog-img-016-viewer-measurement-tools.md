# Viewer Measurement Tools — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Persists clinically selected viewer measurements as provenance-rich references that can support reporting without making openChart an image-rendering engine.
Topics: openchart-feature-catalog, imaging, frappe, image-measurements
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-016 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Longitudinal measurement table** — Compare accepted measurements across studies with explicit method compatibility.

## Focus

This feature isolates the interchange and clinical use of measurements created in an external viewer.

## Behavior

- Supported viewers return measurement type, value, unit, image reference, geometry, author, and timestamp.
- The reporting clinician chooses which returned measurements become report evidence.
- Units and measurement type are validated against the selected structured report field.
- Editing in the report never mutates the source annotation; a revised measurement creates a new record.
- Missing image references, unsupported units, or stale viewer sessions require reconciliation.
- Report signatures snapshot selected measurement identities and source provenance.

## Frappe realization

- **DocTypes:** `OC Imaging Measurement` stores SOP Instance reference, frame, geometry JSON, coded type, value, unit, source system, and author.
- **Roles/permissions:** viewer integrations may create pending records; radiologists accept them; other clinicians receive read-only accepted values.
- **API/surfaces:** signed viewer callback posts measurements to a whitelisted method; report form presents accept or reject actions.
- **Hooks:** report `validate` enforces unit and study consistency; successor links preserve corrected measurements.

## Boundaries

Owns: accepted measurement metadata and report linkage. Consumes: viewer annotations and study references. Emits: report-ready discrete values. Does not own: pixel calibration, geometry rendering, or viewer algorithms.

## Open questions

- Which measurement formats should be supported beyond a minimal viewer-neutral interchange contract?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
