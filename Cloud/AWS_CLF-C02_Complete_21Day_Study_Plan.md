# 🎯 AWS Certified Cloud Practitioner (CLF-C02) - Complete 21-Day Study Plan

## 📋 Table of Contents
- [Exam Overview](#exam-overview)
- [Day 1: Cloud Computing Fundamentals](#day-1)
- [Day 2: AWS Global Infrastructure & EC2 Basics](#day-2)
- [Day 3: Compute Services Deep Dive](#day-3)
- [Day 4: Storage Services](#day-4)
- [Day 5: Database Services](#day-5)
- [Day 6: Networking & Content Delivery](#day-6)
- [Day 7: Security & Identity Services](#day-7)
- [Day 8: Monitoring, Logging & Management](#day-8)
- [Day 9: Serverless & Application Integration](#day-9)
- [Day 10: Migration & Transfer Services](#day-10)
- [Day 11: Machine Learning & AI Services](#day-11)
- [Day 12: AWS Pricing Models](#day-12)
- [Day 13: Billing, Cost Management & Support](#day-13)
- [Day 14: AWS Well-Architected Framework](#day-14)
- [Day 15: Cloud Security Best Practices](#day-15)
- [Day 16: Additional Services & Use Cases](#day-16)
- [Day 17: Practice Exam 1 & Review](#day-17)
- [Day 18: Practice Exam 2 & Weak Areas](#day-18)
- [Day 19: Domain-Focused Review](#day-19)
- [Day 20: Final Practice Exam](#day-20)
- [Day 21: Last-Minute Review & Exam Preparation](#day-21)

---

## Exam Overview {#exam-overview}

**AWS Certified Cloud Practitioner (CLF-C02)**

| Detail | Information |
|--------|-------------|
| **Questions** | 65 (50 scored + 15 unscored) |
| **Duration** | 90 minutes |
| **Passing Score** | 700/1000 (70%) |
| **Format** | Multiple choice + Multiple response |
| **Cost** | $100 USD |
| **Validity** | 3 years |

**Domain Breakdown:**
1. **Cloud Concepts** - 24%
2. **Security & Compliance** - 30%
3. **Cloud Technology & Services** - 34%
4. **Billing, Pricing & Support** - 12%

---

## 🗓️ Day 1: Cloud Computing Fundamentals {#day-1}

### Topics
- What is Cloud Computing
- Cloud Service Models (IaaS, PaaS, SaaS)
- Cloud Deployment Models (Public, Private, Hybrid)
- Benefits of Cloud Computing
- AWS Global Infrastructure Intro

### Key Concepts

**Six Advantages of Cloud Computing:**
1. Trade capital expense for variable expense
2. Benefit from massive economies of scale
3. Stop guessing capacity
4. Increase speed and agility
5. Stop spending money on data centers
6. Go global in minutes

**Service Models:**
- **IaaS**: Most control (EC2, VPC)
- **PaaS**: Platform ready (Elastic Beanstalk)
- **SaaS**: Ready to use (WorkMail, Chime)

**Deployment Models:**
- **Public Cloud**: AWS, Azure, GCP
- **Private Cloud**: On-premises cloud
- **Hybrid Cloud**: Mix of both

### Practice Questions

**Q1:** Which benefit allows paying only for resources consumed?
- A) Economies of scale
- B) Pay-as-you-go pricing ✅
- C) High availability
- D) Global reach

**Q2:** What is the deployment model when using both AWS and on-premises infrastructure?
- A) Public Cloud
- B) Private Cloud  
- C) Hybrid Cloud ✅
- D) Community Cloud

### Mini Project: Cloud Migration Decision

**Scenario:** Local bookstore wants online presence
- **On-premises**: $50,000 upfront + $2,000/month
- **AWS Cloud**: $0 upfront + $500/month + scales automatically

**Recommendation**: AWS Cloud
- No upfront investment
- Pay as you grow
- Global reach
- Auto-scaling during holiday sales

---

## 🗓️ Day 2: AWS Global Infrastructure & EC2 Basics {#day-2}

### Topics
- AWS Regions, Availability Zones, Edge Locations
- Choosing a Region (4 factors)
- Amazon EC2 Introduction
- EC2 Instance Types
- EC2 Pricing Models

### Key Concepts

**Infrastructure Hierarchy:**
- **Regions**: 30+ worldwide
- **Availability Zones**: 2-6 per Region
- **Edge Locations**: 400+ for CloudFront

**Region Selection Factors:**
1. **Compliance**: Data residency laws
2. **Latency**: Proximity to users
3. **Service Availability**: Not all services in all regions
4. **Pricing**: Costs vary by region

**EC2 Instance Types:**
| Type | Use Case | Example |
|------|----------|---------|
| **General Purpose (t3, m5)** | Balanced | Web servers |
| **Compute Optimized (c5)** | High CPU | Gaming, ML |
| **Memory Optimized (r5)** | High RAM | Databases |
| **Storage Optimized (i3)** | High I/O | Data warehouses |
| **Accelerated (p3, g4)** | GPU | AI/ML training |

**EC2 Pricing:**
- **On-Demand**: $$ - Pay per hour, no commitment
- **Reserved**: $ - 1-3 year, up to 75% off
- **Spot**: ¢ - Up to 90% off, can be interrupted
- **Savings Plans**: $ - Flexible commitment
- **Dedicated Hosts**: $$$ - Physical server

### Practice Questions

**Q1:** Each Region has at least how many AZs?
- A) 1
- B) 2 ✅
- C) 3
- D) 6

**Q2:** Which pricing model offers up to 90% discount but can be interrupted?
- A) Reserved
- B) On-Demand
- C) Spot ✅
- D) Savings Plan

**Q3:** For a database needing high RAM, which instance type?
- A) Compute Optimized
- B) Memory Optimized ✅
- C) General Purpose
- D) Storage Optimized

### Exam Tips
✅ **Memorize**: Regions have ≥2 AZs, AZs are isolated data centers
✅ **Spot Instances**: Can be terminated by AWS with 2-min warning
✅ **t2.micro**: Free Tier eligible (750 hrs/month for 12 months)

---

## 🗓️ Day 3: Compute Services Deep Dive {#day-3}

### Topics
- Amazon EC2 Auto Scaling
- Elastic Load Balancing (ALB, NLB)
- AWS Lambda
- Elastic Beanstalk
- Amazon Lightsail
- AWS Fargate

### Key Concepts

**Auto Scaling vs Load Balancing:**
- **Auto Scaling**: Adjusts number of instances
- **Load Balancing**: Distributes traffic across instances
- **Together**: High availability + performance

**Load Balancer Types:**
| Type | Layer | Use Case |
|------|-------|----------|
| **Application LB** | Layer 7 (HTTP/HTTPS) | Web apps, microservices |
| **Network LB** | Layer 4 (TCP/UDP) | Extreme performance |
| **Gateway LB** | Layer 3 | Third-party appliances |

**Lambda Limits (CRITICAL):**
- **Max execution**: 15 minutes
- **Max memory**: 10 GB
- **Pricing**: Per 100ms + memory

**When to use:**
- **Lambda**: Serverless, event-driven, <15 min
- **EC2**: Full control, long-running, any workload
- **Elastic Beanstalk**: Easy deployment, no infrastructure knowledge needed
- **Lightsail**: Simple websites, fixed pricing
- **Fargate**: Containers without servers

### Practice Questions

**Q1:** Which service automatically distributes traffic across EC2 instances?
- A) Auto Scaling
- B) Elastic Load Balancing ✅
- C) Lambda
- D) Route 53

**Q2:** Maximum Lambda execution time?
- A) 5 minutes
- B) 15 minutes ✅
- C) 1 hour
- D) 24 hours

**Q3:** Which load balancer for HTTP/HTTPS web applications?
- A) Network Load Balancer
- B) Application Load Balancer ✅
- C) Classic Load Balancer
- D) Gateway Load Balancer

### Exam Tips
✅ **Elastic Beanstalk is FREE** - you only pay for underlying resources
✅ **Lambda timeout**: 15 min (not 5, not 30, not 60)
✅ **Auto Scaling ≠ Load Balancing** (they complement each other)

---

## 🗓️ Day 4: Storage Services {#day-4}

### Topics
- Amazon S3 (Simple Storage Service)
- S3 Storage Classes
- Amazon EBS (Elastic Block Store)
- Amazon EFS (Elastic File System)
- AWS Snow Family
- AWS Storage Gateway

### Key Concepts

**S3 Storage Classes:**
| Class | Retrieval | Use Case | Cost |
|-------|-----------|----------|------|
| **S3 Standard** | Instant | Frequent access | $$ |
| **S3 Intelligent-Tiering** | Instant | Unknown patterns | $ (auto) |
| **S3 Standard-IA** | Instant | Infrequent access | $ |
| **S3 Glacier Instant** | Instant | Archive, quick retrieval | ¢ |
| **S3 Glacier Flexible** | 1-5min to 12hrs | Archive | ¢ |
| **S3 Glacier Deep Archive** | 12-48 hours | Long-term archive | ¢¢¢ |

**S3 Characteristics:**
- **Durability**: 99.999999999% (11 nines)
- **Availability**: 99.99% (Standard)
- **Max object size**: 5 TB
- **Bucket storage**: Unlimited

**EBS vs EFS vs S3:**
| Feature | EBS | EFS | S3 |
|---------|-----|-----|-----|
| **Type** | Block | File | Object |
| **Attach** | One EC2 (same AZ) | Multiple EC2 (multi-AZ) | Internet/API |
| **Size** | 1 GB - 16 TB | Auto-scales | Unlimited |
| **Use Case** | Boot volumes, databases | Shared storage | Backups, static websites |

**Snow Family:**
- **Snowcone**: 8 TB
- **Snowball Edge**: 80 TB
- **Snowmobile**: 100 PB (exabyte-scale)

### Practice Questions

**Q1:** Which S3 class is cheapest for long-term archive (7+ years)?
- A) S3 Standard
- B) S3 Glacier Flexible
- C) S3 Glacier Deep Archive ✅
- D) S3 Standard-IA

**Q2:** What is S3 durability?
- A) 99.99%
- B) 99.999999999% (11 nines) ✅
- C) 99.9%
- D) 100%

**Q3:** Which can be attached to multiple EC2 instances simultaneously?
- A) EBS
- B) EFS ✅
- C) S3 (as mounted drive)
- D) Instance Store

**Q4:** Maximum S3 object size?
- A) 5 GB
- B) 5 TB ✅
- C) 500 GB
- D) Unlimited

