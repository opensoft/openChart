# Battery And Network-Aware Sync — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules background mobile synchronization according to clinical urgency, connectivity cost, battery state, OS limits, and explicit user override.
Topics: openchart-feature-catalog, mobile-devices, frappe, adaptive-sync
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-038 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Site-tuned sync policy simulator** — Estimate freshness, data use, and battery tradeoffs from synthetic workloads.

## Focus

This capability isolates resource-aware scheduling without letting optimization hide or delay urgent pending clinical work.

## Behavior

- Queue items carry server-defined urgency, payload class, deadline, ordering, and Wi-Fi-only eligibility.
- The app evaluates battery, charging, low-power mode, connection type, metering, roaming, and OS background allowance.
- Urgent small receipts may sync sooner than large routine media while preserving dependency ordering.
- Users see why an item is waiting and may request an allowed foreground retry.
- Policy never labels work accepted until a server receipt returns.
- Extended deferral, OS denial, or network instability escalates visibly before a clinical deadline.
- Device telemetry sent to the server is coarse, purpose-limited, and contains no unrelated usage history.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Sync Policy` and add urgency, deadline, dependency, payload class, and deferral reason to sync receipts.
- **Roles and permissions:** `OC Mobile Administrator` manages technical policy; clinical owners see their item status but cannot lower server-required urgency.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.sync_plan` returns signed policy and accepts coarse state; all writes retain idempotency.
- **Realtime and jobs:** Websocket events announce urgent queue invalidations; server-side RQ jobs prioritize processing, monitor deadlines, and route prolonged deferrals.
- **Files and surfaces:** Frappe private file attachment APIs support resumable staged transfers and digests; mobile status and Desk metrics separate payload metadata from content.

## Boundaries

Owns: sync scheduling policy and deferral evidence. Consumes: queue metadata, device resource state, and connectivity. Emits: execution plan and escalation. Does not own: OS scheduler guarantees, carrier cost, or clinical priority definition.

## Open questions

- Which documentation and media classes may ever wait for Wi-Fi after the visit ends?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
