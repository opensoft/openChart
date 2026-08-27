# Clinical Terminology Lookup — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides governed ICD-10-CM, SNOMED CT, and RxNorm search for coded clinical entry with version-aware results.
Topics: openchart-feature-catalog, medical-records, frappe, terminology-lookup
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-007 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Offline terminology cache packs** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

A shared lookup surface that returns identifiers and displays without owning external terminology licensing.

## Behavior

- Clinicians and clinical data-entry staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are query text, code system, release version, active-only flag, and optional value-set constraint.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are available, degraded, unavailable; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces ranked coded results with release and designation metadata and exposes unresolved items in list filters rather than hiding them.
- Edge handling: An unavailable terminology service permits clearly marked text capture but never fabricates a code.

## Frappe realization

- **DocTypes:** Extend or compose `OC Terminology Release` and add `OC Terminology Search Alias` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Clinical Code System`, Table rows to `OC Terminology Search Alias`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `available, degraded, unavailable` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Terminology%20Release?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: a shared lookup surface that returns identifiers and displays without owning external terminology licensing. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: ranked coded results with release and designation metadata. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which terminology distributions can openChart ship versus require site-managed loading?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
