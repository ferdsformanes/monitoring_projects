# How to Create and Use Variables in Grafana

This guide walks you through creating a **query-based variable** in Grafana and using it to dynamically filter data from a **PostgreSQL** data source.

---

## Grafana Variable Syntax (SQL Data Sources)

Grafana variables are referenced using the `$variable_name` syntax and are resolved at query execution time.

### Basic Variable Usage

```sql
WHERE hostname IN ($hostname)
```

### How It Works

* `$hostname` is a **dashboard variable**
* Grafana replaces the variable with the selected value(s) from the dropdown
* The `IN` clause supports:

  * Single value selection
  * Multiple value selection
  * “All” option (if enabled)

### Important Notes

* Do **not** wrap the variable in quotes
  Grafana automatically formats values correctly for SQL
* Use `IN` instead of `=` to prevent errors when multiple values are selected

---

## Step 1: Open a Dashboard

* Open any existing Grafana dashboard
* Or create a new dashboard if you do not have one yet

---

## Step 2: Open Variable Settings

1. Click **Edit** in the top-right corner to enter edit mode
2. Click **Dashboard settings (⚙️)** in the top toolbar
3. Select **Variables** from the left-side menu
4. Click **+ Add variable**

---

## Step 3: Create a Hostname Variable

In the variable configuration panel, set the following values:

* **Type**: `Query`
* **Name**: `hostname`
* **Label**: `Device Name`
* **Data source**: `PostgreSQL`
* **Query**:

```sql
SELECT hostname
FROM network_devices
ORDER BY hostname;
```

* Click **Apply**

A **Device Name dropdown** will now appear at the top of your dashboard.

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

* Select one or more hostnames from the dropdown
* The panel updates instantly based on your selection

---

## Step 6: Select the Appropriate Panel Type

* Use a **Table** panel to clearly display device and inventory details
