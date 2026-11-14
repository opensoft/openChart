# Urgency-Routed Push Notifications — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes minimum-necessary mobile notifications by urgency, role, acknowledgement policy, and quiet hours without placing PHI in vendor payloads.
Topics: openchart-feature-catalog, mobile-devices, frappe, push-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-012 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Escalation simulation** — Verify quiet-hour and acknowledgement chains with synthetic events before activation.

## Focus

This capability isolates mobile delivery policy; source workflows remain responsible for clinical urgency and escalation meaning.

## Behavior

- Source workflows submit a notification type, urgency, recipient scope, expiry, and chart route.
- The router applies current assignment, role, device, quiet-hour, and acknowledgement policy.
- Vendor push payloads contain an opaque event ID and generic text, never patient name, diagnosis, result, or message body.
- Opening the notification authenticates the user and fetches current content after a fresh permission check.
- Routine notifications wait for quiet hours to end; configured urgent classes may bypass them with visible rationale.
- Delivery, open, acknowledgement, expiry, suppression, and escalation are separate states.
- Failed delivery follows a governed fallback path and never implies that a clinician saw the event.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Notification Policy`, `OC Mobile Notification Event`, and `OC Quiet Hours` with type, urgency, recipient rule, deadlines, states, and source Dynamic Link.
- **Workflow and roles:** Queued → Sent → Opened → Acknowledged/Expired/Escalated/Suppressed; source roles acknowledge, and `OC Communications Administrator` governs policy.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.notifications.fetch` and `acknowledge` resolve opaque IDs; provider callbacks use signed whitelisted methods.
- **Realtime and jobs:** Use websocket events for active sessions and server-side RQ jobs for push send, quiet-hour release, retry, expiry, and fallback escalation.
- **Files and surfaces:** Notification attachments are never embedded; authorized files use Frappe private attachment APIs after app open, with Desk delivery reports.

## Boundaries

Owns: mobile delivery and acknowledgement evidence. Consumes: source urgency, assignments, preferences, and device tokens. Emits: delivery states and escalation signals. Does not own: clinical severity, telecom uptime, or source workflow disposition.

## Open questions

- Which urgency classes may bypass quiet hours, and who approves those mappings?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
