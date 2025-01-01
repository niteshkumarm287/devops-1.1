# Build and Push Docker Image Workflow

This GitHub Actions (GHA) workflow is designed to automate the process of building and pushing Docker images to Docker Hub. By following best practices, this workflow eliminates the manual overhead of managing Docker image builds, tagging, and pushes.

## Workflow Overview

### **Workflow Name:**
`Build and Push Docker Image`

### **Triggers:**
The workflow is triggered whenever code is pushed to the `main` branch.

### **Jobs:**
1. **Checkout Code**
   - Uses the `actions/checkout@v3` action to clone the repository.

2. **Log in to Docker Hub**
   - Utilizes the `docker/login-action@v2` action to authenticate with Docker Hub using credentials stored as GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_TOKEN`).

3. **Generate Version**
   - Dynamically generates a version number based on the number of commits in the repository (`v{commit_count}`).

4. **Extract Git SHA**
   - Captures the short Git commit SHA to include in the Docker image tag.

5. **Build Docker Image**
   - Builds the Docker image from the `simple_python_app` directory.
   - Generates a unique image tag using:
     - Version (`v{commit_count}`)
     - Git SHA
     - Image SHA
     - Timestamp

6. **Tag Docker Image**
   - Tags the Docker image using the generated image tag format.

7. **Push Docker Image**
   - Pushes the tagged Docker image to the specified Docker Hub repository.

8. **Output Docker Image Tag**
   - Outputs the final Docker image tag for reference.

## Problems Solved by This Workflow

This workflow addresses the following challenges:

1. **Manual Overhead**
   - Automates the tedious process of building, tagging, and pushing Docker images.

2. **Best Practices Compliance**
   - Ensures that Docker images are tagged with meaningful, unique identifiers (version, Git SHA, timestamp, etc.).

3. **Reproducibility**
   - Guarantees consistent and predictable image builds by incorporating Git metadata and timestamps.

4. **Integration with CI/CD**
   - Streamlines the process of integrating Docker image builds into continuous delivery pipelines.

## Usage Instructions

1. Ensure that the repository has the following secrets configured:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_TOKEN`: Your Docker Hub access token.

2. Push changes to the `main` branch to trigger the workflow.

3. Monitor the workflow progress in the GitHub Actions tab.

4. Retrieve the final image tag from the workflow logs or Docker Hub repository.

---

### ✨ **Happy Coding!** 🚀
