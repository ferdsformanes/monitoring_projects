# How to Use Overrides in Grafana 12 (Table Panel – PostgreSQL)

Overrides are used to customize how a single column is displayed in Grafana, while the rest of the panel stays the same.


## 1. Open the Existing Table Panel

1. Hover over your **Table panel**
2. Click **Edit**

---

## 2. Open the Overrides Section

1. In the **right-hand configuration panel**
2. Click **Overrides**

Overrides allow you to control formatting and behavior for individual columns.

---

## 3. Add Field Overrides

1. Click **Add an override**
2. Choose **Fields with name**
3. Select the column you want to customize

Repeat the steps below for each field.

---

### Status Column (`status`)

**Goal:** Make device state immediately visible

* Property: **Cell display mode**

  * Set to **Badge**
* Property: **Value mappings**

  * `Up` → Green
  * `Down` → Red
* (Optional) **Thresholds**

  * Green = Up
  * Red = Down

**Result:** Device status is visible at a glance.

---

### Time Column (`time`)

**Goal:** Display readable timestamps

* Property: **Unit**

  * Date & Time → Date Time (local or ISO)

**Result:** Clean and human-readable timestamps.

---

### IP Address Column (`ip_address`)

**Goal:** Improve scan readability

* Property: **Cell type** → Auto
* Property: **Alignment** → Left

**Result:** IP addresses remain easy to scan.

---

### Hostname Column (`hostname`)

**Goal:** Emphasize the primary identifier

* Property: **Cell type** → Auto
* (Optional) **Text size** → Slightly larger

**Result:** Hostnames become the visual anchor of the table.

---

### Device Type Column (`device_type`)

**Goal:** Visually distinguish device roles

* Property: **Cell display mode** → Badge (optional)
* (Optional) **Value mappings**:

  * Router → Blue
  * Switch → Purple
  * Firewall → Orange

**Result:** Device roles are instantly recognizable.

---

### Location Column (`location`)

**Goal:** Keep location data clean and readable

* Property: **Alignment** → Left

No additional formatting required.

---

### Sensitive Columns (`username`, `password`)

**Goal:** Reduce noise and avoid exposing credentials

* Property: **Hide field**

**Result:** A cleaner table with sensitive data removed.

---

## 4. Optional: Global Numeric Alignment

If you later add numeric fields (uptime, latency, counters):

1. Add override → **Fields with type → Number**
2. Property: **Alignment → Right**

---

## 5. Apply Changes

* Click **Apply** in the top-right corner

---

## Final Outcome

After applying these overrides, your table panel will:

* Highlight **device status visually**
* Display **readable timestamps**
* Emphasize **hostnames**
* Hide **sensitive or noisy fields**
* Look intentional and production-ready instead of default Grafana styling
