# In-app Patch Notes — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents version-targeted release notes, administrator actions, and acknowledged impacts inside each upgraded site.
Topics: openchart-feature-catalog, platform, frappe, patch-notes
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-029 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Role-specific change digest** — Summarize only changes relevant to a user's permitted workflows.

## Focus

This feature isolates trustworthy release communication tied to installed versions and executed patches.

## Behavior

- Release managers publish a version, channel, audience, summary, detailed changes, known issues, and required administrator actions.
- Notes distinguish new capability, behavior change, deprecation, security update, migration, and resolved defect.
- Sites receive only notes compatible with their installed app and patch level.
- Critical administrator actions require acknowledgment with actor and timestamp; ordinary notes may be dismissed per version.
- Failed or rolled-back upgrades do not present the target release as installed.
- Links may reference approved local help content or external HTTPS documentation and are validated before publication.

## Frappe realization

- **DocTypes:** `OC Release Note` stores app, version, channel, audience roles, content, action severity, and state; `OC Release Note Acknowledgment` records per-user/site evidence.
- **Hooks:** post-migrate patches update installed release metadata; login boot info returns unread compatible notes.
- **Surface:** Desk release drawer and administrator workspace group notes by installed version and required action.
- **Permissions:** Release Manager publishes; users can acknowledge only their own notices; administrators report site-level completion.

## Boundaries

Owns: version-targeted in-app release communication and acknowledgments. Consumes: installed app and patch state. Emits: notices and action evidence. Does not own: code release, upgrade execution, or support case resolution.

## Open questions

- Which security notes should remain intentionally nonspecific until fleet patch adoption reaches a threshold?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Upgrade Channel And Preflight Manager](openchart-feature-catalog-plt-028-upgrade-channel-and-preflight-manager.md) · [In-app Release Tour Publisher](openchart-feature-catalog-plt-048-in-app-release-tour-publisher.md)
