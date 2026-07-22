# Routine: case-review
- Trigger: review of an escalated case
- Prompt body: draft a grounded case summary from schema.sql + the case API,
  then run a separate adversarial review pass against schema.sql + CLAUDE.md
  before writing anything to outbound/.
- Context sources: schema.sql, GET /api/cases/<id>, usp_UpdateTenantStats.sql, CLAUDE.md
- Skills invoked: case-review
- Trust-spectrum position: always-human on send
- Success signal: summary names only tables in schema.sql; preserves case
  priority (escalated cases flagged ESCALATED); nothing reaches outbound/
  without the review pass AND explicit human approval.
