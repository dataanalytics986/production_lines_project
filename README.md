# 🏭 Production Lines Project

## Short Description

[cite_start]This project is designed to monitor and track the status of **multiple production lines** within a production floor[cite: 1]. [cite_start]By keeping a detailed record of each production line's status, the system calculates critical **Production KPIs** (Key Performance Indicators) for the production manager[cite: 1].

---

## Core Features (Business Questions Addressed)

This solution is structured to answer key business questions regarding production line performance:

1.  **Production Line Specific Analysis:** For a specified production line (e.g., "gr-np-47"), generate a table with the following columns:
    * [cite_start]`start_timestamp`: The timestamp marking the **initiation** of the production process[cite: 2].
    * [cite_start]`stop_timestamp`: The timestamp marking the **termination** of the production process after the last initiation[cite: 3].
    * [cite_start]`duration`: The **total duration** of the production process[cite: 4].
2.  [cite_start]**Overall Floor Uptime/Downtime:** Calculate the **total uptime and downtime** for the entire production floor[cite: 4].
3.  [cite_start]**Downtime Leaderboard:** Identify **which production line** had the **most downtime** and provide the corresponding duration[cite: 5].

---

## 🛠️ Technologies Used

The project utilizes the following technologies:

* [cite_start]**Data Warehouse:** Microsoft SQL Server Datawarehouse [cite: 6]
* [cite_start]**Database Language:** MS SQL [cite: 6]
* [cite_start]**Scripting/Analysis:** Python programming language [cite: 6]

---

## Installation Instructions

To set up the project locally and begin calculating KPIs, follow these two main steps:

1.  **Database Setup:** The user must first execute the provided **SQL scripts** to create the necessary database. [cite_start]This database is where the production lines' event logs will be stored[cite: 7].
2.  **Python Library Setup:** The user must set up the Python library on the host system. [cite_start]This ensures that the **KPI functions** can be imported into the user's main Python script for execution[cite: 8].

---

## Author

* [cite_start]**Name:** Dimitrios Koromilaw [cite: 8]
* [cite_start]**GitHub Profile:** [https://github.com/dataanalytics986](https://github.com/dataanalytics986) [cite: 8]
* [cite_start]**Email:** dimkoromilas@gmail.com [cite: 8]


