# Running Prometheus as a Windows Service

This guide explains how to run **Prometheus** as a Windows service using **NSSM (Non-Sucking Service Manager)**.

---

## ✅ Step 1: Download and Install NSSM
1. Go to [https://nssm.cc/download](https://nssm.cc/download).
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
   - **Arguments**: `--config.file=C:\Prometheus\prometheus.yml`
   - **Startup directory**: `C:\Prometheus`
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
- Ensure Prometheus and its configuration file (`prometheus.yml`) are located in `C:\Prometheus`.
- NSSM is used because Windows does not natively support running `.exe` files as services.
- nssm stop Prometheus
- nssm start Prometheus
- nssm edit Prometheus

