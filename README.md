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

To optimize data retrieval for Business Intelligence environments and ensure efficient KPI computation, a two-tiered data strategy is implemented:

### 1. Source Data Layer

* **Source Table:** Raw log data are automatically stored in the **`production_lines_event_logs`** table upon arrival.
* **Columns:** This table contains the raw event data: `production_line_id`, `status`, and `timestamp`.

### 2. Aggregated BI Layer

* **Target Table:** BI environments query a materialized, aggregated table named **`session_table`**. This ensures the most efficient processing.
* **Structure:** The `session_table` includes: `session_id` (unique identifier), `production_line_id`, `start_timestamp`, `stop_timestamp`, `duration`, and `working_status`.
* **Session Logic:**
    * It tracks only **completed session cycles** (start-stop sequence) based on timestamp order.
    * `working_status=1` denotes an **uptime working session**.
    * `working_status=0` denotes a **downtime session** occurring between two uptime sessions.
    * `duration` is the time in seconds corresponding to each session type.
* **Update Process:** The `session_table` is refreshed via a **stored procedure** named refresh_session_table every **15 minutes** using the newly stored data from the source table. BI analysts query this table exclusively.

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


