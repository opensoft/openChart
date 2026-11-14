# VIS Distribution And Version Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records which Vaccine Information Statement edition, language, and delivery method a patient or guardian received before administration.
Topics: openchart-feature-catalog, public-health, frappe, vis-distribution
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-018 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Portal previsit delivery** — Deliver the current statement electronically and retain acknowledgment evidence.

## Focus

Edition-specific distribution evidence linked to the relevant vaccine and recipient.

## Behavior

- Staff select vaccine, VIS edition date, language, recipient, delivery method, and delivery time.
- The system warns when a newer active edition exists but preserves lawful historical entry.
- Delivery can cover multiple same-edition administrations while retaining explicit links.
- Portal delivery remains pending until delivery or acknowledgment evidence meets configured policy.
- Unavailable translations display a gap and require documented fallback rather than false language matching.
- Accepted logs are immutable and corrected through successors.

## Frappe realization

- **DocTypes:** Add `OC VIS Edition` and submittable `OC VIS Distribution Log` with vaccine mappings, language, recipient, method, evidence, and administration links.
- **Workflow:** Govern editions as draft, active, and retired; logs as prepared, delivered, acknowledged, failed, and superseded.
- **Permissions:** Clinical users record delivery; content administrators manage editions; portal access follows proxy authority.
- **Surfaces:** Provide print/PDF and portal delivery, Notifications for failures, and a missing-VIS Query Report.

## Boundaries

Owns: VIS edition catalog and distribution evidence. Consumes: vaccine, language preference, recipient authority, and document content. Emits: pre-administration disclosure record. Does not own: informed consent or external content licensing.

## Open questions

- Is acknowledgment required or is documented provision sufficient by site policy?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
