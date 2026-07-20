# TenantDB

A small, entirely fictional multi-tenant support/ops app, built as a hands-on lab
repo for a Claude Code best-practices workshop. No real company's data, schema,
or systems are represented here — every tenant, contact, case, and order below is
made up.

## What this is

TenantDB is a support portal for a fictional multi-tenant SaaS product. It tracks:

- **Tenants** — customer accounts, each with a size tier (small/medium/large) and
  a cluster type
- **Contacts** — people at each tenant
- **Orders** — billing/order records per tenant
- **Cases** — support tickets, with notes
- **Tenant stats** — a rollup table (open case count, order count) recomputed by
  a nightly job

It's deliberately small and has a few rough edges on purpose — an undocumented
schema, a couple of "stored procedures" worth reading and reasoning about, and a
monitoring export with a planted anomaly. Those rough edges are the point: they're
what the workshop's exercises are built around.

## Running it locally

No external services, no credentials, no cloud dependencies. Requires Python 3
only.

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py                 # creates and populates tenantdb.sqlite3
python app.py                  # starts on http://localhost:5050
```

Re-run `python seed.py` any time to reset the data back to its original state.

## Layout

```
app.py                              # Flask app: dashboard, case views, JSON API
schema.sql                          # SQLite schema
seed.py                             # populates synthetic seed data
templates/                          # server-rendered HTML views
stored_procedures/                  # T-SQL-style reference files (not executed —
                                     # written for reading/reasoning exercises)
monitoring/query-duration-export.csv  # sample monitoring export, one planted outlier
```

## Note for anyone building labs against this repo

This repo is the `lab_repo` input for the `lab-generation` skill. It's meant to be
mutated — new branches, new files, whatever a given lab needs. The one rule: keep
everything synthetic. Don't let real data of any kind creep in on any branch.
