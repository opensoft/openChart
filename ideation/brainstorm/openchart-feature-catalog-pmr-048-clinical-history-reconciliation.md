# Clinical History Reconciliation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a unified review session for family, social, surgical, hospitalization, pregnancy, and implant history candidates.
Topics: openchart-feature-catalog, medical-records, frappe, history-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-048 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Source-by-source reconciliation views** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A cross-history reconciliation shell with item-specific authority and provenance preserved.

## Behavior

- Clinicians, nurses, and health-information staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are history candidates, current statements, source references, per-item disposition, unresolved reason, and reviewer.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are not-started, in-review, awaiting-clarification, complete, incomplete; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a signed review record and authorized successor history entries and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Completion never flattens restricted data or converts patient reports into clinically verified entries without authority.

## Frappe realization

- **DocTypes:** Extend or compose `OC Clinical History Reconciliation` and add `OC History Reconciliation Item` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Reconciliation Disposition`, Table rows to `OC History Reconciliation Item`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `not-started, in-review, awaiting-clarification, complete, incomplete` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Clinical%20History%20Reconciliation?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a cross-history reconciliation shell with item-specific authority and provenance preserved. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a signed review record and authorized successor history entries. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which history families should be mandatory at particular care transitions?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
