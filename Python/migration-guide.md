# 🧭 Monolith → Modern Stack Migration Guide

---

## 🎯 Current State (Legacy)

| Component | Technology |
|-----------|-----------|
| Language | Java 11 |
| Framework | Spring (XML-heavy or hybrid config) |
| App Server | IBM WebSphere (full Java EE container) |
| Build | Maven (with org-specific shared libs) |
| UI | JSP (server-side rendered) |
| Database | Traditional DB (JDBC, stored procedures) |
| Integration | SOAP + REST APIs |

---

## 🚦 Phased Migration Strategy

> ⚠️ **Do NOT rewrite everything.**
> ⚠️ **Do NOT jump directly to microservices.**

**Core Pattern:** Strangler Fig + Modularization First

---

## 🧩 Phase 0 — Legacy Discovery *(Most Important Phase)*

Before touching a single line of code, build deep understanding of the system.

### Architecture Discovery Map

```
Entry Points        →   Servlets / Controllers / EJBs
Business Layer      →   Services, Managers, Helpers
Data Access Layer   →   JDBC, iBatis, MyBatis, Stored Procs
Integration Points  →   SOAP endpoints, REST clients, MQ, FTP
Cross-Cutting       →   Security, Transactions, Caching, Session, Batch Jobs
```

### Critical Questions to Answer

- Where exactly is business logic located?
- Is logic embedded inside JSP scriptlets?
- Are there WebSphere-specific APIs in use (JNDI, JMS, EJB)?
- How are transactions managed — container-managed (CMT) or bean-managed (BMT)?
- Is there shared static state or application-scoped singletons?
- Which stored procedures contain business rules vs. pure queries?
- What internal/org libraries are used and what do they do?

### 🧠 AI Prompts for Legacy Code Analysis

Use these prompts with Claude or any AI assistant to systematically unpack legacy code:

#### Architecture

```
"Explain the architecture of this module. What are the main layers 
and their responsibilities? Where are the boundaries violated?"
```

```
"Map the dependency graph of this module. Which classes/packages 
does it depend on, and which depend on it?"
```

#### Coupling & WebSphere Dependencies

```
"Identify tight coupling points in this code. Which parts depend 
on WebSphere-specific APIs (JNDI, EJB, JTA, IBM security)?"
```

```
"What would break if I removed WebSphere and deployed this on 
embedded Tomcat instead? List every incompatible API."
```

#### Business Logic Tracing

```
"Trace the full execution path for [use case] from the HTTP request 
to the database. List every class, method, and external call involved."
```

```
"Where is business logic leaking into the wrong layer — e.g., rules 
in JSP, SQL in controllers, or formatting in service classes?"
```

#### Database Analysis

```
"Which tables are read and written by this service? Are there any 
cross-module queries that suggest missing service boundaries?"
```

```
"List all stored procedures called. Which contain business logic 
that should be in the application layer instead?"
```

#### Risk Assessment

```
"Rate the migration complexity of this class from 1–10. Explain 
what makes it hard to migrate and suggest the safest approach."
```

```
"Which modules are hardest to modify? Which areas have the most 
production defects or change failures historically?"
```

#### Domain Discovery

```
"Looking at the package structure and class names, group these into 
logical business domains. Suggest microservice boundaries based 
on bounded contexts."
```

```
"For [Module], describe the business process it implements in 
non-technical language. Who are the actors, what are the steps, 
and what are the business rules?"
```

#### JSP / UI Analysis

```
"Analyse this JSP and its backing servlet/bean. What data does it 
display? Map each data element to a REST endpoint and each user 
action to an HTTP method + URL."
```

```
"What business logic is embedded in this JSP (scriptlets, JSTL 
conditions)? Should this live in the API layer or the React component?"
```

#### Migration Readiness

```
"What are the migration steps to convert this class to Spring Boot 3 
/ Java 21? Flag any javax.* → jakarta.* changes, WebSphere APIs, 
and EJB dependencies that need replacing."
```

