# 📘 DAY 3 — Kubernetes Basics (Local with Minikube or Kind)

Introduction to Kubernetes architecture, core objects, and kubectl hands-on.

## 1️⃣ Kubernetes Architecture: Master & Worker Nodes

Kubernetes is a container orchestration platform that automates deployment, scaling, and management of containerized applications.

K8s clusters consist of **Master (Control Plane)** and **Worker Nodes**.

### 🔹 Control Plane Components (Master Node)

Responsible for managing the entire cluster.

#### 1. API Server (kube-apiserver)

- Front-end of the control plane
- Receives all commands (kubectl)
- Central communication hub

#### 2. Scheduler (kube-scheduler)

- Decides which node a pod should run on
- Based on CPU, memory, taints, affinity, etc.

#### 3. Controller Manager

Runs background controllers:

- Deployment controller
- ReplicaSet controller
- Node controller
- Job controller

#### 4. etcd

- Distributed key-value store
- Stores all cluster state (desired + actual state)
- Heart of the cluster

### 🔹 Worker Node Components

#### 1. Kubelet

- Agent running on each worker node
- Ensures containers/pods are running as expected
- Talks to the API server

#### 2. Kube-proxy

- Manages networking & iptables
- Enables communication between services & pods

#### 3. Container Runtime

Examples:

- Docker
- containerd
- CRI-O

Responsible for running containers.

## 2️⃣ Core Kubernetes Objects

### 🔹 Pods

- Smallest deployable unit in Kubernetes
- Usually 1 container per pod
- Ephemeral—lost if node dies unless managed by higher-level objects

**Example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: app
      image: nginx
```

### 🔹 ReplicaSets

- Ensure a specified number of pod replicas are running
- Self-healing (recreates pods if deleted)

**Example:**

```yaml
kind: ReplicaSet
```

### 🔹 Deployments

- Most commonly used controller
- Manages ReplicaSets
- Supports rolling updates & rollbacks

**Example:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: nginx
          image: nginx
```

### 🔹 Services

Expose applications running inside the cluster.

**Types:**

| Service Type | Use Case |
|--------------|----------|
| ClusterIP | Internal service (default) |
| NodePort | Exposes app on `<NodeIP>:<Port>` |
| LoadBalancer | Cloud provider external LB |
| Headless | DNS-based service for statefulsets |

**Example Service (NodePort):**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
  type: NodePort
```

## 3️⃣ Kubeconfig

The kubeconfig file stores:

- Cluster credentials
- API server URL
- User authentication
- Contexts

**Default location:**

```
~/.kube/config
```

**Switch contexts:**

```bash
kubectl config use-context minikube
```

## 4️⃣ kubectl Basics

### Apply Manifest

```bash
kubectl apply -f deployment.yaml
```

### View Pods

```bash
kubectl get pods
kubectl get pods -o wide
```

### Describe a Pod

```bash
kubectl describe pod <pod-name>
```

### View Logs

```bash
kubectl logs <pod-name>
```

### Exec into Pod

```bash
kubectl exec -it <pod> -- sh
```

## 5️⃣ Hands-On Labs

### ✔ Install Minikube

**Commands:**

Start cluster:

```bash
minikube start
```

Verify:

```bash
kubectl get nodes
```

### ✔ Deploy a Simple App (Deployment)

Create file `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
        - name: hello
          image: nginx
          ports:
            - containerPort: 80
```

Apply:

```bash
kubectl apply -f deployment.yaml
```

### ✔ Expose as NodePort Service

```bash
kubectl expose deployment hello-app --type=NodePort --port=80
```

Get service:

```bash
kubectl get svc
```

Access App:

```bash
minikube service hello-app
```

## 6️⃣ Mini Project — Kubernetes Deployment + Service

### 🔥 Deploy a Real App on Kubernetes (Simple API + NodePort)

**Goal**

Deploy a real API on Kubernetes & expose it externally.

**Steps**

#### 1. Create Deployment (e.g., FastAPI, Node, or Nginx)

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: nginx
          ports:
            - containerPort: 80
```

#### 2. Create Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  type: NodePort
  selector:
    app: api
  ports:
    - targetPort: 80
      port: 80
      nodePort: 30001
```

#### 3. Deploy Everything

```bash
kubectl apply -f api-deployment.yaml
kubectl apply -f api-service.yaml
```

#### 4. Access the App

```bash
minikube service api-service
```