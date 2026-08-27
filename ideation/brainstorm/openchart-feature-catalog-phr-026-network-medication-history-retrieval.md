# Network Medication History Retrieval — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Retrieves externally reported medication history into a source-labeled staging record for clinician reconciliation.
Topics: openchart-feature-catalog, eprescribing, frappe, medication-history
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-026 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Incremental history refresh** — Later retrievals could highlight added, changed, and absent claims while preserving source limitations.

## Focus

This feature isolates network history retrieval and staging. External fill or claim evidence never becomes a confirmed medication statement without human reconciliation.

## Behavior

- An authorized user requests history for a verified patient, coverage context, purpose, and date range.
- The adapter validates consent or legal basis and records identifiers sent to the network.
- Returned medications retain source, dates, product identifiers, prescriber/pharmacy facts, and network caveats.
- Duplicate payloads are idempotently recognized; uncertain patient matches remain quarantined.
- The system labels claim, dispense, and reported data distinctly and never infers adherence.
- Accepted retrievals open a reconciliation session where clinicians disposition each candidate.

## Frappe realization

- **DocTypes:** `OC Medication History Retrieval` and child `OC External Medication Candidate` store request, response digest, source facts, matching, and status.
- **Workflow:** Requested → Retrieved → Identity Review → Ready for Reconciliation → Reconciled/Rejected/Expired.
- **Roles/API:** Authorized clinical roles use guarded retrieval APIs; sensitive raw payload access is restricted and audited.
- **Surfaces/jobs:** Retrieval dialog, quarantined-match queue, reconciliation launch action, and background adapter jobs support the flow.

## Boundaries

Owns: retrieval request, source-preserving staging, and handoff. Consumes: network, patient identity, consent, and coverage. Emits: external medication candidates. Does not own: local medication-list truth, adherence, or claims adjudication.

## Open questions

- What history window and refresh cadence balance completeness, cost, and privacy?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Medication History Reconciliation Inbox](openchart-feature-catalog-phr-027-medication-history-reconciliation-inbox.md)
