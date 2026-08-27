# Expired-Stock Quarantine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects approaching and passed medication expiry, moves affected lots out of availability, and tracks review and disposition.
Topics: openchart-feature-catalog, eprescribing, frappe, expiry-quarantine
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-041 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **First-expire-first-out picking** — Dispensing could recommend eligible earlier-expiring lots while preserving pharmacist confirmation.

## Focus

This feature isolates proactive expiry scanning and lot quarantine. Automated jobs may change operational availability according to policy but cannot destroy, return, or dispense stock.

## Behavior

- Daily scans identify lots approaching warning, removal, and expired thresholds in each location.
- Warning lots remain available with clear shelf-life context when policy permits.
- Removal-threshold or expired lots enter quarantine and are excluded from dispensing and reorder availability calculations.
- Staff verify physical segregation, count, location, and reason and resolve mismatches through inventory review.
- Authorized users choose return, destruction, recall handling, or approved release when evidence supports it.
- Every state change records rule version, actor or scheduler identity, timestamp, quantity, and lot.

## Frappe realization

- **DocTypes:** `OC Medication Lot` carries expiry and quarantine state; `OC Stock Quarantine Event` records quantity, trigger, verification, and disposition.
- **Workflow:** Detected → System Quarantined → Physical Verification → Return/Destroy/Release → Closed.
- **Hooks/jobs:** Daily `scheduler_events` expiry scans create idempotent events, post availability changes, and notify inventory roles.
- **Surfaces:** Expiry dashboard, quarantine worklist, barcode verification, and expiring-stock Query Report support operations.

## Boundaries

Owns: expiry detection, operational quarantine, and disposition workflow. Consumes: lot expiry, location, inventory quantity, and policy thresholds. Emits: availability exclusions and tasks. Does not own: physical destruction or supplier return settlement.

## Open questions

- Which products need beyond-use dates or opened-container dates in addition to manufacturer expiry?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Returned-Medication Destruction Log](openchart-feature-catalog-phr-048-returned-medication-destruction-log.md)
