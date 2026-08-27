# OTC Supplement And Herbal Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures over-the-counter products, vitamins, supplements, and herbals with patient-reported provenance and structured ingredients when known.
Topics: openchart-feature-catalog, medical-records, frappe, supplement-capture
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-020 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Product-label image extraction** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Faithful non-prescription product capture built on OC Supplement Statement without implying endorsement or prescribing.

## Behavior

- Patients, caregivers, clinicians, and intake staff open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are reported product, ingredients, dose text, frequency, purpose, source image, and reporter relationship.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, reviewed, inactive, entered-in-error; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a provenance-marked supplement list that can participate in review and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Unknown composition remains as patient wording and must not be mapped to an ingredient without review.

## Frappe realization

- **DocTypes:** Extend or compose `OC Supplement Statement` and add `OC Supplement Ingredient` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Supplement Product Code`, Table rows to `OC Supplement Ingredient`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, reviewed, inactive, entered-in-error` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Supplement%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: faithful non-prescription product capture built on oc supplement statement without implying endorsement or prescribing. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a provenance-marked supplement list that can participate in review. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- Which supplement terminology source is sufficiently open and maintainable for coded capture?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
