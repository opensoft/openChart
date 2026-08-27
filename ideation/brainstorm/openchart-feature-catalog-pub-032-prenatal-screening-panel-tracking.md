# Prenatal Screening Panel Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks gestational-window prenatal screening panels from offer and order through result review and documented follow-up.
Topics: openchart-feature-catalog, public-health, frappe, prenatal-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-032 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Gestational window visualization** — Show pending panels against effective pregnancy dating and uncertainty.

## Focus

Time-sensitive coordination of prenatal screening milestones without replacing obstetric diagnosis or orders.

## Behavior

- Clinicians select a governed panel profile and link effective pregnancy dating with source and uncertainty.
- The episode displays recommended windows, offer status, patient decision, orders, results, and reviewer.
- Dating changes recalculate windows and mark prior timing displays stale without changing historical actions.
- Declined or externally completed items retain reason and source evidence.
- Abnormal, indeterminate, or overdue items create assignments under reviewed site policy.
- Completion requires disposition for every panel component or an explicit unresolved status.

## Frappe realization

- **DocTypes:** Add `OC Prenatal Screening Episode`, child panel items, and versioned `OC Prenatal Panel Profile` linked to pregnancy status, orders, and results.
- **Workflow:** Use planned, offered, in-progress, awaiting-result, clinician-review, complete, and closed-incomplete states.
- **Permissions:** Restrict to obstetric clinical roles and apply patient User Permissions plus sensitive-result permlevels.
- **Surfaces:** Provide gestational Calendar/Gantt view, overdue Query Report, and chart summary panel.

## Boundaries

Owns: prenatal panel coordination and dispositions. Consumes: pregnancy dating, policy profile, orders, and results. Emits: due windows and follow-up tasks. Does not own: pregnancy record authority, diagnosis, or laboratory interpretation.

## Open questions

- Which panel profiles belong in the public-health domain versus specialty obstetric modules?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
