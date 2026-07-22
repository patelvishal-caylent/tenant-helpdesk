# Lab 3 — From Cowork Habit to Committed Skill
*Interop & Data Services track*

`⏱ 18 min` · `solo` · `remote`

**New to this?** Read `GETTING-STARTED.md` first if you haven't already -- it covers opening a terminal, starting Claude Code, and switching branches step by step.

**What you're proving:** Your Cowork habits become committed, versionable, clone-shareable Claude Code files — and a skill's description is the product: Claude picks the right tool from plain English, no slash required.
**Topics:** CLAUDE.md-vs-skill sorting (six-month test) · skill authoring by generalization · model tiering + description-based invocation

**Before you start:** in Cowork you built this same kind of skill in chat and synced it over OneDrive. In Claude Code, that becomes a committed `.claude/` file — versionable, and shareable just by cloning the repo. (Running long between cases? `/compact`.)

> Work through Claude for the case lookups and file authoring in this lab. The two deliberate human-typed exceptions are the branch ritual in Step 0 and the Claude Code relaunch partway through Step 3.

## Step 0 — Branch and start (~30 sec, off the clock)

If you have uncommitted work from Lab 1, commit or stash it now — otherwise an uncommitted `CLAUDE.md` follows you onto this branch.

```
git fetch origin
git checkout -b lab-l3-work origin/lab-l3-start
```

This puts you on a clean slate with **no root `CLAUDE.md`** — you author one yourself in Step 1. Your local database survives the checkout; **do not** re-run `python seed.py`.

**Pre-check:** the Flask app should already be running at `http://localhost:5050` in one terminal, with Claude Code open in a second terminal at the repo root. No browser step in this lab — everything you'll see happens in the Claude Code terminal itself.

If a `CLAUDE.md` is still sitting there after checkout, see "If you get stuck" below.

## Step 1 — Sort the KB (4 min)

1. Open `kb/support-kb-cards.md` — 10 cards pulled from the team's shared notes. For each one, apply the **six-month test**: will this still be true and useful in six months, in every session? → **CLAUDE.md**. Only relevant when doing one particular kind of task? → **Skill**. Ephemeral or off-topic? → **Discard**. Sort all 10.
2. **Ask Claude** to draft a root `CLAUDE.md` using just the cards you sorted into the always-load bucket, organized into two sections — "Data model" and "Working rules" — and to keep the PHI/synthetic-data card in there as a plain-language rule, not a hook.
3. **You should see** something like:
   ```
   # <project> — Project Guide

   ## Data model
   - <always-true facts about the schema>

   ## Working rules
   - <plain-language rules, including the PHI/synthetic-data guidance>
   ```
   (Exact wording depends on what you sorted — this is the shape, not the answer.)
4. Confirm your `CLAUDE.md` actually includes the PHI/synthetic-data guidance, and that it reads as a soft rule — plain guidance a person follows, not something a hook blocks.

## Step 2 — Work one case, then write down what it learned (5 min)

