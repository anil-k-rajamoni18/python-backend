# 🟡 DAY 6 – Load Balancer & Auto Scaling ⚖️📈

**"Scalability is not adding servers. It's removing single points of failure."**


---

## 1️⃣ High Availability – Start with WHY 🧠

### ❓ Why High Availability?

Systems fail because of:
- Hardware failure
- AZ outages
- Traffic spikes
- Bad deployments

HA ensures:
- No downtime
- Graceful failure
- Elastic scale

📌 **Interview one-liner:**

"High availability is achieved by removing single points of failure using redundancy across AZs."

---

### 🏗️ HA in AWS = Multi-AZ Architecture

- Multiple EC2s
- Multiple subnets
- Multiple AZs
- Load balancer in front

---

## 2️⃣ Elastic Load Balancer (ELB) ⚖️

### What is ELB?

A managed service that distributes incoming traffic across healthy targets.

### WHY ELB?
- No single server dependency
- Built-in health checks
- Native AWS scaling

---

### Types of Load Balancers

### 🟢 Application Load Balancer (ALB)

**Layer 7 (HTTP/HTTPS)**

**Supports:**
- Path-based routing
- Host-based routing
- WebSockets
- HTTP headers

📌 **Used for:**
- Web apps
- APIs
- Microservices

---

### 🔵 Network Load Balancer (NLB)

**Layer 4 (TCP/UDP)**

**Supports:**
- Ultra-low latency
- Static IP
- Millions of requests/sec

📌 **Used for:**
- Real-time systems
- Gaming
- Financial apps

---

### 🎤 Interview Comparison Table

| Feature | ALB | NLB |
|---------|-----|-----|
| Layer | L7 | L4 |
| Routing | Path/Host | TCP |
| Latency | Higher | Ultra-low |
| Use Case | Web apps | High-performance |

---

## 3️⃣ Health Checks ❤️‍🩹

### Why Health Checks Matter

Without health checks:
- Load balancer sends traffic to dead servers
- Users see errors

### How Health Checks Work
- ELB pings target (e.g. `/health`)
- If unhealthy → traffic stops

📌 **Important:**  
Health checks ≠ Auto Scaling checks (different layers)

---

## 4️⃣ Auto Scaling Groups (ASG) 📈

### What is ASG?

A group of EC2 instances that automatically scales based on demand.

### WHY Auto Scaling?
- Handle traffic spikes
- Reduce cost during low usage
- Replace failed instances

---

### Core ASG Components
- Launch Template
- Min / Desired / Max capacity
- Scaling policies
- Health checks

---

### Scaling Types
- Target tracking (CPU 60%)
- Step scaling
- Scheduled scaling

📌 **Senior tip:** Target tracking is most common.

---

## 5️⃣ Hands-On Architecture (Conceptual Flow) 🛠️

```
Internet
   ↓
Application Load Balancer
   ↓
Auto Scaling Group
   ↓
EC2 Instances (Multi-AZ)
```

---

### 🛠️ Hands-On Walkthrough (Step-by-Step)

**Step 1: Launch EC2 Instances**
- Same AMI
- Same security group
- Different AZs
- Install Nginx

Each server returns:
```
Hello from EC2-1
Hello from EC2-2
```

**Step 2: Create Target Group**
- Target type: Instance
- Health check path: `/`

**Step 3: Create Application Load Balancer**
- Internet-facing
- Public subnets in 2 AZs
- Attach target group

**Step 4: Test Load Balancing**
- Refresh ALB DNS
- Responses alternate

**Step 5: Create Launch Template**
- AMI
- User-data script
- Instance type

**Step 6: Create Auto Scaling Group**
- Attach ALB
- Min: 2
- Desired: 2
- Max: 5
- Enable health checks

**Step 7: Test Auto Scaling**
- Stress CPU
- New instances launch
- Old unhealthy ones terminate

---

## 6️⃣ How AWS Achieves High Availability 🔥

AWS HA relies on:
- Multi-AZ design
- Managed ELB
- Health checks
- Auto scaling
- Stateless architecture

📌 **Golden rule:**

"State must live outside EC2."

---

## 7️⃣ Common Production Mistakes 🚨

❌ Single-AZ deployments  
❌ Stateful EC2 servers  
❌ Incorrect health check paths  
❌ No cooldown period  
❌ Hardcoding instance IPs

---

## 🎤 Senior Interview Questions & Answers

### Q1: ALB vs NLB — when to choose?

**Answer:**  
ALB for HTTP logic, NLB for ultra-low latency TCP.

### Q2: How does AWS handle instance failure?

**Answer:**  
Health checks detect failure → ASG replaces instance → ELB reroutes traffic.

### Q3: Can ALB route traffic to containers?

**Answer:**  
Yes (ECS, EKS, IP targets).

### Q4: How do you achieve zero-downtime deployments?

**Answer:**  
Rolling updates, health checks, multiple AZs.

---

## 🧠 System Design Scenario

### ❓ Design a scalable web application.

### ✅ Senior Answer
- ALB (public)
- ASG across AZs
- Stateless EC2
- RDS Multi-AZ
- S3 for assets

---

## ✅ DAY 6 – FINAL TAKEAWAYS

✔ You can design scalable AWS systems  
✔ You understand HA deeply  
✔ You can justify ALB vs NLB choices  
✔ You think like a system designer