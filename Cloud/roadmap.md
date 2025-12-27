# ☁️ AWS Cloud Learning Roadmap – 12 Days (Beginner → Advanced)

---

## 🟢 DAY 1 – Cloud Fundamentals + AWS Basics

### Concepts
- What is Cloud Computing?
- IaaS vs PaaS vs SaaS
- Public vs Private vs Hybrid Cloud
- Why AWS dominates the market

### AWS Global Infrastructure
- Regions
- Availability Zones
- Edge Locations

### AWS Core Services Overview
- EC2
- S3
- RDS
- IAM
- VPC
- ELB
- Auto Scaling

### Hands-on
- Create AWS Free Tier account
- Explore AWS Console
- Understand billing dashboard
- Enable MFA (very important)

### Output
✅ Understand how AWS is structured

---

## 🟢 DAY 2 – IAM (Identity & Access Management) 🔐

### Concepts
- Root account vs IAM User
- IAM Users, Groups, Roles
- Policies (JSON)
- Principle of Least Privilege

### Hands-on
- Create IAM user (Admin + ReadOnly)
- Attach policies
- Create role for EC2
- Test permissions

### Interview Focus
- Difference between IAM User vs Role
- Why roles are used instead of access keys

### Output
✅ Secure AWS account access

---

## 🟢 DAY 3 – EC2 (Compute) Deep Dive

### Concepts
- What is EC2?
- Instance types (t2, t3, m5, c5)
- AMI
- Security Groups vs NACL
- Key pairs
- Elastic IP

### Hands-on
- Launch EC2 (Amazon Linux)
- SSH into EC2
- Install Nginx / Apache
- Host a simple website
- Attach Elastic IP

### Practical Task
```bash
sudo yum install nginx -y
sudo systemctl start nginx
```

### Output
✅ You can run servers on AWS

---

## 🟢 DAY 4 – Storage (S3 + EBS + EFS)

### Concepts
- Object vs Block vs File storage
- S3 buckets
- Versioning
- Lifecycle rules
- S3 vs EBS vs EFS

### Hands-on
- Create S3 bucket
- Upload files
- Enable versioning
- Host static website on S3
- Attach EBS volume to EC2

### Interview Focus
- When to use S3 vs EBS
- S3 durability (11 9's)

### Output
✅ You understand AWS storage options

---

## 🟡 DAY 5 – Networking (VPC) 🌐

### Concepts
- What is VPC?
- CIDR blocks
- Public vs Private Subnet
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Group vs NACL

### Hands-on
- Create custom VPC
- Create public & private subnet
- Launch EC2 in public subnet
- Test internet connectivity

### Diagram Understanding
```
VPC
 ├── Public Subnet (EC2 + IGW)
 └── Private Subnet (RDS)
```

### Output
✅ Strong AWS networking fundamentals

---

## 🟡 DAY 6 – Load Balancer & Auto Scaling

### Concepts
- High Availability
- Elastic Load Balancer
  - ALB
  - NLB
- Auto Scaling Groups
- Health Checks

### Hands-on
- Create Application Load Balancer
- Attach multiple EC2 instances
- Enable Auto Scaling
- Test failover

### Interview Focus
- Difference between ALB vs NLB
- How AWS achieves HA

### Output
✅ You can build scalable architectures

---

## 🟡 DAY 7 – Databases (RDS + DynamoDB)

### Concepts
- SQL vs NoSQL
- RDS engines (MySQL, PostgreSQL)
- Multi-AZ
- Read Replicas
- DynamoDB basics

### Hands-on
- Launch RDS MySQL
- Connect from EC2
- Create DB & table
- Insert sample data

### Output
✅ You can manage databases on AWS

---

## 🟠 DAY 8 – Monitoring, Logging & Security

### Concepts
- CloudWatch (metrics, alarms)
- CloudTrail (audit logs)
- AWS Config
- Shared Responsibility Model

### Hands-on
- Create CloudWatch alarm
- Monitor EC2 CPU
- View CloudTrail logs

### Interview Focus
- How AWS handles security
- What AWS manages vs what you manage

### Output
✅ You can monitor & audit AWS resources

---

## 🔵 DAY 9 – DevOps & Automation (Advanced)

### Concepts
- Infrastructure as Code (IaC)
- Terraform basics
- CI/CD concepts
- AWS CodePipeline overview

### Hands-on
- Install Terraform
- Write Terraform for EC2
- Apply & destroy infrastructure

### Example
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abcdef"
  instance_type = "t2.micro"
}
```

### Output
✅ You can automate AWS infrastructure

---

# 🔵 DAY 10 – Containers on AWS (ECR + ECS + EKS) 🐳☸️

## 🎯 Objective
By end of Day 11, you will:
- Build Docker images
- Push images to Amazon ECR
- Deploy containers using ECS (Fargate) and EKS
- Confidently explain ECR vs DockerHub, ECS vs EKS

---

## 🔹 PART 1: Container Fundamentals (Quick)
- Docker Image vs Container
- Dockerfile basics
- Why container registry is needed

---

## 🔹 PART 2: Amazon ECR (Elastic Container Registry) 📦

### What is ECR?
- Fully managed Docker image registry
- Private & secure (IAM-based)
- Integrated with ECS & EKS

### ECR vs Docker Hub

| Feature | ECR | Docker Hub |
|---------|-----|------------|
| Auth | IAM | Username/password |
| Security | Private VPC | Public by default |
| AWS integration | Native | External |
| Enterprise use | ✅ | ⚠️ |

### Hands-on: ECR Workflow (IMPORTANT)

**Step 1: Create ECR Repository**
```bash
aws ecr create-repository --repository-name my-nginx
```

**Step 2: Build Docker Image**
```bash
docker build -t my-nginx .
```

**Step 3: Authenticate Docker to ECR**
```bash
aws ecr get-login-password \
| docker login \
--username AWS \
--password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