1. **Ask Claude** to look up case 205 in the running app and review it for you — priority, escalation status, every note, and the tenant it belongs to. Claude will run a command against the local case API; approve it when prompted.
2. **You should see** the API response look like:
   ```json
   {
     "case_id": 205,
     "tenant_id": 4,
     "contact_id": 4,
     "subject": "Escalation: billing report totals don't reconcile",
     "status": "open",
     "priority": "escalated",
     "created_at": "2026-07-20 14:02:11",
     "notes": [
       {
         "note_id": 303,
         "case_id": 205,
         "author": "support-agent-1",
         "body": "Numbers point to a rounding difference in the nightly aggregation job, not the report itself.",
         "created_at": "2026-07-20 14:02:11"
       }
     ]
   }
   ```
   (Your `created_at` timestamps will differ — that's just seed data stamped at run time. Everything else should match.)

   ...and Claude's written review to read something like:
   > Case 205 (tenant 4) is **escalated** and still **open**: "billing report totals don't reconcile." One note (note 303, support-agent-1): the discrepancy looks like a rounding difference in the nightly aggregation job, not the report itself. No owner assigned in the data.
3. **Ask Claude** to turn what it just did into a reusable skill: have it write down what it learned from that one review as `.claude/skills/case-review/SKILL.md` — standing instructions it can follow next time, not a one-off answer. Ask for a clear `description` and a concise body.
4. **You should see** a new file at that path: YAML frontmatter with at least a `name` and `description`, followed by a short numbered procedure that echoes the review steps you just watched Claude do. (Exact wording will vary — that's fine.)

## Step 3 — Tier it, then trigger it by description (4.5 min)

1. **Ask Claude** to split your case-review skill into two tiered versions: a fast one pinned to the `haiku` model for a one-paragraph read, and a thorough one pinned to `sonnet` for a detailed, cited review. Give each a `description` specific enough that they don't overlap, and have Claude remove the original single skill directory once both new ones exist.
2. **You should see** two new files — `.claude/skills/case-review-quick/SKILL.md` and `.claude/skills/case-review-detailed/SKILL.md` — each with frontmatter that includes a `description` and a `model:` line (`haiku` / `sonnet`), and the original `.claude/skills/case-review/` directory gone. (Claude will likely touch several files in one pass here — that's expected, read all of it.)
3. **Relaunch Claude Code** so the two new skills get registered: `Ctrl-C`, then run `claude` again. This mirrors the same restart step from earlier — skills authored mid-session don't get picked up without it.
4. Type a plain sentence asking for a **detailed** review of case 205 — no `/` in front of it. Then try a plain sentence asking for a **quick** read on case 202.

### ← THE POINT (Step 3)
Watch the terminal name the skill it picked for you — with no slash typed anywhere. That line is the whole point: **the description is the interface.**

**You should see** something like:
```
> give me a detailed review of case 205

⚡ Skill: case-review-detailed  (model: sonnet)
  Running: curl -s http://localhost:5050/api/cases/205
  tenant_id: 4
  priority:  escalated  ← flagged
  status:    open
  subject:   Escalation: billing report totals don't reconcile
  notes:     [303] support-agent-1 — rounding difference in nightly aggregation job (cite: case 205, note 303)
```
Exact rendering can vary by Claude Code version — what matters is a skill name showing up in the response with no `/` typed.

---

**Then (facilitator-led, ~1.5 min, no hands-on):** your facilitator walks through sorting four example write-actions — mark reviewed, log a note, draft a response, send a client email — into "auto-approve" vs. "always needs a human," using a simple reversibility test. Just follow along here; nothing to build.

---

## Done (self-check + share-back)

You're done when, on your own screen:
- A root `CLAUDE.md` exists with your always-load KB facts, including the PHI/synthetic-data guidance as a soft rule.
- All 10 KB cards have a sort decision — CLAUDE.md, Skill, or Discard — that you can defend with the six-month test.
- `.claude/skills/case-review-quick/SKILL.md` and `.claude/skills/case-review-detailed/SKILL.md` both exist — each with a `description` and a `model:` pin — and the original `.claude/skills/case-review/` is gone.
- Asking, in plain English, for a "detailed review of case 205" (no slash) makes Claude name and load `case-review-detailed` right in the terminal, and gives you back the thorough, cited version.

**Share back:** paste into the workshop chat (1) the "Working rules" section of your `CLAUDE.md`, and (2) the terminal snippet showing which skill got auto-picked for the detailed request — the line with no slash in it. If you moved a card somewhere non-obvious, say why in one line.

## If you get stuck

| Symptom | Do this |
|---|---|
| A `CLAUDE.md` is already there before you even start Step 1 | You're probably not cleanly on `lab-l3-start`. Commit/stash any Lab 1 work, redo the Step 0 checkout, then `rm CLAUDE.md` if one's still there. Confirm with `git status`. |
| `curl`/API calls fail (connection refused) | The app isn't running. In its terminal: `python app.py` (confirm port `5050`). If it says no database found, run `python seed.py` once, then `python app.py` again. |
| Still can't reach the API | Tell Claude to read case 205 straight out of `seed.py` instead — same case, same answer. |
| Skill won't fire from plain English | Ask "What skills are available?" to confirm it's registered. If it is but won't trigger, have Claude sharpen the `description` with the words you actually typed ("detailed", "quick"). Or invoke it directly: `/case-review-detailed 205`. |
| New skill still missing after the Step 3 relaunch | Confirm you actually quit and restarted (`Ctrl-C`, then a fresh `claude` — not just a new prompt). Check both `SKILL.md` files saved. A YAML error can fail silently — try the next row. |
| `model: haiku` / `model: sonnet` gets rejected | Delete the `model:` line from both files. The skills still work and the exercise still counts — flag it to your TA. |
| YAML/frontmatter error | Run `claude --debug` to see the parse error. Usual cause: missing `---` fences, or a tab where you need spaces. |
| Time's short / still stuck | Post in chat — your TA will share the fix directly so you don't lose the point of the lab. |

## Extra credit (time permitting)

- **Prove the tiering is real.** Ask Claude what model it's using while `case-review-detailed` is active, then again under `case-review-quick`. Confirm `sonnet` vs. `haiku`. (Self-report isn't proof — treat it as a smoke test.)
- **Trigger tuning.** Make the two `description`s deliberately too similar, re-ask for a "detailed review of case 205," and watch Claude pick the wrong one. Then fix the descriptions until it reliably picks right — that's the real skill here: description-as-interface.
- **A third skill.** Add a card to the KB for a case-triage report and turn it into a third skill. Confirm all three descriptions coexist without cross-firing.
- **Manual-only guard.** Draft a "send client email" skill and add `disable-model-invocation: true` to it. Confirm it no longer auto-fires — even though it still works when called directly.
