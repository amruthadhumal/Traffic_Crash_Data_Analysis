# 🚦 Traffic Crash Analytics & Safety Intelligence Platform

## 📌 Project Overview

The Traffic Crash Analytics & Safety Intelligence Platform is a data analytics project designed to analyze traffic crash records and generate actionable road-safety insights. 
The project uses:

•	**Python (Pandas)** for data processing

•	**MySQL** for data storage and SQL analytics

•	**SQL** Window Functions & Aggregations for advanced analysis

•	**Streamlit** for interactive dashboard visualization

---

## 🎯 Objectives

* Analyze traffic crash trends and patterns
* Identify accident-prone streets and hotspot zones
* Evaluate the impact of weather and lighting conditions
* Understand injury severity across crash types
* Discover primary causes of accidents
* Build an interactive dashboard for visualization and reporting

---

## 🛠️ Technology Stack

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Data Processing                |
| Pandas     | Data Cleaning & Transformation |
| MySQL      | Data Storage & Analytics       |
| SQL        | Advanced Querying & Insights   |
| Streamlit  | Interactive Dashboard          |
| Tabulate   | Query Result Formatting        |

---

## 📂 Dataset Information

The project uses a Traffic Crash dataset containing:

* Crash Record ID
* Crash Date & Year
* Street Name
* Weather Conditions
* Crash Type
* Traffic Control Devices
* Lighting Conditions
* Injury Information
* Geographic Coordinates (Latitude & Longitude)
* Primary & Secondary Contributing Causes

---

## 🔄 Project Architecture

```text
Traffic Crash Dataset
        │
        ▼
Data Loading (Pandas)
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
MySQL Database Storage
        │
        ▼
Advanced SQL Analytics
        │
        ▼
Insight Generation
        │
        ▼
Streamlit Dashboard
```

---

## 📊 Analytical SQL Use Cases

### Step 1: Import Required Libraries
  import pandas as pd
  
### Purpose
Pandas is used to:

 • Load CSV files

 • Clean and transform data

 • Prepare records for database insertion
________________________________________

### Step 2: Load Traffic Crash Dataset
df = pd.read_csv("Traffic_CrashesData.csv")
### What Happens Here?
The traffic crash dataset is loaded into a Pandas DataFrame.
### Why?
A DataFrame provides a structured format for:

•	Viewing records

•	Cleaning data

•	Performing transformations
________________________________________

### Step 3: Understand the Dataset
View Data Structure

df.info()

### Purpose

Displays:

• Number of rows
• Number of columns
• Data types
• Missing values
________________________________________

### Check Missing Values

df.isnull().sum()

### Purpose

Identifies incomplete records that may affect analysis.
________________________________________

### Check Duplicate Values

df.duplicated()

### Purpose

Identifies duplicate records that may affect analysis.

________________________________________

### View Sample Records

df.head(10)

### Purpose

Displays the first 10 rows for quick inspection.

________________________________________
### Step 4: Data Cleaning & Standardization

Rename Column Names

df.rename(columns={
    'date':'DATE',
    'year':'YEAR'
}, inplace=True)

### Purpose

Standardizes column names.

### Benefits

• Improves readability

• Makes SQL queries easier

• Maintains naming consistency
________________________________________
### Step 5: Connect to MySQL Database
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)
### Purpose
Creates a connection between Python and MySQL.
### Why?
The project stores crash data in a relational database for advanced querying.
________________________________________
### Step 6: Create Database
CREATE DATABASE traffic_crash_db;
### Purpose
Creates a dedicated database to store traffic crash information.
________________________________________
### Step 7: Select Database
USE traffic_crash_db;
### Purpose
Makes MySQL use the newly created database.
________________________________________
### Step 8: Create Traffic Crash Table
A table named:
traffic_crash_data
is created.

### Major Columns
| Column                  | Description             |
| ----------------------- | ----------------------- |
| CRASH_RECORD_ID         | Unique crash identifier |
| CRASH_DATE              | Date of accident        |
| POSTED_SPEED_LIMIT      | Road speed limit        |
| WEATHER_CONDITION       | Weather during crash    |
| CRASH_TYPE              | Type of collision       |
| INJURIES_TOTAL          | Total injuries          |
| LIGHTING_CONDITION      | Daylight/Darkness       |
| LATITUDE                | Location latitude       |
| LONGITUDE               | Location longitude      |
| PRIM_CONTRIBUTORY_CAUSE | Main cause              |

### Purpose
Provides a structured database table for analysis.
________________________________________

### Step 9: Insert Data into MySQL
INSERT INTO traffic_crash_data (...)
VALUES (...)
### Purpose
Transfers cleaned data from Pandas DataFrame to MySQL.
### Benefits

• Permanent storage

• Faster querying

• Scalability
________________________________________
### Step 10: SQL Analytics & Business Insights
The project executes 15 analytical SQL queries.

### Query 1
Top 5 Dangerous Weather and Crash Type Combinations
#### Objective
Find combinations of:

