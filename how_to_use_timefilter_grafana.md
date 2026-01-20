# How to Use $__timeFilter() in Grafana (Time Series Panel)

This guide walks you through using `$__timeFilter()` to make your queries time-aware, so the **time picker controls the X-axis** in a time series panel.

---

## Step 1: Open or Create a Dashboard

- Open an existing Grafana dashboard, **or create a new dashboard**
- Click **Add panel** to start

---

## Step 2: Select a Time Series Panel

1. Choose **Time series** as the visualization type
2. Select a data source (we’ll use **TestData DB** for this example)

---

## Step 3: Use a Query with `$__timeFilter()`

In the panel query editor, use the **TestData DB table `random walk`** or any time series metric.

Example using **PostgreSQL** syntax:

```sql
SELECT
  time AS "time",
  value
FROM random_walk
WHERE $__timeFilter(time)
```

### Notes:
- `time AS "time"` → this column becomes the X-axis  
- `$__timeFilter(time)` → limits results to the dashboard’s selected time range

> In **TestData DB**, you can just use:
```sql
SELECT
  "time",
  "value"
FROM "random walk"
WHERE $__timeFilter("time")
```

---

## Step 4: Apply and Check the Panel

- Click **Apply**  
- Grafana will plot the time series for the selected time range  
- The **X-axis shows timestamps**, Y-axis shows values

---

## Step 5: Test the Time Picker

1. Change the **dashboard time picker** to:
   - Last 5 minutes  
   - Last 24 hours  
   - Custom range
2. The graph **updates automatically** according to the selected time range

> This shows `$__timeFilter()` is working correctly.

---

## Step 6: Optional — Group Data by Time Intervals

For smoother graphs, especially with PostgreSQL:

```sql
SELECT
  time_bucket('1 hour', time) AS "time",
  AVG(value) AS avg_value
FROM random_walk
WHERE $__timeFilter(time)
GROUP BY 1
ORDER BY 1
```

- `time_bucket('1 hour', time)` → groups values into 1-hour intervals  
- `$__timeFilter(time)` ensures only the selected time range is returned  
- `GROUP BY` and `ORDER BY` ensure the graph plots correctly

---

## Step 7: Save the Dashboard

- Click **Apply** in the panel editor  
- Save the dashboard  
- Now the time picker dynamically controls your **X-axis** and the displayed data

---

## ✅ Key Points

- `$__timeFilter()` links the **dashboard time picker** to your SQL query  
- Always use a column named `"time"` for the X-axis  
- Works with **time series panels** and **table panels**  
- Essential for dynamic dashboards and proper Grafana performance

