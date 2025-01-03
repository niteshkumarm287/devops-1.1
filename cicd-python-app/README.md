
# Login Page with FastAPI, Docker, and CI 🚀

---

## Overview

This repository contains a FastAPI-based application showcasing a modern login page. The project integrates with Docker, a CI pipeline using GitHub Actions (GHA), and Google Cloud Artifact Registry (GCR) for seamless deployment.

---

### Project Structure 📁

```
ci-python-app/
├── app/
│   ├── main.py            # FastAPI application with login page
│   └── __init__.py   
├── Dockerfile             # Multi-stage Dockerfile for building the FastAPI app
├── compose.yml            # Docker Compose configuration
├── requirements.txt   # Python dependencies
```

---

## Prerequisites 🔧

1. **Google Cloud Setup**:
   - Enable Artifact Registry API in your GCP project.
   - Create a service account and configure Workload Identity Federation.

2. **Docker**:
   - Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and enable Kubernetes support if required.

3. **GitHub Setup**:
   - Store the `workload_identity_provider` and `service_account` information in the GitHub repository secrets.

---

## Instructions 🛠️

### 1. Local Development and Testing

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/cicd-python-app.git
   cd cicd-python-app
   ```

2. Install Python dependencies locally (optional):
   ```bash
   pip install -r app/requirements.txt
   ```

3. Run the application locally:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the app in your browser at `http://127.0.0.1:8000`.

---

### 2. Build and Run Dockerized Application 🐳

1. Build the Docker image:
   ```bash
   docker build -t login-app:latest .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 login-app:latest
   ```

3. Access the app at `http://localhost:8000`.

---

### 3. Use Docker Compose for Local Deployment 🧩

1. Start the application:
   ```bash
   docker-compose -f compose.yml up
   ```

2. Stop the application:
   ```bash
   docker-compose -f compose.yml down
   ```

---

### 4. CI Workflow with GitHub Actions ⚡

The GitHub Actions pipeline is configured to:
1. Build the Docker image upon pushing changes to the `main` branch.
2. Authenticate with GCP using Workload Identity Federation.
3. Push the built image to Google Artifact Registry.

#### How It Works:
- On every `git push` to the `main` branch:
  - The GHA pipeline (`.github/workflows/gha.yml`) is triggered.
  - The Docker image is built and pushed to GCR.
- Use the Docker image in your GKE or cloud deployment.

#### Triggering the Workflow:
1. Push changes to the repository:
   ```bash
   git add .
   git commit -m "Updated FastAPI login app"
   git push origin main
   ```

2. Verify the image in Google Artifact Registry:
   - Navigate to `Artifact Registry > Repositories > simple-application`.

---

## Features ✨

1. **Interactive Login Page**:  
   - A visually appealing login form with responsive design and animations.

2. **FastAPI Backend**:  
   - Serves the dynamic login page at the root endpoint (`/`).

3. **Dockerized Application**:  
   - Multi-stage Dockerfile ensures lightweight, production-ready images.

4. **CI/CD Pipeline**:  
   - Automated Docker image builds and pushes to Google Artifact Registry using GitHub Actions.

5. **Docker Compose Support**:  
   - Simplifies local development with container orchestration and port mapping.

6. **Google Cloud Integration**:  
   - Fully compatible with Google Cloud services, enabling streamlined deployment workflows.

---

## Future Enhancements 🚀

- Add endpoints for user authentication and database integration (e.g., Cloud SQL).
- Implement a Helm chart for Kubernetes deployment.
- Secure API using OAuth or JWT.

---

## 🏆 Credits
This project was inspired by and incorporates elements from [fastapi](https://github.com/docker/awesome-compose/tree/master/fastapi), which has been generously made available under the CC0 1.0 Universal License.

Under this license, the authors have waived all copyright and related rights to the work to the fullest extent permitted by law. We are deeply grateful for their contribution to the open-source community. For details on the license, please visit CC0 1.0 Universal.

---  

Feel free to extend or modify based on your deployment needs. Happy coding! 🎉
