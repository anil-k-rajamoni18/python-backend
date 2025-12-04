# 🔥 REAL-TIME HANDS-ON QUESTIONS (Kubernetes)

Use these for exams, interviews, or live workshops.

## 1️⃣ Basic Pod & Deployment Practice

### Q1. Create a Pod using an Nginx image.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx
```

**Task:**

```bash
kubectl apply -f nginx-pod.yaml
kubectl get pods
```

### Q2. Describe the Pod & view container details.

```bash
kubectl describe pod nginx-pod
```

### Q3. Delete the Pod.

```bash
kubectl delete pod nginx-pod
```

## 2️⃣ Deployment-Based Real Scenarios

### Q4. Create a Deployment with 3 replicas of httpd image.

### Q5. Scale the Deployment to 5 replicas.

```bash
kubectl scale deploy httpd-deploy --replicas=5
```

### Q6. Update the Deployment image to a newer version.

```bash
kubectl set image deploy/httpd-deploy httpd=httpd:2.4
```

### Q7. Rollback the Deployment.

```bash
kubectl rollout undo deploy/httpd-deploy
```

## 3️⃣ Logs, Exec & Debugging

### Q8. View logs of a Pod.

```bash
kubectl logs <pod>
```

### Q9. Exec inside a Pod.

```bash
kubectl exec -it <pod> -- sh
```

### Q10. List environment variables inside a running Pod.

```bash
env
```

## 4️⃣ Service Hands-On Tasks

### Q11. Expose a Deployment on port 30080 using NodePort.

```bash
kubectl expose deploy nginx-deploy \
  --type=NodePort --port=80 --name=nginx-svc
```

### Q12. Check the NodePort and access the app.

```bash
kubectl get svc nginx-svc
minikube service nginx-svc
```

## 5️⃣ Networking & Cluster Tasks

### Q13. Get all resources in the default namespace.

```bash
kubectl get all
```

### Q14. Get cluster info.

```bash
kubectl cluster-info
```

## 6️⃣ Kubeconfig & Context Switching

### Q15. List kubeconfig contexts.

```bash
kubectl config get-contexts
```

### Q16. Switch to Minikube context.

```bash
kubectl config use-context minikube
```

## 7️⃣ Mini Project Hands-On Questions

### Q17. Deploy a backend API (Node/Python).

### Q18. Deploy a frontend that communicates with the backend.

### Q19. Create Services:

- backend → ClusterIP
- frontend → NodePort

### Q20. Use kubectl port-forward to test API manually.

```bash
kubectl port-forward <pod> 8080:80
```