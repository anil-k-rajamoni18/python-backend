# 🔥 Real-Time Hands-On Questions — DAY 4 (Kubernetes Intermediate)

Covering ConfigMaps, Secrets, Ingress, Rolling Updates, Health Checks, Resource Limits

These are perfect for classroom exercises, interviews, and skill validation.

## 1️⃣ ConfigMaps – Real-Time Hands-On Questions

### Q1. Create a ConfigMap from a literal value and view it.

**✔ Task**

```bash
kubectl create configmap app-config --from-literal=ENV=production
kubectl get configmaps
kubectl describe configmap app-config
```

### Q2. Create a ConfigMap from a file and mount it inside a pod.

**✔ Task**

```bash
echo "WELCOME_MSG=Hello from Kubernetes" > config.env
kubectl create configmap file-config --from-env-file=config.env
```

Then write a pod YAML using this ConfigMap as env variables.

### Q3. Mount a ConfigMap as a volume into a pod.

**✔ Task**

- Create a ConfigMap
- Mount it at `/config/settings`
- Exec into pod and validate

### Q4. Update a ConfigMap and observe the behavior in a running pod.

**✔ Task**

Modify ConfigMap → apply  
Check if pod reloads automatically or requires restart.

## 2️⃣ Secrets – Real-Time Hands-On Questions

### Q5. Create a Kubernetes Secret and view encoded values.

**✔ Task**

```bash
kubectl create secret generic db-secret --from-literal=password=Pass1234
kubectl get secrets
kubectl describe secret db-secret
```

### Q6. Decode a secret locally.

**✔ Task**

```bash
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

### Q7. Inject Secret values into a Deployment as environment variables.

**✔ Task**

Write a Deployment that uses:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password
```

### Q8. Mount a Secret as a file inside a pod.

**✔ Task**

Mount Secret at `/etc/secure`.

## 3️⃣ Ingress & Ingress Controller – Hands-On Questions

### Q9. Install Nginx Ingress Controller in Minikube.

**✔ Task**

```bash
minikube addons enable ingress
```

### Q10. Expose a Deployment using a ClusterIP service.

**✔ Task**

Write:

```yaml
kind: Service
type: ClusterIP
```

### Q11. Write an Ingress rule that routes /api → service api-service.

**✔ Example**

Create `ingress.yaml` and apply:

```bash
kubectl apply -f ingress.yaml
```

### Q12. Test the Ingress endpoint.

**✔ Task**

```bash
minikube ip
curl http://<minikube-ip>/api
```

## 4️⃣ Rolling Updates & Rollbacks – Hands-On Questions

### Q13. Deploy an app with 3 replicas and perform a rolling update.

**✔ Task**

```bash
kubectl set image deployment/myapp myapp=nginx:1.23
kubectl rollout status deployment/myapp
```

### Q14. Check rollout history.

**✔ Task**

```bash
kubectl rollout history deployment/myapp
```

### Q15. Rollback to previous version.

**✔ Task**

```bash
kubectl rollout undo deployment/myapp
```

### Q16. Trigger a failed rollout and observe behavior.

**✔ Task**

Update to a broken image:

```bash
kubectl set image deployment/myapp myapp=nginx:doesnotexist
```

Check status:

```bash
kubectl rollout status deployment/myapp
```

## 5️⃣ Health Checks (Liveness & Readiness) – Hands-On Questions

### Q17. Add liveness probe to a pod and observe restarts.

**✔ Example liveness probe:**

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

Watch restarts:

```bash
kubectl get pods -w
```

### Q18. Add readiness probe and check endpoints.

**✔ Task**

Ensure pod is not added to service until it's ready.

### Q19. Break the liveness probe and see pod restart behavior.

### Q20. Break the readiness probe and see service routing behavior.

## 6️⃣ Resource Limits – Hands-On Questions

### Q21. Add CPU/memory requests & limits to deployment.

**✔ Example**

Set:

```yaml
requests:
  cpu: "100m"
  memory: "128Mi"
limits:
  cpu: "500m"
  memory: "256Mi"
```

### Q22. Stress a pod and hit CPU limits.

**✔ Task**

Exec into pod, run CPU stress tool.

### Q23. Observe throttling in metrics (using Metrics Server).

**✔ Task**

```bash
kubectl top pod
```

### Q24. Deploy two apps with same limits and observe scheduling behavior.

## 7️⃣ Combined Workflow – Real-Time Scenario Questions

### Q25. Deploy an API that:

- uses ConfigMap for environment variables
- uses Secret for database password
- uses readiness/liveness probes
- uses resource limits
- is exposed via a ClusterIP service
- is exposed publicly through Ingress

**✔ You must deploy using separate YAML files (best practice).**

### Q26. Break one component (ConfigMap/Secret/image tag) and debug.

### Q27. Retrieve pod logs + describe events to find root cause.

```bash
kubectl logs <pod>
kubectl describe pod <pod>
```

### Q28. Verify Ingress routing end-to-end.

**✔ Task**

Use:

```bash
curl http://<minikube-ip>/api
```

### Q29. Perform a zero-downtime rolling update.

**✔ Task**

Update image tag → watch pods → test API.

### Q30. Validate that Secrets are not printed in logs or env dumps.

**✔ Task**

```bash
kubectl exec -it <pod> -- env
```

Check that sensitive values remain hidden.