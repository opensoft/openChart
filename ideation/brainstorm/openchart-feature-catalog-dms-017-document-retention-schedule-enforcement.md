# Document Retention Schedule Enforcement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Calculates class-specific retention milestones and drives reviewable disposition without deleting records outside approved policy.
Topics: openchart-feature-catalog, documents, frappe, retention-enforcement
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-017 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Retention impact preview** — Simulate policy-version changes against inventory before any disposition dates move.

## Focus

This feature isolates policy-versioned retention calculation and human-governed disposition of document versions.

## Behavior

- A Records Administrator defines retention rules by document class, patient age basis, event trigger, facility, and jurisdiction.
- Each accepted document records the policy version, trigger facts, calculated review date, and disposition eligibility date.
- Scheduled jobs identify due items but never purge them merely because a date passed.
- An authorized reviewer confirms eligibility, checks holds and active obligations, and approves archive or destruction.
- Missing trigger facts, conflicting policies, active ROI work, or legal hold block disposition with a reason.
- Destruction records approval, method, scope, checksum, and tombstone metadata while removing content through controlled storage operations.
- Policy changes recalculate prospectively with an explainable before-and-after record.

## Frappe realization

- **DocTypes:** `OC Document Retention Policy` (class, jurisdiction, trigger, duration, action, effective dates) and `OC Document Disposition Case` linked to exact versions.
- **Workflow:** Scheduled → Eligibility Review → Approved → Executed, with Blocked, Deferred, and Cancelled states.
- **Roles/permissions:** Records Administrator versions policy; Records Disposition Reviewer approves; Privacy Officer audits; no integration role may approve destruction.
- **Jobs/hooks:** scheduler_events create cases and recheck blockers; controlled File deletion runs only from submitted execution records and leaves a non-PHI tombstone.
- **Surfaces:** Retention calendar, due/blocked Script Reports, policy impact report, and destruction certificate Print Format.

## Boundaries

Owns: retention policies, calculated dates, disposition cases, and execution evidence. Consumes: class, patient/event facts, holds, and active obligations. Emits: archive/destruction instruction and tombstone. Does not own: legal interpretation, storage vendor internals, or legal-hold authority.

## Open questions

- How should conflicting facility and jurisdiction policies choose the controlling longest-retention rule?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Legal Hold Override](openchart-feature-catalog-dms-018-legal-hold-override.md)
