# Expiry-dated Document Alerting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks validity dates for licenses, referrals, authorizations, and other document classes and creates accountable renewal alerts.
Topics: openchart-feature-catalog, documents, frappe, document-expiry
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-035 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Renewal evidence request** — Generate a scoped task or outbound request for a replacement document before expiry.

## Focus

This feature isolates validity-date monitoring and renewal work without deciding the underlying credential or referral authority.

## Behavior

- An indexer records effective date, expiry date, issuing authority, identifier, and expiry basis for configured document classes.
- Class policy defines warning windows, responsible role, and whether expiry affects operational readiness.
- Scheduled evaluation creates one alert cycle per current document version and warning threshold.
- Assigned staff acknowledge, defer with reason, link a replacement, or mark the date as not applicable after review.
- A replacement becomes current only through normal document acceptance and explicit predecessor relationship.
- Superseded, rejected, or corrected versions close or recalculate their alerts without erasing history.
- Alerts inform humans and downstream readiness views but do not autonomously cancel care, credentials, or referrals.

## Frappe realization

- **DocTypes:** `OC Document Validity` (document_version, effective_on, expires_on, issuer, identifier, policy_version, state) and `OC Document Expiry Alert`.
- **Workflow:** Valid → Expiring → Expired → Replaced, with Date Review Required, Deferred, and Not Applicable states.
- **Roles/permissions:** Document Indexer captures; responsible department resolves; Credential/Referral Reviewer confirms domain-specific validity; identifiers use permlevel 1.
- **Automation:** scheduler_events, Notifications, Assignment Rules, and auto-repeat-like policy windows create deduplicated alerts.
- **Surfaces:** Calendar/list views, Number Cards, due-soon Query Report, and patient/subject timeline indicators.

## Boundaries

Owns: document validity metadata, warning cycles, assignments, and replacement linkage. Consumes: accepted document version and class policy. Emits: expiry/renewal events. Does not own: licensing authority, referral authorization, scheduling blocks, or clinical cancellation.

## Open questions

- Which expiry consequences are advisory versus blocking in each consuming workflow?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Department Document Routing Inbox](openchart-feature-catalog-dms-007-department-document-routing-inbox.md)
