# How to Install Infinity Plugin in Grafana

## 1. Install Infinity Plugin via Grafana UI
1. Log in to your Grafana instance.
2. Navigate to **Administration → Plugins** (or **Configuration → Plugins**).
3. Search for **Infinity**.
4. Click on **Infinity (yesoreyeram-infinity-datasource)**.
5. Click **Install Plugin**.
6. Restart Grafana if prompted.

---

## 2. Add Infinity as a Data Source
1. Go to **Configuration → Data Sources → Add data source**.
2. Search for **Infinity** and select it.
3. Configure:
   - **Name**: e.g., `Infinity`
   - **Allowed URLs**: Add the API or file URLs you want to query.
4. Click **Save & Test**.

---

## 3. Create a Dashboard Using Infinity
1. Go to **Dashboards → New → New Dashboard**.
2. Click **Add a new panel**.
3. In the **Query section**:
   - Select **Infinity** as the data source.
   - Choose **Query Type** (JSON, CSV, XML, etc.).
   - Enter the **URL or inline data**.
   - Configure parsing options (e.g., JSONPath, CSV delimiter).
4. Click **Apply** and **Save the dashboard**.

---

### Example JSON Query
If you have an API returning JSON:
```json
[
  {"name": "Server1", "status": "up"},
  {"name": "Server2", "status": "down"}
]
```
Infinity query settings:
- **Type**: JSON
- **Source**: URL
- **URL**: `https://your-api-endpoint`
- **Root Selector**: `$`

