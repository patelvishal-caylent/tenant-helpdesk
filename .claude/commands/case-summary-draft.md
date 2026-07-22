---
description: Quick draft summary of a case for the review pipeline.
model: claude-sonnet-5
---
Draft a quick review summary of case $1. Use the case-review approach, the case's
API data (GET /api/cases/$1), and read stored_procedures/usp_UpdateTenantStats.sql
to reason about how the rollup is maintained (read it — do not run it). Keep it to
a short paragraph. This is a fast first pass; a separate review pass will check it.

Write this draft to docs/case-205-draft.md (create it, or overwrite it if
present) so the review pass can read it back from disk even after a /clear or
relaunch.
