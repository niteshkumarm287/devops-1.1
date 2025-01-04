
# 🚀 Build and Push Docker Image Workflow

This GitHub Actions (GHA) workflow automates the process of building and pushing a Docker image whenever a pull request is approved and merged into the main branch. It also updates the Helm chart deployment with the new Docker image tag and creates a pull request for the changes.

---

## 📋 Workflow Overview

### **Trigger:**
The workflow is triggered when a pull request targeting the `main` branch is **closed** and **merged**.

### **Jobs:**
1. **Build and Push Docker Image**
2. **Update Helm Chart with New Docker Image Tag**

---

## 🛠️ Workflow Steps

### **1️⃣ Build and Push Docker Image**
- Checks out the code from the repository.
- Sets up Docker Buildx for multi-platform builds.
- Logs in to Docker Hub using stored secrets.
- Builds the Docker image using the `cicd-python-app/` directory.
- Pushes the Docker image to Docker Hub with the commit SHA as the tag.

### **2️⃣ Update Helm Chart**
- Checks out the repository code.
- Creates a new branch to update the Helm chart values.
- Updates the Docker image tag in the `deployment.yaml` file.
- Commits and pushes the changes to the new branch.
- Creates a pull request to merge the new branch into `main`.

### **3️⃣ Merge and Approve Changes**
- The pull request for the updated `deployment.yaml` is reviewed and approved.
- Once approved, changes are merged into the `main` branch.

### **4️⃣ Deploy with ArgoCD**
- ArgoCD detects the changes in the `main` branch of the `helm-gke-deployment` repository.
- Automatically syncs the updated configuration to the target Kubernetes cluster.
- Deploys the updated application to GKE, ensuring the desired state matches the declared configuration.


``` mermaid
flowchart LR
    A[🎨 Changes made to cicd-python-app] --> B[📝 PR created]
    B --> C[✅ PR approved]
    C --> D[⚙️ GHA workflow triggers]
    D --> E[📦 Builds and pushes the image to Docker]
    D --> F[🔄 Creates a PR to update deployment.yaml in helm-gke-deployment]
    F --> G[✅ PR approved for deployment.yaml update]
    G --> H[🚀 ArgoCD picks up the changes]
    H --> I[🌐 Deploys updated application to GKE]

    %% Styling for nodes
    style A fill:#f9f,stroke:#333,stroke-width:2,color:#000
    style B fill:#ff9,stroke:#333,stroke-width:2,color:#000
    style C fill:#9f9,stroke:#333,stroke-width:2,color:#000
    style D fill:#9cf,stroke:#333,stroke-width:2,color:#000
    style E fill:#ffcccb,stroke:#333,stroke-width:2,color:#000
    style F fill:#fdd,stroke:#333,stroke-width:2,color:#000
    style G fill:#d4ffcc,stroke:#333,stroke-width:2,color:#000
    style H fill:#d9edf7,stroke:#333,stroke-width:2,color:#000
    style I fill:#d1ecf1,stroke:#333,stroke-width:2,color:#000

```
---

## ⚙️ Secrets Configuration

Ensure that the following secrets are configured in your GitHub repository settings:
- `DOCKER_USERNAME` - Your Docker Hub username.
- `DOCKER_TOKEN` - Your Docker Hub token for authentication.
- `TOKEN` - Personal access token for GitHub.

---

## 🎨 Example Update in `values.yaml`
```yaml
image:
  repository: my-fastapi-image
  tag: abc1234  # Updated with the commit SHA
```

---

## 🔧 How to Use

1. Create a pull request targeting the `main` branch.
2. Once the pull request is **approved** and **merged**, the workflow will:
   - Build and push the Docker image.
   - Update the Helm chart with the new image tag.
   - Create a pull request to update the `deployment.yaml` file.
3. Merge the pull request created by the workflow to apply the changes.
4. ArgoCD detects the change in deployment.yaml and applies the update to the GKE cluster.  

---

## 🎯 Benefits
- Automates Docker image builds and pushes.
- Keeps Helm chart deployments up to date with the latest image tags.
- Saves time by automating the manual update process.

---

## 🔧 Future Enhancements

Here are some suggested improvements for this workflow:

- 🔍 **Integrate vulnerability scanning** before building the Docker image.
- ✅ **Add automated testing** to ensure the Docker image is functional before pushing.
- 📊 **Add resource usage monitoring** during the build process to optimize performance.
- 🚦 **Add notifications** to alert the team when a pull request is created or merged.

---

## 🚀 Let's automate your deployments!
