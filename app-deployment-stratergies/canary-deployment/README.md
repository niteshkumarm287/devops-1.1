
# Canary Deployment with Kubernetes 🚀

This repository contains Kubernetes manifests for deploying a canary deployment setup. The deployment includes two versions of an application (v1 and v2), an NGINX ingress controller for traffic splitting, and a service to expose the application.

---

## **Folder Structure** 📂

- `deployment.yaml`: Defines two deployments for the application, one for version `v1` and another for version `v2`.
- `service.yaml`: Defines a service to expose the deployments.
- `ingress.yaml`: Configures an NGINX ingress controller to route traffic to the different application versions based on specified rules.

---

## **Deployment Overview** 📜

### **Deployment Files**

#### `deployment.yaml`
- **Version v1**
  - Replica count: `1`
  - Image: `nitesh287/my-fastapi-image-1:30a7404`
  - Container port: `80`

- **Version v2**
  - Replica count: `1`
  - Image: `nitesh287/fastapi:v1`
  - Container port: `80`

#### `service.yaml`
- **Type**: ClusterIP (default)
- **Selector**: Matches all pods labeled with `app: canary-deployment`
- **Port Mapping**: Exposes port `80`.

#### `ingress.yaml`
- **Ingress Class**: NGINX
- **Annotations**:
  - `nginx.ingress.kubernetes.io/canary-by-header`: Routes traffic based on the `X-Canary` header.
  - `nginx.ingress.kubernetes.io/canary-by-header-value`: Routes traffic with header value `v2` to the canary deployment.
  - `nginx.ingress.kubernetes.io/canary-weight`: Routes `20%` of traffic to version `v2`.

---

## **Deployment Steps** 🛠️

### **Step 1: Apply the Manifests**

1. **Create the Deployments**:
   ```bash
   kubectl apply -f deployment.yaml
   ```

2. **Create the Service**:
   ```bash
   kubectl apply -f service.yaml
   ```

3. **Create the Ingress**:
   ```bash
   kubectl apply -f ingress.yaml
   ```

### **Step 2: Verify the Deployment**

1. **Check Deployments**:
   ```bash
   kubectl get deployments
   ```

2. **Check Pods**:
   ```bash
   kubectl get pods
   ```

3. **Check Service**:
   ```bash
   kubectl get service
   ```

4. **Check Ingress**:
   ```bash
   kubectl get ingress
   ```

---

## **Improvements** 📈

1. **Automated Canary Analysis**
   - Integrate tools like Flagger for advanced traffic shaping and metrics-based canary analysis.

2. **Monitoring**
   - Use tools like Prometheus and Grafana to monitor metrics from both versions.

3. **Testing**
   - Implement automated testing for canary releases to detect issues early.

4. **Dynamic Weight Adjustment**
   - Use scripts or tools to dynamically adjust canary weights based on live feedback.

---

## **Reference Documentation** 📚

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [NGINX Ingress Controller Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)
- [Canary Deployments in Kubernetes](https://martinfowler.com/bliki/CanaryRelease.html)
