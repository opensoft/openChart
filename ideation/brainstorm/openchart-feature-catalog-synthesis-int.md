# Synthesis: Interoperability Exchange And APIs — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects standards APIs, trusted exchange routes, reconciliation, sector pipelines, portability, and operational governance into one Frappe-native interoperability fabric.
Topics: openchart-feature-catalog, interoperability, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Interoperability Exchange And APIs domain synthesis
Captured: 2026-08-24

## Possible feats

- **Conformance and exchange control plane** — Combine API parity, partner health, consent decisions, channel exceptions, provenance coverage, and service levels into one human-governed release and operations cockpit.

## Focus

This synthesis relates all 65 Interoperability Exchange And APIs capabilities and identifies the authority, trust, state, semantic, and evidence seams that let them operate as a coherent domain.

## Members and their joints

### Standards-based API platform

- [FHIR R4 US Core Server](openchart-feature-catalog-int-001-fhir-r4-us-core-server.md) — standards-conformant resources and operation outcomes.
- [FHIR Capability Statement Publication](openchart-feature-catalog-int-002-fhir-capability-statement-publication.md) — a versioned machine-readable CapabilityStatement matching deployed behavior.
- [Provider-context SMART App Launch](openchart-feature-catalog-int-003-provider-context-smart-app-launch.md) — a short-lived SMART authorization flow with bounded clinical context.
- [Patient-standalone SMART App Launch](openchart-feature-catalog-int-004-patient-standalone-smart-launch.md) — a patient-authorized token set limited to permitted records.
- [OAuth2 and OIDC Token Console](openchart-feature-catalog-int-005-oauth2-oidc-token-console.md) — searchable token lifecycle visibility with targeted revocation.
- [Granular Third-party App Scope Administration](openchart-feature-catalog-int-006-granular-third-party-app-scope-administration.md) — versioned least-privilege scope policies per app.
- [Third-party App Registration and Vetting](openchart-feature-catalog-int-007-third-party-app-registration-and-vetting.md) — an approved or rejected registration with accountable rationale.
- [Population Bulk FHIR Export](openchart-feature-catalog-int-008-population-bulk-fhir-export.md) — asynchronous NDJSON manifests with secure expiring file access.
- [System-level Integrator API Keys](openchart-feature-catalog-int-009-system-level-integrator-api-keys.md) — revocable machine credentials backed by Frappe token authentication.
- [Per-consumer Rate Limits and Quotas](openchart-feature-catalog-int-010-per-consumer-rate-limits-and-quotas.md) — enforced quotas with current usage, reset time, and retry guidance.
- [API Parity Release Gate](openchart-feature-catalog-int-011-api-parity-release-gate.md) — a release gate proving every governed UI feature has documented API reach or an approved exception.
- [Code-generated API Documentation Portal](openchart-feature-catalog-int-012-code-generated-api-documentation-portal.md) — searchable documentation that cannot drift silently from deployed contracts.
- [API Deprecation Header and Notice Enforcement](openchart-feature-catalog-int-013-api-deprecation-header-and-notice-enforcement.md) — consistent response headers, notices, and acknowledgement tracking.
- [Versioned API Coexistence Lifecycle](openchart-feature-catalog-int-014-versioned-api-coexistence-lifecycle.md) — predictable v1 and v2 coexistence with explicit retirement criteria.
- [Partner Sandbox Self-service](openchart-feature-catalog-int-015-partner-sandbox-self-service.md) — isolated synthetic-data access with reset and credential rotation controls.
- [Synthetic Test-patient Data Generator](openchart-feature-catalog-int-016-synthetic-test-patient-data-generator.md) — clearly marked SYN- patients and interoperable records safe for testing.

The joint is shared authority and evidence: FHIR, SMART, OAuth, partner onboarding, documentation, versioning, parity, and safe test data form one externally consumable API product.

### Events, disclosure, security, and compliance

- [Clinical Event Webhook Subscriptions](openchart-feature-catalog-int-017-clinical-event-webhook-subscriptions.md) — consent-aware outbound notifications with delivery evidence.
- [Event-driven Integration Bus](openchart-feature-catalog-int-018-event-driven-integration-bus.md) — decoupled delivery with bounded retries and idempotent consumer checkpoints.
- [Sensitive Export Payload Signing](openchart-feature-catalog-int-019-sensitive-export-payload-signing.md) — detached signatures and verification metadata for tamper-evident exchange.
- [Consent-aware API Response Filtering](openchart-feature-catalog-int-020-consent-aware-api-response-filtering.md) — minimum-necessary FHIR and API responses honoring proxy and adolescent restrictions.
- [API Break-glass Emergency Access](openchart-feature-catalog-int-021-api-break-glass-emergency-access.md) — time-bounded exceptional API access with immediate audit and review.
- [Information-blocking Access and Denial Reports](openchart-feature-catalog-int-022-information-blocking-access-and-denial-reports.md) — auditable metrics for access performance, denials, delays, and asserted exceptions.
- [Patient-requested Data Exchange Fulfillment](openchart-feature-catalog-int-023-patient-requested-data-exchange-fulfillment.md) — tracked electronic fulfillment or a reasoned denial with appeal path.

