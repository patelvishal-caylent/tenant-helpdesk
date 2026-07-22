# Lab 2 — The Reusable Lookup: stored-proc table map as a slash command
*DBA track*

`⏱ 18 min` · `solo` · `remote`

**What you're proving:** The lookup you retype on every procedure — *what tables does this touch?* — becomes a committed, reusable slash command you can point at anything and trust, because it checks its own answer against the schema.
**Topics:** authoring a reusable slash command from a repeated prompt · verifying AI output against `schema.sql` · judging AI reasoning on a live anomaly (facilitator-led)

**Before you start:** the files in `stored_procedures/` are **T-SQL reference documents** written for a different database engine (this app runs SQLite). You'll **read and reason about them** — never run them. Nothing in this lab executes a stored procedure.

> Work through Claude for the table-map lookups in Steps 1–4. The deliberate human-typed exceptions are the branch ritual in Step 0 and the Claude Code relaunch partway through Step 3.

## Step 0 — Branch and start (off the clock)

If you have uncommitted work from Lab 1 (like your own `CLAUDE.md`), commit or stash it now — otherwise it can conflict with the grounding file already committed on this branch.

```
git fetch origin
git checkout -b lab-l2-work origin/lab-l2-start
```

This branch already has a root `CLAUDE.md` waiting for you — the same grounding file from Lab 1 (yours, if you did that lab; a pre-built copy, if you're joining this track fresh). If Claude Code was already open from Lab 1, quit and restart it now so it actually reads this branch's file — `CLAUDE.md` loads at session start, not mid-session.

No app or browser step is needed here — this lab is file-and-terminal work from start to finish. (There's an optional dashboard check in Extra Credit if you want it.)

## Step 1 — Read the first procedure, ask for its table map (3 min)

1. Open `stored_procedures/usp_GetTenantOrders.sql` in your editor so you can see it.
2. **Ask Claude** to read that file as a reference document — not run it — and list, in two groups, the tables it **reads from** and the tables it **writes to**, one per line.
3. **You should see** something like:
   ```
   Reads from:
     <table>   — <why it's touched>
     <table>   — <why it's touched>

   Writes to:
     (none — if this is a read-only procedure)
   ```
   A read-only `SELECT` procedure should get an explicit "none" under writes, not a skipped section — if this procedure does write somewhere, the table name goes there instead. (This is the shape, not the answer — you'll need your own real output for Step 2.)

## Step 2 — Verify against the schema; write down what you catch (3 min)

1. Open `schema.sql` — this is your ground truth for what tables actually exist, not Claude's answer and not this card.
2. **Ask Claude** to check every table it just named against `schema.sql`, flag anything it listed that isn't a real table there, and flag anything it may have mislabeled (a procedure with no writes shouldn't get a "writes to" entry).
3. **You should see** Claude go table-by-table — something like:
   ```
   schema.sql defines <N> tables: <list>.
   - <table> → confirmed
   - <table> → confirmed
   - <table> → NOT in schema.sql — flagged and dropped.
   Verdict: reads {...}; writes {...}.
   ```
   Yours may come back with nothing flagged — that's a legitimate result, not a failure.
4. **Write a one-line note** — this is your keepable artifact:
   *"Claude said ___; schema says ___; I kept/dropped it because ___."*
   If nothing was wrong, write "no mismatch this time, all tables confirmed." That still counts.

## Step 3 — Package the prompt as a reusable command (4 min)

1. **Ask Claude** to save that same lookup as a reusable slash command at `.claude/commands/sp-table-map.md` — it should take a procedure file path as an argument, list reads vs. writes, and verify the result against `schema.sql` the same way you just did by hand. Give it a one-line `description`.
2. **Quit and relaunch Claude Code** — custom commands only register at launch, so this step is required, not optional.
3. **You should see:** a new file at `.claude/commands/sp-table-map.md`, with a `description:` line up top and the lookup-plus-verify instructions written out in the body.

## Step 4 — Reuse your command on a procedure you haven't touched (4 min)

1. Run your new command against the **second** procedure:
   ```
   /sp-table-map stored_procedures/usp_UpdateTenantStats.sql
   ```
2. **You should see** something like:
   ```
   Reads from:
     <table>
     <table>

   Writes to:
     <table>   — <what kind of write>

   Schema check: every table above confirmed against schema.sql.
   ```
   (This is the shape, not the answer — read your own run closely.)
3. Read the write side yourself, and verify that table against `schema.sql` — the same discipline you used in Step 2. This procedure does write to something; confirm what, and confirm it's real.

### ← THE POINT (Step 4)
The thing you typed by hand on the first procedure just fired as **one command** on a procedure you'd never pointed it at — and it checked its own answer against the schema without you asking it to a second time.

---
**Then (facilitator-led, 2 min, no hands-on):** your facilitator will screenshare, open `monitoring/query-duration-export.csv`, and ask Claude to find the outlier day and explain it. Just watch and judge with the room — did Claude name a specific day, size it against the surrounding baseline (a multiple, not just "high"), and say plainly whether it looks like a duration problem or a volume problem — or bury the answer in prose? Nothing to build here.

---

## Done (self-check + share-back)

You're done when, on your own screen:
- `.claude/commands/sp-table-map.md` exists and has a `description:` line. *(Self-check: `ls .claude/commands/` — run it yourself, or ask Claude to run it for you.)*
- Running `/sp-table-map stored_procedures/usp_UpdateTenantStats.sql` triggers your own command (not a plain-text answer) and prints a two-group read/write map for that procedure, with every table checked against `schema.sql` — not just asserted.
- You have your one-line verification note from Step 2 in hand — even "no mismatch, all confirmed" counts. Nobody leaves this lab empty-handed.

**Share back:** paste (or screenshare) your `sp-table-map.md` command plus your one-line catch note into the room chat. Say what Claude got right or wrong on the first procedure, and whether the second run held up under the same check. Not a git commit, not a token count — the command and the catch are the artifact.

## If you get stuck

| Symptom | Do this |
|---|---|
| Claude tries to "run" the procedure, or errors on T-SQL syntax | Paste: *"Don't run this — read `stored_procedures/usp_GetTenantOrders.sql` as a text reference and just tell me the table names in it."* |
| No `CLAUDE.md` at the repo root after checkout, and you expected one | Confirm you're actually on `lab-l2-work` tracking `origin/lab-l2-start`: `git status`. If it's really missing, `git fetch origin`, then `git checkout lab-l2-start -- CLAUDE.md`. |
| Claude's Step 1/2 answer came back completely clean — nothing to flag | That's a real, valid result. Write "no mismatch this time, all tables confirmed" and move on — verifying and finding nothing wrong is still verifying. |
| `/sp-table-map` doesn't show up, or won't trigger | Confirm the file is at exactly `.claude/commands/sp-table-map.md`, then **quit and relaunch Claude Code** — custom commands only register at launch. Self-check: `ls .claude/commands/` |
| Command runs but the output is empty or garbled | Pass the file path explicitly, and confirm you're in the repo root: `/sp-table-map stored_procedures/usp_UpdateTenantStats.sql` |
| Working copy is a mess | `git checkout .` discards uncommitted edits to tracked files — it won't delete your new, not-yet-committed command file. Do **not** re-run `python seed.py`; L2 doesn't change any data, and reseeding would just reset the database for nothing. |
| Still stuck, time's short | Raise your hand or post in chat — a TA will hand you a working reference command directly so you can still hit every Done criterion. |

## Extra credit (time permitting)

1. **Tie it to the dashboard.** Ask Claude when the dashboard's "Open cases" number could go stale, given that `usp_UpdateTenantStats` is the only thing that writes to that table and nothing in `app.py` calls it automatically. Then open `http://localhost:5050/` (start it with `python app.py` from the repo root if it isn't already running) and find the exact column.
2. **Harden the command.** Add a line to `sp-table-map.md` telling Claude to ignore any table name that appears only in a SQL comment, not the SQL body itself. Re-run on both procedures and confirm your Step 2 catch, if you had one, stays gone.
3. **The dialect question (reasoning only — still don't run anything).** Ask Claude what would have to change to run `usp_UpdateTenantStats` against this app's SQLite database instead of SQL Server.
