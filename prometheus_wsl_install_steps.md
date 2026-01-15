# Install Prometheus (Latest Stable v3.9.1) on WSL (Ubuntu) and Run as a Service

**Latest stable version:** Prometheus **v3.9.1** released on **2026‑01‑07** citeturn7search2turn7search3

## STEP 1 — Enable systemd in WSL
```bash
sudo nano /etc/wsl.conf
```
Add:
```
[boot]
systemd=true
```
Restart WSL:
```powershell
wsl --shutdown
```
Verify systemd:
```bash
systemctl is-system-running
```

## STEP 2 — Update Ubuntu
```bash
sudo apt update && sudo apt upgrade -y
```

## STEP 3 — Create Prometheus user and directories
```bash
sudo useradd --no-create-home --shell /usr/sbin/nologin prometheus
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
```

## STEP 4 — Download Prometheus v3.9.1 (Linux AMD64)
```bash
wget https://github.com/prometheus/prometheus/releases/download/v3.9.1/prometheus-3.9.1.linux-amd64.tar.gz
```
Extract:
```bash
tar -xvf prometheus-3.9.1.linux-amd64.tar.gz
cd prometheus-3.9.1.linux-amd64
```

## STEP 5 — Move binaries
```bash
sudo cp prometheus /usr/local/bin/
sudo cp promtool /usr/local/bin/
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
```

## STEP 6 — Move configuration files
```bash
sudo cp -r consoles /etc/prometheus
sudo cp -r console_libraries /etc/prometheus
sudo cp prometheus.yml /etc/prometheus/prometheus.yml
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
```

## STEP 7 — Create the Prometheus systemd service
```bash
sudo nano /etc/systemd/system/prometheus.service
```
Paste:
```
[Unit]
Description=Prometheus Monitoring
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus   --config.file=/etc/prometheus/prometheus.yml   --storage.tsdb.path=/var/lib/prometheus   --web.console.templates=/etc/prometheus/consoles   --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```

## STEP 8 — Enable and start Prometheus
```bash
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus
```

## STEP 9 — Verify
```bash
sudo systemctl status prometheus
```

## STEP 10 — Access Prometheus UI
Open:
```
http://localhost:9090
```
