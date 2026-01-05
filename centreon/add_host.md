# Steps to Add a Host in Centreon

1. **Log in to Centreon Web UI**  
   Go to `http://<Centreon-IP>/centreon` and log in as admin.

2. **Navigate to Host Configuration**  
   - Click **Configuration → Hosts → Add**.

3. **Fill Host Details**  
   - **Name**: e.g., `Switch01`  
   - **Alias**: Friendly name (optional)  
   - **IP Address / DNS**: Enter the switch’s IP  
   - **Monitoring Template**: Select a template (e.g., `Generic-SNMP-Switch`).

4. **Set Poller**  
   - Choose the poller (usually `Central`).

5. **Save & Apply**  
   - Click **Save**.  
   - Then go to **Configuration → Pollers → Export Configuration**.  
   - Click **Generate** and **Apply**.

6. **Verify Monitoring**  
   - Go to **Monitoring → Hosts**.  
   - Check if the switch shows **UP** and services are listed.
