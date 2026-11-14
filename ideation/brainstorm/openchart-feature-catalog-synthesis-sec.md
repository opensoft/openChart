# Synthesis: Security Privacy Audit And Access Control — Brainstorm

Status: brainstorm
Kind: reference
Summary: Relates fifty-five hardened-by-default controls into a coherent security, privacy, audit, identity, resilience, and rights-enforcement architecture for openChart.
Topics: openchart-feature-catalog, security, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog entry SEC synthesis (Security Privacy Audit And Access Control)
Captured: 2026-08-24

## Possible feats

- **Evidence-backed zero-trust conformance suite** — Exercise every authorization seam with synthetic `SYN-` patients, identities, integrations, and failure cases before a site enables production use.

## Focus

This synthesis connects the SEC catalog entries so identity assurance, least privilege, consent, minimum-necessary disclosure, tamper-evident audit, privacy rights, and operational security reinforce one another. The catalog anchor is `openchart-feature-catalog`; every member remains brainstorm material rather than an implemented or ratified control.

## Members and their joints

### Authorization, confidentiality, and consent

[Role-Based Access Control Matrix Editor](openchart-feature-catalog-sec-001-role-based-access-control-matrix-editor.md) · [Fine-Grained Clinical Action Permissions](openchart-feature-catalog-sec-002-fine-grained-clinical-action-permissions.md) · [Provider and Patient Scope Row Filtering](openchart-feature-catalog-sec-003-provider-and-patient-scope-row-filtering.md) · [Break-Glass Emergency Access](openchart-feature-catalog-sec-004-break-glass-emergency-access.md) · [Minimum-Necessary Contextual Field Masking](openchart-feature-catalog-sec-005-minimum-necessary-contextual-field-masking.md) · [Confidential and VIP Patient Restrictions](openchart-feature-catalog-sec-006-confidential-and-vip-patient-restrictions.md) · [Adolescent Confidentiality Across Surfaces](openchart-feature-catalog-sec-007-adolescent-confidentiality-across-surfaces.md) · [Granular Consent Management Engine](openchart-feature-catalog-sec-008-granular-consent-management-engine.md) · [Recipient Organization Sharing Consent](openchart-feature-catalog-sec-009-recipient-organization-sharing-consent.md) · [Research Consent API Filtering](openchart-feature-catalog-sec-010-research-consent-api-filtering.md)

Permission, row scope, masking, confidential populations, and consent combine into one deny-by-default disclosure decision.

### Identity, sessions, and authentication

[Session Timeout and Reauthentication](openchart-feature-catalog-sec-011-session-timeout-and-reauthentication.md) · [Concurrent Session Control](openchart-feature-catalog-sec-012-concurrent-session-control.md) · [Trusted Device Binding](openchart-feature-catalog-sec-013-trusted-device-binding.md) · [MFA Enrollment Policy](openchart-feature-catalog-sec-014-mfa-enrollment-policy.md) · [Conditional MFA by Risk](openchart-feature-catalog-sec-015-conditional-mfa-by-risk.md) · [Staff SSO via OIDC and SAML](openchart-feature-catalog-sec-016-staff-sso-oidc-and-saml.md) · [LDAP and Active Directory Sync](openchart-feature-catalog-sec-017-ldap-and-active-directory-sync.md) · [Password Policy and Breach-List Checks](openchart-feature-catalog-sec-018-password-policy-and-breach-list-checks.md) · [Account Lockout and Brute-Force Protection](openchart-feature-catalog-sec-019-account-lockout-and-brute-force-protection.md) · [Privileged Credential Rotation Reminders](openchart-feature-catalog-sec-020-privileged-credential-rotation-reminders.md)

Session evidence, authenticators, federation, directory state, and credential defenses establish who is acting and at what assurance.

### Audit, monitoring, and privacy response

[Comprehensive Clinical Record Audit](openchart-feature-catalog-sec-021-comprehensive-clinical-record-audit.md) · [Append-Only Hash-Chained Audit Ledger](openchart-feature-catalog-sec-022-append-only-hash-chained-audit-ledger.md) · [Audit Search and Saved Reports](openchart-feature-catalog-sec-023-audit-search-and-saved-reports.md) · [User Activity Anomaly Alerts](openchart-feature-catalog-sec-024-user-activity-anomaly-alerts.md) · [Access Review Certification Campaigns](openchart-feature-catalog-sec-025-access-review-certification-campaigns.md) · [Privacy Incident Register](openchart-feature-catalog-sec-026-privacy-incident-register.md) · [Breach Risk Assessment Worksheet](openchart-feature-catalog-sec-027-breach-risk-assessment-worksheet.md) · [Accounting of Disclosures](openchart-feature-catalog-sec-028-accounting-of-disclosures.md)

