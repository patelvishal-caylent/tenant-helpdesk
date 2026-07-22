---
description: Read a stored-procedure reference file and list the tables it reads vs. writes, verified against schema.sql.
---

Read the stored-procedure file at $ARGUMENTS as a reference document — do NOT run it
(these are T-SQL files against a SQLite app; they exist to read and reason about).

List, in two groups, the tables it READS FROM and the tables it WRITES TO — one table
per line. A SELECT-only procedure writes nothing; say so explicitly.

Then check every table name against schema.sql in this repo. schema.sql is the only
source of truth for which tables exist. Flag any table you named that does NOT appear
in schema.sql, and any table in the procedure body you may have missed. Do not include
tables that appear only in comments and not in the SQL body.