### Exam Tips
✅ **S3 is object storage** (NOT block or file system)
✅ **EBS = single EC2 in same AZ**, **EFS = multiple EC2 multi-AZ**
✅ **Snow Family = physical data transfer** (when internet is too slow)
✅ **11 nines = durability**, **99.99% = availability** (don't confuse!)

---

## 🗓️ Day 5: Database Services {#day-5}

### Topics
- Amazon RDS (Relational Database Service)
- Amazon Aurora
- Amazon DynamoDB
- Amazon Redshift
- Amazon ElastiCache
- Amazon DocumentDB, Neptune
- AWS Database Migration Service (DMS)

### Key Concepts

**RDS vs DynamoDB:**
| Feature | RDS | DynamoDB |
|---------|-----|----------|
| **Type** | Relational (SQL) | NoSQL (key-value, document) |
| **Schema** | Fixed | Flexible |
| **Scaling** | Vertical | Horizontal |
| **Queries** | Complex (JOINs) | Simple (key lookups) |
| **Latency** | ~100ms | <10ms |
| **Use Case** | Structured data, relationships | Massive scale, flexible schema |

**RDS Multi-AZ vs Read Replicas:**
| Feature | Multi-AZ | Read Replicas |
|---------|----------|---------------|
| **Purpose** | High Availability | Performance |
| **Replication** | Synchronous | Asynchronous |
| **Failover** | Automatic | Manual |
| **Read traffic** | No | Yes |

**Database Selection Guide:**
- **RDS**: Relational data, ACID transactions
- **Aurora**: High-performance relational (5x faster than MySQL)
- **DynamoDB**: NoSQL, millisecond latency, billions of items
- **Redshift**: Data warehouse, analytics, petabyte-scale
- **ElastiCache**: In-memory caching (Redis/Memcached)
- **DocumentDB**: MongoDB-compatible
- **Neptune**: Graph database (social networks)

### Practice Questions

**Q1:** Which database service is best for analytics on petabytes of data?
- A) RDS
- B) DynamoDB
- C) Redshift ✅
- D) ElastiCache

**Q2:** What does RDS Multi-AZ provide?
- A) Improved read performance
- B) High availability and automatic failover ✅
- C) Global replication
- D) In-memory caching

**Q3:** Which is a fully managed NoSQL database?
- A) RDS
- B) Aurora
- C) DynamoDB ✅
- D) Redshift

**Q4:** ElastiCache is used for:
- A) Long-term storage
- B) In-memory caching ✅
- C) Data warehousing
- D) Graph databases

### Exam Tips
✅ **Multi-AZ = High Availability**, **Read Replicas = Performance**
✅ **Redshift = OLAP** (analytics), **RDS = OLTP** (transactions)
✅ **Aurora = AWS-proprietary**, faster than standard RDS
✅ **DynamoDB = serverless**, auto-scales, millisecond latency

---

## 🗓️ Day 6: Networking & Content Delivery {#day-6}

### Topics
- Amazon VPC (Virtual Private Cloud)
- Subnets (Public vs Private)
- Internet Gateway, NAT Gateway
- Security Groups vs Network ACLs
- Amazon Route 53
- Amazon CloudFront
- AWS Direct Connect, VPN

### Key Concepts

**VPC Basics:**
- **Region-specific**: One VPC per region
- **CIDR block**: IP range (e.g., 10.0.0.0/16)
- **Subnets**: AZ-specific subdivisions
- **Default VPC**: Pre-configured, ready to use

**Public vs Private Subnet:**
- **Public**: Route to Internet Gateway (internet-accessible)
- **Private**: No direct internet (uses NAT for outbound)

**Security Groups vs NACLs:**
| Feature | Security Groups | Network ACLs |
|---------|-----------------|--------------|
| **Level** | Instance | Subnet |
| **Stateful** | Yes ✅ | No ❌ |
| **Rules** | Allow only | Allow + Deny |
| **Return traffic** | Auto-allowed | Must configure |
| **Default** | Deny inbound | Allow all |

**Route 53 Routing Policies:**
- **Simple**: One resource
- **Weighted**: Traffic split (A/B testing)
- **Latency**: Lowest latency
- **Failover**: Primary + secondary
- **Geolocation**: Based on user location
- **Geoproximity**: Based on resource location

**CloudFront vs S3:**
- **CloudFront**: CDN - caches content at edge locations
- **S3**: Origin storage
- **Together**: Fast global content delivery

**Direct Connect vs VPN:**
| Feature | Direct Connect | VPN |
|---------|----------------|-----|
| **Connection** | Dedicated fiber | Over internet |
| **Bandwidth** | 1-100 Gbps | Variable |
| **Latency** | Low, consistent | Variable |
| **Setup** | Weeks/months | Hours |
| **Cost** | High | Low |
| **Use Case** | Large data, mission-critical | Small data, backup |

### Practice Questions

**Q1:** Which allows instances in public subnet to access internet?
- A) NAT Gateway
- B) Internet Gateway ✅
- C) VPN Gateway
- D) VPC Endpoint

**Q2:** Security Groups are:
- A) Stateless
- B) Stateful ✅
- C) Apply at subnet level
- D) Support deny rules

**Q3:** Which service is a global Content Delivery Network?
- A) Route 53
- B) CloudFront ✅
- C) Direct Connect
- D) S3

**Q4:** NAT Gateway allows:
- A) Internet to reach private instances
- B) Private instances to access internet ✅
- C) VPC peering
- D) DNS resolution

### Exam Tips
✅ **Public subnet = IGW**, **Private subnet = NAT**
✅ **Security Groups = Stateful**, **NACLs = Stateless**
✅ **CloudFront = CDN** (caching), **Route 53 = DNS** (routing)
✅ **VPC is region-specific**, can't span multiple regions

---

## 🗓️ Day 7: Security & Identity Services {#day-7}

### Topics
- AWS Identity and Access Management (IAM)
- IAM Users, Groups, Roles, Policies
- IAM Best Practices
- AWS Organizations
- Amazon Cognito
- AWS IAM Identity Center (SSO)
- AWS Directory Service
- AWS Secrets Manager, Systems Manager Parameter Store

### Key Concepts

**IAM Basics:**
- **User**: Individual person/application
- **Group**: Collection of users
- **Role**: Temporary permissions (for services/users)
- **Policy**: JSON document defining permissions

**IAM Best Practices:**
1. ✅ **Root account**: Use only for initial setup, then lock it
2. ✅ **MFA**: Enable on root and privileged users
3. ✅ **Least Privilege**: Grant minimum permissions needed
4. ✅ **Use Roles**: For EC2, Lambda (not access keys)
5. ✅ **Rotate Credentials**: Change keys regularly
6. ✅ **Use Groups**: Assign permissions to groups, not individual users

**IAM Policy Example:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**AWS Organizations:**
- **Centralized management**: Multiple AWS accounts
- **Consolidated billing**: One bill for all accounts
- **Service Control Policies (SCPs)**: Restrict what accounts can do
- **Organizational Units (OUs)**: Group accounts (Dev, Prod, Finance)

**IAM vs AWS Organizations:**
- **IAM**: Manage users/permissions within ONE account
- **Organizations**: Manage MULTIPLE accounts

**Amazon Cognito:**
- **User authentication** for mobile/web apps
- **User pools**: Sign-up/sign-in
- **Identity pools**: Temporary AWS credentials
- **Social identity**: Login with Google, Facebook, etc.

**AWS Secrets Manager vs Parameter Store:**
| Feature | Secrets Manager | Parameter Store |
|---------|-----------------|-----------------|
| **Purpose** | Passwords, API keys | Configuration data |
| **Rotation** | Automatic ✅ | Manual |
| **Cost** | Paid | Free (standard), Paid (advanced) |
| **Encryption** | Always encrypted | Optional |

### Practice Questions

**Q1:** Which IAM entity should EC2 instances use to access AWS services?
- A) IAM User
- B) IAM Group
- C) IAM Role ✅
- D) Access Keys

**Q2:** What is the AWS best practice for root account?
- A) Use it for daily tasks
- B) Share credentials with team
- C) Lock it down with MFA and only use for account setup ✅
- D) Create multiple root accounts

**Q3:** Which service manages multiple AWS accounts centrally?
- A) IAM
- B) AWS Organizations ✅
- C) AWS Config
- D) AWS Directory Service

**Q4:** Cognito is used for:
- A) Server-side encryption
- B) User authentication in mobile/web apps ✅
- C) Network security
- D) Database access control

**Q5:** Which provides automatic secret rotation?
- A) Parameter Store
- B) Secrets Manager ✅
- C) IAM
- D) KMS

### Exam Tips
✅ **IAM is global** (not region-specific)
✅ **Root account = initial setup only**, then lock with MFA
✅ **Roles > Access Keys** (especially for EC2)
✅ **Policies are JSON documents** (Effect, Action, Resource)
✅ **AWS Organizations = multiple accounts**, **IAM = within one account**
✅ **MFA = Multi-Factor Authentication** (something you know + something you have)

### Security Services Quick Reference

**Identity & Access:**
- **IAM**: Users, groups, roles, policies
- **AWS Organizations**: Multi-account management
- **IAM Identity Center**: Single sign-on (SSO)
- **Cognito**: User authentication for apps
- **Directory Service**: Microsoft Active Directory

**Secret/Key Management:**
- **Secrets Manager**: Automatic rotation, passwords
- **Parameter Store**: Configuration data
- **KMS**: Encryption key management

**Compliance & Governance:**
- **AWS Config**: Resource inventory, compliance
- **CloudTrail**: API call auditing
- **AWS Artifact**: Compliance reports

---

## 🗓️ Day 8: Monitoring, Logging & Management {#day-8}

### Topics
- Amazon CloudWatch (Metrics, Logs, Alarms)
- AWS CloudTrail
- AWS Config
- AWS Trusted Advisor
- AWS Systems Manager
- AWS Personal Health Dashboard
- AWS Service Health Dashboard

### Key Concepts

**Amazon CloudWatch:**
- **Metrics**: Monitor AWS resources (CPU, disk, network)
- **Logs**: Collect and analyze log files
- **Alarms**: Trigger actions based on metrics
- **Dashboards**: Visualize metrics
- **Events**: Respond to state changes

**Default CloudWatch Metrics:**
- **EC2**: CPU, Disk, Network (NOT memory - requires CloudWatch Agent)
- **EBS**: Read/write operations
- **S3**: Request metrics, storage metrics
- **RDS**: Database connections, CPU

**CloudWatch vs CloudTrail:**
| Feature | CloudWatch | CloudTrail |
|---------|------------|------------|
| **Purpose** | Performance monitoring | Auditing (who did what) |
| **Data** | Metrics, logs, alarms | API calls |
| **Use Case** | "Is my app healthy?" | "Who deleted this S3 bucket?" |
| **Retention** | Custom | 90 days (default) |

**AWS Config:**
- **Track resource configurations** over time
- **Compliance checking**: Are resources configured correctly?
- **Change history**: Who changed what and when
- **Example**: Ensure all S3 buckets have encryption enabled

