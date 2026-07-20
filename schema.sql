-- Workshop demo schema — fictional multi-tenant support/ops system.
-- Entirely synthetic. No resemblance to any real company's data intended.

CREATE TABLE tenants (
    tenant_id       INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    tier            TEXT NOT NULL CHECK (tier IN ('small', 'medium', 'large')),
    cluster_type    TEXT NOT NULL,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE contacts (
    contact_id      INTEGER PRIMARY KEY,
    tenant_id       INTEGER NOT NULL REFERENCES tenants(tenant_id),
    name            TEXT NOT NULL,
    title           TEXT,
    email           TEXT NOT NULL,
    is_primary      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE orders (
    order_id        INTEGER PRIMARY KEY,
    tenant_id       INTEGER NOT NULL REFERENCES tenants(tenant_id),
    status          TEXT NOT NULL CHECK (status IN ('open', 'fulfilled', 'cancelled')),
    amount_cents    INTEGER NOT NULL,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE cases (
    case_id         INTEGER PRIMARY KEY,
    tenant_id       INTEGER NOT NULL REFERENCES tenants(tenant_id),
    contact_id      INTEGER REFERENCES contacts(contact_id),
    subject         TEXT NOT NULL,
    status          TEXT NOT NULL CHECK (status IN ('open', 'awaiting_reply', 'resolved')),
    priority        TEXT NOT NULL DEFAULT 'normal' CHECK (priority IN ('low', 'normal', 'high', 'escalated')),
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE case_notes (
    note_id         INTEGER PRIMARY KEY,
    case_id         INTEGER NOT NULL REFERENCES cases(case_id),
    author          TEXT NOT NULL,
    body            TEXT NOT NULL,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE tenant_stats (
    tenant_id       INTEGER PRIMARY KEY REFERENCES tenants(tenant_id),
    open_case_count INTEGER NOT NULL DEFAULT 0,
    order_count     INTEGER NOT NULL DEFAULT 0,
    last_updated    TEXT NOT NULL DEFAULT (datetime('now'))
);
