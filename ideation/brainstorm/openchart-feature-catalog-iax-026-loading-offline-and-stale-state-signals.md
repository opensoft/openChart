# Loading Offline And Stale-state Signals — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Distinguishes loading, delayed, offline, cached, stale, and failed data so users never mistake an incomplete view for current clinical state.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, data-state-signals
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-026 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Freshness service contract** — Standardize last-confirmed timestamps and staleness thresholds for realtime clinical surfaces.

## Focus

This feature isolates honest progress and freshness presentation, including skeleton states and offline banners.

## Behavior

- Initial loads show structure-preserving skeletons only when they cannot be mistaken for real values or controls.
- Long operations switch to descriptive progress with cancelability and background-continuation status where supported.
- A persistent banner identifies Offline, Reconnecting, Cached, Stale, or Server Unavailable states in text and icon form.
- Cached clinical data shows its last server-confirmed timestamp and blocks unsupported mutations while offline.
- Reconnection revalidates permissions and versions before refreshing or submitting queued non-clinical actions.
- Empty results are distinct from loading and failure, with an explanation and safe retry when appropriate.
- Status changes are screen-reader announced without repeatedly interrupting work.

## Frappe realization

- **Configuration:** `OC Surface Freshness Policy` stores route/data class, stale threshold, cache permission, offline actions, and warning key.
- **Client and realtime:** Shared Desk/portal components consume Frappe request state, websocket connectivity, and service-worker cache metadata.
- **Background jobs:** RQ job progress emits realtime events; `OC Background Operation` stores owner, status, percent, result link, and failure code.
- **Surfaces:** Website Theme and Desk themes provide skeleton, banner, timestamp, and status tokens with reduced-motion and high-contrast variants.

## Boundaries

Owns: progress, connectivity, freshness, and failure presentation. Consumes: request state, websocket state, cache metadata, and policy. Emits: honest user-visible state and mutation guards. Does not own: full offline clinical operation or source-system availability.

## Open questions

- Which read-only clinical surfaces may use encrypted cached data, and for how long?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Form Autosave And Recovery](openchart-feature-catalog-iax-023-form-autosave-and-recovery.md)