The joint is shared authority and evidence: Webhooks and the event bus carry governed changes while signing, consent filtering, emergency access, and compliance reports constrain disclosure.

### Clinical document exchange and reconciliation

- [On-demand C-CDA Generation](openchart-feature-catalog-int-024-on-demand-ccda-generation.md) — validated C-CDA artifact generated for immediate review and delivery.
- [Scheduled C-CDA Delivery](openchart-feature-catalog-int-025-scheduled-ccda-delivery.md) — recurring C-CDA packages with per-run evidence and retry policy.
- [C-CDA Structured Import Reconciliation](openchart-feature-catalog-int-026-ccda-structured-import-reconciliation.md) — sectioned candidate facts with accept, reject, defer, and conflict decisions.
- [Outside-record Side-by-side Comparison](openchart-feature-catalog-int-027-outside-record-side-by-side-comparison.md) — field-level differences with accept, reject, and defer controls.
- [Selective External-data Write-back](openchart-feature-catalog-int-028-selective-external-data-write-back.md) — guarded clinical writes carrying external-source and reviewer lineage.
- [Imported-record Duplicate Detection](openchart-feature-catalog-int-029-imported-record-duplicate-detection.md) — ranked duplicate candidates with explainable match evidence.
- [Universal Imported-artifact Provenance](openchart-feature-catalog-int-030-universal-imported-artifact-provenance.md) — queryable lineage attached to every imported clinical artifact.

The joint is shared authority and evidence: C-CDA, comparison, duplicate review, selective write-back, and universal provenance turn outside data into reviewable clinical candidates.

### Direct, national exchange, and discovery

- [Direct Secure-mail Inbox and Outbox](openchart-feature-catalog-int-031-direct-secure-mail-inbox-and-outbox.md) — encrypted inbound and outbound clinical mail with accountable handling.
- [Direct Address Book and Trust Bundles](openchart-feature-catalog-int-032-direct-address-book-and-trust-bundles.md) — searchable trusted recipients and governed certificate acceptance.
- [HISP Connectivity Management](openchart-feature-catalog-int-033-hisp-connectivity-management.md) — validated HISP connections with health and failover evidence.
- [National Network and QHIN-path Configuration](openchart-feature-catalog-int-034-national-network-qhin-path-configuration.md) — governed TEFCA or QHIN-path connectivity with explicit permitted uses.
- [Provider Directory Endpoint Publication](openchart-feature-catalog-int-035-provider-directory-endpoint-publication.md) — validated directory entries and discoverable exchange endpoints.

The joint is shared authority and evidence: Direct messaging, trust, HISP connections, national-network paths, and published endpoints establish discoverable trusted routes.

### HL7 channels and semantic control

- [HL7 v2 ADT Endpoint](openchart-feature-catalog-int-036-hl7-v2-adt-endpoint.md) — validated admit, discharge, transfer, and demographic events with acknowledgments.
- [HL7 v2 ORM Endpoint](openchart-feature-catalog-int-037-hl7-v2-orm-endpoint.md) — validated external order lifecycle updates with deterministic acknowledgments.
- [HL7 v2 ORU Endpoint](openchart-feature-catalog-int-038-hl7-v2-oru-endpoint.md) — discrete or document results linked to the correct patient and order.
- [HL7 v2 SIU Endpoint](openchart-feature-catalog-int-039-hl7-v2-siu-endpoint.md) — reconciled scheduling events with duplicate-safe acknowledgments.
- [Interface Channel Monitoring Dashboard](openchart-feature-catalog-int-040-interface-channel-monitoring-dashboard.md) — near-real-time throughput and failure visibility per channel.
- [Message Replay and Dead-letter Tooling](openchart-feature-catalog-int-041-message-replay-and-dead-letter-tooling.md) — controlled idempotent replay with original and new attempt lineage.
- [Terminology Mapping Service](openchart-feature-catalog-int-042-terminology-mapping-service.md) — versioned local-to-LOINC, SNOMED CT, ICD, and RxNorm translations with confidence.
- [Human Terminology Mapping Editor](openchart-feature-catalog-int-043-human-terminology-mapping-editor.md) — reviewed mappings with dual-control approval for high-impact concepts.
- [Value-set Lifecycle Management](openchart-feature-catalog-int-044-value-set-lifecycle-management.md) — versioned value sets with reproducible expansions and impact analysis.

