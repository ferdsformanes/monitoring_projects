# How to Create Users and Assign Roles in Grafana

## Prerequisites
- You must be logged in as a **Grafana Server Administrator**.
- Grafana authentication must allow **local users** (default behavior).

## Step 1: Verify You Are a Server Administrator
Before creating users:

1. Click your **profile icon** (top-right).
2. Go to **Administration**.
3. If you can access **Administration → Users and access**, you are a **server administrator**.

> Only server administrators can create users and manage global access.

## Step 2: Create a New User
1. In the left-side menu, go to **Administration → Users and access → Users**.
2. Click **New user**.
3. Fill in the required details:
   - **Name**
   - **Email**
   - **Username**
   - **Password**
4. Click **Create user**.

Grafana will:
- Create the user
- Assign the user to the **current organization**
- Set the default role to **Viewer**

## Step 3: Assign an Organization Role to the User
Roles are **organization-specific**, not global.

1. While still on the **Users** page, click the newly created user.
2. Under **Organizations**, locate the current organization.
3. Change the role as needed:
   - **Viewer** – read-only access
   - **Editor** – can create and edit dashboards
   - **Admin** – full control within the organization
4. Click **Save** (if required).

### Organization Roles Explained
- **Viewer**: View dashboards only
- **Editor**: Create and edit dashboards, panels, and alerts
- **Admin**: Manage dashboards, data sources, users, and settings for that organization

## Step 4: Add the User to Another Organization (Optional)
If you have multiple organizations:

1. Open the **user profile**.
2. Click **Add to organization**.
3. Select:
   - The **organization**
   - The **role** for that organization
4. Click **Add**.

> A single user can belong to **multiple organizations**, each with a different role.

## Step 5: Verify User Access
To verify everything works:
- Ask the user to log in
- Switch organizations (top-left org switcher)
- Confirm permissions match the assigned role

## Notes
- User roles apply **per organization**, not globally.
- A **Grafana Server Admin** is different from an **Organization Admin**:
  - Server Admin: manages users and organizations
  - Org Admin: manages resources inside one organization only
