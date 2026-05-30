import streamlit as st
import pandas as pd
import mysql.connector


# Function to connect to MySQL database
def get_data(query, params=None):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678",
    database = "traffic_crash_db"
   )
    if params:
        df = pd.read_sql_query(query, connection, params=params)
    else:
        df = pd.read_sql_query(query, connection)
    connection.close()
    return df

def get_analysis(analysis):
    return st.write(analysis)


# Streamlit App Title
st.set_page_config(page_title="Traffic Crash Data Analysis", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Project Introduction", "SQL Queries", "Creator Info"])

# -------------------------------- PAGE 1: Introduction --------------------------------
if page == "Project Introduction":
    st.title("Traffic Crash Data Analysis")
    st.subheader("📊 A Streamlit App for Exploring Traffic Crash Data")
    st.write("""
    This project analyzes traffic crash data from different locations using MySQL database.
    It provides query results for locations, peak crash times, crashes per year, and other traffic crashes parameters.
    
    **Features:**
    - Analyze crash data using advanced SQL techniques
    - Identify patterns, trends, and risk factors
    - Run predefined SQL queries to explore insights.
    
    **Database Used:** 'traffic_crash_db'
    """)

# -------------------------------- PAGE 3: SQL Queries --------------------------------
elif page == "SQL Queries":
    st.title("📋 SQL Query Results")

    analysis = {

        "1. Top Weather and Crash Type Combinations Causing Most Injuries":""" The report shows which weather conditions and crash types cause the highest number of injury crashes, helping identify the most risky driving situations. """,
        "2. Top 10 Streets with Highest Injury Crash Counts": """ The analysis highlights the streets with the highest number of injury crashes, helping identify accident-prone areas that may need better traffic control and road safety improvements.""",
        "3. Injury Rate Percentage by Crash Type": """ The analysis shows which crash types are most likely to cause injuries, helping prioritize safety measures for the most dangerous accident types.""",
        "4. Monthly Peak Crash Hour Analysis": """ The analysis identifies the busiest crash hours for each month, helping understand when accidents are most likely to happen throughout the year.
These peak crash periods can help traffic authorities plan better road safety measures.""",
        "5. Top Night-Time Contributing Causes of Crashes": """ The analysis reveals the most common causes of crashes during night hours, helping identify risky driving behaviors and conditions after evening time.
These insights can help authorities improve nighttime road safety through better lighting and driver awareness programs.""",
        "6. Injury Comparison: Daylight vs Darkness Conditions": """The comparison shows how lighting conditions affect crash injuries, helping understand whether accidents in darkness are more severe than those in daylight.
These insights can support better road lighting, nighttime safety measures. """,
        "7. Traffic Control Devices with Highest Average Injuries per Crash": """ The analysis identifies which traffic control device is linked to the highest average injuries per crash, helping authorities focus on improving safety measures at those locations.""",
        "8. Top 5 High Crash Frequency Locations (Latitude/Longitude)": """The analysis identifies the locations with the highest number of crashes, helping authorities prioritize high-risk areas for traffic management and road improvements """,
        "9. Streets with Highest Injury Rate (100+ Crash Filter)": """ The analysis highlights streets where crashes are most likely to result in injuries, helping authorities focus on improving safety measures in high-risk road areas.""",
        "10. Most Common Crash Type by Year": """ The analysis shows the most common crash type each year, helping identify recurring accident patterns and areas where road safety efforts should be focused.""",
        "11. Day of Week with Highest Average Hourly Crashes": """ The analysis shows which day of the week has the highest crash activity per hour, helping identify the most accident-prone days for better traffic control and safety planning.""",
        "12. High-Risk Time Slot Analysis Based on Injury Crashes": """ The analysis shows which time of day has the most injury crashes, helping authorities focus safety measures during the most risky hours.""",
        "13. Top Contributing Causes for Each Crash Type": """ The analysis shows the main causes behind each type of crash, helping identify the most common reasons accidents happen so safety measures can be improved.""",
        "14. Year-over-Year Crash Growth Rate Analysis": """ The analysis shows whether crash numbers are increasing or decreasing each year, helping track road safety trends over time.""",
        "15. Top 10 Crash Hotspot Areas Based on Nearby Locations": """ The analysis shows the top 10 crash hotspot zones where accidents happen most often, helping authorities focus on improving road safety in those specific areas."""

    }
    
    queries = {
        "1. Top Weather and Crash Type Combinations Causing Most Injuries":
        """
          SELECT
             WEATHER_CONDITION, 
             CRASH_TYPE, 
             COUNT(*) AS TOTAL_CRASHES
                   FROM traffic_crash_data
                   WHERE INJURIES_TOTAL > 0
                   GROUP BY WEATHER_CONDITION, 
                            CRASH_TYPE
                   ORDER BY TOTAL_CRASHES DESC
                   LIMIT 5
        """,
        

        "2. Top 10 Streets with Highest Injury Crash Counts": 
        """ 
            SELECT STREET_NO,
                       STREET_DIRECTION,
                       STREET_NAME,
                       CRASH_TYPE, 
                       count(INJURIES_TOTAL) as total_injuries 
                FROM traffic_crash_data 
                WHERE INJURIES_TOTAL > 0 
                GROUP BY STREET_NO,
                         STREET_DIRECTION,
                         STREET_NAME,
                         CRASH_TYPE
                ORDER BY count(INJURIES_TOTAL) DESC 
                LIMIT 10
        """,
        
        "3. Injury Rate Percentage by Crash Type": 
        """ 
            SELECT CRASH_TYPE, 
                   COUNT(*) AS total_crashes, 
	               SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) AS injury_crashes,
	               ROUND(100.0 * SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) / COUNT(*),2) AS injury_crashes_percentage
            FROM traffic_crash_data
            GROUP BY CRASH_TYPE
            ORDER BY injury_crashes_percentage DESC;
        """,


        "4. Monthly Peak Crash Hour Analysis": 
        """   
            WITH monthly_crash_hours AS
                (SELECT CRASH_MONTH,
                        CRASH_HOUR,
                        COUNT(*) AS crash_count,
                 ROW_NUMBER() OVER(PARTITION BY CRASH_MONTH ORDER BY COUNT(*) DESC) AS rn
                 FROM traffic_crash_data 
                 GROUP BY CRASH_MONTH,CRASH_HOUR
            )

            SELECT CRASH_MONTH, 
                   CRASH_HOUR AS peak_hour, 
                   crash_count
            FROM monthly_crash_hours
            WHERE rn=1
            ORDER BY CRASH_MONTH
        """,


        "5. Top Night-Time Contributing Causes of Crashes": 
        """     
            SELECT PRIM_CONTRIBUTORY_CAUSE,
                   COUNT(*) AS total_crashes
            FROM traffic_crash_data
            WHERE CRASH_HOUR > 18
            GROUP BY PRIM_CONTRIBUTORY_CAUSE
            ORDER BY total_crashes DESC
            LIMIT 5
        """,

        "6. Injury Comparison: Daylight vs Darkness Conditions": 
        """    
            SELECT LIGHTING_CONDITION, 
                  ROUND(AVG(INJURIES_TOTAL),2) AS avg_injuries
            FROM traffic_crash_data
            WHERE LIGHTING_CONDITION IN('DAYLIGHT','DARKNESS')
            GROUP BY LIGHTING_CONDITION 
        """,

         "7. Traffic Control Devices with Highest Average Injuries per Crash": 
        """   
            SELECT TRAFFIC_CONTROL_DEVICE,
                   ROUND(AVG(INJURIES_TOTAL),2) AS avg_injuries_per_crash
            FROM traffic_crash_data
            GROUP BY TRAFFIC_CONTROL_DEVICE
            ORDER BY avg_injuries_per_crash DESC
            LIMIT 1
        """,

         "8. Top 5 High Crash Frequency Locations (Latitude/Longitude)": 
        """     
            SELECT 
                   STREET_NO,
                   STREET_DIRECTION,
                   STREET_NAME,
                   LOCATION,
                   LATITUDE,
                   LONGITUDE,
                   COUNT(*) AS total_crashes
            FROM traffic_crash_data
            GROUP BY 
                    STREET_NO,
                    STREET_DIRECTION,
                    STREET_NAME,
                    LOCATION,
                    LATITUDE,
                    LONGITUDE
            ORDER BY total_crashes DESC
            LIMIT 5
        """,

         "9. Streets with Highest Injury Rate (100+ Crash Filter)": 
        """     
            SELECT STREET_NAME, 
                   COUNT(*) AS total_crashes, 
                   SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) AS injury_crashes,
                   ROUND(100.0 * SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) / COUNT(*),2) AS injury_rate_percentage
            FROM traffic_crash_data
            GROUP BY STREET_NAME
            Having COUNT(*) > 100
            ORDER BY injury_rate_percentage DESC
            LIMIT 5
        """,

         "10. Most Common Crash Type by Year": 
        """     
            WITH crash_counts AS ( 
                SELECT YEAR, 
                        CRASH_TYPE, 
                        COUNT(*) AS total_crashes,
	                    RANK() OVER (PARTITION BY YEAR ORDER BY COUNT(*) DESC) AS rank_num
                FROM traffic_crash_data
                GROUP BY YEAR,CRASH_TYPE
            )
            SELECT YEAR, 
                   CRASH_TYPE,
                   total_crashes
            FROM crash_counts
            WHERE rank_num = 1
            ORDER BY YEAR DESC
        """,

         "11. Day of Week with Highest Average Hourly Crashes": 
        """     
            WITH hourly_crashes AS(
                SELECT CRASH_DAY_OF_WEEK,
                       CRASH_HOUR,
                       COUNT(*) AS crashes_per_hour,
                       ROW_NUMBER() OVER (PARTITION BY CRASH_DAY_OF_WEEK ORDER BY COUNT(*) DESC) AS rn
                FROM traffic_crash_data 
                GROUP BY CRASH_DAY_OF_WEEK,
                         CRASH_HOUR
            )

            SELECT CRASH_DAY_OF_WEEK,
                   CRASH_HOUR,
                   ROUND(AVG(crashes_per_hour), 0) AS avg_crashes_per_hour 
            FROM hourly_crashes 
            WHERE rn=1
            GROUP BY CRASH_DAY_OF_WEEK,
                     CRASH_HOUR
            ORDER BY avg_crashes_per_hour DESC
        """,

        "12. High-Risk Time Slot Analysis Based on Injury Crashes": 
        """     
            SELECT
                  time_bucket,
                  COUNT(*) AS injury_crashes
            FROM (SELECT
                        CASE
                            WHEN CRASH_HOUR BETWEEN 6 AND 11 THEN 'Morning'
                            WHEN CRASH_HOUR BETWEEN 12 AND 17 THEN 'Afternoon'
                            WHEN CRASH_HOUR BETWEEN 18 AND 23 THEN 'Evening'
                            ELSE 'Night'
                        END AS time_bucket
            FROM traffic_crash_data
            WHERE INJURIES_TOTAL > 0
            )AS grouped_times
            GROUP BY time_bucket
            ORDER BY injury_crashes DESC
        """,

        "13. Top Contributing Causes for Each Crash Type": 
        """     
            WITH contributing_cause AS ( 
                SELECT 
                    PRIM_CONTRIBUTORY_CAUSE, 
                    SEC_CONTRIBUTORY_CAUSE, 
                    CRASH_TYPE, 
                    COUNT(*) AS total_crashes,
	                ROW_NUMBER() OVER (PARTITION BY CRASH_TYPE ORDER BY COUNT(*) DESC) AS rn
                FROM traffic_crash_data
                GROUP BY 
                      PRIM_CONTRIBUTORY_CAUSE,
                      SEC_CONTRIBUTORY_CAUSE,
                      CRASH_TYPE
            )
            SELECT 
                  PRIM_CONTRIBUTORY_CAUSE, 
                  SEC_CONTRIBUTORY_CAUSE, 
                  CRASH_TYPE, 
                  total_crashes
            FROM contributing_cause
            WHERE rn <= 3
            ORDER BY total_crashes DESC
            LIMIT 3
        """,

        "14. Year-over-Year Crash Growth Rate Analysis": 
        """     
            WITH yearly_crashes AS (
                SELECT
                      YEAR,
                      COUNT(*) AS total_crashes
                FROM traffic_crash_data
                GROUP BY YEAR
        ),
        previous_year_data AS (
            SELECT 
                YEAR,
                total_crashes,
                LAG(total_crashes) OVER (ORDER BY YEAR) AS previous_year_crashes
            FROM yearly_crashes
        )
        SELECT
              YEAR,
              total_crashes,
              previous_year_crashes,
              ROUND((
                      (total_crashes - previous_year_crashes)
                    * 100.0) / previous_year_crashes,2) AS yoy_growth_rate_percentage
              FROM previous_year_data
              ORDER BY YEAR
        """,
    

    "15. Top 10 Crash Hotspot Areas Based on Nearby Locations":
    """
       SELECT 
            ROUND(LATITUDE, 2) AS latitude_zone,
            ROUND(LONGITUDE, 2) AS longitude_zone,
            COUNT(*) AS total_crashes
        FROM traffic_crash_data
        GROUP BY 
            ROUND(LATITUDE, 2),
            ROUND(LONGITUDE, 2)
        ORDER BY total_crashes DESC
        LIMIT 10
    
    """
   } 
    selected_query = st.selectbox("Choose a Query", list(queries.keys()))
    query_result = get_data(queries[selected_query])
    
    
    st.write("### Query Result:")
    st.dataframe(query_result)

    analysis_result = get_analysis(analysis[selected_query])


# -------------------------------- PAGE 4: Creator Info --------------------------------
elif page == "Creator Info":
    st.title("👩‍💻 Creator of this Project")
    st.write("""
    **Developed by:** Amrutha Dhumal  
    **Skills:** Python, SQL, Data Analysis,Streamlit, Pandas   
    """)