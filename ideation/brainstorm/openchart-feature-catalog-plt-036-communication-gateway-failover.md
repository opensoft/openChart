# Communication Gateway Failover — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Configures email and SMS gateways with site-scoped routing, health checks, compliant failover, and delivery evidence.
Topics: openchart-feature-catalog, platform, frappe, gateway-failover
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-036 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Channel continuity drills** — Exercise approved failover routes with synthetic recipients and measured recovery time.

## Focus

This feature isolates transport configuration and failover while keeping recipient consent and message content upstream.

## Behavior

- Communications operators define email or SMS gateway bindings with site, region, sender identity, priority, credential reference, and capabilities.
- Synthetic health checks test authentication and delivery without using real patient destinations.
- Bindings move through Draft, Testing, Active, Degraded, Suspended, Failed, and Retired states.
- Routing selects the highest-priority healthy gateway compatible with channel, region, sender, and message class.
- Failover records the original route, reason, selected replacement, and delivery correlation; it never crosses a prohibited residency boundary.
- If no approved route exists, the message remains queued or fails visibly according to purpose-specific policy.

## Frappe realization

- **DocTypes:** `OC Communication Gateway` stores channel, provider, site, region, sender, credential Link, priority, capabilities, and state.
- **Integration:** adapters connect Frappe Email Account/`frappe.email` and SMS Settings points to the route resolver.
- **Automation:** scheduled synthetic probes update health; Notification Log stores gateway fingerprint, attempts, and final status.
- **Permissions:** Communications Operator configures and tests; Security Approver binds credentials; Site Administrator reads local health.

## Boundaries

Owns: gateway bindings, routing, health, and failover evidence. Consumes: rendered messages, channel requirements, region policy, and secret references. Emits: transport attempts and outcomes. Does not own: template content, consent, or carrier infrastructure.

## Open questions

- Which message purposes should queue rather than fail over to a provider with different delivery semantics?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Notification Template Editor](openchart-feature-catalog-plt-014-notification-template-editor.md) · [Integration Credentials Vault](openchart-feature-catalog-plt-035-integration-credentials-vault.md)
