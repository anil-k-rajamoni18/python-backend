# 🟢 DAY 3 – EC2 (Compute) Deep Dive 🖥️☁️

## Mental model for today:
EC2 is not "a VM".  
**EC2 is a design decision about control, cost, performance, and failure.**

---

## 1️⃣ What is EC2? (WHY EC2 Exists) 🤔

### Traditional Servers (Before EC2)
- Buy hardware
- Install OS manually
- Capacity planning nightmare
- Hardware failure = downtime

### EC2 (Elastic Compute Cloud)
On-demand virtual servers with configurable CPU, memory, storage, and network

🧠 **Why EC2 still matters (even with containers & serverless):**
- Full OS control
- Legacy apps
- Custom networking
- Performance-critical workloads
- Stateful services (sometimes unavoidable)

📌 **Interview Insight:**  
If you don't know when NOT to use EC2, you don't understand EC2.

---

## 2️⃣ EC2 Instance Types (Choosing the Right Hammer) 🧠🔨

**Instance type = performance contract with AWS**

### 🧪 General Purpose
- **t2 / t3**
- Burstable CPU
- Low cost
- Dev, test, small services

🧠 **Think:** "Occasional CPU spikes"

---

### 🧱 Balanced
- **m5**
- Balanced CPU & memory
- Most production web apps

🧠 **Think:** "Default choice if unsure"

---

### 🚀 Compute Optimized
- **c5**
- High CPU
- Low latency
- ML inference, batch processing

🧠 **Think:** "CPU-hungry workloads"

---

### 🔥 Interview Question

> Q: Why not always use c5?

**A:** Cost + memory constraints + unnecessary over-provisioning

---

## 3️⃣ AMI (Amazon Machine Image) 🧩

**AMI = Blueprint of your server**

### Contains:
- OS
- Installed software
- Configurations

### Types of AMIs
- AWS-provided (Amazon Linux)
- Marketplace AMIs
- Custom AMIs

🧠 **WHY AMIs matter:**
- Faster scaling
- Consistency
- Disaster recovery

📌 **Senior Insight:**  
Golden AMIs reduce configuration drift.

---

## 4️⃣ Key Pairs (Secure Access Model) 🔑

- SSH access without passwords
- Public key → AWS
- Private key → You

🧠 **WHY AWS does this:**
- Passwords are weak
- Keys are auditable
- Automation-friendly

⚠️ **Common Mistake:**  
Losing private key = rebuild instance

---

## 5️⃣ Security Groups vs NACL (Interview Gold) 🧠🔥

### 🔐 Security Groups
- Instance-level
- Stateful
- Allow rules only

🧠 **Think:** "Firewall attached to instance"

---

### 🧱 Network ACL (NACL)
- Subnet-level
- Stateless
- Allow + deny rules

🧠 **Think:** "Firewall for the subnet"

---

### 🔥 Interview Comparison

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance | Subnet |
| Stateful | ✅ Yes | ❌ No |
| Rules | Allow only | Allow + Deny |
| Usage | Daily | Rare but critical |

---

## 6️⃣ Elastic IP (Static Identity) 🌍

**Elastic IP = Static public IP**

### WHY it exists
- Public IP changes on restart
- DNS updates take time
- External dependencies break

🧠 **Tradeoff:**
- Free when attached
- Charged when idle

📌 **Interview Insight:**  
Elastic IP is usually replaced by Load Balancer in production.

---

## 7️⃣ Hands-on: Launching EC2 (Thinking First) 🛠️

### Step-by-Step with WHY

**Step 1: Choose AMI**
- Amazon Linux

👉 Stable, AWS-optimized

**Step 2: Choose Instance Type**
- t3.micro

👉 Free tier + burstable

**Step 3: Configure Networking**
- Public subnet
- Auto-assign public IP

👉 Needed for internet access

**Step 4: Security Group**

Allow:
- SSH (22)
- HTTP (80)

👉 Principle of least privilege

**Step 5: Key Pair**
- Create new
- Download once

---

## 8️⃣ SSH into EC2 (Control Moment) 🖥️

**This is where "cloud" becomes real.**

```bash
ssh -i key.pem ec2-user@<public-ip>
```

🧠 **Interview Tip:**  
Explain why SSH keys are better than passwords.

---

## 9️⃣ Hosting a Simple Website (Proof of Compute) 🌐

### Install Nginx
```bash
sudo yum install nginx -y
sudo systemctl start nginx
```

👉 **Shows:**
- Package management
- Service management
- OS control

### Verify
- Open browser → EC2 public IP
- See Nginx page

---

## 🔟 Attach Elastic IP (Stability Test)

### Steps
- Allocate Elastic IP
- Associate with EC2

👉 Public IP no longer changes

---

## ⚠️ Common EC2 Mistakes (Seen in Interviews)

- Opening SSH to 0.0.0.0/0
- Using wrong instance type
- Forgetting to stop instances
- Treating EC2 as "just a VM"

---

## 🎤 Interview Questions You MUST Be Ready For

### EC2 Basics
- Why EC2 instead of Lambda?
- How do you choose instance types?
- What happens if EC2 crashes?

### Security
- Security group vs NACL?
- How do you secure SSH access?

### Cost
- How do you reduce EC2 cost?
- On-Demand vs Reserved vs Spot?

---

## 🧠 System Design Thinking (Senior Level)

**"Design a basic web server on AWS."**

### Expected answer:
- EC2 for compute
- Security groups for firewall
- Elastic IP or ALB
- AMI for consistency
- Auto Scaling (later)

---

## ✅ DAY 3 OUTPUT

By end of Day 3, you can:

✔ Launch & manage EC2 instances  
✔ Explain EC2 tradeoffs clearly  
✔ Secure compute workloads  
✔ Host real applications  
✔ Speak EC2 in interview language