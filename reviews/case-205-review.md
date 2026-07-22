# Review — Case 205 summary draft

Reviewed: docs/sample-flawed-draft.md
Against: docs/case-review-requirement.md + schema.sql + CLAUDE.md

## Findings
1. TABLES — FAIL. The draft names "billing_ledger". schema.sql defines exactly six
   tables: tenants, contacts, orders, cases, case_notes, tenant_stats. There is no
   billing_ledger. The nightly rollup the draft describes lives in tenant_stats
   (maintained by usp_UpdateTenantStats). Fix: replace "billing_ledger" with
   "tenant_stats".
2. PRIORITY — FAIL. Requirement #2 says escalated cases must be flagged ESCALATED.
   GET /api/cases/205 returns priority "escalated"; the draft never states it.
   Fix: lead the summary with ESCALATED.
3. GROUNDING — PASS. The rounding-difference root cause is supported by the case note.
4. PHI — PASS. No raw contact email or personal identifier appears in the draft.

## Test plan
- Finding 1: list every table-like identifier in the corrected summary; confirm each
  appears in schema.sql (expect only tenant_stats).
- Finding 2: confirm the string "ESCALATED" appears in the corrected summary.
- Regression: confirm no contact email address appears in the outbound file.
