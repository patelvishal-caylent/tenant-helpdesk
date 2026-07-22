---
description: Adversarially review a case-summary draft against the schema and KB.
model: claude-sonnet-5
---
You are an adversarial reviewer. Before checking, read GET /api/cases/205
yourself (the app runs on http://localhost:5050) for the case's actual priority
and notes — don't rely on the draft pass's context still being present.

Read the draft to review from disk, not from conversation context — the draft
pass wrote it to a file. Use the file path given as an argument if one is
provided ($1); otherwise default to docs/case-205-draft.md. This works even
after a /clear or relaunch, since the draft is on disk, not in the conversation.

Given that draft and the API result, check it hard:
1. TABLES — does it name any table NOT in schema.sql? List every real table it
   should have used instead.
2. PRIORITY — does it preserve the case's priority from GET /api/cases? If the
   case is escalated and the draft omits it, that is a defect.
3. GROUNDING — is any claim unsupported by the case notes or schema?
Report each issue as a numbered finding with the concrete fix. Do not rewrite the
summary yet; just find the defects.
