# Pregnancy Status Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records time-bounded pregnancy status, estimated dates, verification source, and uncertainty for clinical context.
Topics: openchart-feature-catalog, medical-records, frappe, pregnancy-status
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-039 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Gestational-age context service** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A sensitive, versioned clinical status that informs context without owning obstetric care workflows.

## Behavior

- Authorized clinicians, nurses, and patients through consented intake open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are status, effective interval, estimated dates, verification method, source, recorder, and privacy flags.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are unknown, not-pregnant, pregnant, recently-pregnant, uncertain, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a permission-aware current status and history and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Conflicting or stale assertions coexist with provenance and route to review rather than silent selection.

## Frappe realization

- **DocTypes:** Extend or compose `OC Pregnancy Status` and add `OC Pregnancy Status Evidence` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Pregnancy Status Code`, Table rows to `OC Pregnancy Status Evidence`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `unknown, not-pregnant, pregnant, recently-pregnant, uncertain, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Pregnancy%20Status?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a sensitive, versioned clinical status that informs context without owning obstetric care workflows. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a permission-aware current status and history. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- What additional access controls are needed for sensitive reproductive information by jurisdiction?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
