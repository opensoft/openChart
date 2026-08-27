# Cancellation Backfill Analytics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures whether cancelled capacity is reoffered and refilled, with timing and channel attribution.
Topics: openchart-feature-catalog, scheduling, frappe, backfill-analytics
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-051 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Cascade policy comparison** — Compare refill speed and equity across offer strategies.

## Focus

This feature isolates capacity-recovery measurement after cancellation or release.

## Behavior

- Each released interval receives a recovery episode linked to the triggering cancellation or hold release.
- The episode records time to first offer, number of offers, channel, time to refill, and final unused or refilled outcome.
- A refill is attributed only when interval, resource requirements, and configured matching tolerance align.
- Reports segment by service, location, lead time, and recovery pathway without exposing patient identities.
- Corrections to source events recompute the episode with lineage.
- Metrics remain descriptive and do not autonomously change waitlist priority or overbooking.

## Frappe realization

- **DocTypes:** `OC Capacity Recovery Episode` with released slot, trigger, offers, refill appointment, durations, outcome, and source versions.
- **Automation:** event hooks open and update episodes; nightly `scheduler_events` reconciles unresolved attribution.
- **Reports:** Script Reports and Dashboard Charts show refill rate and time-to-refill with privacy-safe drill-down.

## Boundaries

Owns: cancellation-capacity recovery metrics. Consumes: releases, offers, and later bookings. Emits: attributed operational measures. Does not own: cascade policy decisions.

## Open questions

- How close must a replacement booking match the released interval to count as backfill?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Automated Waitlist Offer Cascade](openchart-feature-catalog-sch-012-automated-waitlist-offer-cascade.md)
