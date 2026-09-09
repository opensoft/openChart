# Real-Time Benefit And Formulary Check — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Retrieves patient-specific coverage, restrictions, and formulary alternatives during prescribing with freshness and uncertainty clearly shown.
Topics: openchart-feature-catalog, eprescribing, frappe, real-time-benefit
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-017 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Coverage-change comparison** — Prescribers could compare a refreshed result with the prior response before changing a draft.

## Focus

This feature isolates real-time benefit and formulary retrieval in the prescribing workflow. Results inform a human choice and never autonomously replace the selected medication.

## Behavior

- The prescriber requests a check after selecting patient, medication, dose form, quantity, pharmacy, and coverage context.
- The adapter returns coverage status, tier, restrictions, estimated patient cost, alternatives, and response limitations when available.
- The screen displays payer source, timestamp, request assumptions, and whether values are estimates.
- Identity mismatch, unavailable coverage, timeout, or partial response is explicit and does not masquerade as noncoverage.
- The prescriber may keep the original, choose an alternative into a new editable draft, or defer action with a reason.
- The signed prescription records which response was reviewed but does not copy excess payer data into the clinical record.

## Frappe realization

- **DocTypes:** `OC Benefit Inquiry` stores request digest, minimum coverage references, response summary, alternatives, freshness, and status.
- **API/jobs:** Guarded `open_chart.api.v1.benefits.check` invokes adapters asynchronously with idempotency and realtime completion events.
- **Permissions:** Prescribers and authorized support staff see minimum necessary benefit data under coverage-specific User Permissions.
- **Surfaces:** Composer side panel, comparison dialog, timeout state, and inquiry audit report support review.

## Boundaries

Owns: inquiry lifecycle, display, and reviewed-response linkage. Consumes: coverage, prescription context, and payer service. Emits: reviewable benefit facts and alternatives. Does not own: adjudication, guaranteed price, or autonomous substitution.

## Open questions

- How long may a benefit response remain actionable before a mandatory refresh?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug Price Transparency](openchart-feature-catalog-phr-018-drug-price-transparency.md)
