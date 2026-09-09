# Clinical Record Summary Workspace — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Combines current problems, allergies, medications, recent vitals, and key histories into a role-aware review workspace.
Topics: openchart-feature-catalog, medical-records, frappe, record-summary
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-050 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Shift and handoff summary layouts** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A compositional chart surface that supports review while leaving each underlying record family authoritative.

## Behavior

- Clinicians, nurses, pharmacists, and authorized clinical staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient, role, encounter context, workspace configuration, effective records, alerts, and reconciliation status.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are current, needs-review, filtered; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a configurable chart summary with links to source records and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Stale, unverified, disputed, and patient-reported entries remain visibly labeled and never collapse into a single certainty state.

## Frappe realization

- **DocTypes:** Extend or compose `OC Clinical Summary Preference` and add `OC Summary Section Preference` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Clinical Record Family`, Table rows to `OC Summary Section Preference`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `current, needs-review, filtered` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Clinical%20Summary%20Preference?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a compositional chart surface that supports review while leaving each underlying record family authoritative. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a configurable chart summary with links to source records. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which sections and warning labels must remain non-configurable for safety?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