```
"Generate a risk register for migrating this module. List the top 5 
risks, their likelihood, impact, and a mitigation for each."
```

---

## 🏗️ Phase 1 — Modernize the Monolith *(Foundation Upgrade)*

> **Goal:** Same functionality. New runtime platform. No business logic changes yet.

### Step 1 — Upgrade Java

```
Java 11  →  Java 17 (safe LTS)  →  Java 21 (if ecosystem is stable)
```

**Fix during upgrade:**
- Removed and deprecated APIs
- Illegal reflective access warnings
- JAXB removal (extremely common issue in Java 11 → 17)
- `javax.*` namespace (becomes `jakarta.*` in Spring Boot 3)

**Java 21 bonus — enable virtual threads:**
```yaml
# application.yml
spring:
  threads:
    virtual:
      enabled: true   # Zero-cost for I/O-bound services
```

### Step 2 — Remove WebSphere Dependencies

| WebSphere | Spring Boot Equivalent |
|-----------|----------------------|
| JNDI DataSource | `spring.datasource.*` in `application.yml` |
| EJB Session Bean | `@Service` + `@Transactional` |
| Container-Managed Transactions | `@Transactional` (Spring) |
| WebSphere Security (JAAS) | Spring Security |
| EJB Message-Driven Bean | `@KafkaListener` / `@RabbitListener` |
| EAR / WAR deployment | Standalone Spring Boot JAR |
| WebSphere JMS | Spring JMS / Kafka / RabbitMQ |
| `web.xml` | Auto-configuration / `@Configuration` |
| IBM logging | Logback / SLF4J |

**Old JNDI config:**
```xml
<resource-ref>
  <res-ref-name>jdbc/myDS</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
</resource-ref>
```

**New Spring Boot config:**
```yaml
spring:
  datasource:
    url: jdbc:postgresql://host:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASS}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
```

### Step 3 — Convert to Spring Boot

**Add:**
- `@SpringBootApplication` entry point
- Embedded Tomcat (auto-included)
- `application.yml` / `application.properties`
- Spring Boot Actuator (`/health`, `/metrics`, `/info`)
- Structured JSON logging

**Remove:**
- `web.xml`
- `ibm-*.xml` deployment descriptors
- All WebSphere Admin Console configuration
- EJB deployment descriptors (`ejb-jar.xml`)

✅ **Result:** A bootable, modern monolith running on embedded Tomcat.

---

## 🎨 Phase 2 — API-First Backend

Before separating the UI, expose proper, well-structured APIs.

### Service Layer Architecture

```
Controller  (HTTP handling, request/response mapping)
    ↓
Service     (business logic, transactions)
    ↓
Domain      (entities, value objects, business rules)
    ↓
Repository  (data access — JPA or JDBC)
```

> Even while still a monolith — structure your code like microservices. This pays dividends in every future phase.

### REST API Checklist

- [ ] `@RestController` with proper HTTP verbs (GET / POST / PUT / DELETE / PATCH)
- [ ] OpenAPI 3.0 documentation via `springdoc-openapi`
- [ ] DTO layer (never expose `@Entity` directly in API responses)
- [ ] Global exception handler (`@RestControllerAdvice`)
- [ ] Input validation (`@Valid` + `jakarta.validation` annotations)
- [ ] API versioning from day one: `/api/v1/orders`
- [ ] Standard error response format (RFC 7807 `problem+json`)

### SOAP Handling Strategy

```
External SOAP Consumer
        ↓
Anti-Corruption Layer (ACL Adapter)
        ↓
Internal Domain / Service Layer
```

- Wrap all SOAP calls in an ACL — never let SOAP types leak into your domain
- Use **Apache CXF** (`cxf-spring-boot-starter-jaxws`) for both consuming and exposing SOAP
- Generate Java stubs from WSDL using `wsdl2java` Maven plugin
- Add circuit breakers (Resilience4j) around all outbound SOAP calls
- Keep WSDL contracts immutable for external consumers while refactoring internally

