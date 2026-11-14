# Provider Availability Exceptions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records bounded additions or removals from a provider's normal availability with conflict-aware approval.
Topics: openchart-feature-catalog, scheduling, frappe, availability-exceptions
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-022 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Coverage suggestion** — Identify qualified substitute providers for affected appointments.

## Focus

This feature isolates provider-specific deviations such as leave, meetings, added clinics, or reduced hours.

## Behavior

- Providers or managers request an exception with interval, type, reason, and recurrence when applicable.
- The system previews appointments, holds, and resources affected by removing availability.
- Approved added availability creates capacity only within facility and credential constraints.
- Approved unavailability blocks new bookings but does not silently cancel existing appointments.
- Overlapping exceptions resolve by explicit precedence and display the effective result.
- Rejection or withdrawal retains the request and decision history.

## Frappe realization

- **DocTypes:** `OC Availability Exception` with provider, interval, exception_type, recurrence, reason, state, and impact snapshot.
- **Workflow:** Draft → Submitted → Approved/Rejected/Withdrawn; provider self-service and manager permissions differ.
- **Automation/surface:** Frappe auto-repeat supports bounded recurrence; native Calendar view overlays approved exceptions on provider schedules.

## Boundaries

Owns: provider-specific availability deviations. Consumes: baseline templates and booked appointments. Emits: effective availability change and impact list. Does not own: leave entitlement.

## Open questions

- Which exception types may providers approve for themselves?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Provider Substitution Workflow](openchart-feature-catalog-sch-052-provider-substitution-workflow.md)
