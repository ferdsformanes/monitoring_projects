
# Simple Guide: How to Use Value Mapping in Grafana

## 1. Open or Create a Panel
- Go to your dashboard.
- Add a new panel or edit an existing one.

## 2. Go to the Field Tab
- On the right panel, select **Field**.
- Scroll to find **Value mappings**.

## 3. Choose Mapping Type
- **Value to text** – for exact numbers.
- **Range to text** – for numeric ranges.
- **Regex to text** – for pattern matching.

## 4. Add a Mapping
  - Click **Add a mapping**.
  ### 🟢 UP Mapping
  - **Value**: `up`
  - **Text**: 🟢 **Up**
  - **Color**: Green
  
  ### 🔴 DOWN Mapping
  - **Value**: `down`
  - **Text**: 🔴 **Down**
  - **Color**: Red

## 5. Check Your Panel
- Make sure the mapping changes the value.
- Add an "undefined" mapping if needed.

## That’s it!
Value mapping makes your dashboards more readable and user-friendly.