The joint is shared authority and evidence: Typed HL7 endpoints share channel observability and replay controls, while terminology and value-set governance preserve meaning.

### Public-health, laboratory, payer, pharmacy, and device links

- [Immunization Registry Bidirectional Pipeline](openchart-feature-catalog-int-045-immunization-registry-bidirectional-pipeline.md) — submitted immunizations, acknowledgments, query responses, and reconciliation tasks.
- [Syndromic Surveillance Pipeline](openchart-feature-catalog-int-046-syndromic-surveillance-pipeline.md) — minimum-necessary syndromic messages with acknowledgment evidence.
- [Electronic Case Reporting Pipeline](openchart-feature-catalog-int-047-electronic-case-reporting-pipeline.md) — reviewable electronic case reports and reportability responses.
- [Electronic Laboratory Reporting Pipeline](openchart-feature-catalog-int-048-electronic-laboratory-reporting-pipeline.md) — timely ELR messages, acknowledgments, corrections, and exception evidence.
- [Laboratory Network Connector Console](openchart-feature-catalog-int-049-laboratory-network-connector-console.md) — managed lab connections with versioned mapping and health evidence.
- [Payer Eligibility 270 and 271 Channel](openchart-feature-catalog-int-050-payer-eligibility-channel.md) — transported eligibility requests and normalized 271 response handoffs.
- [Payer Claims 837 Transport Channel](openchart-feature-catalog-int-051-payer-claims-837-transport-channel.md) — secure claims transport and acknowledgment handoff to the owning financial system.
- [Electronic Remittance 835 Transport Channel](openchart-feature-catalog-int-052-electronic-remittance-835-transport-channel.md) — validated 835 retrieval and normalized handoff with duplicate protection.
- [Prior Authorization 278 Transport Channel](openchart-feature-catalog-int-053-prior-authorization-278-transport-channel.md) — secure prior-authorization request and response transport with status correlation.
- [Payer Response Normalization](openchart-feature-catalog-int-054-payer-response-normalization.md) — canonical response facts, raw-source linkage, and explicit unmapped elements.
- [E-prescribing Network Transport Management](openchart-feature-catalog-int-055-e-prescribing-network-transport-management.md) — managed NewRx, refill, cancel, status, and medication-history transport connections.
- [Device Gateway Vitals Ingest API](openchart-feature-catalog-int-056-device-gateway-vitals-ingest-api.md) — validated candidate vital observations with source lineage and review policy.

The joint is shared authority and evidence: Sector-specific pipelines reuse common connection, acknowledgment, normalization, security, and exception semantics without absorbing downstream workflows.

### Portability, migration, and operational assurance

- [Cross-organization Chart Transfer Package](openchart-feature-catalog-int-057-cross-organization-chart-transfer-package.md) — portable chart package with checksums, provenance, and import instructions.
- [Full EHI Export Including Media](openchart-feature-catalog-int-058-full-ehi-export-including-media.md) — complete machine-readable EHI archive with manifest, media, checksums, and exclusions report.
- [Full Record-set Import](openchart-feature-catalog-int-059-full-record-set-import.md) — staged full-record candidates with reconciliation and per-item outcomes.
- [EMR Migration Toolkit](openchart-feature-catalog-int-060-emr-migration-toolkit.md) — repeatable staged migrations with dry-run, reconciliation, and signed acceptance evidence.
- [OpenEMR Migration Mapping Templates](openchart-feature-catalog-int-061-openemr-migration-mapping-templates.md) — versioned original mapping templates into openChart clinical contracts without copying implementation code.
- [Epic and Community-format Migration Templates](openchart-feature-catalog-int-062-epic-community-format-migration-templates.md) — versioned mapping templates for common community transition formats.
- [Mutual TLS and Client Certificate Management](openchart-feature-catalog-int-063-mutual-tls-client-certificate-management.md) — governed mTLS identities with expiry warnings and zero-downtime rotation windows.
- [API Audit and Correlation Explorer](openchart-feature-catalog-int-064-api-audit-and-correlation-explorer.md) — permissioned end-to-end traces across API, queue, webhook, and import events.
- [Integration Service-level Health Dashboard](openchart-feature-catalog-int-065-integration-service-level-health-dashboard.md) — service-level trends and actionable breach evidence per integration.

