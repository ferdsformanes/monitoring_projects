# Steps to Add a Regular User in Centreon

1. **Log in to Centreon Web UI**  
   Go to `http://<Centreon-IP>/centreon` and log in as an admin.

2. **Navigate to User Management**  
   - Click **Administration → ACL → Contacts**.

3. **Add New Contact**  
   - Click **Add**.  
   - Fill in:  
     - **Name**: e.g., `RegularUser`  
     - **Alias**: Friendly name  
     - **Email**: For notifications  
     - **Password**: Set a strong password

4. **Assign Limited Permissions**  
   - Go to **Administration → ACL → ACL Groups**.  
   - Create or select a group with **restricted rights** (e.g., view-only or limited host/service access).  
   - Add the new user to this group.

5. **Save & Apply**  
   - Click **Save**.  
   - Log out and test the new user account.

