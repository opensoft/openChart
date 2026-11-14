# Prescriber Credential Eligibility — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates effective professional, jurisdictional, organizational, and controlled-substance credentials before a prescription can be signed.
Topics: openchart-feature-catalog, eprescribing, frappe, prescriber-credentials
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-013 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Credential-expiry intervention queue** — Administrators could resolve approaching expirations before prescribing access is interrupted.

## Focus

This feature isolates the effective authority check for the prescriber, patient location, medication schedule, and signature time. It records why signing was allowed or blocked without becoming the credentialing source of truth.

## Behavior

- The signer check evaluates active license, jurisdiction, organization privileges, DEA registration when applicable, schedule scope, and effective dates.
- Patient and encounter location determine which jurisdictional rules apply where configured.
- Missing, expired, suspended, or mismatched credentials block signature with a precise non-clinical reason.
- Authorized credentialing staff may correct source data but may not override a failed signing check inside the prescription.
- Every decision records the credential versions and policy release evaluated.
- Scheduled scans notify users and administrators before expiration without extending authority automatically.

## Frappe realization

- **DocTypes:** `OC Prescriber Credential` and child `OC Credential Scope` store type, issuer, jurisdiction, identifiers, schedules, effective dates, and verification source.
- **Permissions:** `OC Credentialing Administrator` maintains records; prescribers read their status; clinical records reference immutable eligibility snapshots.
- **Hooks/API:** A shared server service is called by `before_submit`; `scheduler_events` creates expiry notifications and access-review tasks.
- **Surfaces:** Credential dashboard, blocked-signature explanation, and expiring-credentials Query Report support operations.

## Boundaries

Owns: local eligibility evaluation and snapshots. Consumes: verified credential records, location, medication schedule, and policy. Emits: allow/block result and expiry tasks. Does not own: licensing-board or DEA source authority.

## Open questions

- How should telehealth location uncertainty affect jurisdiction checks at signing time?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [DEA Schedule Display](openchart-feature-catalog-phr-016-dea-schedule-display.md)
