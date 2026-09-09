# Global Search Configuration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs which DocTypes and fields participate in global search with permission-safe indexing and relevance controls.
Topics: openchart-feature-catalog, platform, frappe, global-search
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-018 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Search quality test suite** — Score approved synthetic queries against expected safe result classes.

## Focus

This feature isolates global-search administration so discoverability improves without broadening record or field access.

## Behavior

- Search administrators select eligible DocTypes, indexed fields, display labels, boosts, aliases, and site scopes.
- Sensitive fields and protected record classes are excluded by policy even when technically searchable.
- Preview runs synthetic queries under selected role profiles and shows ranking plus hidden-result counts.
- Configurations move through Draft, Review, Active, Retired, and Superseded states.
- Reindexing runs in the background with progress, failure, and last-success evidence; the prior index stays available until cutover.
- Every result is rechecked against current DocType, row, and field permissions before display.

## Frappe realization

- **DocTypes:** `OC Search Profile` stores DocType, field rows, aliases, boosts, scope, version, and state; `OC Search Reindex Run` stores progress.
- **Surface:** a Desk configuration page wraps Frappe global search settings with role simulation and relevance preview.
- **Automation:** publication enqueues an RQ reindex job; realtime events update progress and atomically activate the completed profile.
- **API:** guarded search methods apply Frappe permission queries and minimum-necessary snippets at read time.

## Boundaries

Owns: search participation, ranking configuration, and reindex evidence. Consumes: DocType metadata and permissions. Emits: active search profile and permission-filtered results. Does not own: source records or external search engines.

## Open questions

- Should indexing retain prior field values long enough to support zero-downtime cutover?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Team-shared Saved Filters](openchart-feature-catalog-plt-019-team-shared-saved-filters.md)
