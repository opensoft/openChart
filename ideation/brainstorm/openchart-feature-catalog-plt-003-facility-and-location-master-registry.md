# Facility And Location Master Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains effective-dated facilities, departments, rooms, and service locations as a governed operational hierarchy.
Topics: openchart-feature-catalog, platform, frappe, facility-location-master
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-003 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Location readiness score** — Combine hours, contacts, equipment, and required configuration into a launch view.

## Focus

This feature isolates authoritative place management so clinical and operational records link stable location identities rather than free text.

## Behavior

- Site administrators create facilities and nested service locations with codes, names, addresses, time zones, and active dates.
- A location may be a building, department, room, virtual service point, collection site, or mobile unit.
- Duplicate active codes and hierarchy cycles are rejected with actionable validation messages.
- Renaming preserves the stable identifier and prior display names; historical records continue resolving correctly.
- Inactivation is blocked while future operational commitments reference the location unless an explicit replacement is selected.
- Users search only locations allowed by site and role permissions, with inactive records excluded by default.

## Frappe realization

- **DocTypes:** tree DocType `OC Facility Location` uses parent, location_type, code, address, timezone, valid_from, valid_to, and replacement Link fields.
- **Permissions:** Facility Administrator has create/write; operational roles receive read access filtered through site User Permissions.
- **Hooks:** `validate` prevents cycles, overlapping codes, and invalid effective dates; `on_update` publishes a cache-invalidation realtime event.
- **Surface/API:** Tree and List views plus guarded `/api/resource/OC Facility Location` reads and `open_chart.api.v1.platform.retire_location`.

## Boundaries

Owns: facility and service-location identities and hierarchy. Consumes: site identity and postal data. Emits: stable location Links and lifecycle events. Does not own: appointment capacity, staffing, or real-estate management.

## Open questions

- Should room identities move between departments or be retired and succeeded?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Provider Master Registry](openchart-feature-catalog-plt-004-provider-master-registry.md)
