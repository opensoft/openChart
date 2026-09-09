# Existing Specimen Add-On Tests — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Requests additional tests against an existing accession only when specimen type, volume, stability, and retention permit.
Topics: openchart-feature-catalog, laboratory, frappe, add-on-testing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-030 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Existing Specimen Add-On Tests assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates add-on intent and feasibility response as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies accession, requested test, indication, requester, specimen availability, stability deadline, volume, and lab response.
- The system produces an accepted, rejected, or clarification-required add-on linked to the original specimen and exposes its current state to permitted users.
- The governed lifecycle is Requested → Feasibility Review → Accepted, Rejected, or Clarification → Resulted; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Expired, exhausted, contaminated, already-discarded, or incompatible specimens produce coded rejection and alternate recollection guidance.

## Frappe realization

- **DocTypes:** `OC Lab Add-On Request` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Requested → Feasibility Review → Accepted, Rejected, or Clarification → Resulted; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.existing_specimen_add_on_tests` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Add-On%20Request` reads and a Desk worklist or report.

## Boundaries

Owns: add-on intent and feasibility response. Consumes: accessions, retained specimen inventory, catalog requirements, and ordering authority. Emits: an accepted, rejected, or clarification-required add-on linked to the original specimen. Does not own: specimen retention policy or external laboratory performance.

## Open questions

- Which organization-level policy values and exception thresholds for existing specimen add-on tests must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
