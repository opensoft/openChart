# Synthesis: Labs And Diagnostics — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects governed ordering, specimen operations, external exchange, structured results, accountability handoffs, and diagnostic quality controls into a traceable laboratory lifecycle.
Topics: openchart-feature-catalog, laboratory, frappe, synthesis, diagnostic-lifecycle
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB synthesis (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Closed-loop diagnostic operations cockpit** — Combine order, specimen, interface, result, acknowledgment, quality, and release signals while leaving every clinical action under qualified human control.

## Focus

This synthesis relates the LAB catalog's atomic capabilities into an API-first Frappe model where ordered intent, physical specimens, transport transactions, diagnostic records, and accountability evidence remain distinct but linked.

## Members and their joints

### Ordering, guidance, and financial context

[Catalog-Driven Lab Order Creation](openchart-feature-catalog-lab-001-catalog-driven-lab-order-creation.md), [Order Diagnosis And Indication Linkage](openchart-feature-catalog-lab-002-order-diagnosis-indication-linkage.md), [Patient Collection Preparation Instructions](openchart-feature-catalog-lab-003-patient-collection-preparation-instructions.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Collection, specimen identity, and accession

[Specimen Collection Status Tracking](openchart-feature-catalog-lab-004-specimen-collection-status-tracking.md), [Barcode Specimen Labeling](openchart-feature-catalog-lab-005-barcode-specimen-labeling.md), [Laboratory Accessioning](openchart-feature-catalog-lab-006-laboratory-accessioning.md), [Collection Center Routing](openchart-feature-catalog-lab-007-collection-center-routing.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Reference-lab exchange and result ingestion

[Reference Lab Order Transmission](openchart-feature-catalog-lab-008-reference-lab-order-transmission.md), [Reference Lab Connector Profiles](openchart-feature-catalog-lab-009-reference-lab-connector-profiles.md), [Inbound Lab Result Parsing](openchart-feature-catalog-lab-010-inbound-lab-result-parsing.md), [Laboratory Result Chart Filing](openchart-feature-catalog-lab-011-result-chart-filing.md), [LOINC Panel Result Normalization](openchart-feature-catalog-lab-012-loinc-panel-result-normalization.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Interpretation, accountability, and longitudinal review

[Reference Range Abnormal Flagging](openchart-feature-catalog-lab-013-reference-range-abnormal-flagging.md), [Demographic-Specific Reference Ranges](openchart-feature-catalog-lab-014-demographic-specific-reference-ranges.md), [Critical Result Accountability Handoff](openchart-feature-catalog-lab-015-critical-result-accountability-handoff.md), [Pending Results Worklist](openchart-feature-catalog-lab-016-pending-results-worklist.md), [Resulted-But-Unacknowledged Tracking](openchart-feature-catalog-lab-017-unacknowledged-result-tracking.md), [Cumulative Laboratory Results Flowsheet](openchart-feature-catalog-lab-018-cumulative-results-flowsheet.md), [Serial Laboratory Result Graphing](openchart-feature-catalog-lab-019-serial-result-graphing.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Specialized and externally sourced diagnostics

[Outside Lab Result Manual Entry](openchart-feature-catalog-lab-020-outside-lab-result-manual-entry.md), [PDF Result Structured Extraction Assist](openchart-feature-catalog-lab-021-pdf-result-structured-extraction-assist.md), [Microbiology Culture Workbench](openchart-feature-catalog-lab-022-microbiology-culture-workbench.md), [Synoptic Pathology Report Capture](openchart-feature-catalog-lab-023-synoptic-pathology-report-capture.md), [Genomic Test Ordering](openchart-feature-catalog-lab-024-genomic-test-ordering.md), [Discrete Genomic Variant Result Return](openchart-feature-catalog-lab-025-discrete-genomic-variant-results.md), [Genetic Consent Order Gating](openchart-feature-catalog-lab-026-genetic-consent-order-gating.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Recurring orders and exception recovery

[Screening-Driven Lab Order Suggestions](openchart-feature-catalog-lab-027-screening-driven-lab-suggestions.md), [Standing Preventive Lab Orders](openchart-feature-catalog-lab-028-standing-preventive-lab-orders.md), [Repeat And Series Lab Orders](openchart-feature-catalog-lab-029-repeat-series-lab-orders.md), [Existing Specimen Add-On Tests](openchart-feature-catalog-lab-030-existing-specimen-add-on-tests.md), [Failed Specimen Handling And Recollection](openchart-feature-catalog-lab-031-failed-specimen-recollection.md), [Laboratory Order Rejection Loop](openchart-feature-catalog-lab-032-laboratory-order-rejection-loop.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Operations, cost, billing, and interface control

[Laboratory Turnaround Time Dashboard](openchart-feature-catalog-lab-033-laboratory-turnaround-time-dashboard.md), [Lab Order Cost Display](openchart-feature-catalog-lab-034-lab-order-cost-display.md), [Advance Beneficiary Notice Trigger](openchart-feature-catalog-lab-035-advance-beneficiary-notice-trigger.md), [Outreach Lab Billing Routing](openchart-feature-catalog-lab-036-outreach-lab-billing-routing.md), [Specimen Chain Of Custody](openchart-feature-catalog-lab-037-specimen-chain-of-custody.md), [Lab Interface Failure Monitoring Dashboard](openchart-feature-catalog-lab-038-lab-interface-monitoring-dashboard.md), [Stuck Transaction Reconciliation Queue](openchart-feature-catalog-lab-039-stuck-transaction-reconciliation.md), [Duplicate Result Import Detection](openchart-feature-catalog-lab-040-duplicate-result-import-detection.md), [Versioned Reference Range Editor](openchart-feature-catalog-lab-041-versioned-reference-range-editor.md), [Lab Catalog Import And Update Management](openchart-feature-catalog-lab-042-lab-catalog-import-management.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

### Point-of-care, custody, safety, and release

[Point-Of-Care Test Capture](openchart-feature-catalog-lab-043-point-of-care-test-capture.md), [Point-Of-Care Quality Control Logging](openchart-feature-catalog-lab-044-point-of-care-quality-control.md), [Waived Test Compliance Records](openchart-feature-catalog-lab-045-waived-test-compliance-records.md), [Blood Bank Product Request Hooks](openchart-feature-catalog-lab-046-blood-bank-product-request-hooks.md), [Laboratory Delta Check Alerts](openchart-feature-catalog-lab-047-laboratory-delta-check-alerts.md), [Critical Value Call Documentation With Read-Back](openchart-feature-catalog-lab-048-critical-value-call-readback.md), [Specimen Container And Handling Rules](openchart-feature-catalog-lab-049-specimen-container-handling-rules.md), [Corrected Laboratory Result Succession](openchart-feature-catalog-lab-050-corrected-result-succession.md) jointly preserve state, provenance, and accountable handoffs across this part of the diagnostic lifecycle.

The end-to-end joint is order intent → preparation and collection → accession and routing → analysis or external exchange → normalization and filing → critical or routine accountability → longitudinal use and governed release. Technical delivery, specimen receipt, result filing, and clinical acknowledgment are separate facts, so failures cannot be hidden by a single completed flag.

## Emergent behavior

Together the members support a closed diagnostic loop that can explain what was ordered, why it was ordered, which specimen and interface events occurred, what source reported, how values were normalized or corrected, and whether urgent information reached accountable humans. Shared provenance and succession rules make outside results, POCT, microbiology, pathology, and genomics interoperable without pretending their structures are identical.

## Tensions to hold

- Rapid ordering and collection must not weaken indication, consent, specimen, identity, or privilege checks.
- Normalization improves longitudinal comparison, but source codes, methods, units, ranges, and narrative must never be discarded.
- Automated flags, extraction, screening suggestions, and delta checks assist review; none may autonomously diagnose, order, suppress, or treat.
- Operational retries and replay improve reliability, but idempotency and immutable clinical records must prevent duplicate or rewritten evidence.
- Patient access should be timely and transparent while sensitive-result exceptions remain explicit, narrow, reviewable, and policy-versioned.

## Recombination opportunities

- Combine catalog, specimen-requirement, routing, cost, ABN, and connector versions into a single pre-signature feasibility explanation.
- Join pending-result, interface-health, reconciliation, recollection, turnaround-time, and unacknowledged-result projections into service-line assurance dashboards.
- Reuse accession, custody, correction, duplicate, and provenance primitives across central lab, POCT, microbiology, pathology, genomic, and outside-result workflows.
- Feed critical flags, delta checks, corrected-result events, and communication evidence into the named Result Accountability process without duplicating its authority model.

## Frappe realization

- **Core DocTypes:** use submittable `OC Lab Order`, `OC Specimen Collection`, `OC Lab Accession`, `OC Laboratory Result`, and specialized submitted result records; govern catalogs, connector profiles, ranges, mappings, rules, and policies through succession-based versions.
- **Workflows:** separate clinical intent, physical collection, technical transport, analytic result, quality review, accountability handoff, and patient-release states; never collapse them into one status field.
- **Hooks/jobs:** server-side `validate` and `on_submit` enforce identity, version, consent, unit, and succession invariants; idempotent background jobs handle transmissions, retries, pending projections, TAT aggregates, expiry checks, and escalation signals.
- **APIs/surfaces:** guarded `open_chart.api.v1.labs` methods are the supported write surface; permission-aware Frappe Workspaces, Query or Script Reports, Dashboard Charts, Assignments, Notifications, print formats, barcode labels, and portal reads expose role-specific work.

## Boundaries

Owns: laboratory-specific order detail, specimen operations, diagnostic interfaces, result structures, normalization evidence, quality controls, and accountability handoffs. Consumes: patient and encounter context, consent evidence, terminology, coverage context, organization directories, and the named Result Accountability process. Emits: signed lab orders, traceable specimen and transaction events, filed results, urgent handoffs, operational exceptions, and release decisions. Does not own: autonomous clinical action, claims or billing ledgers, external-laboratory authority, blood-bank inventory, or the Result Accountability lifecycle itself.

## Open questions

- Which canonical event envelope can connect orders, specimens, transactions, and results without flattening their different authority and amendment semantics?
- Which terminology, unit, message, barcode, and genomic profiles are mandatory for the first interoperable release?
- Which failures must stop clinical filing or transmission, and which can proceed with explicit uncertainty plus an assigned exception?

## Relationships

[LAB catalog anchor](openchart-feature-catalog-synthesis-lab.md)