•	Weather condition

•	Crash type

that result in the highest number of crashes.

#### Business Value
Helps authorities identify high-risk driving situations.
________________________________________
### Query 2
Top 10 Streets with Highest Injury Crashes
#### Objective
Identify streets with maximum injury-causing accidents.
#### Business Value
Supports:

•	Road safety planning

•	Traffic control improvements

•	Infrastructure upgrades

________________________________________
### Query 3
Injury Percentage by Crash Type
#### Objective
Calculate:
(Injury Crashes / Total Crashes) × 100
for every crash type.
#### Business Value
Highlights crash types that are most dangerous.
________________________________________
### Query 4
Peak Crash Hour for Each Month
#### Objective

Determine:

•	Which hour has the highest crashes for every month

Techniques Used

•	Common Table Expressions (CTE)

•	ROW_NUMBER()

#### Business Value
Helps deploy enforcement resources effectively.
________________________________________
### Query 5
Top Night-Time Crash Causes
#### Objective
Analyze crashes occurring after 6 PM.
#### Business Value
Identifies risky behaviours during night driving.
________________________________________
### Query 6
Daylight vs Darkness Injury Comparison
#### Objective
Compare average injuries under:

•	Daylight

•	Darkness

#### Business Value
Evaluates the impact of lighting conditions on crash severity.
________________________________________
### Query 7
Traffic Control Device with Highest Average Injuries
#### Objective
Determine which traffic control devices are associated with higher injury severity.

Examples:

•	Stop Signs
 
•	Traffic Signals

•	Yield Signs

#### Business Value
Supports traffic infrastructure improvements.
________________________________________
### Query 8
Top 5 Crash Locations
#### Objective
Identify locations with the highest crash frequency.

Fields Used

•	Latitude

•	Longitude

•	Street Information

#### Business Value
Pinpoints accident hotspots.
________________________________________
### Query 9
Streets with Highest Injury Rate
#### Objective
Find streets where crashes are most likely to cause injuries.
constraint only streets with, more than 100 crashes are considered.
#### Business Value
Improves prioritization of safety interventions.
________________________________________
### Query 10
Most Common Crash Type Per Year
#### Objective
Identify the dominant crash type for each year.

Techniques Used

•	RANK()

•	Window Functions

#### Business Value
Tracks long-term accident trends.
________________________________________
### Query 11
Day of Week with Highest Average Crashes
### Objective
Determine which weekday experiences the highest average crashes per hour.
### Business Value
Supports scheduling of enforcement and monitoring activities.
________________________________________
### Query 12
High-Risk Time Buckets
Time Groups

| Bucket          | Hours       |
| ----------------| ----------- |
| Morning         | 6-11        |
| Afternoon       | 12-17       |
| Evening         | 18-23       |
| Night           | 0-5         |

#### Objective
Find which period records the most injury crashes.
#### Business Value
Helps focus road safety campaigns.
________________________________________
### Query 13
Top 3 Causes for Each Crash Type
#### Objective

Identify:

•	Most common primary causes

•	Most common secondary causes for every crash type.

#### Techniques Used

•	CTE

•	Window Functions

•	ROW_NUMBER()

#### Business Value
Provides root-cause analysis.
________________________________________
### Query 14
Year-over-Year Crash Growth Rate
#### Objective
Measure annual crash growth.

#### Techniques Used

LAG()

#### Business Value
Tracks whether road safety is improving or worsening.
________________________________________
### Query 15
Crash Hotspot Zones
#### Objective
Group nearby locations by rounding:

Latitude → 2 decimal places

Longitude → 2 decimal places

#### Business Value
Identifies geographic clusters with high accident frequency.
________________________________________

## 📈 SQL Concepts Demonstrated

This project showcases advanced SQL techniques including:

* Common Table Expressions (CTEs)
* Aggregate Functions
* Window Functions
* ROW_NUMBER()
* RANK()
* LAG()
* GROUP BY & HAVING
* Date & Time Analysis

________________________________________

### Step 11: Build Streamlit Dashboard
The project includes a Streamlit-based dashboard for interactive analysis and visualization.

#### Install Streamlit

pip install streamlit

________________________________________
### Run Dashboard
streamlit run demo.py
#### Purpose
Provides:

•	Interactive visualizations

•	Query results

•	Road safety insights

________________________________________

## ⭐ Key Features

* Data Cleaning & Transformation
* Relational Database Design
* MySQL Integration
* Advanced SQL Analytics
* Interactive Dashboard Development

________________________________________

## 📊 Business Impact

The solution helps stakeholders:

* Improve road safety planning
* Identify dangerous intersections and roads
* Understand accident causes
________________________________________

## Conclusion
The Traffic Crash Analytics & Safety Intelligence Platform transforms raw traffic crash records into meaningful safety insights. By combining Python, MySQL, SQL analytics, and Streamlit visualization, the project enables data-driven decision-making for traffic management, accident prevention, and public safety improvement.

