# Adding PostgreSQL as a Data Source in Grafana 12

This guide walks you through connecting a PostgreSQL database to Grafana 12 as a data source.

---

## Prerequisites

- Grafana 12 installed and running.
- PostgreSQL database credentials:
  - Hostname / IP
  - Port (default 5432)
  - Database name
  - Username
  - Password
- Ensure Grafana server can reach the PostgreSQL server.

---

## Steps

### 1. Log in to Grafana

1. Open your browser.
2. Go to `http://<grafana-server-ip>:3000/`.
3. Enter your Grafana username and password.
4. Click **Log in**.

---

### 2. Open the Data Sources Settings

1. Click the **gear icon** (⚙️) on the left-hand menu.
2. Select **Data Sources**.

---

### 3. Add a New Data Source

1. Click **Add data source** (top right corner).
2. In the list of data source types, select **PostgreSQL**.

---

### 4. Configure PostgreSQL Connection

Fill in the following fields:

| Field                  | Description                                                      |
|------------------------|------------------------------------------------------------------|
| Name                   | Give a name for the data source (e.g., `PostgreSQL_DB`).         |
| Host                   | PostgreSQL host and port, e.g., `localhost:5432`.                |
| Database               | The name of your PostgreSQL database.                             |
| User                   | PostgreSQL username.                                              |
| Password               | PostgreSQL password.                                              |
| SSL Mode               | Choose appropriate mode: `disable`, `require`, or `verify-full`. |

> **Tip:** If Grafana runs on the same machine as PostgreSQL, `localhost:5432` usually works.

---

### 5. Set Advanced Options (Optional)

- **Max Open Connections**: Limits concurrent connections.
- **Max Idle Connections**: Controls idle connections.
- **Connection Max Lifetime**: Optional, usually default is fine.

---

### 6. Test Connection

1. Scroll down and click **Test connection**.
2. If everything is correct, you’ll see: