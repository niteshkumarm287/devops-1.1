## ArgoCD Kubernetes Deployment Setup 🚀

This repository contains the necessary Kubernetes configurations to deploy a sample application using ArgoCD for continuous deployment. The deployment involves persistent volumes and a simple NGINX-based containerized application.

### Prerequisites 🛠️

Before using this setup, ensure you have the following tools installed:

* kubectl 🔧
* ArgoCD 💻
* A Kubernetes cluster (local or cloud-based) ☁️
* GitHub repository integration with ArgoCD 📂

### Installing ArgoCD 🚀

To install ArgoCD in your Kubernetes cluster, run the following commands:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f [https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml](https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml) 
```

This will set up ArgoCD in the argocd namespace.

Note: The service.yaml file is for exposing ArgoCD, not for the application itself.

service.yaml
```
apiVersion: v1
kind: Service
metadata:
  name: argocd-server
  namespace: argocd
  labels:
    app.kubernetes.io/name: argocd-server
    app.kubernetes.io/part-of: argocd
spec:
  type: LoadBalancer
  ports:
    - name: http
      port: 80
      targetPort: 8080
    - name: https
      port: 443
      targetPort: 8080
  selector:
    app.kubernetes.io/name: argocd-server
```

### Application Deployment via ArgoCD 📦
The files below define the resources needed for deploying an application that uses a persistent volume:

- deployment.yaml: Defines the Kubernetes deployment for the application. 🏗️
- pv.yaml: Defines a persistent volume. 💾
- pvc.yaml: Defines a persistent volume claim to attach to the deployment. 📂
- service.yaml: Exposes the ArgoCD server. 🌐

### File Descriptions 📑
deployment.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pvc-pod-deployment
  labels:
    app: pvc-pod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: pvc-pod
  template:
    metadata:
      labels:
        app: pvc-pod
    spec:
      containers:
        - name: pvc-pod-container
          image: nginx:latest
          volumeMounts:
            - mountPath: /data
              name: data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: demo-pvc
```

pv.yaml
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: demo-pv
spec:
  accessModes:
    - ReadWriteOnce
  capacity:
    storage: 15Mi
  storageClassName: standard
  hostPath:
    path: /tmp/demo-pv
```

pvc.yaml
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: demo-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Mi
  storageClassName: standard
  volumeName: demo-pv
```

### ArgoCD Application Structure 📊
This diagram represents the structure of the ArgoCD application configuration.

![image](https://github.com/user-attachments/assets/7e5918e0-3023-4658-8821-4b4249bb9287)


### Deployment with ArgoCD ⚙️
Once you’ve set up your Kubernetes environment and ArgoCD, follow these steps to deploy the configurations:

- Push the YAML files to your GitHub repository. 📤
- In ArgoCD, create a new application that points to your GitHub repository. 📲
- ArgoCD will sync the repository and deploy the resources defined in the YAML files. 🔄

### Conclusion 🎉
This setup allows you to deploy a simple Kubernetes application with persistent storage using ArgoCD for GitOps-based continuous deployment. The ```service.yaml``` file exposes the ArgoCD UI, not the application itself, ensuring a secure and flexible deployment process.
