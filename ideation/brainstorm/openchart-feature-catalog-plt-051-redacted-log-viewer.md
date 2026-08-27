# Redacted Log Viewer — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized operators search application and worker logs by severity and correlation while enforcing safe redaction and retention.
Topics: openchart-feature-catalog, platform, frappe, redacted-logs
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-051 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Incident evidence bundle** — Export a time-bounded, reviewed, further-redacted log package with integrity manifest.

## Focus

This feature isolates operational log access and treats redaction as a server-side invariant rather than a UI convenience.

## Behavior

- Operators filter by site, service, time, severity, logger, request or job correlation, and known event class.
- Results show structured metadata and redacted messages; credentials, tokens, patient identifiers, and configured patterns are masked before storage or display.
- Raw-log access is unavailable through the viewer and requires a separate emergency process outside ordinary administration.
- Search limits time range and result volume and reports truncation explicitly.
- Saved queries contain filters only, never copied log text, and remain site- and role-scoped.
- Export requires reason and approval, applies a second redaction pass, expires, and records a digest.

## Frappe realization

- **DocTypes:** `OC Log Source`, `OC Redaction Policy`, and `OC Log Export Request` store source metadata, patterns, retention, scopes, and approval evidence.
- **API:** guarded whitelisted search queries a structured log backend and applies server-side field allowlists and redaction.
- **Permissions:** Log Operator searches permitted sites; Security Reviewer manages redaction policy; export requires Audit Approver.
- **Surface:** Desk viewer supports severity facets, correlation timeline, safe copy, and links to job or administrative audit evidence.

## Boundaries

Owns: permissioned log search, redaction, saved filters, and export evidence. Consumes: structured operational logs and correlation IDs. Emits: redacted views and protected bundles. Does not own: raw log transport, SIEM incident response, or clinical audit.

## Open questions

- How should administrators report a suspected redaction failure without reproducing sensitive content?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Capacity And Performance Diagnostics](openchart-feature-catalog-plt-050-capacity-and-performance-diagnostics.md) · [Administrative Change Audit](openchart-feature-catalog-plt-032-administrative-change-audit.md)
