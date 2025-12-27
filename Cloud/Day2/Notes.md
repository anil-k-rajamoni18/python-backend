# 🟢 DAY 2 – IAM (Identity & Access Management) 🔐

**Secure by design. Trusted by enterprises. Non-negotiable in interviews.**

## Mental Model for IAM:
IAM is not about users clicking buttons.  
**IAM is about controlling blast radius when things go wrong.**

---

## 1️⃣ Root Account vs IAM User (WHY FIRST) 🧠

### 🔥 Root Account
- Created when AWS account is created
- Has unrestricted power
- Cannot be limited by policies

🧠 **Analogy:**  
Root is like the master key to the building — you lock it away, not carry it daily.

### Best Practice
- Enable MFA
- Never create access keys
- Never use it for daily work

---

### 👤 IAM User
- Represents a human
- Has long-term credentials
- Should be tightly scoped

🧠 **Interview Insight:**  
Modern AWS environments minimize IAM users and favor roles.

---

## 2️⃣ IAM Core Components (How AWS Thinks) 🧩

### 🧑 Users
- Humans
- Console / CLI access

---

### 👥 Groups
- Collection of users
- Permissions assigned once

🧠 **WHY groups exist:**  
Permissions scale better than managing users individually.

---

### 🎭 Roles (MOST IMPORTANT)
- No credentials
- Assumed temporarily
- Used by:
  - EC2
  - Lambda
  - ECS
  - EKS
  - Cross-account access

🧠 **Golden Rule**  
**Machines should never use access keys.**

---

### 📜 Policies (JSON)
- Define what is allowed or denied
- Attached to:
  - Users
  - Groups
  - Roles

---

## 3️⃣ Policy Evaluation Logic (INTERVIEW GOLD) 🧠🔥

AWS checks permissions in this order:

1. **Explicit DENY**
2. **Explicit ALLOW**
3. **Default DENY**

**If not explicitly allowed → it is denied**

🧠 **Follow-up Question:**

> "What happens if one policy allows and another denies?"

**Answer:** Deny always wins.

---

## 4️⃣ Principle of Least Privilege (Security Mindset) 🎯

### What it means
- Give only what is required
- Nothing more
- Nothing permanent

### Why it matters
- Limits damage
- Meets compliance
- Passes audits

🧠 **Senior Engineer Thinking**  
Security is about reducing blast radius, not trusting people.

---

## 🛠️ HANDS-ON REALTIME PROJECTS (IAM)

These are production-grade, not tutorials.

---

## 🚀 PROJECT 1: Secure Enterprise IAM Setup

### 🎯 Problem Statement
"Create a secure IAM structure for a growing engineering team."

### 🏗️ Architecture
```
Root Account (Locked)
   |
IAM Groups
   ├── Admins
   ├── Developers
   └── ReadOnly
```

### 🛠️ Implementation Steps

**Step 1: Root Hardening**
- Enable MFA
- Remove access keys

**Step 2: Create Groups**
- Admins → AdministratorAccess
- Developers → PowerUserAccess
- ReadOnly → ReadOnlyAccess

**Step 3: Create IAM Users**
- Assign to groups
- Enforce password reset
- Enable MFA

### ⚠️ Common Mistakes
- Giving Admin to everyone
- No MFA
- Users instead of roles for services

### 🎤 Interview Questions
- Why not use root?
- Why groups over individual policies?
- How do you audit IAM usage?

---

## 🚀 PROJECT 2: Read-Only Audit User (Security Scenario)

### 🎯 Problem Statement
"Create a user that can view everything but modify nothing."

### 🛠️ Implementation Steps
- Create IAM user
- Attach ReadOnlyAccess
- Test:
  - Can list EC2
  - Cannot stop instance

### 🧠 WHY Interviewers Love This
- Shows understanding of least privilege
- Real audit scenario

### 🎤 Interview Questions
- Difference between ReadOnly and PowerUser?
- Why auditors don't need write access?

---

## 🚀 PROJECT 3: EC2 Role for Secure S3 Access (CRITICAL)

### 🎯 Problem Statement
"Allow EC2 to access S3 without access keys."

### 🏗️ Architecture
```
EC2 Instance
   |
IAM Role
   |
S3 Bucket
```

### 🛠️ Implementation Steps

**Step 1: Create IAM Role**
- Trusted entity: EC2
- Policy: S3 read access

**Step 2: Attach Role to EC2**
- No access keys used

**Step 3: Test Access**
- EC2 can read S3
- Cannot access other services

### 🧠 WHY This Is Non-Negotiable
- Access keys leak
- Roles rotate credentials automatically

### 🎤 Interview Questions
- Why roles instead of access keys?
- How does AWS rotate credentials?
- What is STS?

---

## 🚀 PROJECT 4: Permission Boundary Scenario (Advanced)

### 🎯 Problem Statement
"Limit what even admins can do."

### 🧠 Use Case
- Prevent deleting IAM
- Prevent disabling logging

### 🛠️ Implementation Steps (Conceptual)
- Create permission boundary
- Attach to admin roles
- Test restricted actions

### 🎤 Interview Questions
- What are permission boundaries?
- Difference between SCP and IAM policy?

---

## 🔥 IAM INTERVIEW RAPID-FIRE QUESTIONS

| Question | What Interviewer Wants |
|----------|------------------------|
| User vs Role | Security maturity |
| Why no access keys | Best practice |
| How AWS evaluates policy | Deep knowledge |
| How to prevent privilege escalation | Senior thinking |
| How IAM scales | Architecture mindset |

---

## 🚨 Common IAM Anti-Patterns

- Hard-coded credentials
- One user = many permissions
- No role separation
- Overusing AdministratorAccess

---

## ✅ DAY 2 OUTPUT (What You Can Do Now)

✔ Design secure IAM architectures  
✔ Explain IAM decisions confidently  
✔ Pass IAM interview rounds  
✔ Build enterprise-grade access models  
✔ Think like a security-aware cloud engineer