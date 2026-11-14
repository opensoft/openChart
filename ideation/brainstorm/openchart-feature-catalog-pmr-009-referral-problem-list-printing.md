# Referral Problem List Printing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces a referral-ready problem list with selected active and historical entries, provenance, and as-of timestamp.
Topics: openchart-feature-catalog, medical-records, frappe, problem-printing
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-009 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Specialty-specific referral layouts** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A clinician-controlled print artifact that presents problems without transferring record authority.

## Behavior

- Referring clinicians and authorized staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are patient, as-of date, inclusion filters, recipient context, selected problems, and letter head.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are draft, finalized, superseded; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a versioned Jinja PDF and machine-readable extract manifest and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Sensitive or disputed entries require explicit inclusion and all omissions are disclosed in the print metadata.

## Frappe realization

- **DocTypes:** Extend or compose `OC Clinical Record Extract` and add `OC Extract Problem Item` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Extract Inclusion Reason`, Table rows to `OC Extract Problem Item`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `draft, finalized, superseded` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Clinical%20Record%20Extract?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a clinician-controlled print artifact that presents problems without transferring record authority. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a versioned Jinja PDF and machine-readable extract manifest. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Should the default include resolved problems from a configurable lookback period?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
