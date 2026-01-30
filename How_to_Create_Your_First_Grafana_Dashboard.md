
# How to Create Your First Grafana Dashboard

This guide helps you build your first **Grafana dashboard** using **fake sample data** from the TestData datasource.

---
## Step 1: Log In to Grafana
- Open your browser and go to your Grafana URL.
- Log in using your credentials.

---
## Step 2: Add a Data Source
1. Click the **menu (☰)** on the left.
2. Go to **Connections → Data sources**.
3. Click **Add data source**.
4. Choose **TestData DB** (this provides *fake* sample data for learning).
5. Click **Save & test**.

---
## Step 3: Create a New Dashboard
1. Open the **menu (☰)** again.
2. Select **Dashboards**.
3. Click **New → New dashboard**.
4. Click **Add visualization**.

---
## Step 4: Add a Time Series Panel
1. Select **TestData DB** as your datasource.
2. Set the **Scenario** to **Random Walk**. This generates **fake simulated data** that looks like a real metric.
3. Set an **Alias** such as **“Simulated Metric”** to indicate the data is not real.
4. You should now see the generated sample data in the panel preview.

---
## Step 5: Customize the Panel
- Rename the panel title (e.g., **“Random Walk Demo (Fake Data)”**).
- Adjust visualization settings (colors, legends, units, etc.).
- Keep it simple for your first dashboard.

---
## Step 6: Save the Dashboard
1. Click **Save** (top-right).
2. Enter a dashboard name (e.g., **“My First Dashboard”**).
3. Click **Save** again.

---
## Step 7: View Your Dashboard
- Exit edit mode.
- You now have a working Grafana dashboard displaying **fake test data**.

---
## Key Takeaway
Creating dashboards in Grafana is easiest when you start with **fake simulated data**. Once you're comfortable, you can connect real datasources like Prometheus, Loki, InfluxDB, or PostgreSQL.

---
