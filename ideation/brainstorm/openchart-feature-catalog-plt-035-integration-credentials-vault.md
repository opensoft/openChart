# Integration Credentials Vault — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stores references to protected integration secrets and mediates least-privilege retrieval, rotation, and access evidence.
Topics: openchart-feature-catalog, platform, frappe, credentials-vault
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-035 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Secret dependency map** — Show which approved integrations and sites depend on a credential before rotation.

## Focus

This feature isolates credential custody so passwords, tokens, certificates, and keys never live in fixtures, logs, or ordinary DocType fields.

## Behavior

- Security administrators register a secret purpose, owner, site scope, external vault path, type, rotation policy, and consumers.
- The system stores only an opaque reference, fingerprint, metadata, and health state in Frappe.
- Runtime retrieval requires an approved consumer identity and returns the secret only in process memory for the bounded operation.
- Secret records move through Pending, Active, Rotation Due, Rotating, Suspended, Revoked, and Unavailable states.
- Access, denial, rotation, and health checks produce redacted evidence without secret values.
- Vault failure uses an explicitly configured fail-closed or limited fallback policy; plaintext fallback is prohibited.

## Frappe realization

- **DocTypes:** `OC Secret Reference` stores vault provider, path token, fingerprint, owner, scopes, consumers, dates, and state.
- **Hooks/API:** server-only vault adapter resolves references after role and consumer checks; `get_password` and client APIs never expose managed secrets.
- **Permissions:** Secret Custodian manages metadata; Integration Operator can test bindings but cannot reveal values; Audit Reviewer reads evidence.
- **Surface:** health and rotation dashboard shows references, dependencies, due dates, and access failures.

## Boundaries

Owns: secret references, access mediation, lifecycle metadata, and evidence. Consumes: external vault service and consumer identity. Emits: bounded in-memory credentials and status. Does not own: vault infrastructure or credential use inside third-party services.

## Open questions

- Which deployment profiles must support a local hardware-backed vault when no managed service is available?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [API Key Lifecycle Administration](openchart-feature-catalog-plt-034-api-key-lifecycle-administration.md) · [Communication Gateway Failover](openchart-feature-catalog-plt-036-communication-gateway-failover.md)
