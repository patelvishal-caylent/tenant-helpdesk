<!--
Capstone card — "The Two-Pass Review Pipeline." Lives at labs/CAPSTONE.md.
Three cohort tracks share this one card: Interop (full loop, hands-on),
SysOps / NetSuite-scripting (review -> verify, hands-on; spec/plan/implement
provided), DBA (guided walkthrough + take-home). Satisfies lab-card-contract.md
C1-C10 + CAP1-CAP2. Source design: lab-build/20-capstone-design.md.
-->

# Capstone — The Two-Pass Review Pipeline

`⏱ 15 min` · `solo`

**New to this?** Read `GETTING-STARTED.md` first if you haven't already -- it covers opening a terminal, starting Claude Code, and switching branches step by step.

**What you're proving:** splitting one confident pass into a cheap drafter plus a skeptical reviewer — writing the review down and gating the send on a human — is the multi-agent win, and you get it with two prompts, not a subagent framework.

**This lab covers three things:**
1. Splitting a draft pass from a separate, skeptical review pass — two invocations, not one.
2. Reviewing against a written source of truth (a requirement doc + the schema), and writing the findings plus a test plan down — not just saying them out loud.
3. Gating a send behind a soft CLAUDE.md rule and an explicit human approval — not a hook.

The full loop is **spec → plan → implement → review → verify**, expressed as committed `.claude/` commands you can re-run, version, and share by clone — not one long chat. The three tracks below run different slices of it; find yours after setup.