**AWS Trusted Advisor:**
Free automated recommendations in 5 categories:
1. **Cost Optimization**: Underutilized resources
2. **Performance**: Improve speed
3. **Security**: Security gaps (open ports, public S3 buckets)
4. **Fault Tolerance**: Increase availability
5. **Service Limits**: Approaching limits

**Free vs Business/Enterprise Support:**
- **Free/Basic**: 7 core checks
- **Business/Enterprise**: All checks (50+)

**AWS Systems Manager:**
- **Centralized management**: Manage EC2 at scale
- **Session Manager**: Secure shell access (no SSH keys needed)
- **Patch Manager**: Automated OS patching
- **Parameter Store**: Configuration and secrets
- **Run Command**: Execute commands across instances

**Health Dashboards:**
| Dashboard | Scope | Information |
|-----------|-------|-------------|
| **Service Health Dashboard** | Global | All AWS services status |
| **Personal Health Dashboard** | Your account | Issues affecting YOUR resources |

### Practice Questions

**Q1:** Which service monitors performance metrics and sets alarms?
- A) CloudTrail
- B) CloudWatch ✅
- C) Config
- D) Trusted Advisor

**Q2:** Which service records AWS API calls for auditing?
- A) CloudWatch
- B) CloudTrail ✅
- C) Config
- D) Systems Manager

**Q3:** What does AWS Trusted Advisor provide?
- A) Automated backups
- B) Best practice recommendations ✅
- C) Threat detection
- D) Network security

**Q4:** By default, CloudWatch monitors which EC2 metric?
- A) CPU ✅
- B) Memory
- C) Disk space
- D) Application logs

**Q5:** Which service helps ensure resources are configured according to compliance standards?
- A) CloudWatch
- B) CloudTrail
- C) AWS Config ✅
- D) Trusted Advisor

### Exam Tips
✅ **CloudWatch = Monitoring/Performance**, **CloudTrail = Auditing/Governance**
✅ **CloudWatch does NOT monitor memory by default** (need CloudWatch Agent)
✅ **Trusted Advisor = Best practices** (cost, security, performance, etc.)
✅ **Config = Configuration tracking and compliance**
✅ **Systems Manager = Operational management at scale**

### Monitoring Services Decision Tree

```
Need to know resource performance?
└─> CloudWatch (CPU, disk, network)

Need to know who made API calls?
└─> CloudTrail (audit trail)

Need to track resource configuration changes?
└─> AWS Config (compliance)

Need best practice recommendations?
└─> Trusted Advisor

Need to manage EC2 instances at scale?
└─> Systems Manager

Need to know if AWS services are down?
└─> Service Health Dashboard (global)
└─> Personal Health Dashboard (your resources)
```

---

## 🗓️ Day 9: Serverless & Application Integration {#day-9}

### Topics
- AWS Lambda (Deep Dive)
- Amazon API Gateway
- AWS Step Functions
- Amazon SQS (Simple Queue Service)
- Amazon SNS (Simple Notification Service)
- Amazon EventBridge
- AWS AppSync

### Key Concepts

**Serverless Architecture:**
Components that don't require managing servers:
- Lambda (compute)
- DynamoDB (database)
- S3 (storage)
- API Gateway (API management)
- EventBridge (event bus)

**AWS Lambda Details:**
- **Max execution**: 15 minutes
- **Max memory**: 10 GB
- **Supported languages**: Python, Node.js, Java, Go, .NET, Ruby, custom runtimes
- **Pricing**: $0.20 per 1M requests + compute time
- **Free Tier**: 1M requests/month + 400,000 GB-seconds

**Lambda Triggers:**
- S3 events (file upload)
- DynamoDB streams
- API Gateway (HTTP requests)
- EventBridge (scheduled events)
- SNS, SQS messages

**Amazon API Gateway:**
- **Create REST APIs and WebSocket APIs**
- **Fully managed** (auto-scaling)
- **Integrations**: Lambda, HTTP endpoints, AWS services
- **Features**: Authentication, throttling, caching, monitoring

**Amazon SQS (Queue):**
- **Message queue**: Decouple applications
- **Standard Queue**: At-least-once delivery, best effort ordering
- **FIFO Queue**: Exactly-once delivery, guaranteed ordering
- **Retention**: 1 min to 14 days (default: 4 days)
- **Use Case**: Asynchronous processing

**Amazon SNS (Pub/Sub):**
- **Publish-Subscribe**: One message → many subscribers
- **Subscribers**: Email, SMS, Lambda, SQS, HTTP endpoints
- **Use Case**: Notifications, fan-out messages

**SQS vs SNS:**
| Feature | SQS | SNS |
|---------|-----|-----|
| **Pattern** | Point-to-point (queue) | Pub-Sub (fan-out) |
| **Consumers** | Pull messages | Push messages |
| **Delivery** | One consumer processes | Many subscribers receive |
| **Use Case** | Job queue | Notifications |

**Amazon EventBridge:**
- **Event bus**: Route events between services
- **Sources**: AWS services, SaaS apps, custom apps
- **Targets**: Lambda, SQS, SNS, Step Functions
- **Scheduled events**: Cron-like scheduling

**AWS Step Functions:**
- **Orchestrate workflows**: Coordinate multiple Lambda functions
- **Visual workflow**: State machine
- **Error handling**: Retry, catch, fallback
- **Use Case**: Multi-step processes (order processing, data pipelines)

### Practice Questions

**Q1:** What is the maximum execution time for Lambda?
- A) 5 minutes
- B) 15 minutes ✅
- C) 1 hour
- D) 24 hours

**Q2:** Which service creates and manages REST APIs?
- A) Lambda
- B) API Gateway ✅
- C) EventBridge
- D) AppSync

**Q3:** SQS is best described as:
- A) Pub/Sub messaging
- B) Message queue ✅
- C) Event bus
- D) Workflow orchestration

**Q4:** SNS delivers messages using which pattern?
- A) Queue
- B) Publish-Subscribe ✅
- C) Point-to-point
- D) Request-response

**Q5:** Which service orchestrates multi-step workflows?
- A) Lambda
- B) SQS
- C) SNS
- D) Step Functions ✅

### Exam Tips
✅ **Lambda = Serverless compute** (15 min max, event-driven)
✅ **SQS = Queue** (one-to-one), **SNS = Pub/Sub** (one-to-many)
✅ **API Gateway = REST/WebSocket APIs**
✅ **EventBridge = Event routing** (AWS events, scheduled events)
✅ **Step Functions = Workflow orchestration**

### Application Integration Use Cases

**Use Case: Order Processing System**
```
User places order (API Gateway)
       ↓
Lambda validates order
       ↓
SQS queue (order processing)
       ↓
Lambda processes payment
       ↓
SNS notification (email confirmation to customer)
       ↓
Step Functions (coordinate fulfillment: inventory, shipping, etc.)
```

---

## 🗓️ Day 10: Migration & Transfer Services {#day-10}

### Topics
- AWS Migration Hub
- AWS Application Discovery Service
- AWS Database Migration Service (DMS)
- AWS Server Migration Service (SMS)
- AWS DataSync
- AWS Transfer Family
- AWS Snow Family (review)

### Key Concepts

**AWS Migration Hub:**
- **Central dashboard**: Track migrations from single location
- **Supports multiple tools**: DMS, SMS, CloudEndure
- **Progress tracking**: See status of all migrations

**AWS Application Discovery Service:**
- **Discover on-premises resources**: Servers, applications, dependencies
- **Plan migrations**: Understand what you have before migrating
- **Two types**:
  - **Agentless**: VMware environment discovery
  - **Agent-based**: Detailed server data

**AWS Database Migration Service (DMS):**
- **Migrate databases to AWS**: Minimal downtime
- **Homogeneous**: MySQL → RDS MySQL
- **Heterogeneous**: Oracle → Aurora PostgreSQL (+ Schema Conversion Tool)
- **Continuous replication**: Keep source and target in sync
- **Use Cases**: Migration, disaster recovery, database consolidation

**DMS Schema Conversion Tool (SCT):**
- **Convert database schemas**: Oracle → PostgreSQL
- **Required for heterogeneous migrations**
- **Analyzes compatibility**

**AWS Server Migration Service (SMS):**
- **Migrate on-premises servers** to EC2
- **Incremental replication**: Minimizes downtime
- **Automated**: Minimal manual intervention
- **Supports**: VMware, Hyper-V, Azure VMs

**AWS DataSync:**
- **Transfer data**: On-premises ↔ AWS (S3, EFS, FSx)
- **Automated**: Scheduled transfers
- **Fast**: Up to 10x faster than open-source tools
- **Use Cases**: Data migration, data replication, disaster recovery

**DataSync vs Snow Family:**
| Service | Connection | Speed | Use Case |
|---------|------------|-------|----------|
| **DataSync** | Network (Direct Connect/VPN) | Up to 10 Gbps | Ongoing sync, <10 TB |
| **Snow Family** | Physical device | Offline | One-time migration, >10 TB |

**AWS Transfer Family:**
- **SFTP, FTPS, FTP**: File transfers to/from S3 or EFS
- **Fully managed**: No servers to manage
- **Use Case**: Replace legacy FTP servers

### Practice Questions

**Q1:** Which service migrates databases with minimal downtime?
- A) Server Migration Service
- B) Database Migration Service ✅
- C) DataSync
- D) Snow Family

**Q2:** DataSync is used for:
- A) Database migration
- B) Server migration
- C) Data transfer between on-premises and AWS ✅
- D) Email migration

**Q3:** When migrating Oracle to PostgreSQL, what additional tool is needed with DMS?
- A) Migration Hub
- B) Schema Conversion Tool ✅
- C) Application Discovery
- D) DataSync

**Q4:** Which service discovers on-premises infrastructure before migration?
- A) Migration Hub
- B) Application Discovery Service ✅
- C) DMS
- D) SMS

**Q5:** Transfer Family supports which protocols?
- A) HTTP/HTTPS
- B) SFTP, FTPS, FTP ✅
- C) SMB, NFS
- D) iSCSI

### Exam Tips
✅ **DMS = Database migration** (minimal downtime)
✅ **SMS = Server migration** (on-prem VMs → EC2)
✅ **DataSync = Data transfer** (S3, EFS, FSx)
✅ **Snow Family = Physical data transfer** (>10 TB, no internet)
✅ **Schema Conversion Tool** required for heterogeneous DB migrations

### Migration Strategy (The 6 Rs)

1. **Rehost** (Lift and Shift): Move as-is (SMS)
2. **Replatform** (Lift, Tinker, Shift): Small optimizations (RDS instead of EC2)
3. **Repurchase**: Move to SaaS (Salesforce, Workday)
4. **Refactor**: Re-architect for cloud-native (containers, serverless)
5. **Retire**: Decommission unneeded systems
6. **Retain**: Keep on-premises (for now)

