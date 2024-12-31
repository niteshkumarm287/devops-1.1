
# 📦 PVC Pod Deployment & 🔥 Load Testing

This README provides a guide for 🚀 deploying a Kubernetes pod with Persistent Volume (PV) 📂 & Persistent Volume Claim (PVC) 📝, verifying volume persistence 🛠️, and running load tests 📊 on the pod.

---

## 🛠️ Deployment Components

### 1. **📂 PersistentVolume (PV)**
The `pv.yaml` file defines a PersistentVolume resource.

#### ⚙️ Configuration:
- **🔑 Access Mode**: `ReadWriteOnce`
- **📦 Capacity**: `15Mi`
- **📚 Storage Class**: `standard`
- **📍 Path**: `/tmp/demo-pv`

```yaml
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

### 2. **📑 PersistentVolumeClaim (PVC)**
The `pvc.yaml` file defines a PersistentVolumeClaim to request storage from the PV.

#### ⚙️ Configuration:
- **🔑 Access Mode**: `ReadWriteOnce`
- **📦 Requested Storage**: `10Mi`
- **📚 Storage Class**: `standard`

```yaml
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

### 3. **🚀 Pod**
The `pod.yaml` file deploys a Pod that mounts the PVC at `/data`.

#### ⚙️ Configuration:
- **📦 Container Image**: `nginx:latest`
- **📂 Volume Mount**: `/data`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pvc-pod
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

---

## 🧩 Deployment Steps

### 1. **📂 Create PersistentVolume**
```bash
kubectl apply -f pv.yaml
```

### 2. **📑 Create PersistentVolumeClaim**
```bash
kubectl apply -f pvc.yaml
```

### 3. **🚀 Deploy the Pod**
```bash
kubectl apply -f pod.yaml
```

### 4. **🔍 Verify Deployment**
Check the status of the PV, PVC, and Pod:
```bash
kubectl get pv
kubectl get pvc
kubectl get pods
```

---

## 🔍 Testing Volume Persistence

### 1. **🖋️ Create Files in the Mounted Volume**
Exec into the pod and create files in the `/data` directory:
```bash
kubectl exec -it pvc-pod -- /bin/sh
# Inside the pod:
cd /data
echo "Test file" > testfile.txt
ls
```

### 2. **♻️ Delete and Recreate the Pod**
Delete the pod and redeploy:
```bash
kubectl delete pod pvc-pod
kubectl apply -f pod.yaml
```

### 3. **🗂️ Verify Files Persist**
Exec into the new pod instance and check if the files exist:
```bash
kubectl exec -it pvc-pod -- /bin/sh
# Inside the pod:
ls /data
cat /data/testfile.txt
```

---

## ⚡ Load Testing

### 1. **🏋️‍♀️ Run Load Locally in the Pod**
Exec into the pod:
```bash
kubectl exec -it pvc-pod -- /bin/sh
```
Run load tests from within the pod:

#### 🔄 Continuous Requests:
```bash
while true; do curl -s http://localhost > /dev/null; done
```

#### 🧵 Concurrent Requests:
```bash
seq 1 1000 | xargs -n1 -P10 curl -s http://localhost > /dev/null
```

### 2. **📊 Monitor Resource Usage**
Check the pod’s CPU and memory utilization:
```bash
kubectl top pod pvc-pod
```

---

## 🧹 Cleanup

To delete all resources:
```bash
kubectl delete pod pvc-pod
kubectl delete pvc demo-pvc
kubectl delete pv demo-pv
```

---

## 📝 Notes
- Ensure the storage backend supports `hostPath` (e.g., for testing purposes on a local cluster).
- For production environments, use a cloud-based storage solution instead of `hostPath`.
- Monitor the pod’s performance and scale as needed for sustained load scenarios.

---

This guide demonstrates a basic setup for Kubernetes persistent storage and load testing. For more advanced configurations, consider using StatefulSets, custom monitoring tools, or scaling mechanisms.