---

## 🖥️ Phase 3 — UI Migration: JSP → React

### Strangler UI Migration Pattern

```
Step 1:  Build REST APIs for a feature
Step 2:  Build the React component (with mock data first)
Step 3:  Wire React component to real API
Step 4:  Use feature flag to toggle JSP vs React for same URL
Step 5:  Verify React version in production (A/B testing)
Step 6:  Retire the JSP page and backing servlet
Step 7:  Repeat for next feature
```

### Target Architecture

```
React SPA (served from CDN)
        ↓
API Gateway
        ↓
Spring Boot Backend
```

### Recommended React Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Framework | React 18+ | Component UI with hooks |
| Build Tool | Vite | Fast dev server, optimized builds |
| Routing | React Router v6 | Client-side navigation |
| Server State | TanStack Query | API calls, caching, loading states |
| Global State | Zustand / Redux Toolkit | Session, user, cart state |
| HTTP Client | Axios | REST calls with auth interceptors |
| UI Library | Ant Design / MUI | Enterprise component library |
| Forms | React Hook Form + Zod | Performant forms + validation |
| Auth | Keycloak OIDC Client | OAuth2 PKCE + JWT management |
| Testing | Vitest + Testing Library | Component unit tests |

---

## 🗄️ Phase 4 — Database Modernization: JPA Introduction

> ⚠️ **Do NOT rewrite all JDBC at once.** Migrate module by module.

### Migration Path

| Legacy | Modern |
|--------|--------|
| Raw JDBC / RowMapper | `@Entity` + Spring Data JPA `@Repository` |
| iBatis / MyBatis XML | `@Query` (JPQL / native SQL) or QueryDSL |
| Stored procedure (simple) | Refactor to service layer |
| Stored procedure (complex) | `@NamedStoredProcedureQuery` (keep temporarily) |
| Manual connection pool | HikariCP (Spring Boot default) |
| No schema versioning | Flyway or Liquibase (mandatory) |
| Cross-module foreign keys | Soft references — ID only, no FK across services |

### JPA Best Practices

```yaml
spring:
  jpa:
    open-in-view: false          # Prevents N+1 anti-pattern — ALWAYS disable
    hibernate:
      ddl-auto: validate         # NEVER use create-drop or update in production
    properties:
      hibernate:
        format_sql: true
        generate_statistics: true  # Enable during migration to spot slow queries
```

- Always use **DTO projections** for read queries — never return raw `@Entity` from APIs
- Use **lazy loading** by default; fetch eagerly only when you know you need it
- Control transaction boundaries explicitly — don't rely on defaults
- Add query performance monitoring from day one (Hibernate statistics + slow query log)
- Write Flyway/Liquibase scripts for every schema change — no manual DDL

---

## 🧱 Phase 5 — Modular Monolith

> **Do this before microservices.** This is the most skipped and most critical phase.

### Target Package Structure

```
com.company.application
    ├── user
    │     ├── controller
    │     ├── service
    │     ├── domain
    │     ├── repository
    │     └── config
    ├── order
    │     ├── controller
    │     ├── service
    │     ├── domain
    │     └── repository
    ├── payment
    ├── notification
    └── shared
          ├── exception
          ├── config
          └── security
```

### Module Rules (Enforce Strictly)

- ❌ No direct cross-module `@Repository` access
- ❌ No cyclic dependencies between modules
- ❌ No shared `@Entity` classes between modules
- ✅ Cross-module communication via service interfaces only
- ✅ Shared utilities in a `common` / `shared` module
- ✅ Each module owns its own DB tables

> If you can enforce these rules as a monolith, extracting microservices later becomes straightforward — you're essentially just moving packages to new services.

