# How to Add Field Overrides in Grafana | Table Panel Tutorial

This tutorial shows how to use **field overrides** in a Grafana **Table panel**, focusing only on the **Status** and **Time** columns.

---

## Step 1: Open the Table Panel

* Hover over your **Table panel**
* Click **Edit**

---

## Step 2: Go to Overrides

* In the **right-hand panel**
* Click **Overrides**

This section allows you to control how **individual fields (columns)** are displayed.

---

## Step 3: Add an Override for the Status Column

1. Click **Add an override**
2. Select **Fields with name**
3. Choose `status`

### Configure the Status Override

* **Cell display mode** → Badge
* **Value mappings**

  * `Up` → Green
  * `Down` → Red

**Result:** The Status column is displayed as a colored badge.

---

## Step 4: Add an Override for the Time Column

1. Click **Add an override**
2. Select **Fields with name**
3. Choose `time`

### Configure the Time Override

* **Unit** → Date & Time

**Result:** The Time column is formatted as a readable timestamp.

---

## Step 5: Apply Changes

* Click **Apply** (top-right)

---

## Key Takeaway

> **Field overrides let you format specific columns—like Status and Time—without changing the query or affecting other fields in the table.**

This makes overrides ideal for demonstrations and tutorials, where you want to highlight specific fields while leaving the rest of the data unchanged.
