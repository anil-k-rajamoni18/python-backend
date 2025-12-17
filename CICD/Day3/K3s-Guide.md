# 🚀 K3s Crash Course – In-Depth Notes

## 1️⃣ What is K3s?

K3s is a lightweight, certified Kubernetes distribution created by Rancher (SUSE).

### Why K3s exists

**Traditional Kubernetes:**
- Needs 2–4 GB RAM minimum
- Many components (etcd, controller, scheduler, kubelet, kube-proxy)

**K3s:**
- Runs in ~512MB RAM
- Single binary
- Simplified installation
- Perfect for edge, IoT, dev, labs, EC2 free tier

👉 CNCF certified → Fully Kubernetes-compliant.

## 2️⃣ K3s vs Kubernetes (kubeadm)

| Feature | Kubernetes | K3s |
|---------|-----------|-----|
| Binary | Multiple | Single |
| Memory | High | Very Low |
| etcd | External | Embedded SQLite / etcd |
| Install | Complex | One command |
| Cloud | Heavy | Edge + Cloud |
| Production | Yes | Yes |

💡 **Rule:**
- Learning / low memory → K3s
- Large enterprise → Full K8s

## 3️⃣ K3s Architecture

### Control Plane Components (Built-in)
- API Server
- Controller Manager
- Scheduler
- Cloud Controller Manager
- kubelet
- kube-proxy

### Storage Options
- **Default:** SQLite
- **Production:**
  - etcd
  - MySQL
  - PostgreSQL

### Networking
- **Default CNI:** Flannel
- **Others:** Calico, Cilium (advanced)

## 4️⃣ K3s Installation (Single Node)

### ✅ System Requirements
- Linux (Ubuntu 20.04+ recommended)
- 512MB RAM (1GB better)
- 1 CPU
- Root access

### 🔹 Install K3s (1 command)

```bash
curl -sfL https://get.k3s.io | sh -
```

✔ Installs  
✔ Starts service  
✔ Configures kubectl

### 🔹 Check Status

```bash
sudo k3s kubectl get nodes
```

OR

```bash
kubectl get nodes
```

Expected output:

```
NAME     STATUS   ROLES                  AGE
node1    Ready    control-plane,master   1m
```

## 5️⃣ K3s File Locations

| Purpose | Path |
|---------|------|
| Binary | /usr/local/bin/k3s |
| Config | /etc/rancher/k3s |
| kubeconfig | /etc/rancher/k3s/k3s.yaml |
| Data | /var/lib/rancher/k3s |

## 6️⃣ K3s Services

```bash
sudo systemctl status k3s
```

Stop / Start:

```bash
sudo systemctl stop k3s
sudo systemctl start k3s
```

## 7️⃣ kubectl with K3s

### Export kubeconfig

```bash
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

### Verify

```bash
kubectl cluster-info
```

## 8️⃣ Deploy Your First Application

### 🔹 NGINX Deployment

```bash
kubectl create deployment nginx --image=nginx
```

Check:

```bash
kubectl get pods
```

### 🔹 Expose as Service

```bash
kubectl expose deployment nginx \
  --type=NodePort \
  --port=80

kubectl get svc
```

Access:

```
http://<node-ip>:<node-port>
```

## 9️⃣ Pods, Deployments & Services (Quick Recap)

### Pod
- Smallest unit
- Runs containers

### Deployment
- Manages replicas
- Handles rolling updates

### Service
- Exposes pods
- **Types:**
  - ClusterIP
  - NodePort
  - LoadBalancer

## 🔟 Ingress in K3s (Very Important)

K3s comes with **Traefik Ingress Controller** by default.

### Sample Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
  - host: nginx.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx
            port:
              number: 80
```

Add to `/etc/hosts`:

```
<node-ip> nginx.local
```

## 1️⃣1️⃣ Storage in K3s

### Default Storage Class

```bash
kubectl get storageclass
```

Output:

```
local-path (default)
```

### PVC Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

## 1️⃣2️⃣ Multi-Node K3s Cluster

### Install Server (Master)

```bash
curl -sfL https://get.k3s.io | sh -
```

Get token:

```bash
sudo cat /var/lib/rancher/k3s/server/node-token
```

### Install Agent (Worker)

```bash
curl -sfL https://get.k3s.io | K3S_URL=https://<server-ip>:6443 K3S_TOKEN=<token> sh -
```

Check:

```bash
kubectl get nodes
```

## 1️⃣3️⃣ K3s on EC2 (Free Tier Friendly)

### Recommended Instance
- t2.micro / t3.micro
- Ubuntu 22.04
- 8–20GB disk

### Open Ports
- 6443 (API server)
- 80 / 443 (Ingress)

## 1️⃣4️⃣ Disable Default Components (Advanced)

Disable Traefik:

```bash
curl -sfL https://get.k3s.io | sh -s - --disable traefik
```

Disable Flannel:

```bash
--flannel-backend=none
```

## 1️⃣5️⃣ Uninstall K3s

**Server:**

```bash
/usr/local/bin/k3s-uninstall.sh
```

**Agent:**

```bash
/usr/local/bin/k3s-agent-uninstall.sh
```

## 1️⃣6️⃣ K3s vs Minikube vs Kind

| Tool | Best For |
|------|----------|
| K3s | Low memory, EC2, edge |
| Minikube | Local dev |
| Kind | CI/CD testing |

🏆 **Best overall for learning on low RAM** → K3s

## 1️⃣7️⃣ Real-World Use Cases

- Edge computing
- IoT clusters
- Dev/Test clusters
- CI pipelines
- Lightweight production workloads

## 1️⃣8️⃣ Interview Questions (Quick)

**Q1. Why K3s?**  
👉 Lightweight, fast, single binary Kubernetes

**Q2. Default DB?**  
👉 SQLite

**Q3. Default Ingress?**  
👉 Traefik

**Q4. Can K3s be production?**  
👉 Yes

**Q5. Difference between K3s and K8s?**  
👉 Same API, smaller footprint