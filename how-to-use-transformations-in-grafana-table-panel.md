# How to Use Transformations in Grafana (Table Panel)

This step-by-step guide explains how to use **Grafana Transformations**
to modify, clean, and format data **after** it is returned from a query.
The example uses a **PostgreSQL table** and a **Table panel**.

------------------------------------------------------------------------

## Step 1: Open or Create a Dashboard

-   Open an existing Grafana dashboard\
-   Or create a new dashboard if needed

------------------------------------------------------------------------

## Step 2: Add or Edit a Table Panel

1.  Click **Add panel** or edit an existing panel\
2.  Select **Table** as the visualization type\
3.  Choose **PostgreSQL** as the data source

------------------------------------------------------------------------

## Step 3: Use the Base SQL Query

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
WHERE hostname IN ($hostname);
```

------------------------------------------------------------------------

## Step 4: Open the Transformations Tab

1.  In the panel editor, click the **Transformations** tab\
2.  Click **Add transformation**

------------------------------------------------------------------------

## Step 5: Organize and Rename Columns

### Transformation: Organize fields

-   Reorder columns\
-   Hide columns\
-   Rename columns

------------------------------------------------------------------------

## Step 9: Apply and Save the Dashboard

-   Click **Apply**
-   Save the dashboard
