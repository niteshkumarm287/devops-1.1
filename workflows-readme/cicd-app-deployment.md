
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

---

## 🎯 Benefits
- Automates Docker image builds and pushes.
- Keeps Helm chart deployments up to date with the latest image tags.
- Saves time by automating the manual update process.

---

## 🚀 Let's automate your deployments!
