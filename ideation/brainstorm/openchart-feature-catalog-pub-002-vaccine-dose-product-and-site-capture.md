# Vaccine Dose Product And Site Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures dose quantity, manufacturer, lot, expiry, route, body site, and funding details for each vaccine administration.
Topics: openchart-feature-catalog, public-health, frappe, vaccine-dose-details
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-002 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Device camera lot capture** — Read a package barcode while retaining human verification.

## Focus

The product and delivery details needed to interpret, trace, and report one administered dose.

## Behavior

- Vaccinators select a stocked lot or enter an external product source with manufacturer and lot number.
- Dose amount and UCUM unit, expiry, route, and anatomical site are explicit inputs.
- VFC funding source and eligibility snapshot can be attached without changing patient eligibility history.
- Product data fetched from inventory remain snapshots on the accepted administration.
- Expired or quarantined stock blocks selection unless an authorized correction workflow explains historical use.
- Incomplete details remain visibly incomplete and cannot be silently defaulted after acceptance.

## Frappe realization

- **DocTypes:** Add child `OC Immunization Dose Detail` under `OC Immunization Administration` with product, lot, expiry, dose, UCUM unit, route, site, and funding fields.
- **Client behavior:** Filter lot Links by facility, vaccine product, usable state, and date; Fetch From descriptive values into read-only snapshots.
- **Permissions:** Allow vaccinators permlevel 0 entry while protecting funding and override fields at permlevel 1 for `OC Vaccine Program Manager`.
- **Hooks and API:** Validate lot state and required combinations in `validate`; accept details only through the parent guarded API and show them in administration Print Formats.

## Boundaries

Owns: dose-level product and delivery snapshots. Consumes: administration, inventory lot, terminology, and funding program data. Emits: traceable dose details. Does not own: inventory depletion or eligibility decisions.

## Open questions

- Which route and site combinations should be warnings versus hard stops?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
