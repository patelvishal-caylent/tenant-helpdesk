# Demo materials (Session 1 live demos)

Not auto-loaded by Claude Code — these are staging files for the facilitator to copy into place live. Nothing here affects Demo 1's "no grounding" starting state.

## Demo 1 → Demo 2 sequence

1. **Demo 1 (the gap):** repo has no `CLAUDE.md`. Ask Claude an ungrounded question about the schema and let it guess/hallucinate.
2. **Demo 2 (the payoff):** copy this folder's `CLAUDE.md.for-demo-2` into the repo root as `CLAUDE.md`, then re-ask the same question.

```bash
cp demo-materials/CLAUDE.md.for-demo-2 CLAUDE.md
```

To reset back to Demo 1's starting state for a re-run (e.g., a second cohort, or a dry run beforehand):

```bash
rm CLAUDE.md
```

The content matches the deck's Demo 2 codewin exactly — it describes the app's real schema (`tenants`, `contacts`, `orders`, `cases`, `case_notes`, `tenant_stats`), not a fictional one, so what Claude reads here matches what's actually in `schema.sql`.
