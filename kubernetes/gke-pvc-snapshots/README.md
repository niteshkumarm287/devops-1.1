
# 📦 GKE PVC Snapshots with HPA, Grafana, and Prometheus Integration

This project demonstrates how to deploy and manage Kubernetes applications in GKE using Persistent Volumes (PVs), Persistent Volume Claims (PVCs), Horizontal Pod Autoscalers (HPA), and monitoring tools such as Prometheus and Grafana.

## 📂 Folder Structure

Here is an overview of the files in the `gke-pvc-snapshots` folder:

1. **`deployment.yaml`**: Defines the deployment of a sample application using a PVC for data storage.
2. **`Grafana.yaml`**: Sets up Grafana with a PVC for persistent data storage.
3. **`hpa.yaml`**: Configures an HPA to scale the application based on CPU utilization.
4. **`pv.yaml`**: Defines a Persistent Volume (PV) to provide storage.
5. **`pvc.yaml`**: Configures a Persistent Volume Claim (PVC) to request storage from the PV.
6. **`service.yaml`**: Creates a LoadBalancer service to expose the application to external traffic.

## 🚀 Deployment Guide

### 1. **Create Persistent Volume and Claim**
Apply the `pv.yaml` and `pvc.yaml` files to set up persistent storage.

```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```

### 2. **Deploy the Application**
Use the `deployment.yaml` file to deploy the sample application.

```bash
kubectl apply -f deployment.yaml
```

### 3. **Set Up the Service**
Expose the application with the `service.yaml` file.

```bash
kubectl apply -f service.yaml
```

### 4. **Configure Horizontal Pod Autoscaler (HPA)**
Deploy the HPA to scale pods based on CPU utilization.

```bash
kubectl apply -f hpa.yaml
```

To test the HPA, run the following command in one of the pods to simulate high CPU usage:

```bash
kubectl -n <namespace> exec -it <pod-name> -- /bin/sh -c "yes > /dev/null"
```

### 5. **Deploy Grafana**
Set up Grafana with persistent storage using the `Grafana.yaml` file.

```bash
kubectl apply -f Grafana.yaml
```

Access Grafana through the exposed service and add Prometheus as a data source.

### 6. **Set Up Prometheus**
Install Prometheus using Helm:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

### 7. **Integrate Grafana with Prometheus**
Add Prometheus as a data source in Grafana to enable monitoring and visualization.

## 📊 Monitoring and Scaling

- **HPA**: Automatically adjusts the number of pods to maintain CPU utilization at 50%.
- **Prometheus and Grafana**: Monitor application metrics and visualize data.

## 📥 Downloadable Files

[Click here to download all YAML files](https://github.com/niteshkumarm287/devops-1.1/archive/main.zip)

## 📝 Notes

- Replace `<namespace>` and `<pod-name>` with your actual namespace and pod name.
- Modify resource requests and limits as per your application's requirements.
- For secure access, configure authentication for Grafana and Prometheus.

Enjoy setting up your Kubernetes cluster! 🚀
