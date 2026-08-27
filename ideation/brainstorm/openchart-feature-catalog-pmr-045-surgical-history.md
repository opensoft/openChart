# Surgical History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records past procedures with codes, dates or ranges, body sites, facilities, outcomes, complications, and provenance.
Topics: openchart-feature-catalog, medical-records, frappe, surgical-history
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-045 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Procedure timeline visualization** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A structured procedure history that can link source documents without becoming a surgical scheduling system.

## Behavior

- Patients, clinicians, nurses, and health-information staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are procedure code and wording, date precision, body site, facility, surgeon text, outcome, complications, and source.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, documented, verified, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a chronological surgical-history list with source links and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Approximate dates retain their precision and must not be normalized to invented exact dates.

## Frappe realization

- **DocTypes:** Extend or compose `OC Surgical History` and add `OC Surgical History Detail` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Procedure Code`, Table rows to `OC Surgical History Detail`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, documented, verified, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Surgical%20History?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a structured procedure history that can link source documents without becoming a surgical scheduling system. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a chronological surgical-history list with source links. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- What minimum detail distinguishes a useful surgical-history entry from an unstructured note?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
