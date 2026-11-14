# API Key Lifecycle Administration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs creation, scoped display, rotation, suspension, expiry, and revocation of machine API credentials.
Topics: openchart-feature-catalog, platform, frappe, api-key-lifecycle
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-034 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Automated consumer rotation handshake** — Coordinate overlap and proof-of-use before retiring an old key.

## Focus

This feature isolates Frappe token lifecycle administration without storing recoverable secrets in ordinary configuration records.

## Behavior

- Integration administrators request a credential for a service identity, site, purpose, scopes, expiry, owner, and network constraints.
- Approval creates a secret shown once through a protected channel; only a fingerprint and vault reference remain visible.
- Credentials move through Requested, Active, Rotation Pending, Suspended, Expired, Revoked, and Compromised states.
- Rotation supports a bounded overlap window and reports which fingerprint last succeeded.
- Revocation blocks new authentication immediately and preserves prior request audit by credential fingerprint.
- Unknown owner, excess scope, overdue rotation, anomalous use, or expired credentials create review alerts.

## Frappe realization

- **DocTypes:** `OC API Credential` stores service User, site, scopes, fingerprint, vault reference, dates, owner, and state; secret material is excluded.
- **Workflow:** Integration Administrator requests; Security Approver activates, suspends, or marks compromised.
- **API/hooks:** guarded methods create Frappe API secrets, rotate, and revoke; authentication logs attach credential fingerprint and correlation ID.
- **Surface:** lifecycle dashboard shows age, expiry, last use, scope, and rotation status without secret values.

## Boundaries

Owns: machine credential lifecycle, scope record, and fingerprint evidence. Consumes: service identity, approval, and vault. Emits: active authentication material and revocation events. Does not own: human sessions, OAuth client policy, or integration business logic.

## Open questions

- What maximum overlap window balances rotation reliability with exposure risk?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Integration Credentials Vault](openchart-feature-catalog-plt-035-integration-credentials-vault.md) · [Administrative Change Audit](openchart-feature-catalog-plt-032-administrative-change-audit.md)
