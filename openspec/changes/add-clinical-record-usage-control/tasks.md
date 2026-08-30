## 1. Owner Ratification And Single Speckit Handoff

- [ ] 1.1 Obtain the owner's unconditional ratification of this exact change revision and durably record the owner, unconditional decision, change name and revision or digest, and time; OpenSpec validity alone is not ratification.
- [ ] 1.2 Only after the durable ratification record exists, create exactly one Speckit feature named `clinical-record-usage-control` from the clean base checkout; do not split either capability delta into another feature.
- [ ] 1.3 Record immutable two-way links between this change and the generated `specs/NNN-clinical-record-usage-control` feature, then carry every requirement and scenario from both delta specs into its specification and traceability model without duplicating an executable task list in OpenSpec.

## 2. Separate Constitution Gate And Speckit Definition

- [ ] 2.1 Adopt the repository constitution through its separate project-governance process before the feature plan phase; do not make constitution adoption or amendment a deliverable inside the Speckit feature.
- [ ] 2.2 Complete feature clarification and checklist work, then record a meaningful Constitution Check against the adopted constitution's actual security, privacy, portability, atomicity, test, and governance constraints as a prerequisite to advancing the feature plan; do not use a boilerplate pass.
- [ ] 2.3 Complete the linked feature's plan, tasks, and analyze stages, resolving all contract, migration, failure-semantics, security, privacy, neutral-envelope, and standalone-conformance details within this proposal and design.

## 3. Speckit Delivery

- [ ] 3.1 Implement only through the linked Speckit feature, preserving portable authority and policy adapters with no direct Medx dependency and the provider-evidence → governed-verifier appraisal → KMS-enforced-release ownership chain.
- [ ] 3.2 Select and version-pin exactly one neutral public-envelope profile; verify exact conformance, no openChart public superset, no stable correlatable public identifiers, and owner-local outbox and receipt association.
- [ ] 3.3 Produce requirement-to-test evidence for atomic local decision/event/mutation behavior, idempotent external outbox effects, indeterminate reconciliation without false success, allowed and refused attempts, leases and exercises, break-glass review, TEE/KMS binding failures, bounded-output rejection, scoped deletion language, `anchor_pending`, and public-PHI exclusion.

## 4. Acceptance And Governance Closure

- [ ] 4.1 Verify the repository's full validation tiers pass, including standalone operation with no Medx application installed and compatibility coverage for the breaking protected-client migration.
- [ ] 4.2 Publish the supported versioned contracts, activation and rollback guidance, residual-security claims, atomic and indeterminate failure semantics, and owner-local/public evidence boundary from the linked feature.
- [ ] 4.3 Record durable acceptance against both delta specs and archive this OpenSpec change only after the single linked feature's implementation is merged into its intended base and all required validation has passed.
