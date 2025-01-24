Here’s the updated `README.md` file without the **Table of Contents**, **Note in Step 4**, and **example SA name**:

---

# Datadog GCP Integration Guide

This guide provides step-by-step instructions for integrating **Google Cloud Platform (GCP)** with **Datadog** using a **Service Account (SA)** with the appropriate permissions.

---

## Prerequisites

Before proceeding, ensure you have the following:

1. **GCP Project**: A GCP project with the necessary permissions to create and manage Service Accounts.
2. **Datadog Account**: A Datadog account with administrative access.
3. **Service Account (SA)**: A GCP Service Account with the following permissions:
   - **Monitoring Viewer**
   - **Compute Viewer**
   - **Cloud Asset Viewer**
   - **Browser**

---

## Step 1: Create a Service Account

1. **Navigate to the GCP Console**:
   - Go to the [GCP Console](https://console.cloud.google.com/).
   - Select your project.

2. **Create a Service Account**:
   - Go to **IAM & Admin** > **Service Accounts**.
   - Click on **Create Service Account**.
   - Provide a name for the Service Account.
   - Click **Create**.

3. **Assign Roles to the Service Account**:
   - Add the following roles to the Service Account:
     - **Monitoring Viewer**
     - **Compute Viewer**
     - **Cloud Asset Viewer**
     - **Browser**
   - Click **Done**.

   ![Create Service Account](images/create-sa.png)  
   *Add a screenshot of the GCP Service Account creation page.*

4. **Note the Service Account Email**:
   - After creating the Service Account, note the **Service Account Email**.

---

## Step 2: Add GCP Account in Datadog

1. **Navigate to Datadog Integration Tab**:
   - Log in to your Datadog account.
   - Go to the **Integrations** tab.
   - Search for **Google Cloud Platform**.

2. **Add GCP Account**:
   - Click on **+ Add Account**.
   - Copy the **Datadog Principal** provided.

   ![Datadog GCP Integration](images/datadog-gcp-integration.png)  
   *Add a screenshot of the Datadog GCP Integration page.*

3. **Grant Permissions to the Service Account**:
   - Go back to the GCP Console.
   - Navigate to **IAM & Admin** > **IAM**.
   - Find the Service Account you created earlier.
   - Click on the **Edit** icon.
   - Add the **Service Account Token Creator** role to the Service Account.
   - Paste the **Datadog Principal** in the **Members** field.
   - Click **Save**.

   ![Add Datadog Principal](images/add-datadog-principal.png)  
   *Add a screenshot of the GCP IAM page showing the Datadog Principal added to the Service Account.*

---

## Step 3: Verify and Save the Integration

1. **Return to Datadog**:
   - Go back to the Datadog GCP Integration page.
   - Enter the **Service Account Email** in the **Service Account** field.
   - Click on **Verify and Save Account**.

2. **Verify the Integration**:
   - If the integration is successful, you’ll see a confirmation message.
   - Datadog will start collecting metrics and logs from your GCP project.

   ![Verify and Save](images/verify-and-save.png)  
   *Add a screenshot of the Datadog GCP Integration verification page.*

---

## Troubleshooting

### Common Issues

1. **403 Access Denied**:
   - Ensure the Service Account has the correct roles and permissions.
   - Verify that the **Datadog Principal** is correctly added to the Service Account.

2. **Integration Verification Failed**:
   - Double-check the **Service Account Email** and ensure it matches the one created in GCP.
   - Ensure the **Service Account Token Creator** role is assigned.

3. **No Data in Datadog**:
   - Verify that the GCP project has active resources (e.g., Compute Engine instances, Cloud Storage buckets).
   - Check the Datadog logs for any errors.

---

## Conclusion

You have successfully integrated **Google Cloud Platform (GCP)** with **Datadog**. This integration allows you to monitor your GCP resources, collect metrics, and analyze logs in Datadog.

For more information, refer to the official documentation:
- [Datadog GCP Integration Guide](https://docs.datadoghq.com/integrations/google_cloud_platform/)
- [GCP IAM Documentation](https://cloud.google.com/iam/docs)

---

### Suggested Places to Add Images

1. **Create Service Account**:
   - Screenshot of the GCP Service Account creation page.

2. **Datadog GCP Integration Page**:
   - Screenshot of the Datadog GCP Integration page showing the **+ Add Account** button.

3. **Add Datadog Principal**:
   - Screenshot of the GCP IAM page showing the Datadog Principal added to the Service Account.

4. **Verify and Save**:
   - Screenshot of the Datadog GCP Integration verification page.

---

Let me know if you need further assistance! 😊
