# Newborn Screen Coordination — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates newborn hearing, metabolic, and related screening records across collection, result receipt, repeat testing, and referral.
Topics: openchart-feature-catalog, public-health, frappe, newborn-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-033 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Birth-facility reconciliation** — Match outside newborn screen records to the infant chart with human identity review.

## Focus

A unified infant screening coordination episode that keeps each program's evidence and follow-up distinct.

## Behavior

- Staff record screen type, birth context, collection or test time, facility, specimen/device identifiers, and source.
- Results remain linked to source records and display pass, refer, pending, unsatisfactory, or unknown program states.
- Repeat requirements create dated tasks and retain the original screen outcome.
- Identity ambiguity between parent, birth record, and infant chart blocks automatic acceptance.
- Abnormal or missing results route accountable clinical and program follow-up.
- Corrections and outside reconciliations preserve source provenance and successor history.

## Frappe realization

- **DocTypes:** Add `OC Newborn Screening Episode` and child program milestones with Links to infant, related person, specimens, results, and referrals.
- **Workflow:** Use expected, collected/tested, awaiting-result, repeat-needed, referral-needed, complete, and unable-to-confirm states.
- **Permissions:** Grant neonatal and pediatric roles access; protect parent/infant linkage and sensitive results with permlevels.
- **Surfaces:** Provide newborn-screen worklists, overdue Notifications, and a longitudinal family-aware chart panel.

## Boundaries

Owns: newborn screening coordination and follow-up status. Consumes: infant identity, birth context, tests, results, and referrals. Emits: milestones and tasks. Does not own: birth registration, source results, or diagnostic conclusions.

## Open questions

- Which identity evidence is sufficient to accept an outside newborn result?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