---

## 🚀 Phase 6 — Microservice Extraction *(Selective)*

> Only extract a service when **all three** conditions are true:

| Condition | Why It Matters |
|-----------|---------------|
| Independent scaling required | The module has different load characteristics |
| Separate release cycle needed | The team needs to deploy it independently |
| Clear bounded context exists | No shared transactions with other modules |
| Team ownership available | One team owns and operates the service end-to-end |

### Extraction Blueprint

```
Step 1:  Identify the bounded context (e.g., Notification)
Step 2:  Validate — no distributed transactions, separate DB tables, independent logic
Step 3:  Create new service repo: notification-service
Step 4:  Move domain, service, repository, and API layer
Step 5:  Start with same DB, separate schema (safe start)
Step 6:  Route traffic via API Gateway to new service
Step 7:  Migrate to independent DB when service is stable
Step 8:  Delete old module from monolith after stability window
```

### Good First Microservice Candidates

- Notifications (email / SMS / push)
- Reporting / analytics
- Document generation
- User / identity management (if complex enough)
- File upload / storage

### When NOT to Extract

```
Two modules share the same DB tables          →  Not yet
Two modules share a transaction boundary      →  Not yet
Two modules share domain model / entities     →  Not yet
Team size < 8–10 engineers                   →  Probably not
No CI/CD pipeline in place                   →  Definitely not
```

---

## 🏛️ High-Level Architecture

### Development Architecture

```
┌─────────────────────────────────────────────┐
│              Developer Machine               │
│                                             │
│  React Dev Server (:3000)                   │
│       ↓                                     │
│  Spring Boot App (:8080)                    │
│       ↓                                     │
│  PostgreSQL + Kafka (Docker Compose)        │
│                                             │
│  Config Server  │  Eureka  │  Zipkin        │
└─────────────────────────────────────────────┘
```

### Production Architecture

```
Users
  ↓
CDN  (React SPA static assets)
  ↓
WAF / DDoS Protection
  ↓
Load Balancer (L7)
  ↓
API Gateway  (auth, routing, rate limiting)
  ↓
┌──────────────────────────────────────────┐
│         Spring Boot Services             │
│  (Kubernetes Pods — auto-scaling)        │
│                                          │
│  user-service  │  order-service  │  ...  │
└──────────────────────────────────────────┘
  ↓
Database Cluster  (PostgreSQL RDS — per service)
  ↓
Cache  (Redis Cluster)
  ↓
Message Broker  (Kafka / RabbitMQ)

Cross-Cutting:
  Prometheus → Grafana      (metrics)
  ELK Stack                 (centralised logging)
  Jaeger / Zipkin           (distributed tracing)
  Keycloak                  (identity + OAuth2)
  Vault                     (secrets management)
```

---

## ⚠️ Key Challenges & Mitigations

### 1. Hidden Business Logic

Logic buried in JSPs, stored procedures, and static utility classes is the #1 migration risk. You cannot safely move what you cannot see.

**Mitigation:** Write characterization tests (approval tests) that capture current behavior *before* moving any code. These act as a safety net during migration.

### 2. Transaction Boundary Changes

WebSphere container-managed transactions behave differently from Spring's `@Transactional`. Subtle differences in commit/rollback behavior can cause data integrity bugs that only appear in production.

**Mitigation:** Map every transaction boundary explicitly during Phase 0 discovery. Test with production-clone data.

### 3. JPA Performance Regressions

Naively replacing JDBC with JPA can introduce N+1 query problems, Cartesian product queries, and memory spikes that didn't exist before.

**Mitigation:** Enable Hibernate statistics during migration. Set up slow query logging. Use DTO projections — never return full entity graphs from APIs.

### 4. SOAP Edge Cases

Legacy SOAP services frequently have custom headers, non-standard XML namespaces, WS-Security quirks, and WSDL inconsistencies that generate incorrect stubs.