---

## 🗓️ Day 11: Machine Learning & AI Services {#day-11}

### Topics
- Amazon SageMaker
- Amazon Rekognition
- Amazon Polly
- Amazon Transcribe
- Amazon Translate
- Amazon Comprehend
- Amazon Lex
- Amazon Textract
- Amazon Forecast

### Key Concepts

**AWS AI/ML Services (No ML expertise needed):**

**Amazon Rekognition:**
- **Image and video analysis**
- **Features**: Object/scene detection, facial analysis, text in images, celebrity recognition
- **Use Cases**: Content moderation, face search, security

**Amazon Polly:**
- **Text-to-Speech (TTS)**
- **Multiple languages and voices**
- **Use Cases**: Audiobooks, voice announcements, accessibility

**Amazon Transcribe:**
- **Speech-to-Text**
- **Automatic speech recognition (ASR)**
- **Features**: Timestamps, speaker identification, custom vocabulary
- **Use Cases**: Meeting transcription, subtitles, call analytics

**Amazon Translate:**
- **Neural machine translation**
- **75+ languages**
- **Use Cases**: Localize content, real-time translation

**Amazon Comprehend:**
- **Natural Language Processing (NLP)**
- **Features**: Sentiment analysis, entity extraction, topic modeling
- **Use Cases**: Customer feedback analysis, document classification

**Amazon Lex:**
- **Build conversational interfaces** (chatbots)
- **Same tech as Amazon Alexa**
- **Features**: Voice and text, multi-turn conversations
- **Use Cases**: Customer service chatbots, virtual assistants

**Amazon Textract:**
- **Extract text and data from documents**
- **Goes beyond OCR**: Understands forms, tables
- **Use Cases**: Invoice processing, ID verification

**Amazon Forecast:**
- **Time-series forecasting** using ML
- **Use Cases**: Demand planning, resource planning, financial forecasting

**Amazon SageMaker:**
- **Build, train, deploy ML models** (for ML engineers)
- **Fully managed**: Infrastructure handled
- **Jupyter notebooks**: Development environment

### Service Categories

**Vision:**
- **Rekognition**: Image/video analysis

**Speech:**
- **Polly**: Text → Speech
- **Transcribe**: Speech → Text

**Language:**
- **Translate**: Language translation
- **Comprehend**: NLP/text analysis
- **Lex**: Chatbots

**Document:**
- **Textract**: Extract text/data from documents

**Forecasting:**
- **Forecast**: Time-series predictions

**ML Platform:**
- **SageMaker**: Build custom ML models

### Practice Questions

**Q1:** Which service converts text to speech?
- A) Transcribe
- B) Polly ✅
- C) Translate
- D) Lex

**Q2:** Amazon Rekognition is used for:
- A) Speech recognition
- B) Image and video analysis ✅
- C) Text translation
- D) Chatbots

**Q3:** Which service builds conversational chatbots?
- A) Polly
- B) Comprehend
- C) Lex ✅
- D) Transcribe

**Q4:** Amazon Textract is used to:
- A) Translate text
- B) Extract text from documents ✅
- C) Convert speech to text
- D) Analyze sentiment

**Q5:** Which service provides time-series forecasting?
- A) SageMaker
- B) Forecast ✅
- C) Comprehend
- D) Rekognition

### Exam Tips
✅ **Polly = Text to Speech**, **Transcribe = Speech to Text**
✅ **Rekognition = Image/video analysis** (faces, objects, text)
✅ **Lex = Chatbots** (same as Alexa)
✅ **Textract = Document data extraction** (beyond simple OCR)
✅ **SageMaker = For ML engineers** (others are "ready-to-use" AI services)

### Real-World Use Cases

**E-commerce:**
- **Rekognition**: Visual product search
- **Polly**: Voice shopping assistant
- **Forecast**: Demand prediction

**Customer Service:**
- **Lex**: Chatbot for common questions
- **Comprehend**: Analyze customer feedback sentiment
- **Transcribe**: Call transcription

**Document Processing:**
- **Textract**: Extract invoice data
- **Comprehend**: Classify documents
- **Translate**: Multi-language documents

---

## 🗓️ Day 12: AWS Pricing Models {#day-12}

### Topics
- AWS Pricing Principles
- Free Tier
- EC2 Pricing Models (detailed)
- S3 Pricing
- RDS Pricing
- Data Transfer Costs
- TCO Calculator
- AWS Pricing Calculator

### Key Concepts

**AWS Pricing Principles:**
1. **Pay-as-you-go**: No upfront commitment
2. **Pay less when you reserve**: Reserved capacity discounts
3. **Pay less with more usage**: Volume discounts
4. **Pay even less as AWS grows**: Economies of scale passed to customers

**AWS Free Tier:**
Three types:
1. **Always Free**: Lambda (1M requests/month), DynamoDB (25 GB)
2. **12 Months Free**: EC2 t2.micro (750 hrs/month), S3 (5 GB), RDS (750 hrs/month)
3. **Trials**: SageMaker (2 months), Redshift (2 months)

**EC2 Pricing Breakdown:**
```
On-Demand: $0.0416/hour (t3.medium)
Reserved (1-year): $0.0249/hour (40% savings)
Reserved (3-year): $0.0167/hour (60% savings)
Spot: $0.0125/hour (70% savings, can be interrupted)
```

**Savings Plans vs Reserved Instances:**
| Feature | Savings Plans | Reserved Instances |
|---------|---------------|-------------------|
| **Flexibility** | Any instance type, region, OS | Specific instance type |
| **Commitment** | $/hour for 1-3 years | Capacity reservation |
| **Discount** | Up to 72% | Up to 75% |
| **Use Case** | Dynamic workloads | Predictable workloads |

**S3 Pricing Components:**
1. **Storage**: Per GB/month (varies by class)
2. **Requests**: GET, PUT, COPY, etc.
3. **Data Transfer**: OUT of S3 (IN is free)
4. **Management**: S3 Inventory, Analytics

**Example S3 Costs:**
- Storage (Standard): $0.023/GB/month
- GET requests: $0.0004 per 1,000
- PUT requests: $0.005 per 1,000
- Data transfer OUT: $0.09/GB (first 10 TB)

**Data Transfer Costs:**
✅ **Free:**
- Inbound to AWS (from internet)
- Between services in same region
- S3 to CloudFront
- CloudFront to internet

💰 **Paid:**
- Outbound from AWS to internet
- Between regions
- Between AZs (small charge)

**RDS Pricing:**
1. **Instance hours**: db.t3.micro = $0.017/hour
2. **Storage**: $0.115/GB/month (gp2)
3. **Backup storage**: Free up to DB size, then $0.095/GB/month
4. **Data transfer**: OUT of RDS

### Practice Questions

**Q1:** Which EC2 pricing model provides up to 75% discount with 1-3 year commitment?
- A) On-Demand
- B) Spot
- C) Reserved Instances ✅
- D) Dedicated Hosts

**Q2:** AWS Free Tier EC2 includes how many hours per month?
- A) 500
- B) 750 ✅
- C) 1000
- D) Unlimited

**Q3:** Which data transfer is FREE?
- A) From EC2 to internet
- B) From S3 to CloudFront ✅
- C) Between AWS regions
- D) From AWS to on-premises

**Q4:** Savings Plans provide discounts for commitment to:
- A) Specific instance type
- B) $/hour usage for 1-3 years ✅
- C) Number of instances
- D) Specific region

**Q5:** What is always free with AWS Free Tier Lambda?
- A) 500,000 requests/month
- B) 1 million requests/month ✅
- C) Unlimited requests
- D) 100,000 requests/month

### Exam Tips
✅ **Data transfer IN is always free**
✅ **Data transfer OUT costs money** (except S3 → CloudFront)
✅ **Reserved Instances = 1-3 year commitment = up to 75% savings**
✅ **Spot Instances = up to 90% savings** but can be interrupted
✅ **Free Tier: 750 hours EC2 t2.micro/month for 12 months**

### Cost Optimization Strategies

1. **Right-sizing**: Don't over-provision (use t3.medium, not t3.2xlarge)
2. **Reserved Instances/Savings Plans**: For predictable workloads
3. **Spot Instances**: For flexible, fault-tolerant workloads
4. **S3 Lifecycle Policies**: Move old data to cheaper storage classes
5. **Auto Scaling**: Scale down when not needed
6. **Use CloudFront**: Reduce data transfer costs

---

## 🗓️ Day 13: Billing, Cost Management & Support {#day-13}

### Topics
- AWS Billing Dashboard
- AWS Cost Explorer
- AWS Budgets
- AWS Cost and Usage Reports
- AWS Cost Allocation Tags
- AWS Support Plans
- AWS Trusted Advisor (Billing focus)
- Consolidated Billing

### Key Concepts

**AWS Billing Dashboard:**
- **View current and forecasted costs**
- **Month-to-date spending**
- **Free Tier usage**

**AWS Cost Explorer:**
- **Visualize and analyze costs**
- **Filter by service, region, tag**
- **Forecast future costs** (up to 12 months)
- **Historical data**: Up to 12 months
- **Use Cases**: Identify cost drivers, spot trends

**AWS Budgets:**
- **Set custom budgets** (cost, usage, reservation)
- **Alerts**: Email/SNS when threshold exceeded
- **Types**:
  - Cost budgets
  - Usage budgets
  - Reservation budgets
  - Savings Plans budgets
- **Free**: First 2 budgets, then $0.02/day per budget

**AWS Cost and Usage Reports (CUR):**
- **Most detailed cost data**
- **Delivered to S3**
- **Hourly, daily, monthly granularity**
- **Analyze with Athena, QuickSight, or third-party tools**

**Cost Allocation Tags:**
- **Track costs** by project, department, environment
- **Types**:
  - **AWS-generated**: Automatically applied (e.g., aws:createdBy)
  - **User-defined**: Custom tags (e.g., Project:WebApp)
- **Activate tags** in Billing Dashboard to use in reports

**Consolidated Billing (AWS Organizations):**
- **One bill** for multiple accounts
- **Volume discounts**: Combined usage
- **Free**: No extra charge
- **Benefits**: Centralized payment, easier tracking

**AWS Support Plans:**

| Plan | Cost | Response Times | Features |
|------|------|----------------|----------|
| **Basic** | Free | No technical support | Billing support, forums, 7 Trusted Advisor checks |
| **Developer** | $29/month | 12-24 hours (business hours) | Email support, 7 TA checks, 1 primary contact |
| **Business** | $100/month | 1 hour (urgent), 4 hours (general) | Phone/chat support, all TA checks, unlimited contacts, infrastructure event mgmt |
| **Enterprise** | $15,000/month | 15 min (critical), 1 hour (urgent) | TAM (Technical Account Manager), Concierge Support, all Business features |

