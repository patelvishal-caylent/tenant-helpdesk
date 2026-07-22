# Lab 1 — Ground & Verify: catch the hallucination with CLAUDE.md
*Shared foundation lab — every track starts here*

`⏱ 15 min` · `solo` · `remote`

**New to this?** Read `GETTING-STARTED.md` first if you haven't already -- it covers opening a terminal, starting Claude Code, and switching branches step by step.

**What you're proving:** Grounding Claude in your own codebase narrows the gap between what it says and what's true — but it never closes it, so you still verify.
**Topics:** CLAUDE.md grounding & context authoring · verifying AI output against ground truth · reading a T-SQL file as reference documentation, not executing it

**Before you start:** the files in `stored_procedures/` are **T-SQL reference documents** written for a different database engine. You'll **read and reason about them** — never run them. Nothing in this lab executes a stored procedure.

> Work through Claude for the file-reading question in Steps 1 and 3. The deliberate human-typed exceptions are the branch ritual in Step 0 and authoring `CLAUDE.md` yourself in Step 2.

## Step 0 — Branch and start (off the clock)

```
git fetch origin
git checkout -b lab-l1-work origin/lab-l1-start
```

This branch has **no root `CLAUDE.md`** — that absence is the point, and you'll feel why in Step 1.

In your already-activated virtual environment, from the repo root, bring the app up once for the whole session:
```
python seed.py
python app.py
```
Leave `app.py` running in its own terminal on `http://localhost:5050`, and open Claude Code in a second terminal at the repo root. **Do not re-run `seed.py`** later — it wipes and rebuilds the database.

**Tip:** you can ask Claude Code to run these two commands for you instead of typing them into a separate terminal.

## Step 1 — Ask cold, and write down what you can't confirm (4 min)

1. In Claude Code, confirm there is **no `CLAUDE.md`** in this repo yet.
2. **Ask Claude** to read `stored_procedures/usp_UpdateTenantStats.sql` and tell you which tables it reads from, which it writes to, and how the tenant-stats numbers shown on the dashboard stay accurate.
3. **You should see** something like:
   ```
   Reads:   <one or more tables, each with a short reason>
   Writes:  <one or more tables, each with a short reason>

   <a paragraph on when/how the procedure runs, and whether anything keeps
    the written table's numbers in sync with live activity>
   ```
   Your answer's specific tables and claims are the point of this exercise — read the whole thing, not just the table list.
4. On paper or in a scratch note, start a two-column list titled **Ungrounded** / **Grounded**. Under **Ungrounded**, write down every table name and every "how it stays in sync" claim in Claude's answer that you **cannot personally confirm** from a file you've actually read.

## Step 2 — Ground it in five lines (4 min)

1. Create a file named `CLAUDE.md` at the repo root — you're writing this one yourself, not asking Claude to draft it.
2. In about five lines, state: this is a Flask + SQLite app; `schema.sql` is the source of truth for tables and columns; name the six tables; note that `tenant_stats` is a denormalized rollup that is **not** kept live (only `seed.py` and the stored procedure set it, so it can be stale); note that `stored_procedures/*.sql` are T-SQL reference files that are **not executed**; and that all data is synthetic.
3. **You should see** a short file (roughly five lines) at the repo root when you run `ls`.

Stuck on the wording? See "If you get stuck" below for a reference version you can pull in without derailing the exercise.

## Step 3 — Re-ask the exact same question, then compare (4 min)

1. **Relaunch Claude Code** (quit and restart it in the repo) so it picks up your new `CLAUDE.md`.
2. **Ask Claude** the **byte-for-byte identical** question from Step 1 — same file, same three questions (reads, writes, how the dashboard stays accurate).
3. **You should see** something like:
   ```
   Per CLAUDE.md and schema.sql:

   Reads:   <tables, ideally now citing schema.sql>
   Writes:  <tables, ideally now citing schema.sql>

   <a paragraph on whether anything keeps the written table's numbers in sync —
    ideally grounded in what CLAUDE.md and schema.sql actually say, rather than assumed>
   ```
   Compare this line by line against your Step 1 answer.
4. Fill your **Grounded** column: for each item in your Ungrounded column, did the new answer cite `schema.sql`/`CLAUDE.md`, drop the claim, or correctly say the stats can be stale? **Circle** anything the grounded answer still asserts that you'd want to verify yourself.

### ← THE POINT (Step 3)
Grounding narrowed the answer — but you still had to check it against `schema.sql` to be sure. That's the whole point: **it narrows the gap between what Claude says and what's true. It doesn't close it.**

## Done (self-check + share-back)

You're done when, on your own screen:
- `CLAUDE.md` exists at the repo root (`ls` shows it — roughly 5 lines).
- Your two-column **Ungrounded / Grounded** list has at least one entry that moved — or at least one entry you're consciously still choosing to verify yourself. Either counts.
- Your Step 3 answer, checked against `schema.sql` itself, correctly scopes which tables the procedure reads from and writes to, and matches what `CLAUDE.md` says about whether those numbers stay live.

**Share back:** show the room (screenshare or paste into chat) your two-column before/after list plus your `CLAUDE.md` — the specific claim *you personally caught* moving from unconfirmed to grounded (or the one you're still not taking on faith).

## If you get stuck

| Symptom | Do this |
|---|---|
| Claude nailed it cold — nothing landed in your Ungrounded column | Ask directly: "does `app.py` call this procedure anywhere?" or "is there anything keeping this live between runs?" Still clean? Write down "grounding already tight — verified against `schema.sql` anyway." That's a valid outcome. |
| Running low on time / can't finish the `CLAUDE.md` | `git fetch origin`, then `git checkout origin/lab-l1-solution -- CLAUDE.md` to pull in a reference version. Continue at Step 3. |
| Step 3's answer reads just like Step 1's | Make sure you fully **relaunched** Claude Code before re-asking — quit and restart it. `CLAUDE.md` loads at session start, not mid-session. |
| `python app.py` says no database found | Run `python seed.py` once, then `python app.py`. Don't re-run `seed.py` if it already succeeded. |
| Port 5050 is busy | Edit the `app.run(..., port=5050)` line in `app.py`, or stop the conflicting process. (Not required for Steps 1–3 anyway.) |
| Something else entirely / still stuck | Post in chat — a TA will get you unblocked without spoiling the exercise for anyone else. |

## Extra credit (time permitting)

1. **See the staleness on the actual dashboard.** Open `http://localhost:5050/` and note a tenant's `open_case_count`. **Ask Claude:** given what `CLAUDE.md` says about `tenant_stats`, describe a sequence of API calls after which this dashboard number would be wrong, and how you'd detect it.
2. **The dialect question.** **Ask Claude:** this procedure is T-SQL but the app runs SQLite — what would you have to change to express this logic against the app's actual database, and why can't it run as written? Reasoning only — don't try to run anything.
3. **Harden your CLAUDE.md.** Add one line telling Claude to always cite `schema.sql` when asked a schema question. Re-ask and see whether the citation becomes consistent.
