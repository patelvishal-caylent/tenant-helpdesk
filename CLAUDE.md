# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A small, entirely fictional multi-tenant support/ops app ("Tenant Helpdesk"), built as a
hands-on lab repo for a Claude Code best-practices workshop. No real company's data, schema,
or systems are represented — every tenant, contact, case, and order is synthetic.

This repo is also the `lab_repo` input for the `lab-generation` skill: it's meant to be
mutated (new branches, new files) for whatever a given lab needs. The one rule: keep
everything synthetic — don't let real data of any kind creep in on any branch.

It's deliberately small and has a few rough edges on purpose — an undocumented schema (from
the app's perspective, before this file existed), a couple of "stored procedures" worth
reading and reasoning about, and a monitoring export with a planted anomaly. Those rough
edges are what the workshop's exercises (`labs/`) are built around.

## Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python seed.py                 # creates/resets workshop_demo.sqlite3 from schema.sql
python app.py                  # runs Flask dev server on http://localhost:5050
```

Re-run `python seed.py` any time to reset the data back to its original synthetic state
(it drops and rebuilds `workshop_demo.sqlite3`). There is no test suite, linter, or build
step — just the Flask app and the seed script.

## Architecture

- `app.py` — Flask app with two kinds of routes: server-rendered pages (`/`, `/tenants/<id>`,
  `/cases`, `/cases/<id>`) using templates in `templates/`, and a read-only JSON API
  (`/api/tenants`, `/api/tenants/<id>/orders`, `/api/cases`, `/api/cases/<id>`) intended for
  skills/scripts to query against. Each request gets its own SQLite connection via Flask's
  `g` object (`get_db()`), opened lazily and closed in `teardown_appcontext`.
- `schema.sql` — source of truth for the SQLite schema, executed by `seed.py` via
  `executescript`. `app.py` never modifies the schema at runtime.
- `seed.py` — drops and rebuilds `workshop_demo.sqlite3` from `schema.sql`, then inserts
  fixed synthetic rows (tenants, contacts, orders, cases, case_notes) and computes the
  `tenant_stats` rollup (open case count, order count per tenant) in plain Python/SQL
  (~lines 66-76). This rollup logic is the live equivalent of `usp_UpdateTenantStats` below.
- `stored_procedures/*.sql` — T-SQL-style **reference-only** artifacts for reasoning
  exercises. They are never executed against the app's SQLite database — `app.py` doesn't
  call them, and there's no SQL Server anywhere in this stack. Treat them as read-and-reason
  material, not runnable code.
- `monitoring/query-duration-export.csv` — a sample monitoring export with one planted
  outlier, used by workshop exercises.
- `labs/` — the workshop's lab instructions (`GETTING-STARTED.md`, `LAB-1.md` through
  `LAB-3.md`, `CAPSTONE.md`). These describe exercises to run *against* this repo; they are
  not code.
- `demo-materials/` — facilitator-only staging files for a live "no grounding vs. grounding"
  demo (copying an alternate `CLAUDE.md` into place mid-demo). Not auto-loaded, not part of
  the app.

# Schema shape (synthetic support/ops system)
Each tenant has contacts, orders, and cases.
Case notes live in case_notes; rollups in tenant_stats.
Known tables: tenants, contacts, orders,
  cases, case_notes, tenant_stats.
If a table is not listed here, say you don't know.
Full schema source: schema.sql (SQLite; loaded by seed.py).

# Stored procedures (stored_procedures/)
These are reference-only T-SQL artifacts for reasoning exercises.
They are NOT executed against the app's live SQLite database
(workshop_demo.sqlite3) — app.py never calls them. The equivalent
stats-rollup logic that actually runs live is plain Python/SQL in
seed.py (~lines 66-76).
- usp_UpdateTenantStats(@TenantId): reads cases (open count) and
  orders (order count) for the tenant, then upserts into
  tenant_stats (UPDATE, falling back to INSERT if no row exists).
- usp_GetTenantOrders(@TenantId): read-only SELECT joining orders,
  tenants, and contacts (primary contact) for a tenant.