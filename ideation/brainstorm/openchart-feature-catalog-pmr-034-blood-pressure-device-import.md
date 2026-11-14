# Blood Pressure Device Import — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides vendor-neutral hooks for importing blood-pressure cuff readings with device identity and transmission provenance.
Topics: openchart-feature-catalog, medical-records, frappe, blood-pressure-import
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-034 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Validated device registry checks** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A guarded ingestion adapter from device payload to patient-reported observation candidates.

## Behavior

- Patients, integration operators, and reviewing clinicians open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are external patient identifier, systolic, diastolic, pulse, measured time, cuff identifier, payload identifier, and source.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are received, matched, identity-review, accepted, rejected; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces reviewable blood-pressure observation candidates and import status and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Ambiguous patient identity never auto-attaches a reading and duplicate payload identifiers are idempotent.

## Frappe realization

- **DocTypes:** Extend or compose `OC Device Observation Import` and add `OC Imported BP Reading` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Device Type Code`, Table rows to `OC Imported BP Reading`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `received, matched, identity-review, accepted, rejected` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Device%20Observation%20Import?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a guarded ingestion adapter from device payload to patient-reported observation candidates. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: reviewable blood-pressure observation candidates and import status. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which transport profiles should be supported before vendor-specific adapters?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
