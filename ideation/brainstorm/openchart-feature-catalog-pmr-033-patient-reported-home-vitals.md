# Patient Reported Home Vitals — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Accepts patient or caregiver home vital readings with device, method, timestamp, and patient-reported provenance.
Topics: openchart-feature-catalog, medical-records, frappe, home-vitals
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-033 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Home-reading reminders** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A portal and API intake path that keeps home readings distinct from clinic measurements while enabling review.

## Behavior

- Patients, caregivers, and reviewing clinicians open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are measurement type, value, unit, measured time, device, posture or context, symptoms, and reporter.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are received, needs-review, accepted, rejected, amended; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces provenance-marked home readings and a clinician review queue and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Duplicate uploads are idempotent and suspicious timestamps or units route to review rather than silent normalization.

## Frappe realization

- **DocTypes:** Extend or compose `OC Observation Statement` and add `OC Home Vital Context` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Observation Code`, Table rows to `OC Home Vital Context`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `received, needs-review, accepted, rejected, amended` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Observation%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a portal and api intake path that keeps home readings distinct from clinic measurements while enabling review. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: provenance-marked home readings and a clinician review queue. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which reading types may become accepted automatically after device validation?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
