# Adding PostgreSQL Data Source in Grafana

This guide shows how to add a PostgreSQL database as a data source in Grafana, using a local database running on port **5433**.

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
3. Click **Add new data source**.

---

### 3. Select PostgreSQL

1. From the list of available data sources, click **PostgreSQL**.

---

### 4. Configure PostgreSQL Connection

Fill in the fields exactly as follows:

#### Basic Settings

| Setting        | Value        |
|---------------|--------------|
| Name           | grafana-postgresql-datasource |
| Host           | localhost    |
| Port           | 5433         |
| Database name  | testdb       |
| Username       | postgres     |
| Password       | postgres     |
| TLS/SSL Mode   | disable      |

---

### 5. Test the Connection

1. Scroll down.
2. Click **Test connection**.

If successful, you will see:

```
Data source is working
```

---

### 6. Save the Data Source

1. Click **Save & test**.
2. PostgreSQL is now ready for use in dashboards.

---

## Using PostgreSQL in a Dashboard

1. Go to **Dashboards** → **New dashboard**.
2. Click **Add panel**.
3. Select **grafana-postgresql-datasource** as the data source.
4. Example SQL query:

```sql
SELECT * FROM network_devices;
```

5. Choose Table panel.
6. Save the dashboard.

---

## Notes

- Port **5433** is non-default; ensure PostgreSQL is listening on this port.
- If Grafana and PostgreSQL are on different machines, replace `localhost` with the PostgreSQL server IP.
- Authentication issues usually relate to credentials or `pg_hba.conf`.

---

## Reference
https://grafana.com/docs/grafana/latest/datasources/postgres/configure/