The joint is shared authority and evidence: Transfer packages, EHI movement, migration templates, certificates, audit traces, and service-level health make exchange portable and operable over time.

## Frappe realization

- **Core model:** OC-prefixed app, credential, policy, exchange, channel, message, mapping, import, export, provenance, audit, and service-level DocTypes use explicit versions, correlation IDs, and succession-based correction for accepted clinical records.
- **Native extension:** Frappe REST, token authentication, and OAuth2 remain the base; `open_chart.api.v1` adds FHIR, SMART, disclosure, exchange, connector, migration, and operations contracts rather than creating a parallel identity stack.
- **Workflows and permissions:** Frappe Workflows separate partner submission, technical review, clinical reconciliation, security approval, replay, release, and retirement; DocPerms and user permissions enforce organization, facility, patient, and purpose boundaries.
- **Events and jobs:** `doc_events` publish canonical integration events only after accepted transactions; `scheduler_events` and RQ jobs run exports, channels, retries, polling, expiry, conformance probes, and service-level aggregation with idempotency.
- **Surfaces:** Desk workspaces, Kanban queues, Query and Script Reports, Number Cards, Dashboard Charts, public documentation pages, and partner or patient portal pages project the same server-authoritative records.
- **Audit and safety:** Every import, disclosure, emergency grant, transformation, replay, and delivery records actor, source, policy version, purpose, provenance, and correlation; ambiguous authority denies or quarantines rather than guessing.

## Boundaries

Owns: openChart API contracts, exchange configuration, transport state, reconciliation evidence, terminology mappings, imported-artifact lineage, portability packages, and integration operations. Consumes: patient identity, consent, clinical records, organization and provider authority, partner contracts, and external standards. Emits: standards payloads, acknowledged messages, guarded clinical candidates, events, metrics, and audit evidence. Does not own: partner systems, national networks, source truth before reconciliation, billing or claims workflows, prescribing decisions, certificate authorities, or public-health adjudication.

## Emergent behavior

Together these features make API completeness a product invariant rather than an afterthought: each governed UI capability must map to a tested and documented API contract, and the same contract participates in consent filtering, provenance, rate policy, audit correlation, and lifecycle notices. Trusted routes then carry those contracts through FHIR, C-CDA, Direct, HL7, sector networks, webhooks, bulk export, and migration without allowing transport success to masquerade as clinical acceptance. Operators can trace one request from authorization through queue attempts, semantic mapping, reconciliation, delivery, and service-level impact.

## Tensions to hold

- Broad exchange and information-access duties must coexist with proxy, adolescent, consent, minimum-necessary, and emergency-access protections.
- Fast automated transport improves timeliness, but patient matching, semantic ambiguity, duplicate detection, and clinical write-back require accountable human decisions.
- Native Frappe REST and OAuth2 reduce duplicate infrastructure, while FHIR, SMART, bulk data, signed payloads, and partner isolation require carefully bounded extensions.
- Version coexistence protects consumers, but indefinite compatibility creates security, documentation, and maintenance debt; deprecation evidence must make retirement governable.
- Rich operational traces help support and compliance, but payload minimization, redaction, retention, and role-limited access remain mandatory.

## Recombination opportunities

- Combine API parity records, generated documentation, conformance probes, deprecation notices, and sandbox scenarios into an executable release certification gate.
- Combine consent decisions, SMART scopes, bulk exports, patient requests, break-glass grants, and information-blocking metrics into a disclosure-policy feedback loop.
- Combine imported-artifact provenance, terminology versions, duplicate candidates, field decisions, and write-back lineage into a longitudinal external-data evidence graph.
- Combine channel telemetry, dead letters, certificate expiry, partner quotas, audit correlation, and service levels into a cross-transport integration command center.
- Combine migration rehearsals, full-record import, EHI export, chart transfer, and synthetic datasets into a portable onboarding and exit-assurance program.

## Open questions

- Which US Core version, implementation guides, national-network paths, and jurisdictional profiles form the first supported conformance matrix?
- Which exchange actions require dual approval, clinical review, patient confirmation, or compliance review, and where may policy permit straight-through processing?
- What canonical event envelope and provenance model can span REST, FHIR, HL7 v2, documents, files, webhooks, and background jobs without flattening source meaning?
- Which service-level objectives and deprecation windows are public commitments versus tenant-configurable operating targets?
- How should openChart expose financial transports while preserving openPractice ownership of claims, remittance posting, eligibility workflows, and prior-authorization operations?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
