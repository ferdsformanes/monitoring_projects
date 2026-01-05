# Running Prometheus as a Windows Service

This guide explains how to run **Prometheus** as a Windows service using **NSSM (Non-Sucking Service Manager)**.

---

## ✅ Step 1: Download and Install NSSM
1. Go to https://nssm.cc/download
2. Download the latest stable version for Windows.
3. Extract the archive and place `nssm.exe` in a folder (e.g., `C:\nssm`).

---

## ✅ Step 2: Create the Prometheus Service
1. Open **Command Prompt as Administrator**.
2. Run:
   ```cmd
   C:\nssm\nssm.exe install Prometheus
   ```
3. In the NSSM GUI:
   - **Path**: `C:\Prometheus\prometheus.exe`
   - **Startup directory**: `C:\Prometheus`
   - **Arguments**: `--config.file=C:\Prometheus\prometheus.yml`
4. Click **Install Service**.

---

## ✅ Step 3: Start the Service
1. Open **Services** (press `Win + R`, type `services.msc`).
2. Find **Prometheus**, right-click → **Start**.
3. (Optional) Set **Startup type** to **Automatic** so it starts on boot.

---

## ✅ Step 4: Verify
- Open [http://localhost:9090](http://localhost:9090) in your browser.
- Confirm Prometheus is running even after a reboot.

---

### Notes:
- nssm stop Prometheus
- nssm start Prometheus
- nssm edit Prometheus

