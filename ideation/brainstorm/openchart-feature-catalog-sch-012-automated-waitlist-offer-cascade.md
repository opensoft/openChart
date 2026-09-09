# Automated Waitlist Offer Cascade — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Offers newly opened capacity to eligible waitlist patients in a timed, auditable cascade without autonomous clinical decisions.
Topics: openchart-feature-catalog, scheduling, frappe, waitlist-cascade
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-012 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Parallel offer cohorts** — Offer to a bounded cohort when expiry risk outweighs strict serial outreach.

## Focus

This feature isolates cancellation-triggered matching, offer timing, acceptance, and fallback through a waitlist.

## Behavior

- Released capacity triggers matching against active, eligible waitlist entries.
- The engine orders candidates by approved priority policy and records why each candidate matched or was skipped.
- An offer reserves the slot until its deadline and includes a secure accept or decline action.
- Acceptance revalidates constraints before booking; a stale acceptance receives a clear unavailable response.
- Decline, expiry, or delivery failure advances to the next candidate according to cascade policy.
- Staff can pause or terminate a cascade, and no clinical eligibility is inferred autonomously.

## Frappe realization

- **DocTypes:** `OC Waitlist Cascade` and child `OC Waitlist Offer` with slot, candidate, rank_basis, channel, deadline, and outcome.
- **Automation:** `scheduler_events` and background jobs advance due offers idempotently; Notification doctypes deliver channel-specific offers.
- **API/events:** signed portal methods accept or decline; websocket events update scheduling worklists.

## Boundaries

Owns: offer sequence and temporary slot control. Consumes: released slots and eligible waitlist entries. Emits: booking attempt or exhausted cascade. Does not own: clinical eligibility rules.

## Open questions

- Should high-demand slots use serial offers or bounded simultaneous cohorts?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Waitlist Management](openchart-feature-catalog-sch-011-waitlist-management.md)
