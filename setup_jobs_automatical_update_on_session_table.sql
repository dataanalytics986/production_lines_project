/* Job creation - SQL Serverl Agent job */
USE msdb;
GO

EXEC sp_add_job
    @job_name = N'Refresh Session Table Job',
    @enabled = 1,
    @description = N'Refresh session_table every 15 minutes';
GO


/* Job stepping */
EXEC sp_add_jobstep
    @job_name = N'Refresh Session Table Job',
    @step_name = N'Refresh Step',
    @subsystem = N'TSQL',
    @database_name = N'test',
    @command = N'EXEC dbo.refresh_session_table;',
    @on_success_action = 1,
    @on_fail_action = 2;
GO


/* 15-minute scheduler */
EXEC sp_add_schedule
    @schedule_name = N'Every 15 Minutes',
    @freq_type = 4,     
    @freq_interval = 1,
    @freq_subday_type = 4, 
    @freq_subday_interval = 15,
    @active_start_time = 000000; 
GO

/* Schedule attachment to a job */
EXEC sp_attach_schedule
    @job_name = N'Refresh Session Table Job',
    @schedule_name = N'Every 15 Minutes';
GO


/* Job assignment to the SQL Server */
EXEC sp_add_jobserver
    @job_name = N'Refresh Session Table Job';
GO