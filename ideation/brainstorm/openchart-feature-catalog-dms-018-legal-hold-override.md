# Legal Hold Override — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies scoped legal holds that block document alteration or disposition while preserving authority, notice, review, and release history.
Topics: openchart-feature-catalog, documents, frappe, legal-hold
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-018 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Hold coverage attestation** — Produce a signed inventory proving which records, versions, and storage replicas were placed under hold.

## Focus

This feature isolates a higher-authority preservation control that overrides ordinary retention and purge eligibility.

## Behavior

- A Legal Hold Officer creates a hold with authority reference, matter, scope, custodians, start time, and review date.
- Scope may target patients, classes, date ranges, documents, or import packages and resolves to exact version identifiers.
- Activating a hold immediately blocks disposition jobs and marks affected records without exposing matter details broadly.
- New records matching an active dynamic scope are added and logged by scheduled evaluation.
- Attempts to destroy, overwrite, or exclude held content fail closed and create alerts.
- Releasing a hold requires authorized approval, reason, time, and a final coverage snapshot.
- Release restores ordinary retention evaluation; it never triggers immediate automatic deletion.

## Frappe realization

- **DocTypes:** `OC Legal Hold` (matter_key, authority_file, scope JSON, state, review_at) with child `OC Held Document Version` and immutable coverage snapshots.
- **Workflow:** Draft → Counsel Review → Active → Release Review → Released, with Suspended and Superseded states.
- **Roles/permissions:** Legal Hold Officer manages; Privacy Officer audits; ordinary users see only a preservation flag; matter details use permlevel 2.
- **Hooks/jobs:** File and document `validate` consult active hold mappings; scheduler_events expand dynamic scope and alert on attempted violations.
- **API/surfaces:** Guarded hold activation/release methods, restricted Desk workspace, coverage Script Report, and hold certificate Print Format.

## Boundaries

Owns: hold authority reference, scope resolution, preservation block, and release evidence. Consumes: document inventory and legal direction. Emits: immutable hold mappings and disposition blockers. Does not own: legal advice, litigation workflow, or retention policy calculation.

## Open questions

- Should dynamic scope be frozen at activation or continuously include newly matching records by default?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Document Retention Schedule Enforcement](openchart-feature-catalog-dms-017-document-retention-schedule-enforcement.md)
