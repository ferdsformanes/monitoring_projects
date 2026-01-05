# Steps to Add an Admin User in Centreon

1. **Log in to Centreon Web UI**  
   Go to `http://<Centreon-IP>/centreon` and log in as an existing admin.

2. **Navigate to User Management**  
   - Click **Administration → ACL → Contacts**.

3. **Add New Contact**  
   - Click **Add**.  
   - Fill in:  
     - **Name**: e.g., `AdminUser`  
     - **Alias**: Friendly name  
     - **Email**: For notifications  
     - **Password**: Set a strong password

4. **Assign Admin Rights**  
   - Go to **Administration → ACL → ACL Groups**.  
   - Add the new user to the **Administrators** group (or create a custom group with full permissions).

5. **Save & Apply**  
   - Click **Save**.  
   - Log out and test the new admin account.

