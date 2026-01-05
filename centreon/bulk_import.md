# Bulk Import Hosts in Centreon

## ✅ Steps to Import Multiple Hosts Using CSV

1. **Prepare the CSV File**  
   Use the following format (semicolon `;` separated):
   ```
   name;alias;address;template
   Switch01;CoreSwitch;192.168.1.10;Generic-SNMP-Switch
   Switch02;AccessSwitch;192.168.1.11;Generic-SNMP-Switch
   Switch03;DistributionSwitch;192.168.1.12;Generic-SNMP-Switch
   ```

2. **Upload CSV in Centreon**  
   - Go to **Configuration → Hosts → Import**.
   - Select your CSV file.
   - Validate the data preview.

3. **Import and Apply Configuration**  
   - Click **Import**.
   - Then go to **Configuration → Pollers → Export Configuration**.
   - Click **Generate** and **Apply**.

4. **Verify Hosts**  
   - Go to **Monitoring → Hosts**.
   - Ensure all imported hosts show **UP** and services are listed.

---

✅ Done! You have successfully added multiple hosts to Centreon using bulk import.
