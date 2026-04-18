# Hanuman Sports Academy — Court Booking Calendar System
## Development Plan v1.0

---

## Table of Contents

1. [BRD Review & Gap Analysis](#1-brd-review--gap-analysis)
2. [System Architecture](#2-system-architecture)
3. [Tech Stack](#3-tech-stack)
4. [Database Schema Design](#4-database-schema-design)
5. [Module Breakdown](#5-module-breakdown)
6. [API Design Overview](#6-api-design-overview)
7. [Development Phases & Milestones](#7-development-phases--milestones)
8. [Team Structure & Roles](#8-team-structure--roles)
9. [Risk Register](#9-risk-register)
10. [Testing Strategy](#10-testing-strategy)
11. [Deployment & DevOps](#11-deployment--devops)
12. [Open Questions & Decisions Required](#12-open-questions--decisions-required)

---

## 1. BRD Review & Gap Analysis

### 1.1 Strengths of the BRD

The BRD covers the core booking lifecycle well: availability, booking creation, payment, notifications, waitlist, and admin dashboard. Stakeholder mapping and use cases are clear. Non-functional requirements (performance, security, uptime) are stated at a high level.

---

### 1.2 Identified Gaps

The following gaps were identified after a full-stack review of the BRD. Each gap is rated by severity: **Critical**, **High**, **Medium**, or **Low**.

#### GAP-01 — Authentication & Authorization Model [Critical]

**Issue:** The BRD mentions "multi-user login (players, admins)" but does not define the auth mechanism, role hierarchy, session management, or OAuth/SSO support.

**Missing:**
- Role definitions (Super Admin, Admin, Coach, Player, Finance)
- Permission matrix per role
- Auth method (JWT, sessions, OAuth with Google/Apple)
- Account verification flow (email/phone OTP)
- Password reset / account recovery flows
- Social login (Google, Apple ID)

**Recommendation:** Define a 5-role RBAC model with a permissions matrix before sprint 1.

---

#### GAP-02 — Court Resource Model is Underspecified [Critical]

**Issue:** The BRD references indoor courts, ping pong tables, and cricket nets but does not define the physical resource hierarchy or the rules engine formally.

**Missing:**
- How many indoor courts total? (BRD implies 3 courts + 2 ping pong tables + 3 cricket nets — but the relationship is ambiguous)
- Outdoor courts count and types
- A formal resource conflict resolution model
- Ping Pong → Court blocking logic is mentioned but not defined as a formal algorithm
- Cricket Net → Indoor court area conflict logic is vague

**Recommendation:** Produce a Resource Dependency Map before DB schema is finalized. Define explicit slot-reservation logic as pseudocode.

---

#### GAP-03 — No Pricing & Tariff Model Defined [Critical]

**Issue:** The BRD mentions dynamic pricing, membership plans, and partial payments, but there is no pricing schema.

**Missing:**
- How many membership tiers? What are the benefits?
- How is peak/off-peak pricing configured? (time-based? day-based?)
- Package deals — are these credits or unlimited sessions?
- Partial payment minimum threshold
- Tax handling (is tax applicable? which jurisdiction?)
- Refund policy on cancellation after partial payment

**Recommendation:** Requires a Product Owner decision document before the Payment module is built.

---

#### GAP-04 — No User Registration / Onboarding Flow [High]

**Issue:** The BRD describes user inputs at booking time but there is no registration, profile, or onboarding flow defined.

**Missing:**
- Guest checkout vs. registered user distinction
- Mandatory vs. optional profile fields
- Age verification (BRD mentions age restrictions as "optional")
- Minor/guardian consent flow
- Profile picture, skill level, and sports preferences for personalization
- KYC or ID verification requirements (if any)

---

#### GAP-05 — Liability / Safety Form Lifecycle is Incomplete [High]

**Issue:** The BRD says users must acknowledge a release of liability form, but the lifecycle is not defined.

**Missing:**
- Is this a one-time sign at registration or per-booking?
- Versioning: what happens when the form changes? Do existing users need to re-sign?
- How does admin "verify" the signed form? Dashboard action? Auto-verification?
- Storage and legal retention period for signed forms
- Minor/guardian consent signature flow

---

#### GAP-06 — Cancellation & Refund Workflow Not Defined [High]

**Issue:** The BRD mentions cancellation policies are "configurable by admin" and references no-show penalties, but there is no defined workflow.

**Missing:**
- Who can cancel? (user, admin, coach)
- Refund calculation logic: full refund before X hours, partial refund between X–Y hours, no refund after Y
- What happens to equipment rental on cancellation?
- No-show penalty mechanism: automatic charge? credit deduction?
- Dispute/appeal process for wrongful no-show charges
- Recurring booking cancellation: cancel one occurrence vs. all future

---

#### GAP-07 — Notification System Architecture Not Specified [High]

**Issue:** The BRD lists notification triggers but there is no architecture or provider defined.

**Missing:**
- SMS provider (Twilio? AWS SNS?)
- Email provider (SendGrid? AWS SES?)
- Push notification provider and mobile app assumption (is there a mobile app or only web?)
- Notification preference management (opt-in/opt-out per channel)
- Notification templates and localization
- Admin notification preferences (digest vs. real-time)

---

#### GAP-08 — Reporting & Analytics Depth Undefined [Medium]

**Issue:** The BRD lists report types but not their format, access level, or export requirements.

**Missing:**
- Export formats: PDF, CSV, Excel?
- Who has access to which reports? (Finance team vs. Admin vs. Management)
- Scheduled report delivery (weekly/monthly email)?
- Real-time vs. batch analytics?
- Data retention period for historical reports
- Occupancy rate calculation formula

---

#### GAP-09 — Waitlist Logic is Incomplete [Medium]

**Issue:** Waitlist is mentioned but the algorithm is not defined.

**Missing:**
- FIFO vs. priority-based (members first)?
- How long does a waitlisted user have to confirm before the slot goes to the next person?
- Maximum waitlist size per slot
- Notification expiry window

---

#### GAP-10 — Equipment Rental Return & Damage Handling [Medium]

**Issue:** Equipment rental inventory management is mentioned but return/damage flows are missing.

**Missing:**
- Return confirmation mechanism (staff scans? self-report?)
- Damage deposit / security hold
- Late return penalties
- Damaged equipment reporting and billing

---

#### GAP-11 — No Multi-Tenancy or Franchise Consideration [Medium]

**Issue:** The system is scoped to one academy but future scalability should be considered now.

**Missing:**
- Is this single-academy only, or should the schema support multiple branches?
- If single-academy, is there a plan to white-label later?

---

#### GAP-12 — Audit Trail & Compliance Not Addressed [Medium]

**Issue:** No mention of audit logs for booking changes, payment events, or admin actions.

**Missing:**
- Audit log requirements (who changed what, when)
- PCI-DSS compliance scope (card data handling — Stripe handles this, but must be confirmed)
- GDPR/data privacy compliance (if any international users)
- Data deletion/right-to-forget support

---

#### GAP-13 — Calendar Integration Strategy Deferred [Low]

**Issue:** Google Calendar / Outlook is listed as a "future add-on" with no hook defined.

**Recommendation:** Design the booking event model with iCal-compatible fields from day one (uid, dtstart, dtend, summary) to avoid rework.

---

#### GAP-14 — No Accessibility (a11y) Requirements [Low]

**Issue:** Mobile-first design is mentioned, but no WCAG compliance level is stated.

**Recommendation:** Commit to WCAG 2.1 AA as the baseline.

---

### 1.3 Gap Summary Table

| ID | Gap | Severity | Owner |
|----|-----|----------|-------|
| GAP-01 | Auth & RBAC model missing | Critical | PO + Tech Lead |
| GAP-02 | Court resource model underspecified | Critical | PO + Architect |
| GAP-03 | Pricing & tariff model undefined | Critical | PO + Finance |
| GAP-04 | User onboarding flow missing | High | PO + UX |
| GAP-05 | Liability form lifecycle incomplete | High | PO + Legal |
| GAP-06 | Cancellation & refund workflow missing | High | PO + Finance |
| GAP-07 | Notification architecture undefined | High | Tech Lead |
| GAP-08 | Reporting depth undefined | Medium | PO + Finance |
| GAP-09 | Waitlist algorithm incomplete | Medium | Tech Lead |
| GAP-10 | Equipment return/damage flow missing | Medium | PO |
| GAP-11 | Multi-tenancy not considered | Medium | Architect |
| GAP-12 | Audit trail & compliance missing | Medium | Tech Lead |
| GAP-13 | Calendar integration hooks deferred | Low | Tech Lead |
| GAP-14 | Accessibility requirements missing | Low | UX |

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                          │
│   Web App (React)          Mobile App (React Native / PWA)   │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTPS / REST + WebSocket
┌──────────────────────────▼──────────────────────────────────┐
│                     API GATEWAY / BFF                        │
│         (Rate limiting, Auth, Routing, Logging)              │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐
│ Auth Service │  │Booking Engine│  │ Notification Service  │
│ (JWT/OAuth)  │  │(Conflict Eng)│  │  (Email/SMS/Push)     │
└──────────────┘  └──────┬───────┘  └──────────────────────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
    ┌──────────────┐ ┌──────────┐ ┌──────────────────┐
    │  PostgreSQL  │ │  Redis   │ │   File Storage   │
    │  (Primary DB)│ │ (Cache,  │ │  (S3 / Signed    │
    │              │ │ Locks,   │ │   Forms, Docs)   │
    │              │ │Waitlist) │ │                  │
    └──────────────┘ └──────────┘ └──────────────────┘
              │
    ┌─────────▼──────────┐
    │  Payment Gateway   │
    │  (Stripe / PayPal) │
    └────────────────────┘
```

### 2.2 Key Architectural Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| API Style | REST + WebSocket | REST for CRUD; WS for real-time calendar sync |
| Session Management | JWT (short-lived) + Refresh Tokens | Stateless, scalable |
| Booking Conflict Engine | Pessimistic DB locking + Redis distributed lock | Prevent race conditions during simultaneous bookings |
| Real-time Availability | WebSocket broadcast on slot state change | Immediate UI sync without polling |
| Queue for Notifications | Bull / BullMQ (Redis-backed) | Reliable async delivery, retry on failure |
| File Storage | AWS S3 (signed URLs) | Secure form storage, scalable |

---

## 3. Tech Stack

### 3.1 Backend

| Layer | Technology | Notes |
|-------|-----------|-------|
| Runtime | Node.js 20 LTS | High ecosystem support |
| Framework | NestJS | Modular, TypeScript-native, DI container |
| ORM | Prisma | Type-safe DB access, migrations |
| Database | PostgreSQL 16 | ACID compliance, row-level locking |
| Cache / Locks | Redis 7 | Real-time slot locking, session cache |
| Queue | BullMQ | Notification jobs, recurring booking scheduler |
| Auth | Passport.js + JWT | Multi-strategy (local, Google OAuth) |
| File Storage | AWS S3 | Signed form PDFs, document storage |
| Payment | Stripe SDK | Primary; PayPal as secondary |
| Email | SendGrid | Templated transactional emails |
| SMS | Twilio | OTP, booking reminders |
| Logging | Winston + Datadog | Structured logging, alerting |

### 3.2 Frontend

| Layer | Technology | Notes |
|-------|-----------|-------|
| Framework | Next.js 14 (App Router) | SSR for SEO, RSC for performance |
| Language | TypeScript | Type safety across the stack |
| UI Library | shadcn/ui + Tailwind CSS | Accessible, customizable components |
| Calendar | FullCalendar.io | Feature-rich, supports resource views |
| State | Zustand + React Query | Server state via RQ; UI state via Zustand |
| Forms | React Hook Form + Zod | Validation aligned with backend schemas |
| Real-time | Socket.io Client | Calendar live sync |
| Testing | Playwright + Vitest | E2E and unit |

### 3.3 Infrastructure

| Component | Technology |
|-----------|-----------|
| Cloud | AWS (primary) |
| Compute | ECS Fargate (containerized) |
| CI/CD | GitHub Actions |
| Container | Docker |
| IaC | Terraform |
| Monitoring | Datadog / CloudWatch |
| CDN | CloudFront |
| DNS | Route 53 |

---

## 4. Database Schema Design

### 4.1 Core Entities (ERD Summary)

```
users
  id, email, phone, full_name, role, skill_level, 
  is_verified, is_minor, guardian_id, created_at

roles
  id, name (SUPER_ADMIN | ADMIN | COACH | PLAYER | FINANCE)

courts
  id, name, type (INDOOR | OUTDOOR), sport_type,
  capacity, is_active, requires_net_config

resources
  id, court_id, resource_type (COURT | TABLE | NET),
  name, status (AVAILABLE | BLOCKED | MAINTENANCE)

resource_dependencies
  id, parent_resource_id, child_resource_id, 
  dependency_type (EXCLUSIVE | SHARED)
  -- handles ping pong table → indoor court blocking

bookings
  id, user_id, court_id, start_time, end_time,
  status (PENDING | CONFIRMED | CANCELLED | NO_SHOW),
  payment_status, is_recurring, recurrence_rule,
  coach_id, num_players, special_notes, created_at

booking_resources
  id, booking_id, resource_id
  -- many-to-many for multi-resource bookings

waitlist
  id, user_id, court_id, requested_date, requested_slot,
  position, status, notified_at, expires_at

equipment
  id, name, sport_type, total_qty, available_qty,
  rental_price_per_session, deposit_amount

equipment_rentals
  id, booking_id, equipment_id, qty, returned_at,
  damage_reported, damage_fee

payments
  id, booking_id, user_id, amount, currency,
  method (STRIPE | PAYPAL | VENUE), status,
  stripe_payment_intent_id, receipt_url, created_at

refunds
  id, payment_id, amount, reason, status, processed_at

membership_plans
  id, name, price, duration_days, max_bookings_per_week,
  discount_pct, includes_equipment_rental

user_memberships
  id, user_id, plan_id, starts_at, expires_at, status

pricing_rules
  id, court_id, day_of_week, start_hour, end_hour,
  price_per_slot, is_peak

liability_forms
  id, user_id, version, signed_at, storage_url,
  is_current

notifications
  id, user_id, type, channel (EMAIL|SMS|PUSH),
  status, sent_at, payload

audit_logs
  id, actor_id, entity_type, entity_id, action,
  before_state (json), after_state (json), ip, created_at
```

### 4.2 Booking Conflict Engine (Core Logic)

```
BOOK(court_id, start_time, end_time, user_id):
  1. Acquire Redis distributed lock on court_id+date_slot
  2. BEGIN TRANSACTION (serializable isolation)
  3. Check direct overlap: SELECT * FROM bookings WHERE court_id=X 
     AND status NOT IN (CANCELLED) AND tsrange overlaps
  4. Check resource dependencies: resolve all affected resources
  5. If any conflict → ROLLBACK, release lock, return 409
  6. INSERT booking + booking_resources
  7. UPDATE equipment available_qty
  8. COMMIT, release lock
  9. Enqueue notification job
```

---

## 5. Module Breakdown

### 5.1 Auth Module

- Registration (email + phone OTP verification)
- Login (email/password, Google OAuth)
- JWT issuance (15 min access token, 7-day refresh token)
- RBAC guard on all protected routes
- Password reset via email link
- Minor account with guardian linkage

### 5.2 User & Profile Module

- CRUD for user profile
- Skill level, preferred sports
- Booking history view
- Membership status
- Liability form signing flow

### 5.3 Court & Resource Module

- Court CRUD (Admin only)
- Resource dependency configuration
- Maintenance blocking (date-range based)
- Court availability engine (respects all resource dependencies)

### 5.4 Booking Module (Core)

- Slot availability check API
- Booking creation with atomic conflict check
- Recurring booking scheduler (BullMQ cron)
- Booking modification (reschedule)
- Cancellation with refund trigger
- No-show flagging (automated post-slot-end)
- Admin override and manual booking

### 5.5 Waitlist Module

- Join waitlist for a slot
- FIFO queue management in Redis
- Automatic slot-offer notification with 2-hour confirmation window
- Expiry and cascade to next in queue

### 5.6 Equipment Module

- Equipment catalog (CRUD)
- Rental request attached to booking
- Inventory decrement on booking confirmation
- Return confirmation by staff
- Damage reporting and fee billing

### 5.7 Payment Module

- Stripe payment intent creation
- PayPal order creation (secondary)
- Partial payment logic (configurable minimum %)
- Pay-at-venue booking flag
- Automated receipt via SendGrid
- Refund processing (full / partial per policy)
- Membership plan purchase and renewal
- Webhook handlers for payment events

### 5.8 Notification Module

- BullMQ queue consumers (email, SMS, push)
- Templates for: confirmation, reminder (24h), cancellation, waitlist offer, no-show penalty
- User notification preference management
- Admin alert service

### 5.9 Admin Dashboard Module

- Booking management (view, edit, cancel, override)
- Court blocking scheduler
- Equipment inventory management
- Pricing rule configuration
- Liability form management
- Incident logging

### 5.10 Reporting & Analytics Module

- Court utilization report (by day/week/month)
- Revenue report (by sport, period)
- Equipment rental demand report
- Player engagement insights
- Scheduled report email delivery
- Export: CSV, PDF

### 5.11 Calendar Module (Frontend)

- FullCalendar resource view (courts as resources)
- Real-time WebSocket slot updates
- Color-coded sport display
- Daily / weekly / monthly toggle
- Admin-only edit mode overlay

---

## 6. API Design Overview

### 6.1 Base URL Pattern

```
/api/v1/{resource}
```

### 6.2 Key Endpoints

#### Authentication
```
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/refresh
POST   /api/v1/auth/logout
POST   /api/v1/auth/verify-otp
POST   /api/v1/auth/forgot-password
POST   /api/v1/auth/reset-password
```

#### Courts & Availability
```
GET    /api/v1/courts                         # list courts
GET    /api/v1/courts/:id/availability        # slots with filters
GET    /api/v1/courts/:id/availability?date=&sport=&duration=
POST   /api/v1/courts                         # admin: create court
PATCH  /api/v1/courts/:id                     # admin: update court
POST   /api/v1/courts/:id/block               # admin: block court
```

#### Bookings
```
POST   /api/v1/bookings                       # create booking
GET    /api/v1/bookings                       # user's bookings
GET    /api/v1/bookings/:id
PATCH  /api/v1/bookings/:id                   # reschedule
DELETE /api/v1/bookings/:id                   # cancel
GET    /api/v1/bookings/admin/all             # admin view
```

#### Payments
```
POST   /api/v1/payments/intent                # Stripe intent
POST   /api/v1/payments/paypal/order          # PayPal order
POST   /api/v1/payments/webhook/stripe
POST   /api/v1/payments/webhook/paypal
POST   /api/v1/payments/:id/refund            # admin refund
```

#### Equipment
```
GET    /api/v1/equipment
POST   /api/v1/equipment                      # admin: add item
PATCH  /api/v1/equipment/:id/return           # staff: mark returned
POST   /api/v1/equipment/:id/damage           # staff: report damage
```

#### Waitlist
```
POST   /api/v1/waitlist                       # join waitlist
DELETE /api/v1/waitlist/:id                   # leave waitlist
POST   /api/v1/waitlist/:id/confirm           # user confirms offered slot
```

#### Reports
```
GET    /api/v1/reports/utilization
GET    /api/v1/reports/revenue
GET    /api/v1/reports/equipment
GET    /api/v1/reports/players
GET    /api/v1/reports/export?type=pdf|csv
```

---

## 7. Development Phases & Milestones

### Phase 0 — Foundation (Weeks 1–2)

| Task | Owner | Deliverable |
|------|-------|------------|
| Gap resolution workshop with PO | PM + Tech Lead | Signed-off answers for all Critical gaps |
| Resource dependency map finalized | Architect + PO | Court/Resource Dependency Doc |
| Pricing model document | PO + Finance | Pricing Rules Spec |
| Auth & RBAC matrix | Tech Lead | RBAC Permission Matrix Doc |
| Project scaffolding (monorepo, CI/CD, Docker, environments) | DevOps + Backend | Dev/Staging environments live |
| DB schema v1 | Backend Lead | Prisma schema + migration scripts |
| Design system setup | Frontend | Tailwind config, component library |

**Exit Criteria:** All Critical gaps resolved. Dev environment running. DB schema approved.

---

### Phase 1 — Core MVP (Weeks 3–8)

**Goal:** Working booking flow end-to-end (no payments).

| Week | Focus | Deliverables |
|------|-------|-------------|
| 3 | Auth module | Register, Login, OTP, JWT, RBAC |
| 3–4 | Court & Resource module | Court CRUD, availability API, conflict engine |
| 4–5 | Booking module (core) | Create, view, cancel bookings |
| 5 | Calendar frontend | FullCalendar resource view, slot click to book |
| 6 | Equipment module | Catalog, rental with booking |
| 6–7 | Liability form flow | Digital signing, storage, admin verification |
| 7–8 | Notification module (email) | Confirmation, reminder, cancellation |
| 8 | User portal UI | Dashboard, booking history, profile |

**Exit Criteria:** Complete booking lifecycle works without payment. Admin can manage bookings.

---

### Phase 2 — Payments & Waitlist (Weeks 9–12)

| Week | Focus | Deliverables |
|------|-------|-------------|
| 9 | Stripe integration | Full payment, partial payment, pay-at-venue |
| 10 | PayPal integration | Secondary payment option |
| 10 | Refund & cancellation policy engine | Configurable policy, automated refund triggers |
| 11 | Membership plans | Plan purchase, user membership gating |
| 11 | Dynamic pricing | Peak/off-peak pricing rules engine |
| 12 | Waitlist module | Join, FIFO queue, 2-hour confirm window |
| 12 | SMS notifications | Twilio integration, OTP, reminders |

**Exit Criteria:** Full payment flow working. Waitlist functional. Membership plans purchasable.

---

### Phase 3 — Admin Dashboard & Reporting (Weeks 13–15)

| Week | Focus | Deliverables |
|------|-------|-------------|
| 13 | Admin dashboard UI | Booking management, court blocking, calendar admin view |
| 14 | Recurring bookings | Weekly recurrence scheduler (BullMQ cron) |
| 14 | Pricing & policy config UI | Admin-configurable rules |
| 15 | Reporting module | Utilization, revenue, equipment, player reports |
| 15 | Report export | PDF and CSV download |

**Exit Criteria:** Admin can manage all system entities. Reports are accurate and exportable.

---

### Phase 4 — Polish, Hardening & Launch (Weeks 16–18)

| Week | Focus | Deliverables |
|------|-------|-------------|
| 16 | Performance optimization | Query optimization, Redis caching, CDN |
| 16 | Accessibility audit | WCAG 2.1 AA compliance check |
| 17 | Security audit | Penetration test, OWASP checklist |
| 17 | Load testing | Simulate peak concurrent bookings |
| 18 | UAT with stakeholders | Sign-off from PO, Admin, Finance |
| 18 | Production deployment | Go-live checklist, monitoring live, runbook |

**Exit Criteria:** UAT sign-off. Zero P0 bugs. All acceptance criteria from BRD §10 met.

---

### Phase 5 — Post-Launch Enhancements (Weeks 19–24)

- Google Calendar / Outlook sync integration
- Mobile PWA optimization or native app (React Native)
- Push notification support
- Social sharing / referral program
- Advanced analytics dashboard (Recharts / Metabase)
- Multi-branch / franchise support (if needed)

---

### Timeline Summary

```
Week  1- 2 │ Phase 0 — Foundation
Week  3- 8 │ Phase 1 — Core MVP
Week  9-12 │ Phase 2 — Payments & Waitlist
Week 13-15 │ Phase 3 — Admin & Reporting
Week 16-18 │ Phase 4 — Hardening & Launch
Week 19-24 │ Phase 5 — Post-Launch
```

**Total to Production: ~18 weeks (~4.5 months)**

---

## 8. Team Structure & Roles

| Role | Count | Responsibilities |
|------|-------|-----------------|
| Product Owner | 1 | Requirements, gap closure, UAT |
| Project Manager | 1 | Sprint planning, risk tracking, stakeholder communication |
| Backend Engineer (Lead) | 1 | Architecture, NestJS, DB schema, booking engine |
| Backend Engineer | 1–2 | Auth, payments, notifications, reporting |
| Frontend Engineer (Lead) | 1 | Next.js, calendar, admin dashboard |
| Frontend Engineer | 1 | User portal, forms, mobile optimization |
| DevOps / Cloud Engineer | 1 (part-time) | AWS infra, CI/CD, monitoring |
| QA Engineer | 1 | Test plan, E2E with Playwright, load testing |
| UI/UX Designer | 1 (part-time) | Wireframes, design system, a11y audit |

**Team Size:** 8–10 people  
**Sprint Cadence:** 2-week sprints  
**Ceremonies:** Daily standup (15 min), Sprint planning, Sprint review, Retrospective

---

## 9. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Booking conflict race condition at peak load | High | Critical | Redis distributed locking + DB serializable transactions |
| Payment gateway downtime (Stripe/PayPal) | Medium | High | Circuit breaker pattern; fallback to pay-at-venue; queue retry |
| GAP-02 resource model unclear → rework DB | High | High | Resolve in Phase 0 before schema is built |
| Scope creep (new features mid-development) | High | Medium | Strict change management; defer to Phase 5 backlog |
| SMS/email deliverability issues | Medium | Medium | Use reputable providers; monitor delivery rates; retry queue |
| Recurring booking edge cases (DST, holidays) | Medium | Medium | Use date-fns-tz or Luxon; explicit timezone storage; test suite |
| Security breach (payment or PII) | Low | Critical | PCI-DSS scoping; all card data via Stripe; encryption at rest |
| Key person dependency | Medium | High | Knowledge documentation; pair programming for critical modules |

---

## 10. Testing Strategy

### 10.1 Unit Testing

- Backend: Vitest / Jest — all service-layer functions
- Frontend: Vitest + React Testing Library — components and hooks
- Target coverage: 80% minimum on critical paths

### 10.2 Integration Testing

- API integration tests using Supertest
- Database layer tested against test PostgreSQL container
- Payment flows tested against Stripe test mode

### 10.3 End-to-End Testing

- Playwright — full booking lifecycle scenarios
- Scenarios:
  - Happy path: search → book → pay → receive confirmation
  - Conflict scenario: two users book the same slot simultaneously
  - Cancellation → refund flow
  - Admin blocks court with active bookings
  - Waitlist offer → confirm → book

### 10.4 Load Testing

- Tool: k6
- Target: 200 concurrent users booking simultaneously
- Verify no double-bookings occur under load
- Redis lock performance validation

### 10.5 Security Testing

- OWASP Top 10 checklist
- JWT validation edge cases
- SQL injection protection (Prisma parameterized queries)
- Stripe webhook signature validation

---

## 11. Deployment & DevOps

### 11.1 Environments

| Environment | Purpose | Update Frequency |
|-------------|---------|-----------------|
| Development | Local dev | On commit |
| Staging | QA & UAT | On merge to `main` |
| Production | Live users | On tagged release |

### 11.2 CI/CD Pipeline (GitHub Actions)

```
PR opened → Lint + Type check + Unit tests
            ↓
Merge to main → Build Docker images → Push to ECR
                 ↓
               Deploy to Staging → Run E2E tests
                 ↓
Tagged release → Deploy to Production → Smoke tests → Notify team
```

### 11.3 Monitoring & Alerting

- **APM:** Datadog APM for API latency and error rates
- **Uptime:** Pingdom / Datadog synthetic monitors (99.9% target)
- **Log aggregation:** CloudWatch Logs + Datadog
- **Alerts:** PagerDuty for P0/P1 incidents
- **Error tracking:** Sentry (frontend + backend)

### 11.4 Backup & Recovery

- PostgreSQL: automated daily RDS snapshots, 30-day retention
- Redis: AOF persistence enabled
- S3: versioning enabled on signed-form bucket
- RTO (Recovery Time Objective): 4 hours
- RPO (Recovery Point Objective): 24 hours

---

## 12. Open Questions & Decisions Required

The following items require explicit decisions from the Product Owner and stakeholders before development begins on the affected modules.

| # | Question | Blocking | Needed By |
|---|----------|----------|-----------|
| Q1 | Exact court/resource count and layout (indoor courts, nets, tables, outdoor courts) | Phase 1 Week 3 | PO + Academy Mgmt |
| Q2 | Membership tiers: how many, what benefits, what price? | Phase 2 Week 11 | PO + Finance |
| Q3 | Cancellation policy: what are the specific refund windows? | Phase 2 Week 10 | PO + Finance |
| Q4 | Liability form: one-time at registration or per booking? | Phase 1 Week 7 | PO + Legal |
| Q5 | Is a mobile native app required or is mobile-web (PWA) sufficient for launch? | Phase 0 | PO |
| Q6 | Which SMS provider? (Twilio recommended) | Phase 2 Week 12 | Tech Lead + PO |
| Q7 | Should guest (no-account) bookings be supported? | Phase 1 Week 3 | PO |
| Q8 | Tax: Is sales tax applied to bookings? Which tax jurisdiction? | Phase 2 Week 9 | Finance |
| Q9 | Waitlist confirmation window: how many hours before offering to next user? | Phase 2 Week 12 | PO |
| Q10 | Data retention: how long to keep booking/payment records? | Phase 0 | PO + Legal |

---

## Appendix A — Acceptance Criteria Traceability

| BRD §10 Criterion | Implemented In | Verified By |
|-------------------|---------------|------------|
| No double bookings | Booking Engine (§5.4) + Redis Lock | Load Test + E2E |
| Real-time sync without conflicts | WebSocket + booking engine | E2E (concurrent test) |
| Payment & receipt for all options | Payment Module (§5.7) | Integration test |
| Reliable notifications | Notification Module (§5.8) + BullMQ | Integration test |
| Admin dashboard with stats | Admin Module (§5.9) + Reports (§5.10) | UAT |

---

*This document is a living plan and should be updated at each sprint review. All gaps marked Critical must be resolved before the end of Phase 0.*
