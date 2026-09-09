# Medication Reconciliation Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares current, patient-reported, outside, and encounter medication lists and records a signed disposition for every item.
Topics: openchart-feature-catalog, medical-records, frappe, medication-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-018 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Admission-to-discharge comparison** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A structured reconciliation workflow that preserves source differences and prevents silent list replacement.

## Behavior

- Clinicians, nurses, and pharmacists open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are medication candidates, source lists, local matches, proposed dispositions, encounter, and reviewer.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are not-started, in-review, awaiting-clarification, complete, incomplete; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a signed reconciliation record and authorized medication successors and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Unresolved identity, dose, or status discrepancies remain visible and block a clean-complete attestation.

## Frappe realization

- **DocTypes:** Extend or compose `OC Medication Reconciliation` and add `OC Medication Reconciliation Item` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Reconciliation Disposition`, Table rows to `OC Medication Reconciliation Item`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `not-started, in-review, awaiting-clarification, complete, incomplete` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Medication%20Reconciliation?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a structured reconciliation workflow that preserves source differences and prevents silent list replacement. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a signed reconciliation record and authorized medication successors. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which care transitions require mandatory reconciliation before encounter closure?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
