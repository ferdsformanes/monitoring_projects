# Adding PostgreSQL as a Data Source in Grafana 1

This guide shows how to add a PostgreSQL database as a data source in Grafana, using a local database running on port **5433**.

---

## Prerequisites

- Grafana 12 is installed and running
- PostgreSQL 17 running and accessible
- Database connection details:

| Setting        | Value        |
|---------------|--------------|
| Host           | localhost    |
| Port           | 5433         |
| Database name  | testdb       |
| Username       | postgres     |
| Password       | postgres     |
| TLS/SSL Mode   | disable      |

---

## Step-by-Step Instructions

### 1. Log in to Grafana

1. Open a browser.
2. Go to:

```
http://localhost:3000
```

3. Log in with your Grafana credentials.

---

### 2. Open Data Sources

1. Click the **Settings (⚙️)** icon on the left sidebar.
2. Select **Data Sources**.
3. Click **Add data source**.

---

### 3. Select PostgreSQL

1. From the list of available data sources, click **PostgreSQL**.

---

### 4. Configure PostgreSQL Connection

Fill in the fields exactly as follows:

#### Basic Settings

| Field | Value |
|-----|------|
| **Name** | PostgreSQL_TestDB |
| **Host** | localhost:5433 |
| **Database** | testdb |
| **User** | postgres |
| **Password** | postgres |

---

### 5. Configure TLS / SSL

Under **TLS/SSL Mode**, select:

```
disable
```

---

### 6. PostgreSQL Version

- Grafana will automatically detect the PostgreSQL version.
- PostgreSQL **17-1** works without additional configuration.

---

### 7. (Optional) Connection Limits

You may leave these at default values:

- Max open connections
- Max idle connections
- Connection max lifetime

---

### 8. Test the Connection

1. Scroll down.
2. Click **Test connection**.

If successful, you will see:

```
Data source is working
```

---

### 9. Save the Data Source

1. Click **Save & test**.
2. PostgreSQL is now ready for use in dashboards.

---

## Using PostgreSQL in a Dashboard

1. Go to **Dashboards** → **New dashboard**.
2. Click **Add panel**.
3. Select **PostgreSQL_TestDB** as the data source.
4. Example SQL query:

```sql
SELECT
  NOW() as time,
  count(*) as value
FROM your_table;
```

5. Choose a visualization.
6. Save the dashboard.

---

## Notes

- Port **5433** is non-default; ensure PostgreSQL is listening on this port.
- If Grafana and PostgreSQL are on different machines, replace `localhost` with the PostgreSQL server IP.
- Authentication issues usually relate to credentials or `pg_hba.conf`.

---

## Reference

https://grafana.com/docs/grafana/latest/datasources/postgres/
