# 🟢 DAY 1 – HANDS-ON REALTIME PROJECTS (AWS FUNDAMENTALS)

---

## 🚀 PROJECT 1: Secure AWS Account Setup (Enterprise-Grade)

### 🎯 Problem Statement
"Set up a production-ready AWS account with proper security and access controls."

**This is not optional in real companies.**

### 🧠 Why This Project Matters
- 90% of cloud breaches = bad IAM
- Interviewers assume you know this
- Shows security-first mindset

### 🏗️ Architecture
```
AWS Root Account
   |
IAM Users + Groups
   |
IAM Roles
   |
MFA Enabled
```

### 🛠️ Implementation Steps

**Step 1: Root Account Hardening**
- Login as root
- Enable MFA
- Disable access keys for root

**Step 2: IAM Structure**
- Create IAM groups:
  - Admins
  - Developers
  - ReadOnly
- Attach AWS managed policies

**Step 3: IAM User Creation**
- Create user (no access keys initially)
- Force password reset
- Enable MFA

**Step 4: IAM Role (Preview for Day 2)**
- Create EC2 role with limited permissions

### ⚠️ Common Mistakes
- Using root for daily tasks
- Giving AdministratorAccess to everyone
- No MFA

### 🎤 Interview Questions
- **Q:** Why should root account never be used daily?
- **Q:** IAM User vs IAM Role?
- **Q:** What happens if MFA is compromised?

---

## 🚀 PROJECT 2: Multi-Region Architecture Understanding (Design-Oriented)

### 🎯 Problem Statement
"Design a highly available AWS setup for a global application."

### 🧠 Why This Project Matters
- Appears in every system design interview
- Tests AWS global infrastructure knowledge

### 🏗️ Architecture Diagram (Conceptual)
```
Region A (ap-south-1)
 ├─ AZ1
 ├─ AZ2

Region B (us-east-1)
 ├─ AZ1
 ├─ AZ2
```

### 🛠️ Implementation Steps (Console-Based)

**Step 1: Switch Regions**
- Create S3 bucket in Mumbai
- Create S3 bucket in Virginia

**Step 2: Observe Differences**
- Region-specific names
- Latency awareness

**Step 3: Think Through Failure**
- What happens if ap-south-1 goes down?

### 🧠 Tradeoffs
- Multi-region = expensive
- Complexity vs availability

### 🎤 Interview Questions
- **Q:** Difference between Region & AZ?
- **Q:** When do you need multi-region?
- **Q:** Why not deploy everything globally?

---

## 🚀 PROJECT 3: Static Website Hosting Using S3 + Edge Locations

### 🎯 Problem Statement
"Host a globally available static website with low latency."

### 🧠 Why This Project Matters
- Shows Edge + S3 understanding
- Real-world use case

### 🏗️ Architecture
```
User → CloudFront (Edge)
           ↓
         S3 Bucket
```

### 🛠️ Implementation Steps

**Step 1: Create S3 Bucket**
- Enable static website hosting
- Upload index.html

**Step 2: Permissions**
- Bucket policy for public read

**Step 3: Add CloudFront**
- Origin: S3
- Enable caching

### ⚠️ Common Mistakes
- Making S3 public accidentally
- Forgetting HTTPS via CloudFront

### 🎤 Interview Questions
- **Q:** Why CloudFront in front of S3?
- **Q:** Edge locations vs regions?
- **Q:** How does caching reduce cost?

---

## 🚀 PROJECT 4: Cost Awareness & Billing Guardrails

### 🎯 Problem Statement
"Prevent unexpected AWS bills in production."

### 🧠 Why This Project Matters
- Cost overruns kill startups
- Interviewers love cost-aware engineers

### 🛠️ Implementation Steps

**Step 1: Billing Alerts**
- Create AWS Budget
- Set alert at 80%

**Step 2: Cost Explorer**
- Analyze service usage

**Step 3: Free Tier Monitoring**
- Identify limits

### ⚠️ Common Mistakes
- No budgets
- Forgetting running EC2 instances

### 🎤 Interview Questions
- **Q:** How do you control cloud cost?
- **Q:** Why cloud is not always cheaper?
- **Q:** How would you reduce AWS bill?

---

## 🧠 SYSTEM DESIGN THINKING EXERCISE (CRITICAL)

**"Design a basic web app using AWS core services."**

### Expected Answer Structure
- EC2 for compute
- ELB for traffic
- RDS for DB
- S3 for assets
- IAM for security
- Multi-AZ for HA

---

## 📌 How to Explain These Projects in Interviews

❌ "I created an AWS account and hosted a website."

✅ "I designed a secure AWS account with IAM best practices, enabled MFA, and deployed a globally cached static site using S3 and CloudFront with cost controls."

---

## ✅ FINAL OUTPUT (DAY 1 PROJECTS)

✔ Real AWS experience  
✔ Security-first mindset  
✔ Architecture thinking  
✔ Cost awareness  
✔ Interview-ready explanations