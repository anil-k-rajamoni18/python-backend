# Vulnerability Triage & Jira Ticket Generator

## Context
SRE engineer using: **Jira** (tickets), **Secure Guardians** (vuln source), **One Pipeline** (CI/CD), **ETIP / Ozone** (cloud & secret compliance).

---

## SLA Reference — Priority Decision Table

| Type | SLA | Breached = | At Risk = |
|------|-----|-----------|-----------|
| CONFIG COMPLIANCE | Resolve ASAP | P0 immediately | P0 (always) |
| SAST / CHECKMARX | Blocks release | P0 — pipeline blocked | P0 if release pending |
| SECRET ROTATION | Every 90 days | P0 if >90d | P1 if 85–90d |
| CONTAINERS | 30-day window | P1 | P2 if ≤5d remaining |
| IMAGE FINDINGS | 30-day window | P1 | P2 if ≤5d remaining |
| SCA / MEND | Continuous | P1 (Critical), P2 (High) | P3 (Medium) |
| EOL SOFTWARE | Per EOL date | P1 | P2 if <30d to EOL |
| ETBS | 90-day lead | P2 | P3 |
| API DORMANCY | Monitor weekly | P3 | P4 |
| DAST | Annual minimum | P3 | P4 |
| SCA/SAST ONBOARDING | 100% target | P3 | P4 |

---

## Prioritization Logic

```
1. CONFIG COMPLIANCE open?         → P0. Act before anything else.
2. SAST blocking One Pipeline?     → P0. Fix or suppression request NOW.
3. SECRET ROTATION >90 days?       → P0. Rotate immediately.
4. SECRET ROTATION 85–90 days?     → P1. Rotate this sprint.
5. CONTAINERS / IMAGE >30 days?    → P1. Escalate to service owner.
6. SCA Critical / High new?        → P1–P2. Assign and track.
7. EOL within 30 days?             → P2. Plan upgrade sprint.
8. Everything else                 → P3–P4. Backlog + monitor.
```

---

## Jira Ticket Templates

### CONTAINERS / IMAGE FINDINGS
```
Title: [CONTAINERS] Remediate {N} vulns — {service_name} — Due {due_date}

Type: Bug
Priority: {P1 / P2}
Labels: containers, vulnerability, sla-tracking
Assignee: {service_owner}
Secure Guardians ref: #{sg_ticket_id}

Description:
{N} container image vulnerabilities identified via WMC/Tableau.

Service: {service_name}
Image: {image_name:tag}
Finding age: {days} days (SLA: 30 days)
Severity breakdown: Critical: {n} | High: {n} | Medium: {n}

CVEs:
- {CVE-ID}: {description} — Fix: upgrade to {version}

Acceptance Criteria:
- [ ] All Critical/High CVEs patched
- [ ] Image rebuilt and redeployed
- [ ] Verified clean in WMC/Tableau dashboard
- [ ] Secure Guardians ticket #{id} closed
```

### SAST Suppression Request
```
Title: [SAST] Suppression Request — {finding_id} — {service_name}

Type: Security Exception
Priority: High
Labels: sast, suppression, checkmarx, one-pipeline
One Pipeline run: {link}

Description:
Requesting suppression of Checkmarx/CXFlow finding blocking release pipeline.

Finding ID: {id}
Rule: {rule_name}
File/Line: {file}:{line}
Severity: {severity}
Branch: {branch}

Justification:
{reason — e.g. "False positive: input is validated upstream at {location}"}

Risk Assessment:
Exploitability: {Low / Medium / High}
Compensating controls: {describe or "none identified"}

Approver required: Security team lead
Pipeline currently blocked: Yes — {link}

Acceptance Criteria:
- [ ] Security lead approval received
- [ ] Finding suppressed in Checkmarx
- [ ] Pipeline unblocked and deployment successful
```