**Mitigation:** Test generated stubs against real endpoints with production-representative payloads before going live.

### 5. Shared Database During Transition

While migrating, services will inevitably share a database temporarily. This creates tight coupling and prevents true independence.

**Mitigation:** Use the staged approach:
```
Stage 1:  Same DB, same schema      (temporary — monolith phase)
Stage 2:  Same DB, separate schemas (transition)
Stage 3:  Separate DB instances     (target state)
```

### 6. Team Readiness

Microservices dramatically increase operational complexity. If the team isn't ready for distributed systems, the migration will fail regardless of how good the architecture is.

**Mitigation:** Run workshops on Spring Boot, Docker, Kubernetes, and React before starting. Don't extract microservices until the team is comfortable operating the simpler modular monolith.

---

## 📉 Risk Mitigation Strategy

- ✅ Write automated tests **before** migration begins (characterization tests)
- ✅ Add structured logging and monitoring from **day one**
- ✅ Use **feature toggles** to run old and new paths in parallel
- ✅ Deploy new services in parallel — **canary release** approach
- ✅ Always maintain a **rollback strategy** for each migration step
- ✅ Never migrate the database and application layer simultaneously

---

## 📊 Migration Decision Matrix

| Situation | Recommendation |
|-----------|---------------|
| No test coverage | Write characterization tests first — do not migrate yet |
| Heavy stored procedure logic | Modular monolith first; migrate DB logic gradually |
| Team size < 8 engineers | Avoid microservices — modular monolith is the right end state |
| High traffic on specific module | Extract only that module; keep rest as monolith |
| Tight deadline | Upgrade Java + Spring Boot runtime first; everything else after |
| Heavy SOAP integrations | Wrap in ACL adapters before decomposing |
| No CI/CD pipeline | Build pipeline before extracting any service |

---

## 🧠 How to Identify Microservice Boundaries (DDD Approach)

Use **Domain-Driven Design (DDD)** concepts:

```
Aggregate     →  A cluster of objects treated as a single unit (e.g., Order + OrderLines)
Entity        →  An object with a unique identity (e.g., Customer, Product)
Bounded Context  →  A clear boundary within which a domain model is defined and consistent
Ubiquitous Language  →  Shared vocabulary between dev team and business stakeholders
```

### The Shared-Anything Test

> If two modules share **any** of the following — they should **not** be separate services yet:

- Shared DB tables
- Shared transaction boundaries
- Shared domain model / entity classes
- Shared business invariants

---

## 🏗️ Governance Model for Microservices

Microservices fail without governance. Establish these before the first service goes to production.

### API Standards
- REST naming conventions (nouns, not verbs: `/orders` not `/getOrders`)
- Versioning from day one: `/api/v1/`
- Mandatory OpenAPI 3.0 documentation for every endpoint
- Standard error format: RFC 7807 `problem+json`

### Developer Standards
- Centralised structured logging format (JSON with `traceId`, `serviceId`, `correlationId`)
- Correlation ID propagated across all service calls
- Mandatory health check endpoints (`/actuator/health`)
- Code review + quality gate (SonarQube ≥ 80% coverage, 0 critical vulnerabilities)

### DevOps Standards
- Every service containerised (Docker)
- Every service has its own CI/CD pipeline
- Automated tests mandatory (unit + integration + contract tests)
- Monitoring dashboards (Prometheus + Grafana) required before go-live

### Operational Standards
- Defined SLA per service
- Clear service ownership (one team = one service)
- Incident response runbook per service
- Defined release cadence and change freeze windows

---

## 📅 6–12 Month Migration Roadmap

### 🔵 Month 1–2 — Discovery & Stabilization

**Goal:** Understand the system deeply before touching it.

- [ ] Full codebase architecture mapping
- [ ] Identify modules and domain boundaries
- [ ] DB schema documentation (SchemaSpy / DBeaver)
- [ ] Dependency graph analysis (Maven dependency:tree)
- [ ] Add standardized structured logging
- [ ] Introduce centralized configuration

