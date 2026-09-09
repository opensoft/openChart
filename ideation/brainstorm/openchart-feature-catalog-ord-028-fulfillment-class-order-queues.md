# Fulfillment-Class Order Queues — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents permissioned operational worklists partitioned by laboratory, imaging, procedure, referral, nursing, diet, and medication fulfillment class.
Topics: openchart-feature-catalog, cpoe, frappe, fulfillment-queues
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-028 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Cross-class coordination board** — Show dependent orders without collapsing each service's authority.

## Focus

This feature isolates actionable queue views over accepted orders for fulfillment teams.

## Behavior

- Staff see only order classes, facilities, services, and patient details authorized for their role and user permissions.
- Filters include status, priority, due window, location, assigned pool, clarification state, and aging.
- Queue rows distinguish new, acknowledged, held, cancelled, overdue, and in-progress orders.
- Claiming work records assignment but does not change clinical intent.
- Concurrent claims produce a clear conflict and refresh the item.
- Every status action opens the source order and requires the class-specific evidence fields.

## Frappe realization

- **DocTypes:** queues query submitted `OC Clinical Order`, `OC Order Lifecycle Event`, and assignment metadata rather than duplicating orders.
- **Roles/permissions:** Frappe permission query conditions and user permissions scope class, service, and facility.
- **API/surface:** `/api/resource/OC Clinical Order` supports allowlisted filters for order_class, status, priority, assigned_pool, and due range; Query Reports and Desk workspaces provide saved views.
- **Events:** `on_update` and lifecycle hooks publish websocket refreshes; assignment actions use row locking.

## Boundaries

Owns: queue projection, filters, and work claiming. Consumes: orders, lifecycle states, and permissions. Emits: assignments and operational actions. Does not own: clinical order content.

## Open questions

- Which queue sorting rules are fixed safety priorities versus local configuration?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Dispatch Status Tracking](openchart-feature-catalog-ord-029-order-dispatch-status-tracking.md)
