# Monitoring Cisco Switches with Prometheus and Grafana
---

## ✅ 1. Enable SNMP on Cisco Switch
```
configure terminal
snmp-server community <community_string> RO
snmp-server enable traps
```
Replace `<community_string>` with a secure string.

---

## ✅ 2. Deploy SNMP Exporter
Prometheus needs SNMP Exporter to collect metrics:
- Download SNMP Exporter: [https://github.com/prometheus/snmp_exporter](https://github.com/prometheus/snmp_exporter)
- Generate Cisco-specific config:
```
./generator generate
```
This creates `snmp.yml` with Cisco OIDs.

Run SNMP Exporter:
```
./snmp_exporter --config.file=snmp.yml
```
Default port: `9116`.

---

## ✅ 3. Configure Prometheus to Scrape SNMP Exporter
Edit `prometheus.yml`:
```yaml
scrape_configs:
  - job_name: 'cisco-switches'
    static_configs:
      - targets: ['<switch_ip>']
    metrics_path: /snmp
    params:
      module: [cisco]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - target_label: instance
        replacement: <switch_ip>
      - target_label: __address__
        replacement: localhost:9116
```
Restart Prometheus.

---

## ✅ 4. Add Grafana Dashboard
- In Grafana:
  - Add Prometheus as a **data source**.
  - Import a Cisco SNMP dashboard from [Grafana Dashboards](https://grafana.com/grafana/dashboards/).
    - Popular dashboard ID: **11529** (Cisco SNMP Monitoring).

---

## ✅ 5. Verify
- Check Prometheus targets: `http://<prometheus_ip>:9090/targets`
- Metrics should appear.
- Grafana dashboard should show CPU, memory, interface traffic, etc.

---

### 🔥 Optional Enhancements
- Use **Alertmanager** for alerts.
- Secure SNMP with **SNMPv3** for authentication and encryption.
- Add multiple switches in `prometheus.yml`.
