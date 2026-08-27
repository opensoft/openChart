# Syndromic Surveillance Export — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces policy-scoped, auditable syndromic surveillance feeds from qualifying encounters with data-minimization and delivery controls.
Topics: openchart-feature-catalog, public-health, frappe, syndromic-surveillance
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-023 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Feed quality observability** — Monitor timeliness, completeness, rejection, and field conformance without exposing payload content.

## Focus

Reliable surveillance export under explicit jurisdiction, facility, encounter, and disclosure profiles.

## Behavior

- Administrators configure which facilities, encounter classes, and dates qualify for each destination.
- Export candidates snapshot only approved demographic, visit, symptom, diagnosis, and disposition fields.
- Validation states missing required data without blocking source encounter completion.
- Every sent version records authority basis, profile, digest, destination, and delivery correlation.
- Corrections and cancellations produce governed follow-up messages rather than editing prior exports.
- Connector outages queue bounded retries and expose timeliness risk to operations users.

## Frappe realization

- **DocTypes:** Add `OC Surveillance Feed Profile`, `OC Surveillance Export Event`, and protected payload artifact with source-version links.
- **Jobs:** Use scheduler and rq queues for candidate selection, serialization, transport, retry, and acknowledgment polling.
- **Permissions:** Separate profile administration, operational monitoring, and identifiable payload access with permlevels.
- **Surfaces:** Provide feed-health Dashboard Charts, timeliness Number Cards, and exception Query Reports.

## Boundaries

Owns: surveillance export selection, transformation, and delivery evidence. Consumes: accepted encounter data and disclosure policy. Emits: minimized surveillance messages. Does not own: encounter documentation or agency analytics.

## Open questions

- Which corrections require replacement messages versus a new event under each profile?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