**Step 4: Tag & Push Image**
```bash
docker tag my-nginx:latest <account-id>.dkr.ecr.<region>.amazonaws.com/my-nginx:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/my-nginx:latest
```

### Output
✅ Your Docker image is now stored in AWS securely

---

## 🔹 PART 3: Amazon ECS (Using ECR Image)

### ECS Flow (Very Important)
```
Docker Image → ECR → ECS Task Definition → ECS Service → ALB
```

### Hands-on
- Create ECS cluster (Fargate)
- Create Task Definition
  - Image: ECR image
  - CPU / Memory
  - IAM role
- Create ECS Service
- Attach Application Load Balancer
- Access app via ALB DNS

### Interview Focus
- Why ECS pulls images from ECR securely
- Role of task execution role

---

## 🔹 PART 4: Amazon EKS (Using ECR Image)

### EKS Flow
```
Docker Image → ECR → Kubernetes Deployment → Service → Ingress
```

### Hands-on (Light)
```bash
kubectl create deployment nginx \
--image=<account-id>.dkr.ecr.<region>.amazonaws.com/my-nginx:latest
```

### Important Note
- EKS nodes need ECR permissions
- Use IAM Roles for Service Accounts (IRSA)

---

## 🔹 PART 5: ECS vs EKS vs ECR (Interview Table)

| Feature | ECR | ECS | EKS |
|---------|-----|-----|-----|
| Purpose | Image Registry | Container Orchestration | Kubernetes |
| Managed | Fully | Fully | Control plane |
| Complexity | Low | Low | High |
| Skill demand | Docker | AWS-native | Kubernetes |

---

## 🔹 PART 6: Real-World Architecture (Very Common)

```
Developer
   ↓
Docker Build
   ↓
Amazon ECR
   ↓
ECS / EKS
   ↓
ALB
```

**Used by:**
- Microservices
- AI inference services
- Background workers
- APIs

---

## DAY 10 Final Output
✅ You understand ECR + ECS + EKS end-to-end  
✅ You can deploy containers professionally on AWS  
✅ You can answer container interview questions confidently

---

# 🔴 DAY 11 – Generative AI on AWS (Amazon Bedrock) 🤖🧠

## 🎯 Objective
Learn AWS-native Generative AI, LLM usage, and enterprise AI architecture.

---

## 🔹 PART 1: What is Amazon Bedrock?

### Concepts
- Fully managed Foundation Model service
- No infrastructure management
- Secure, private, enterprise-ready
- Supports multiple models

### Available Model Providers
- Amazon Titan
- Anthropic Claude
- Meta Llama
- Mistral (where available)

---

## 🔹 PART 2: Bedrock Architecture

```
Client App
   |
API Gateway
   |
Lambda
   |
Amazon Bedrock
   |
Foundation Model
```

### Key Features
- Prompt management
- Model selection
- Fine-tuning (limited)
- Guardrails (safety, compliance)

---

## 🔹 PART 3: Hands-on (Conceptual + Code)

### Use Case: Text Generation API

**Flow**
- User sends prompt
- Lambda calls Bedrock
- Model returns response

### Sample Python (Conceptual)

```python
import boto3

client = boto3.client("bedrock-runtime")

response = client.invoke_model(
    modelId="anthropic.claude-v2",
    body='{"prompt":"Explain AWS ECS in simple terms"}'
)

print(response)
```

---

## 🔹 PART 4: Bedrock vs OpenAI (Interview Gold)

| Feature | Bedrock | OpenAI |
|---------|---------|--------|
| Hosting | AWS | External |
| Security | Private VPC | Public |
| Compliance | Enterprise | Limited |
| Model choice | Multiple | Few |
| Infra mgmt | AWS | OpenAI |

---

## 🔹 PART 5: Real-world Bedrock Use Cases
- Enterprise chatbots
- Internal knowledge assistants
- Legal / medical summarization
- Code generation tools
- RAG pipelines (Bedrock + S3 + OpenSearch)

---

## 🔹 PART 6: Bedrock + Your Existing Skills (BIG VALUE)

Since you already work with:
- Embeddings
- Search
- FastAPI

👉 **You can build:**

```
S3 → Chunking → Embeddings → Vector DB
          ↓
     Amazon Bedrock (LLM)
```

This is top-tier cloud + AI architecture 🔥

---

## DAY 11 Output
✅ You understand Generative AI on AWS  
✅ You can design Bedrock-based AI systems  
✅ You stand out as Cloud + AI Engineer

## 🔴 DAY 12 – Advanced Cloud Architecture + Career Prep

### Advanced Topics
- Well-Architected Framework
- Cost Optimization
- Fault Tolerance
- Disaster Recovery
- Serverless (Lambda + API Gateway)
- Containers (ECS + EKS overview)

### Mini Capstone Project
🚀 **Deploy a 3-Tier Application**
- ALB
- EC2 (App Layer)
- RDS (DB Layer)
- S3 (Static assets)

### Career Prep
- Resume AWS project points
- Common AWS interview questions
- Certification roadmap


---

## 🎓 Certifications (Optional but Recommended)

| Level | Certification |
|-------|--------------|
| Beginner | AWS Cloud Practitioner |
| Intermediate | AWS Solutions Architect – Associate |
| Advanced | AWS DevOps Engineer / SA Professional |

---

## 🧠 How YOU Should Learn Daily

- **30%** Reading
- **60%** Hands-on
- **10%** Interview questions