# Analytics And Population Health — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should pair governed registries, cohort building, and claims+clinical integration with radically open semantic metric definitions and exports — delivering Healthy Planet/Care Compass capability while rejecting Cosmos-style closed data moats as a design choice.
Topics: openchart-feature-list, population-health, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Governed cohort builder** — interactive filtering across clinical/financial/demographic data with saved, shareable definitions (SlicerDicer analog, open implementation).
- **Actionable registries** — care-gap cohorts driving outreach tasks through scheduling/messaging, closing loops measurably (Care Compass/Healthy Planet pattern).
- **Reproducible semantic layer** — every metric (no-show rate, gap-closure rate, denial rate) has a public definition, version history, and query implementation.
- **Claims ingestion** — paid-claims reconciliation joining payer data to clinical records for value-based work.
- **Risk stratification and SDOH** — hierarchical conditions, readmission risk, social-determinants screening with geospatial context (Determinants of Health analog).
- **Natural-language reporting** — plain-language question to report draft, SideKick-style, scoped by permission.

## Focus

What analytics architecture gives openChart clinics enterprise population-health capability while making data exit easy — and does that openness become the differentiator?

## Current state: OpenEMR baseline

OpenEMR ships broad operational reports (appointments, encounters, prescriptions, referrals, immunizations, labs, procedures, sales, collections, insurance distribution, EDI history), CQM/eCQM calculation with QRDA support, AMC calculations, syndrome-surveillance reports, custom SQL reporting, multipage PDF/CSV export. Advanced analytics requires SQL expertise, custom reports, external BI, or warehouses; there are no cohort builders, registries-with-outreach, claims feeds, risk models, or semantic metric definitions. Reviewers consistently flag analytics depth as a top gap versus enterprise platforms.

Sources: open-emr.org Features wiki; Release Features wiki; Medesk/SoftwareFinder reviews.

## Enterprise gap candidates

- Epic: SlicerDicer cohort exploration, Radar dashboards, Healthy Planet risk stratification/outreach, claims reconciliation into the longitudinal record, Payer Platform quality-data collaboration, Cosmos de-identified research network with point-of-care similar-patient evidence, Curiosity foundation models.
- Oracle: HealtheIntent lineage, AI Data Platform (EHR-agnostic warehouse), Quality Management (300+ disease categories, care gaps), Determinants of Health geospatial SDOH, Learning Health Network scale claims, Lights On Network utilization analytics, Fusion Cloud financial integration.
- MEDITECH: Business and Clinical Analytics dashboards, Data Repository, Expanse Care Compass real-time registries, Community Care Transitions Portal for post-acute coordination, remote-monitoring-fed registries, no-show prediction.
- Moat observation: incumbents monetize data gravity; none offer reproducible open metric semantics as policy.

## Proposed feature set for openChart

Parity floor: OpenEMR's report breadth + CQM/eCQM currency. Adopted gaps: registry engine where every cohort can emit outreach tasks into scheduling-and-access and messaging queues; cohort builder with saved/shareable definitions and permission scoping; claims ingestion pipeline reconciling 835/paid-claim data against clinical activity; SDOH screening instruments feeding stratification; NL-to-report drafting under permission scope; optional federated research-cohort contribution with explicit consent governance (the open answer to Cosmos). Twist: the semantic layer is versioned, documented, and exportable — metrics survive migration, audits reproduce, and BI tools plug into definitions not raw tables.

## Interfaces and boundaries

Consumes: signed clinical facts, order/result outcomes, financial events from revenue-cycle, claims via interoperability channels, patient-reported/device data from patient-engagement, access funnel metrics from scheduling-and-access. Emits: outreach cohorts to engagement surfaces, surveillance triggers to orders-and-cds, research extracts under governance. Owns metric definitions and aggregate stores; does not own raw-source systems of record.

## Alternatives and tensions

Building a warehouse vs federated-query-over-live-systems changes latency/freshness tradeoffs. Research-network ambitions invite governance burden small teams cannot staff initially. Claims ingestion requires payer relationships independent of EHR deployment. Open metric semantics expose unflattering operational numbers internally — political friction is real.

## Open questions

- Warehouse-first or semantic-layer-over-live-queries for v1?
- Is federated research contribution a funded roadmap item or aspiration?
- Which ten metrics get canonical v1 definitions?

## Relationships

Clustered in [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md). Adjacent: [Revenue Cycle](openchart-feature-list-revenue-cycle.md), [Clinical AI And Governance](openchart-feature-list-clinical-ai.md).
