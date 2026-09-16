# Minutes of Meeting — Office Hours: ETB 2440

**Date:** September 16
**Session:** ETB 2440 Office Hours (CAR AutoSchedule / ETB team)
**Attendees mentioned:** Joe, Akash, Sandeep, Shalom, PFC platform team representative (Mark and Ravnid signed up but did not attend)

---

## 1. Library Packages — Temporary ETB Exclusion Confirmed

**Question raised:** PFC platform team owns components that are all **library packages** — published as artifacts for downstream consumers (SDKs, wrappers, compilation checks) on an opt-in basis. These never go to production. Are they in scope for the ETB?

**Response:**
- A link to the **approved exclusions list** was shared in chat — this document is updated frequently (at least weekly).
- **Library package flavor currently has a temporary ETB-level exclusion.**
- This is **temporary only** — the team is actively working to incorporate library packages and remove roadblocks. Compliance will be required at some point in the future.

**Follow-up on what compliance will look like once the exclusion ends:**
- It is a **rolling seven-day window**, not "four times a month." Every seven days, a deployment is expected.
- **Deployment is required even with no code changes.**

## 2. What the ETB Actually Checks

Clarified during the session:
- **Only the Docker image version is checked.** Specifically, the golden images published to the **gold image dashboard**.
- **No OS-level checks currently exist.** The team confirmed after reviewing the JIRA/compliance doc that there is nothing about OS version checks in the current criteria — earlier mention of an OS check appears to have been edited out of the doc.
- OS-level checks may be implemented in the future, but nothing is confirmed at this time.

**Practical takeaway:** Keeping Docker images current with the latest available golden image, plus deploying on a rolling seven-day cadence, is what satisfies the ETB today.

## 3. CAR Auto-Schedule for Non-PAR Components — Timeline Update

**Question raised (Sandeep):** All PAR-eligible repos are onboarded. When will CAR auto-schedule be enabled for **non-PAR / non-prod components**? Is there an ETA?

**Response:**
- This work is **active and in progress** — the responder is personally working on it.
- It requires **JPL changes**, which must go through the **JPL team's approval process**.
- Documentation was being wrapped up that same day to send to the JPL team.
- Normally this process takes **1–2 months** for a full cycle, but due to the **severity/priority of the ETB**, an expedited/streamlined path has been indicated.
- **Goal: complete within one sprint — implemented, tested, and available to users by end of month.**
- **Caveat:** This is a goal, not a commitment — the approval dependencies mean the timeline can't be guaranteed.

## 4. Why Onboarded Repos Haven't Triggered Builds

**Question raised (Sandeep):** Repos are onboarded to CAR auto-schedule but builds haven't triggered. Are there rules governing this?

**Three things to check:**
1. **Trex pause (Sept 8–15)** — all releases were paused during this window. Releases resumed the previous day. Depending on which train a repo is in, a release should appear within the next day or two.
2. **Check whether the schedule is paused** — paused schedules will not run. If nothing appears by tomorrow, reach out to the team to verify pause status.
3. **Human commits** — if there's been a human commit in the last week, the repo may go through a manual PAR release path.

**Important additional rule clarified by Akash:**
> For CAR auto-schedule to pick up a repo, there must be a **successful production release within the past 30 days.**

## 5. How to Confirm CAR Auto-Schedule Triggered a Build

**Question raised (Sandeep):** Some onboarded repos have Slack notifications configured and some don't. For those without, how can we tell whether a build was triggered by CAR auto-schedule?

**Response:**
- **Slack notification is the only mechanism available** for this.
- Recommendation: **opt in to Slack notifications for all onboarded repos** via **DevNav Hub** — the existing onboarding config can be updated to add the Slack channel ID, after which alerts will be received on build triggers.
- No alternative detection method exists at this time.

## 6. Detecting Failed Main Builds / Dashboard Discrepancy

**Question raised (Shalom):** How do we detect failed main builds for repos that are in scope but non-compliant? Also, a discrepancy was observed — the dashboard showed "days since last valid deploy" as ~34 weeks, while the pipeline showed builds completing through to the final stage.

**Clarifications provided:**
- A build must be **fully successful and deployed** to count toward ETB compliance. A failed build does not count.
- On the specific example raised: the pipeline was reaching the "check production" stage and then **being aborted** — an aborted deployment would not count as a valid deploy.
- Discussion noted that for a **pre-production repo** (never deployed to prod), the check looks at non-prod deployments. However, **if a repo has ever deployed to prod, the ETB will look for a prod deployment.**
- **Resolution:** On re-checking the dashboard (refreshed that morning), the September 14 deployment **was** in fact now counted as a valid deploy. The discrepancy was a **dashboard timing/staleness issue**, not a compliance failure.

**Dashboard refresh cadence clarified:**
- The **ETB dashboard (QuickSight) refreshes every morning, roughly 7–8 AM.**
- A separate dashboard referenced is **not** updated daily; the team is working to move it to a daily cadence.
- Guidance: always confirm you're viewing the most current version before raising a discrepancy. The exact refresh timing will be double-checked by the ETB team.

---

## Action Items

| # | Action | Owner |
|---|--------|-------|
| 1 | Review the approved exclusions list (link shared in chat) to confirm which components qualify | Each team |
| 2 | Plan for library packages to eventually come into scope — exclusion is temporary | PFC platform team |
| 3 | Complete JPL documentation and submit to JPL team for expedited approval (non-PAR auto-schedule enablement) | ETB/CAR team — target end of month |
| 4 | Verify onboarded repos are not paused; check for human commits requiring a manual deployment | Sandeep |
| 5 | Opt in to Slack build notifications via DevNav Hub for all onboarded repos missing them | Sandeep |
| 6 | Confirm each in-scope repo has a successful prod release within the past 30 days (required for auto-schedule pickup) | Each team |
| 7 | Verify dashboard refresh timing and confirm compliance status against the latest refresh before escalating discrepancies | ETB team / all teams |

---

## Key Takeaways
- **Only the Docker image version is checked** for ETB compliance today — no OS-level checks currently in place.
- **Library packages are temporarily excluded**, but this will not last — plan for eventual compliance.
- **Non-PAR auto-schedule support is actively being built**, targeting end of month, though the JPL approval dependency means it isn't guaranteed.
- **A successful prod release in the last 30 days is a prerequisite** for CAR auto-schedule to pick up a repo — worth verifying across our onboarded repos.
- **Dashboard staleness can create false non-compliance signals** — always check against the latest morning refresh before investigating.

---
*Note: Some speaker attributions are inferred from context due to overlapping audio in the source recording; please verify before wider distribution.*
