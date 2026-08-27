# Veterinary Prescription Flag — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Marks and validates veterinary prescriptions with animal, owner, species, weight, prescriber authority, and pharmacy-routing context.
Topics: openchart-feature-catalog, eprescribing, frappe, veterinary-prescribing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-050 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Species-aware dose review hook** — Licensed veterinary rule providers could supply non-autonomous guidance when reliable species data exists.

## Focus

This feature isolates an explicit veterinary mode so animal prescriptions cannot be mistaken for human patient orders. It remains optional and segregated from the human clinical chart model.

## Behavior

- An authorized veterinary prescriber explicitly starts a veterinary prescription and selects an animal and responsible owner.
- Required context includes species, name, weight with timestamp, owner contact, medication, SIG, quantity, and destination.
- The composer visibly labels veterinary context throughout review, print, and transmission.
- Human-only safety rules are not silently applied; unsupported veterinary checks show as unavailable.
- Prescriber credential scope and destination acceptance are validated before signing.
- No animal data is written into `OC Patient` or reused for human medication-history reconciliation.

## Frappe realization

- **DocTypes:** `OC Veterinary Subject` and submittable veterinary variant in the `OC Prescription` family store owner linkage, species, weight, and explicit context flag.
- **Permissions:** Separate `OC Veterinary Prescriber` and veterinary-support roles prevent ordinary human-chart workflows from creating records.
- **Hooks:** Context-specific validation selects eligible rules, credentials, fields, print formats, and adapters.
- **Surfaces:** Distinct composer branding, veterinary prescription Print Format, and segregated workspace reduce context errors.

## Boundaries

Owns: explicit veterinary prescription context and validation. Consumes: animal/owner record, veterinary credentials, medication data, and pharmacy endpoint. Emits: clearly labeled prescription. Does not own: a full veterinary EHR or human patient records.

## Open questions

- Is veterinary support within openChart's long-term product boundary or best delivered as an optional app?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [NewRx Electronic Prescription Routing](openchart-feature-catalog-phr-001-newrx-electronic-prescription-routing.md)
