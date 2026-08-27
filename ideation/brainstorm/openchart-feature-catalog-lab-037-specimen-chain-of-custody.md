# Specimen Chain Of Custody — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records every custody transfer, seal state, location, and witness for specimens requiring defensible handling history.
Topics: openchart-feature-catalog, laboratory, frappe, chain-of-custody
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-037 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Specimen Chain Of Custody assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates custody evidence and exception history as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Specimen Custodian supplies specimen identifier, releasing and receiving parties, timestamps, locations, seal identifiers, condition, purpose, and witness.
- The system produces an append-only chronological custody ledger and exposes its current state to permitted users.
- The governed lifecycle is In Custody → Transfer Pending → Accepted or Disputed → Final Disposition; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Broken seals, missing receivers, time gaps, and disputed transfers create exceptions and cannot be corrected in place.

## Frappe realization

- **DocTypes:** `OC Specimen Custody Event` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements In Custody → Transfer Pending → Accepted or Disputed → Final Disposition; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Specimen Custodian` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.specimen_chain_of_custody` is the supported write method, with allowlisted `/api/resource/OC%20Specimen%20Custody%20Event` reads and a Desk worklist or report.

## Boundaries

Owns: custody evidence and exception history. Consumes: specimen identity, authorized custodians, locations, and retention policy. Emits: an append-only chronological custody ledger. Does not own: legal conclusions, test interpretation, or external custody after acknowledged handoff.

## Open questions

- Which organization-level policy values and exception thresholds for specimen chain of custody must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
