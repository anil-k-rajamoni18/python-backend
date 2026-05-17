# Business Requirements Document (BRD)
## Competitive Exam Preparation Portal

---

| **Document Info**     | **Details**                                      |
|-----------------------|--------------------------------------------------|
| Document Title        | Business Requirements Document (BRD)             |
| Project Name          | Competitive Exam Preparation Portal              |
| Version               | 1.1 (Updated — Subjects & Project Name Added)    |
| Prepared By           | Product & Engineering Team                       |
| Document Status       | Draft – Pending Stakeholder Review               |
| Date                  | May 2026                                         |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Business Objectives](#2-business-objectives)
3. [Scope](#3-scope)
4. [Stakeholders](#4-stakeholders)
5. [User Roles & Personas](#5-user-roles--personas)
6. [Functional Requirements](#6-functional-requirements)
   - 6.1 Landing Page | 6.2 Auth | 6.3 Course & Content | **6.4 Subject Taxonomy** | 6.5 Member | 6.6 Faculty | 6.7 Admin | 6.8 Subscriptions
7. [Non-Functional Requirements](#7-non-functional-requirements)
8. [System Architecture Overview](#8-system-architecture-overview)
9. [Feature Phasing & Roadmap](#9-feature-phasing--roadmap)
10. [Subscription Plans](#10-subscription-plans)
11. [Technology Stack Recommendations](#11-technology-stack-recommendations)
12. [Data & Privacy Considerations](#12-data--privacy-considerations)
13. [Assumptions & Constraints](#13-assumptions--constraints)
14. [Risks & Mitigations](#14-risks--mitigations)
15. [**Project Name Suggestions**](#15-project-name-suggestions)
16. [Glossary](#16-glossary)

---

## 1. Executive Summary

**ExamEdge** is a web-based learning and exam preparation portal designed for students targeting competitive examinations at the state and national levels in India. The platform aims to centralize study materials, live and recorded sessions, mock tests, and AI-assisted learning into a single, organized, and role-based environment.

The portal will cater to three primary user groups — **Students (Members)**, **Faculty (Tutors)**, and **Platform Administrators** — each with purpose-built interfaces and access controls.

The initial development phase focuses exclusively on the **Notes/Study Material** feature. Subsequent phases will introduce video recordings, AI-assisted content Q&A, mock assessments, and quizzes.

---

## 2. Business Objectives

| # | Objective |
|---|-----------|
| BO-01 | Provide a centralized, organized platform for competitive exam aspirants in India |
| BO-02 | Enable faculty to publish day-wise structured study materials (notes, PDFs) efficiently |
| BO-03 | Enable students to access curated content aligned with their subscribed course and tier |
| BO-04 | Introduce a tiered subscription model to generate sustainable revenue |
| BO-05 | Deliver AI-powered content assistance (Q&A on PDFs and videos) in later phases |
| BO-06 | Build a scalable foundation to support College Entrance exams in future roadmap |

---

## 3. Scope

### 3.1 In Scope — Phase 1 (MVP)

- Public landing page with current affairs / news feed and course overviews
- Three-role authentication system: **Member (Student)**, **Faculty**, **Admin**
- Faculty dashboard to upload and organize day-wise PDF notes
- Member dashboard to browse, subscribe, and view course materials
- Subscription management (Free, Elite, Pro tiers)
- Admin panel for user management, course management, and subscription oversight
- Course and chapter/day-wise content structuring

### 3.2 In Scope — Future Phases

| Phase | Feature |
|-------|---------|
| Phase 2 | Video Recordings (upload, stream, access-controlled) |
| Phase 3 | Mock Tests & Self-Assessment Modules |
| Phase 4 | Quizzes (topic-wise, timed, scored) |
| Phase 5 | AI Chat Assistant (context: PDFs and video transcripts) |
| Phase 6 | College Entrance Exams (POLYCET, ECET, EAMCET, JEE Main, JEE Advanced, CAT, etc.) |

### 3.3 Out of Scope

- Mobile Native Applications (iOS/Android) — Phase 1 only web responsive
- Live Streaming / Real-time Classes — considered in future
- Payment Gateway Integration — Phase 1 uses manual/admin-assigned plans
- Third-party LMS integrations (Moodle, etc.)

---

## 4. Stakeholders

| Stakeholder | Role | Interest |
|---|---|---|
| Product Owner | Internal | Vision alignment, feature prioritization |
| Platform Admin | Internal | Day-to-day portal management |
| Faculty / Tutors | External | Upload content, manage their courses |
| Students / Members | External (End Users) | Access study materials, prepare for exams |
| Development Team | Internal | Technical implementation |
| Business/Finance Team | Internal | Subscription revenue tracking |

---

## 5. User Roles & Personas

### 5.1 Member (Student)

**Who:** A student preparing for competitive exams such as IBPS PO/Clerk, SBI PO, RBI Grade B, SSC CGL, or State PSC examinations.

**Goals:**
- Access organized, day-wise study notes
- Track progress across enrolled courses
- Upgrade subscription to unlock premium content

**Pain Points:**
- Scattered notes across YouTube, Telegram, and individual coaching websites
- No single source of truth for structured exam preparation

---

### 5.2 Faculty (Tutor)

**Who:** A subject-matter expert or coaching professional who delivers content for one or more exam categories.

**Goals:**
- Upload structured, day-wise PDF notes
- Manage their own course content independently
- Track student engagement with materials (future)

**Pain Points:**
- Lack of a professional platform to publish and monetize content
- No mechanism to track if students are actually reading materials

---

### 5.3 Admin

**Who:** The platform operator managing the entire ecosystem.

**Goals:**
- Manage users (approve/suspend accounts)
- Manage courses and assign faculty
- Configure subscription plans and access rules
- Monitor platform health and usage analytics

---

## 6. Functional Requirements

### 6.1 Landing Page (Public)

| ID | Requirement |
|----|-------------|
| LP-01 | Display latest current affairs / news (curated or RSS-integrated) |
| LP-02 | Display overview of available courses with exam categories |
| LP-03 | Call-to-action buttons for Registration and Login |
| LP-04 | Display subscription plan comparison (Free, Elite, Pro) |
| LP-05 | Testimonials section and exam category navigation |

---

### 6.2 Authentication & Authorization

| ID | Requirement |
|----|-------------|
| AU-01 | Separate login flows for Member, Faculty, and Admin |
| AU-02 | Role-Based Access Control (RBAC) enforced at API and UI levels |
| AU-03 | Member self-registration with email verification |
| AU-04 | Faculty accounts created by Admin (not self-registered) |
| AU-05 | Password reset via email OTP |
| AU-06 | Session management with JWT (access + refresh token) |
| AU-07 | Optional: Google OAuth for student login |

---

### 6.3 Course & Content Management

| ID | Requirement |
|----|-------------|
| CM-01 | Courses organized by Exam Category → Course → Subject → Day/Chapter |
| CM-02 | Admin creates exam categories and assigns courses to faculty |
| CM-03 | Faculty can create subjects and upload day-wise PDFs within their assigned courses |
| CM-04 | PDF upload supports drag-and-drop with file size and format validation |
| CM-05 | Faculty can edit, replace, or delete uploaded content |
| CM-06 | Content visibility toggled: Draft / Published / Scheduled |
| CM-07 | System tracks upload timestamps and version history (overwrite log) |

---

### 6.4 Subject Taxonomy — Core Syllabus Structure

This section defines the **standard subject categories** that form the backbone of every competitive exam course on the platform. All faculty uploads, course hierarchies, and AI chat contexts will be organized under these subject groups.

#### 6.4.1 Core Subjects (Common Across All Banking, SSC & PSC Exams)

| Subject | Key Topics Covered |
|---|---|
| **Quantitative Aptitude** | Number Systems, Simplification, Percentages, Profit & Loss, Ratio & Proportion, Time-Speed-Distance, Time & Work, Simple & Compound Interest, Averages, Mixtures & Alligations, Data Interpretation (Tables, Bar, Pie, Line), Mensuration, Algebra |
| **Reasoning Ability** | Seating Arrangement, Puzzles, Syllogisms, Coding-Decoding, Blood Relations, Direction Sense, Inequalities, Input-Output, Data Sufficiency, Logical Reasoning, Alphanumeric Series |
| **English Language** | Reading Comprehension, Cloze Test, Error Detection, Sentence Improvement, Para Jumbles, Fill in the Blanks, Vocabulary (Synonyms/Antonyms), Phrase/Idiom Meaning, Sentence Connectors |
| **General Awareness / GK** | Current Affairs (Monthly), Banking & Financial Awareness, Static GK (Capitals, Currencies, Awards), Government Schemes, Important Dates, Sports, National & International News |
| **Computer Knowledge** | Basics of Computers, MS Office, Internet & Networking, Cyber Security Fundamentals, Input/Output Devices, Memory & Storage, Software Concepts |

#### 6.4.2 Exam-Specific Additional Subjects

| Exam | Additional Subject(s) |
|---|---|
| **RBI Grade B** | Economics & Social Issues (ESI), Finance & Management, General Finance |
| **SSC CGL** | General Intelligence & Reasoning (Advanced), Statistics (Tier II), General Studies |
| **State PSC (Group 1/2)** | Indian Polity, Indian History, Indian Geography, Economy, Science & Technology, Telangana/AP State Affairs |
| **IBPS PO / Clerk** | Data Analysis & Interpretation (Advanced), Descriptive English (Letter/Essay Writing) |
| **SBI PO** | Data Analysis, Marketing & Computers, Descriptive Test |

#### 6.4.3 College Entrance Subjects (Phase 6 — Future Scope)

| Exam | Subjects |
|---|---|
| **POLYCET** | Mathematics, Physical Science, Biology |
| **ECET** | Mathematics, Engineering subjects (Diploma stream specific) |
| **EAMCET (Engg.)** | Mathematics, Physics, Chemistry |
| **EAMCET (Medical)** | Botany, Zoology, Physics, Chemistry |
| **JEE Main & Advanced** | Physics, Chemistry, Mathematics (Advanced Problem Solving) |
| **CAT** | VARC (Verbal Ability & RC), DILR (Data Interpretation & Logical Reasoning), QA (Quantitative Aptitude) |

#### 6.4.4 Subject Management Requirements

| ID | Requirement |
|----|-------------|
| SM-01 | Admin can create, edit, and reorder subjects within any course |
| SM-02 | A course can have one or more assigned faculty, each managing specific subjects |
| SM-03 | Subjects are tagged with exam category for filtering and search purposes |
| SM-04 | Members can filter content by subject within their enrolled course |
| SM-05 | AI Chat (Phase 5) will be context-isolated per subject — questions answered only from that subject's content |
| SM-06 | Mock tests and quizzes (Phase 3/4) will be generated or uploaded per subject |

---

### 6.5 Member Dashboard

| ID | Requirement | View all subscribed courses and progress (days completed) |
| MD-02 | Day-wise content listing with read/unread indicators |
| MD-03 | In-browser PDF viewer (no download unless Pro tier allows) |
| MD-04 | Bookmark individual notes for quick revisit |
| MD-05 | Search within course content (by title, subject, day number) |
| MD-06 | Notification badge for new content added to enrolled courses |

---

### 6.6 Faculty Dashboard

| ID | Requirement |
|----|-------------|
| FD-01 | View assigned courses and their content tree |
| FD-02 | Upload PDF for a specific subject and day number |
| FD-03 | Add a title, description, and tags to each upload |
| FD-04 | Preview uploaded PDF before publishing |
| FD-05 | View upload history with edit/delete options |
| FD-06 | View basic engagement stats (views per note — future) |

---

### 6.7 Admin Panel

| ID | Requirement |
|----|-------------|
| AD-01 | User management: list, search, activate, suspend Members and Faculty |
| AD-02 | Course management: create, edit, archive exam categories and courses |
| AD-03 | Assign Faculty to specific courses |
| AD-04 | Manage subscription plans (define features per tier) |
| AD-05 | Manually assign or upgrade subscription tier for a Member |
| AD-06 | Content moderation: view and remove any uploaded content |
| AD-07 | Dashboard overview: total members, active subscriptions, content count |

---

### 6.8 Subscription & Access Control

| ID | Requirement |
|----|-------------|
| SC-01 | Free tier: Access to limited/preview content per course |
| SC-02 | Elite tier: Full access to notes; limited downloads |
| SC-03 | Pro tier: Full access to all content + downloads + priority features |
| SC-04 | Access checks enforced server-side on every content request |
| SC-05 | Admin can configure which content is available per tier |
| SC-06 | Subscription expiry with graceful downgrade to Free tier |

---

## 7. Non-Functional Requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NF-01 | Performance | Page load time < 2.5s on 4G connection |
| NF-02 | Scalability | System should support up to 50,000 concurrent members at launch scale |
| NF-03 | Availability | 99.5% uptime SLA; scheduled downtime during off-peak hours |
| NF-04 | Security | HTTPS enforced; PDFs served via signed/expiring URLs (not public S3 links) |
| NF-05 | Security | OWASP Top 10 compliance; no direct file URL exposure |
| NF-06 | Responsiveness | Fully responsive UI for desktop, tablet, and mobile browsers |
| NF-07 | Accessibility | WCAG 2.1 AA compliance for key user flows |
| NF-08 | Audit | Admin actions (delete, suspend) logged with actor, timestamp, and reason |
| NF-09 | Storage | PDF storage on cloud object storage (S3/Azure Blob) with CDN delivery |
| NF-10 | Backup | Daily automated database backups with 30-day retention |

---

## 8. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     CLIENT LAYER                            │
│   [Public Landing Page]  [Member Portal]  [Admin Panel]     │
│              [Faculty Dashboard]                            │
│                 (React / Next.js)                           │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTPS / REST API
┌─────────────────────────▼───────────────────────────────────┐
│                    API GATEWAY / BFF                        │
│          (Rate Limiting, Auth Middleware, RBAC)             │
└──────────┬─────────────────────┬───────────────────────────┘
           │                     │
┌──────────▼──────────┐  ┌──────▼──────────────────┐
│   Auth Service      │  │   Core API Service       │
│ (JWT, OAuth, OTP)   │  │ (Courses, Notes, Users,  │
└─────────────────────┘  │  Subscriptions)          │
                         └──────┬───────────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
   ┌──────▼──────┐    ┌─────────▼──────┐    ┌────────▼──────┐
   │  Database   │    │  File Storage  │    │  CDN / Media  │
   │ (PostgreSQL │    │ (S3 / Azure    │    │  Delivery     │
   │  / MongoDB) │    │  Blob Storage) │    │  (CloudFront) │
   └─────────────┘    └────────────────┘    └───────────────┘

         ── Future Phases ──
   ┌─────────────────────────────────────────┐
   │         AI / LLM Service               │
   │  (PDF Embeddings → Vector DB → RAG)    │
   │   Video Transcription → Q&A Chat       │
   └─────────────────────────────────────────┘
```

---

## 9. Feature Phasing & Roadmap

```
PHASE 1 — MVP (Notes Portal)
├── Landing Page (News + Course Overview)
├── Three-role Auth System (Member / Faculty / Admin)
├── Course & Subject Hierarchy
├── Faculty: Day-wise PDF Upload
├── Member: Browse & View Notes (in-browser PDF viewer)
├── Subscription Tiers (Free / Elite / Pro) — Admin Managed
└── Admin Panel (Users, Courses, Content)

PHASE 2 — Video Recordings
├── Faculty: Upload Recorded Lectures (video files)
├── Cloud video storage + streaming (HLS)
├── Member: Watch recordings within subscribed course
└── Playback controls, progress tracking

PHASE 3 — Mock Tests & Self-Assessment
├── Admin/Faculty: Create mock test with questions
├── Timed, full-length exam simulations
├── Auto-scoring and result analysis
└── Performance history per student

PHASE 4 — Quizzes
├── Topic-wise short quizzes
├── Instant feedback (correct/wrong with explanation)
└── Streak tracking and leaderboards

PHASE 5 — AI Chat Assistant
├── PDF-to-Embeddings pipeline (LangChain + Vector DB)
├── Video transcription (Whisper / AssemblyAI)
├── RAG-based Q&A: "Ask a question about today's notes"
└── Per-course AI chat context isolation

PHASE 6 — College Entrance Exams
├── New exam categories: POLYCET, ECET, EAMCET
├── JEE Main, JEE Advanced, CAT
└── Separate content tracks and mock test series
```

---

## 10. Subscription Plans

| Feature | 🆓 Free | ⭐ Elite | 🚀 Pro |
|---------|---------|---------|--------|
| Browse course catalog | ✅ | ✅ | ✅ |
| Access to current affairs / news | ✅ | ✅ | ✅ |
| Preview notes (limited days/chapters) | ✅ (3 days) | ✅ (All) | ✅ (All) |
| Full notes access | ❌ | ✅ | ✅ |
| PDF Download | ❌ | ❌ | ✅ |
| Video Recordings (Phase 2) | ❌ | ✅ | ✅ |
| Mock Tests (Phase 3) | ❌ (limited) | ✅ | ✅ |
| AI Chat Assistant (Phase 5) | ❌ | Limited | Unlimited |
| Priority Support | ❌ | ❌ | ✅ |
| Pricing (Monthly) | ₹0 | ₹299 | ₹499 |

> **Note:** Pricing is indicative and subject to market validation. Admin can override per-user plans manually in Phase 1.

---

## 11. Technology Stack Recommendations

| Layer | Recommended Technology | Rationale |
|-------|------------------------|-----------|
| Frontend | Next.js (React) + TypeScript | SSR for SEO, strong ecosystem, aligns with existing team skills |
| UI Library | shadcn/ui + Tailwind CSS | Flexible, accessible, low-overhead |
| Backend API | Node.js + Express / NestJS (TypeScript) | Consistent language across stack |
| Database | PostgreSQL | Relational, ACID-compliant, ideal for subscriptions and RBAC |
| File Storage | AWS S3 / Azure Blob Storage | Scalable, CDN-compatible, signed URL support |
| CDN | AWS CloudFront / Azure CDN | Fast PDF and video delivery |
| Auth | JWT + Refresh Tokens; Google OAuth (optional) | Stateless, scalable |
| Search | Meilisearch (self-hosted) or Algolia | Fast content search within courses |
| Deployment | Azure Kubernetes Service (AKS) | Aligns with existing infrastructure |
| CI/CD | GitHub Actions | Automated testing and deployment |
| AI (Phase 5) | LangChain + pgvector / Pinecone + OpenAI API | RAG pipeline for PDF Q&A |
| Video (Phase 2) | Cloudflare Stream / AWS Elemental MediaConvert | HLS streaming, cost-effective |

---

## 12. Data & Privacy Considerations

| Area | Requirement |
|------|-------------|
| PII Handling | Store only essential PII (name, email, phone); no Aadhaar/PAN unless required for billing |
| Password Security | Passwords hashed using bcrypt (min rounds: 12) |
| PDF Access Security | PDFs served via signed, time-expiring URLs — never public bucket links |
| Data Residency | Prefer India-region cloud resources for compliance with DPDP Act 2023 |
| Consent | Explicit consent collection during registration for marketing communications |
| Data Retention | Inactive accounts archived after 12 months; permanently deleted after 24 months |
| Admin Audit Logs | All destructive admin actions logged (actor, timestamp, target, reason) |

---

## 13. Assumptions & Constraints

### Assumptions

- Faculty are onboarded by admin; they do not self-register
- Phase 1 subscription assignments are manual (no payment gateway)
- PDF is the only content format in Phase 1 (no PPT, Word, etc.)
- Notes are organized strictly by Day Number within a Subject
- Internet connectivity is available for target users (4G minimum assumed)

### Constraints

- Phase 1 budget limited; self-hosted PDF viewer preferred (PDF.js)
- No live streaming in Phase 1 or Phase 2 (only recorded uploads)
- AI features require LLM API costs — must be gated to paid tiers
- Team is TypeScript/Node.js oriented; avoid introducing unrelated language stacks

---

## 14. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| PDF content piracy / screenshot leaks | High | Medium | Watermark PDFs with member email on-the-fly; disable easy download |
| Faculty not adopting the upload workflow | Medium | High | Intuitive UX; onboarding walkthrough; admin support channel |
| Scope creep in Phase 1 (adding quiz/video early) | High | High | Strict phase gate reviews; feature freeze policy |
| Scalability under exam season traffic spikes | Medium | High | Horizontal pod autoscaling on AKS; CDN caching for static assets |
| AI phase cost overruns (LLM API usage) | Medium | Medium | Token usage limits per user/tier; caching repeated queries |
| Subscription revenue not matching projections | Low | High | Validate pricing with early cohort; introduce referral incentives |

---

## 15. Project Name Suggestions

Choosing the right name is a strategic decision — it shapes the brand, domain availability, SEO, and long-term recall among students. Below are curated suggestions across different positioning angles.

---

### 15.1 Naming Criteria

A good portal name should be:
- **Short** — 1–2 words, easy to type and say
- **Memorable** — students should recall it without effort
- **Available** — .com or .in domain should be registerable
- **Relevant** — conveys learning, exams, or achievement
- **Scalable** — works even when you expand to college entrance exams later

---

### 15.2 Recommended Names

#### 🥇 Top Picks

| Name | Domain Suggestion | Positioning Angle | Why It Works |
|---|---|---|---|
| **PrepSphere** | prepsphere.in | All-in-one prep hub | "Sphere" implies a complete world of preparation; modern, scalable |
| **CrackPath** | crackpath.in | Aspirational / goal-driven | "Crack" is student slang for clearing exams; "Path" implies structured journey |
| **AptaLearn** | aptalearn.in | Subject-rooted (Aptitude) | "Apta" means capable/worthy in Sanskrit; directly ties to Aptitude — the core subject |
| **ScoreNest** | scorenest.in | Achievement-focused | Warm and motivating; implies a safe place to build your score |
| **ExamVault** | examvault.in | Content-rich / resource depth | "Vault" implies a treasure chest of resources; premium feel |

---

#### 🔵 Strong Alternatives

| Name | Domain Suggestion | Positioning Angle |
|---|---|---|
| **RankReady** | rankready.in | Outcome-oriented (rank = result of competitive exams) |
| **StudyMarg** | studymarg.in | Localized (Marg = path in Hindi); connects with Indian students |
| **NitiPath** | nitipath.in | Policy/Governance feel; good for banking + PSC exams |
| **PrepGrid** | prepgrid.in | Structured/systematic; appeals to analytical students |
| **AptaEdge** | aptaedge.in | Combines Aptitude + competitive edge |
| **ClearDeck** | cleardeck.in | "Clear" = exam cleared; "Deck" = prepared and ready |
| **ZealPrep** | zealprep.in | Energy and enthusiasm; good for younger audience |
| **MeritPath** | meritpath.in | Merit-based aspiration; trustworthy and professional |

---

#### 🟢 Domain-First Short Names (if .com matters)

| Name | Domain | Note |
|---|---|---|
| **Aptara** | aptara.in / .com | Sounds like a proper brand; root in Aptitude |
| **Prepva** | prepva.in | Short, clean, techy feel |
| **Crackit** | crackit.in | Action-driven; high recall |
| **Znotes** | znotes.in | Simple, notes-first positioning for Phase 1 |
| **Markr** | markr.in | Modern, minimalist; marks + marker |

---

### 15.3 Name-to-Brand Fit Matrix

| Name | Student Appeal | Faculty Trust | Premium Feel | Domain Ease | Scalable to Entrance Exams |
|---|---|---|---|---|---|
| PrepSphere | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| CrackPath | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| AptaLearn | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| ScoreNest | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| ExamVault | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

### 15.4 Recommendation

> **Top Recommendation: `PrepSphere`** — universally readable, exam-agnostic (scales to banking, PSC, and college entrance without rebrand), feels modern and trustworthy, and the `.in` domain is highly likely to be available.
>
> **Budget/startup feel: `CrackPath`** — highest recall among students; very aligned with how aspirants talk about exams ("crack the exam").
>
> **If rooted in your core subject: `AptaLearn`** — the Sanskrit root "Apta" (capable) combined with Aptitude makes it unique, culturally resonant, and professional.

**Next Step:** Verify domain availability on [GoDaddy.in](https://www.godaddy.com) or [Namecheap](https://www.namecheap.com) before finalizing.

---

## 16. Glossary

| Term | Definition |
|------|------------|
| BRD | Business Requirements Document |
| RBAC | Role-Based Access Control |
| MVP | Minimum Viable Product |
| SSC CGL | Staff Selection Commission – Combined Graduate Level |
| IBPS | Institute of Banking Personnel Selection |
| SBI PO | State Bank of India Probationary Officer |
| RBI Grade B | Reserve Bank of India Grade B Officer |
| PSC | Public Service Commission (State Level) |
| EAMCET | Engineering, Agriculture & Medical Common Entrance Test |
| ECET | Engineering Common Entrance Test |
| POLYCET | Polytechnic Common Entrance Test |
| JEE | Joint Entrance Examination |
| CAT | Common Admission Test (IIMs) |
| RAG | Retrieval-Augmented Generation (AI technique) |
| HLS | HTTP Live Streaming (video format) |
| DPDP Act | Digital Personal Data Protection Act, India 2023 |
| JWT | JSON Web Token |
| CDN | Content Delivery Network |
| AKS | Azure Kubernetes Service |

---

*Document Version 1.1 | Competitive Exam Prep Portal | Prepared: May 2026*
*Next Step: Stakeholder Review → Project Name Finalization → Sign-off → Technical Design Document (TDD)*