**Deliverables:**
- Architecture diagram (current state)
- Domain map and bounded context candidates
- Risk heatmap
- Prioritized migration backlog

---

### 🟢 Month 3–4 — Runtime Modernization

**Goal:** Java 21 + Spring Boot 3 — same business logic, new runtime.

- [ ] Java 17 upgrade (then 21)
- [ ] `javax.*` → `jakarta.*` migration
- [ ] Remove all WebSphere-specific APIs
- [ ] Replace JNDI → `application.yml` datasource
- [ ] Replace container transactions → `@Transactional`
- [ ] Replace WebSphere security → Spring Security
- [ ] Add Spring Boot Actuator endpoints
- [ ] Add HikariCP connection pool configuration

**Result:** ✅ Bootable modern monolith on embedded Tomcat. No business logic changes.

---

### 🟡 Month 5–6 — API-First + UI Separation

**Goal:** Decouple UI from backend. Expose clean APIs.

- [ ] Introduce `@RestController` layer
- [ ] Add OpenAPI / Swagger documentation
- [ ] Create DTO layer (request / response objects)
- [ ] Global exception handler (`@RestControllerAdvice`)
- [ ] Build React SPA consuming APIs
- [ ] Gradually retire JSP screens (feature-by-feature)

**Target:** 30–50% of JSP screens retired by end of this phase.

---

### 🟠 Month 7–8 — Modular Monolith

**Goal:** Clear domain boundaries. Eliminate cross-module coupling.

- [ ] Restructure packages by business domain
- [ ] Eliminate cross-module direct repository access
- [ ] Introduce service interface boundaries between modules
- [ ] Add integration tests per module
- [ ] Introduce Flyway/Liquibase for schema management
- [ ] Migrate first module from JDBC to JPA

**Result:** ✅ Clean modular monolith with enforceable boundaries.

---

### 🔴 Month 9–12 — Selective Microservice Extraction

**Extract only modules that qualify:**
- High independent load
- Clear bounded context
- Dedicated team ownership
- Separate release cadence

**Good first candidates:** Notifications, Reporting, User Management

**For each extracted service:**
```
1. New Git repo + CI/CD pipeline
2. Own Spring Boot application
3. Same DB / separate schema (transition)
4. API Gateway routing
5. Separate DB (when stable)
6. Remove from monolith
```

---

## ❌ What You Should NOT Do

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Rewrite everything from scratch | You lose domain knowledge; high risk; takes 2–3x longer than expected |
| Split into 20 microservices immediately | Distributed systems complexity with none of the benefits yet |
| Replace DB and architecture simultaneously | Too many moving parts; impossible to debug regressions |
| Remove JSP before APIs exist | Nothing to connect the UI to |
| Ignore performance testing | JPA migrations routinely introduce 10x query regressions |
| Skip the modular monolith phase | Services with shared state / transactions will just be a distributed monolith |
| No governance model | Microservices become unmanageable without API standards and ownership |

---

## 🔍 Key Questions to Answer Before Proceeding

Understanding your context determines how aggressive the migration plan should be:

- **Estimated lines of code?** — Determines effort and phasing
- **Number of DB tables?** — Complexity of data migration
- **Team size?** — Determines whether microservices are viable
- **Current test coverage?** — Determines how much safety net work is needed first
- **Deployment frequency?** — Determines urgency of CI/CD investment
- **Number of external SOAP/REST integrations?** — Determines ACL layer complexity
- **Any regulatory / compliance requirements?** — May constrain DB split strategy

---

> 💡 **Final Philosophy:** Don't optimize your architecture for résumé, trend, or conference talks. Optimize for **maintainability**, **scalability**, and **operational simplicity**. A well-structured modular monolith beats a chaotic microservices setup every time.