**Response Times (Business vs Enterprise):**
| Severity | Business | Enterprise |
|----------|----------|------------|
| **Critical** | 1 hour | 15 minutes |
| **Urgent** | 4 hours | 1 hour |
| **General** | 12 hours | 4 hours |

**Trusted Advisor (Support Plan Access):**
- **Basic/Developer**: 7 core checks (S3 bucket permissions, Security groups)
- **Business/Enterprise**: All checks (50+) in 5 categories

### Practice Questions

**Q1:** Which tool visualizes and forecasts AWS costs?
- A) Cost and Usage Reports
- B) Cost Explorer ✅
- C) Budgets
- D) Billing Dashboard

**Q2:** Which Support plan includes Technical Account Manager (TAM)?
- A) Basic
- B) Developer
- C) Business
- D) Enterprise ✅

**Q3:** AWS Budgets can alert when:
- A) A new service is launched
- B) Costs exceed a threshold ✅
- C) A resource is deleted
- D) An AZ fails

**Q4:** Consolidated Billing provides:
- A) Technical support
- B) One bill for multiple AWS accounts ✅
- C) Free tier extensions
- D) Automatic cost optimization

**Q5:** Which Support plan has 1-hour response for urgent issues?
- A) Basic
- B) Developer
- C) Business ✅
- D) Free

**Q6:** Cost Allocation Tags are used to:
- A) Reduce costs
- B) Track costs by category (project, dept, etc.) ✅
- C) Encrypt data
- D) Improve performance

### Exam Tips
✅ **Cost Explorer = Visualize and forecast costs**
✅ **Budgets = Set alerts** when costs exceed thresholds
✅ **Consolidated Billing = One bill for multiple accounts** (volume discounts)
✅ **Enterprise Support = TAM + 15 min critical response**
✅ **Business Support = Full Trusted Advisor + 1 hour urgent response**
✅ **Basic Support = Free, no technical support**, 7 TA checks

### Cost Management Best Practices

1. **Set up Budgets**: Alert before overspending
2. **Use Cost Allocation Tags**: Track costs by project/team
3. **Review Cost Explorer monthly**: Identify trends
4. **Enable Cost and Usage Reports**: Detailed analysis
5. **Leverage Consolidated Billing**: Volume discounts
6. **Use Trusted Advisor**: Cost optimization recommendations

---

## 🗓️ Day 14: AWS Well-Architected Framework {#day-14}

### Topics
- Well-Architected Framework Overview
- 6 Pillars
- AWS Well-Architected Tool
- Design Principles

### Key Concepts

**AWS Well-Architected Framework:**
Best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud.

**6 Pillars:**

### 1. Operational Excellence
**Design Principles:**
- Perform operations as code (IaC)
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure
- Learn from operational failures

**Key Services:**
- CloudFormation (Infrastructure as Code)
- CodeDeploy (Deployment automation)
- CloudWatch (Monitoring)
- Systems Manager (Operations)

### 2. Security
**Design Principles:**
- Implement strong identity foundation (IAM)
- Enable traceability (CloudTrail, Config)
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data (use roles, not root)
- Prepare for security events

**Key Services:**
- IAM (Identity)
- KMS (Encryption)
- CloudTrail (Audit)
- GuardDuty (Threat detection)
- WAF (Web application firewall)

### 3. Reliability
**Design Principles:**
- Automatically recover from failure
- Test recovery procedures
- Scale horizontally
- Stop guessing capacity (Auto Scaling)
- Manage change through automation

**Key Services:**
- Auto Scaling
- Multi-AZ deployments
- Route 53 (DNS failover)
- Backup
- CloudFormation

**Reliability Metrics:**
- **MTBF (Mean Time Between Failures)**: How long until failure
- **MTTR (Mean Time To Repair)**: How long to recover
- **RTO (Recovery Time Objective)**: Max downtime
- **RPO (Recovery Point Objective)**: Max data loss

### 4. Performance Efficiency
**Design Principles:**
- Democratize advanced technologies (use managed services)
- Go global in minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy (choose right tool)

**Key Services:**
- Lambda (Serverless)
- Auto Scaling
- CloudFront (CDN)
- ElastiCache (Caching)

### 5. Cost Optimization
**Design Principles:**
- Implement cloud financial management
- Adopt consumption model (pay for what you use)
- Measure overall efficiency
- Stop spending on undifferentiated heavy lifting
- Analyze and attribute expenditure

**Key Services:**
- Cost Explorer
- Budgets
- Trusted Advisor
- Reserved Instances/Savings Plans
- Auto Scaling (scale down when not needed)

### 6. Sustainability
**Design Principles:**
- Understand your impact
- Establish sustainability goals
- Maximize utilization (right-size resources)
- Anticipate and adopt more efficient offerings
- Use managed services
- Reduce downstream impact

**Key Services:**
- Auto Scaling (reduce unused capacity)
- Serverless (Lambda - no idle resources)
- Graviton processors (more efficient)

### Trade-offs Between Pillars

**Example 1: Speed vs Cost**
- **Performance**: Use larger instances, more replicas
- **Cost**: Use smaller instances, fewer replicas
- **Balance**: Auto Scaling, right-sizing

**Example 2: Security vs Operational Excellence**
- **Security**: Manual approval for changes
- **Operational Excellence**: Automated deployments
- **Balance**: Automated security checks, auditing

### AWS Well-Architected Tool
- **Free service**: Review workloads against best practices
- **Generates reports**: Identifies high and medium risks
- **Improvement plans**: Step-by-step recommendations

### Practice Questions

**Q1:** Which Well-Architected pillar focuses on recovering from failures?
- A) Operational Excellence
- B) Reliability ✅
- C) Performance Efficiency
- D) Security

**Q2:** "Implement strong identity foundation" is a design principle of which pillar?
- A) Operational Excellence
- B) Security ✅
- C) Reliability
- D) Cost Optimization

**Q3:** Which pillar emphasizes using serverless and managed services?
- A) Security
- B) Performance Efficiency ✅
- C) Reliability
- D) Operational Excellence

**Q4:** "Stop guessing capacity" is a principle of which pillar?
- A) Cost Optimization
- B) Reliability ✅
- C) Security
- D) Sustainability

**Q5:** The AWS Well-Architected Tool is used to:
- A) Deploy applications
- B) Review workloads against best practices ✅
- C) Monitor costs
- D) Manage IAM users

### Exam Tips
✅ **6 Pillars**: Operational Excellence, Security, Reliability, Performance, Cost, Sustainability
✅ **Reliability = Auto Scaling, Multi-AZ, backup**
✅ **Cost Optimization = Right-sizing, Reserved Instances, Auto Scaling down**
✅ **Performance = Serverless, managed services, global deployment**
✅ **Security = IAM, encryption, least privilege**
✅ **Well-Architected Tool = Free review against best practices**

---

## 🗓️ Day 15: Cloud Security Best Practices {#day-15}

### Topics
- Shared Responsibility Model
- AWS Shield, AWS WAF
- Amazon GuardDuty
- Amazon Inspector
- AWS Key Management Service (KMS)
- AWS Certificate Manager (ACM)
- AWS Security Hub
- Amazon Macie
- Compliance Programs

### Key Concepts

**Shared Responsibility Model:**

**AWS Responsibility: "Security OF the Cloud"**
- Physical infrastructure
- Hardware, software, networking
- Global infrastructure (Regions, AZs)
- Managed services (RDS, Lambda)

**Customer Responsibility: "Security IN the Cloud"**
- Customer data
- Platform, applications
- IAM (users, groups, roles)
- OS, network, firewall configuration
- Encryption (data at rest, in transit)
- Network traffic protection

**Memory Aid:**
- **AWS**: Hardware, global infrastructure
- **Customer**: Data, access control, encryption

**Service-Specific Responsibilities:**

| Service | AWS Manages | Customer Manages |
|---------|-------------|------------------|
| **S3** | Infrastructure, durability | Bucket policies, encryption, versioning |
| **EC2** | Hardware, hypervisor | OS, patches, security groups, applications |
| **RDS** | Hardware, DB engine patches | Database configuration, backups, encryption |
| **Lambda** | Everything except code | Function code, IAM permissions |

### Security Services

**AWS Shield:**
- **DDoS protection**
- **Two tiers**:
  - **Shield Standard**: Free, automatic, protects all AWS customers
  - **Shield Advanced**: $3,000/month, 24/7 DDoS response team, cost protection
- **Protected resources**: CloudFront, Route 53, ALB, Global Accelerator

**AWS WAF (Web Application Firewall):**
- **Protect web applications** from common exploits
- **Filter HTTP/HTTPS requests** based on rules
- **Rules**: IP addresses, HTTP headers, body, URI strings
- **Common attacks**: SQL injection, cross-site scripting (XSS)
- **Integration**: CloudFront, ALB, API Gateway, AppSync

**Amazon GuardDuty:**
- **Intelligent threat detection**
- **Continuous monitoring**: CloudTrail, VPC Flow Logs, DNS logs
- **Machine learning**: Detect anomalies
- **Threats**: Cryptocurrency mining, unauthorized access, data exfiltration
- **Alerts**: SNS, EventBridge
- **30-day free trial**

**Amazon Inspector:**
- **Automated security assessment** for EC2 and container images
- **Scans for**:
  - Vulnerabilities in software
  - Network accessibility
  - Best practice deviations
- **Reports**: Prioritized findings

**Amazon Macie:**
- **Data security and privacy**
- **Uses ML** to discover and protect sensitive data in S3
- **Identifies**: PII (personally identifiable information), financial data
- **Alerts**: Unusual data access patterns

**AWS Security Hub:**
- **Central security dashboard**
- **Aggregates findings** from GuardDuty, Inspector, Macie, etc.
- **Compliance checks**: CIS, PCI-DSS
- **Automated remediation**: Integrates with EventBridge

**AWS Key Management Service (KMS):**
- **Create and manage encryption keys**
- **Integrated**: S3, EBS, RDS, etc.
- **Audit**: CloudTrail logs all key usage
- **Customer Managed Keys (CMK)**: You control key rotation
- **AWS Managed Keys**: Automatic rotation

**AWS Certificate Manager (ACM):**
- **Provision SSL/TLS certificates** for free
- **Automatic renewal**: No expiration hassles
- **Integration**: CloudFront, ALB, API Gateway
- **Use Case**: HTTPS on websites

### Compliance Programs

AWS complies with many standards:
- **HIPAA**: Healthcare
- **PCI-DSS**: Payment cards
- **SOC**: Auditing standards
- **GDPR**: EU data privacy
- **ISO 27001**: Information security

**AWS Artifact:**
- **Access compliance reports** and agreements
- **Free service**
- **Download**: SOC reports, PCI reports, certifications

**AWS Audit Manager:**
- **Automate evidence collection** for compliance audits
- **Pre-built frameworks**: HIPAA, GDPR, SOC 2

