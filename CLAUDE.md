# Tenant Helpdesk — Project Guide

## Data model
- tenants have many contacts, orders, and cases; case_notes belong to a case.
- tenant_stats is a per-tenant denormalized rollup (open_case_count, order_count). It is NOT live: it is only recomputed by usp_UpdateTenantStats, so dashboard numbers can be stale after a case resolves or an order lands.

## Working rules
- Stored procedures in stored_procedures/ are T-SQL reference artifacts. The app runs SQLite. Read and reason about them; never run them.
- All tenant, contact, and case data in this repo is synthetic. Never introduce real patient or client PHI. Screen any client-facing text you draft for PHI before it leaves the repo. (Soft rule — reviewed by a human, not enforced by tooling.)
