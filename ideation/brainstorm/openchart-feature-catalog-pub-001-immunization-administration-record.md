# Immunization Administration Record — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records a clinically administered vaccine as a coded, attributable, and amendable event in the longitudinal chart.
Topics: openchart-feature-catalog, public-health, frappe, immunization-administration
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-001 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Barcode-assisted administration** — Populate product and lot details from a verified package scan.

## Focus

One accepted immunization event with CVX identity, administration context, clinical authority, and provenance.

## Behavior

- Authorized clinicians select the patient, vaccine CVX code, administration time, performer, and ordering context.
- The form distinguishes administered, not-administered, and entered-in-error outcomes.
- Submission produces an immutable accepted event and updates the patient immunization history.
- Corrections create a successor with reason and predecessor linkage rather than overwriting the event.
- Duplicate checks compare patient, CVX, time, lot, and source but leave disposition to a user.
- Missing required coding or performer authority blocks acceptance and explains the failed invariant.

## Frappe realization

- **DocTypes:** Add submittable `OC Immunization Administration` with `OC PUB-.YYYY.-.#####` naming and Links to `OC Patient`, encounter, CVX code, performer, and predecessor.
- **Workflow:** Use draft, accepted, superseded, and entered-in-error states with succession-based amendment through guarded `open_chart.api.v1` methods.
- **Permissions:** Grant entry to `OC Immunization User`, acceptance to `OC Clinician`, and correction review to `OC Health Information Manager`, constrained by patient User Permissions.
- **Hooks and surfaces:** Validate code, authority, and duplicate candidates on submit; expose a patient timeline, List View, read-only auto-REST, and whitelisted supported writes.

## Boundaries

Owns: the accepted administration event. Consumes: patient identity, CVX terminology, encounter, consent, and provenance. Emits: chart history and downstream registry candidates. Does not own: vaccine scheduling, inventory accounting, or registry transport.

## Open questions

- Which administration outcomes require a cosigner by site policy?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
