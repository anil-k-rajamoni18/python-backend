# .github/prompts — SRE Prompt Library

Reusable AI prompt files for daily SRE work. Compatible with GitHub Copilot Chat, Claude, or any assistant supporting `.prompt.md` files.

## My Setup
- **Role**: SRE Engineer
- **Responsibilities**: Vulnerability remediation · CI/CD pipeline health (One Pipeline) · Cloud infra (AWS/Azure/GCP) · Secret rotation & compliance · Incident response & on-call
- **Tools**: Slack · Jira · One Pipeline · Secure Guardians · ETIP · Ozone · QuickSight · Confluence

---

## Prompt Files

| File | Purpose | Use When |
|------|---------|----------|
| `sre-daily-tasks.prompt.md` | Morning checklist — pipeline health, vuln triage, secret health, cloud infra | Every morning, start of shift |
| `slack-message-composer.prompt.md` | 9 Slack templates for SLA alerts, escalations, incidents, FYIs | Before posting anything to the team |
| `scrum-standup-generator.prompt.md` | Convert raw task notes → clean daily standup (verbal or Slack) | Before daily standup |
| `vuln-triage-jira-tickets.prompt.md` | Prioritize findings (P0–P4), generate Jira tickets for all vuln types | Processing new vuln batches from Secure Guardians |
| `incident-response-comms.prompt.md` | Incident Slack comms, status updates, post-mortem/PIR template | During and after incidents |

---
# GitHub Copilot Prompt Files Setup Guide

## 1. Add Prompt Files to Your Repository

Place the prompt files in your repository root under the exact folder structure:

```text
your-repo/
└── .github/
    └── prompts/
        ├── sre-daily-tasks.prompt.md
        ├── slack-message-composer.prompt.md
        ├── scrum-standup-generator.prompt.md
        ├── vuln-triage-jira-tickets.prompt.md
        └── incident-response-comms.prompt.md
```

---

# 2. Install GitHub Copilot Extension

If not already installed:

- Open the **Extensions** sidebar in VS Code
- Search for:
  
```text
GitHub Copilot
```

- Install the extension

---

# 3. Open Copilot Chat

You can open Copilot Chat using:

```text
Ctrl + Shift + I
```

Or:
- Click the Copilot Chat icon in the VS Code sidebar

---

# Daily Usage — Attach a Prompt File

## 4. Attach Context

Inside the Copilot Chat input box:

- Click the **paperclip icon** (Attach context)

---

## 5. Select Prompt File

Choose:

```text
Prompt file...
```

from the menu.

---

## 6. Pick the Appropriate Prompt File

Navigate to:

```text
.github/prompts/
```

Select the prompt file based on your task:

| Prompt File | Usage |
|---|---|
| `sre-daily-tasks.prompt.md` | Morning triage, pipeline checks |
| `slack-message-composer.prompt.md` | Writing Slack messages |
| `scrum-standup-generator.prompt.md` | Daily scrum/standup updates |
| `vuln-triage-jira-tickets.prompt.md` | Secure Guardians / vulnerability triage |
| `incident-response-comms.prompt.md` | Incident communication updates |

---

# 7. Start Using Copilot

Now simply type your task or notes.

Example:

```text
done: triaged 5 container vulns, rotated 2 secrets,
fixed pipeline on auth-service.
today: eol review.
no blockers
```

Copilot will automatically:
- read the attached prompt file
- understand the context
- generate a clean formatted response

Example outputs:
- standup updates
- Slack messages
- Jira comments
- incident communications

---

# Important Note

The prompt file remains attached for the entire chat session.

You do NOT need to re-attach it between messages unless:
- you start a new session
- you want to switch to a different prompt context

---

## Quick Usage

### Standup (fastest daily use)
Paste `scrum-standup-generator.prompt.md` into Claude, then:
> "Done: triaged 5 container vulns, rotated 2 secrets, fixed pipeline failure on auth-service. Today: EOL review, config compliance sweep. Blockers: none."

Get a clean Slack standup post in seconds.

### Slack Message
Paste `slack-message-composer.prompt.md`, then:
> "Write me a message for a SAST block on payments-service, Jira ticket PAY-1234, dev owner is @alice"

### Jira Ticket
Paste `vuln-triage-jira-tickets.prompt.md`, then:
> "Container finding: checkout-service, image node:16, 3 critical CVEs, 28 days old, SG ticket #4521"

---

## SLA Quick Reference

| SLA | Vulnerability Types |
|-----|---------------------|
| 🔴 Resolve ASAP | CONFIG COMPLIANCE |
| 🔴 Blocks release | SAST / CHECKMARX |
| 🔴 Every 90 days | SECRET ROTATION |
| 🟠 30-day window | CONTAINERS, IMAGE FINDINGS |
| 🟠 Continuous | SCA / MEND |
| 🟡 Per EOL date | EOL SOFTWARE |
| 🟡 90-day lead | ETBS |
| 🟢 Monitor weekly | API DORMANCY |
| 🟢 Annual minimum | DAST |
| 🟢 100% target | SCA/SAST ONBOARDING |

---



## Contributing
When you discover new team conventions, tool changes, or channel names — update the relevant prompt file. Keep everything grounded in actual SLAs and tools from this org.
