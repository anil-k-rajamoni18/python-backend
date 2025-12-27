# 🟢 DAY 1 – Cloud Fundamentals + AWS Basics ☁️

## Mindset for today:
**Don't memorize services.**  
Understand why cloud exists, how AWS is structured, and how interviewers expect you to think.

---

## 1️⃣ What is Cloud Computing? (The WHY) 🤔

### Traditional IT (Before Cloud)
- Buy physical servers
- Predict peak load (often wrong)
- Over-provision hardware
- Weeks/months to provision infra
- Infra team + procurement + data center

💡 **Problem:** Slow, expensive, inflexible.

### Cloud Computing (Core Idea)
**Cloud = On-demand computing resources delivered over the internet, billed per use**

Think of cloud like:
🚕 **Uber for servers**
- You don't own the car
- You pay only when you ride
- You scale instantly

### Key Characteristics (Interview Favorite)
- On-demand self-service
- Elastic scalability
- Pay-as-you-go
- High availability by design
- Global access

📌 **Interview Follow-up Question:**

> "Why did companies move to cloud?"

**Answer:** Cost efficiency, speed, scalability, reliability, and focus on business instead of infrastructure.

---

## 2️⃣ IaaS vs PaaS vs SaaS (Mental Model, Not Definitions) 🧠

### Think in terms of Who Manages What

### 🧱 IaaS – Infrastructure as a Service
"AWS gives you the building blocks"

**You manage:**
- OS
- Runtime
- Application

**AWS manages:**
- Hardware
- Data center
- Networking

📌 **Examples:**
- EC2
- EBS
- VPC

🧠 **Use When:** You want full control

---

### 🧩 PaaS – Platform as a Service
"AWS runs the platform, you run the code"

**You manage:**
- Application logic

**AWS manages:**
- OS
- Scaling
- Patching

📌 **Examples:**
- Elastic Beanstalk
- Lambda
- RDS (partially)

🧠 **Use When:** You want speed, not control

---

### 🧑‍💻 SaaS – Software as a Service
"You just use the product"

**You manage:**
- Nothing infra-related

**Provider manages everything**

📌 **Examples:**
- Gmail
- Salesforce
- Slack

---

### 🔥 Interview Trap

> Q: "Is RDS IaaS or PaaS?"

**A:** Managed PaaS (you manage schema, not OS)

---

## 3️⃣ Public vs Private vs Hybrid Cloud 🌍

### ☁️ Public Cloud
- Shared infrastructure
- Managed by AWS
- Most startups + enterprises

📌 **Example:** AWS

---

### 🏢 Private Cloud
- Dedicated infrastructure
- On-prem or hosted
- More control, less agility

📌 **Example:** On-prem OpenStack

---

### 🔗 Hybrid Cloud
"Best of both worlds"
- Sensitive workloads on-prem
- Scalable workloads on AWS

📌 **Example:**
- Bank runs core DB on-prem
- Runs analytics on AWS

🧠 **Interview Insight:**  
Hybrid is about risk, regulation, and migration strategy, not technology alone.

---

## 4️⃣ Why AWS Dominates the Market 🏆

Interviewers care more about reasoning than stats.

### Key Reasons
- First mover advantage
- Massive global footprint
- Deep service ecosystem
- Enterprise trust
- Strong security + compliance
- Tight service integration

💡 AWS is not "better", it's more mature and battle-tested.

---

## 5️⃣ AWS Global Infrastructure 🌐 (VERY IMPORTANT)

This section appears directly in system design interviews.

### 🌍 Regions
**A Region = geographic area**

**Example:**
- us-east-1 (N. Virginia)
- ap-south-1 (Mumbai)

📌 **Why Regions exist**
- Data residency
- Latency
- Fault isolation

---

### 🧱 Availability Zones (AZs)
- A physically separate data center within a region
- 1 Region → multiple AZs
- Independent power, cooling, network

🧠 **Golden Rule**  
**Never deploy production workloads in a single AZ.**

---

### 🚀 Edge Locations
- Used for content delivery
- Powered by CloudFront
- Cache content close to users
- Reduce latency

📌 **Example:**  
Static images served from nearest edge

---

### 🔥 Interview Question

> Q: "Why not just use one AZ?"

**A:** AZ failure ≠ Region failure. Multi-AZ ensures high availability.

---

## 6️⃣ AWS Core Services Overview (Big Picture) 🧩

**Don't memorize APIs.**  
Understand the role each service plays in an architecture.

### 🖥️ EC2 – Compute
- Virtual servers
- Full control
- Backbone of many systems

🧠 **Think:** "VMs in the cloud"

---

### 📦 S3 – Object Storage
- Store files, backups, media
- Infinitely scalable
- 11 9's durability

🧠 **Think:** "Google Drive at cloud scale"

---

### 🗄️ RDS – Managed Databases
- MySQL, PostgreSQL, etc.
- Automated backups
- Multi-AZ support

🧠 **Think:** "DB without OS headaches"

---

### 🔐 IAM – Identity & Access
- Users, roles, policies
- Security backbone of AWS

🧠 **Think:** "Who can do what"

---

### 🌐 VPC – Networking
- Private network in AWS
- Subnets, routing, firewalls

🧠 **Think:** "Your own data center in AWS"

---

### ⚖️ ELB – Load Balancing
- Distributes traffic
- Health checks
- High availability

---

### 📈 Auto Scaling
- Adjusts capacity automatically
- Saves cost
- Handles spikes

---

### 🧠 System Design View
```
User → ELB → EC2 → RDS
           ↓
          S3
```

---

## 7️⃣ Hands-on (Foundational, Not Technical) 🛠️

### Step 1: Create AWS Free Tier Account
- Use personal email
- Add credit card
- Choose basic support

### Step 2: Explore AWS Console
- Notice service categories
- Search bar (used daily)
- Region selector (top-right)

📌 **Mistake:** Creating resources in wrong region

### Step 3: Billing Dashboard 💰
**Understand:**
- Free tier limits
- Cost explorer
- Budgets

📌 **Interview Tip:**  
Cost awareness = senior engineer mindset.

### Step 4: Enable MFA (Critical)
- Root account → MFA
- IAM users → MFA

🧠 **Security mindset:**  
Root account is never for daily use.

---

## 8️⃣ Common Beginner Mistakes 🚨

- Using root account daily
- Ignoring regions
- Forgetting to delete resources
- Assuming AWS is "automatically secure"
- Thinking cloud = cheaper always

---

## 9️⃣ How Interviewers Evaluate You on Day-1 Topics 🎯

**They look for:**
- Clear mental models
- Architecture thinking
- Security awareness
- Cost consciousness
- Ability to explain tradeoffs

❌ "AWS has EC2, S3, RDS…"  
✅ "I'd use EC2 when I need OS control, S3 for durable object storage…"

---

## ✅ DAY 1 OUTPUT (What You Should Now Be Able to Do)

✔ Explain why cloud exists  
✔ Describe AWS global architecture confidently  
✔ Talk about AWS services in system design language  
✔ Avoid beginner-level cloud mistakes  
✔ Sound like a senior engineer, not a cert crammer