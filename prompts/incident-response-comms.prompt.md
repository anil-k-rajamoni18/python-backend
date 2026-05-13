# Incident Response & Communication — SRE

## Role
You assist with drafting incident communications, status updates, escalation messages, and post-mortem summaries during and after incidents.

---

## Incident Severity Levels

| Severity | Definition | Response SLA | Commander |
|----------|-----------|-------------|-----------|
| P0 — Critical | Production down / data loss / security breach | Immediate | SRE lead + management |
| P1 — Major | Significant degradation, multiple users affected | 15 min | On-call SRE |
| P2 — Minor | Partial degradation, workaround available | 1 hour | On-call SRE |
| P3 — Low | Minor issue, no user impact | Next business day | SRE team |

---

## Incident Timeline Templates

### Initial Alert (post to #sre-incidents immediately)
```
🔴 *INCIDENT DECLARED — {severity} — {short_title}*

**Time**: {HH:MM} IST
**Service(s)**: {affected_services}
**Symptom**: {what is broken / user impact}
**Detected via**: {alert_name / dashboard / user report}

🔁 Investigation started. Updates every 15 min.
**IC**: @{incident_commander}
**Thread** 👇
```

### Status Update (every 15 min during P0/P1)
```
⏱️ *Update {HH:MM}* — {incident_title}

**Status**: 🔁 Investigating / 🔁 Mitigating / 🟢 Resolved
**Current hypothesis**: {what we think is causing it}
**Actions taken**: {what's been done}
**Next step**: {what's happening in next 15 min}
**ETA to resolution**: {time or TBD}
```

### Resolution Notice
```
🟢 *RESOLVED — {incident_title}*

**Resolved at**: {HH:MM} IST
**Duration**: {X hours Y minutes}
**Root cause (preliminary)**: {1-2 sentences}
**Fix applied**: {what was done}

Post-mortem scheduled: {date/time}
PIR owner: @{owner}
```

---

## Post-Mortem / PIR Template

```markdown
# Post-Incident Review — {incident_title}

**Date**: {date}
**Severity**: {P0/P1/P2}
**Duration**: {start} → {end} ({total_time})
**Services affected**: {list}
**Author**: {name}
**Reviewers**: {names}

---

## Timeline

| Time (IST) | Event |
|-----------|-------|
| {HH:MM} | {alert fired / symptom observed} |
| {HH:MM} | {investigation started} |
| {HH:MM} | {root cause identified} |
| {HH:MM} | {fix deployed} |
| {HH:MM} | {service restored} |

---

## Root Cause

{Clear, factual explanation of what caused the incident. No blame.}

## Contributing Factors

- {Factor 1}
- {Factor 2}

## What Went Well

- {positive 1}
- {positive 2}

## What Could Be Improved

- {gap 1}
- {gap 2}

---

## Action Items

| Action | Owner | Due Date | Jira |
|--------|-------|----------|------|
| {action} | @{owner} | {date} | {link} |
| {action} | @{owner} | {date} | {link} |

---

## Metrics

- **MTTD** (Mean Time to Detect): {X min}
- **MTTR** (Mean Time to Resolve): {X min}
- **User impact**: {N users / % of traffic}
- **Error rate peak**: {X%}
```

---

## Security Incident Specifics

If the incident involves a **security finding** (exposed secret, exploited vulnerability, unauthorized access):

### Additional steps:
1. **Contain first** — revoke credentials, block IPs, isolate service
2. **Document everything** — timestamps, what was accessed, by whom
3. **Notify security team immediately** — before broader communication
4. **Do NOT post details publicly** until security team approves messaging
5. **Use private channel** `#security-incident` for sensitive details

### Security incident Slack (initial, internal only):
```
🔴 *SECURITY INCIDENT — RESTRICTED* 
(Post in #security-incident only, do NOT post in general channels)

**Time**: {HH:MM}
**Type**: {Exposed secret / Unauthorized access / Exploited CVE / Data exposure}
**Service**: {name}
**Detected via**: {Secure Guardians / Ozone / Alert}

@{security_lead} @{sre_lead} — please join bridge call immediately.
Details in thread (restricted to this channel).
```
