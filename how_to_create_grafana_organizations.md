# How to Create a New Organization in Grafana

## Prerequisites
- You must be signed in as a **Grafana Server Administrator**.

## Verify You Are a Server Administrator
Before creating a new organization, make sure you’re logged in as a **Grafana Server Admin**:

1. Click your **profile icon** (top-right).
2. Go to **Administration**.
3. If you can see **Administration → General → Organizations**, you are a **server administrator**.

> Only server admins can create and manage organizations.

## Steps to Create a New Organization
1. In the left-side menu, go to **Administration → General → Organizations**.
2. You will initially see **one organization** (usually the default one).
3. Click **+ New org**.
4. Enter the **name** of the new organization and click **Create**.

Grafana will automatically:
- Create the new organization
- Add you as the **Organization Administrator**
- Redirect you to the **Default Preferences** page of the new organization

## Verify the New Organization Was Created
After creating the organization:

1. Go back to **Administration → General → Organizations**.
2. You should now see **two organizations** listed:
   - The original (default) organization
   - The newly created organization
3. This confirms:
   - You are a **server administrator**
   - The new organization was successfully created
   - You are an **admin of both organizations**

## Optional: Configure Organization Preferences
You can now configure settings specific to the new organization:
- Home dashboard
- Time zone
- Week start day

## Optional: Add Users to the Organization
- Users can be added and assigned roles (Viewer, Editor, Admin).
- A user can belong to **multiple organizations** with different roles.

## Notes
- Organizations provide isolation for:
  - Dashboards
  - Data sources
  - Alerts
  - Folders
- This is useful for separating teams, environments (prod vs lab), or customers.
