# Role-Based Mobile Home Screens — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents physician, nurse, and home-care mobile landing screens composed from permission-filtered work priorities.
Topics: openchart-feature-catalog, mobile-devices, frappe, role-home-screens
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-004 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **User-arranged safe widgets** — Let clinicians reorder approved widgets without broadening data scope.

## Focus

This feature isolates role-specific orientation on a small screen while allowing one person to switch among authorized contexts.

## Behavior

- Physicians see rounding, results, messages, and signature work; nurses see assigned patients, administrations, collections, and tasks; home-care staff see visits, checklists, and route status.
- Every tile is server-filtered by current role, facility, care-team, assignment, and user permissions.
- Counts identify work categories without putting patient names on the locked or notification surface.
- Users with multiple roles can switch context explicitly and always see the active role and site.
- Offline tiles show cached-as-of time and omit work that cannot be safely represented from the local cache.
- Selecting a tile revalidates access before revealing patient content.
- Empty, stale, denied, and service-unavailable states are distinct and actionable.

## Frappe realization

- **DocTypes:** Create `OC Mobile Home Profile` and child `OC Mobile Home Widget` with role, route, query key, ordering, offline eligibility, and effective version.
- **Roles and permissions:** Mobile profiles are managed by `OC Mobile Administrator`; widget data uses source DocType permissions and patient/facility user permissions, never profile grants.
- **API and auth:** Serve `open_chart.api.v1.mobile.home` over TLS REST token/OAuth2 auth; prohibit clients from submitting arbitrary report names or filters.
- **Realtime and jobs:** Push count invalidations through permission-safe websocket events; calculate expensive aggregates in server-side RQ jobs with per-user cache keys.
- **Files and surfaces:** Widget icons use public non-PHI Frappe file attachments; Desk configuration and preview surfaces mirror mobile composition.

## Boundaries

Owns: mobile home composition and safe count presentation. Consumes: authorized work queues and assignments. Emits: navigation intent and refresh requests. Does not own: source workflow states or clinical prioritization.

## Open questions

- Which widgets must remain fixed to prevent role customization from hiding safety-critical work?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
