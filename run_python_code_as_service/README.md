# Run Python SD-WAN Exporter as a Windows Service

This guide explains how to run a Python-based SD-WAN Prometheus exporter as a **Windows Service** using **NSSM (Non-Sucking Service Manager)**.

---

Run sdwan_exporter.py as a Windows Service (NSSM)

1) Prerequisites
- Windows 10/11
- Python installed (python --version)
- sdwan_exporter.py runs manually
- Example paths:
  Python: C:\Python312\python.exe
  Script: C:\sdwan\sdwan_exporter.py

2) Download NSSM
- https://nssm.cc/download
- Extract to: C:\nssm\win64\nssm.exe

3) Install Service
- Open Command Prompt as Administrator
- Run:
  C:\nssm\win64\nssm.exe install SDWAN_Exporter

Application tab:
- Path: C:\Python312\python.exe
- Arguments: sdwan_exporter.py
- Startup directory: C:\sdwan
- Click Install service

4) Start Service
- Command line:
  nssm start SDWAN_Exporter
- Or:
  services.msc → SDWAN_Exporter → Start

5) Verify
- Browser:
  http://localhost:8000/metrics
- Prometheus:
  Status → Targets → sdwan_exporter = UP

6) Optional: Auto-Restart & Logs
- nssm edit SDWAN_Exporter
- Exit Actions: Restart, Delay 5000ms
- I/O:
  stdout: C:\sdwan\sdwan_exporter.out.log
  stderr: C:\sdwan\sdwan_exporter.err.log

7) Stop / Remove
- nssm stop SDWAN_Exporter
- nssm remove SDWAN_Exporter confirm

---

## Notes
- Tested on **Windows 10 / 11**
- Works for **Flask exporters**, background scripts, and long-running Python processes
- Ideal for **Prometheus exporters**

## License
MIT