### SECRET ROTATION
```
Title: [SECRET-ROTATION] Rotate {secret_name} — Due {due_date}

Type: Task
Priority: {P0 if >90d | P1 if 85–90d}
Labels: secret-rotation, compliance, ozone
Assignee: {secret_owner}
Secure Guardians ref: #{sg_ticket_id}

Description:
Secret approaching / past the 90-day compulsory rotation deadline.

Secret: {secret_name}
System: {system_name}
Current age: {days} days
Dashboard: Ozone / QuickSight

Rotation Steps:
- [ ] Generate new secret in {vault / system}
- [ ] Update all services consuming this secret
- [ ] Verify no service disruption post-rotation
- [ ] Mark rotated in Ozone dashboard
- [ ] Close Secure Guardians ticket #{id}
```

### CONFIG COMPLIANCE (P0)
```
Title: [CONFIG] Non-compliant resource — {resource_name} — RESOLVE ASAP

Type: Bug
Priority: P0 — Critical
Labels: config-compliance, cloud-controls, {aws/azure/gcp}
Assignee: {resource_owner}
Secure Guardians ref: #{sg_ticket_id}

Description:
Non-compliant cloud resource identified via Ozone / Lazer / ETIP.

Cloud: {AWS / Azure / GCP}
Resource: {resource_id / resource_name}
Control: {control_id} — {control_description}
SLA: Resolve ASAP

Remediation Steps:
{steps — e.g. enable encryption, restrict public access, apply policy}

Acceptance Criteria:
- [ ] Resource brought into compliance
- [ ] Verified clean in Ozone / ETIP dashboard
- [ ] Secure Guardians ticket closed
```

### EOL SOFTWARE
```
Title: [EOL] Upgrade {framework} before EOL — {service_name} — EOL: {date}

Type: Task
Priority: {P1 if <30d | P2 if 30–90d}
Labels: eol, upgrade, {springboot/nodejs/springframework}
Assignee: {service_owner}
Dashboard: QuickSight EOL Dashboard

Description:
Runtime/framework reaching end-of-life. Must upgrade before EOL date to avoid security exposure.

Service: {service_name}
Framework: {framework}
Current version: {version}
EOL date: {date}
Recommended upgrade: {target_version}
Upgrade guide: {link or TBD}

Acceptance Criteria:
- [ ] Service upgraded to {target_version}
- [ ] Tests passing on One Pipeline
- [ ] Deployed to production before {date}
- [ ] Secure Guardians / QuickSight EOL Dashboard updated
```

### SCA/SAST ONBOARDING (ETIP Gap)
```
Title: [ONBOARDING] Onboard {service_name} to SCA/SAST scanning

Type: Task
Priority: P3
Labels: sca-onboarding, sast-onboarding, etip
Source: ETIP gap report

Description:
Service not yet onboarded to SCA or SAST scanning. Target: 100% coverage.

Service: {service_name}
Gap type: {SCA / SAST / Both}
ETIP gap report ref: {ref}

Steps:
- [ ] Onboard to Mend (Whitesource) for SCA
- [ ] Configure Checkmarx/CXFlow in One Pipeline for SAST
- [ ] Verify first scan completes cleanly
- [ ] Update ETIP gap report — service marked as onboarded
```

---

## Escalation Decision Tree

```
Is there a CONFIG COMPLIANCE finding?
  → YES: P0. Notify owner immediately. Jira ticket. Escalate in 24h if no response.

Is SAST blocking One Pipeline release?
  → YES: P0. Fix or raise suppression request before end of day.

Is a secret >85 days old?
  → YES: P1. Assign rotation ticket. Due within 5 days.

Is a CONTAINER/IMAGE finding >25 days old?
  → YES: P2. Assign ticket. Escalate to team lead if no owner.

Has owner not responded to Secure Guardians ticket in 48h?
  → YES: Escalate to team lead via Slack. Tag in ticket. Post in #sre-vulns.

Is severity Critical/High on a new SCA finding?
  → YES: P1–P2. Assign and track in current sprint.

Everything else?
  → P3–P4. Add to Jira backlog. Review weekly.
```
