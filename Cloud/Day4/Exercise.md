# 🟢 DAY 4 – HANDS-ON REALTIME PROJECTS
## AWS Storage: S3 + EBS + EFS

---

## 🔴 PROJECT 1: Static Website Hosting for a Startup (S3)

### 📌 Business Scenario

A startup wants:
- A marketing website
- Low cost
- High availability
- No backend servers
- Traffic can spike during campaigns.

### 🧠 WHY S3?
- No servers to manage
- 11 9's durability
- Scales automatically
- Cheapest option

**Senior thinking:** This is a read-heavy, static workload → object storage.

---

### 🛠️ Implementation Steps (Hands-on)

**Step 1: Create S3 Bucket**
- Bucket name: `startup-marketing-site`
- Region: any
- Disable public access temporarily

**Step 2: Upload Website Files**
- `index.html`
- `style.css`
- `error.html`

**Step 3: Enable Static Website Hosting**
- Properties → Static website hosting
- Index: `index.html`
- Error: `error.html`

**Step 4: Configure Bucket Policy**
- Allow public read-only access to objects.
- ⚠️ No write permissions!

**Step 5: Test Website**
- Access via S3 website endpoint
- Validate page loads

---

### 🔥 Production Enhancements (Talk in Interviews)
- CloudFront in front of S3
- HTTPS using ACM
- Versioning for rollback
- Lifecycle rules for logs

---

### ❌ Common Mistakes
- Making entire bucket public
- No CloudFront → slow global access
- Forgetting versioning

---

### 🎤 Interview Questions

**Q1. Why S3 instead of EC2 for website hosting?**  
✅ No servers, cheaper, auto-scale, highly durable

**Q2. Is S3 highly available?**  
✅ Yes, multi-AZ by default

**Q3. Can S3 run backend code?**  
❌ No (needs Lambda / API Gateway)

---

## 🔴 PROJECT 2: EC2 Database Server with Persistent Storage (EBS)

### 📌 Business Scenario

A backend service runs on EC2 and needs:
- Persistent data
- Low latency
- High IOPS
- Example: MySQL / PostgreSQL

### 🧠 WHY EBS?
- Block-level access
- Low latency
- Persistent beyond EC2 lifecycle

**Senior thinking:** Databases need block storage, not object storage.

---

### 🛠️ Implementation Steps

**Step 1: Launch EC2**
- Amazon Linux
- Same AZ as EBS
- Attach default root volume

**Step 2: Create EBS Volume**
- Type: gp3
- Size: 20 GB
- Same AZ as EC2

**Step 3: Attach EBS to EC2**
- Attach as `/dev/xvdf`

**Step 4: Configure Disk on EC2**
```bash
lsblk
sudo mkfs -t xfs /dev/xvdf
sudo mkdir /data
sudo mount /dev/xvdf /data
```

**Step 5: Test Persistence**
- Create file in `/data`
- Stop EC2
- Start EC2
- Data still exists ✅

---

### 🔥 Production Enhancements
- EBS snapshots for backup
- Multi-AZ DB via RDS
- Encryption at rest

---

### ❌ Common Mistakes
- Attaching EBS from different AZ ❌
- Forgetting to mount after reboot
- Using EBS for shared access

---

### 🎤 Interview Questions

**Q1. What happens if EC2 is terminated?**  
✅ EBS survives (unless delete-on-termination)

**Q2. Can multiple EC2s use the same EBS?**  
❌ No (except special io2 multi-attach)

**Q3. Why not store DB data in S3?**  
❌ High latency, no block access

---

## 🔴 PROJECT 3: Shared Uploads for Microservices (EFS)

### 📌 Business Scenario

Multiple EC2 instances need:
- Shared uploads
- Same data view
- Auto-scaling backend
- Example: Image uploads, CMS

### 🧠 WHY EFS?
- Multiple EC2s mount same filesystem
- No manual resizing
- POSIX compatible

**Senior thinking:** Shared state → network file system.

---

### 🛠️ Implementation Steps

**Step 1: Create EFS**
- Default settings
- Enable encryption
- Create mount targets in multiple AZs

**Step 2: Launch 2 EC2 Instances**
- Same VPC
- Allow NFS (port 2049)

**Step 3: Mount EFS on Both EC2s**
```bash
sudo yum install amazon-efs-utils -y
sudo mkdir /shared
sudo mount -t efs fs-xxxx:/ /shared
```

**Step 4: Validate Shared Access**
- Create file on EC2-1
- Read from EC2-2 ✅

---

### 🔥 Production Enhancements
- Use with Auto Scaling Groups
- Access Points for permissions
- Lifecycle management

---

### ❌ Common Mistakes
- Using EFS for databases
- Forgetting NFS security group
- Ignoring cost

---

### 🎤 Interview Questions

**Q1. Why not EBS here?**  
❌ EBS is single-attach

**Q2. Why not S3 for uploads?**  
❌ App expects filesystem semantics

**Q3. Is EFS multi-AZ?**  
✅ Yes

---

## 🔥 SYSTEM DESIGN SCENARIO (VERY IMPORTANT)

### ❓ Design Question:
"Design a web app where users upload images and admins view reports."

### ✅ Senior Answer
- **Frontend assets:** S3 + CloudFront
- **Uploads:** EFS
- **Metadata:** RDS
- **Logs:** S3
- **Compute:** EC2 / ECS

---

## 🧠 FINAL INTERVIEW MASTER QUESTIONS

- S3 vs EBS vs EFS — explain with latency & cost
- Durability vs Availability
- When NOT to use EFS
- How do you back up EBS?
- How does S3 achieve 11 9's?

---

## ✅ FINAL TAKEAWAY (INTERVIEW SIGNAL)

If you can explain:
- **WHY** a storage choice
- What breaks if you choose wrong
- How cost + scale change decisions

👉 **You are thinking like a Senior Cloud Engineer.**