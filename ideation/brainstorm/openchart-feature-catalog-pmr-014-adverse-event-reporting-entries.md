# Adverse Event Reporting Entries — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents suspected medication or substance adverse events with timing, outcome, seriousness, and report disposition.
Topics: openchart-feature-catalog, medical-records, frappe, adverse-event
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-014 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Regulator-specific report adapters** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A reportable clinical event linked to but distinct from allergy and medication statements.

## Behavior

- Clinicians, pharmacists, and safety officers open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are suspected agent, event description, onset, seriousness criteria, outcome, reporter, and related records.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are draft, under-review, reportable, reported, closed; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a safety event record and export-ready reporting dataset and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Causality remains an assessment with uncertainty and is never inferred solely from temporal proximity.

## Frappe realization

- **DocTypes:** Extend or compose `OC Adverse Event` and add `OC Adverse Event Suspect` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Adverse Event Outcome Code`, Table rows to `OC Adverse Event Suspect`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `draft, under-review, reportable, reported, closed` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Adverse%20Event?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a reportable clinical event linked to but distinct from allergy and medication statements. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a safety event record and export-ready reporting dataset. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which reporting destinations and jurisdictional forms should be supported first?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
