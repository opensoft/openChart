# Study Radiation Dose Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures modality-reported and manually reconciled radiation dose metrics for each performed imaging study with device and source provenance.
Topics: openchart-feature-catalog, imaging, frappe, radiation-dose
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-021 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Dose exception review** — Route studies outside governed reference ranges for human quality review.

## Focus

This feature isolates dose evidence for a single performed study before longitudinal aggregation.

## Behavior

- The system receives dose metrics from modality metadata, structured dose reports, interfaces, or authorized manual entry.
- Each value records metric type, unit, acquisition context, device, protocol, source, and timestamp.
- Imported values are matched to the performed study and rejected from auto-association when identifiers conflict.
- Manual corrections preserve the source value and require reason and reviewer identity.
- Missing expected dose data creates a reconciliation status rather than a zero value.
- Outlier flags are advisory quality signals and never alter clinical care automatically.

## Frappe realization

- **DocTypes:** `OC Imaging Dose Record` with child `OC Dose Metric`, performance Link, device, protocol version, source artifact, and reconciliation state.
- **Workflow:** Received → Matched → Verified, with Conflict and Missing Expected Data states.
- **Roles/permissions:** integrations create pending data; dose reviewers verify; technologists may explain discrepancies; clinicians read accepted records.
- **Hooks/API/surfaces:** idempotent ingestion method accepts source IDs; validation normalizes units; Query Report shows missing and outlier records.

## Boundaries

Owns: study-level dose metrics, provenance, and reconciliation. Consumes: performance and modality data. Emits: verified dose records and quality flags. Does not own: scanner control, dose limits, or clinical risk decisions.

## Open questions

- Which modality-specific dose metrics are required for a record to be considered complete?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
