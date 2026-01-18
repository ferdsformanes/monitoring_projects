# How to Use Variables in Grafana (PostgreSQL -- Simple Steps)

## Step 1: Open a Dashboard

-   Open any Grafana dashboard

## Step 2: Add a Variable

1.  Click **Dashboard settings (⚙️)**
2.  Click **Variables**
3.  Click **Add variable**

## Step 3: Create the Hostname Variable

-   **Name**: `hostname`
-   **Type**: `Query`
-   **Data source**: `PostgreSQL`
-   **Query**:

``` sql
SELECT hostname FROM network_devices ORDER BY hostname;
```

-   Click **Apply**

A hostname dropdown appears at the top of the dashboard.

## Step 4: Use the Variable in a Panel

1.  Add or edit a panel
2.  Use this SQL query:

``` sql
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

3.  Click **Apply**

## Step 5: Select from the Dropdown

-   Select a hostname from the dropdown
-   The panel updates automatically

## Step 6: Choose the Right Panel Type

-   Use **Table panel** to display device details

## Simple Explanation

Grafana variables let you filter PostgreSQL data using a dropdown
instead of editing SQL.

## Important Note

Avoid showing **username and password** in dashboards unless this is
strictly for lab or demo use.
