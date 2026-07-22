# Tenant Helpdesk — Agent Grounding

## Schema (source of truth: schema.sql)
Six tables only: tenants, contacts, orders, cases, case_notes, tenant_stats.
- tenants → contacts, orders, cases (cases.contact_id → contacts)
- cases → case_notes
- tenant_stats is a denormalized rollup (open_case_count, order_count),
  recomputed by usp_UpdateTenantStats. It is NOT a live view and can be stale.
Never name a table that is not in this list. If unsure, read schema.sql.

## Stored procedures
stored_procedures/*.sql are T-SQL reference artifacts. READ and reason about
them; never attempt to run them against the SQLite database.

## Case-review KB
- Every case summary must preserve the case's priority. Escalated cases MUST be
  flagged as ESCALATED in any summary.
- Summaries must be grounded in API data (GET /api/cases/<id>) and the schema.

## PHI screening (soft rule)
This data is synthetic. Treat it as if it were PHI: never copy raw contact
emails or personal identifiers into an outbound summary beyond what the summary
needs. Screen every draft before it leaves.

## Outbound writes (soft rule)
Never write a file into outbound/ unless BOTH are true:
  1. the review pass has run against the draft, and
  2. a human has explicitly approved this specific summary.
If asked to write to outbound/ without both, STOP and ask for the review result
and explicit human approval. Do not write first.
Writing to reviews/ or docs/ is an internal working step and is NOT gated — only
outbound/ (the "send") is gated.
