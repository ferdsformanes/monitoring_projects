# Configure Task Scheduler for Prometheus Without Elevated Privileges

This guide explains how to run **Prometheus** automatically using **Task Scheduler** without requiring administrator rights.

---

## ✅ Steps

### 1. Open Task Scheduler
- Press **Win + R**, type `taskschd.msc`, and hit **Enter**.

### 2. Create a New Task
- Click **Action → Create Task**.
- In the **General** tab:
  - Name: `Prometheus`
  - **Security Options**:
    - Select **Run only when user is logged on** (avoids password prompt).
    - Check **Run with highest privileges** if allowed (optional).

### 3. Set the Trigger
- Go to **Triggers** tab → Click **New**.
- **Begin the task**: `At log on`.
- Select your user account.
- Click **OK**.

### 4. Set the Action
- Go to **Actions** tab → Click **New**.
- **Action**: `Start a program`.
- **Program/script**:
  ```
  C:\prometheus\prometheus.exe
  ```
- **Add arguments**:
  ```
  --config.file=C:\prometheus\prometheus.yml
  ```
- **Start in**:
  ```
  C:\prometheus
  ```
- Click **OK**.

### 5. Conditions & Settings
- In **Conditions**, uncheck “Start only if on AC power” (optional).
- In **Settings**, enable:
  - “Allow task to be run on demand”
  - “Restart the task if it fails” (optional)

### 6. Save and Test
- Click **OK**.
- You won’t be asked for a password because it runs under your account when logged in.
- Log off and log back in to confirm Prometheus starts automatically.

---

## ⚠ Important Limitation
This method **does not run Prometheus as a true Windows Service**. It will only start when you log in, and if you log out, Prometheus stops.

---

## ✅ Alternative Options
- Use a **Startup Shortcut** in `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`.
- Create a **batch script** and link it to Task Scheduler.

