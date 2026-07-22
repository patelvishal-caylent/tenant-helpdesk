# Support KB — dump for sorting

Ten cards pulled from the team's shared notes. Sort each into:
- **CLAUDE.md** — always true, useful in every session (six-month test)
- **Skill** — only useful when doing one specific kind of task
- **Discard** — ephemeral, off-topic, or already expired

All data below is synthetic.

1. Data model: tenants have many contacts, orders, and cases; case_notes belong to a case. tenant_stats is a per-tenant rollup (open_case_count, order_count).
2. tenant_stats is NOT live — it is only recomputed by usp_UpdateTenantStats (nightly, or ad hoc). Dashboard counts can be stale right after a case resolves or an order lands.
3. Stored procedures in stored_procedures/ are T-SQL reference artifacts. The app runs SQLite. Read and reason about them; never run them.
4. All tenant, contact, and case data here is synthetic. Never introduce real patient or client PHI. Screen any client-facing text you draft for PHI before it leaves the repo.
5. Case-review checklist: confirm the priority, check whether the case is escalated, read every note, name the tenant and primary contact, and flag anything unresolved.
6. Duration-anomaly procedure: to chase a slow query, open monitoring/query-duration-export.csv, find the day that deviates from the 41-47ms baseline, and tie it back to the stored procedure named in the file.
7. Escalation triage format: an escalated-case report leads with tenant name, then subject, then the latest note, then an owner.
8. Q3 all-hands moved to Thursday at 10am — bring your laptop.
9. Sticky note: ask Marco whether the deck accent color should match the new brand green.
10. Heads-up: staging DB was down the morning of 7/12, so ignore that day's numbers when comparing.