Complete events become tamper-evident evidence, searchable oversight, anomaly signals, certifications, incident cases, and patient disclosure accounts.

### Cryptography, transport, and resilience

[Encryption-at-Rest Configuration Verification](openchart-feature-catalog-sec-029-encryption-at-rest-configuration-verification.md) · [Field-Level Encryption for Sensitive Identifiers](openchart-feature-catalog-sec-030-field-level-encryption-for-sensitive-identifiers.md) · [TLS and mTLS Integration Policy](openchart-feature-catalog-sec-031-tls-and-mtls-integration-policy.md) · [Vault-Backed Secrets Management](openchart-feature-catalog-sec-032-vault-backed-secrets-management.md) · [IP Allowlisting by Role and Site](openchart-feature-catalog-sec-033-ip-allowlisting-by-role-and-site.md) · [Geo-Access Impossibility Detection](openchart-feature-catalog-sec-034-geo-access-impossibility-detection.md) · [EPCS Identity-Proofing Records](openchart-feature-catalog-sec-035-epcs-identity-proofing-records.md) · [Electronic Signature Ceremony Integrity](openchart-feature-catalog-sec-036-electronic-signature-ceremony-integrity.md) · [Document Tamper-Evidence Checksums](openchart-feature-catalog-sec-037-document-tamper-evidence-checksums.md) · [Backup Encryption Verification Jobs](openchart-feature-catalog-sec-038-backup-encryption-verification-jobs.md) · [Disaster Recovery Drill Evidence](openchart-feature-catalog-sec-039-disaster-recovery-drill-evidence.md)

Encryption, secure transport, vault references, network controls, signature integrity, backups, and recovery create hardened technical boundaries.

### Vulnerability and workforce assurance

[Vulnerability Disclosure Intake](openchart-feature-catalog-sec-040-vulnerability-disclosure-intake.md) · [Dependency CVE Monitoring and Triage](openchart-feature-catalog-sec-041-dependency-cve-monitoring-and-triage.md) · [Deployment Patch Campaign Tracking](openchart-feature-catalog-sec-042-deployment-patch-campaign-tracking.md) · [Hardening Baseline Self-Assessment](openchart-feature-catalog-sec-043-hardening-baseline-self-assessment.md) · [Security Training Attestations](openchart-feature-catalog-sec-044-security-training-attestations.md) · [Phishing Report Integration Hooks](openchart-feature-catalog-sec-045-phishing-report-integration-hooks.md)

Researcher intake, CVE triage, patch campaigns, hardening checks, training, and phishing reports close operational security feedback loops.

### Privacy rights, lifecycle, vendors, and governance

[Data Retention and Legal Hold Engine](openchart-feature-catalog-sec-046-data-retention-and-legal-hold-engine.md) · [Right-of-Access Request Fulfillment](openchart-feature-catalog-sec-047-right-of-access-request-fulfillment.md) · [Privacy Restriction Request Handling](openchart-feature-catalog-sec-048-privacy-restriction-request-handling.md) · [Minor Data Age-Transition Rules](openchart-feature-catalog-sec-049-minor-data-age-transition-rules.md) · [Deceased Patient Access Window Policy](openchart-feature-catalog-sec-050-deceased-patient-access-window-policy.md) · [Vendor and BAA Registry](openchart-feature-catalog-sec-051-vendor-and-baa-registry.md) · [Penetration-Test Remediation Tracker](openchart-feature-catalog-sec-052-penetration-test-remediation-tracker.md) · [Administrator Security Posture Scorecard](openchart-feature-catalog-sec-053-administrator-security-posture-scorecard.md) · [Delegated Security Administration](openchart-feature-catalog-sec-054-delegated-security-administration.md) · [API Scope and Object Authorization](openchart-feature-catalog-sec-055-api-scope-and-object-authorization.md)

