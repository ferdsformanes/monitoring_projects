
# Build a Live SD‑WAN Dashboard in Grafana Using a Python REST API (Step‑by‑Step Guide)

This guide explains how to expose your Cisco Catalyst SD-WAN Python script as a REST API so that Grafana’s Infinity datasource can consume it.

---

## 1. Install Grafana Infinity Plugin

Run on the Grafana server:

```bash
grafana-cli plugins install yesoreyeram-infinity-datasource
sudo systemctl restart grafana-server
```

Verify installation in Grafana: **Configuration → Plugins → Infinity Datasource**.

---

## 2. Convert the Python Script into a REST API Using Flask

Create a file named `sdwan_api.py`:

```python
from flask import Flask, jsonify
import requests, urllib3

app = Flask(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

@app.route("/devices", methods=["GET"])
def get_devices():

    session = requests.Session()

    login_url = f"{HOST}/j_security_check"
    payload = {"j_username": USERNAME, "j_password": PASSWORD}
    resp = session.post(login_url, data=payload, verify=False)

    if resp.status_code != 200 or "JSESSIONID" not in session.cookies:
        return {"error": "Login failed"}, 500

    devices_url = f"{HOST}/dataservice/device"
    resp = session.get(devices_url, verify=False)

    if resp.status_code != 200:
        return {"error": "Failed to retrieve devices"}, 500

    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
```

---

## 3. Run the Python API Service

Install Flask:
```bash
pip install flask
```

Run the script:
```bash
python sdwan_api.py
```

Your new endpoint will be:
```
http://<your-server-ip>:5001/devices
```

Open it in a browser to verify JSON output.

---

## 4. Configure Grafana Infinity Datasource

1. Open Grafana → **Configuration → Data Sources**
2. Add Datasource → **Infinity**
3. Configure:
   - **Name:** SD-WAN Devices
   - **Type:** JSON/REST API
   - **Base URL:**
     ```
     http://<your-server-ip>:5001
     ```
4. Save & Test

---

## 5. Build the Query in Grafana

In a new dashboard panel:

- Datasource: **SD-WAN Devices**
- Query Type: **URL**
- URL Path:
  ```
  /devices
  ```
- Format: **JSON**
- Data Path:
  ```
  data
  ```

Grafana Infinity will parse the fields automatically.

---

## 6. Visualize Device Information

### Recommended Columns
- `host-name`
- `deviceId`
- `system-ip`
- `device-type`
- `reachability`

### Example Visualizations
- **Table** → full device list
- **Pie Chart** → Device types breakdown
- **Stat** → Count reachable devices

---

## Summary
You now have a live API that Grafana can query using the Infinity datasource, enabling continuous visualization of SD-WAN device inventory.

---
