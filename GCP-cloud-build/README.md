
# 🚀 GCP DevOps Project

Welcome to the **GCP DevOps Project** repository! This project demonstrates building, pushing, and deploying a simple Python Flask application to a GKE cluster using Cloud Build. 🎉

## 📂 Project Structure

Here's the folder structure of the project:

```
GCP-cloud-build/
├── Docker/
│   ├── Dockerfile
│   └── main.py
├── cloudbuild.yaml
└── deployment.yaml
```

## 🛠️ Components

### 1. **Dockerfile** 🐳

Defines the application environment and dependencies.

```Dockerfile
FROM python:3.13.1-slim-bookworm 
RUN pip install flask
WORKDIR /app
COPY main.py /app/main.py
CMD [ "python", "/app/main.py" ]
```

### 2. **main.py** 🐍

A simple Flask application.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<div style="text-align: center;"><h1>Hello from Nitesh!</h1><p>Welcome to GCP DevOps Course.</p><p></p></div>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
```

### 3. **cloudbuild.yaml** 🔧

Defines steps for CI/CD pipeline using Google Cloud Build.

```yaml
steps:
  - name: "gcr.io/cloud-builders/docker"
    args: ["build", "-t", "gcr.io/$PROJECT_ID/gcpdevops:latest", "GCP-cloud-build/Docker"]
  - name: "gcr.io/cloud-builders/docker"
    args: ["push", "gcr.io/$PROJECT_ID/gcpdevops:latest"]
  - name: "gcr.io/cloud-builders/gke-deploy"
    args:
      - run
      - --filename=GCP-cloud-build/deployment.yaml
      - --image=gcr.io/$PROJECT_ID/gcpdevops:latest
      - --location=us-central1-c
      - --cluster=devops-cluster
      - --namespace=mynamespace

timeout: "1200s"
logsBucket: "gs://cloud-build-demo-2"
serviceAccount: "gha-sa@nitesh-gcp-444718.iam.gserviceaccount.com"
options:
  defaultLogsBucketBehavior: REGIONAL_USER_OWNED_BUCKET
```

### 4. **deployment.yaml** 📜

Defines the deployment configuration for GKE.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-app
  namespace: mynamespace
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-app
  template:
    metadata:
      labels:
        app: simple-app
    spec:
      containers:
        - name: simple-app
          image: gcr.io/nitesh-gcp-444718/gcpdevops:latest
          ports:
            - containerPort: 8080
```

## 🚀 Deployment Process

1. **Build Docker Image**: Cloud Build creates a Docker image from the Dockerfile.
2. **Push to Container Registry**: The image is pushed to Google Container Registry (GCR).
3. **Deploy to GKE**: The image is deployed to a GKE cluster using `gke-deploy`.

## 📋 Logs Summary

- Docker image built successfully.
- Image pushed to GCR: `gcr.io/nitesh-gcp-444718/gcpdevops:latest`.
- Deployment applied to GKE cluster.

## 🔗 Useful Links

- [Workloads](https://console.cloud.google.com/kubernetes/workload?project=nitesh-gcp-444718)
- [Services & Ingress](https://console.cloud.google.com/kubernetes/discovery?project=nitesh-gcp-444718)
- [Applications](https://console.cloud.google.com/kubernetes/application?project=nitesh-gcp-444718)
- [Configuration](https://console.cloud.google.com/kubernetes/config?project=nitesh-gcp-444718)
- [Storage](https://console.cloud.google.com/kubernetes/storage?project=nitesh-gcp-444718)

## 🎯 Key Notes

- Namespace `mynamespace` is created if it doesn't exist.
- Flask app is exposed on port `8080`.

Happy coding! 🧑‍💻🌟
