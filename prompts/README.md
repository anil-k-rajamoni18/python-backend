# .github/prompts — SRE Prompt Library

This directory contains reusable prompt files for daily SRE workflows. Use these with GitHub Copilot Chat, Claude, or any AI assistant that supports `.prompt.md` files.

## Prompt Files

| File | Purpose | When to Use |
|------|---------|-------------|
| `sre-daily-tasks.prompt.md` | Morning triage, SLA checks, vulnerability prioritization | Every morning / ad hoc during shift |
| `slack-message-composer.prompt.md` | Craft Slack messages for SLA alerts, escalations, FYIs | Whenever you need to post to the team |
| `scrum-standup-generator.prompt.md` | Convert task notes into standup updates | Before daily standup / async post |
| `vuln-triage-jira-tickets.prompt.md` | Prioritize findings, generate Jira tickets, suppression requests | When processing new vulnerability batches |
| `incident-response-comms.prompt.md` | Incident Slack updates, post-mortem template, security incidents | During and after incidents |

---

## Quick Usage

### In VS Code with GitHub Copilot:
Attach the relevant prompt file to your Copilot Chat context, then describe your task.

### With Claude:
Paste the relevant prompt file content at the start of your conversation, then provide your specific task inputs.

### Example — Standup:
1. Open `scrum-standup-generator.prompt.md`
2. Paste into Claude
3. Then type: *"Done: triaged 5 container vulns, rotated 2 secrets. Today: EOL review for NodeJS services. Blockers: none."*
4. Get a clean standup in seconds.

---

## Vulnerability Types Quick Reference

| SLA | Types |
|-----|-------|
| Resolve ASAP | CONFIG COMPLIANCE |
| Blocks release | SAST / CHECKMARX |
| 30-day window | CONTAINERS, IMAGE FINDINGS |
| Every 90 days | SECRET ROTATION |
| Continuous | SCA / MEND |
| Monitor weekly | API DORMANCY |
| Per EOL date | EOL SOFTWARE |
| 90-day lead | ETBS |
| 100% target | SCA/SAST ONBOARDING |
| Annual minimum | DAST |

---

## Contributing

When you discover new patterns or team conventions, update the relevant prompt file. Keep templates grounded in actual SLAs and tool names from this org.
