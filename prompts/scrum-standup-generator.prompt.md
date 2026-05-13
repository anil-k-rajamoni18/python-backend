# Scrum Standup Generator — SRE Daily Standup

## Context
- **Cadence**: Daily standup only (no sprint planning/retro in this prompt)
- **Role**: SRE — covering vulns, pipelines, cloud infra, secret rotation, incidents
- **Tools**: Jira (tickets), One Pipeline (CI/CD), Secure Guardians, ETIP, Ozone, Slack

---

## How to Use This Prompt

Paste your raw notes in any format — I'll convert them into a clean standup update.

**Example input (freeform dump):**
> "yesterday fixed sast block on payments service, rotated 2 secrets expiring this week, investigated a container vuln ticket. today doing eol review and checking config compliance findings. waiting on dev team to confirm suppression approval"

**Example input (bullet dump):**
```
done: sast block resolved on payments, 2 secrets rotated, 5 container vulns triaged
today: eol review, config compliance sweep
blocked: suppression approval pending from dev team
```

---

## Output Formats

### Format A — Verbal Standup (speak aloud, ~45 seconds)
```
Yesterday:
• {verb} {what} — {outcome if relevant} [{TAG}]
• {verb} {what} [{TAG}]

Today:
• {verb} {what} [{TAG}]
• {verb} {what}

Blockers:
• {blocker} / None
```

### Format B — Slack Standup Post
```
*🗓️ {Day, Date} Standup*

✅ *Done*
• {action} [{TAG}]
• {action} [{TAG}]

🔁 *Today*
• {action} [{TAG}]
• {action}

🚧 *Blockers*
• {blocker} / None
```

---

## Work Area Tags

Always include the relevant tag when referencing SRE work:

| Work Area | Tag |
|-----------|-----|
| Container image vulns | `[CONTAINERS]` |
| Open source / library vulns | `[SCA]` |
| Code scan / static analysis | `[SAST]` |
| Dynamic attack simulation | `[DAST]` |
| Base image findings | `[IMAGE]` |
| Cloud config non-compliance | `[CONFIG]` |
| Credential rotation | `[SECRET-ROTATION]` |
| Unused API cleanup | `[API-DORMANCY]` |
| Framework end-of-life | `[EOL]` |
| Tech backlog compliance | `[ETBS]` |
| Scan coverage gaps | `[ONBOARDING]` |
| One Pipeline build/deploy | `[PIPELINE]` |
| Active incident | `[INCIDENT]` |
| On-call / pager | `[ON-CALL]` |
| Cloud infra (AWS/Azure/GCP) | `[INFRA]` |

---

## Writing Rules

- **Lead with a strong verb**: Triaged / Resolved / Rotated / Escalated / Reviewed / Unblocked / Deployed / Investigated / Closed / Raised / Updated
- **Never say "worked on"** — say what was accomplished or the specific action taken
- **Include outcome if time-sensitive**: "within SLA" / "SLA breach avoided" / "pipeline unblocked"
- **One line per bullet** — no sub-bullets
- **Incomplete items**: "Continuing {X}" not "Tried to do X"
- **Blockers must name**: WHO is blocking, WHAT is needed, and WHEN you need it

---

## Examples

### Example 1 — Vuln-heavy day
**Input**: "triaged container vulns, raised sast suppression for checkout service, rotated 3 secrets, escalated a config compliance finding that had no owner. today: eol dashboard review, follow up on yesterday's escalation. blocked on dev team approving suppression"

**Output:**
```
*🗓️ Tuesday, 13 May Standup*

✅ *Done*
• Triaged 7 container vulns — 3 escalated to service owners [CONTAINERS]
• Raised SAST suppression request for checkout-service in Jira [SAST]
• Rotated 3 secrets approaching 90-day deadline [SECRET-ROTATION]
• Escalated unowned config compliance finding to team lead [CONFIG]

🔁 *Today*
• EOL dashboard review for SpringBoot/NodeJS services [EOL]
• Follow up on config compliance escalation [CONFIG]

🚧 *Blockers*
• Waiting on dev team to approve SAST suppression — needed before checkout-service can release
```

### Example 2 — Pipeline + incident day
**Input**: "resolved an overnight incident - api gateway latency. fixed pipeline failure on auth service (it was a missing secret). today continuing post-mortem write-up and checking for more dormant apis. no blockers"

**Output:**
```
*🗓️ Tuesday, 13 May Standup*

✅ *Done*
• Resolved overnight API gateway latency incident — root cause identified, service restored [INCIDENT]
• Fixed One Pipeline failure on auth-service — missing secret injected via Ozone [PIPELINE][SECRET-ROTATION]

🔁 *Today*
• Writing post-mortem for API gateway incident [INCIDENT]
• Weekly API dormancy review in QuickSight [API-DORMANCY]

🚧 *Blockers*
• None
```

### Example 3 — Cloud infra focus day
**Input**: "reviewed etip gap report for sca/sast onboarding, found 4 services not yet onboarded. also checked azure config compliance - 2 new findings. today: onboarding tickets in jira for the 4 services, and a cloud infra review for gcp quota. blocked waiting on gcp access"

**Output:**
```
*🗓️ Tuesday, 13 May Standup*

✅ *Done*
• Reviewed ETIP gap report — identified 4 services not onboarded to SCA/SAST scanning [ONBOARDING]
• Triaged 2 new Azure config compliance findings in Ozone — owners notified [CONFIG]

🔁 *Today*
• Raise Jira tickets for 4 unboarded services to get onto SCA/SAST [ONBOARDING]
• GCP infra quota review [INFRA]

🚧 *Blockers*
• GCP access pending — need @{name} to provision role before infra review can proceed
```

---

## Quick-fire Mode

If I just give you a one-liner like:
> "standup: rotated secrets, reviewed vulns, fixed pipeline, checking eol today, no blockers"

Generate a clean Slack standup post without asking for more details. Make reasonable assumptions about specifics and use appropriate tags.
