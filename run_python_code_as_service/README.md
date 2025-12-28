# Run Python SD-WAN Exporter as a Windows Service

This guide explains how to run a Python-based SD-WAN Prometheus exporter as a **Windows Service** using **NSSM (Non-Sucking Service Manager)**.

---

Run sdwan_exporter_flask.py as a Windows Service (NSSM)

1) Prerequisites
- Windows 10/11
- Python installed (python --version)
- sdwan_exporter_flask.py runs manually
- Example paths:
  Python: C:\Users\user\AppData\Local\Programs\Python\Python313\python.exe
  Script: C:\sdwan\sdwan_exporter_flask.py

2) Download NSSM
- https://nssm.cc/download
- Extract to: C:\nssm\win64\nssm.exe

3) Install Service
- Open Command Prompt as Administrator
- Run:
  C:\nssm\win64\nssm.exe install sdwan_exporter_flask

Application tab:
- Path: C:\Users\user\AppData\Local\Programs\Python\Python313\python.exe
- Arguments: sdwan_exporter_flask.py
- Startup directory: C:\sdwan
- Click Install service

4) Start Service
- Command line:
  nssm start sdwan_exporter_flask
- Or:
  services.msc → sdwan_exporter_flask → Start

5) Verify
- Browser:
  http://localhost:8000/metrics
- Prometheus:
  Status → Targets → sdwan_exporter_flask = UP

6) Optional: Auto-Restart & Logs
- nssm edit sdwan_exporter_flask
- Exit Actions: Restart, Delay 5000ms
- I/O:
  stdout: C:\sdwan\sdwan_exporter_flask.out.log
  stderr: C:\sdwan\sdwan_exporter_flask.err.log

7) Stop / Remove / Status
- nssm stop sdwan_exporter_flask
- nssm remove sdwan_exporter_flask confirm
- nssm status sdwan_exporter_flask
- nssm start sdwan_exporter_flask



---

## Notes
- Tested on **Windows 10 / 11**
- Works for **Flask exporters**, background scripts, and long-running Python processes
- Ideal for **Prometheus exporters**

## License
MIT
