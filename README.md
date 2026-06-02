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

Data Set Link: <a href="https://drive.google.com/file/d/1jAFsxF8ri--wYC1A-8k_Otdlf8xfcODN/view?usp=sharing">Traffic_CrashesData</a>

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

<img width="1390" height="524" alt="image" src="https://github.com/user-attachments/assets/d1d23242-f684-47bc-af3e-89421a0b8e60" />

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

<img width="1367" height="783" alt="image" src="https://github.com/user-attachments/assets/b22c9273-6149-4531-9234-7a10292c3491" />

________________________________________
### Query 3
Injury Percentage by Crash Type
#### Objective
Calculate:
(Injury Crashes / Total Crashes) × 100
for every crash type.
#### Business Value
Highlights crash types that are most dangerous.

<img width="1380" height="409" alt="image" src="https://github.com/user-attachments/assets/e57c0653-1ea6-4f90-8d51-6f07322ecff2" />

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

<img width="1377" height="793" alt="image" src="https://github.com/user-attachments/assets/274a7ad9-df56-41e2-a0c1-b5bddcf07902" />

________________________________________
### Query 5
Top Night-Time Crash Causes
#### Objective
Analyze crashes occurring after 6 PM.
#### Business Value
Identifies risky behaviours during night driving.

<img width="1378" height="574" alt="image" src="https://github.com/user-attachments/assets/42670368-1661-441b-8782-a90be82663d3" />

________________________________________
### Query 6
Daylight vs Darkness Injury Comparison
#### Objective
Compare average injuries under:

•	Daylight

•	Darkness

#### Business Value
Evaluates the impact of lighting conditions on crash severity.

<img width="1389" height="429" alt="image" src="https://github.com/user-attachments/assets/4ac95094-c12e-4272-bb35-15f836497539" />

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

<img width="1377" height="360" alt="image" src="https://github.com/user-attachments/assets/13b7e233-f000-468b-9e01-2db410728b93" />

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

<img width="1359" height="551" alt="image" src="https://github.com/user-attachments/assets/5131e5dd-5b3f-48c2-8fd4-f3531c717640" />

________________________________________
### Query 9
Streets with Highest Injury Rate
#### Objective
Find streets where crashes are most likely to cause injuries.
constraint only streets with, more than 100 crashes are considered.
#### Business Value
Improves prioritization of safety interventions.

<img width="1366" height="519" alt="image" src="https://github.com/user-attachments/assets/54f52a03-8db9-4ef5-8594-a1bb2b8e2f37" />

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

<img width="1363" height="612" alt="image" src="https://github.com/user-attachments/assets/db08e7b1-a61d-4008-857a-59caaeb6248d" />

________________________________________
### Query 11
Day of Week with Highest Average Crashes
### Objective
Determine which weekday experiences the highest average crashes per hour.
### Business Value
Supports scheduling of enforcement and monitoring activities.

<img width="1363" height="636" alt="image" src="https://github.com/user-attachments/assets/f6ea7151-330f-46ce-b9c1-ab3e6b48c4be" />

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

<img width="1376" height="480" alt="image" src="https://github.com/user-attachments/assets/a20fa466-b988-48d6-8e65-3c95ece27fdb" />

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

<img width="1367" height="454" alt="image" src="https://github.com/user-attachments/assets/b46db581-6f88-4d15-945f-5b0bf219b6dc" />

________________________________________
### Query 14
Year-over-Year Crash Growth Rate
#### Objective
Measure annual crash growth.

#### Techniques Used

LAG()

#### Business Value
Tracks whether road safety is improving or worsening.

<img width="1356" height="608" alt="image" src="https://github.com/user-attachments/assets/5c8c649a-15ef-480a-96de-554f828997cc" />

________________________________________
### Query 15
Crash Hotspot Zones
#### Objective
Group nearby locations by rounding:

Latitude → 2 decimal places

Longitude → 2 decimal places

#### Business Value
Identifies geographic clusters with high accident frequency.

<img width="1360" height="761" alt="image" src="https://github.com/user-attachments/assets/76c9b511-8962-4268-8256-acadb599b1df" />

________________________________________

## 📈 SQL Concepts Demonstrated

This project showcases advanced SQL techniques including:

* Common Table Expressions (CTEs)
* Aggregate Functions - GROUP BY & HAVING
* Window Functions - ROW_NUMBER(),RANK(),LAG()
* Subqueries
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