### Practice Questions

**Q1:** In the Shared Responsibility Model, who is responsible for patching the OS on EC2?
- A) AWS
- B) Customer ✅
- C) Both
- D) Third-party vendor

**Q2:** Which service protects against DDoS attacks?
- A) WAF
- B) Shield ✅
- C) GuardDuty
- D) Inspector

**Q3:** GuardDuty detects threats using:
- A) Manual reviews
- B) Machine learning and threat intelligence ✅
- C) Penetration testing
- D) Firewall rules

**Q4:** Which service discovers sensitive data like PII in S3?
- A) GuardDuty
- B) Inspector
- C) Macie ✅
- D) Security Hub

**Q5:** AWS Artifact provides access to:
- A) IAM policies
- B) Compliance reports ✅
- C) Encryption keys
- D) Security groups

**Q6:** Who is responsible for RDS database engine patches?
- A) AWS ✅
- B) Customer
- C) Third-party
- D) Shared

### Exam Tips
✅ **Shared Responsibility**: AWS = infrastructure, Customer = data & access
✅ **Shield = DDoS protection** (Standard free, Advanced paid)
✅ **WAF = Web application firewall** (SQL injection, XSS)
✅ **GuardDuty = Threat detection** using ML
✅ **Macie = Find sensitive data in S3**
✅ **Inspector = Automated vulnerability scanning (EC2)**
✅ **Security Hub = Central dashboard** for all security findings
✅ **KMS = Encryption key management**
✅ **ACM = Free SSL/TLS certificates**

### Security Best Practices Summary

1. **Enable MFA** on root and privileged accounts
2. **Use IAM roles** instead of access keys for EC2
3. **Encrypt data** at rest (KMS) and in transit (HTTPS/ACM)
4. **Enable CloudTrail** for audit logging
5. **Use GuardDuty** for threat detection
6. **Scan with Inspector** for vulnerabilities
7. **Protect web apps** with WAF
8. **Enable Shield Standard** (it's free!)
9. **Classify data** with Macie
10. **Centralize security** with Security Hub

---

## 🗓️ Day 16: Additional Services & Use Cases {#day-16}

### Topics
- AWS Outposts
- AWS Wavelength
- AWS Local Zones
- Amazon WorkSpaces
- Amazon AppStream 2.0
- AWS IoT Core
- Amazon Elastic Transcoder / AWS Elemental MediaConvert
- AWS Glue
- Amazon Athena
- Amazon QuickSight

### Key Concepts

**Hybrid Cloud / Edge Services:**

**AWS Outposts:**
- **AWS infrastructure on-premises**
- **Same APIs, tools, hardware** as AWS cloud
- **Use Cases**: Low latency, data residency, hybrid cloud
- **AWS maintains**: Hardware, software updates
- **Sizes**: 42U rack or 1U/2U servers

**AWS Wavelength:**
- **5G edge computing**
- **Deploy apps** at telecom provider edge
- **Ultra-low latency** (<10ms)
- **Use Cases**: AR/VR, real-time gaming, autonomous vehicles

**AWS Local Zones:**
- **Extension of AWS Region** closer to users
- **Single-digit millisecond latency**
- **Use Cases**: Media, gaming, real-time applications
- **Example**: Los Angeles Local Zone (part of us-west-2)

### End User Computing

**Amazon WorkSpaces:**
- **Managed Desktop-as-a-Service (DaaS)**
- **Virtual desktops** in the cloud
- **Windows or Linux**
- **Use Cases**: Remote work, contractor access, BYOD
- **Pricing**: Monthly or hourly

**Amazon AppStream 2.0:**
- **Application streaming**
- **Stream desktop apps** to browsers
- **No app installation** on user devices
- **Use Cases**: Software trials, temporary access, BYOD

**WorkSpaces vs AppStream:**
| Feature | WorkSpaces | AppStream 2.0 |
|---------|------------|---------------|
| **Provides** | Full desktop | Specific applications |
| **Persistent** | Yes | No (sessions) |
| **Use Case** | Full-time remote work | Application access |

### IoT & Media Services

**AWS IoT Core:**
- **Connect IoT devices** to AWS
- **Device management**: Millions of devices
- **Message broker**: MQTT, HTTPS
- **Use Cases**: Smart home, industrial IoT, connected vehicles

**Amazon Elastic Transcoder / AWS Elemental MediaConvert:**
- **Video transcoding** (convert formats)
- **Elastic Transcoder**: Older, simpler
- **MediaConvert**: Newer, more features
- **Use Cases**: Streaming video platforms, video on demand

### Analytics Services

**AWS Glue:**
- **ETL service** (Extract, Transform, Load)
- **Serverless**: No infrastructure
- **Data Catalog**: Centralized metadata repository
- **Use Cases**: Prepare data for analytics (move to Redshift, Athena)

**Amazon Athena:**
- **Query S3 data using SQL**
- **Serverless**: No infrastructure
- **Pay per query**: Scan TB data
- **Use Cases**: Log analysis, ad-hoc queries
- **Integration**: Glue Data Catalog, QuickSight

**Amazon QuickSight:**
- **Business Intelligence (BI) tool**
- **Create dashboards and visualizations**
- **Serverless**: Auto-scales
- **ML-powered insights**
- **Use Cases**: Reports, KPI dashboards, data visualization

### Workflow & Orchestration

**AWS Batch:**
- **Run batch computing jobs**
- **Managed compute**: Provisions optimal compute
- **Use Cases**: Genomics, financial risk, drug discovery

**Amazon Managed Workflows for Apache Airflow (MWAA):**
- **Orchestrate workflows**
- **Managed Apache Airflow**
- **Use Cases**: Data pipelines, ML workflows

### Practice Questions

**Q1:** Which service provides virtual desktops in the cloud?
- A) AppStream 2.0
- B) WorkSpaces ✅
- C) Lightsail
- D) WorkLink

**Q2:** AWS Glue is used for:
- A) Monitoring
- B) ETL (Extract, Transform, Load) ✅
- C) Streaming video
- D) IoT device management

**Q3:** Athena allows you to:
- A) Create databases
- B) Query S3 data using SQL ✅
- C) Stream videos
- D) Deploy applications

**Q4:** Which service connects millions of IoT devices?
- A) WorkSpaces
- B) IoT Core ✅
- C) AppStream
- D) Wavelength

**Q5:** QuickSight is used for:
- A) Video transcoding
- B) Business intelligence and dashboards ✅
- C) Application streaming
- D) IoT management

**Q6:** AWS Outposts provides:
- A) Edge computing for 5G
- B) AWS infrastructure on-premises ✅
- C) Virtual desktops
- D) SQL queries on S3

### Exam Tips
✅ **Outposts = AWS infrastructure on-premises**
✅ **Wavelength = 5G ultra-low latency edge**
✅ **WorkSpaces = Virtual desktops** (DaaS)
✅ **AppStream 2.0 = Application streaming**
✅ **Glue = ETL**, **Athena = SQL on S3**, **QuickSight = BI dashboards**
✅ **IoT Core = Connect IoT devices**

---

## 🗓️ Day 17: Practice Exam 1 & Review {#day-17}

### Today's Focus
- Take full-length practice exam (65 questions, 90 minutes)
- Review answers carefully
- Identify weak domains
- Create focused study plan for weak areas

### Practice Exam Domains

**Domain 1: Cloud Concepts (15-16 questions)**
**Domain 2: Security & Compliance (19-20 questions)**
**Domain 3: Cloud Technology & Services (22-23 questions)**
**Domain 4: Billing & Support (8-9 questions)**

### Sample Questions (Full exam in separate practice test files)

**Q1:** A company wants to run applications in AWS but maintain some data on-premises due to regulations. What deployment model is this?
- A) Public Cloud
- B) Private Cloud
- C) Hybrid Cloud ✅
- D) Community Cloud

**Q2:** Which EC2 pricing model provides up to 90% discount but instances can be interrupted?
- A) On-Demand
- B) Reserved
- C) Spot ✅
- D) Dedicated

**Q3:** What is the AWS responsibility in the Shared Responsibility Model?
- A) Customer data
- B) Application code
- C) Physical infrastructure ✅
- D) IAM users and permissions

**Q4:** Which service automatically distributes incoming application traffic across multiple targets?
- A) Auto Scaling
- B) Elastic Load Balancing ✅
- C) CloudFront
- D) Route 53

**Q5:** Amazon S3 durability is:
- A) 99.9%
- B) 99.99%
- C) 99.999999999% ✅
- D) 100%

### After Practice Exam: Analysis Template

**Score by Domain:**
```
Domain 1 (Cloud Concepts): ___/16 = ___%
Domain 2 (Security): ___/20 = ___%
Domain 3 (Technology): ___/23 = ___%
Domain 4 (Billing): ___/9 = ___%

Total: ___/65 = ___%
Passing Score: 45/65 (70%)
```

**Weak Areas Identified:**
1. ____________________________
2. ____________________________
3. ____________________________

**Review Priority:**
- [ ] Re-read weak domain notes
- [ ] Watch videos on confusing topics
- [ ] Practice questions for weak areas
- [ ] Hands-on labs for services you're unsure about

### Common Mistakes to Avoid

1. **Not reading questions carefully**: Keywords matter!
2. **Confusing similar services**: EC2 vs Lambda, RDS vs DynamoDB
3. **Forgetting Shared Responsibility**: Who manages what?
4. **Mixing up pricing models**: Reserved vs Spot vs On-Demand
5. **Not knowing AWS limitations**: Lambda 15 min, S3 object 5 TB

### Key Topics to Review Tonight

**If scored <70% in Domain 1:**
- Cloud benefits (6 advantages)
- Service models (IaaS, PaaS, SaaS)
- Deployment models
- Global infrastructure

**If scored <70% in Domain 2:**
- IAM (users, groups, roles, policies)
- Shared Responsibility Model
- Security services (Shield, WAF, GuardDuty)
- Encryption (KMS, ACM)

**If scored <70% in Domain 3:**
- Compute (EC2, Lambda, Beanstalk)
- Storage (S3, EBS, EFS)
- Databases (RDS, DynamoDB, Redshift)
- Networking (VPC, Route 53, CloudFront)

**If scored <70% in Domain 4:**
- Pricing models
- Support plans
- Cost management tools
- Billing and cost optimization

---

## 🗓️ Day 18: Practice Exam 2 & Weak Areas {#day-18}

### Today's Focus
- Take second full-length practice exam
- Compare scores with Exam 1
- Deep dive into persistent weak areas
- Hands-on review of confusing services

### Score Comparison

```
             Exam 1   Exam 2   Change
Domain 1:    ___      ___      ___
Domain 2:    ___      ___      ___
Domain 3:    ___      ___      ___
Domain 4:    ___      ___      ___
Total:       ___      ___      ___
```

### Weak Area Deep Dive Exercises

