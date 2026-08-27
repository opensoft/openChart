# Synthesis: Intelligence Platform — Brainstorm

Status: brainstorm
Kind: architecture
Summary: governed AI, open analytics, and a hardened mobile-first platform form openChart's strategic wedge — each capability amplifies the others into a trust-and-openness position neither OpenEMR nor the proprietary big-3 occupies.
Topics: openchart-feature-list, intelligence-platform-synthesis, synthesis, clinical-ai, population-health, emr-platform
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Trust stack** — AI artifact registry + immutable audit chain + break-glass governance = a compliance posture marketable to risk officers, not just clinicians.
- **Open intelligence loop** — semantic metric definitions make AI model performance publicly evaluable inside a deployment; monitoring dashboards are just more metrics.
- **Mobile as execution surface** — offline-capable apps carry bedside/home workflows where the accountability loops (acknowledge, scan, document) actually execute.
- **Managed-cloud trust delivery** — the subscription tier operationalizes patch SLAs and advisory response that self-hosted OpenEMR users must improvise.

## Members and their joints

Atomic members: [Clinical AI And Governance](openchart-feature-list-clinical-ai.md), [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md), [Platform Security And Deployment](openchart-feature-list-platform-and-security.md).

### AI ↔ Analytics

Model outputs are typed artifacts flowing into the same semantic layer as clinical facts; acceptance rates, override patterns, and drift signals become versioned metrics. Evaluation harnesses (golden sets) run against production-shaped definitions — AI governance without analytics is vibes.

### Platform ↔ AI

Mobile capture feeds ambient pipelines; device integration supplies signal; identity/MFA gates which models may act for whom; the artifact registry lives on the platform's append-only audit chain. Pluggable-model contracts need platform-grade isolation to let untrusted weights near PHI.

### Analytics ↔ Mobile

Dashboards follow role onto phones (Expanse Now pattern); home-care documentation executed offline syncs into cohort registries when connectivity returns — population health only works if field capture does.

### Managed cloud ↔ Everything

Update trains deliver model upgrades, metric-definition versions, and security patches atomically; the subscription tier is how governance promises become operationally real rather than aspirational documentation.

## Emergent behavior

Together the three produce something none ships alone: an EMR whose intelligence can be audited by its customers, whose metrics survive migration, whose field workflows keep working offline, and whose openness lets competitors' ecosystems plug in without surrendering governance. That composite is the answer to Epic's Cosmos moat (closed) and OpenEMR's assembly burden (ungoverned).

## Tensions to hold

Openness exposes unflattering internal metrics and enables fork-based competition; governance slows AI velocity competitors flaunt; native mobile spend competes with web-first reach; managed-cloud revenue needs licensing boundaries that must not poison community goodwill. Each tension is strategic, not incidental — resolving them prematurely collapses the differentiation.

## Recombination opportunities

Audit-chain infrastructure recombines with [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md) provenance requirements; semantic metrics recombine with [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md) pipeline-health measures; assistant surfaces recombine with [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md).

## Open questions

- What is the minimum evaluation infrastructure before any third-party model ships?
- Does the open-core boundary draw before or after managed-cloud pricing exists?
- Which single composite demo (offline home care? audited ambient note?) proves the wedge?

## Relationships

Owned by [Overview](openchart-feature-list-overview.md). Cross-cluster: [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md).
