# 🟡 DAY 6 – HANDS-ON REALTIME PROJECTS
## Load Balancer & Auto Scaling (ALB, NLB, ASG, HA) ⚖️📈

---

## 🔴 PROJECT 1: Highly Available Web Application (ALB + ASG)

### 📌 Business Scenario

A SaaS product needs:
- Zero downtime
- Ability to handle traffic spikes
- Automatic recovery from failures

### 🧠 WHY This Architecture?
- ALB distributes traffic
- ASG maintains capacity
- Multi-AZ removes single points of failure

**Senior insight:** HA ≠ more servers; HA = no single failure point.

---

### 🏗️ Architecture

```
Internet
   ↓
Application Load Balancer
   ↓
Auto Scaling Group
   ↓
EC2 (AZ-A, AZ-B)
```

---

### 🛠️ Step-by-Step Implementation

**Step 1: Create Launch Template**
- AMI: Amazon Linux
- Instance type: t3.micro
- User-data:

```bash
yum install nginx -y
echo "Hello from $(hostname)" > /usr/share/nginx/html/index.html
systemctl start nginx
```

**Step 2: Create Target Group**
- Target type: Instance
- Protocol: HTTP
- Health check path: `/`

**Step 3: Create Application Load Balancer**
- Internet-facing
- Public subnets (2 AZs)
- Listener: HTTP :80 → Target Group

**Step 4: Create Auto Scaling Group**
- Attach launch template
- Min: 2 | Desired: 2 | Max: 6
- Attach ALB
- Health checks: ELB + EC2

**Step 5: Test Load Balancing**
- Open ALB DNS
- Refresh page → different hostnames

**Step 6: Test Auto Scaling**
- Stress CPU on instance
- ASG launches new EC2 automatically
- Traffic spreads evenly

---

### ❌ Common Mistakes
- Single AZ ASG ❌
- Wrong health check path
- Hardcoded IPs
- Stateful EC2 servers

---

### 🎤 Interview Questions

**Q1: How does AWS replace a failed EC2?**  
✅ Health check fails → ASG terminates → new instance launched

**Q2: What happens if an AZ goes down?**  
✅ ALB routes traffic to healthy AZ

---

## 🔴 PROJECT 2: API Backend with Path-Based Routing (ALB)

### 📌 Business Scenario

Microservices architecture:
- `/users` → User service
- `/orders` → Order service

### 🧠 WHY ALB?
- Layer-7 routing
- No need for separate load balancers
- Clean microservices design

---

### 🏗️ Architecture

```
ALB
├── /users → ASG-1
└── /orders → ASG-2
```

---

### 🛠️ Implementation Steps

1. Create two target groups
2. Launch EC2 instances with different responses
3. Configure ALB listener rules:
   - `/users*` → Target Group 1
   - `/orders*` → Target Group 2
4. Test endpoints

---

### ❌ Common Mistakes
- Using NLB for HTTP routing
- Forgetting priority rules

---

### 🎤 Interview Questions

**Q1: Can NLB do path-based routing?**  
❌ No (Layer 4 only)

**Q2: Why not separate ALBs?**  
💰 Cost + complexity

---

## 🔴 PROJECT 3: High-Performance TCP Service (NLB)

### 📌 Business Scenario

A fintech app needs:
- Millions of connections
- Ultra-low latency
- Static IPs

### 🧠 WHY NLB?
- Layer-4 routing
- Static IP support
- Handles extreme throughput

---

### 🏗️ Architecture

```
Clients
  ↓
Network Load Balancer
  ↓
EC2 (TCP service)
```

---

### 🛠️ Implementation Steps

1. Launch EC2 with TCP service
2. Create target group (TCP)
3. Create NLB
4. Attach target group
5. Test latency

---

### ❌ Common Mistakes
- Using ALB for TCP workloads
- Expecting HTTP headers in NLB

---

### 🎤 Interview Questions

**Q1: Why is NLB faster than ALB?**  
✅ No HTTP processing

**Q2: Does NLB support SSL termination?**  
✅ Yes (TLS listeners)

---

## 🔴 PROJECT 4: Failover Testing (Chaos Engineering)

### 📌 Business Scenario

Test resilience under failure.

### 🛠️ Steps

1. Terminate EC2 manually
2. Observe:
   - ALB removes unhealthy target
   - ASG launches replacement
3. Kill instance in AZ-A
4. Traffic continues via AZ-B

---

### 🎤 Interview Questions

**Q: How do you test HA?**  
✅ Kill instances intentionally

---

## 🔥 SYSTEM DESIGN INTERVIEW SCENARIO

### ❓ Design a globally scalable web application.

### ✅ Senior Answer
- Route53 latency routing
- ALB per region
- ASG across AZs
- Stateless EC2
- S3 + CloudFront
- RDS Multi-AZ

---

## 🧠 FINAL INTERVIEW MASTER QUESTIONS

1. ALB vs NLB?
2. How does AWS achieve HA?
3. What triggers scaling?
4. How do health checks work?
5. How to avoid downtime during deploys?

---

## ✅ FINAL TAKEAWAY (INTERVIEW SIGNAL)

If you can:
- Explain traffic flow
- Trigger scaling
- Kill instances confidently
- Justify ALB vs NLB

👉 **You're thinking like a Senior Cloud Engineer.**