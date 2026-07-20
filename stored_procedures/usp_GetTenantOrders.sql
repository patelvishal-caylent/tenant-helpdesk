-- usp_GetTenantOrders
-- Reference artifact only — written in T-SQL style for the "read and reason about it"
-- exercises. Not executed against the app's SQLite database; this file exists for
-- Claude Code to read, not to run.
--
-- Returns all orders for a given tenant, joined with contact info for the tenant's
-- primary contact. Used by the support portal's tenant detail view.

CREATE PROCEDURE usp_GetTenantOrders
    @TenantId INT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        o.order_id,
        o.status,
        o.amount_cents,
        o.created_at,
        c.name  AS primary_contact_name,
        c.email AS primary_contact_email
    FROM orders o
    INNER JOIN tenants t
        ON t.tenant_id = o.tenant_id
    LEFT JOIN contacts c
        ON c.tenant_id = t.tenant_id
        AND c.is_primary = 1
    WHERE o.tenant_id = @TenantId
    ORDER BY o.created_at DESC;
END
