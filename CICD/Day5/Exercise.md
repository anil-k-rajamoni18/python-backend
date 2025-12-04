# 🔥 DAY 5 — Kubernetes Advanced — Real-Time Hands-On Questions

## 1️⃣ StatefulSets (Real-time Hands-On)

### Q1. Create a StatefulSet with 3 replicas running Nginx.

**Requirements:**

- Name: `web-ss`
- Image: `nginx:1.25`
- Pod naming must follow: `web-ss-0`, `web-ss-1`, `web-ss-2`

**Hints:** Use:

```yaml
kind: StatefulSet
serviceName: web
```

### Q2. Verify stability by deleting a pod. Does it recreate with the SAME name?

**Commands:**

```bash
kubectl delete pod web-ss-1
kubectl get pods
```

**Expected:** Pod recreated with same name (unique to StatefulSets).

### Q3. Scale the StatefulSet to 5 replicas.

**Task:**

```bash
kubectl scale statefulset web-ss --replicas=5
```

### Q4. Inspect the stable network identity assigned to each pod.

**Commands:**

```bash
kubectl exec -it web-ss-0 -- hostname
kubectl exec -it web-ss-2 -- hostname
```

## 2️⃣ Persistent Volumes + Persistent Volume Claims

### Q5. Create a PersistentVolume of 5Gi using hostPath.

**Requirements:**

- Name: `pv-data`
- Storage: 5Gi
- hostPath: `/mnt/k8s-data`

### Q6. Create a PVC that binds to the PV created above.

**PVC Requirements:**

- Name: `pvc-data`
- Storage: 3Gi
- Access: `ReadWriteOnce`

**Test binding:**

```bash
kubectl get pv,pvc
```

### Q7. Attach the PVC to a pod and write data in it.

**Steps:**

- Create a simple busybox pod
- Mount the volume at `/data`
- Inside pod:

```bash
echo "hello k8s" > /data/test.txt
```

Delete pod and recreate → data should persist.

### Q8. Confirm volume persistence by redeploying pod.

**Commands:**

```bash
kubectl delete pod busybox
kubectl apply -f busybox.yaml
kubectl exec -it busybox -- cat /data/test.txt
```

## 3️⃣ Stateful Database Deployment (PostgreSQL)

### Q9. Deploy PostgreSQL using StatefulSet + PVC.

**Requirements:**

- Image: `postgres:15`
- PVC per pod for `/var/lib/postgresql/data`
- Use `POSTGRES_PASSWORD=mysecret` env variable

### Q10. Verify that DB pods have unique volumes.

**Commands:**

```bash
kubectl get pvc
kubectl describe pvc <any>
```

You should see PVC names like:

```
data-postgres-0
data-postgres-1
```

## 4️⃣ Metrics Server + Horizontal Pod Autoscaler

### Q11. Install metrics-server into cluster.

**Command:**

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Q12. Verify metrics availability.

```bash
kubectl top nodes
kubectl top pods
```

### Q13. Deploy a sample app and configure HPA.

**App Requirements:**

- Deployment name: `autoscale-app`
- Image: `k8s.gcr.io/hpa-example`
- Expose port: 80

**HPA Requirements:**

- Min replicas: 2
- Max replicas: 10
- Target CPU: 50%

**Create HPA:**

```bash
kubectl autoscale deployment autoscale-app --cpu-percent=50 --min=2 --max=10
```

### Q14. Generate artificial load to trigger autoscaling.

**Commands:**

```bash
kubectl run load-generator --image=busybox -- /bin/sh -c "while true; do wget -q -O- http://autoscale-app; done"
```

**Watch scaling:**

```bash
kubectl get hpa -w
```

### Q15. Verify scaled pod count.

```bash
kubectl get deploy autoscale-app
```

**Expected:** Pods increase based on CPU load.

## 5️⃣ RBAC + ServiceAccounts (Practical Security Exercises)

### Q16. Create a ServiceAccount named `app-user`.

```bash
kubectl create sa app-user
```

### Q17. Create an RBAC role that allows listing pods only.

**Role Requirements:**

- Resource: pods
- Verb: list
- Namespace: default

### Q18. Bind the role to the ServiceAccount.

Use:

```
RoleBinding
```

### Q19. Test RBAC permissions using `kubectl auth can-i`.

```bash
kubectl auth can-i list pods --as=system:serviceaccount:default:app-user
```

**Expected:** `yes`

### Q20. Test forbidden actions (e.g., delete pods).

```bash
kubectl auth can-i delete pods --as=system:serviceaccount:default:app-user
```

**Expected:** `no`

## 🔥 Bonus Real-World Scenarios

### Q21. Your HPA is not scaling! Troubleshoot.

**Check:**

- Metrics server running?
- CPU requests set?
- `kubectl top` working?
- App actually receiving load?

### Q22. PostgreSQL pod stuck in CrashLoopBackoff — fix it.

**Possible causes:**

- Missing password env vars
- PVC permission issues
- Disk full
- Incorrect mount path

### Q23. PV stuck in "Pending" — why?

**Reasons:**

- Storage class mismatch
- Node affinity conflict
- PVC size > PV size

### Q24. StatefulSet pods not attaching volumes.

**Check:**

- VolumeClaimTemplates syntax
- StorageClass availability
- PVC naming pattern

### Q25. Autoscaling goes above limit. Why?

**Investigate:**

- Multiple HPAs applied?
- Misconfigured target metrics?