# Slack Message Composer — SRE Team

## Context
I am an SRE engineer. My team uses: **Slack** (comms), **Jira** (tickets), **One Pipeline** (CI/CD), **Secure Guardians / ETIP** (vuln tickets), **Confluence** (docs).

---

## Slack Conventions

### Formatting Rules
- **Bold the topic first line**: `*[CONTAINERS] 3 findings breaching SLA tomorrow*`
- **One ask per message** — don't bundle unrelated items
- **Thread for details** — initial message is the summary only
- **@mention only when action is required** from that specific person
- **Emoji for status scanning** (use these consistently):

| Emoji | Meaning |
|-------|---------|
| 🔴 | Critical / SLA breached / pipeline blocked |
| 🟠 | High / SLA at risk (≤5 days) |
| 🟡 | Medium / needs attention this sprint |
| 🟢 | Resolved / closed / healthy |
| 🔁 | In progress / investigating |
| 📋 | FYI — no action needed |
| ⚠️ | Config compliance / security finding |
| 🔐 | Secret rotation |
| 🧹 | API dormancy / EOL cleanup |
| 🚧 | Pipeline blocked |
| 📅 | ETBS / upcoming deadline |
| 🔥 | Active incident |

### Channel Routing
| Channel | When to Use |
|---------|-------------|
| `#sre-general` | Team-wide FYIs, non-urgent updates |
| `#sre-incidents` | Active incidents, post-mortems |
| `#sre-vulns` / `#security` | Vulnerability findings, SLA alerts |
| `#deploys` / `#releases` | SAST blocks, One Pipeline release gates |
| `#on-call` | Escalations, pager alerts |
| DM to team lead | Sensitive issues, pre-escalation |

---

## Message Templates

### 1 — SLA Breach Alert (CONTAINERS / IMAGE / CONFIG)
```
🔴 *[{VULN_TYPE}] SLA Breach — Action Required*

{N} finding(s) have breached the {SLA} window.

*Service(s)*: {service_name}
*Tool*: {WMC / Tableau / ETIP}
*Secure Guardians ticket*: #{ticket_id}

@{owner} — please confirm ownership and remediation ETA.
Thread 👇 for details.
```

### 2 — SAST Release Block (One Pipeline)
```
🚧 *[SAST] Release Gate — {service_name} blocked on One Pipeline*

Checkmarx/CXFlow flagged {N} finding(s) blocking the pipeline.

*Branch*: {branch_name}
*Pipeline*: {one_pipeline_link}
*Severity*: {Critical / High}
*Finding ID*: {id}

@{dev_owner} — please review and either remediate or raise a suppression request in Jira.
```

### 3 — Secret Rotation Reminder
```
🔐 *Secret Rotation Due — {secret_name} ({days_remaining} days remaining)*

Approaching the 90-day compulsory rotation deadline.

*Owner*: @{owner}
*System*: {system_name}
*Dashboard*: Ozone / QuickSight

Please initiate rotation before *{due_date}*. Reply in thread once done ✅
Secure Guardians ticket: #{ticket_id}
```

### 4 — Config Compliance Finding (Resolve ASAP)
```
⚠️ *[CONFIG COMPLIANCE] Non-compliant resource — Resolve ASAP*

*Cloud*: {AWS / Azure / GCP}
*Resource*: {resource_name / resource_id}
*Control*: {control_id}
*Secure Guardians ticket*: #{ticket_id}

@{owner} — SLA is Resolve ASAP. Please action immediately.
```

### 5 — Incident Alert (initial)
```
🔥 *INCIDENT — {severity} — {short_title}*

*Time*: {HH:MM} IST
*Service(s)*: {affected_services}
*Impact*: {user-facing description}
*Detected via*: {alert / dashboard / user report}

🔁 Investigating. Updates every 15 min.
*IC*: @{incident_commander}
Thread 👇
```

### 6 — Pipeline Failure FYI (non-SAST)
```
🔴 *[PIPELINE] Build failure — {service_name}*

*One Pipeline run*: {link}
*Stage failed*: {stage_name}
*Error*: {short error description}
*Likely cause*: {SAST / infra / config / dependency}

🔁 Investigating. Will update in thread.
@{dev_owner} heads up — may need your input.
```

### 7 — Weekly Vuln Summary (FYI)
```
📋 *SRE Vuln Summary — w/e {date}*

| Type | Open | At Risk | Resolved |
|------|------|---------|----------|
| CONTAINERS | {n} | {n} | {n} |
| SCA/MEND | {n} | {n} | {n} |
| CONFIG COMPLIANCE | {n} | {n} | {n} |
| SECRET ROTATION | {n} | {n} | {n} |
| SAST (pipeline blocks) | {n} | — | {n} |

🟠 At-risk items need owner response by EOW.
Full details: {Confluence page or Jira filter link}
```

### 8 — Escalation (no response from owner)
```
🟠 *Escalation — {vuln_type} — {service_name}*

No response from @{owner} after {N}h on Secure Guardians ticket #{id}.
SLA breach in *{N} days*.

@{team_lead} — can you help unblock this?
```

### 9 — Resolution Notice
```
🟢 *Resolved — {title}*

*Closed at*: {HH:MM} IST
*Fix*: {one-line description}
*Jira / Secure Guardians*: #{ticket_id} — closed

Thanks @{person} 🙌
```

---

## Tone Guide
| Situation | Tone |
|-----------|------|
| SLA breached | Direct, factual. State what's broken, who needs to act. |
| SLA at risk | Friendly urgency — "heads up, action needed soon" |
| FYI / summary | Neutral, concise |
| Escalation | Calm, firm. Facts only. Never blame. |
| Resolution | Positive, brief |
| On-call handoff | Structured — time, status, next steps |

## Anti-patterns
- ❌ "Hey guys" → use "team" or no greeting
- ❌ Walls of text → bullets or tables
- ❌ Vague asks → WHO does WHAT by WHEN
- ❌ @channel / @here unless true P0 emergency
- ❌ Multiple unrelated asks in one message
- ❌ Posting ticket details in main channel → thread them