**If still struggling with Compute:**

**Exercise:** Compare services in a table:

| Scenario | Use This | Why? |
|----------|----------|------|
| Event-driven, <15 min | Lambda | Serverless, auto-scale |
| Long-running web server | EC2 | Full control, any duration |
| Deploy app without infrastructure knowledge | Elastic Beanstalk | Platform managed |
| Simple website, fixed price | Lightsail | Simplified, predictable cost |
| Containers without servers | Fargate | Serverless containers |

**If still struggling with Storage:**

**Exercise:** Decision tree:

```
Need storage for what?
├─ Objects/files (images, videos, backups) → S3
├─ EC2 boot volume → EBS
├─ Shared file system (multiple EC2) → EFS
└─ Transfer 100 TB to AWS physically → Snowball
```

**If still struggling with Databases:**

```
What type of data?
├─ Relational (tables, SQL)
│   ├─ Standard engines (MySQL, PostgreSQL) → RDS
│   └─ Need 5x performance → Aurora
├─ NoSQL (key-value, document)
│   └─ Massive scale, millisecond latency → DynamoDB
├─ Data warehouse (analytics)
│   └─ Petabyte-scale queries → Redshift
└─ Caching (in-memory)
    └─ Speed up database → ElastiCache
```

**If still struggling with Security:**

**Shared Responsibility Chart:**

| Component | AWS | Customer |
|-----------|-----|----------|
| Data center security | ✅ | |
| Hardware | ✅ | |
| RDS patches | ✅ | |
| EC2 OS patches | | ✅ |
| IAM users | | ✅ |
| Data encryption | | ✅ |
| Network config | | ✅ |

### Hands-On Review (Console Exploration)

**Activity 1: Explore Billing Dashboard**
1. Go to Billing Dashboard
2. View month-to-date spending
3. Check Free Tier usage
4. Open Cost Explorer (visualize)

**Activity 2: IAM Best Practices Check**
1. IAM Dashboard → Security Recommendations
2. Check if MFA enabled on root
3. Review active access keys
4. Look at password policy

**Activity 3: Service Limits**
1. Service Quotas console
2. Search "Lambda"
3. See concurrent executions limit (1,000)
4. Search "EC2"
5. See On-Demand instance limit per region

### Flash Card Review

Create mental flash cards for:

**Front: "Distribute traffic across instances"**
Back: Elastic Load Balancing

**Front: "Serverless compute, 15 min max"**
Back: Lambda

**Front: "99.999999999% durability"**
Back: S3

**Front: "DDoS protection"**
Back: Shield

**Front: "SQL queries on S3"**
Back: Athena

### Question Pattern Recognition

**Pattern 1: "Company needs to..."**
→ Focus on business requirement, not technical details
→ Often testing cost optimization or service selection

**Pattern 2: "Which AWS responsibility..."**
→ Testing Shared Responsibility Model
→ AWS = hardware/infrastructure, Customer = data/config

**Pattern 3: "Minimum cost solution..."**
→ Testing pricing knowledge
→ Often: Spot instances, S3 Glacier, Reserved Instances

**Pattern 4: "Highest availability..."**
→ Testing high availability concepts
→ Often: Multi-AZ, Auto Scaling, Load Balancer

---

## 🗓️ Day 19: Domain-Focused Review {#day-19}

### Focus: Intensive Review by Domain

### Domain 1: Cloud Concepts (24%)

**Must-Know Topics:**
- 6 advantages of cloud computing
- AWS global infrastructure (Regions, AZs, Edge)
- Cloud deployment models
- Economic benefits

**Quick Quiz:**
1. How many AZs per Region? **Minimum 2**
2. What is hybrid cloud? **Mix of on-premises and public cloud**
3. Pay-as-you-go means? **Pay only for what you use, no upfront**
4. Benefit of elasticity? **Auto-scale up and down based on demand**

### Domain 2: Security & Compliance (30%)

**Must-Know Topics:**
- IAM (users, groups, roles, policies)
- Shared Responsibility Model
- Security services (Shield, WAF, GuardDuty, Inspector, Macie)
- Encryption (KMS, ACM)
- Compliance (Artifact)

**Critical Distinctions:**
- **IAM User**: Person or application
- **IAM Role**: Temporary permissions for AWS services
- **IAM Group**: Collection of users
- **IAM Policy**: Permissions document (JSON)

**Security Services Matrix:**

| Service | Purpose | Key Feature |
|---------|---------|-------------|
| **Shield** | DDoS protection | Standard free, Advanced paid |
| **WAF** | Web app firewall | Filter HTTP requests |
| **GuardDuty** | Threat detection | ML-based, CloudTrail/VPC logs |
| **Inspector** | Vulnerability scanning | EC2, containers |
| **Macie** | Find sensitive data | S3, PII detection |
| **Security Hub** | Central dashboard | Aggregate findings |

**Shared Responsibility Examples:**

| Scenario | Responsible Party |
|----------|-------------------|
| Patching RDS database engine | AWS |
| Patching EC2 operating system | Customer |
| Physical security of data centers | AWS |
| IAM user creation | Customer |
| S3 bucket permissions | Customer |
| S3 infrastructure | AWS |

### Domain 3: Cloud Technology & Services (34%)

**Compute Services:**
```
EC2: Virtual servers (full control)
Lambda: Serverless (event-driven, <15 min)
Elastic Beanstalk: PaaS (easy deployment)
Lightsail: Simple (fixed pricing)
Fargate: Containers (serverless)
```

**Storage Services:**
```
S3: Object storage (unlimited, 11 nines durability)
EBS: Block storage (one EC2, same AZ)
EFS: File storage (multiple EC2, multi-AZ)
Glacier: Archive (cheap, slow retrieval)
Snow Family: Physical transfer (Snowball, Snowmobile)
```

**Database Services:**
```
RDS: Relational (MySQL, PostgreSQL, etc.)
Aurora: High-performance relational (AWS-proprietary)
DynamoDB: NoSQL (millisecond latency, massive scale)
Redshift: Data warehouse (analytics)
ElastiCache: In-memory cache (Redis, Memcached)
```

**Networking:**
```
VPC: Virtual network (isolated)
Subnets: Public (internet) vs Private (internal)
Internet Gateway: VPC to internet
NAT Gateway: Private subnet outbound internet
Security Groups: Instance-level firewall (stateful)
Network ACLs: Subnet-level firewall (stateless)
Route 53: DNS (domain name resolution)
CloudFront: CDN (global content delivery)
```

**Application Integration:**
```
SQS: Queue (one-to-one messaging)
SNS: Pub/Sub (one-to-many messaging)
EventBridge: Event bus (route events)
Step Functions: Workflow orchestration
API Gateway: API management
```

### Domain 4: Billing, Pricing & Support (12%)

**Pricing Models:**
```
On-Demand: Pay per hour, no commitment
Reserved: 1-3 years, up to 75% off
Spot: Bid for unused, up to 90% off (can be interrupted)
Savings Plans: Flexible commitment
```

**Cost Tools:**
```
Cost Explorer: Visualize costs, forecast
Budgets: Set alerts, monitor spending
Cost and Usage Reports: Detailed data
Consolidated Billing: One bill for multiple accounts
```

**Support Plans:**
```
Basic: Free, no technical support
Developer: $29/month, email support
Business: $100/month, phone support, 1hr urgent, all Trusted Advisor
Enterprise: $15,000/month, TAM, 15min critical
```

**Free Tier:**
```
EC2: 750 hrs/month t2.micro (12 months)
S3: 5 GB storage (12 months)
RDS: 750 hrs/month db.t2.micro (12 months)
Lambda: 1M requests/month (always free)
DynamoDB: 25 GB storage (always free)
```

### Rapid-Fire Review (Memorization)

**Repeat aloud 5 times:**

1. "Multi-AZ for high availability, Read Replicas for performance"
2. "Security Groups are stateful, Network ACLs are stateless"
3. "Lambda max 15 minutes, 10 GB memory"
4. "S3 durability 11 nines, availability 99.99%"
5. "AWS handles infrastructure, customer handles data and configuration"
6. "Spot instances up to 90% off but can be interrupted"
7. "CloudWatch monitors performance, CloudTrail audits API calls"
8. "RDS for relational, DynamoDB for NoSQL, Redshift for analytics"
9. "Public subnet has Internet Gateway, private subnet has NAT Gateway"
10. "Enterprise Support includes TAM and 15-minute critical response"

---

## 🗓️ Day 20: Final Practice Exam {#day-20}

### Today's Goal
✅ Score 80%+ on final practice exam
✅ Simulate real exam conditions
✅ Identify any remaining gaps
✅ Build confidence

### Exam Simulation Instructions

**Setup:**
1. Find quiet space (90 minutes uninterrupted)
2. No notes, no internet (except exam)
3. Use scratch paper only
4. Set timer: 90 minutes

**Mindset:**
- This is the real exam
- Read each question twice
- Eliminate obviously wrong answers first
- Flag questions you're unsure about
- Review flagged questions if time permits

### After Exam: Final Analysis

**Target Scores:**
- Domain 1: 85%+
- Domain 2: 80%+
- Domain 3: 80%+
- Domain 4: 85%+
- **Overall: 80%+**

**If you scored 80%+:**
✅ You're ready for the exam!
✅ Review flagged questions tonight
✅ Light review tomorrow

**If you scored 70-79%:**
⚠️ Review weak domains tonight
⚠️ Focus on question patterns
⚠️ Take one more mini-quiz tomorrow

**If you scored <70%:**
❌ Consider rescheduling exam
❌ Spend 2-3 more days on weak domains
❌ Focus on understanding concepts, not memorization

### Final Exam Tips

**Time Management:**
- 65 questions in 90 minutes = 1.4 minutes per question
- Spend 60-70 minutes on first pass (answer all)
- Reserve 20-30 minutes for review

**Elimination Strategy:**
1. Read question and all options
2. Eliminate clearly wrong answers
3. Between remaining options, choose best fit
4. If stuck, flag and move on

**Keywords to Watch:**
- **"Most cost-effective"** → Spot, Reserved, Glacier, lifecycle policies
- **"Highest availability"** → Multi-AZ, multiple regions, failover
- **"Minimum latency"** → Edge locations, regions closer to users, caching
- **"Serverless"** → Lambda, DynamoDB, S3, Fargate
- **"Highly durable"** → S3 (11 nines)
- **"Audit trail"** → CloudTrail
- **"Performance monitoring"** → CloudWatch

