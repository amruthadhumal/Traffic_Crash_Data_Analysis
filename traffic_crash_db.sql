USE traffic_crash_db;
SELECT * FROM traffic_crash_data;
SELECT count(*) FROM traffic_crash_data;

-- Query-1 : Find the top 5 most dangerous combinations of weather and crash type based on total crashes.

SELECT WEATHER_CONDITION, CRASH_TYPE, COUNT(*) AS total_crashes
FROM traffic_crash_data
WHERE INJURIES_TOTAL > 0
GROUP BY WEATHER_CONDITION, CRASH_TYPE
ORDER BY total_crashes DESC
LIMIT 5;

-- Query-2 : Identify the top 10 streets with the highest number of injury crashes

SELECT STREET_NO,STREET_DIRECTION,STREET_NAME,CRASH_TYPE, COUNT(INJURIES_TOTAL) as total_injuries 
FROM traffic_crash_data 
WHERE INJURIES_TOTAL > 0 
GROUP BY STREET_NO,STREET_DIRECTION,STREET_NAME,CRASH_TYPE
ORDER BY COUNT(INJURIES_TOTAL) DESC 
LIMIT 10;


-- Query-3 : Find the percentage of crashes that resulted in injuries for each crash type

SELECT CRASH_TYPE, 
       COUNT(*) AS total_crashes, 
	   SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) AS injury_crashes,
	   ROUND(100.0 * SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) / COUNT(*),2) AS injury_crashes_percentage
FROM traffic_crash_data
GROUP BY CRASH_TYPE
ORDER BY injury_crashes_percentage DESC;

-- Query-4 : Determine the peak crash hour for each month

WITH monthly_crash_hours AS
(SELECT CRASH_MONTH,CRASH_HOUR,COUNT(*) AS crash_count,
 ROW_NUMBER() OVER(PARTITION BY CRASH_MONTH ORDER BY COUNT(*) DESC) AS rn
 FROM traffic_crash_data GROUP BY CRASH_MONTH,CRASH_HOUR
)

SELECT CRASH_MONTH, CRASH_HOUR AS peak_hour, crash_count
FROM monthly_crash_hours
WHERE rn=1
ORDER BY CRASH_MONTH;


-- Query-5 : Find the top 5 primary causes of crashes during night time (CRASH_HOUR ≥ 18)

SELECT PRIM_CONTRIBUTORY_CAUSE,COUNT(*) AS total_crashes
FROM traffic_crash_data
WHERE CRASH_HOUR > 18
GROUP BY PRIM_CONTRIBUTORY_CAUSE
ORDER BY total_crashes DESC
LIMIT 5;



-- Query-6 : Compare average number of injuries in daylight vs darkness conditions

SELECT LIGHTING_CONDITION, ROUND(AVG(INJURIES_TOTAL),2) AS avg_injuries
FROM traffic_crash_data
WHERE LIGHTING_CONDITION IN('DAYLIGHT','DARKNESS') AND INJURIES_TOTAL > 0
GROUP BY LIGHTING_CONDITION
ORDER BY avg_injuries DESC;
      

-- Query-7 : Find which traffic control device type has the highest average injuries per crash

SELECT TRAFFIC_CONTROL_DEVICE,
       ROUND(AVG(INJURIES_TOTAL),2) AS avg_injuries_per_crash
FROM traffic_crash_data
GROUP BY TRAFFIC_CONTROL_DEVICE
ORDER BY avg_injuries_per_crash DESC
LIMIT 1;


-- Query-8 : Identify the top 5 locations (latitude/longitude) with the highest crash frequency.

SELECT STREET_NO,STREET_DIRECTION,STREET_NAME,LOCATION,LATITUDE,LONGITUDE,COUNT(*) AS total_crashes
FROM traffic_crash_data
GROUP BY STREET_NO,STREET_DIRECTION,STREET_NAME,LOCATION,LATITUDE,LONGITUDE
ORDER BY total_crashes DESC
LIMIT 5;


-- Query-9 : Find the top 5 streets with the highest injury rate, considering only streets with more than 100 crashes

SELECT
    STREET_NAME,
    COUNT(*) AS total_crashes,
    SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) AS injury_crashes,
    ROUND(100.0 * SUM(CASE WHEN INJURIES_TOTAL > 0 THEN 1 ELSE 0 END) / COUNT(*),2) AS injury_rate_percentage
FROM traffic_crash_data
GROUP BY STREET_NAME
Having COUNT(*) > 100
ORDER BY injury_rate_percentage DESC
LIMIT 5;


-- Query-10 : For each year, identify the most common crash type. 

WITH crash_counts AS ( 
       SELECT YEAR, CRASH_TYPE, COUNT(*) AS total_crashes,
	   RANK() OVER (PARTITION BY YEAR
	   ORDER BY COUNT(*) DESC
	  ) AS rank_num
    FROM traffic_crash_data
    GROUP BY 
        YEAR,
        CRASH_TYPE
)
SELECT YEAR, CRASH_TYPE, total_crashes
FROM crash_counts
WHERE rank_num = 1
ORDER BY YEAR DESC;

-- Query-11 : Find the day of the week with the highest average crashes per hour

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
GROUP BY CRASH_DAY_OF_WEEK,CRASH_HOUR
ORDER BY avg_crashes_per_hour DESC;

-- Query-12 : Identify high-risk time slots:
-- Group hours into buckets (Morning, Afternoon, Evening, Night)
-- Find which bucket has the highest injury crashes

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
ORDER BY injury_crashes DESC;  

-- Query-13 : Find the top 3 contributing causes for each crash type.
-- (Use window functions like ROW_NUMBER() or RANK())
WITH contributing_cause AS ( 
       SELECT PRIM_CONTRIBUTORY_CAUSE, SEC_CONTRIBUTORY_CAUSE, CRASH_TYPE, COUNT(*) AS total_crashes,
	   ROW_NUMBER() OVER (PARTITION BY CRASH_TYPE ORDER BY COUNT(*) DESC) AS rn
    FROM traffic_crash_data
    GROUP BY 
        PRIM_CONTRIBUTORY_CAUSE,
        SEC_CONTRIBUTORY_CAUSE,
        CRASH_TYPE
)
SELECT PRIM_CONTRIBUTORY_CAUSE, SEC_CONTRIBUTORY_CAUSE, CRASH_TYPE, total_crashes
FROM contributing_cause
WHERE rn <= 3
ORDER BY total_crashes DESC
LIMIT 3;


-- Query-14 : Calculate the year-over-year growth rate of crashes.
-- (Use LAG() window function)
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
    FROM 
        yearly_crashes
)
SELECT
    YEAR,
    total_crashes,
    previous_year_crashes,
    ROUND((
          (total_crashes - previous_year_crashes)
          * 100.0) / previous_year_crashes,
        2) AS yoy_growth_rate_percentage
FROM previous_year_data
ORDER BY YEAR;


-- Query-15 : Identify hotspot zones:
-- Group nearby locations (round latitude & longitude to 2 decimal places)
-- Find top 10 zones with highest crashes

SELECT 
    ROUND(LATITUDE, 2) AS latitude_zone,
    ROUND(LONGITUDE, 2) AS longitude_zone,
    COUNT(*) AS total_crashes
FROM traffic_crash_data
GROUP BY 
    ROUND(LATITUDE, 2),
    ROUND(LONGITUDE, 2)
ORDER BY total_crashes DESC
LIMIT 10;
 
        
