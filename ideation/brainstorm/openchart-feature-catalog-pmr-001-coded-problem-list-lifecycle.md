# Coded Problem List Lifecycle — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains a coded longitudinal problem list from identification through active management and closure.
Topics: openchart-feature-catalog, medical-records, frappe, problem-lifecycle
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-001 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Problem episode rollups** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

One clinician-facing lifecycle for coded conditions without turning patient-reported assertions into confirmed diagnoses.

## Behavior

- Clinicians and health-information staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient, reported wording, ICD-10-CM or SNOMED CT code, onset date, verification status, and recorder provenance.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are proposed, confirmed, active, resolved, inactive, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a current problem-list row plus an immutable lifecycle history and exposes unresolved items in list filters rather than hiding them.
- Edge handling: A code may be absent while an uncoded problem remains in terminology review, but confirmation requires clinical authority.

## Frappe realization

- **DocTypes:** Extend or compose `OC Condition Statement` and add `OC Condition Lifecycle Event` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Clinical Condition Code`, Table rows to `OC Condition Lifecycle Event`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `proposed, confirmed, active, resolved, inactive, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Condition%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: one clinician-facing lifecycle for coded conditions without turning patient-reported assertions into confirmed diagnoses. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a current problem-list row plus an immutable lifecycle history. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Should resolved problems remain visible by default in every specialty workspace?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
