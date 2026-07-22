# CLAUDE.md — Workshop Demo App

- This is a Flask + SQLite multi-tenant support/ops app. `schema.sql` is the source of truth for every table and column — read it before answering any schema question.
- Tables: tenants, contacts, orders, cases, case_notes, tenant_stats. `tenant_stats` is a denormalized rollup (open_case_count, order_count); it is NOT kept live — only `seed.py` and `usp_UpdateTenantStats` set it, so dashboard numbers can be stale. There is no trigger.
- `stored_procedures/*.sql` are T-SQL reference artifacts for reading/reasoning only. They are NOT executed against this SQLite database.
- All data in this repo is entirely synthetic. Never introduce real data on any branch.
