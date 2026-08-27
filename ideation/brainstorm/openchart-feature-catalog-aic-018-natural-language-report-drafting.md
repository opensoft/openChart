# Natural-Language Report Drafting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts an authorized natural-language analytics request into a reviewable report definition and narrative without executing unrestricted queries.
Topics: openchart-feature-catalog, clinical-ai, frappe, analytics-drafting
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-018 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Question-to-report gallery** — Save approved prompt and report pairs as reusable governed analytics recipes.

## Focus

This feature isolates natural-language assistance inside analytics while preserving permissions, bounded query templates, and human publication.

## Behavior

- An analyst states a question and selects an approved dataset, measure catalog, date range, and aggregation scope.
- The system drafts a structured report plan, filters, definitions, caveats, and optional narrative before execution.
- Users inspect and approve the plan; only allowlisted fields, joins, functions, and row limits can run.
- Results remain permission-filtered and display the generated plan and data-through timestamp.
- The model cannot issue arbitrary SQL, modify records, or publish a dashboard automatically.
- Ambiguous measures trigger clarification rather than inferred definitions.

## Frappe realization

- **DocTypes:** `OC AI Report Draft` stores question, approved dataset, structured plan JSON, artifact, reviewer, execution record, and publication status.
- **Workflow:** Drafted → Plan Review → Approved To Run → Executed → Published/Rejected.
- **Roles/permissions:** `OC Clinical Analyst` drafts and runs within existing Report permissions; `OC Analytics Publisher` publishes.
- **API/jobs/surfaces:** whitelisted compiler maps plans to allowlisted Query/Script Report parameters; rq handles bounded execution; Desk preview shows definitions and lineage.

## Boundaries

Owns: natural-language report plan and narrative draft. Consumes: governed semantic catalog and authorized datasets. Emits: reviewed bounded report configuration. Does not own: arbitrary SQL, data authorization, or automatic publication.

## Open questions

- Which aggregation sizes and rare-condition combinations require additional privacy review?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Cost And Usage Metering](openchart-feature-catalog-aic-030-ai-cost-and-usage-metering.md)
