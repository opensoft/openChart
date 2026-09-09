# Problem Driven Care Gap Flags — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Derives reviewable care-gap flags from confirmed problem-list criteria without autonomously placing orders or changing care.
Topics: openchart-feature-catalog, medical-records, frappe, care-gap-flags
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-010 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Population care-gap worklists** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Transparent problem-triggered reminders with human review and bounded clinical action.

## Behavior

- Clinicians and care coordinators open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are confirmed condition codes, demographic qualifiers, rule release, evidence timestamp, and exclusions.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are open, acknowledged, deferred, satisfied, not-applicable; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces an explainable patient flag with evidence and disposition and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Missing or uncertain source data produces an indeterminate flag rather than a definitive gap.

## Frappe realization

- **DocTypes:** Extend or compose `OC Care Gap Flag` and add `OC Care Gap Evidence` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Care Gap Rule`, Table rows to `OC Care Gap Evidence`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `open, acknowledged, deferred, satisfied, not-applicable` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Care%20Gap%20Flag?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: transparent problem-triggered reminders with human review and bounded clinical action. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: an explainable patient flag with evidence and disposition. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Who approves rule releases and site-specific exclusion logic?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
