# How to Import Dashboards in Grafana

This guide walks you through importing existing **Grafana dashboards**. There are **two ways** to import a dashboard: using a **Grafana.com dashboard ID** or a **JSON file**.

---

## Step 1: Log In to Grafana

* Open your browser and go to your Grafana URL.
* Log in using your credentials.

---

## Step 2: Open the Dashboard Import Menu

1. Click the **menu (☰)** on the left.
2. Select **Dashboards → Manage**.
3. Click **Import** (top-right corner).

---

## Step 3: Import Using Grafana.com Dashboard ID

1. Go to [Grafana Dashboards](https://grafana.com/grafana/dashboards) and find a dashboard you want to import.
2. Copy the **Dashboard ID** (number shown on Grafana.com).
3. In Grafana, under the **Import** page, select **Import via Grafana.com Dashboard ID**.
4. Paste the Dashboard ID into the field.
5. Click **Load**.
6. Choose the **Data source** you want the dashboard to use.
7. Click **Import**.

---

## Step 4: Import Using a JSON File

1. If you have a JSON file of a dashboard, go to the **Import** page.
2. Click **Upload JSON file**.
3. Select your JSON file from your computer.
4. Choose the **Data source** the dashboard should use.
5. Click **Import**.

---

## Step 5: Verify Your Imported Dashboard

* The imported dashboard should open automatically.
* Check that panels display data correctly (especially if using TestData or another sample datasource).
* Adjust panels if necessary (colors, titles, units, etc.).

---

## Step 6: Save and Organize Your Dashboard

1. Click **Save** (top-right) if you make changes.
2. Give the dashboard a descriptive name (e.g., **Imported Dashboard Demo**).
3. Optionally, move it to a folder for better organization.

---

## Key Takeaway

There are **two ways to import dashboards in Grafana**: using a **Grafana.com dashboard ID** or a **JSON file**. Importing dashboards is a **quick way to get pre-built panels and visualizations**. Once comfortable, you can modify imported dashboards or create your own from scratch.
