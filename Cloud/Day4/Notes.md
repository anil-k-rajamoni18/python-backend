# 🟢 DAY 4 – AWS Storage Deep Dive (S3 + EBS + EFS) 🗄️☁️

## Mindset for today:
Storage is not about where data sits.  
**It's about durability, performance, access patterns, and cost.**

---

## 🎯 Session Goals

By the end of this session, you should be able to:

✅ Choose correct storage for any system design  
✅ Explain WHY S3 ≠ EBS ≠ EFS  
✅ Defend your choice confidently in interviews  
✅ Avoid common production mistakes

---

## 🧠 Big Picture: Why Storage Decisions Matter

Bad storage choice leads to:

- 💸 Massive AWS bills
- 🐢 Performance bottlenecks
- 🔥 Data loss incidents
- ❌ Interview rejection

**Senior engineers are judged on trade-off thinking, not memorization.**

---

## 1️⃣ Storage Types – Conceptual Foundation 🧱

Let's start with first principles.

### 📦 Object vs Block vs File Storage

### 🟠 Object Storage (S3)

**Think:** Google Drive / Dropbox

- Stores data as objects
- Each object = data + metadata + unique key
- No folders (only prefixes)

📌 **Optimized for:**
- Massive scale
- High durability
- Low cost

---

### 🔵 Block Storage (EBS)

**Think:** Hard disk attached to a server

- Raw disk blocks
- OS controls file system
- Attached to one EC2 at a time

📌 **Optimized for:**
- Databases
- OS disks
- Low-latency I/O

---

### 🟢 File Storage (EFS)

**Think:** Shared network drive

- POSIX-compliant file system
- Mounted on multiple EC2s
- NFS-based

📌 **Optimized for:**
- Shared access
- Microservices
- Content management systems

---

### 🧠 Interview Analogy

| Storage | Real World |
|---------|-----------|
| S3 | Warehouse |
| EBS | Personal laptop hard disk |
| EFS | Shared office file server |

---

## 2️⃣ Amazon S3 – Object Storage Deep Dive 🪣

### 🔍 What is S3?

Infinitely scalable, highly durable object storage

**Key properties:**
- Global service (regional buckets)
- Unlimited objects
- Object size: 0 bytes – 5 TB

### 🧠 WHY Companies Use S3
- 11 9's durability (99.999999999%)
- Cheap storage
- Native integration with almost every AWS service

---

### 🪣 S3 Buckets – Core Concepts

- Bucket name = globally unique
- Objects identified by:
  ```
  s3://bucket-name/key
  ```

📌 No real directories — only prefixes.

---

### 🕒 Versioning – WHY it Matters

**What Versioning Solves**
- Accidental deletes
- Overwrites
- Rollbacks

**How It Works**
- Every update creates a new version
- Delete = delete marker

📌 **Interview Insight:**  
Versioning is a data protection feature, not a backup solution.

---

### ♻️ Lifecycle Rules – Cost Optimization Tool

**WHY Lifecycle Rules Exist**
- Old data is rarely accessed
- Storage costs add up silently

**Typical Lifecycle Flow**
```
S3 Standard
 → S3 IA (30 days)
 → Glacier (90 days)
 → Delete (365 days)
```

📌 **Used heavily in:**
- Logs
- Compliance data
- ML datasets

---

### 🌐 Hosting Static Website on S3

**WHY Use S3 for Static Websites**
- No servers
- No patching
- Near-zero cost
- Massive scale

**How It Works (Conceptually)**
- Enable static website hosting
- Public read access (via policy)
- Upload HTML/CSS/JS

📌 **Tradeoff:**  
No backend logic → Pair with API Gateway + Lambda

---

### ⚠️ Common S3 Mistakes

- Making buckets public unintentionally
- No lifecycle rules → huge bills
- Using S3 like a database ❌

---

## 3️⃣ Amazon EBS – Block Storage 🧲

### 🔍 What is EBS?

- Persistent block storage for EC2
- Exists independently of EC2
- Can be detached & reattached
- AZ-scoped

### 🧠 WHY EBS Exists

EC2 instances are ephemeral

**You need persistent disks for:**
- OS
- Databases
- Applications

---

### 🧠 EBS Volume Types (High-Level)

| Type | Use Case |
|------|----------|
| gp3 | General purpose |
| io2 | High IOPS databases |
| st1 | Throughput-heavy |
| sc1 | Cold data |

---

### 🧪 Hands-on Concept: Attach EBS to EC2

**What happens internally:**
1. Disk attached
2. OS detects block device
3. You format
4. You mount

📌 **Key Insight:**  
EBS is useless without a filesystem.

---

### ⚠️ Common EBS Mistakes

- Assuming EBS is multi-attach (default ❌)
- Forgetting AZ limitation
- Over-provisioning IOPS

---

## 4️⃣ Amazon EFS – File Storage 📁

### 🔍 What is EFS?

- Fully managed, elastic, shared file system
- Multiple EC2s can mount simultaneously
- Scales automatically
- Linux-only

### 🧠 WHY Use EFS

**Use when:**
- Shared configuration
- Shared uploads
- CMS (WordPress, Drupal)
- ML training data

---

### 🧠 EFS vs EBS (Critical Interview Topic)

| Feature | EBS | EFS |
|---------|-----|-----|
| Attachment | Single EC2 | Multiple EC2 |
| Performance | Very high | Moderate |
| Cost | Lower | Higher |
| Use case | Databases | Shared storage |

---

### ⚠️ EFS Tradeoffs

- Higher latency than EBS
- More expensive
- Not ideal for databases

---

## 5️⃣ S3 vs EBS vs EFS – Interview Master Table 🧠🔥

| Scenario | Correct Choice | WHY |
|----------|----------------|-----|
| Static website | S3 | Cheap, scalable |
| Database | EBS | Low latency |
| Shared uploads | EFS | Multi-attach |
| Logs | S3 | Durability |
| EC2 OS disk | EBS | Boot support |
| ML datasets | S3 / EFS | Scale |

---

## 6️⃣ Interview Focus Topics 🎤

### ❓ When to Use S3 vs EBS?

**Answer Structure:**
- Access pattern
- Latency needs
- Scalability
- Cost

**Example:** "S3 for object-based, highly durable data; EBS for low-latency block storage attached to EC2."

---

### ❓ What Does 11 9's Durability Mean?

Data loss probability is near-zero

**Achieved via:**
- Multi-AZ replication
- Integrity checks
- Self-healing

📌 **Important:** Durability ≠ availability

---

### ❓ Why Not Use EFS Everywhere?

- Cost
- Latency
- Overkill for single-instance workloads

---

## 7️⃣ Common Interview Traps 🚨

❌ Saying S3 is a filesystem  
❌ Ignoring cost implications  
❌ Confusing durability with backup  
❌ Using EBS for shared workloads

---

## ✅ DAY 4 – FINAL TAKEAWAYS

You now understand:

✔ Object vs Block vs File storage  
✔ How S3, EBS, and EFS differ fundamentally  
✔ When to use each in real systems  
✔ How to justify decisions like a senior engineer