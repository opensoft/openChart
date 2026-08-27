# Recent And Pinned Navigation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives users permission-safe recent-patient context and cross-module favorites without turning navigation history into an uncontrolled disclosure surface.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, navigation-shortcuts
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-021 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Shift handoff pin set** — Let users temporarily group permitted destinations for a bounded work period without sharing patient history.

## Focus

This feature isolates two personal navigation aids: a bounded recently viewed patient strip and explicit favorites across supported modules.

## Behavior

- The recent strip lists only patients the user deliberately opened, ordered by last access, with a site-configured maximum and expiry.
- Users pin or unpin permitted patients, reports, lists, workspaces, and routes; pins remain separate from recency.
- Every render rechecks current permission and protected-access policy before showing a label or navigation target.
- Revoked, merged, deleted, or inaccessible records disappear without revealing why to an unauthorized viewer.
- Users can clear recents, reorder pins, and disable patient recency on shared-device sessions.
- Labels remain minimum necessary and conceal sensitive secondary details unless policy explicitly permits them.
- Keyboard and screen-reader users can traverse, reorder, dismiss, and open entries with equivalent feedback.

## Frappe realization

- **DocTypes:** `OC User Navigation Pin` stores user, target type, Dynamic Link/route, position, and scope; recents use a bounded permission-filtered activity projection rather than clinical records.
- **Bootinfo and preferences:** Authorized pins and recency policy load through bootinfo; Frappe user preferences hold strip visibility and device-local suppression.
- **API:** Guarded `open_chart.api.v1.ux.navigation` methods add, reorder, remove, clear, and resolve entries with row-level permission checks.
- **Surfaces:** A shared Desk strip and workspace sidebar component expose recents and pins; realtime events remove entries after permission changes.

## Boundaries

Owns: personal navigation recency and pins. Consumes: deliberate views, current permissions, protected-access policy, and target labels. Emits: minimum-necessary shortcuts. Does not own: chart access authorization, team assignments, or a permanent access audit trail.

## Open questions

- Should patient recency be disabled by default on workstations designated as shared?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Universal Search Command Palette](openchart-feature-catalog-iax-020-universal-search-command-palette.md)
