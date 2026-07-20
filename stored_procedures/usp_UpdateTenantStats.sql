-- usp_UpdateTenantStats
-- Reference artifact only — written in T-SQL style for the "read and reason about it"
-- exercises (e.g. "what tables does this touch, so I know what to check for stale
-- stats"). Not executed against the app's SQLite database.
--
-- Recomputes the rollup counters in tenant_stats for a single tenant: how many
-- open cases, how many total orders. Runs nightly in production for every tenant;
-- this version takes a single @TenantId so it can also be run ad hoc after a
-- support agent flags a tenant's dashboard numbers as looking stale.

CREATE PROCEDURE usp_UpdateTenantStats
    @TenantId INT
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @OpenCaseCount INT;
    DECLARE @OrderCount INT;

    SELECT @OpenCaseCount = COUNT(*)
    FROM cases
    WHERE tenant_id = @TenantId
      AND status <> 'resolved';

    SELECT @OrderCount = COUNT(*)
    FROM orders
    WHERE tenant_id = @TenantId;

    UPDATE tenant_stats
    SET open_case_count = @OpenCaseCount,
        order_count     = @OrderCount,
        last_updated    = GETDATE()
    WHERE tenant_id = @TenantId;

    IF @@ROWCOUNT = 0
    BEGIN
        INSERT INTO tenant_stats (tenant_id, open_case_count, order_count, last_updated)
        VALUES (@TenantId, @OpenCaseCount, @OrderCount, GETDATE());
    END
END
