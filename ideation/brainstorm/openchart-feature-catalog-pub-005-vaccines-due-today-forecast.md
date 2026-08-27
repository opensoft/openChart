# Vaccines Due Today Forecast — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays vaccines due, overdue, conditionally eligible, or not yet due today with supporting schedule evidence.
Topics: openchart-feature-catalog, public-health, frappe, vaccine-forecast
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-005 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Previsit vaccine review** — Populate a supervised preparation queue before scheduled encounters.

## Focus

A concise point-of-care forecast derived from a current, versioned schedule evaluation.

## Behavior

- Clinical staff see a forecast on the patient chart and can refresh it for today's date.
- Each row shows due state, vaccine series, timing window, rationale, and evaluation freshness.
- Conditional items state the missing indication, history, or contraindication information.
- Users can acknowledge, defer, or document not-addressed without converting the forecast into an order.
- New accepted doses or relevant patient data invalidate cached results.
- Engine errors display an unavailable state and route diagnostics without presenting stale guidance as current.

## Frappe realization

- **DocTypes:** Add `OC Immunization Forecast Snapshot` and child rows linked to the governing schedule evaluation.
- **Client scripts:** Render color-independent due-state badges and evidence drill-down on the patient form.
- **Permissions:** Clinical roles may view; only `OC Clinician` may record clinical dispositions, with complete audit history.
- **Jobs and API:** Refresh through a background job or whitelisted method, publish realtime completion, and expose a due-vaccine Query Report.

## Boundaries

Owns: the current display and disposition of forecast results. Consumes: schedule evaluations and freshness events. Emits: due-state visibility and review dispositions. Does not own: schedule rules, orders, or outreach.

## Open questions

- How long may a forecast remain cached before it must show as stale?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
