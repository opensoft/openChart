# Hospitalization History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records prior hospital stays with reason, facility, date range, discharge disposition, and supporting provenance.
Topics: openchart-feature-catalog, medical-records, frappe, hospitalization-history
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-046 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Readmission context views** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A longitudinal hospitalization summary separate from local encounter ownership and imported documents.

## Behavior

- Patients, caregivers, clinicians, and health-information staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are reason or condition, facility, admission and discharge date precision, disposition, source document, and reporter.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, documented, verified, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a chronological hospitalization list and duration where calculable and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Overlapping or incomplete date ranges remain reviewable and are not automatically merged as one stay.

## Frappe realization

- **DocTypes:** Extend or compose `OC Hospitalization History` and add `OC Hospitalization Reason` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Discharge Disposition Code`, Table rows to `OC Hospitalization Reason`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, documented, verified, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Hospitalization%20History?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a longitudinal hospitalization summary separate from local encounter ownership and imported documents. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a chronological hospitalization list and duration where calculable. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Should outside encounter imports create candidates or verified hospitalization entries?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
