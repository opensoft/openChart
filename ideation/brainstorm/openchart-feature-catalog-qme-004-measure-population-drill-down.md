# Measure Population Drill Down — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized users inspect denominator, numerator, exclusion, exception, and unmet patient lists with explainable evidence for each classification.
Topics: openchart-feature-catalog, quality-reporting, frappe, population-drill-down
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-004 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Cohort comparison bookmark** — Save permission-bound filters for recurring quality huddles.

## Focus

Transparent navigation from an aggregate performance rate to the patient evidence and rule branch that produced it.

## Behavior

- A reviewer opens a measure rate and chooses initial population, denominator, numerator, exclusion, exception, or not-met cohort.
- Lists show only patients allowed by role, facility, care-team, and purpose restrictions.
- Each row displays classification, evaluated date, data freshness, and the decisive evidence or missing requirement.
- A trace panel presents rule steps in clinician-readable language with links to permitted source records.
- Filters support provider, facility, payer, demographic, and attribution dimensions without changing the stored result.
- Export is permission-checked, watermarked, audited, and disabled for small cohorts when site policy requires.
- Disputed classifications create review tasks; they do not directly edit clinical evidence or calculated output.

## Frappe realization

- **DocTypes:** Reuse `OC Patient Measure Result`; add `OC Measure Result Review` with classification, dispute reason, assignment, disposition, and successor result link.
- **Permissions:** Apply patient and facility User Permissions, report query conditions, permlevel controls, and `OC Quality Reviewer` export rights.
- **API and client:** Provide paginated whitelisted drill-down and trace methods; use a Desk report with server-side filters and source-record dialogs.
- **Surfaces:** Deliver Script Reports, Dashboard Chart click-through, CSV/PDF audit stamps, and Assignment Rules for disputed rows.

## Boundaries

Owns: explainable result presentation and review initiation. Consumes: patient measure results, trace evidence, identity, and permissions. Emits: filtered views, audited exports, and disputes. Does not own: calculation logic, source-record amendment, or care assignment.

## Open questions

- What minimum-cell and export controls should apply to sensitive demographic slices?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
