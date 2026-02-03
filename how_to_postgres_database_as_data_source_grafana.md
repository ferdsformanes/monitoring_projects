# Add PostgreSQL as a Data Source in Grafana 12 (Step-by-Step)

This guide walks you through adding **PostgreSQL** as a data source in **Grafana 12** using the Grafana UI.

---

## Prerequisites

Before you start, make sure you have:

- Grafana **v12.x** installed and running
- PostgreSQL running and accessible from the Grafana server
- PostgreSQL credentials:
  - Host
  - Port (default: `5432`)
  - Database name
  - Username
  - Password
- A Grafana user with **Admin** or **Editor** permissions

---

## Step 1: Log in to Grafana

1. Open your browser.
2. Go to:
   ```
   http://localhost:3000
   ```
   (or your Grafana server URL)
3. Log in using your Grafana credentials.

---

## Step 2: Open Data Sources

1. In the left sidebar, click **Connections**.
2. Select **Data sources**.
3. Click **Add new data source**.

---

## Step 3: Select PostgreSQL

1. In the list of available data sources, search for **PostgreSQL**.
2. Click **PostgreSQL**.

Grafana will open the PostgreSQL configuration page.

---

## Step 4: Configure PostgreSQL Connection

Fill in the following fields:

### Connection Details

- **Host**
  ```
  localhost:5432
  ```
  (Replace with your PostgreSQL host and port)

- **Database**
  ```
  your_database_name
  ```

- **User**
  ```
  your_username
  ```

- **Password**
  ```
  your_password
  ```

> Tip: Click **Save & test** later to verify credentials.

---

## Step 5: Configure PostgreSQL Options

### SSL Mode
Choose one based on your setup:
- `disable` â Local or non-SSL connections
- `require` â Common for production environments

### TimescaleDB (Optional)
- Enable **TimescaleDB** only if your PostgreSQL uses TimescaleDB extensions.

---

## Step 6: Set Time Column Defaults (Recommended)

In the **PostgreSQL details** section:

- **Time column name**
  ```
  time
  ```
  (or your actual timestamp column)

- **Metric column**
  ```
  none
  ```
  (Used mainly for legacy queries)

---

## Step 7: Save and Test

1. Click **Save & test**.
2. If successful, you will see:
   ```
   Database Connection OK
   ```

If it fails, double-check:
- Host and port
- Credentials
- Firewall or network access
- PostgreSQL `pg_hba.conf` settings

---

## Step 8: Use PostgreSQL in a Dashboard

1. Go to **Dashboards** â **New** â **New dashboard**.
2. Click **Add visualization**.
3. Select **PostgreSQL** as the data source.
4. Write your SQL query.

### Example Query

```sql
SELECT
  NOW() as time,
  COUNT(*) as value
FROM users;
```

---

## Notes & Best Practices

- Use indexed timestamp columns for better performance
- Avoid `SELECT *` in dashboards
- Limit time ranges when querying large tables
- Use views for complex queries

---

## Youâre All Set ð

Your PostgreSQL data source is now connected to Grafana 12 and ready for dashboards and visualizations.
