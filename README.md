# Production Lines Project

## Short Description

This project is designed to monitor and track the status of **multiple production lines** within a production floor. By keeping a detailed record of each production line's status, the system calculates critical **Production KPIs** (Key Performance Indicators) for the production manager.

---

## Core Features (Business Questions Addressed)

This solution is structured to answer key business questions regarding production line performance:

1.  **Production Line Specific Analysis:** For a specified production line (e.g., "gr-np-47"), generate a table with the following columns:
    * `start_timestamp`: The timestamp marking the **initiation** of the production process[cite: 2].
    * `stop_timestamp`: The timestamp marking the **termination** of the production process after the last initiation.
    * `duration`: The **total duration** of the production process.
2.  **Overall Floor Uptime/Downtime:** Calculate the **total uptime and downtime** for the entire production floor.
3. **Downtime Leaderboard:** Identify **which production line** had the **most downtime** and provide the corresponding duration.

---

## Technologies Used

The project utilizes the following technologies:

* **Data Warehouse:** Microsoft SQL Server Datawarehouse
* **Database Language:** MS SQL
* **Scripting/Analysis:** Python programming language

---

## Installation Instructions

To set up the project locally and begin calculating KPIs, follow these two main steps:

1.  **Database Setup:** The user must first execute the provided **SQL scripts** to create the necessary database. This database is where the production lines' event logs will be stored.
2.  **Python Library Setup:** The user must set up the Python library on the host system. This ensures that the **KPI functions** can be imported into the user's main Python script for execution.

---

## Author

* **Name:** Dimitrios Koromilas
* **GitHub Profile:** [https://github.com/dataanalytics986](https://github.com/dataanalytics986)
* **Email:** dimkoromilas@gmail.com


