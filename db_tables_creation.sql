/* Database creation */
CREATE DATABASE production_lines_db;

/* Make database usable */
USE production_lines_db;
GO


/* The initial creation of the event logs table named 'production_lines_event_logs' */
CREATE TABLE [production_lines_db].[dbo].[production_lines_event_logs] (
	id BIGINT PRIMARY KEY IDENTITY(1,1), 
    production_line_id VARCHAR(50) NOT NULL,
    status VARCHAR(10) NOT NULL,
    timestamp datetime DEFAULT(getdate())
);


/* Creation of the materialized table named 'session_table' for BI purposes */
CREATE TABLE [production_lines_db].[dbo].session_table (
    session_id INT IDENTITY(1,1) PRIMARY KEY,
    production_line_id VARCHAR(100) NOT NULL,
    start_timestamp DATETIME NOT NULL,
    stop_timestamp DATETIME NOT NULL,
    duration INT NOT NULL,
    working_status BIT NOT NULL,
	CONSTRAINT uq_session UNIQUE (production_line_id, start_timestamp, stop_timestamp)
);