# Production Lines Project

## Short Description

This project is designed to monitor and track the status of **multiple production lines** within a production floor. By keeping a detailed record of each production line's status, the system calculates critical **Production KPIs** (Key Performance Indicators) for the production manager.

---

## Core Features (Business Questions Addressed)

This solution is structured to answer key business questions regarding production line performance:

1.  **Production Line Specific Analysis:** For a specified production line (e.g., "gr-np-47"), generate a table with the following columns:
    * `start_timestamp`: The timestamp marking the **initiation** of the production process.
    * `stop_timestamp`: The timestamp marking the **termination** of the production process after the last initiation.
    * `duration`: The **total duration** of the production process.
2.  **Overall Floor Uptime/Downtime:** Calculate the **total uptime and downtime** for the entire production floor.
3. **Downtime Leaderboard:** Identify **which production line** had the **most downtime** and provide the corresponding duration.

---

## Data Strategy for Efficient BI & KPIs

To ensure **efficient computation of the KPIs** and effective presentation on a Business Intelligence (BI) dashboard environment, the following strategic tactics are employed:

* **Raw Data Storage:** Raw log data, upon their arrival, are automatically stored on the source table named **`production_lines_event_logs`**. This table has the columns: `production_line_id`, `status`, and `timestamp`.
* **Aggregated BI Table (`session_table`):** For BI purposes and the most efficient processing, BI environments will only query on an aggregated table derived from the source, named **`session_table`**.
* **`session_table` Structure:** This table is created as a **materialized table** and consists of the columns: `session_id` (as unique identifier), `production_line_id`, `start_timestamp`, `stop_timestamp`, `duration`, and `working_status`.
* **Session Tracking:** The `session_table` tracks and contains only the **completed session cycles** (start-stop sequence) according to the timestamp order.
    * Sessions with `working_status=1` are considered **uptime working sessions**.
    * Sessions with `working_status=0` are considered **downtime sessions** between two uptime sessions.
* **Duration Measurement:** The `duration` column is the time in seconds corresponding to each type of session.
* **BI Querying:** BI analysts only see and query the `session_table`.
* **Update Frequency:** The `session_table` is updated via a **stored procedure** every **15 minutes** from the newly data stored at the `production_lines_event_logs` source table.

## Technologies Used

The project utilizes the following technologies:

* **Data Warehouse:** Microsoft SQL Server Datawarehouse
* **Database Language:** MS SQL
* **Scripting/Analysis:** Python programming language

---

## Installation Instructions

To set up the project locally and begin calculating KPIs, follow these two main steps:

1.  **Database Setup:** The user must first make sure that the Microsoft SQL Server is properly installed on his system. Secondly, user must execute the provided **SQL scripts** to create the necessary database, tables and routines for writing/updating the tables. This database and tables is where the production lines' event logs will be stored.
2.  **Python Library Setup:** The user must set up the Python library on the host system. This ensures that the **KPI functions** can be imported into the user's main Python script for execution.

---

## Author

* **Name:** Dimitrios Koromilas
* **GitHub Profile:** [https://github.com/dataanalytics986](https://github.com/dataanalytics986)
* **Email:** dimkoromilas@gmail.com


