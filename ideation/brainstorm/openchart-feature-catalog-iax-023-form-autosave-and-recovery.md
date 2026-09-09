# Form Autosave And Recovery — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves recoverable draft form work with version-aware autosave while never presenting a local draft as an accepted clinical record.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, draft-recovery
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-023 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Draft recovery center** — Show a user's recoverable drafts, age, source route, and conflicts from one permission-safe workspace.

## Focus

This feature isolates loss prevention for in-progress forms from authoritative submission, amendment, and signing behavior.

## Behavior

- Eligible forms autosave changed draft fields after a quiet interval and before supported navigation or session expiry.
- A visible status distinguishes Unsaved, Saving, Saved Draft, Offline Draft, Conflict, Recovered, and Discarded states.
- Returning users may restore, compare, or discard their own unexpired draft after permission is rechecked.
- If the server record changed, recovery shows a field-level comparison and never overwrites accepted data automatically.
- Sensitive drafts are encrypted in approved storage, expire by policy, and are unavailable to other shared-device users.
- Submission uses the ordinary guarded API and separately confirms acceptance; autosave success never implies clinical acceptance.
- Network and storage failures retain an accessible warning and recovery instructions without trapping the user on the page.

## Frappe realization

- **DocTypes:** `OC Form Recovery Draft` stores owner, target DocType/name, base version, encrypted payload, state, timestamps, expiry, and device-session reference.
- **Hooks and jobs:** Form client scripts debounce saves; `validate` enforces field allowlists and ownership; `scheduler_events` purges expired drafts with evidence.
- **API:** Guarded `open_chart.api.v1.ux.drafts` methods save, compare, restore, discard, and submit using optimistic version checks.
- **Surfaces:** Accessible save-state indicators, conflict dialogs, and a Desk recovery workspace use realtime events for server acknowledgments.

## Boundaries

Owns: temporary form drafts, autosave state, conflict presentation, and recovery. Consumes: form schema, user permission, base version, and connectivity. Emits: recoverable drafts and explicit submit handoff. Does not own: accepted records, signatures, amendments, or offline clinical synchronization.

## Open questions

- Which clinical form fields must be excluded from browser-local offline draft storage even when encrypted?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Secure Session Context Resume](openchart-feature-catalog-iax-027-secure-session-context-resume.md)
