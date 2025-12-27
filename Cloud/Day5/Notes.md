# 🟡 DAY 5 – AWS Networking (VPC) 🌐

**"If you don't understand VPC, you don't understand AWS."**

## 🔑 Mental Model for Today:
A VPC is your private data center inside AWS, with controlled entry and exit points.

---

## 🎯 Session Goals

By the end of this session, you should be able to:

✅ Design secure AWS networks  
✅ Explain public vs private subnets clearly  
✅ Debug "EC2 has no internet" issues  
✅ Confidently answer VPC interview questions  
✅ Read & draw AWS network diagrams

---

## 1️⃣ What is a VPC? (Start with WHY)

### ❓ Why does AWS even need VPCs?

AWS serves millions of customers. Without isolation:
- Networks would clash
- IPs would overlap
- Security would be impossible

### ✅ VPC = Logical Network Isolation
- Your own IP range
- Your own routing
- Your own firewall rules

📌 **Interview one-liner:**

"A VPC is a logically isolated virtual network where we define IP ranges, routing, and security."

---

### 🏢 Real-World Analogy

| AWS Concept | Real World |
|-------------|-----------|
| VPC | Office building |
| Subnet | Floor |
| Route Table | GPS directions |
| IGW | Main gate |
| NAT | Reception desk |
| Security Group | Door lock |
| NACL | Building security policy |

---

## 2️⃣ CIDR Blocks – IP Planning 🧠

### What is CIDR?

CIDR defines how many IPs you get.

**Example:**
```
10.0.0.0/16
```
- Total IPs ≈ 65,536
- Private IP range (RFC 1918)

### Why CIDR Planning Matters

❌ Bad CIDR → No room for growth  
❌ Overlapping CIDRs → VPC peering fails

📌 **Senior Tip:**  
Always think future expansion (multi-AZ, more subnets, peering).

---

### Common Interview Question

> Q: Can two VPCs with same CIDR be peered?

❌ No, overlapping CIDRs are not allowed.

---

## 3️⃣ Subnets – Public vs Private 🧩

### 🔹 What is a Subnet?

A subnet is a portion of a VPC CIDR, tied to one AZ.

---

### 🌍 Public Subnet

**Definition**

A subnet is public if:
- Its route table has a route to Internet Gateway (IGW)

**Typical Resources**
- Bastion host
- Load Balancer
- Public EC2

📌 **Important:**  
Public subnet ≠ public IP  
(EC2 must explicitly get a public IP)

---

### 🔒 Private Subnet

**Definition**

A subnet is private if:
- No direct route to IGW

**Typical Resources**
- RDS
- Backend EC2
- Internal services

📌 Private ≠ No internet  
(Outbound access via NAT is possible)

---

### Interview Trap 🚨

❌ "Private subnet means no internet"  
✅ **Correct:** No direct inbound internet

---

## 4️⃣ Internet Gateway (IGW) 🌐

### What is IGW?
- AWS-managed gateway
- Enables internet traffic for VPC

### IGW Rules
- One IGW per VPC
- Stateless
- Required for public subnets

📌 **Without IGW → No internet, no matter what.**

---

## 5️⃣ NAT Gateway – Controlled Internet Access 🔁

### Why NAT Exists

Private resources need:
- Software updates
- API calls
- Outbound internet

But must not be reachable from internet.

### How NAT Works
```
Private EC2 → NAT Gateway → Internet
Internet → ❌ cannot initiate back
```

### Key Properties
- Lives in public subnet
- Uses Elastic IP
- Outbound only

---

### Interview Gold Question

> Q: Why not put EC2 directly in public subnet?

✅ Security, compliance, reduced attack surface

---

## 6️⃣ Route Tables – Traffic Control 🧭

### What is a Route Table?

A set of rules:
```
Destination → Target
```

**Example:**
```
0.0.0.0/0 → IGW
```

### Typical Setup

| Subnet | Route |
|--------|-------|
| Public | 0.0.0.0/0 → IGW |
| Private | 0.0.0.0/0 → NAT |

📌 **Key Debug Rule:**  
No route → no traffic (even if SG allows)

---

## 7️⃣ Security Group vs NACL 🔐🔥 (VERY IMPORTANT)

### 🔒 Security Groups (SG)
- Instance-level firewall
- Stateful
- Allow rules only

📌 If inbound allowed → response allowed automatically

---

### 🚧 Network ACL (NACL)
- Subnet-level firewall
- Stateless
- Allow + Deny rules

📌 Both inbound & outbound must be allowed

---

### Interview Comparison Table

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Usage | Primary defense | Extra layer |

---

### Interview Insight

"Security Groups are sufficient in most cases; NACLs are for coarse-grained control."

---

## 8️⃣ Hands-On Walkthrough (Conceptual Steps) 🛠️

**Step 1: Create Custom VPC**
- CIDR: 10.0.0.0/16
- Enable DNS

**Step 2: Create Subnets**
- Public Subnet: 10.0.1.0/24
- Private Subnet: 10.0.2.0/24
- Place in same AZ initially

**Step 3: Create & Attach IGW**
- Attach IGW to VPC

**Step 4: Configure Route Tables**
- Public RT → IGW
- Private RT → NAT Gateway

**Step 5: Launch EC2 in Public Subnet**
- Assign public IP
- Open port 22 / 80 in SG

**Step 6: Test Connectivity**
- SSH from local machine
- Ping external site

**If fails → check:**
- Route table
- IGW attachment
- SG rules

---

## 9️⃣ Diagram Understanding (INTERVIEW ESSENTIAL)

```
VPC (10.0.0.0/16)
│
├── Public Subnet (10.0.1.0/24)
│    ├── EC2 (Public IP)
│    └── Internet Gateway
│
└── Private Subnet (10.0.2.0/24)
     ├── RDS
     └── NAT Gateway (via public subnet)
```

📌 **You MUST be able to draw this on a whiteboard**

---

## 🔥 Common Production Mistakes

❌ EC2 has public IP but no internet (missing IGW route)  
❌ NAT in private subnet  
❌ Overlapping CIDRs across environments  
❌ Opening 0.0.0.0/0 everywhere

---

## 🎤 Senior Interview Questions & Expected Answers

### Q1: How does traffic reach EC2 in public subnet?

**Answer:**  
Public IP → IGW → Route Table → Subnet → SG → EC2

### Q2: Can RDS be in public subnet?

Technically yes, but never recommended.

### Q3: Why is NAT Gateway expensive?

- Managed service
- High availability
- Data processing costs

### Q4: SG vs NACL – which one do you use?

- SG for most cases
- NACL for additional boundary control

---

## ✅ DAY 5 – FINAL TAKEAWAYS

✔ You understand AWS networking architecture  
✔ You can debug connectivity issues logically  
✔ You can explain VPC designs confidently  
✔ You think like a system designer, not a console clicker