# Tenant Helpdesk

A small, entirely fictional multi-tenant support/ops app, built as a hands-on lab
repo for a Claude Code training exercise. No real company's data, schema, or
systems are represented here — every tenant, contact, case, and order below is
made up.

## What this is

This is a support portal for a fictional multi-tenant SaaS product. It tracks:

- **Tenants** — customer accounts, each with a size tier (small/medium/large) and
  a cluster type
- **Contacts** — people at each tenant
- **Orders** — billing/order records per tenant
- **Cases** — support tickets, with notes
- **Tenant stats** — a rollup table (open case count, order count), recomputed
  periodically, not live

It's deliberately small and has a few rough edges on purpose — an undocumented
schema, a couple of "stored procedures" worth reading and reasoning about, and a
monitoring export with a planted anomaly. Those rough edges are the point: they're
what the exercises in `labs/` are built around.

## Running it locally

No external services, no credentials, no cloud dependencies. Requires Python 3
only.

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py                 # creates and populates tenant_helpdesk.sqlite3
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
labs/                                # hands-on lab instructions (start here if
                                     # you're doing a lab, not just reading this)
```

## First time doing one of these labs? Start here.

You've likely already done the async "Claude Code in Action" course. This part
is the mechanical piece: exactly what to click and type, assuming none of it yet.

1. **Open a terminal.** Mac: `Cmd+Space`, type `Terminal`, Enter. Windows: Start
   menu, type `Windows Terminal` or `PowerShell`, Enter. You'll type commands
   here instead of clicking icons.
2. **Get into this folder.** Type `cd ` (note the trailing space), then drag this
   project's folder from Finder/File Explorer onto the terminal window — the
   path fills in automatically. Press Enter. Confirm with `ls`: you should see
   `README.md`, `app.py`, `labs/`.
3. **Start Claude Code.** Type `claude`, press Enter. A welcome screen followed
   by an input box means you're ready. To stop it: **Ctrl-C**. Several labs ask
   you to quit and restart Claude Code partway through — that's how it picks up
   a changed file, like a new `CLAUDE.md`.
4. **Prompts are plain English.** Type a request the way you'd ask a coworker,
   press Enter. Claude reads the real files in this folder and answers from
   what's actually there — not a guess.
5. **What comes back:** a **diff** (a before/after of just the changed lines), a
   plain question, or a **permission prompt** before it writes or runs anything
   — e.g. "Do you want to make this edit? Yes / Yes, don't ask again / No." This
   is normal, every lab, every time. Answering **Yes** is expected and safe.
6. **Branches are starting kits.** Each lab's "Step 0" gives you two commands
   like:
   ```
   git fetch origin
   git checkout -b lab-l1-work origin/lab-l1-start
   ```
   This pulls down that lab's exact starting files onto a new local copy —
   nothing from an earlier lab carries over unless you deliberately kept it. Use
   the exact names printed on *your* lab's own Step 0, not this example. If
   Claude Code was already running, `Ctrl-C` and restart it (`claude`) after
   switching branches — it won't notice the new branch on its own.
7. **Stuck?** Say so immediately, out loud or in chat. Check your lab card's own
   "If you get stuck" table first — most issues are already answered there by
   symptom. Not listed, or the fix doesn't work? Ask a TA. Asking early is
   expected, not falling behind.

## Note for anyone building labs against this repo

This repo is the `lab_repo` input for the `lab-generation` skill. It's meant to be
mutated — new branches, new files, whatever a given lab needs. The one rule: keep
everything synthetic. Don't let real data of any kind creep in on any branch.
