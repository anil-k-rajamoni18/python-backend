# 📘 Class Session Notes

## 1. What is CI/CD?

CI/CD stands for Continuous Integration and Continuous Delivery/Deployment. It is a set of practices used in DevOps to automate software development, testing, and deployment.

### 🔹 Continuous Integration (CI)

- Developers frequently merge code changes into a shared repository.
- Automated builds and tests are triggered after each commit.
- **Purpose:**
  - Detect bugs early
  - Ensure codebase stability
  - Improve collaboration

### 🔹 Continuous Delivery (CD)

- Builds on CI by automatically preparing code for release.
- Code is deployed to staging environments.
- Requires manual approval to release to production.
- Ensures the product is always in a "release-ready" state.

### 🔹 Continuous Deployment (CD)

- Takes Continuous Delivery a step further.
- Every approved change is automatically deployed to production.
- No manual approval needed.

### 🔹 CI/CD Pipeline Stages

1. **Source Code** – Code commit triggers pipeline.
2. **Build Stage**
   - Code compilation
   - Dependency installation
   - Docker image build (if containerized)
3. **Test Stage**
   - Unit tests
   - Integration tests
   - Security scans
4. **Artifact Storage**
   - Binaries, Docker images, or packages stored in repositories.
5. **Deploy Stage**
   - Deploy to Dev, QA, Staging, or Prod environments
   - Tools like Kubernetes, ECS, or EC2 are used
6. **Monitoring & Feedback**
   - Track performance, errors, logs via tools like Prometheus, CloudWatch, ELK.

## 2. Different Environments

Organizations use multiple environments to ensure quality and stability.

### 🔹 Development (Dev)

- Used by developers for coding and initial testing.
- Frequent updates & unstable.

### 🔹 Testing / QA

- Quality Assurance team tests functionality and bug fixes.
- More stable than Dev.

### 🔹 Staging / Pre-Production

- Replica of Production environment.
- Final testing before deployment.
- Used for UAT (User Acceptance Testing).

### 🔹 Production (Prod)

- Live environment accessed by end users.
- Very stable, monitored 24/7.

**Other common envs:**

- **Sandbox** – For experimentation.
- **Performance / Load Testing** – For stress and scale testing.
- **Disaster Recovery (DR)** – Backup environment for emergencies.

## 3. What is DevOps?

DevOps is a culture, mindset, and set of practices that integrates Development (Dev) and Operations (Ops) teams to automate and streamline the software lifecycle.

### 🔹 DevOps Principles

- Collaboration & shared responsibility
- Automation of repetitive tasks
- Continuous Improvement
- Infrastructure as Code (IaC)
- Monitoring & logging
- Rapid feedback loops

### 🔹 Benefits of DevOps

- Faster delivery of features
- Reduced errors/bugs
- Scalable systems
- Faster recovery from failures
- Higher deployment frequency

## 4. Tools Used in DevOps, CI/CD, Cloud & Containers

### 🔹 CI/CD Tools

- Jenkins
- GitHub Actions
- GitLab CI
- CircleCI
- Azure DevOps Pipelines
- AWS CodePipeline

### 🔹 Version Control Tools

- Git
- GitHub / GitLab / Bitbucket

### 🔹 Build Tools

- Maven
- Gradle
- npm/yarn

### 🔹 Containerization Tools

- Docker
- Podman
- Docker Compose

### 🔹 Container Orchestration

- Kubernetes (K8s)
- Amazon EKS
- AWS ECS / Fargate

### 🔹 Configuration Management

- Ansible
- Chef
- Puppet
- SaltStack

### 🔹 Infrastructure as Code (IaC)

- Terraform
- AWS CloudFormation

### 🔹 Cloud Platforms

- AWS
- Azure
- Google Cloud Platform (GCP)

### 🔹 Monitoring & Logging

- Prometheus + Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- AWS CloudWatch
- Splunk

### 🔹 Artifact Repositories

- Nexus
- JFrog Artifactory
- AWS ECR (Elastic Container Registry)

---

# 📘 CI/CD Pipeline Flow Diagrams

## 1️⃣ Simple CI/CD Pipeline Diagram

