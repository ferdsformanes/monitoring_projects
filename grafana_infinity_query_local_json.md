# Querying a Local JSON Endpoint in Grafana Using Infinity Datasource

This guide explains how to query a local HTTP JSON endpoint (`http://localhost:8000/metrics`) in Grafana using the **Infinity datasource**, which is the recommended approach for table-based JSON data.

---

## Option A: Use Infinity Datasource (JSON → Table)

### 1. Install Infinity Datasource

1. Open Grafana
2. Go to **Administration → Plugins**
3. Search for **Infinity**
4. Click **Install**
5. Restart Grafana if prompted

---

### 2. Add Infinity as a Data Source

1. Go to **Connections → Data sources**
2. Click **Add data source**
3. Select **Infinity**
4. Click **Save & Test**

No authentication is required for `localhost`.

---

### 3. Create a New Dashboard

1. Go to **Dashboards → New**
2. Click **New dashboard**
3. Select **Add visualization**
4. Choose **Infinity** as the data source

---

### 4. Configure the Query

- **Query Type:** JSON
- **Source:** URL
- **Method:** GET
- **URL:**
  ```
  http://localhost:8000/metrics
  ```

---

### 5. Configure Parsing Options

Under **Parsing options**:

- **Format:** Table
- **Root Selector:** Leave empty (the endpoint returns a JSON array)

Example response format:
```json
[
  {
    "hostname": "edge-1",
    "system_ip": "10.10.10.1",
    "status": "connected"
  }
]
```

Grafana will automatically map each JSON field to a table column.

---

### 6. Set Visualization to Table

1. In the visualization panel, select **Table**
2. Verify that rows and columns appear correctly

Expected columns may include:
- hostname
- system_ip
- device_type
- site_id
- status
- reachability
- version
- uptime

---

### 7. Optional Table Enhancements

- Add **value mappings** for status (e.g., connected / disconnected)
- Apply **color thresholds**
- Sort by hostname or site ID
- Filter unreachable devices

---

## Important Notes

- Do **not** use the Prometheus datasource for this endpoint
- Prometheus only supports metrics (`text/plain`)
- JSON endpoints are meant to be queried directly by Grafana

---

## Architecture Reminder

- Flask: Data collection
- Prometheus: Metrics only
- Grafana: Visualization (metrics + JSON)

This separation keeps your monitoring stack clean and scalable.
