
# 🚀 Deploying a Python Flask App on GKE with 🌐 Load Balancer

## 📝 Overview

This guide explains how to deploy a simple Flask application on **Google Kubernetes Engine (GKE)** and expose it to the public using a 🌐 Load Balancer Service. 

---

## 🛠️ Application Code

The application is a basic Flask web app that responds with "welcome" when accessed.

### 🐍 Flask Application (`main.py`)

```python
from flask import Flask # type: ignore
app = Flask(__name__)
@app.route('/')
def index():
    return 'welcome'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

---

## 🐳 Dockerfile

The application is containerized using the following Dockerfile:

```Dockerfile
FROM python:3.13.1-slim-bookworm
RUN pip install flask
WORKDIR /myapp
COPY main.py /Docker/main.py
CMD [ "python", "/Docker/main.py" ]
```

---

## 📦 Steps to Deploy on GKE

### 1. 🔑 Prerequisites

1. A Google Cloud account with a GKE cluster set up.
2. The `gcloud` CLI installed and configured.
3. Docker installed locally for building the container image.
4. Kubernetes CLI (`kubectl`) configured to interact with your GKE cluster.

---

### 2. 🏗️ Build and Push the Docker Image

1. **Build the Docker image:**
   ```bash
   docker build -t gcr.io/<your-project-id>/flask-app:v1 .
   ```

2. **Authenticate Docker with Google Cloud:**
   ```bash
   gcloud auth configure-docker
   ```

3. **Push the image to Google Container Registry (GCR):**
   ```bash
   docker push gcr.io/<your-project-id>/flask-app:v1
   ```

---

### 3. 🛡️ Deploy the Application to GKE

#### a. Create a Deployment YAML file (`deployment.yaml`)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
  labels:
    app: flask-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-app
        image: gcr.io/<your-project-id>/flask-app:v1
        ports:
        - containerPort: 8080
```

#### b. Create a Service YAML file (`service.yaml`)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-app-lb
spec:
  type: LoadBalancer
  selector:
    app: flask-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

---

### 4. 🛠️ Apply Kubernetes Configurations

1. **Deploy the application:**
   ```bash
   kubectl apply -f deployment.yaml
   ```

2. **Expose the application using a Load Balancer:**
   ```bash
   kubectl apply -f service.yaml
   ```

---

### 5. 🌐 Access the Application

1. Run the following command to get the external IP of the Load Balancer:
   ```bash
   kubectl get service flask-app-lb
   ```

2. Access the app in your browser using the external IP:
   ```
   http://<EXTERNAL-IP>
   ```

---

## ⚙️ Best Practices

1. **📈 Scaling:** Adjust the `replicas` in `deployment.yaml` for scaling.
2. **📊 Monitoring:** Use Google Cloud Monitoring and Logging to monitor the application.
3. **🔒 Security:** Secure the Load Balancer with HTTPS by setting up an SSL certificate.
4. **📂 Namespace:** Use namespaces for better resource segregation in Kubernetes.

---

## 🧹 Clean-Up

To avoid incurring charges, delete the resources when you're done:
```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
```

---

