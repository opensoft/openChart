# Prescriber Identity-Proofing Enrollment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides supervised prescriber identity proofing, authenticator binding, approval, and revocation for high-assurance electronic prescribing.
Topics: openchart-feature-catalog, eprescribing, frappe, identity-proofing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-012 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Periodic re-proofing campaigns** — Compliance teams could schedule risk-based re-verification before authority lapses.

## Focus

This feature isolates enrollment evidence and lifecycle for prescribers who require high-assurance signing. Clinical administrators cannot self-approve their own proofing or silently restore revoked enrollment.

## Behavior

- An enrollment case starts with verified user identity, professional identifiers, and required proofing method.
- A designated identity verifier records evidence references and result without storing unnecessary identity documents.
- The prescriber binds approved authentication factors and demonstrates possession.
- A separate approver confirms proofing, credential match, factor binding, and policy completion.
- Enrollment becomes active only after all required checks pass; failures remain reviewable with reason and retry policy.
- Revocation, factor loss, role change, or credential lapse immediately prevents new high-assurance signatures while preserving history.

## Frappe realization

- **DocTypes:** `OC Prescriber Assurance Enrollment` stores verifier/approver separation, evidence references, factor metadata, status, effective dates, and revocation reason.
- **Workflow:** Initiated → Proofing → Factor Binding → Independent Approval → Active → Suspended/Revoked/Expired.
- **Roles:** `OC Identity Verifier`, `OC EPCS Approver`, and `OC Prescriber` have segregated transition permissions and no self-approval path.
- **Surfaces/hooks:** Restricted Desk workspace, Assignment Rules, expiry notifications, and authority-check APIs expose only minimum necessary evidence.

## Boundaries

Owns: local enrollment decision, factor binding metadata, and revocation history. Consumes: authoritative identity and credential evidence. Emits: effective assurance status. Does not own: external identity-provider records or professional licensing truth.

## Open questions

- Which proofing evidence may be retained locally versus referenced by an external proofing provider?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescriber Credential Eligibility](openchart-feature-catalog-phr-013-prescriber-credential-eligibility.md)
