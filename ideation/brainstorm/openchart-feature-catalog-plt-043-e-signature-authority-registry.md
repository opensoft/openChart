# E-signature Authority Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines effective, evidence-backed rules for who may sign or co-sign each governed document class and context.
Topics: openchart-feature-catalog, platform, frappe, signature-authority
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-043 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Authority simulation** — Explain whether a synthetic actor can sign a document under a proposed policy version.

## Focus

This feature isolates signing eligibility configuration from the signature ceremony and from provider credential source records.

## Behavior

- Authorized administrators define document class, signer role, provider type, credential requirements, facility scope, co-sign rules, and effective dates.
- Policies move through Draft, Legal Review, Clinical Review, Active, Suspended, Retired, and Superseded states.
- Evaluation returns Allowed, Co-sign Required, Blocked, or Review Required with cited policy and credential facts.
- Expired credentials, suspended providers, inactive affiliations, or missing scope block new signatures but do not invalidate historical ones.
- Emergency exceptions require a named approver, reason, expiry, and retrospective review task.
- Policy changes never rewrite signature evidence already attached to accepted records.

## Frappe realization

- **DocTypes:** `OC Signature Authority Policy` stores document DocType, roles, provider types, credential rules, scopes, co-sign conditions, version, and state.
- **Workflow:** Policy Administrator authors; Legal and Clinical Approvers activate; emergency exception uses separate Workflow Actions.
- **API:** `open_chart.api.v1.platform.evaluate_signature_authority` returns decision, policy version, and safe reasons to signing services.
- **Permissions:** permlevel-protected legal fields; provider and facility User Permissions constrain policy administration.

## Boundaries

Owns: signature eligibility policy and decision evidence. Consumes: provider, credentials, roles, affiliations, document context, and effective dates. Emits: authority decisions and review tasks. Does not own: cryptographic signing, authentication, or record acceptance.

## Open questions

- Which policy sources take precedence when site and organization rules conflict?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Provider Credential Expiry Monitoring](openchart-feature-catalog-plt-005-provider-credential-expiry-monitoring.md) · [Provider Delegation And Coverage](openchart-feature-catalog-plt-044-provider-delegation-and-coverage.md)
