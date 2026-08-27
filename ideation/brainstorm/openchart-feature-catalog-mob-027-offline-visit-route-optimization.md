# Offline Visit Route Optimization — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Prepares an offline-capable visit sequence and bounded map pack that staff can adjust without exposing unrelated patient locations.
Topics: openchart-feature-catalog, mobile-devices, frappe, offline-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-027 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Constraint-aware team planning** — Suggest human-reviewed route splits by visit window, skill, and travel burden.

## Focus

This feature isolates route preparation and offline navigation handoff; it does not autonomously assign or cancel care.

## Behavior

- Authorized staff request a route pack for assigned visits and a defined work period.
- The server considers visit windows, starting point, declared constraints, estimated duration, and approved routing provider.
- Users can reorder or exclude a stop with a reason and see resulting time and distance estimates.
- The downloaded pack contains only assigned destinations, bounded map data or navigation links, expiry, and freshness.
- Offline changes remain personal proposals until synchronized and do not alter another worker's assignment.
- Cancelled, reassigned, urgent, or address-corrected visits trigger visible route invalidation.
- Route optimization remains advisory and preserves human override and patient-specific scheduling constraints.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Visit Route Plan` and child `OC Route Stop` with assignments, order, windows, estimates, constraints, provider version, status, and expiry.
- **Roles and permissions:** `OC Community Staff` sees own assigned routes; supervisors manage team proposals through facility and staff user permissions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.routes.prepare` and `resequence` resolve destinations server-side and never return unrelated addresses.
- **Realtime and jobs:** Websocket invalidations flag assignment changes; server-side RQ jobs call routing adapters, build offline packs, and expire provider artifacts.
- **Files and surfaces:** Map packs use encrypted private Frappe file attachment APIs with short-lived grants; mobile map/list modes and a restricted Desk planner share versions.

## Boundaries

Owns: route plan, stop sequence, and offline pack. Consumes: assignments, addresses, windows, and routing adapter. Emits: advisory sequence and navigation handoff. Does not own: assignment authority, navigation safety, or travel reimbursement.

## Open questions

- Should openChart store offline map tiles or delegate all map packaging to a managed navigation SDK?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
