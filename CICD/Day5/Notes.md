# 📘 DAY 5 — Kubernetes Advanced (Medium Level) — In-Depth Session Notes

## 1️⃣ StatefulSets

### What are Stateful Applications?

Stateful apps require:

- Stable network identity
- Stable storage
- Ordered deployment
- Ordered scaling

**Examples:**

✔ Databases (PostgreSQL, MySQL)  
✔ Message brokers (RabbitMQ, Kafka)  
✔ Caches (Redis with persistence)

### What are StatefulSets in Kubernetes?

StatefulSet is a Kubernetes controller designed for stateful workloads.

### StatefulSet Unique Features

| Feature | Description |
|---------|-------------|
| Stable names | Pods get predictable names: pod-0, pod-1, pod-2 |
| Stable storage | Each replica gets its own PVC (data-pod-0, data-pod-1) |
| Ordered startup | Starts pods sequentially |
| Ordered scaling | Terminates pods reverse order |
| No rolling updates by default | Requires careful configuration |

### StatefulSet Example

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: pg-db
spec:
  serviceName: "postgres"
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:15
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 5Gi
```

## 2️⃣ Persistent Volumes (PV) & Persistent Volume Claims (PVC)

### Why Persistent Storage?

- Pods are ephemeral
- Need storage that outlives pod lifecycle
- Required by stateful services

### Persistent Volume (PV)

- Actual storage
- Pre-provisioned or dynamically provisioned
- Could be backed by:
  - AWS EBS
  - GCP Persistent Disk
  - NFS
  - HostPath

### PV Example

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

### Persistent Volume Claim (PVC)

- Pod's request for storage
- Binds to a PV automatically if matching size + access modes

### PVC Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

### How PV/PVC Works:

```
PVC → Claims Storage → Binds to PV → Mounted into Pod
```

## 3️⃣ Horizontal Pod Autoscaler (HPA)

### What is HPA?

HPA automatically scales pod replicas based on:

- CPU utilization
- Memory utilization
- Custom metrics
- External metrics

### Why HPA?

- Handle traffic spikes
- Save cost
- Improve resilience

### HPA Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 60
```

## 4️⃣ Metrics Server

### Why Do We Need Metrics Server?

HPA works ONLY if Metrics Server is installed:

- Collects resource metrics from Kubelet
- Provides CPU/Memory metrics to Kubernetes API

### Install Metrics Server (Minikube/Kubernetes Lab)

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Test Metrics Server

```bash
kubectl top pods
kubectl top nodes
```

## 5️⃣ ServiceAccounts & RBAC Basics

### What is RBAC?

Role-Based Access Control:
Controls who can do what inside Kubernetes.

### Three main objects in RBAC

| Object | Purpose |
|--------|---------|
| Role/ClusterRole | Define permissions |
| RoleBinding/ClusterRoleBinding | Assign roles to subjects |
| ServiceAccount | Identity for pods |

### ServiceAccount Example

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
```

### Role + RoleBinding Example

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
  - apiGroups: [""] 
    resources: ["pods"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods-binding
subjects:
  - kind: ServiceAccount
    name: app-sa
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

This allows the service account to read pods only.

## 🧪 Hands-On Labs (Day 5)

### ✔ Create PV + PVC

- Create a 5Gi PV
- Bind a PVC to it
- Mount it into a Pod

### ✔ Build a Stateful Database (PostgreSQL)

- Deploy PostgreSQL using StatefulSet
- Use PVC templates
- Verify persistent data

### ✔ Install Metrics Server

- Apply metrics server manifests
- Validate HPA metrics

### ✔ Configure HPA

- Deploy a demo API
- Apply HPA
- Simulate load using:

```bash
kubectl run -it load --image=busybox -- /bin/sh
```

- Observe autoscaling

## 🧱 Mini Project (Day 5)

### ⚙️ Fully Scalable Microservice with Autoscaling + Persistent DB

**Requirements**

- Deploy a microservice backend
- Deploy PostgreSQL using StatefulSet
- Create PV/PVC for database storage
- Install & verify metrics-server
- Create an HPA for microservice
- Test autoscaling under load

### Architecture

```
        +--------------+
        |    Client    |
        +------+-------+
               |
           Ingress
               |
    +-----------------------+
    | Scalable API Service |
    |   (Deployment + HPA) |
    +----------+------------+
               |
           PostgreSQL
      (StatefulSet + PVC)
```