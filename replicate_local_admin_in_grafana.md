# How to Replicate the Default Local Admin User in Grafana

## Overview
The default local `admin` user in Grafana has:
- **Grafana Server Administrator** privileges (can manage server-wide settings and users) :contentReference[oaicite:0]{index=0}
- **Organization Admin** role (full access within an organization) :contentReference[oaicite:1]{index=1}

This guide shows how to replicate that using the Grafana UI.

## Prerequisites
- Log in as the existing **local admin** or another **Grafana Server Administrator** user.
- Ensure local authentication is enabled.

## Step 1: Create a New Local User
1. Sign in to Grafana.
2. Go to **Administration → Users and access → Users**.
3. Click **New user**.
4. Fill in the user details (Name, Username, Email, Password).
5. Click **Create user**.

According to Grafana docs, server administrators can manage all users on the instance. :contentReference[oaicite:2]{index=2}

## Step 2: Grant Grafana Server Admin Privileges
1. Open the **newly created user**.
2. Enable **Grafana Admin** (server admin) privileges.
3. Save the changes.

Server admins can assign or remove these admin privileges. :contentReference[oaicite:3]{index=3}

## Step 3: Assign Organization Admin Role
1. In the user profile, scroll to **Organizations**.
2. For each organization:
   - Set the role to **Admin**.
3. Save if required.

Organization roles determine access within that organization. :contentReference[oaicite:4]{index=4}

## Step 4: Add the User to Other Organizations (Optional)
1. Click **Add to organization**.
2. Select another organization.
3. Assign the **Admin** role.
4. Repeat as needed.

Users can belong to multiple organizations with different roles. :contentReference[oaicite:5]{index=5}

## Step 5: Verify the Replicated Local Admin User
Log in as the new user and confirm:
- **Administration** menu is visible  
- **Users and access** exists  
- The user can manage dashboards, data sources, and roles

## Notes
- Use named local admin accounts instead of the default `admin` for daily work.
- Server admin is different from organization admin: server admins have instance-wide rights, org admins have org-level rights. :contentReference[oaicite:6]{index=6}
