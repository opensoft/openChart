# Synthesis: Clinical Core — Brainstorm

Status: brainstorm
Kind: architecture
Summary: openChart's point-of-care advantage comes from running documentation, orders, medications, labs, and imaging as one closed-loop, provenance-bearing circuit — the seams between these five domains are where OpenEMR leaks work and where the enterprise leaders hide their depth.
Topics: openchart-feature-list, clinical-core-synthesis, synthesis, clinical-documentation, cpoe, eprescribing, laboratory, imaging
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **One accountable clinical circuit** — a result or finding can never exist without an owner, and an owner can never be unassigned; the loop is structural, not procedural.
- **Ambient-to-action pipeline** — conversation → note draft → suggested order → suggested charge, each hop human-gated, each hop provenance-linked (Oracle agent-chain pattern with published governance).
- **Chart-wide semantic search** — one query across structured data, documents, faxes, and imported records answering "what do we know about this patient's X?" (Navigator pattern).
- **Closed-loop medication safety for ambulatory scale** — interaction/genotype/benefit checks at prescribe time plus barcode verification wherever administration happens.

## Members and their joints

Atomic members: [Clinical Documentation And Ambient Capture](openchart-feature-list-clinical-documentation.md), [Clinical Orders And Decision Support](openchart-feature-list-orders-and-cds.md), [Pharmacy And E-Prescribing](openchart-feature-list-pharmacy-and-eprescribing.md), [Labs And Diagnostics](openchart-feature-list-labs-and-diagnostics.md), [Imaging Workflows](openchart-feature-list-imaging-workflows.md).

### Documentation ↔ Orders

The note proposes; the order commits. Ambient capture drafts both together (Oracle order creation from conversation), so documentation and ordering must share one draft/review state machine rather than two. If they diverge, clinicians re-enter data — OpenEMR's core friction.

### Orders ↔ Labs/Imaging

Orders create fulfillment obligations in labs-and-diagnostics and imaging-workflows; results return into the Result Accountability object (owner, acknowledgment, escalation). The seam is a contract, not an interface convention: no result may arrive unowned, no order may close unfulfilled silently.

### Pharmacy ↔ Labs

Drug–gene decision support makes genotype observations (labs) inputs to prescribing safety (pharmacy) — MEDITECH productizes this; OpenEMR cannot express it. Benefit/formulary responses also flow lab-like (external network data into prescribing flow).

### Results ↔ Documentation

Abnormal findings must become documented clinical reasoning: acknowledged results pre-fill note context, and signed notes cite which results informed them. This closes the medico-legal loop Epic handles implicitly through In Basket routing.

## Emergent behavior

The cluster can answer questions no single domain can: "which patients have unacknowledged critical results older than 24 hours?", "show every step between this conversation and this prescription", "what fraction of incidental imaging findings became completed follow-up?". That audit-grade traceability across five domains is what separates an EMR platform from a charting app — and it only exists if the joints above are enforced data contracts.

## Tensions to hold

Structured capture improves data quality but slows clinicians; ambient AI restores speed but floods the system with drafts needing review. Closed loops add accountability clicks that AI assistance must absorb, creating dependency between the governance roadmap and the AI roadmap. Ambulatory launch scope keeps colliding with inpatient expectations (BCMA, smart pumps) embedded in enterprise table stakes.

## Recombination opportunities

This cluster's accountability objects recombine with [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md) as safety-performance metrics; its AI-draft plumbing recombines with [Clinical AI And Governance](openchart-feature-list-clinical-ai.md) as the review-queue substrate; its result-routing model extends naturally to [Patient Engagement And Telehealth](openchart-feature-list-patient-engagement.md) result-release rules.

## Open questions

- Does the draft/review state machine live in documentation domain or a shared orchestration layer?
- Which joint ships first as enforceable contract versus advisory convention?
- How much inpatient-pattern capability (barcode administration) enters v1 scope via mobile apps?

## Relationships

Owned by [Overview](openchart-feature-list-overview.md). Cross-cluster: [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md).
