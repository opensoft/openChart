# Schedule Change Broadcasts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates consent-aware, channel-appropriate notifications to everyone affected by material schedule disruptions.
Topics: openchart-feature-catalog, scheduling, frappe, change-broadcasts
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-055 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Response reconciliation** — Track who acknowledged a disruption and who still needs staff contact.

## Focus

This feature isolates communication orchestration after closures, provider absence, or other bulk schedule changes.

## Behavior

- An approved disruption produces an audience of affected patients, providers, rooms, interpreters, and operational teams.
- Staff preview audience, channels, language, message variant, and excluded recipients before release.
- Patient messages reveal only their appointment impact and approved next actions.
- Delivery follows consent and verified channels, with fallback and staff-call tasks governed explicitly.
- Corrections issue a new version and do not erase prior delivery evidence.
- Staff monitor queued, sent, delivered, failed, acknowledged, and manual-follow-up outcomes.

## Frappe realization

- **DocTypes:** `OC Schedule Broadcast` and child `OC Schedule Broadcast Recipient` with disruption source, message version, channel, consent snapshot, and delivery state.
- **Workflow:** Draft → Audience Reviewed → Approved → Sending → Completed/Partial/Cancelled.
- **Automation:** Frappe Notification doctypes, background jobs, Notification Log, email/SMS integrations, and realtime progress support delivery.

## Boundaries

Owns: disruption audience and delivery orchestration. Consumes: approved schedule change and current consent. Emits: messages and follow-up tasks. Does not own: the underlying schedule decision.

## Open questions

- Which disruption severities justify fallback to manual calling automatically?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Holiday Closure Management](openchart-feature-catalog-sch-023-holiday-closure-management.md)
