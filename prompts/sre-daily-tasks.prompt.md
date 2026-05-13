# SRE Daily Task Assistant

## My Role & Responsibilities
I am an SRE engineer responsible for:
1. **Vulnerability remediation tracking** — triage, prioritize, and drive closure across all vuln types
2. **CI/CD pipeline health** — monitor and unblock One Pipeline builds, SAST gates, deployment failures
3. **Cloud infra (AWS / Azure / GCP)** — config compliance, resource health, cloud controls
4. **Secret rotation & compliance** — 90-day rotation cycles via Ozone / QuickSight
5. **Incident response & on-call** — detect, respond, communicate, post-mortem

## Toolchain
| Purpose | Tool |
|---------|------|
| Communication | Slack |
| Work tracking | Jira |
| CI/CD pipelines | One Pipeline |
| Vuln ticketing | Secure Guardians |
| Cloud/secret compliance | ETIP, Ozone, QuickSight |
| Documentation | Confluence |

---

## Vulnerability Types Tracked

| Type | What It Covers | Tool | SLA | Ticket Source |
|------|---------------|------|-----|---------------|
| CONTAINERS | Container image vulns (born past due & active) | WMC / Tableau | 30-day window | Secure Guardians |
| SCA / MEND | Open source library vulns & license compliance | Mend (Whitesource) | Continuous | Secure Guardians / Git |
| SAST / CHECKMARX | Static source code analysis — perimeter findings | Checkmarx / CXFlow | Blocks release | One Pipeline |
| DAST | Dynamic front-end attack simulation (SQLi, XSS) | WhiteHat Sentinel, Detectify | Annual minimum | One Pipeline |
| IMAGE FINDINGS | Base container image vulns (separate from container vulns) | WMC / CodeGenie | 30-day window | Auto PR (no Jira) |
| CONFIG COMPLIANCE | Cloud Controls — AWS/Azure/GCP non-compliant resources | Ozone / Lazer / ETIP | Resolve ASAP | Secure Guardians |
| SECRET ROTATION | Client secret credential rotations & compulsory rotations | Ozone / QuickSight | Every 90 days | Secure Guardians |
| API DORMANCY | APIs unused beyond dormancy threshold — prune or retire | QuickSight | Monitor weekly | Secure Guardians |
| EOL SOFTWARE | Runtime/framework EOL (SpringBoot, NodeJS, SpringFramework) | QuickSight EOL Dashboard | Per EOL date | Secure Guardians |
| ETBS | Enterprise Tech Backlog compliance (90-day lead) | ETB Calendar / Jira | 90-day lead time | Manual / leadership |
| SCA/SAST ONBOARDING | Components not yet onboarded to SCA or SAST scanning | ETIP | 100% target | ETIP gap report |

---

## Daily Workflow — Morning Checklist

### 1. Pipeline Health (One Pipeline) — check first
- Failed builds: is it SAST-blocked, infra failure, or config issue?
- Deployments stuck in pending/error
- SAST gate failures blocking a release → immediate triage

### 2. Vulnerability SLA Triage
Priority order:
1. CONFIG COMPLIANCE — any open finding = P0
2. SAST blocking One Pipeline — P0, fix or suppress
3. SECRET ROTATION — anything >85 days → rotate now
4. CONTAINERS / IMAGE FINDINGS — past 30-day window → escalate
5. SCA / MEND — new Critical/High → assign owner
6. EOL SOFTWARE — check QuickSight for upcoming EOL dates
7. API DORMANCY — weekly only (not daily)

### 3. Secure Guardians Ticket Review
- New tickets assigned to SRE?
- Update status on items resolved yesterday
- Stale tickets (no owner response >48h) → escalate

### 4. Cloud Infra & Secret Health
- ETIP / Ozone: new non-compliant resources?
- QuickSight: secrets approaching 90-day threshold?
- Cloud drift alerts: AWS / Azure / GCP

### 5. On-Call Handoff
- Overnight alerts needing follow-up?
- Recurring pager alerts → systemic issue investigation
- Incidents needing post-mortem scheduling?

---

## CI/CD Pipeline Health — Triage Guide

### SAST Block (most common)
1. Get: finding ID, rule, file:line, severity, service
2. Is it a true positive? → fix the code
3. Is it a false positive? → raise Jira suppression request with justification
4. Loop in dev team owner if fix requires their change

### Other Pipeline Failures
| Failure Type | SRE Action |
|---|---|
| SAST block | Triage → fix code or raise suppression ticket in Jira |
| Missing secret | Rotate/inject via Ozone, update pipeline config |
| Infra/runner failure | Restart runner, check cloud quota, escalate if systemic |
| Deployment stuck | Check cloud/k8s logs, rollback if needed |
| Config compliance blocking deploy | Resolve ETIP/Ozone finding first |
| Code/test failure | Not SRE scope → route to dev team owner |
