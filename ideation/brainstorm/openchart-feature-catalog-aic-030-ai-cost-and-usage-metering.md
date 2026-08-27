# AI Cost And Usage Metering — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Meters invocation volume, tokens, media duration, latency, and estimated cost by capability, site, model, and workflow.
Topics: openchart-feature-catalog, clinical-ai, frappe, cost-metering
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-030 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Budget guardrails** — Warn or suspend nonclinical generation when approved site or capability budgets are exhausted.

## Focus

This feature isolates operational accountability for AI consumption without exposing PHI in finance-facing reports.

## Behavior

- Every invocation records normalized usage dimensions, provider-reported usage, estimated rate-card cost, latency, retries, and outcome.
- Administrators view aggregate usage by site, capability, model, adapter, workflow, and time period.
- Rate cards are versioned so historical estimates do not change when prices change.
- Missing provider usage is labeled estimated or unavailable rather than recorded as zero.
- Budget warnings create operator notifications; any suspension follows approved enablement policy and preserves clinical manual paths.
- Finance exports contain aggregate identifiers and no prompt or patient content.

## Frappe realization

- **DocTypes:** `OC AI Usage Event`, `OC AI Rate Card`, and `OC AI Budget` store normalized units, cost currency, source, estimate flag, dimensions, thresholds, and effective dates.
- **Roles/permissions:** site administrators view their aggregates; `OC AI Finance Analyst` sees cost reports without clinical payloads.
- **Hooks/jobs/reports:** adapter response hook records usage; scheduler reconciles late provider reports; Query Reports, Number Cards, and Dashboard Charts show consumption.
- **API:** whitelisted aggregate export method applies site and role filters; direct usage-event writes are service-only.

## Boundaries

Owns: normalized AI usage and estimated cost evidence. Consumes: provider telemetry, rate cards, and capability context. Emits: aggregate budgets and reports. Does not own: invoices, billing, or clinical priority decisions.

## Open questions

- Which safety-critical capabilities may exceed a budget while still alerting accountable operators?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Inference Latency And Fallback Policy](openchart-feature-catalog-aic-048-inference-latency-and-fallback-policy.md)
