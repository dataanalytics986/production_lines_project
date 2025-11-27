# production_lines_lib

A lightweight Python package designed to calculate key performance indicators (KPIs) related to production line activity, downtime, and uptime analysis using Pandas DataFrames.

---

## Features

This library provides three core functions for analyzing production data:

1.  **`get_kpi_1`**: Filters and returns specific session data for a designated production line (`gr-np-47`) during its uptime.
2.  **`get_kpi_2`**: Calculates the **Total Uptime** and **Total Downtime** duration for the entire production floor.
3.  **`get_kpi_3`**: Identifies the single **production line with the maximum total downtime** and returns that value.

---

## Installation

Since the package relies on the `pandas` library, ensure you have it installed.

### Prerequisites

You need **Python 3.8+** and **Pandas**.

### Local Installation (for development/use)

Assuming you have cloned the project repository or created the file structure, navigate to the root directory (`production_lines_lib_project/`) containing `setup.py` and run:

```bash
pip install -e .
```
---

## kpi_DEMO.py

This self-contained Python script connects directly to the SQL Server, retrieves the necessary session_table data, and immediately executes all three KPI functions to address the specified business questions, without requiring the pre-built KPI library package.


