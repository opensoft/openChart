# Historical Immunization Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Adds prior immunizations with explicit source attribution, date precision, verification state, and import provenance.
Topics: openchart-feature-catalog, public-health, frappe, historical-immunization
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-007 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Document evidence linking** — Associate a scanned card region with each transcribed dose.

## Focus

Historical dose capture that preserves what is known, unknown, and asserted by each source.

## Behavior

- Authorized staff enter vaccine identity, occurrence date or date precision, source type, source organization, and recorder.
- Historical entries are visibly distinct from administrations performed by the local organization.
- Verification states are unverified, document-reviewed, registry-confirmed, and clinician-confirmed.
- Unknown lot, route, or site values remain absent and are not backfilled from product defaults.
- Candidate duplicates are shown before acceptance with compare-and-keep options.
- Corrections create successors and retain the original source wording and evidence attachment.

## Frappe realization

- **DocTypes:** Add submittable `OC Historical Immunization` with source, precision, verification, evidence Attach, predecessor, and CVX fields.
- **Workflow:** Use draft, accepted-unverified, verified, superseded, and entered-in-error states.
- **Permissions:** Permit entry to `OC Immunization User`, verification to `OC Clinician`, and source correction to `OC Health Information Manager`.
- **API and surfaces:** Guard writes under `open_chart.api.v1`, support Data Import with provenance columns, and show source badges in the immunization history.

## Boundaries

Owns: sourced historical-dose assertions. Consumes: patient identity, terminology, and evidence. Emits: schedule-engine candidates with verification labels. Does not own: local administration or external-source authority.

## Open questions

- Which verification states should each schedule rule accept by default?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
