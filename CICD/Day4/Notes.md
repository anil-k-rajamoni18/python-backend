# 📘 DAY 4 — Kubernetes Intermediate (Session Notes)

## 1️⃣ ConfigMaps & Secrets

### 🔹 ConfigMaps

Used to store non-sensitive configuration such as:

- Environment variables
- Config files
- Command-line args

### Why ConfigMaps?

- Separate config from container image
- Make deployments reusable
- Update configs without rebuilding images

### Create ConfigMap (Literal)

```bash
kubectl create configmap app-config --from-literal=ENV=dev
```

### Create from File

```bash
kubectl create configmap app-config --from-file=config.json
```

### Use ConfigMap in Pod

```yaml
env:
  - name: ENV
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: ENV
```

### Mount ConfigMap as Volume

```yaml
volumeMounts:
  - name: config
    mountPath: /app/config

volumes:
  - name: config
    configMap:
      name: app-config
```

### 🔹 Secrets

Used for sensitive data like:

- Passwords
- DB credentials
- API keys
- TLS certs

### Secret Encoding

Stored as base64 encoded values (not encrypted by default).
Best stored with:

- Sealed Secrets
- Vault
- KMS

### Create Secret (Literal)

```bash
kubectl create secret generic db-secret \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASS=pass123
```

### Use Secret as env var

```yaml
env:
  - name: DB_USER
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: DB_USER
```

### Use Secret as file

```yaml
volumeMounts:
  - name: secret-vol
    mountPath: /etc/secret

volumes:
  - name: secret-vol
    secret:
      secretName: db-secret
```

## 2️⃣ Ingress & Ingress Controllers (Nginx)

### What is Ingress?

Ingress exposes HTTP/HTTPS applications with:

- Clean URLs (no NodePort)
- Path-based routing
- Host-based routing
- TLS termination

### Why Ingress instead of NodePort?

| Type | Use Case |
|------|----------|
| NodePort | Quick testing |
| LoadBalancer | Cloud environments |
| Ingress | Production-grade routing, clean URLs |

### Ingress Controller

Ingress requires a controller, e.g.:

- NGINX Ingress Controller (most common)
- Traefik
- HAProxy
- Kong

### Install NGINX Ingress (Minikube)

```bash
minikube addons enable ingress
```

### Ingress Example

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-ingress
spec:
  rules:
    - host: demo.local
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
```

**Access:**

```
http://demo.local/api
```

## 3️⃣ Rolling Updates & Rollbacks

### Rolling Updates

- Zero-downtime deployment
- Old pods terminated gradually
- New pods created step-by-step

### Trigger Rolling Update

```bash
kubectl set image deployment/api api=myimage:v2
```

### Check rollout status

```bash
kubectl rollout status deployment/api
```

### Rollbacks

Return to previous version.

### Rollback Deployment

```bash
kubectl rollout undo deployment/api
```

### Rollback to a specific revision

```bash
kubectl rollout undo deployment/api --to-revision=2
```

## 4️⃣ Health Checks (Probes)

### Liveness Probe

Checks if the container is alive.
If it fails → Kubernetes restarts container.

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
```

### Readiness Probe

Checks if container is ready to receive traffic.
If it fails → Pod removed from Service's endpoints.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 3
```

## 5️⃣ Resource Limits (CPU/Memory)

### Why resource limits?

- Prevent one container from consuming entire node
- Ensure fair usage
- Support autoscaling
- Create reliable multi-tenant clusters

### Define Resource Requests & Limits

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

**Requests** → Minimum guaranteed  
**Limits** → Maximum allowed

## 🧪 Hands-On Labs

### ✔ Inject Env Variables Using ConfigMap

- Create ConfigMap
- Inject via env
- Mount as files

### ✔ Secure Values with Secrets

- Store DB credentials
- Mount secret into Pod
- Use environment variables

### ✔ Use Ingress to Access API

- Enable Minikube Ingress
- Deploy Ingress YAML
- Access via domain/path

### ✔ Perform Rolling Update

- Deploy v1
- Update image to v2
- Observe rolling update
- Roll back

## 🧱 Mini Project — Production-like App

### 🔐 Deploy an API Using ConfigMap, Secrets & Ingress Routing

You will create:

- API Deployment
- Service
- ConfigMap for env variables
- Secret for DB credentials
- Ingress route `/api`
- Rolling update to new version

### Flow

```
ConfigMap → Deployment → Service → Ingress → Browser
Secrets → Deployment (DB creds)
```