# Pharmacy And E-Prescribing — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should collapse OpenEMR's fragmented third-party prescribing stack (Ensora/NewCrop, WENO, paid EPCS add-ons) into one governed medication workflow spanning e-Rx, real-time benefit, EPCS identity proofing, PDMP, electronic prior authorization, and pharmacogenomic checks.
Topics: openchart-feature-list, eprescribing, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **One-stack e-prescribing** — NewRx/CancelRx/RxRenewal routing, pharmacy directory, and med-history exchange without per-clinic subscription sprawl.
- **Integrated EPCS** — identity proofing, supervised credential enrollment, two-factor signing, and reporting built into the platform's auth model.
- **Real-time benefit and formulary checks** — price/alternative/coverage signals at the moment of prescribing.
- **Electronic prior authorization** — ePA requests and status tracked as first-class objects attached to the prescription.
- **PDMP one-tap access** — state prescription-monitoring lookup inside the prescribing flow.
- **Pharmacogenomic decision support** — drug–gene conflict warnings when genotype results exist (Expanse pattern).

## Focus

How does openChart deliver enterprise-grade medication management without forcing clinics to assemble three vendors the way OpenEMR users must?

## Current state: OpenEMR baseline

Core OpenEMR covers medication/prescription records, drug and allergy lists with interaction lookup, prescription print/fax/email, RxNorm import, in-house dispensary, and dispensing reports. Electronic prescribing to pharmacies is NOT core: it requires Ensora Health (formerly NewCrop) subscription services or the WENO Exchange module (7.0.2+), each a separate contract; EPCS is an additional paid add-on requiring external identity proofing. PDMP access needs Bamboo Health PMP Gateway (third-party). There is no real-time benefit engine, no electronic prior authorization, no pharmacogenomic CDS.

Sources: open-emr.org ePrescribe wiki; Modules catalog; Release Features wiki.

## Enterprise gap candidates

- Oracle bundles Electronic Prescription Interoperability (med history, drug price, prior-auth status, opioid-management info), Surescripts connectivity, and Workflow Authentication for EPCS with supervised enrollment and MFA.
- MEDITECH Expanse e-Prescribing pairs real-time benefit checks, electronic prior authorization, and one-tap PDMP access in flow; adds pharmacogenomic drug–gene decision support.
- Epic Willow spans ambulatory-to-inpatient medication lifecycle; specialty-pharmacy depth (Compass Rose benefit investigation, adherence tracking, MSOT authorization routing) and AI prior-auth drafting are emerging differentiators.
- All three treat closed-loop administration (BCMA barcode scanning) as table stakes for facility care.

## Proposed feature set for openChart

Parity floor: med/allergy records, interaction checking, RxNorm terminology, dispensary/inventory. Adopted gaps: certified e-Rx routing bundled as first-party capability (partner network behind a single contract); EPCS via platform-native identity proofing and signing ceremony; real-time benefit/formulary at prescribe time; ePA object model with payer round-trip status; PDMP gateway integration; drug–gene CDS keyed to stored genotype observations; specialty-medication work queues (authorization → benefit check → dispensing → adherence follow-up). Twist: every prescription state transition is provenance-audited end to end.

## Interfaces and boundaries

Consumes: patient demographics and coverage from registration, allergy/med history from clinical-documentation, encounter context, formulary/benefit feeds from external networks. Emits: dispense events and adherence data to analytics-and-population-health, charge hints to revenue-cycle, genotype queries to labs-and-diagnostics. Owns the prescription lifecycle; does not own pharmacy fulfillment outside the dispensary.

## Alternatives and tensions

Partner-first (WENO/Surescripts-only) minimizes build cost but recreates OpenEMR's fragmentation complaint. Bundling certification costs (Surescripts, EPCS audits, DIR fees logic) raises platform operating burden. Pharmacogenomics requires lab partnerships and guideline content that age. Specialty-pharmacy workflows may be premature for openChart's initial clinic-scale market.

## Open questions

- Which single e-Rx network partner gives the best national pharmacy coverage for launch?
- Does EPCS identity proofing run through an existing IAFC-certified partner or in-house?
- Is specialty pharmacy a v1 domain or a later expansion gated by market pull?

## Relationships

Clustered in [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md). Adjacent: [Clinical Orders And Decision Support](openchart-feature-list-orders-and-cds.md), [Labs And Diagnostics](openchart-feature-list-labs-and-diagnostics.md).
