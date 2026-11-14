# Synthesis: Business And Exchange — Brainstorm

Status: brainstorm
Kind: architecture
Summary: revenue cycle and interoperability are one flow in openChart — eligibility, claims, remittances, outside records, and public-health exchange all ride the same governed pipeline with observability and provenance, replacing OpenEMR's clearinghouse-assembly and interface-project economics.
Topics: openchart-feature-list, business-exchange-synthesis, synthesis, revenue-cycle, interoperability
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **One exchange spine, many payloads** — X12 (270/271/837/835), FHIR, C-CDA/Direct, lab HL7, and public-health submissions share transport, monitoring, retry, and reconciliation infrastructure.
- **Financial provenance query** — order → charge → claim → denial → appeal as one traversable chain via supported API.
- **Outside-data normalization service** — external records (clinical or payer) matched, deduplicated, cleansed, presented side-by-side, selectively written back with approval.
- **Exchange health as product UI** — every clinic sees its own pipeline dashboard: stuck transactions, mapping failures, payer response times.

## Members and their joints

Atomic members: [Revenue Cycle](openchart-feature-list-revenue-cycle.md), [Interoperability And Exchange](openchart-feature-list-interoperability.md).

### Eligibility ↔ Network participation

Real-time 270/271 rides the same managed connectivity that carries clinical exchange; a clinic's network membership is established once and consumed by both money and data flows. Oracle bundles exactly this way; OpenEMR makes clinics assemble it from clearinghouse contracts.

### Claims ↔ Outside records

Denials frequently cite missing documentation that exists in imported outside records — normalization that surfaces those records into appeal evidence turns interop plumbing into recovered revenue. This recombination is invisible in vendor checklists but decisive in practice.

### Remittances ↔ Normalization

835 posting requires the same identifier-matching discipline as patient-record matching; one matching engine with audit trails serves both, instead of two half-built matchers.

### Public health ↔ Reporting

Registry/syndromic/electronic-case-reporting pipelines feed quality measurement; managed connections mean eCQM attestation stops being a quarterly fire drill.

## Emergent behavior

The pair makes "operational data health" a measurable property of the deployment: percentage of transactions acknowledged, denial rate by payer with root causes, outside-record reconciliation completeness. Clinics can finally see — and vendors can be judged on — the reliability OpenEMR leaves implicit. Financially, the combination shortens days-in-AR through faster eligibility and evidence-rich appeals.

## Tensions to hold

Owning exchange operations concentrates liability (a failed submission is now our failure, not a clearinghouse's). Normalization write-back trades clinician review time against record completeness. Payer-behavior heterogeneity resists clean taxonomies; scope discipline on v1 payer coverage matters more than ambition.

## Recombination opportunities

The provenance chain recombines with [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md) for value-based-care attribution; network membership recombines with [Platform Security And Deployment](openchart-feature-list-platform-and-security.md) managed-cloud tier as turnkey compliance; estimates recombine with [Scheduling And Patient Access](openchart-feature-list-scheduling-and-access.md) self-service booking.

## Open questions

- Build the exchange spine on an existing open-source engine (Mirth-class) or first-party?
- Does one aggregator partnership cover both clinical networks and X12 clearinghouse functions?
- Which three payers anchor v1 denial-workflow normalization?

## Relationships

Owned by [Overview](openchart-feature-list-overview.md). Cross-cluster: [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md).
