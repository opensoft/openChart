# Offline Home-Care Visit Checklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides field staff through versioned home-care visit steps offline and synchronizes attributable completion and exceptions afterward.
Topics: openchart-feature-catalog, mobile-devices, frappe, home-care-checklists
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-024 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Supply-aware visit pack** — Pair checklist steps with previsit supply confirmation and exception capture.

## Focus

This entry isolates offline execution of a human-assigned visit plan without turning prompts into autonomous care decisions.

## Behavior

- Before departure, staff download assigned visits, current checklist versions, allowed chart context, and expiry.
- Steps support complete, not applicable, unable, declined, deferred, and exception outcomes with required rationale rules.
- Conditional steps follow server-issued template logic and never create unapproved clinical actions.
- The app autosaves encrypted progress and shows which items require connectivity or supervisor review.
- Visit completion remains Pending Sync until the server accepts all required steps or records an authorized exception.
- Template changes do not rewrite an in-progress visit; reconciliation identifies materially changed requirements.
- Photos, signatures, readings, and location evidence remain separately attributable attachments or observations.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Home Visit Checklist Template`, `OC Home Visit Execution`, and child `OC Visit Checklist Response` with version, step, outcome, evidence links, and sync state.
- **Workflow and roles:** Assigned → In Progress → Pending Sync → Completed/Needs Review/Cancelled; `OC Home Care Clinician` acts and `OC Home Care Supervisor` reviews exceptions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.home_visit.package` and `submit_checklist` enforce assignment, version, idempotency, and guarded clinical writes.
- **Realtime and jobs:** Websocket receipts update review status; server-side RQ jobs prepare visit packs, validate submissions, and route exceptions.
- **Files and surfaces:** Evidence uses private Frappe file attachment APIs with per-step purpose and retention; mobile checklist, Calendar, and Desk review queues share state.

## Boundaries

Owns: checklist template, offline execution, and exception evidence. Consumes: visit assignment, care plan, permissions, and device services. Emits: completed responses and review requests. Does not own: clinical orders, staffing, or autonomous escalation.

## Open questions

- Which checklist changes are material enough to require re-performance during an active offline visit?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
