# Monitoring Cisco SD-WAN Devices with Prometheus and Grafana

This project demonstrates how to monitor Cisco SD-WAN devices using a custom Python exporter, Prometheus, and Grafana.

---

## ✅ Step 1: Create and Run the SD-WAN Exporter
Save the following code as `sdwan_exporter_flask.py`:

```python
from flask import Flask, Response
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco SD-WAN Sandbox credentials
HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

app = Flask(__name__)

# Create session and login once
session = requests.Session()
login_url = f"{HOST}/j_security_check"
payload = {"j_username": USERNAME, "j_password": PASSWORD}
resp = session.post(login_url, data=payload, verify=False)

if resp.status_code != 200 or "JSESSIONID" not in session.cookies:
    raise Exception("Login failed!")

print("JSESSIONID", session.cookies.get("JSESSIONID"))
print("Logged in successfully")

@app.route("/metrics")
def metrics():
    try:
        # Retrieve device list
        devices_url = f"{HOST}/dataservice/device"
        resp = session.get(devices_url, verify=False)
        if resp.status_code != 200:
            raise Exception(f"Failed to retrieve devices: {resp.status_code}, {resp.text}")
        devices = resp.json().get("data", [])
        
        # Count all devices
        up_count = len(devices)
        
        # Prometheus metric format
        output = f"# HELP sdwan_devices_up Number of SD-WAN devices
"
        output += f"# TYPE sdwan_devices_up gauge
"
        output += f"sdwan_devices_up {up_count}
"
    except Exception as e:
        output = f"# Error: {str(e)}"
    return Response(output, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Run the exporter:
```bash
python sdwan_exporter_flask.py
```

Test:
```bash
curl http://localhost:8000/metrics
```

---

## ✅ Step 2: Configure Prometheus
Edit `prometheus.yml` and add this scrape job:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
        labels:
          app: "prometheus"

  # Scrape your SD-WAN exporter
  - job_name: "sdwan"
    static_configs:
      - targets: ["localhost:8000"]
        labels:
          app: "sdwan_exporter"
```

Validate config:
```powershell
promtool.exe check config prometheus.yml
```

Restart Prometheus:
```powershell
./prometheus.exe --config.file=prometheus.yml
```

Verify targets:
Open `http://localhost:9090/targets` → Both jobs should show **UP**.

---

## ✅ Step 3: Configure Grafana
1. Open Grafana at `http://localhost:3000` (default user/pass: `admin/admin`).
2. Go to **Connections → Data Sources → Add Data Source**.
   - Select **Prometheus**.
   - URL: `http://localhost:9090`.
   - Click **Save & Test**.

---

## ✅ Step 4: Create Grafana Dashboard
1. Go to **Dashboards → New → New Dashboard**.
2. Add a **Stat Panel**:
   - Query:
     ```
     sdwan_devices_up
     ```
   - Visualization: **Stat**.
   - Set thresholds (e.g., green > 5, red < 3).
3. Add a **Time Series Panel**:
   - Query:
     ```
     sdwan_devices_up
     ```
   - Shows trend over time.
4. Save dashboard as **SD-WAN Monitoring**.

---

## ✅ Optional Enhancements
- Add more metrics in exporter (CPU, memory, tunnel status):
```python
for device in devices:
    hostname = device.get("host-name", "unknown")
    cpu = device.get("cpu", 0)
    output += f'sdwan_device_cpu{{hostname="{hostname}"}} {cpu}
'
```
- Add alerts in Grafana for device count drops.
- Secure the exporter with basic auth or reverse proxy.

---

## ✅ Repo Structure Suggestion
```
monitoring_tools_projects/
├── sdwan_exporter/
│   ├── sdwan_exporter_flask.py
│   ├── requirements.txt
│   └── README.md
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml (optional)
├── grafana/
│   ├── dashboards/
│   │   └── sdwan_dashboard.json
│   └── README.md
└── docker-compose.yml (optional for full stack)
```