**Common Traps:**
- Don't confuse RDS Multi-AZ (availability) with Read Replicas (performance)
- Security Groups are stateful, Network ACLs are stateless
- Glacier has retrieval delays (not instant like S3 Standard)
- Lambda has 15-minute limit (not unlimited)
- EBS is AZ-specific (can't attach across AZs)

### Question Type Strategies

**Scenario Questions** (Most common):
- Identify the business requirement
- Match requirement to AWS service capabilities
- Consider cost, performance, availability trade-offs

**Example:**
*"A company needs to store petabytes of data for analytics. Data is queried infrequently but needs to be analyzed when accessed. What service?"*

**Analysis:**
- **Petabytes** → Data warehouse
- **Analytics** → OLAP, not OLTP
- **Infrequent queries** → Not real-time database
**Answer:** Redshift ✅

**Comparison Questions:**
*"What is the difference between X and Y?"*

**Strategy:**
- Make a quick mental table
- Compare purpose, features, use cases

**Multiple Response Questions:**
*"Select TWO ways to reduce costs"*

**Strategy:**
- Need to select exactly 2 correct answers
- Partial credit = no credit
- If unsure, eliminate definitely wrong first

### Tonight's Checklist

- [ ] Review all flagged questions
- [ ] Re-read weak domain notes (30 min)
- [ ] Sleep early (7-8 hours)
- [ ] Prepare exam day logistics (ID, confirmation, quiet space)
- [ ] Positive mindset: "I am prepared and confident"

---

## 🗓️ Day 21: Last-Minute Review & Exam Preparation {#day-21}

### 🎯 You're Ready! Today is About Confidence

### Morning Review (2-3 hours max)

**Quick Reference Card (Print or write on paper):**

```
COMPUTE
├─ EC2: Virtual servers
├─ Lambda: Serverless (<15 min)
├─ Beanstalk: Easy deployment
├─ Lightsail: Simple, fixed price
└─ Fargate: Serverless containers

STORAGE
├─ S3: Objects (11 nines durability)
│   ├─ Standard: Frequent access
│   ├─ IA: Infrequent access
│   └─ Glacier: Archive
├─ EBS: Block (one EC2, same AZ)
└─ EFS: File (multiple EC2, multi-AZ)

DATABASE
├─ RDS: Relational (MySQL, PostgreSQL)
├─ Aurora: Fast relational (AWS)
├─ DynamoDB: NoSQL (millisecond)
├─ Redshift: Data warehouse
└─ ElastiCache: Caching

NETWORKING
├─ VPC: Virtual network
├─ IGW: Internet access (public subnet)
├─ NAT: Outbound internet (private subnet)
├─ SG: Stateful firewall
├─ NACL: Stateless firewall
├─ Route 53: DNS
└─ CloudFront: CDN

SECURITY
├─ IAM: Users, groups, roles, policies
├─ Shield: DDoS protection
├─ WAF: Web app firewall
├─ GuardDuty: Threat detection
├─ KMS: Encryption keys
└─ CloudTrail: API audit

MONITORING
├─ CloudWatch: Performance metrics
├─ CloudTrail: API calls
├─ Config: Configuration tracking
└─ Trusted Advisor: Best practices

PRICING
├─ On-Demand: No commitment
├─ Reserved: 1-3 years (up to 75% off)
├─ Spot: Bid for unused (up to 90% off)
└─ Savings Plans: Flexible commitment

SUPPORT
├─ Basic: Free
├─ Developer: $29/month
├─ Business: $100/month (1hr urgent)
└─ Enterprise: $15k/month (TAM, 15min critical)
```

### Critical Numbers to Memorize

- **Regions**: 30+ globally
- **AZs per Region**: Minimum 2
- **Edge Locations**: 400+
- **S3 Durability**: 99.999999999% (11 nines)
- **S3 Availability**: 99.99% (Standard)
- **S3 Max Object**: 5 TB
- **Lambda Max Time**: 15 minutes
- **Lambda Max Memory**: 10 GB
- **EC2 Free Tier**: 750 hours/month t2.micro (12 months)
- **S3 Free Tier**: 5 GB (12 months)
- **Lambda Free Tier**: 1M requests/month (always)
- **Spot Discount**: Up to 90%
- **Reserved Discount**: Up to 75%

### Top 20 Most-Tested Concepts

1. ✅ Shared Responsibility Model
2. ✅ EC2 pricing models
3. ✅ S3 storage classes
4. ✅ RDS Multi-AZ vs Read Replicas
5. ✅ VPC: Public vs Private subnets
6. ✅ Security Groups vs Network ACLs
7. ✅ IAM best practices
8. ✅ CloudWatch vs CloudTrail
9. ✅ Lambda limitations
10. ✅ EBS vs EFS vs S3
11. ✅ RDS vs DynamoDB vs Redshift
12. ✅ Auto Scaling + Load Balancing
13. ✅ Well-Architected Framework pillars
14. ✅ Support plan features
15. ✅ Cost optimization tools
16. ✅ Global infrastructure
17. ✅ Migration services (DMS, SMS, DataSync)
18. ✅ Security services (Shield, WAF, GuardDuty)
19. ✅ Serverless services
20. ✅ Free Tier offerings

### Final Confidence Boosters

**You know this:**
- ✅ You've completed 21 days of focused study
- ✅ You've taken 3+ practice exams
- ✅ You understand AWS fundamentals
- ✅ You can differentiate between services
- ✅ You know when to use what

**Remember:**
- The exam is designed to be passable
- 70% is passing (you likely know 80%+)
- Most questions test understanding, not memorization
- You can eliminate 2 wrong answers easily in most questions

### Pre-Exam Checklist

**Technical:**
- [ ] Stable internet connection
- [ ] Quiet testing environment
- [ ] Computer/laptop charged
- [ ] Webcam/mic working (if online proctored)
- [ ] Browser compatible (Chrome recommended)
- [ ] Closed other applications

**Documents:**
- [ ] Government-issued ID ready
- [ ] Exam confirmation email
- [ ] AWS account login (if needed)

**Physical:**
- [ ] Well-rested (7-8 hours sleep)
- [ ] Light meal (don't test hungry or overly full)
- [ ] Water nearby
- [ ] Comfortable clothing
- [ ] Bathroom break before starting

### During the Exam

**First 10 Minutes:**
- Read instructions carefully
- Note time limit and question count
- Take a deep breath
- Start with confidence

**Strategy:**
1. **Read question stem carefully** (don't skim)
2. **Identify keywords** (most, least, cost-effective, highest availability)
3. **Eliminate obviously wrong answers**
4. **Choose best remaining option**
5. **Flag if uncertain, move on**
6. **Don't overthink** (first instinct often correct)

**Time Check:**
- 30 minutes in: Should be around question 25
- 60 minutes in: Should be around question 45
- 70 minutes: First pass complete
- 70-90 minutes: Review flagged questions

### After the Exam

**If you pass (700+):**
🎉 Congratulations! You're AWS Certified Cloud Practitioner!
- Download certification from AWS Certification account
- Add to LinkedIn, resume
- Explore next certification (Solutions Architect Associate?)

**If you don't pass (<700):**
- Don't be discouraged (happens to many)
- AWS provides score report by domain
- Identify weak domains
- Restudy for 1-2 weeks
- Retake exam (wait 14 days)

### Positive Affirmations

**Say these aloud before exam:**
- "I am well-prepared for this exam"
- "I understand AWS fundamentals"
- "I can differentiate between AWS services"
- "I will pass this exam"
- "I am confident and calm"

---

# 🎯 You've Got This!

## Final Reminders

✅ **Passing Score**: 700/1000 (70%)
✅ **65 Questions**: 50 scored + 15 unscored (you don't know which)
✅ **90 Minutes**: About 1.4 minutes per question
✅ **Immediate Results**: Pass/fail shown immediately

## Day of Exam Mantra

*"I've studied for 21 days. I've taken multiple practice exams. I understand cloud concepts, AWS services, security, and billing. I can eliminate wrong answers. I will read carefully and choose the best option. I am prepared. I am confident. I will pass."*

---

# 📚 Appendix: Quick Reference Tables

## Service Categories

### Compute
| Service | Description | Use Case |
|---------|-------------|----------|
| EC2 | Virtual servers | Full control, any workload |
| Lambda | Serverless functions | Event-driven, <15 min |
| Elastic Beanstalk | PaaS | Easy deployment |
| Lightsail | Simple VPS | Fixed pricing |
| Fargate | Serverless containers | Containers without servers |

### Storage
| Service | Type | Attachment | Use Case |
|---------|------|------------|----------|
| S3 | Object | API/Internet | Backups, static websites |
| EBS | Block | One EC2 (same AZ) | Boot volumes, databases |
| EFS | File | Multiple EC2 (multi-AZ) | Shared storage |
| Glacier | Archive | API | Long-term archive |

### Database
| Service | Type | Best For |
|---------|------|----------|
| RDS | Relational | Structured data, SQL |
| Aurora | Relational | High performance SQL |
| DynamoDB | NoSQL | Massive scale, key-value |
| Redshift | Data Warehouse | Analytics, petabyte-scale |
| ElastiCache | In-memory | Caching, performance |

### Networking
| Service | Purpose |
|---------|---------|
| VPC | Virtual network |
| Subnets | Network subdivision |
| Internet Gateway | VPC internet access |
| NAT Gateway | Private subnet outbound |
| Security Groups | Instance firewall (stateful) |
| Network ACLs | Subnet firewall (stateless) |
| Route 53 | DNS |
| CloudFront | CDN |

### Security
| Service | Purpose |
|---------|---------|
| IAM | Identity and access |
| Shield | DDoS protection |
| WAF | Web application firewall |
| GuardDuty | Threat detection |
| Inspector | Vulnerability scanning |
| Macie | Find sensitive data |
| KMS | Encryption keys |
| CloudTrail | API audit trail |

## Decision Trees

### Compute Selection
```
Need what?
├─ Virtual server with full control → EC2
├─ Code runs on events, <15 min → Lambda
├─ Easy app deployment, no infrastructure knowledge → Elastic Beanstalk
├─ Simple website, predictable cost → Lightsail
└─ Containers without managing servers → Fargate
```

### Database Selection
```
What data type?
├─ Relational (SQL)
│   ├─ Standard engines (MySQL, Postgres) → RDS
│   └─ Need 5x performance → Aurora
├─ NoSQL (key-value, document)
│   └─ Massive scale, millisecond latency → DynamoDB
├─ Analytics on historical data
│   └─ Petabyte-scale queries → Redshift
└─ Need caching
    └─ In-memory speed → ElastiCache
```

### Storage Selection
```
What are you storing?
├─ Objects (files, backups, media)
│   ├─ Frequent access → S3 Standard
│   ├─ Infrequent access → S3 IA
│   └─ Archive (rarely accessed) → S3 Glacier
├─ EC2 boot/root volume → EBS
├─ Shared file system → EFS
└─ Physical data transfer (>10 TB) → Snow Family
```

---

# 🎓 Good Luck!

**You've prepared thoroughly. Trust your preparation. Stay calm. Read carefully. You will pass!**

**Go get certified! 🚀**

