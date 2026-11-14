# Revenue Cycle — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should make the order-to-charge-to-claim-to-denial chain a provenance-linked, natively-worked pipeline with pre-service estimates and AI-assisted coding under human review, instead of OpenEMR's broad-but-clearinghouse-dependent billing core.
Topics: openchart-feature-list, revenue-cycle, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Provenance-linked financial chain** — every charge traceable to its order/encounter/documentation; every claim to its charges; every denial to its claim; appeals linked to denials.
- **Native denial management** — worklists by denial reason, appeal generation with evidence assembly, payer-performance scorecards.
- **Pre-service estimates** — patient responsibility estimates at scheduling/check-in feeding payment plans.
- **AI-assisted coding** — documentation-derived code suggestions (Oracle Clinical AI Agent pattern) always requiring coder/clinician confirmation.
- **Charge-capture automation** — infusion/injection-class charges generated from discrete documentation events.
- **Unified patient statements** — cross-encounter balances on one statement with portal/SMS payment paths.

## Focus

Which revenue-cycle capabilities let openChart run a clinic's revenue without clearinghouse-assembled point solutions, and give finance leaders audit-grade visibility OpenEMR cannot?

## Current state: OpenEMR baseline

OpenEMR's billing core is unusually deep for open source: fee sheets, CPT/HCPCS/ICD-10/SNOMED coding, professional and institutional claims (837), UB-04, X12 5010, ERA/835 posting, EOB entry, ledgers/invoices/statements/dunning, AR, batch payments, adjustments/refunds, collections reporting, payment-gateway hooks. But live submission, eligibility (270/271 transmission), claim status, and ERA delivery all ride on configured clearinghouses (Office Ally, ClaimRev module, Waystar-era partners); prior authorization is a paid module; denial management is rudimentary; estimates/payment plans are thin; no native coding assistance.

Sources: open-emr.org Medical Billing features page; Features wiki; ClaimRev Clearinghouse Module wiki; Modules catalog.

## Enterprise gap candidates

- Epic Resolute PB/HB: enterprise charge/claims/remittance with transaction lineage structures, patient estimates, MyChart/web/SMS/guest-pay digital channels, and emerging AI coding/denial-follow-up agents visible in its AI interaction exports.
- Oracle Millennium Patient Accounting plus RevElate transition; clinical-to-financial automation (infusion charge generation from documentation; AI professional-fee coding suggestions for review).
- MEDITECH Practice Management/Patient Accounting Desktop packaging eligibility, authorizations, claims, remittances, denial follow-up; AI claim-denial agent generating appeal action plans; one unified statement across acute/ambulatory/LTC settings; Quality Vantage regulatory/reimbursement dashboards.
- KLAS reality check: Oracle customers still report RCM difficulty — breadth ≠ usable RCM; workflow quality is the opening.

## Proposed feature set for openChart

Parity floor: full OpenEMR-equivalent billing core (coding, 837/835, ledger, statements, AR). Adopted gaps: first-party clearinghouse integration operated as product with status/999/277 handling surfaced in-app; denial-management workbench (reason taxonomy, appeal builder attaching chart evidence, payer scorecards); estimate engine keyed to contracted rates + benefits data; payment plans and saved-payment consent flows; charge-capture automation from discrete clinical events; coding-suggestion service producing draft codes with confidence + citation into documentation, human-confirm required. Twist: financial provenance query ("show me everything between this order and this denial") is a supported API, not a forensic project.

## Interfaces and boundaries

Consumes: encounters/charges from clinical-documentation and orders-and-cds, coverage/eligibility from registration, benefit responses from payers via interoperability channels, payments from patient-engagement surfaces. Emits: financial cohorts and denial patterns to analytics-and-population-health, deposit/prepayment hooks to scheduling-and-access. Owns the financial lifecycle; does not own payer contracts or clinical coding policy.

## Alternatives and tensions

Owning clearinghouse operations adds compliance/ops load vs pure partner resale. AI coding suggestions risk upcoding scrutiny without rigorous human-in-loop defaults and monitoring. Estimate accuracy depends on payer contract data quality clinics may not hold. Denial workflows need payer-response normalization across hundreds of payers — scope discipline matters.

## Open questions

- Clearinghouse strategy: certify direct, aggregate through one hub partner, or both tiers?
- Is RevElate-style rearchitecture a cautionary tale to avoid (ship stable core first)?
- Which denial reason taxonomy — X12 CARC-native or a curated operational layer?

## Relationships

Clustered in [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md). Adjacent: [Scheduling And Patient Access](openchart-feature-list-scheduling-and-access.md), [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md).