```
   ┌───────────┐        ┌────────────┐        ┌─────────────┐
   │   Dev      │ Push   │   Source    │ Trigger│    Build      │
   │  Writes    ├───────▶│ Repository │────────▶│   Stage      │
   │   Code     │        │  (Git)     │        │ (Compile/App)│
   └───────────┘        └────────────┘        └─────────────┘
                                                             │
                                                             ▼
                                                    ┌────────────────┐
                                                    │   Test Stage   │
                                                    │ (Unit/Integration)          
                                                    └────────────────┘
                                                             │
                                                             ▼
                                              ┌───────────────────────────┐
                                              │  Artifact / Image Store   │
                                              │ (ECR / Artifactory / S3)  │
                                              └───────────────────────────┘
                                                             │
                                                             ▼
                                     ┌───────────────────────────────────────────┐
                                     │          Deploy to Environments          │
                                     │ Dev → QA → Staging → Production          │
                                     └───────────────────────────────────────────┘
                                                             │
                                                             ▼
                                             ┌────────────────────────────────┐
                                             │   Monitoring & Observability  │
                                             │ (Grafana, CloudWatch, ELK)    │
                                             └────────────────────────────────┘
```

## 2️⃣ CI/CD Stages with Environments Flow

```
                ┌────────────────────────────┐
                │         CI Pipeline        │
                └────────────────────────────┘
                         │
                         ▼
           ┌────────────────────────────┐
           │     Continuous Integration │
           └────────────────────────────┘
                         │
     ┌───────────────────┼───────────────────┐
     ▼                   ▼                   ▼
┌─────────┐        ┌───────────┐       ┌────────────┐
│  Build  │        │   Test    │       │  Package   │
└─────────┘        └───────────┘       └────────────┘
     │                   │                   │
     └─────────────┬─────┴──────────────┬────┘
                   ▼                    ▼
         ┌────────────────┐    ┌──────────────────┐
         │  Artifact Repo │    │ Container Registry│
         │ (Nexus/S3/ECR) │    │     (ECR/GCR)     │
         └────────────────┘    └──────────────────┘



Then CD begins:

                ┌──────────────────────────────┐
                │       CD Pipeline            │
                └──────────────────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │ Deploy to Dev Env  │
              └────────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │ Deploy to QA Env   │
              └────────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │ Deploy to Staging  │
              └────────────────────┘
                         │
                         ▼
             ┌──────────────────────┐
             │ Deploy to Production │
             └──────────────────────┘
```

## 3️⃣ CI/CD With Docker + Kubernetes Diagram

```
                   ┌─────────────────────┐
                   │ Developer Commits   │
                   │    Code to Git      │
                   └─────────────────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │ CI System (GitHub, Jenkins etc)│
              └────────────────────────────────┘
                               │
   ┌───────────────────────────┼──────────────────────────┐
   ▼                           ▼                          ▼
┌───────────┐          ┌───────────────┐           ┌─────────────────┐
│ Build App │          │ Run Unit Test │           │ Build Docker Img│
└───────────┘          └───────────────┘           └─────────────────┘
                                                         │
                                                         ▼
                                         ┌────────────────────────────────┐
                                         │ Push Image → Docker Registry  │
                                         │     (ECR / DockerHub)         │
                                         └────────────────────────────────┘
                                                         │
                                                         ▼
                                 ┌──────────────────────────────────────────┐
                                 │ CD Deploy using Kubernetes (K8s)        │
                                 │ kubectl apply / Helm / ArgoCD / FluxCD  │
                                 └──────────────────────────────────────────┘
                                                         │
                                                         ▼
                                       ┌─────────────────────────────────┐
                                       │ App Running in Pods on Cluster │
                                       │ (AWS EKS / GKE / On-prem K8s)  │
                                       └─────────────────────────────────┘
```

## 4️⃣ End-to-End DevOps Workflow Diagram

```
   ┌──────────┐      ┌───────────┐      ┌─────────────┐      ┌────────────┐
   │ Planning │─────▶│ Coding    │─────▶│ Build & Test│─────▶│ Deployment │
   └──────────┘      └───────────┘      └─────────────┘      └────────────┘
                                                         │
                                                         ▼
                                              ┌──────────────────┐
                                              │   Monitoring     │
                                              └──────────────────┘
                                                         │
                                                         ▼
                                         ┌────────────────────────────┐
                                         │ Feedback & Continuous Loop │
                                         └────────────────────────────┘
```