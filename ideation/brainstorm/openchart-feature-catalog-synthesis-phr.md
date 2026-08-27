# Synthesis: Pharmacy And E-Prescribing — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects 55 first-party prescribing, medication-safety, benefit, pharmacy-network, specialty, dispensing, inventory, and continuity capabilities into one accountable medication pathway.
Topics: openchart-feature-catalog, eprescribing, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog synthesis PHR (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **First-party pharmacy operations workspace** — A role-aware command center could combine prescriptions, network exceptions, renewals, authorizations, dispensing, stock risk, and recalls without replacing each submitted source record.

## Focus

This synthesis shows how the PHR capabilities form an end-to-end pharmacy and e-prescribing domain that can be delivered independently of paid third-party modules. The design keeps human prescribing authority, provenance, consent, immutable accepted records, and non-autonomous clinical decision support intact.

## Members and their joints

### Prescription composition, destination, and accountable routing

The prescribing path begins with explicit pharmacy selection and ends with a signed, immutable prescription whose transport can be observed and recovered independently.

- [PHR-001 NewRx Electronic Prescription Routing](openchart-feature-catalog-phr-001-newrx-electronic-prescription-routing.md) — creates, signs, and routes a NewRx message.
- [PHR-002 Pharmacy Directory Search](openchart-feature-catalog-phr-002-pharmacy-directory-search.md) — finds current, connected pharmacy endpoints.
- [PHR-003 Patient Pharmacy Preference](openchart-feature-catalog-phr-003-patient-pharmacy-preference.md) — supplies revocable destination guidance.
- [PHR-007 Prescription Status Tracking](openchart-feature-catalog-phr-007-prescription-status-tracking.md) — reconciles local and pharmacy-reported states.
- [PHR-008 Structured SIG Builder](openchart-feature-catalog-phr-008-structured-sig-builder.md) — preserves coded directions and deterministic rendering.
- [PHR-009 Free-Form SIG Fallback](openchart-feature-catalog-phr-009-free-form-sig-fallback.md) — handles exceptional directions with explicit limitations.
- [PHR-010 Prescription Review And Signing](openchart-feature-catalog-phr-010-prescription-review-and-signing.md) — binds ordinary human review and signature evidence.
- [PHR-050 Veterinary Prescription Flag](openchart-feature-catalog-phr-050-veterinary-prescription-flag.md) — segregates animal prescriptions from human charts.

### Controlled-substance authority and safeguards

Schedule classification drives credential, quantity, PDMP, and EPCS requirements, but the prescriber remains the only actor who applies clinical authority.

- [PHR-011 EPCS Two-Factor Signing Ceremony](openchart-feature-catalog-phr-011-epcs-two-factor-signing-ceremony.md) — binds two-factor assurance to the exact prescription digest.
- [PHR-012 Prescriber Identity-Proofing Enrollment](openchart-feature-catalog-phr-012-prescriber-identity-proofing-enrollment.md) — governs supervised proofing and factor enrollment.
- [PHR-013 Prescriber Credential Eligibility](openchart-feature-catalog-phr-013-prescriber-credential-eligibility.md) — evaluates effective professional and jurisdictional authority.
- [PHR-014 PDMP One-Tap Lookup](openchart-feature-catalog-phr-014-pdmp-one-tap-lookup.md) — retrieves state-selected monitoring evidence with access logging.
- [PHR-015 Controlled-Substance Quantity Guardrails](openchart-feature-catalog-phr-015-controlled-substance-quantity-guardrails.md) — checks quantity arithmetic and effective limits.
- [PHR-016 DEA Schedule Display](openchart-feature-catalog-phr-016-dea-schedule-display.md) — exposes source-versioned schedule classification everywhere it matters.

### Benefit, affordability, authorization, and specialty access

Benefit inquiries and specialty coordination form a long-running access pathway in which payer facts, chart evidence, authorizations, and shipment milestones retain separate provenance.

- [PHR-017 Real-Time Benefit And Formulary Check](openchart-feature-catalog-phr-017-real-time-benefit-and-formulary-check.md) — retrieves patient-specific coverage and alternatives.
- [PHR-018 Drug Price Transparency](openchart-feature-catalog-phr-018-drug-price-transparency.md) — compares sourced cost estimates and assumptions.
- [PHR-019 Prescriber Formulary Favorites](openchart-feature-catalog-phr-019-prescriber-formulary-favorites.md) — accelerates selection without carrying forward patient-specific approval.
- [PHR-020 Therapeutic Alternative Suggestion Hooks](openchart-feature-catalog-phr-020-therapeutic-alternative-suggestion-hooks.md) — exposes non-autonomous, evidence-labeled suggestion adapters.
- [PHR-021 Electronic Prior Authorization Workflow](openchart-feature-catalog-phr-021-electronic-prior-authorization-workflow.md) — manages payer questions, submission, and determination states.
- [PHR-022 Prior-Authorization Evidence Assembly](openchart-feature-catalog-phr-022-prior-authorization-evidence-assembly.md) — creates minimum-necessary, cited evidence packets.
- [PHR-023 Specialty Benefit Investigation](openchart-feature-catalog-phr-023-specialty-benefit-investigation.md) — resolves benefit, network, site-of-care, and assistance facts.
- [PHR-024 Specialty Authorization Tracking](openchart-feature-catalog-phr-024-specialty-authorization-tracking.md) — coordinates approvals, appeals, effective periods, and renewal milestones.
- [PHR-025 Specialty Dispensing Coordination](openchart-feature-catalog-phr-025-specialty-dispensing-coordination.md) — tracks pharmacy onboarding, shipment, receipt, and exceptions.

### Inbound requests, history, exceptions, and transport resilience

Inbound pharmacy and patient messages enter dedicated review workflows; correlation and retry controls preserve intent without silently mutating accepted records.

- [PHR-004 CancelRx Cancellation Routing](openchart-feature-catalog-phr-004-cancelrx-cancellation-routing.md) — communicates cancellation while preserving uncertainty about external outcome.
- [PHR-005 RxRenewal Pharmacy Request Processing](openchart-feature-catalog-phr-005-rxrenewal-pharmacy-request-processing.md) — routes pharmacy renewals through matching and prescriber decision.
- [PHR-006 Portal Refill Request Queue](openchart-feature-catalog-phr-006-portal-refill-request-queue.md) — keeps patient requests distinct from prescriptions.
- [PHR-026 Network Medication History Retrieval](openchart-feature-catalog-phr-026-network-medication-history-retrieval.md) — stages source-labeled external medication candidates.
- [PHR-027 Medication History Reconciliation Inbox](openchart-feature-catalog-phr-027-medication-history-reconciliation-inbox.md) — records clinician dispositions before local acceptance.
- [PHR-053 Transmission Retry And Dead-Letter Queue](openchart-feature-catalog-phr-053-transmission-retry-and-dead-letter-queue.md) — recovers failed or indeterminate messages idempotently.
- [PHR-054 Pharmacy Response Exception Workflow](openchart-feature-catalog-phr-054-pharmacy-response-exception-workflow.md) — handles clarification, change, denial, and unable-to-fill responses.

### Explainable medication-safety review

Safety checks share one evidence and disposition model while retaining their distinct inputs, uncertainty, severity policy, and clinical meaning.

- [PHR-028 Drug-Drug Interaction Checking](openchart-feature-catalog-phr-028-drug-drug-interaction-checking.md) — evaluates ingredient interactions with severity tiers.
- [PHR-029 Drug-Allergy Interaction Checking](openchart-feature-catalog-phr-029-drug-allergy-interaction-checking.md) — explains direct and class-mediated allergy matches.
- [PHR-030 Duplicate-Therapy Detection](openchart-feature-catalog-phr-030-duplicate-therapy-detection.md) — identifies exact, ingredient, class, and transitional overlap.
- [PHR-031 Dose-Range And Age Checking](openchart-feature-catalog-phr-031-dose-range-and-age-checking.md) — checks age-, weight-, and indication-aware dose ranges.
- [PHR-032 Renal And Hepatic Adjustment Guidance](openchart-feature-catalog-phr-032-renal-and-hepatic-adjustment-guidance.md) — links guidance to selected labs and calculations.
- [PHR-033 Pregnancy And Lactation Warnings](openchart-feature-catalog-phr-033-pregnancy-and-lactation-warnings.md) — uses time-bounded, privacy-aware reproductive context.
- [PHR-034 Pharmacogenomic Drug-Gene Alerts](openchart-feature-catalog-phr-034-pharmacogenomic-drug-gene-alerts.md) — evaluates verified genomic results against versioned guidance.
- [PHR-035 Clinical Alert Override Documentation](openchart-feature-catalog-phr-035-clinical-alert-override-documentation.md) — captures accountable dispositions and follow-up commitments.

### In-house dispensing, packaging, and patient support

A verified dispense links prescription intent to physical product and patient handoff while counseling, packaging, samples, synchronization, and follow-up remain independently evidenced.

- [PHR-036 In-House Dispensary Dispensing Record](openchart-feature-catalog-phr-036-in-house-dispensary-dispensing-record.md) — records pharmacist-verified product and lot handoff.
- [PHR-042 Dispensing Label Printing](openchart-feature-catalog-phr-042-dispensing-label-printing.md) — controls label content, barcode, print, and reprint evidence.
- [PHR-043 Unit-Dose And Blister-Pack Support](openchart-feature-catalog-phr-043-unit-dose-and-blister-pack-support.md) — traces medication components into verified packs.
- [PHR-044 Sample Medication Dispensing Log](openchart-feature-catalog-phr-044-sample-medication-dispensing-log.md) — maintains accountable sample issuance and lot history.
- [PHR-045 Medication Synchronization Programs](openchart-feature-catalog-phr-045-medication-synchronization-programs.md) — aligns refill cycles through patient-approved coordination.
- [PHR-046 Adherence Follow-Up Tasks](openchart-feature-catalog-phr-046-adherence-follow-up-tasks.md) — routes documented barriers without algorithmic labeling.
- [PHR-047 Patient Counseling At Dispense](openchart-feature-catalog-phr-047-patient-counseling-at-dispense.md) — records counseling offer, delivery, topics, and outcomes.
- [PHR-049 Compounding Order Capture](openchart-feature-catalog-phr-049-compounding-order-capture.md) — represents detailed compounded prescription intent.

### Inventory, procurement, fallback, and medication-risk operations

Lot-aware stock, procurement, expiry, returns, recalls, and fallback renditions keep physical and communication risks traceable without crossing into claims or autonomous clinical action.

- [PHR-037 Dispensary Inventory Counts](openchart-feature-catalog-phr-037-dispensary-inventory-counts.md) — maintains lot-aware stock and reconciled counts.
- [PHR-038 Medication Reorder Points](openchart-feature-catalog-phr-038-medication-reorder-points.md) — creates reviewable replenishment requests.
- [PHR-039 Multi-Store Inventory Visibility](openchart-feature-catalog-phr-039-multi-store-inventory-visibility.md) — exposes policy-filtered availability across locations.
- [PHR-040 Supplier Purchase Orders](openchart-feature-catalog-phr-040-supplier-purchase-orders.md) — governs medication procurement and receipt discrepancies.
- [PHR-041 Expired-Stock Quarantine](openchart-feature-catalog-phr-041-expired-stock-quarantine.md) — uses scheduled scans to remove expired lots from availability.
- [PHR-048 Returned-Medication Destruction Log](openchart-feature-catalog-phr-048-returned-medication-destruction-log.md) — preserves custody, witnesses, and destruction disposition.
- [PHR-051 Prescription Print Report](openchart-feature-catalog-phr-051-prescription-print-report.md) — produces policy-controlled signed paper or PDF renditions.
- [PHR-052 Outbound Pharmacy Fax Fallback](openchart-feature-catalog-phr-052-outbound-pharmacy-fax-fallback.md) — sends verified fallback disclosures with delivery evidence.
- [PHR-055 Drug Recall Lot Traceability](openchart-feature-catalog-phr-055-drug-recall-lot-traceability.md) — matches recalls to stock, dispenses, samples, packs, and recipients.

## Frappe realization

- **Submittable prescription family:** Use submittable `OC Prescription`, controlled and veterinary context variants, `OC Prescription Cancellation`, `OC Dispense`, and related accepted records with OC naming series, immutable signed snapshots, docstatus semantics, and succession-based amendments through guarded `open_chart.api.v1` methods.
- **Stateful workflows:** Frappe Workflows govern RxRenewal matching and prescriber decisions, portal refills, ePA question/answer/submission/determination, specialty authorizations, pharmacy exceptions, dispensing verification, inventory variances, returns, and recalls with role-separated transitions and Workflow Actions.
- **Clinical evidence graph:** Child tables and Dynamic Links preserve SIG components, safety findings, source record versions, evidence citations, status events, network correlation, lot lineage, consent, authority, and disclosure provenance without creating a second source of truth.
- **Roles and APIs:** `OC Prescriber`, `OC EPCS Prescriber`, `OC Pharmacist`, `OC Pharmacy Technician`, `OC Prior Authorization Specialist`, `OC Specialty Pharmacy Coordinator`, inventory, credentialing, integration, privacy, and portal roles use DocPerms, permlevels, User Permissions, guarded write APIs, and read-only auto-REST where appropriate.
- **Barcode and print surfaces:** Native Frappe Barcode fields support product, lot, label, sample, pack, receipt, count, return, and destruction verification; governed Jinja Print Formats render dispensing labels, patient instructions, prescription reports, purchase orders, manifests, and permitted fax attachments.
- **Jobs and integration:** RQ jobs, authenticated adapters, idempotency keys, immutable payload digests, realtime events, and `scheduler_events` handle transport, polling, retries, renewal reminders, authorization expiry, cycle generation, reorder evaluation, daily expiry scans, dead letters, and recall escalation.
- **Workspaces and reports:** Role-aware Desk workspaces, Kanban/Gantt/Calendar views, portal pages, Query Reports, Script Reports, Number Cards, dashboards, assignment rules, and notifications expose queues and exceptions while keeping sensitive clinical, genomic, controlled, and financial data segmented.

## Boundaries

Owns: first-party prescription intent, accountable signing, pharmacy message orchestration, medication-safety review, authorization evidence, in-house dispensing, pharmacy inventory, and provenance-rich operational workflows. Consumes: patient identity, consent and proxy authority, accepted medication/allergy/observation records, terminology and rules releases, prescriber credentials, coverage, pharmacy networks, payer services, and supplier/recall sources. Emits: signed prescriptions, pharmacy messages, review tasks, determinations, dispense and stock events, patient-safe statuses, labels, reports, and audit evidence. Does not own: claims adjudication, general revenue cycle, external pharmacy decisions, medication administration, autonomous clinical decisions, or proprietary network and clinical-rule content.

## Emergent behavior

Together, the members create a closed but non-autonomous medication pathway: a prescriber composes and signs accountable intent; safety, benefit, authority, and patient context are reviewed with versioned evidence; network messages and exceptions remain correlated; authorization and specialty access progress through staffed workflows; dispensing links intent to a verified physical product; and lot-aware inventory, expiry, destruction, and recall controls preserve physical accountability. First-party orchestration makes these capabilities independently deployable while adapters isolate external networks and licensed data.

## Tensions to hold

- Fast prescribing and favorites must coexist with current patient-specific safety, benefit, identity, credential, and destination review.
- Rich decision support improves context but can create alert fatigue, proprietary-data dependencies, bias, and unsafe automation if suggestions are not explainable and human-controlled.
- Pharmacy status, benefit, price, and medication-history feeds are useful but incomplete; the chart must display source and uncertainty rather than infer adherence or clinical truth.
- EPCS, PDMP, genomic, controlled-inventory, and financial data demand stronger access segmentation without fragmenting the prescriber's accountable review.
- In-house inventory and procurement should remain independently usable while offering optional integration seams to ERPNext or openPractice rather than transferring clinical authority.
- Print and fax fallbacks improve resilience but increase duplicate, privacy, tamper, and delivery risk and therefore require explicit policy and evidence.

## Recombination opportunities

- Combine prescription status, transport dead letters, pharmacy exceptions, renewals, and CancelRx into a medication communications command center.
- Combine real-time benefit, price, ePA evidence, specialty investigation, and authorization tracking into a patient-access pathway with cited payer facts.
- Combine safety checks, source data quality, override dispositions, and follow-up commitments into a medication-safety governance program.
- Combine dispensing, native barcode verification, packaging, counseling, synchronization, and follow-up into an accountable community-pharmacy service model.
- Combine inventory counts, reorder rules, multi-store visibility, purchase orders, expiry scans, destruction, and recalls into a lot-level medication supply chain.
- Combine print, fax, and adapter conformance with synthetic fixtures into an outage and non-connected-pharmacy resilience kit.

## Open questions

- Which prescribing, pharmacy-network, benefit, and clinical-rule standards can openChart implement openly, and which production services require licensed adapters or certification?
- Which accepted pharmacy records require Frappe cancellation semantics versus succession-only correction under clinical provenance policy?
- How should multi-site deployments divide patient, prescriber, inventory, controlled-substance, and pharmacy-endpoint authority across benches?
- What minimum evidence and governance threshold is required before enabling each decision-support source?
- Which patient-facing prescription, authorization, price, shipment, counseling, and recall states are safe and useful to expose through the portal?

## Relationships

[Catalog anchor: Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md)
