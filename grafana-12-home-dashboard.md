# How to Set a Home Dashboard in Grafana 12

This guide covers setting up your landing page for individual users and entire organizations in Grafana 12 (released 2025).

## Prerequisites
* **Permissions:** You must have Admin or Editor access.
* **Star the Dashboard:** Click the **star icon** on your target dashboard before trying to select it as home.

---

## 1. Global Home Dashboard (Organization-wide)
*Use this to set a default landing page for every member of your organization.*

1. **Navigate to Administration:** Click the **Administration** (gear icon) in the left sidebar.
2. **Access Default Preferences:** Select **Default Preferences** under the **General** section.
3. **Select Home Dashboard:** Choose your starred dashboard from the **Home Dashboard** dropdown.
4. **Save:** Click **Save** to apply the changes globally.

---

## 2. Personal Home Dashboard (User-specific)
*Use this to override the global default with a custom view just for your account.*

1. **Open User Profile:** Click your **user profile icon** at the bottom-left of the side menu.
2. **Select Preferences:** Navigate to the **Preferences** tab.
3. **Set Home Dashboard:** Find the **Home Dashboard** setting and select your starred dashboard.
4. **Save:** Click **Save** at the bottom of the page.

---

## 3. Team-Specific Home Dashboard
*Ideal for specific departments (e.g., SRE or Marketing teams).*

1. Navigate to **Administration** > **Users and access** > **Teams**.
2. Select your **Team Name** and go to the **Settings** tab.
3. Update the **Home Dashboard** option and click **Save**.

---
*Note: For automated setups, Grafana 12 supports "Observability as Code," allowing you to provision these settings via environment variables like `GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH`.*
