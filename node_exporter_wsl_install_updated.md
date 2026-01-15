
# Option A — Install Node Exporter Inside WSL (with Testing & Grafana Setup)

This guide explains how to install Prometheus Node Exporter inside a WSL (Ubuntu/Debian) environment, verify that it works, and visualize the data in Grafana.

---

## 1. Update WSL
```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Download Node Exporter
Check the latest release at:
https://github.com/prometheus/node_exporter/releases

Example:
```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-amd64.tar.gz
```

---

## 3. Extract the Archive
```bash
tar -xvzf node_exporter-1.8.1.linux-amd64.tar.gz
```

---

## 4. Move Binary to `/usr/local/bin`
```bash
sudo mv node_exporter-1.8.1.linux-amd64/node_exporter /usr/local/bin/
```

---

## 5. Create a Systemd Service
(Requires SystemD-enabled WSL)

```bash
sudo nano /etc/systemd/system/node_exporter.service
```

Paste the following:
```ini
[Unit]
Description=Prometheus Node Exporter
After=network.target

[Service]
User=nobody
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

---

## 6. Enable and Start the Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
```

---

## 7. Test Node Exporter Endpoint
Use curl inside WSL:
```bash
curl http://localhost:9100/metrics
```

Or open your browser on Windows:
```
http://localhost:9100/metrics
```

If you see metrics text, Node Exporter is running correctly.

---

## 8. Add Node Exporter to Prometheus
Add this block to your `prometheus.yml`:
```yaml
scrape_configs:
  - job_name: 'wsl_node'
    static_configs:
      - targets: ['localhost:9100']
```

Restart Prometheus after changes.

---

## 9. Verify Prometheus is Scraping Node Exporter
Open Prometheus UI at:
```
http://localhost:9090
```

Go to **Status → Targets** and confirm:
- `wsl_node` is **UP**
- The target `localhost:9100` is reachable

---

## 10. Add Prometheus as a Data Source in Grafana
1. Open Grafana:
```
http://localhost:3000
```

2. Login (default):
- **User:** admin
- **Password:** admin

3. Go to **Connections → Data sources**
4. Click **Add data source**
5. Select **Prometheus**
6. Set URL:
```
http://localhost:9090
```
7. Click **Save & Test** → should show *Data source is working*

---

## 11. Import a Node Exporter Dashboard in Grafana
Grafana provides ready‑made dashboards.

1. Go to **Dashboards → New → Import**
2. Enter dashboard ID:
```
1860
```
(This is a popular Node Exporter dashboard.)

3. Select your Prometheus datasource
4. Click **Import**

You should now see CPU, RAM, disk, filesystem, and network metrics from WSL.

---

## Node Exporter in WSL is Now Fully Integrated
You now have:
- Node Exporter running inside WSL
- Metrics scraped by Prometheus
- Visualizations in Grafana

---