## 0 — Branch and start
```
git fetch origin
git checkout -b lab-capstone-work origin/lab-capstone-start
```
Relaunch Claude Code after checkout — it needs the relaunch to pick up the `CLAUDE.md` and pre-baked `.claude/` commands that ship on this branch. Confirm the app is running at `http://localhost:5050` (start it with `python app.py` if it isn't).

Everything you need is already on the branch — grounding rules, the case-review skill, all pipeline commands, the spec template, the requirement doc, and a sample draft. You don't need to have finished any earlier lab to start this one.

All artifacts in this lab stay local — you'll show them, not commit them.

## Find your track

| Track | You do | Time |
|---|---|---|
| **Interop** | Full loop, hands-on: spec → plan → implement → review → verify | 15 min |
| **SysOps / NetSuite-scripting** | Review → verify, hands-on. A requirement doc and a first-pass draft are already provided — your hands-on time goes entirely to reviewing and gating the send | 15 min |
| **DBA** | Guided walkthrough of all five stages (facilitator drives) + your own take-home spec | 15 min |

---

## Interop track — full loop, hands-on

### 1 — Spec (3 min)
Open `docs/routine-template.md`. Fill each field yourself for a "case-review" pipeline — trigger, prompt body, context sources, skills invoked, trust-spectrum position, and success signal.

The success signal is the field people skip — don't leave it blank. Write one concrete, checkable sentence (e.g., "summary names only tables that appear in `schema.sql`, preserves the case's priority, and no draft reaches `outbound/` without human approval").

### 2 — Plan (2 min)
**Ask Claude** to read your filled `docs/routine-template.md` and turn it into an ordered plan for the pipeline. Read the plan against your spec — does it include a separate review step and a human gate?

### 3 — Implement (3 min)
**Ask Claude** to draft a review summary of case 205 — using the case-review skill, the case's live API data, and by reading (never running) `stored_procedures/usp_UpdateTenantStats.sql` to reason about how the rollup is maintained. The draft pass saves its output to `docs/case-205-draft.md`.

**You should see** the case's live data shaped like this (`GET /api/cases/205`):
```json
{
  "case_id": 205,
  "contact_id": 4,
  "created_at": "2026-07-20 14:02:11",
  "notes": [
    {
      "author": "support-agent-1",
      "body": "Numbers point to a rounding difference in the nightly aggregation job, not the report itself.",
      "case_id": 205,
      "created_at": "2026-07-20 14:02:11",
      "note_id": 303
    }
  ],
  "priority": "escalated",
  "status": "open",
  "subject": "Escalation: billing report totals don't reconcile",
  "tenant_id": 4
}
```

### 4 — Review ⭐ (3 min — the payoff step)
Run the review as a **separate** invocation from the draft pass — that separation is the whole point. **Ask Claude** to act as an adversarial reviewer and check the draft (it reads your saved draft from `docs/case-205-draft.md` by default) against `schema.sql` and the CLAUDE.md KB — specifically, whether it named a table that doesn't exist, and whether it preserved the case's priority. It's checking against more than one source at once — expect that, not a single-file read.

**You should see** a numbered finding list, one line per check:
```
1. <CATEGORY> — PASS/FAIL, + fix on FAIL
2. <CATEGORY> — PASS/FAIL, + fix on FAIL
3. <CATEGORY> — PASS/FAIL, + fix on FAIL
```

Optional: corroborate the catch yourself by opening `http://localhost:5050/cases/205` (Windows: add `--browser msedge`) — the case's priority renders as a tag on the page, e.g. `escalated`.

### 5 — Verify (1.5 min)
**Ask Claude** to write the approved summary to `outbound/case-205-summary.md`.

**You should see** it decline first:
```
I'm not writing to outbound/ yet. Per CLAUDE.md, nothing is written to outbound/
until (a) the review pass has run and (b) a human has explicitly approved this
specific summary. The review flagged an invented table and a missing escalated
flag — please confirm those are fixed and approve the write.
```
Fix the draft per the reviewer's catch, then explicitly approve the write. Confirm `outbound/case-205-summary.md` now exists.

**Done:**
- `docs/routine-template.md`'s success-signal field is non-empty.
- The review named at least one concrete catch.
- The `outbound/` write happened only after the review ran and you gave explicit approval — either Claude declined on its own and you then approved, or (if it didn't decline) you made the human-approval call out loud before the write anyway.
- `outbound/case-205-summary.md` exists and, on open, contains "escalated" and names only real tables (no `billing_ledger`).

**Share back:** one or two volunteers screenshare the review catching the issue, plus the approved `outbound/case-205-summary.md`.

---

## SysOps / NetSuite-scripting track — review → verify, hands-on

You're running the same draft-then-review move your own team already practices: take a requirement and a first-pass draft, review the draft against the requirement, and write the review down as a doc plus a test plan. The requirement and the draft are **provided** — your hands-on time goes entirely to the review and the send gate, not to authoring spec/plan/implement. You start your hands-on work earlier than the room does; everyone converges at verify.

### 1 — Orient (2 min)
Open the provided requirement, `docs/case-review-requirement.md`, and the provided draft, `docs/sample-flawed-draft.md`. Read both — you're about to review the draft against that requirement.

**The provided draft**, for reference:
```
Case 205 (Cascade Orthopedic Associates): billing report totals don't reconcile.
Per the note, the cause is a rounding difference in the nightly aggregation job.
The rollup is maintained in the billing_ledger table and surfaced on the
dashboard. Recommend confirming the aggregation rounding.
```

### 2 — Review ⭐ (6 min — the payoff step)
**Ask Claude** to run the review-writeup pass: adversarially review the draft strictly against the original requirement plus `schema.sql` and the CLAUDE.md KB, and write the findings to a markdown doc at `reviews/case-205-review.md`, including a short test-plan sketch — one checkable step per fix. It's checking against several sources at once (the requirement, the schema, the KB, the case's live data), not just the draft alone. Then open `reviews/case-205-review.md` and read it.

**You should see** a doc shaped like this:
```md
## Findings
<one numbered line per requirement checked — #, PASS or FAIL, and on FAIL the concrete fix>

## Test plan
<one checkable step per FAIL finding>
```

### 3 — Corroborate (same 6-minute block as step 2)
Don't just trust the review — check it yourself. Open `schema.sql` and confirm the table it flagged as invented is genuinely absent from the six real tables. Then open `http://localhost:5050/cases/205` (Windows: add `--browser msedge`) and confirm the priority tag rendered on the page matches what the review told you. If the findings were vague, re-run the review-writeup pass and ask it to name the concrete fix per finding.

### 4 — Verify (3.5 min)
Apply the fix the review named, then **ask Claude** to write the corrected summary to `outbound/case-205-summary.md`.

**You should see** it decline first:
```
I'm not writing to outbound/ yet. Per CLAUDE.md, nothing is written to outbound/
until (a) the review pass has run and (b) a human has explicitly approved this
specific summary. The review flagged an invented table and a missing escalated
flag — please confirm those are fixed and approve the write.
```
Confirm your `reviews/case-205-review.md` exists, then explicitly approve. Confirm `outbound/case-205-summary.md` now exists.

**Done:**
- `reviews/case-205-review.md` exists and contains at least one **FAIL** finding plus a "Test plan" section.
- You corroborated at least one finding yourself, against the schema or the live page.
- The `outbound/` write happened only after the review ran and you gave explicit approval — either Claude declined on its own and you then approved, or (if it didn't decline) you made the human-approval call out loud before the write anyway.
- `outbound/case-205-summary.md` exists and, on open, contains "escalated"/"ESCALATED" and names only real tables (no `billing_ledger`).

**Share back:** a volunteer screenshares `reviews/case-205-review.md` (the findings + test plan) and the approved `outbound/case-205-summary.md`, and says the one thing the review caught.

---

## DBA track — guided walkthrough + take-home

The facilitator drives all five stages on-screen — spec through verify — at the same pace as the Interop track, using the same commands. Your hands-on artifact is your own copy of the spec: fill `docs/routine-template.md` as a take-home, anchored on your own `/sp-table-map` lookup from an earlier lab. A good anchor for the success-signal field: *zero invented tables; every table in the summary appears in `schema.sql`.*

No invocation of your own is required to reach done — the filled template is the artifact.

**Done:** `docs/routine-template.md` is filled — every field, including success signal.

**Share back:** show your filled take-home template.

---

## If you get stuck

| Symptom | Do this |
|---|---|
| (SysOps) Review-writeup pass didn't write the file, or the findings are vague | Ask your facilitator for the exact prompt. Still stuck? Restore the reference: `git checkout origin/lab-capstone-solution -- reviews/case-205-review.md` |
| (Interop) Your own draft came out clean — nothing for the review to catch | Re-run the review pass, pointing it at `docs/sample-flawed-draft.md` instead of your own draft |
| (Interop) Review output is vague | Ask your facilitator for the exact reviewer prompt |
| Claude doesn't decline the premature `outbound/` write | That's fine — it's a soft CLAUDE.md reminder, not a hard block. Make the human-approval call yourself, out loud, before the write happens |
| `CLAUDE.md` or the pre-baked commands got edited or broken | `git checkout origin/lab-capstone-start -- CLAUDE.md .claude/` |
| The requirement or sample-draft file got edited | `git checkout origin/lab-capstone-start -- docs/case-review-requirement.md docs/sample-flawed-draft.md` |
| Need the reference final artifact | `git checkout origin/lab-capstone-solution -- outbound/case-205-summary.md` |
| Database looks corrupted | `python seed.py` once |
| Time is short | Skip to verify: restore just the final artifact — `git checkout origin/lab-capstone-solution -- outbound/case-205-summary.md` — rather than switching branches. A full branch switch conflicts with your own uncommitted work (routine template, review doc); this doesn't. |

**Never** restore `docs/` broadly, and never restore `docs/routine-template.md` specifically, to fix something else — that silently overwrites your filled spec/take-home, and since nothing in this lab is committed, that loss is unrecoverable. Restore files by exact path only.
