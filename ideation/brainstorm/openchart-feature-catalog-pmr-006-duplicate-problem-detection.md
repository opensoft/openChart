# Duplicate Problem Detection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Flags likely duplicate problem entries using codes, wording, dates, and status while keeping merge decisions clinician-controlled.
Topics: openchart-feature-catalog, medical-records, frappe, problem-deduplication
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-006 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Patient-specific duplicate suppression** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Explainable duplicate candidates and safe resolution without autonomous clinical merging.

## Behavior

- Clinicians and health-information staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient condition statements, normalized codes, lexical similarity, onset intervals, and prior decisions.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are candidate, dismissed, linked-as-related, consolidated; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces an explainable review queue and preserved decision trail and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Same-code problems with distinct episodes may be related rather than duplicates and must remain separate.

## Frappe realization

- **DocTypes:** Extend or compose `OC Problem Duplicate Review` and add `OC Problem Duplicate Candidate` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Duplicate Decision Code`, Table rows to `OC Problem Duplicate Candidate`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `candidate, dismissed, linked-as-related, consolidated` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Problem%20Duplicate%20Review?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: explainable duplicate candidates and safe resolution without autonomous clinical merging. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: an explainable review queue and preserved decision trail. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- How long should a dismissed candidate suppress equivalent future suggestions?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
