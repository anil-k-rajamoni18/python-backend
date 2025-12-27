# 🟢 DAY 3 – EC2 HANDS-ON REALTIME PROJECTS 🖥️☁️

## Mental shift:
EC2 projects are not about "launching instances".  
**They are about compute decisions, security, availability, and cost.**

---

## 🚀 PROJECT 1: Production-Ready Linux Web Server on EC2

### 🎯 Problem Statement
"Deploy and secure a Linux web server to host a public application."

### 🧠 WHY THIS PROJECT MATTERS
- Baseline compute skill
- Appears in every interview
- Tests networking, security, OS control

### 🏗️ Architecture
```
Internet
   ↓
Security Group (22, 80)
   ↓
EC2 (Amazon Linux)
   ↓
Nginx Web Server
```

### 🛠️ Implementation Steps (WHAT + WHY)

**Step 1: Choose AMI**
- Amazon Linux 2

👉 AWS-optimized, long-term support

**Step 2: Choose Instance Type**
- t3.micro

👉 Burstable CPU, cost-effective

**Step 3: Configure Networking**
- Public subnet
- Auto-assign public IP

👉 Required for internet access

**Step 4: Security Group**

Allow:
- SSH (22) → your IP only
- HTTP (80) → public

👉 **WHY:** Least privilege, reduced attack surface

**Step 5: Key Pair**
- Create once
- Download securely

👉 **WHY:** Password-less authentication

**Step 6: SSH into Instance**
```bash
ssh -i key.pem ec2-user@<public-ip>
```

**Step 7: Install & Start Nginx**
```bash
sudo yum install nginx -y
sudo systemctl start nginx
```

### ⚠️ Common Mistakes
- SSH open to 0.0.0.0/0
- Using large instance unnecessarily
- Forgetting to stop instance

### 🎤 Interview Questions
- Why EC2 over Lambda?
- Why t3 instead of m5?
- How do you secure SSH?

### 💬 Interview-Ready Statement
"I deployed and secured an EC2-based Linux web server using least-privilege security groups and hosted a production-ready Nginx service."

---

## 🚀 PROJECT 2: Static Website with Elastic IP (Stability Scenario)

### 🎯 Problem Statement
"Ensure a public application remains reachable even after EC2 restarts."

### 🧠 WHY THIS PROJECT MATTERS
- Shows understanding of IP volatility
- Introduces infrastructure stability

### 🏗️ Architecture
```
Elastic IP
   ↓
EC2 Instance
   ↓
Nginx Website
```

### 🛠️ Implementation Steps

**Step 1: Allocate Elastic IP**
- From EC2 console

**Step 2: Associate with Instance**
- Attach to running EC2

👉 **WHY:** Public IP no longer changes

### ⚠️ Trade-Offs
- Elastic IP costs money if idle
- Load Balancer preferred in production

### 🎤 Interview Questions
- Why not rely on public IP?
- Elastic IP vs Load Balancer?
- When should Elastic IP be avoided?

### 💬 Interview Statement
"I used Elastic IP to ensure stable public access, while recognizing ALBs are preferred for scalable production workloads."

---

## 🚀 PROJECT 3: Security Groups vs NACL – Traffic Control Lab

### 🎯 Problem Statement
"Control network access at both instance and subnet levels."

### 🧠 WHY THIS PROJECT MATTERS
- Classic interview topic
- Tests networking depth

### 🏗️ Architecture
```
VPC
 └── Subnet
     ├── NACL
     └── EC2 (Security Group)
```

### 🛠️ Implementation Steps

**Step 1: Modify Security Group**
- Remove HTTP rule
- Verify site unreachable

**Step 2: Restore HTTP**
- Site accessible again

**Step 3: Modify NACL**
- Add DENY rule for port 80
- Verify traffic blocked

👉 **WHY:** NACL deny overrides SG allow

### 🎤 Interview Questions (VERY COMMON)
- SG vs NACL?
- Stateful vs stateless?
- Why use NACL at all?

### 💬 Interview Statement
"I tested traffic control using both security groups and NACLs to understand layered network security and precedence rules."

---

## 🚀 PROJECT 4: AMI Creation for Fast Scaling & Recovery

### 🎯 Problem Statement
"Create a reusable server image for quick recovery and scaling."

### 🧠 WHY THIS PROJECT MATTERS
- Shows production maturity
- Reduces configuration drift

### 🛠️ Implementation Steps

**Step 1: Configure EC2**
- Install software
- Apply configs

**Step 2: Create Custom AMI**
- From running instance

👉 **WHY:** Immutable infrastructure pattern

### 🎤 Interview Questions
- Why use custom AMIs?
- AMI vs user-data?
- How AMIs help disaster recovery?

### 💬 Interview Statement
"I created custom AMIs to standardize deployments and reduce configuration drift across EC2 instances."

---

## 🚀 PROJECT 5: EC2 Cost Optimization Scenario

### 🎯 Problem Statement
"Reduce EC2 costs without impacting performance."

### 🧠 WHY THIS PROJECT MATTERS
- Cost optimization = senior mindset

### 🛠️ Implementation Steps (Conceptual)
- Right-size instance
- Use Reserved Instances
- Stop non-prod instances
- Use Spot for batch jobs

### 🎤 Interview Questions
- On-Demand vs Reserved vs Spot?
- How do you detect over-provisioning?
- How to reduce EC2 bill?

---

## 🔥 EC2 INTERVIEW MASTER QUESTIONS

| Question | What They Test |
|----------|----------------|
| EC2 vs Lambda | Architecture thinking |
| Instance selection | Performance awareness |
| Security groups | Security maturity |
| Elastic IP usage | Stability vs scalability |
| Cost models | Financial awareness |

---

## ✅ DAY 3 – FINAL OUTPUT

After these projects, you can:

✔ Deploy production-ready EC2 servers  
✔ Secure compute workloads correctly  
✔ Explain EC2 design trade-offs  
✔ Handle failure & recovery scenarios  
✔ Speak confidently in system design interviews