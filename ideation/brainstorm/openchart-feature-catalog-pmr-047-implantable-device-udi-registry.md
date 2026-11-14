# Implantable Device UDI Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Registers implantable devices using UDI components, device type, implant and explant dates, status, site, and provenance.
Topics: openchart-feature-catalog, medical-records, frappe, implant-registry
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-047 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **UDI resolver integration** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A patient-linked implant registry with lifecycle and source traceability, not inventory or supply-chain management.

## Behavior

- Clinicians, procedural staff, and health-information managers open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are UDI or manual identifiers, device type, manufacturer data, lot or serial, body site, implant date, status, and source.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are candidate, active, inactive, explanted, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a current implant list, scan history, and printable device card and exposes unresolved items in list filters rather than hiding them.
- Edge handling: An unreadable or invalid UDI can be retained as an image-backed candidate but cannot fabricate parsed identifiers.

## Frappe realization

- **DocTypes:** Extend or compose `OC Implantable Device` and add `OC Device Identifier Component` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Implant Device Type`, Table rows to `OC Device Identifier Component`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `candidate, active, inactive, explanted, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Implantable%20Device?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a patient-linked implant registry with lifecycle and source traceability, not inventory or supply-chain management. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a current implant list, scan history, and printable device card. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which UDI databases and offline fallback behavior should be supported?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
