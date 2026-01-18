# How to Create and Use Variables in Grafana

This guide walks you through creating a **query-based variable** in Grafana and using it to dynamically filter data from a **PostgreSQL** data source.

---

## Step 1: Open a Dashboard

- Open any existing Grafana dashboard  
- Or create a new dashboard if you do not have one yet

---

## Step 2: Open Variable Settings

1. Click **Edit** in the top-right corner to enter edit mode  
2. Click **Dashboard settings (⚙️)** in the top toolbar  
3. Select **Variables** from the left-side menu  
4. Click **+ Add variable**

---

## Step 3: Create a Hostname Variable

In the variable configuration panel, set the following values:

- **Type**: `Query`  
- **Name**: `hostname`  
- **Label**: `Device Name`  
- **Data source**: `PostgreSQL`  
- **Query**:

```sql
SELECT hostname
FROM network_devices
ORDER BY hostname;
```

- Click **Apply**

✅ A **Device Name dropdown** will now appear at the top of your dashboard.

---

## Step 4: Use the Variable in a Panel Query

1. Add a new panel or edit an existing panel  
2. Use the variable in your SQL query:

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
WHERE hostname IN ($hostname);
```

3. Click **Apply**

Grafana automatically replaces `$hostname` with the value selected in the dropdown.

---

## Step 5: Filter Data Using the Dropdown

- Select one or more hostnames from the dropdown  
- The panel updates instantly based on your selection

---

## Step 6: Select the Appropriate Panel Type

- Use a **Table** panel to clearly display device and inventory details

---

## Simple Explanation

Grafana variables allow you to make dashboards **interactive**.  
Instead of editing SQL queries manually, you can filter PostgreSQL data using dropdowns that control your queries dynamically.

---

## ⚠️ Important Security Note

Avoid displaying **username** and **password** fields in dashboards unless this is strictly for **lab, demo, or testing purposes**.  
For production environments, always follow proper credential management and security best practices.
