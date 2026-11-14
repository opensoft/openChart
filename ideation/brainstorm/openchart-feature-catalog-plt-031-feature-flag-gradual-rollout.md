# Feature Flag Gradual Rollout — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Controls reversible feature exposure by site, role, cohort, and time with approval, observability, and fail-safe defaults.
Topics: openchart-feature-catalog, platform, frappe, feature-flags
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-031 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Guardrail-driven rollout pauses** — Halt cohort expansion when approved operational thresholds are crossed.

## Focus

This feature isolates runtime exposure decisions without using flags as permanent authorization, schema, or clinical-policy controls.

## Behavior

- Release managers define a flag key, owner, purpose, default, eligible sites and roles, cohorts, dates, and expiry.
- Flags move through Draft, Review, Active, Paused, Completed, Retired, and Expired states.
- Evaluation order and cohort membership are previewable and deterministic for the same subject and version.
- Activation requires a fallback behavior, monitoring signals, and explicit prohibition on weakening permissions or consent.
- Pausing or killing a flag takes effect through cache invalidation and records the actor, reason, and affected scope.
- Expired flags fall back safely and create cleanup tasks so conditional code and fixtures do not become permanent drift.

## Frappe realization

- **DocTypes:** `OC Feature Flag` and child `OC Flag Target` store key, version, default, scopes, percentage, dates, owner, and state.
- **Hooks/API:** a cached `open_chart.platform.flags.is_enabled` evaluator checks site, role, cohort, and active version; realtime events invalidate caches.
- **Permissions:** Release Manager authors; Feature Flag Approver activates; Site Administrator sees effective local flags.
- **Surface:** rollout dashboard charts exposure, errors, latency, and manual pause evidence by cohort.

## Boundaries

Owns: temporary feature exposure and evaluation evidence. Consumes: site, role, cohort, and operational signals. Emits: deterministic flag decisions and rollout events. Does not own: RBAC, consent, schema migration, or clinical decisions.

## Open questions

- Which flags require patient-stable cohorting versus user-stable or site-stable cohorting?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Configuration Promotion Pipeline](openchart-feature-catalog-plt-030-configuration-promotion-pipeline.md) · [Opt-in Usage Telemetry Dashboard](openchart-feature-catalog-plt-049-opt-in-usage-telemetry-dashboard.md)
