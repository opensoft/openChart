# Labs And Diagnostics — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should ship turnkey, monitored bidirectional lab exchange plus genomic ordering with discrete results, replacing OpenEMR's works-if-you-integrate-it HL7 plumbing and matching the discrete-result expectations Epic set with Aura.
Topics: openchart-feature-list, laboratory, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Turnkey reference-lab exchange** — pre-built Quest/Labcorp-class bidirectional connections with credential onboarding, not SFTP projects.
- **Exchange observability** — order/result pipeline monitoring: queue depth, mapping failures, reconciliation reports, alerting on stuck transactions.
- **Specimen lifecycle tracking** — collection → accession → result linkage with barcoded specimen identity.
- **Genomic ordering and discrete results** — genetic tests ordered in workflow; variants returned as structured data feeding pharmacogenomic CDS.
- **Outside-result normalization** — imported results mapped to local LOINC panels, deduplicated, and reconciled against chart values (Seamless Exchange pattern applied to labs).

## Focus

What makes laboratory data flow reliably enough in openChart that a clinic never hires an interface engineer?

## Current state: OpenEMR baseline

OpenEMR includes procedure-order forms, lab orders, electronic result collection linked to charts, pending-order reports, address-book lab directories, and HL7 2.x-oriented interfaces. Real bidirectional connectivity depends on per-lab interfaces, SFTP/file-drop setups, Mirth Connect deployments, Quest Quantum Hub module, or custom LIS work — mapping, patient matching, transport reliability, and error reconciliation all fall on the implementer. Immunization registry exchange shows the same pattern (formats supported, state-specific configuration required).

Sources: open-emr.org Features wiki; Modules catalog; CapMinds interoperability guide; Immunization Registries wiki.

## Enterprise gap candidates

- Epic Beaker provides LIS-grade specimen tracking and integrated pathology; Aura returns genomic results discretely rather than PDFs.
- Oracle carries PathNet heritage (accessioning, microbiology, result verification) and Connection Hub-style centralized exchange management across labs/diagnostics/public health.
- MEDITECH integrates lab/microbiology/outreach/phlebotomy modules with mobile phlebotomy capture and smart-pump/device connectivity around diagnostics.
- The common enterprise thread: exchange is a managed product with operations tooling, not an integration project.

## Proposed feature set for openChart

Parity floor: order/result data model, result display in charts, pending-order reporting. Adopted gaps: certified bidirectional connectors to major reference labs shipped and operated as product; pipeline observability dashboard with failure alerts and reconciliation views; barcoded specimen tracking; LOINC-normalized outside-result ingestion with dedupe/reconcile UI; genomic order class returning structured variant observations that feed pharmacy drug–gene checks. Twist: exchange health is itself a monitored clinical safety metric with published uptime semantics.

## Interfaces and boundaries

Consumes: orders from orders-and-cds, patient demographics, specimen events from point-of-care/mobile capture. Emits: verified results into the longitudinal record and analytics-and-population-health, genotype observations to pharmacy-and-eprescribing, abnormal-result events into the accountability loop. Owns lab order fulfillment state and result normalization; does not own LIS bench operations.

## Alternatives and tensions

Building connector operations in-house vs certifying through an aggregator hub changes margin and liability profiles. Deep LIS features (microbiology detail, anatomic pathology) may exceed ambulatory scope yet enterprise buyers expect them. Genomic results carry consent and re-identification sensitivities beyond ordinary labs.

## Open questions

- Launch connector set: which two reference labs and what aggregator fallback?
- Are genomics v1 or v2 given consent complexity?
- What SLA semantics can an open-source project honestly publish for exchange uptime?

## Relationships

Clustered in [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md). Adjacent: [Imaging Workflows](openchart-feature-list-imaging-workflows.md), [Interoperability And Exchange](openchart-feature-list-interoperability.md), [Pharmacy And E-Prescribing](openchart-feature-list-pharmacy-and-eprescribing.md).
