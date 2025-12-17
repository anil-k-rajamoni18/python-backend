# Kubernetes Practice Options 

## 1️⃣ LOCAL MACHINE (Best for learning & quick practice)

| Tool | What it is | RAM Needed | Use Case |
|------|-----------|------------|----------|
| Minikube | Single-node K8s cluster | 2–4 GB | Beginners, most tutorials |
| Kind (K8s in Docker) | Runs K8s inside Docker containers | ⭐ 1–2 GB | Low memory systems |
| k3s | Lightweight Kubernetes | ⭐ < 1 GB | Edge, low-resource systems |
| Docker Desktop K8s | Built-in K8s | 4–6 GB | Heavy, not recommended |

👉 **Best for low RAM:** k3s or Kind

## 🔹 CLOUD (AWS EC2)

| Option | Cost | RAM | Recommended |
|--------|------|-----|-------------|
| EC2 + k3s | Low | 1–2 GB | ⭐ YES |
| EC2 + kubeadm | Medium | 2–4 GB | For real-world practice |
| EKS | Expensive | Managed | Not for beginners |

👉 **Best on EC2:** k3s on t2.micro / t3.micro

## 2️⃣ BEST CHOICE (Based on Your Requirement)

### ✅ Lowest Memory (Local or EC2)
🥇 **k3s**

### ✅ Easiest & Popular for Practice
🥈 **Minikube**

### ✅ Docker-based & Lightweight
🥉 **Kind**

## 3️⃣ HOW TO INSTALL (STEP-BY-STEP)

### 🟢 OPTION 1: KIND (Best for Low RAM on Local)

**Prerequisites**
- Docker installed
- kubectl installed

**Install Kind**

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/
```

**Create Cluster**

```bash
kind create cluster
```

**Verify**

```bash
kubectl get nodes
```

🟢 **Memory usage:** ~1.5 GB  
🟢 **Perfect for laptop practice**

### 🟢 OPTION 2: K3S (🔥 BEST for Low Memory)

**Local / EC2 Install (Single Command)**

```bash
curl -sfL https://get.k3s.io | sh -
```

**Check status**

```bash
sudo kubectl get nodes
```

👉 **kubeconfig location:**

```bash
sudo cat /etc/rancher/k3s/k3s.yaml
```

🟢 **Memory usage:** ~512 MB – 1 GB  
🟢 **Production-like**

### 🟢 OPTION 3: MINIKUBE (Most Tutorials Use This)

**Install**

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

**Start with low memory**

```bash
minikube start --memory=2048 --cpus=2
```

🟡 **Memory usage:** ~2–3 GB

## 4️⃣ EC2 SETUP (CHEAP & EFFECTIVE)

**Recommended EC2**
- Instance: t3.micro
- OS: Ubuntu 22.04
- RAM: 1 GB
- Disk: 10 GB

**Install k3s on EC2**

```bash
curl -sfL https://get.k3s.io | sh -
```

**Open Security Group Ports**

| Port | Reason |
|------|--------|
| 6443 | Kubernetes API |
| 80, 443 | Services |
| 22 | SSH |

## 5️⃣ WHAT TO PRACTISE (HANDS-ON CHECKLIST)

Start with this order 👇

- ✔ Pods
- ✔ ReplicaSet
- ✔ Deployment
- ✔ Services (ClusterIP, NodePort)
- ✔ ConfigMap & Secrets
- ✔ Volumes
- ✔ Ingress (Nginx)
- ✔ Helm basics
- ✔ Rolling updates
- ✔ Autoscaling (HPA)

## 6️⃣ FINAL RECOMMENDATION (SHORT ANSWER)

| Scenario | Best Tool |
|----------|-----------|
| Low RAM laptop | ⭐ k3s / Kind |
| Beginner learning | Minikube |
| EC2 cheap setup | ⭐ k3s on t3.micro |
| Real-world prod feel | kubeadm |