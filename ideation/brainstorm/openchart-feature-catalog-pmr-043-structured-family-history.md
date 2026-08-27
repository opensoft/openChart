# Structured Family History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records relatives, relationship, conditions, age at onset, age or cause of death, and source provenance.
Topics: openchart-feature-catalog, medical-records, frappe, family-history
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-043 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Pedigree visualization** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A relationship-aware family history model that keeps relative identity minimal and conditions coded when known.

## Behavior

- Patients, caregivers, genetic counselors, and clinicians open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are relationship, optional relative label, condition code and wording, onset age, vital status, death age or cause, and reporter.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, reviewed, amended, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a pedigree-ready structured family history list and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Approximate ages and unknown relatives remain explicit without creating identifiable patient records for family members.

## Frappe realization

- **DocTypes:** Extend or compose `OC Family History` and add `OC Family History Condition` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Family Relationship Code`, Table rows to `OC Family History Condition`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, reviewed, amended, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Family%20History?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a relationship-aware family history model that keeps relative identity minimal and conditions coded when known. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a pedigree-ready structured family history list. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- How much relative detail is appropriate before separate consent or identity governance is required?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
