# 🟡 DAY 5 – HANDS-ON REALTIME PROJECTS
## AWS Networking (VPC, Subnets, IGW, NAT, Routing, Security) 🌐

---

## 🔴 PROJECT 1: Secure Public Web Server Architecture

### 📌 Business Scenario

A company wants:
- Public website accessible from internet
- EC2 server should be reachable via browser
- Future backend DB must be private

### 🧠 WHY This Design?
- Public subnet for internet-facing workloads
- Controlled inbound access
- Separation of concerns for security

**Senior insight:** Never put everything in public subnet "for simplicity".

---

### 🏗️ Architecture
```
VPC (10.0.0.0/16)
└── Public Subnet (10.0.1.0/24)
    ├── EC2 (Web Server)
    └── Internet Gateway
```

---

### 🛠️ Implementation Steps

**Step 1: Create VPC**
- CIDR: 10.0.0.0/16
- Enable DNS hostnames

**Step 2: Create Public Subnet**
- CIDR: 10.0.1.0/24
- Auto-assign public IP → ENABLE

**Step 3: Create Internet Gateway**
- Attach to VPC

**Step 4: Route Table**

Add route:
```
0.0.0.0/0 → IGW
```
- Associate with public subnet

**Step 5: Launch EC2**
- Amazon Linux
- Public subnet
- Assign public IP
- SG: Allow 22, 80

**Step 6: Test**
- SSH into EC2
- Install Nginx
- Access via browser

---

### ❌ Common Mistakes
- Public IP but no IGW route
- SG allows traffic but route table blocks it
- Using 0.0.0.0/0 for SSH

---

### 🎤 Interview Questions

**Q1: What makes a subnet public?**  
✅ Route to IGW, not public IP alone

**Q2: Can EC2 in private subnet have public IP?**  
❌ No

---

## 🔴 PROJECT 2: Private Backend with Internet Access (NAT Gateway)

### 📌 Business Scenario

Backend servers need:
- Internet access for updates
- Must not be accessible from internet

### 🧠 WHY NAT Gateway?
- Outbound access only
- Prevents inbound exposure
- Compliance-friendly

---

### 🏗️ Architecture
```
VPC
├── Public Subnet
│   └── NAT Gateway
└── Private Subnet
    └── EC2 (Backend)
```

---

### 🛠️ Implementation Steps

**Step 1: Create Private Subnet**
- CIDR: 10.0.2.0/24
- No public IP

**Step 2: Create NAT Gateway**
- In public subnet
- Attach Elastic IP

**Step 3: Update Route Table (Private)**
```
0.0.0.0/0 → NAT Gateway
```

**Step 4: Launch EC2 in Private Subnet**
- No public IP
- SG allows outbound

**Step 5: Test**
- SSH via bastion or SSM
- Run `yum update`

---

### ❌ Common Mistakes
- NAT in private subnet ❌
- Forgetting Elastic IP
- Expecting inbound traffic to work

---

### 🎤 Interview Questions

**Q1: Why not use IGW for private EC2?**  
❌ Security risk

**Q2: Is NAT stateful?**  
✅ Yes

---

## 🔴 PROJECT 3: Secure RDS in Private Subnet

### 📌 Business Scenario

Production database must:
- Never be exposed publicly
- Only accessible by backend services

### 🧠 WHY Private Subnet?
- Databases should not be internet-facing
- Reduces attack surface

---

### 🏗️ Architecture
```
Public Subnet → EC2
Private Subnet → RDS
```

---

### 🛠️ Implementation Steps

**Step 1: Create DB Subnet Group**
- Only private subnets

**Step 2: Launch RDS**
- Public access: ❌ NO
- SG: Allow DB port only from backend SG

**Step 3: Test Connectivity**
- Connect from EC2
- Try from local → FAIL (expected)

---

### ❌ Common Mistakes
- Publicly accessible RDS
- Using 0.0.0.0/0 for DB SG

---

### 🎤 Interview Questions

**Q1: Can RDS access internet?**  
✅ Via NAT if required

**Q2: How do you secure DB access?**  
SG referencing SG (not IPs)

---

## 🔴 PROJECT 4: Bastion Host Pattern (Production Standard)

### 📌 Business Scenario

Admins need SSH access to private servers securely.

### 🧠 WHY Bastion?
- Single controlled entry point
- Auditable access
- Minimal exposure

---

### 🏗️ Architecture
```
Internet
 → Bastion (Public)
 → Private EC2
```

---

### 🛠️ Implementation Steps

- Launch Bastion in public subnet
- Allow SSH only from office IP
- Private EC2 allows SSH only from Bastion SG
- Disable public IP on private EC2

---

### ❌ Common Mistakes
- SSH open to world
- Direct access to private EC2

---

### 🎤 Interview Questions

**Q1: Bastion vs SSM?**  
SSM preferred (no SSH, no keys)

---

## 🔥 SYSTEM DESIGN INTERVIEW SCENARIO

### ❓ Question:
"Design a highly secure web application network on AWS."

### ✅ Senior Answer Structure:
- VPC with /16 CIDR
- Public subnets → ALB, Bastion
- Private subnets → App, DB
- NAT for outbound
- SG-based access
- No public DB

---

## 🧠 FINAL INTERVIEW CHEAT QUESTIONS

- Public vs private subnet?
- Why NAT is expensive?
- SG vs NACL?
- Can private EC2 access S3?
- How to debug "no internet" on EC2?

---

## ✅ FINAL TAKEAWAY (INTERVIEW SIGNAL)

If you can:
- Draw VPC architecture
- Explain traffic flow
- Justify NAT + private subnets
- Avoid common traps

👉 **You are thinking like a Senior Cloud Engineer.**