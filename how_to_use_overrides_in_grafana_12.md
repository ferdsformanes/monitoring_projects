
# How to Use Overrides in Grafana 12

## 1. Open Panel
- Click your table → **Edit**

## 2. Go to Overrides
- Right side → **Overrides**

## 3. Add Override
- Click **Add an override**
- Select a column (e.g., `device_status`, `bytes`, `last_seen`)

## 4. Add Property
### Common properties:
- **Status → Badge**
  - Cell display mode → Badge
  - Value mapping → 1=Up, 0=Down
- **Bytes columns**
  - Unit → bytes (GB/MB)
- **Timestamps**
  - Unit → Date & Time
- **Uptime**
  - Unit → seconds → Display as Duration
- **CPU/Memory %**
  - Thresholds → green/yellow/red
- **Numeric columns**
  - Alignment → Right
- **Hide noisy columns**
  - Hide field

## 5. Save
- Click **Apply** (top right)
