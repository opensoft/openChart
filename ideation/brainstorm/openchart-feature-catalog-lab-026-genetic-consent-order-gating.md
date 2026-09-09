# Genetic Consent Order Gating — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Prevents genomic order transmission until the required consent scope, signer authority, and validity period are documented.
Topics: openchart-feature-catalog, laboratory, frappe, genetic-consent
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-026 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Genetic Consent Order Gating assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates order-time consent eligibility evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Genetics Clinician supplies genomic order, consent record reference, test purpose, specimen use, secondary findings choice, signer authority, and effective dates.
- The system produces a pass, block, or review decision pinned to consent evidence and exposes its current state to permitted users.
- The governed lifecycle is Pending → Passed, Blocked, or Manual Review → Rechecked; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Withdrawn, mismatched, expired, or narrower consent blocks transmission and explains the unmet scope.

## Frappe realization

- **DocTypes:** `OC Genetic Consent Check` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Pending → Passed, Blocked, or Manual Review → Rechecked; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Genetics Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.genetic_consent_order_gating` is the supported write method, with allowlisted `/api/resource/OC%20Genetic%20Consent%20Check` reads and a Desk worklist or report.

## Boundaries

Owns: order-time consent eligibility evidence. Consumes: genomic orders and governed consent records. Emits: a pass, block, or review decision pinned to consent evidence. Does not own: consent capture policy, counseling, or overriding patient choices.

## Open questions

- Which organization-level policy values and exception thresholds for genetic consent order gating must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
