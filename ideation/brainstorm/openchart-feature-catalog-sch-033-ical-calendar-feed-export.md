# iCalendar Feed Export — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes revocable, privacy-minimized iCalendar feeds for authorized appointment calendar synchronization.
Topics: openchart-feature-catalog, scheduling, frappe, ical-export
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-033 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **One-time calendar file** — Export a bounded date range without issuing a persistent feed token.

## Focus

This feature isolates outbound calendar synchronization and its privacy and revocation controls.

## Behavior

- Providers or patients create a feed scoped to their permitted appointments and chosen detail level.
- Events include stable identifiers, times, status, and privacy-safe labels; clinical detail is excluded.
- Reschedules update the event and cancellations emit a cancelled event state.
- Feed URLs contain high-entropy revocable tokens and never rely on guessable user identifiers.
- Revocation takes effect immediately and is logged with actor and timestamp.
- Consumers receive correct time-zone information and bounded cache guidance.

## Frappe realization

- **DocTypes:** `OC Calendar Feed` with owner, scope, token_hash, detail_level, active, created_at, and revoked_at.
- **API:** guest-readable token endpoint returns `text/calendar`; server resolves the hash, permissions, and event projection without logging raw tokens.
- **Surface:** provider and portal settings pages create or revoke feeds; native Frappe Calendar remains the internal view.

## Boundaries

Owns: privacy-safe iCalendar projection and token lifecycle. Consumes: authorized appointment state. Emits: RFC-style calendar events. Does not own: external calendar behavior.

## Open questions

- What minimum event detail remains useful while protecting privacy on shared devices?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Provider Calendar](openchart-feature-catalog-sch-001-provider-calendar.md)
