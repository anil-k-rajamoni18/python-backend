# 🚀 10-Day DevOps Mastery Plan (Docker → K8s → CI/CD → AWS)

## ✅ DAY 1 — Docker Fundamentals

### Topics
- Why containers? VM vs Containers
- Docker architecture: images, containers, layers
- Dockerfile basics
- Important commands

### Core Commands
```bash
docker build
docker run
docker ps
docker exec
docker logs
docker stop
docker rm
docker rmi
```

### Hands-On
- Install Docker
- Build your first image (simple Python/Node app)
- Run container in detached mode
- View logs, exec into container

### Mini Project
🔥 **Containerize a simple "Hello API" microservice**

---

## ✅ DAY 2 — Intermediate Docker + Docker Compose

### Topics
- Dockerfile optimization (multi-stage builds intro)
- Docker volumes
- Networks
- Environment variables
- Docker Compose

### Hands-On
- Add volume-based persistence (e.g., database)
- Run multi-container apps (API + DB) using docker-compose
- Map ports, environment vars

### Mini Project
🧱 **Build a 2-container application (FastAPI + PostgreSQL) using Docker Compose**

---

## ✅ DAY 3 — Kubernetes Basics (Local with Minikube or Kind)

### Topics
- K8s architecture (master & worker nodes)
- Pods, Deployments, ReplicaSets, Services
- Kubeconfig
- kubectl basics

### Important Commands
```bash
kubectl apply -f
kubectl get pods
kubectl describe pod
kubectl logs
kubectl exec -it
```

### Hands-On
- Install minikube
- Deploy a simple app as a Deployment
- Expose service (NodePort)

### Mini Project
☸️ **Deploy your Dockerized API to Kubernetes**

---

## ✅ DAY 4 — Kubernetes Intermediate

### Topics
- ConfigMaps & Secrets
- Ingress & Ingress Controllers (Nginx)
- Rolling updates & rollbacks
- Health checks (liveness/readiness)
- Resource limits (CPU/memory)

### Hands-On
- Inject env variables using ConfigMap
- Secure values with Secrets
- Use Ingress to access service via path/URL
- Perform rolling update

### Mini Project
🔐 **Deploy API with ConfigMap/Secrets + Ingress routing**

---

## ✅ DAY 5 — Kubernetes Advanced (Medium Level)

### Topics
- StatefulSets
- Persistent Volume / Persistent Volume Claims
- Horizontal Pod Autoscaler (HPA)
- Metrics Server
- ServiceAccounts & RBAC basics

### Hands-On
- Create PVC + PV
- Create Stateful database (e.g., PostgreSQL)
- Install metrics-server
- Configure HPA to auto-scale the app

### Mini Project
⚙️ **Fully scalable microservice with autoscaling + persistent DB**

---

## ✅ DAY 6 — CI/CD Basics with GitHub Actions

### Topics
- GitHub Actions basics
- Workflow syntax (YAML)
- Runners (GitHub-hosted vs self-hosted)
- Triggers (push, PR, schedule)
- Jobs, steps, actions marketplace

### Hands-On
- Create your first workflow `.github/workflows/main.yml`
- Run basic build/test pipeline

### Mini Project
🔄 **CI Pipeline: Run tests automatically on every commit**

---

## ✅ DAY 7 — CI/CD Advanced (Docker + Kubernetes Integration)

### Topics
- Build & push Docker images using Actions
- Using secrets in GitHub Actions
- Create CI/CD workflows:
  - Build image
  - Run tests
  - Publish to Docker Hub / GitHub Container Registry

### Hands-On
- Build & push Docker image from GitHub Actions
- Tag images using GitHub SHA & semantic versioning

### Mini Project
🚀 **CI pipeline to build, test, and publish Docker images automatically**

---

## ✅ DAY 8 — AWS for DevOps (Core Services)

### Topics
- EC2 basics
- IAM fundamentals (roles, policies, users)
- VPC basics
- ECR (Elastic Container Registry)
- S3 basics
- RDS basics

### Hands-On
- Create ECR repo
- Push Docker image from local & GitHub Actions
- Configure IAM roles for EC2 or ECS

### Mini Project
🗃️ **Create and push API Docker image to ECR**

---

## ✅ DAY 9 — AWS Deployment (Medium Level)

### Topics (choose your track)

#### Track A — ECS (Easier)
- Fargate vs EC2 launch types
- Task Definitions
- Services
- Load Balancers

#### Track B — EKS (More advanced)
- Create EKS cluster (UI or eksctl)
- Configure kubectl with AWS
- Deploy workloads

### Hands-On (Pick one track)
- Deploy your microservice to ECS/EKS
- Configure Load Balancer
- Use environment variables, logging

### Mini Project
🌍 **Deploy your Dockerized API to AWS ECS/EKS**

---

## ✅ DAY 10 — Full Real-World CI/CD + Cloud Deployment Project

### Topics
- Full pipeline automation:
  - Build image
  - Push to ECR
  - Automatic deployment to ECS/EKS
- GitHub Actions + AWS OIDC authentication
- Alerts & Monitoring:
  - CloudWatch Logs
  - CloudWatch Metrics & Alarms

### Hands-On
- Create a GitHub Actions workflow:
  - On merge to main → build → push → deploy
- Configure OIDC roles for GitHub Actions to access AWS securely

### Final Project
🔥 **Complete Production-Level CI/CD Pipeline**

#### Pipeline Workflow
1. Developer pushes code → GitHub
2. GitHub Actions:
   - Run test suite
   - Build Docker image
   - Push image to ECR
   - Deploy to ECS/EKS
3. CloudWatch monitors app health
4. Autoscaling triggers if required

### Output
You will have a fully automated DevOps pipeline.

---

## 🎯 After 10 Days You Will Be Able To:

✔️ Containerize any application using Docker  
✔️ Build and orchestrate microservices in Kubernetes  
✔️ Write advanced Dockerfiles & deploy multi-container setups  
✔️ Configure Ingress, Secrets, Autoscaling, Persistent Storage  
✔️ Build real CI/CD pipelines using GitHub Actions  
✔️ Deploy real applications on AWS ECS/EKS  
✔️ Use AWS services like IAM, EC2, ECR, S3, VPC  
✔️ Build production-grade infra pipelines