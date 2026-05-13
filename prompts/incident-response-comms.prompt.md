# Incident Response & Communication — SRE On-Call

## Context
SRE on-call engineer. Tools: **Slack** (#sre-incidents), **Jira** (action items), **One Pipeline** (pipeline-triggered incidents), **Confluence** (post-mortem storage), **Secure Guardians** (security incidents).

---

## Incident Severity Levels

| Severity | Definition | Response Time | Who to Loop In |
|----------|-----------|--------------|----------------|
| P0 — Critical | Production down / data loss / security breach | Immediate | SRE lead + management |
| P1 — Major | Significant degradation, multiple users affected | 15 min | On-call SRE + team lead |
| P2 — Minor | Partial degradation, workaround exists | 1 hour | On-call SRE |
| P3 — Low | No user impact, background issue | Next business day | SRE team |

---

## Incident Response Phases

### Phase 1 — Detect & Declare (first 5 min)
1. Confirm the incident is real (not a flaky alert)
2. Assess severity (P0–P3)
3. Post initial alert in **#sre-incidents**
4. Assign Incident Commander (IC) — usually the on-call SRE

### Phase 2 — Investigate & Mitigate (ongoing)
1. Identify blast radius — which services/users affected?
2. Check One Pipeline for recent deployments (rollback candidate?)
3. Check Ozone / ETIP for recent config changes
4. Check Secure Guardians for related vuln tickets
5. Post status updates every **15 min** for P0/P1

### Phase 3 — Resolve & Communicate
1. Deploy fix or rollback
2. Verify service restored
3. Post resolution notice in #sre-incidents
4. Notify affected teams

### Phase 4 — Post-Mortem
1. Schedule within 48h of resolution (P0/P1)
2. Write PIR in Confluence
3. Create Jira action items
4. Share summary in #sre-incidents

---

## Slack Message Templates

### Initial Alert — Post in #sre-incidents immediately
```
🔥 *INCIDENT DECLARED — {P0/P1/P2} — {short_title}*

*Time*: {HH:MM} IST
*Service(s)*: {affected_services}
*Impact*: {user-facing description — e.g. "checkout API returning 503"}
*Detected via*: {alert name / dashboard / user report / One Pipeline}

🔁 Investigating. Updates every 15 min.
*IC*: @{incident_commander}
Thread 👇
```

### Status Update — Every 15 min during P0/P1
```
⏱️ *Update {HH:MM}* — {incident_title}

*Status*: 🔁 Investigating / 🔁 Mitigating / 🟢 Resolved
*Hypothesis*: {current best guess at root cause}
*Actions taken*: {what's been done}
*Next step*: {what happens in next 15 min}
*ETA*: {time or TBD}
```

### Resolution Notice
```
🟢 *RESOLVED — {incident_title}*

*Resolved at*: {HH:MM} IST
*Duration*: {X hr Y min}
*Root cause (preliminary)*: {1–2 sentences}
*Fix applied*: {what was done — rollback / config change / secret rotation / etc.}

Post-mortem: {scheduled for date/time}
PIR owner: @{owner}
Confluence draft: {link}
```

### Rollback Decision Message
```
🔁 *Rollback initiated — {service_name}*

Last deploy: {time} by @{deployer} — {commit/PR link}
Rollback to: {previous version}
Pipeline: {one_pipeline_link}

Will confirm restore in thread. @{dev_owner} heads up.
```

---

## Post-Mortem / PIR Template (Confluence)

```markdown
# Post-Incident Review — {incident_title}

**Date**: {date}
**Severity**: {P0/P1/P2}
**Duration**: {start} → {end} ({total time})
**Services affected**: {list}
**Author**: {name}
**Reviewers**: {names}

---

## Summary
{2–3 sentence plain-English summary of what happened, impact, and how it was resolved.}

---

## Timeline

| Time (IST) | Event |
|-----------|-------|
| {HH:MM} | Alert fired / symptom observed |
| {HH:MM} | Incident declared, IC assigned |
| {HH:MM} | Root cause identified |
| {HH:MM} | Fix deployed |
| {HH:MM} | Service restored, incident resolved |

---

## Root Cause
{Clear, factual, blameless explanation of what caused the incident.}

## Contributing Factors
- {Factor 1 — e.g. recent deployment introduced regression}
- {Factor 2 — e.g. no alert for this failure mode}

## What Went Well
- {Positive 1}
- {Positive 2}

## What Could Be Improved
- {Gap 1}
- {Gap 2}

---

## Action Items

| Action | Owner | Due Date | Jira |
|--------|-------|----------|------|
| {action} | @{owner} | {date} | {link} |
| {action} | @{owner} | {date} | {link} |

---

## Metrics

| Metric | Value |
|--------|-------|
| MTTD (Mean Time to Detect) | {X min} |
| MTTR (Mean Time to Resolve) | {X min} |
| User impact | {N users / % of traffic / revenue impact if known} |
| Peak error rate | {X%} |
| Deployments rolled back | {N} |
```

---

## Security Incident — Special Handling

If the incident involves: exposed secret / exploited CVE / unauthorized access / data exposure:

### Rules:
1. **Contain first** — revoke credentials, block IPs, isolate service
2. **Use restricted channel only** — `#security-incident`, NOT #sre-incidents
3. **Notify security team before broader communication**
4. **Do NOT post finding details publicly** until security team approves
5. **Create Secure Guardians ticket** immediately

### Initial message (restricted channel only):
```
🔴 *SECURITY INCIDENT — RESTRICTED*
(Post ONLY in #security-incident)

*Time*: {HH:MM} IST
*Type*: {Exposed secret / Unauthorized access / Exploited CVE / Data exposure}
*Service*: {name}
*Detected via*: {Secure Guardians / Ozone / alert / user report}

@{security_lead} @{sre_lead} — please join bridge immediately.
Containment steps in thread (restricted to this channel).
```

---

## Pipeline-Triggered Incidents

When One Pipeline deployment causes a prod incident:

1. **Check**: what changed in the last deploy? (commit, config, secrets)
2. **Decide**: fix-forward or rollback?
   - Rollback if: unknown root cause, data risk, >30 min to fix
   - Fix-forward if: clear bug, fix is ready, rollback would cause data loss
3. **Communicate**: post in #sre-incidents AND #deploys
4. **Jira**: create incident ticket linked to the pipeline run
5. **Post-mortem**: include "deployment process" as a contributing factor if relevant
