# Slot Release Windows — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Releases reserved appointment inventory to broader audiences at configured times while preserving protected access policy.
Topics: openchart-feature-catalog, scheduling, frappe, slot-release
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-045 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Release effectiveness review** — Compare protected-slot use with late-release fill rates.

## Focus

This feature isolates time-based widening of who may book reserved capacity.

## Behavior

- Managers define inventory classes, initial eligible audiences, release offsets, and final public audience.
- A slot reports its current inventory class and next release time to authorized staff.
- Before release, ineligible searches do not expose the protected slot.
- At release time, the slot becomes searchable by the next audience unless booked, held, or closed.
- Manual early release requires permission and reason; delayed release is a visible exception.
- Policy versions remain attached to materialized slots for audit and metric interpretation.

## Frappe realization

- **DocTypes:** `OC Slot Release Policy` with child stages and `OC Slot Inventory State` with slot reference, audience, next_release_at, and version.
- **Automation:** `scheduler_events` advances due releases idempotently and publishes availability changes.
- **Surface:** schedule forms and capacity reports show protected inventory; booking APIs enforce audience eligibility server-side.

## Boundaries

Owns: timed inventory audience transitions. Consumes: slot supply and access policy. Emits: widened search eligibility. Does not own: patient eligibility definitions.

## Open questions

- How should protected access be balanced against near-term unused capacity?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Booking Horizon Rules](openchart-feature-catalog-sch-046-booking-horizon-rules.md)
