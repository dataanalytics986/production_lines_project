/* Stored Procedure for adding new data to the session_table for BI purposes */
USE production_lines_db;
GO

CREATE OR ALTER PROCEDURE [dbo].[refresh_session_table]
AS
BEGIN
SET NOCOUNT ON;

WITH temp_t AS 
(
	SELECT
	production_line_id,
	timestamp AS start_timestamp,
	LEAD(timestamp) OVER (PARTITION BY production_line_id ORDER BY timestamp) AS stop_timestamp,
	DATEDIFF(SECOND, timestamp,
				LEAD(timestamp) OVER (PARTITION BY production_line_id ORDER BY timestamp)) AS duration,
	CASE WHEN status = 'START' THEN 1 ELSE 0 END AS working_status
	FROM [production_lines_db].[dbo].[production_lines_event_logs]
	WHERE status!='ON'
)
INSERT INTO dbo.session_table 
(
	production_line_id,
	start_timestamp,
	stop_timestamp,
	duration,
	working_status
)
SELECT
	t2.production_line_id,
	t2.start_timestamp,
	t2.stop_timestamp,
	t2.duration,
	t2.working_status
FROM temp_t AS t2
WHERE t2.duration IS NOT NULL
AND NOT EXISTS 
(
	SELECT 1
	FROM [production_lines_db].[dbo].[session_table ] AS t1
	WHERE t1.production_line_id = t2.production_line_id
	AND t1.start_timestamp = t2.start_timestamp
	AND t1.stop_timestamp = t2.stop_timestamp
);
END;