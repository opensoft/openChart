# Medication Source Provenance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows who reported, imported, reviewed, or clinically confirmed each medication-list assertion and when.
Topics: openchart-feature-catalog, medical-records, frappe, medication-provenance
Repository context: openChart — Frappe v15 native EMR; catalog entry PMR-025 (Problems Allergies Medication Records And Vitals)
Captured: 2026-08-24

## Possible feats

- **Source-comparison visualization** — Extend this record with an optional companion capability after its authority and safety rules are governed.

## Focus

Source authority and review lineage for medication statements across patient, caregiver, exchange, and clinician inputs.

## Behavior

- All medication-list users open the capability from the patient chart, relevant encounter, or assigned review queue.
- Required inputs are source type, source reference, reporter relationship, capture time, reviewer, confidence, and consent context.
- The interface identifies patient-reported, imported, and clinician-authored assertions instead of flattening their authority.
- Domain states are reported, imported, reviewed, confirmed, disputed; every transition records actor, effective time, source, and reason where applicable.
- Accepted clinical content is immutable; correction or reclassification creates a successor linked to its predecessor.
- Clinical roles may create and review records, while restricted or destructive dispositions require explicit Role and User Permissions.
- The capability produces a provenance panel and filterable trust state and exposes unresolved items in list filters rather than hiding them.
- Edge handling: Multiple sources may support or dispute the same medication and remain independently inspectable.

## Frappe realization

- **DocTypes:** Extend or compose `OC Medication Statement` and add `OC Medication Provenance` as a child DocType; use `OC PMR-.YYYY.-.#####` naming for new standard records.
- **Fields:** Link `patient` to `OC Patient`, Link coded values to `OC Provenance Source Type`, Table rows to `OC Medication Provenance`, and Fetch From the selected code's `display`, `system`, and `release_version` into read-only snapshot fields.
- **Versioning:** Keep accepted records append-only and route amendments through `open_chart.api.v1.amend`; store `predecessor`, `submission_version`, `amendment_reason`, and provenance rather than editing in place.
- **Workflow:** Configure Frappe Workflow states for `reported, imported, reviewed, confirmed, disputed` with transition reasons and Workflow Actions where a second review is required.
- **Permissions:** Grant permlevel 0 entry to `OC Clinical User`, review to `OC Clinician`, specialized review to `OC Pharmacist` or `OC Health Information Manager`, and apply patient User Permissions at every query.
- **Hooks:** Use `validate` for code-release and state-transition invariants, `on_update` for audit-safe derived flags, and scheduler events only for due review work; no hook performs autonomous clinical action.
- **API and surfaces:** Add guarded methods under `open_chart.api.v1`; allow read-only `/api/resource/OC%20Medication%20Statement?filters=[["patient","=","..."],["modified",">=","..."]]&fields=["name","patient","modified"]`, plus a Desk workspace, filtered List View, and Query or Script Report.

## Boundaries

Owns: source authority and review lineage for medication statements across patient, caregiver, exchange, and clinician inputs. Consumes: patient identity, encounter context where relevant, terminology releases, consent, and source provenance. Emits: a provenance panel and filterable trust state. Does not own: prescribing, medication administration, external terminology licensing, billing, or autonomous diagnosis and treatment decisions.

## Open questions

- What vocabulary should distinguish clinical confirmation from administrative verification?

## Relationships

[Synthesis: Problems Allergies Medication Records And Vitals](openchart-feature-catalog-synthesis-pmr.md)
