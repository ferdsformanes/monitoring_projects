# How to Create Variables in Grafana

## Step 1: Open a Dashboard

* Open any existing Grafana dashboard
  (or create a new one if needed)

## Step 2: Go to Variables Settings

1. Click **Dashboard settings (⚙️)**
2. Select **Variables**
3. Click **Add variable**

## Step 3: Create a Hostname Variable

* **Name**: `hostname`
* **Type**: `Query`
* **Data source**: `PostgreSQL`
* **Query**:

```sql
SELECT hostname FROM network_devices ORDER BY hostname;
```

* Click **Apply**

A **hostname dropdown** will now appear at the top of the dashboard.

## Step 4: Use the Variable in a Panel Query

1. Add a new panel or edit an existing one
2. Use the following SQL query:

```sql
SELECT
  now() AS "time",
  ip_address,
  device_type,
  hostname,
  location,
  username,
  password
FROM network_devices
WHERE hostname = '$hostname';
```

3. Click **Apply**

## Step 5: Filter Data Using the Dropdown

* Select a hostname from the dropdown
* The panel updates automatically based on your selection

## Step 6: Choose the Correct Panel Type

* Use a **Table panel** to display device details clearly

## Simple Explanation

Grafana variables allow you to dynamically filter PostgreSQL data using
dropdowns, instead of manually editing SQL queries every time.

## Important Note

Avoid displaying **username and password** fields in dashboards unless
this is strictly for lab or demo purposes.
