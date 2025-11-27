/* Query for updating the session_table by inserting new sessions computed by the 'production_lines_event_logs' source table */
WITH temp_t AS
(
	/*
		This temporary table returns rows for uptime, downtime and incomplete sessions.
		Due to the partitioning windows based on the production_line_id ordered by the timestamp, we can track the lead values, 
		if they exist.
		The distinction mark of a incomplete sesstion is stop_timestamp=NULL. For an uptime session we need status=START, 
		which is stored as working_status=1, while status=STOP flags a downtime session setting the working_status=0.
		That way, we can keep information for both uptime and downtime session durations.

		execution example:
		
		production_line_id	start_timestamp			 stop_timestamp 			duration	working_status
		gr-np-08			2020-10-07 05:55:08.000	 NULL						NULL			0
		gr-np-22			2020-10-07 03:05:02.000	 NULL						NULL			0
		gr-np-47			2020-10-07 01:33:20.000	 2020-10-07 02:03:20.000	1800			1
		gr-np-47			2020-10-07 02:03:20.000	 2020-10-07 02:15:02.000	702				0
		gr-np-47			2020-10-07 02:15:02.000	 2020-10-07 04:15:02.000	7200			1
		gr-np-47			2020-10-07 04:15:02.000	 2020-10-07 05:00:00.000	2698			0
		gr-np-47			2020-10-07 05:00:00.000	 2020-10-07 05:55:17.000	3317			1
		gr-np-47			2020-10-07 05:55:17.000	 NULL						NULL			0

	*/
	SELECT
	production_line_id,
	timestamp AS start_timestamp,

	/* Windows function for window partitioning using the next (lead) row, if it exists */
	LEAD(timestamp) OVER (PARTITION BY production_line_id ORDER BY timestamp) AS stop_timestamp,

	/* Computes the time difference in seconds */
	DATEDIFF(SECOND, timestamp, LEAD(timestamp) OVER (PARTITION BY production_line_id ORDER BY timestamp)) AS duration,

	/* If status=START working_status is set to 1, else is set to 0 */
	CASE WHEN status='START' THEN 1 ELSE 0 END AS working_status

	FROM [production_lines_db].[dbo].[production_lines_event_logs]

	/* We only need lines with status=START or status=STOP */
	WHERE status!='ON' 
)
INSERT INTO [test].dbo.session_table 
(

	/* exexution example of session_table snapshot:
	
		 session_id		production_line_id	start_timestamp				stop_timestamp				duration	working_status
		 4				gr-np-47			2020-10-07 01:33:20.000		2020-10-07 02:03:20.000		1800			1
		 5				gr-np-47			2020-10-07 02:03:20.000		2020-10-07 02:15:02.000		702				0
		 6				gr-np-47			2020-10-07 02:15:02.000		2020-10-07 04:15:02.000		7200			1
		 7				gr-np-47			2020-10-07 04:15:02.000		2020-10-07 05:00:00.000		2698			0
		 8				gr-np-47			2020-10-07 05:00:00.000		2020-10-07 05:55:17.000		3317			1
	  */

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

/* We keep only the complete sessions (uptime - downtime) */
WHERE t2.duration IS NOT NULL 

/* To avoid duplicates, we must check that the newly computed rows do not exist already in the session_table */
AND NOT EXISTS 
(
	SELECT 1
	FROM [test].dbo.session_table AS t1
	WHERE t1.production_line_id=t2.production_line_id
	AND t1.start_timestamp=t2.start_timestamp
	AND t1.stop_timestamp=t2.stop_timestamp
);