Retention, individual rights, life transitions, third-party assurance, remediation, posture, delegation, and API checks make governance enforceable end to end.

## Frappe realization

- **Control plane:** Model shared policy metadata in `OC Security Policy`, decision evidence in `OC Security Decision`, and normalized append-only activity in `OC Audit Event`, while member DocTypes retain their own workflows and provenance.
- **Authorization:** Use Role Permission Manager for baseline DocPerms, user permissions for patient/provider/facility/site scope, permlevels 1–2 for restricted evidence, and server-side permission query conditions plus `has_permission` checks for row and object access.
- **Audit hooks:** Register central `hooks.py` `doc_events` for `validate`, `before_save`, `after_insert`, `on_update`, and `on_submit`; all supported read, search, print, and export APIs explicitly append view events because document hooks alone cannot observe reads.
- **API boundary:** Route protected writes and policy evaluation through versioned `open_chart.api.v1.security` whitelisted methods; direct Frappe REST writes are guarded, and each API combines role, user permission, consent, purpose, session assurance, and object relationship checks.
- **Operations:** Use scheduler events and background jobs for reviews, integrity verification, CVE triage, retention, drills, and scorecards; publish permission-aware Script Reports and dashboards in a Security and Privacy Desk workspace.
- **Safety:** Synthetic `SYN-` fixtures exercise IDOR, stored and reflected XSS, certificate-verification failure, privilege escalation, audit tampering, and consent revocation so the cautionary defects seen in legacy EHR advisories become explicit negative tests rather than copied implementation patterns.

## Boundaries

Owns: openChart security and privacy policy evidence, authorization decisions, audit records, and control workflows. Consumes: identity providers, directory sources, vaults, infrastructure attestations, advisory feeds, legal policy configuration, and clinical context. Emits: allow or deny decisions, review assignments, alerts, disclosure evidence, remediation tasks, and posture measures. Does not own: external identity systems, encryption keys, legal advice, vendor infrastructure, billing operations, or autonomous clinical decisions.

## Emergent behavior

The combined system can explain not only whether access occurred, but who acted, under which identity assurance, role, relationship, consent, purpose, patient restriction, network context, and policy version. Technical controls feed review campaigns and incident workflows; those outcomes feed remediation and scorecards without letting scores or anomaly models autonomously interrupt care. Immediate consent revocation, object-level API checks, and surface-independent masking prevent a valid session or broad role from becoming an IDOR path. Tamper-evident audit, signature hashes, document checksums, encrypted backups, and recovery drills preserve trustworthy evidence across the full record lifecycle.

## Tensions to hold

- Emergency access must remain clinically usable while being narrow, conspicuous, time-bounded, and retrospectively accountable.
- Minimum-necessary masking and confidentiality segmentation must remain consistent across Desk, portal, print, search, reports, notifications, and APIs without making care context unintelligible.
- Strong authentication and network controls can raise friction; exceptions must be explicit and expiring rather than hidden bypasses.
- Audit completeness competes with data minimization, retention limits, legal holds, and the need not to duplicate clinical payloads.
- Open-source deployments vary in infrastructure maturity, so verification must distinguish failed, passed, and inconclusive evidence rather than claiming universal compliance.

## Recombination opportunities

- Combine the authorization matrix, clinical action objects, API policy, and conformance fixtures into an executable least-privilege test harness.
- Join consent, confidentiality, masking, accounting, and rights workflows into a patient-facing privacy control center.
- Feed audit integrity, anomaly review, certification, incident, vulnerability, and remediation evidence into a non-gameable governance board report.
- Couple transport policy, vault references, vendor agreements, and patch posture so an integration cannot remain active after its trust prerequisites expire.
- Use lifecycle transitions, retention rules, legal holds, signature evidence, and disaster-recovery drills to prove continuity without rewriting accepted history.

## Open questions

- Which controls are mandatory platform invariants, which are site-configurable policies, and which require jurisdiction-specific rule packs?
- What independent trust anchor best protects audit integrity from a compromised site administrator?
- How should openChart publish secure defaults without implying regulatory certification for every deployment?
- Which emergency paths remain available when identity, vault, directory, or network dependencies are unavailable?

## Relationships

Catalog anchor: `openchart-feature-catalog`. All fifty-five SEC members are linked above; no cross-domain relationship is asserted in this batch.
