# Medication Adherence Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records patient-reported or clinician-assessed medication-taking patterns, barriers, and observation periods without overstating certainty.
Topics: openchart-feature-catalog, medical-records, frappe, medication-adherence
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-021 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Barrier-specific support suggestions** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Time-bounded adherence observations linked to medication statements rather than a permanent compliant/noncompliant label.

## Behavior

- Patients, caregivers, clinicians, and pharmacists open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are medication, observation period, reporter, adherence category, missed-dose pattern, barriers, and notes.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, reviewed, superseded; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a longitudinal adherence history and current review cue and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Conflicting reports coexist with separate provenance and are not averaged into false precision.

## Frappe realization

- **DocTypes:** Extend or compose `OC Medication Adherence Observation` and add `OC Adherence Barrier` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Adherence Code`, Table rows to `OC Adherence Barrier`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, reviewed, superseded` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Medication%20Adherence%20Observation?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: time-bounded adherence observations linked to medication statements rather than a permanent compliant/noncompliant label. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a longitudinal adherence history and current review cue. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which adherence categories balance interoperability with nonjudgmental language?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
