# Centreon Installation via OVA on VMware

1. **Download the Centreon OVA**  
   - Go to [Centreon Download Page](https://download.centreon.com/) and get the latest OVA file.

2. **Import OVA into VMware**  
   - Open VMware Workstation → **File → Open**.  
   - Select the downloaded `.ova` file.  
   - Click **Import** and wait for the process to finish.

3. **Start the VM**  
   - Power on the imported VM.  
   - Default credentials (check official docs):  
     ```
     Username: root
     Password: centreon
     ```

4. **Configure Network**  
   - Assign a static IP or use DHCP.  
   - Note the IP address for web access.

5. **Access Centreon Web UI**  
   - Open browser → `http://<VM-IP>/centreon`.  
   - Complete the initial setup wizard (DB and admin account are usually pre-configured).


