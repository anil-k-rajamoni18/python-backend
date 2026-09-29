# Minutes of Meeting — Office Hours: ETB 2440

**Date:** September 29
**Session:** ETB 2440 Office Hours
**Attendees mentioned:** Joe, Talyne, Rahul, Zach, Varun, Sandeep, Amit, Morty/Morthy, Alex, Drew (plus other teams on the signup sheet)

---

## 🔴 Headline Update: ETB Deadline Extended by One Month
**The ETB due date has been pushed back to October 30th** (from the original 9/30 deadline). This applies specifically to the ETB dashboard/tracking — confirmed as **not** applicable to a separately referenced item (ALBs), which the panel wasn't familiar with. Check the pinned link in the ETB Slack channel for official confirmation. Teams reacted very positively to this news across the session.

---

## Key Discussion Points

### 1. Infrastructure Repos Tied to In-Scope Repos
- **Question:** If a non-infrastructure repo (in scope) depends on a separate infrastructure repo (not tagged as in-scope) to deploy, do both need to be deployed weekly?
- **Answer:** Yes — not because the infrastructure repo itself is in scope, but because the in-scope repo depends on it. If infra deployment is slow (this team estimated **a couple of days per week**), auto-schedule isn't supported for this use case, so it becomes a **manual process**.
- **Exception guidance:** Exceptions are **not given out lightly** — "it takes a long time" or general technical difficulty does **not** qualify. Only genuine **business-critical failure risk** or potential for a significant incident qualifies. An approved-exceptions reference doc was shared in chat; exception submissions go through an **EMR form** (linked in the doc, not the general UTEP process).

### 2. Two-Week Deployment History Requirement
- **Question:** If onboarding today, do we need 2 weeks of deployment history to satisfy the ETB immediately?
- **Answer:** Yes, it's a **rolling two-week requirement**, and this is now moot in the near term thanks to the deadline extension to Oct 30.
- **Important clarification:** Two weeks isn't a "finish line" — once achieved, **weekly deployments must continue indefinitely**, or the repo falls back into non-compliance. Non-compliant repos post-deadline get **reported up to leadership via ETIP data**.

### 3. Full Build vs. Redeploy — What Satisfies the ETB
- ETB has **two checks**: (1) deployment frequency, and (2) an existing **IBC check** (already in OPL) verifying the image is within **N-2 versions or less than 40 days old** for first-party base images.
- **Recommendation: use full build + deploy** — this is what sets teams up for long-term success and ensures the latest patches are applied.
- However, **a deploy-only action (no new build) still counts** toward ETB compliance if you're already on the latest version.
- **Serverless/no-base-image components:** if there's no first-party base image to check, the team is **assumed compliant** on the software recency check by default.
- Post-ETB, **additional software recency checks** will eventually be added, but not yet — data/tooling isn't in place.

### 4. Auto-Schedule Trigger Timing
- Currently runs on a **train schedule: Monday–Thursday at 9 AM, 1 PM, and 4 PM.**
- Placement into a train depends on **how close a repo is to its 7-day compliance mark** — not fixed/consistent per repo.
- **Future capability (in development):** teams will eventually be able to **set their own custom trigger times** — not available yet.

### 5. Auto-Approval vs. Manual PAR Approval
- If the most recent build is based on a **bot commit** (no human change), it can be **auto-approved and auto-merged** for deployment.
- **Any human commit requires manual PAR approval** — this is intentional, so a human confirms the change before it's pushed.

### 6. Pipeline Failure Handling During Auto-Runs
- Each onboarded repo gets a **dedicated Slack channel** (team + bot) — failures trigger a push notification there.
- On failure, the repo is **automatically pushed to the next train** (e.g., fails 9 AM run → picked up at 1 PM run).
- The team is also working on **shrinking the compliance window from 7 days to 5 days** to build in more buffer against failures.

### 7. Repos With No Library/Security Updates
- **Question:** How does the ETB handle repos with no code/library/security changes at all?
- **Answer:** Just deploy anyway — as long as there's no first-party base image needing a version/age update, the repo is **deemed compliant** by deployment frequency alone. Deploying through the train at least once every 7 days is sufficient.

### 8. Dependency Version Ranges & Hot Fixes (Open Question)
- **Question:** For Python/serverless projects using **pinned dependency ranges** (rather than exact versions) to pick up hot fixes — would a hot fix only be captured via a **full rebuild**?
- **Answer:** Not confirmed on the spot — the ETB team asked the requester to post this in the Slack channel and tag them for a same-day answer.

### 9. Retrograde Compliance Status — Bug Fix Explanation
- Multiple teams reported repos **flipping backward** from "Complete" to "In Progress"/"Not Started" — ~10 repos flagged by one team.
- **Root cause explained:** A **logic bug** in the compliance calculation allowed some repos to be marked "Complete" even when deployments were spaced **more than 7 days apart** across two separate windows. This was **fixed last night** to correctly enforce the 7-day rule.
- **Expected effect:** Most repos previously marked "Complete" under the old (buggy) logic will now show as **"In Progress"** — a new deployment within the next 7 days will restore "Complete" status.
- **Self-service tip:** Scroll to the **second table at the bottom of the dashboard — the "rolling window" table** — for per-repo details on deployment windows and the exact date the next deployment is needed by.

### 10. Status of Approved Exclusions
- Approximately **80+ exclusion requests** are in the queue.
- The ETB team is aiming to complete a **first pass on all of them by end of this week**, including internal VP approval for ones that will be dropped from reporting.
- Acknowledged as **behind schedule** — commitment made to keep the Slack channel updated as this progresses.

### 11. Non-Prod-Only Components — Compliance Tracking
- **Question:** How is compliance tracked for components that are **non-prod only** (never deploy to prod)? Currently showing as "Not Started."
- **Answer:** Additional gates/metrics exist specifically for non-prod deployment tracking (a metrics-calculation reference link was shared in chat). **Auto-schedule does not currently support non-prod deployments** — these must be **pushed manually**.

### 12. New Pipeline Flavor Timeline
- Several new flavors have been released in recent weeks; more remain in backlog (e.g., **Kubernetes** flagged as high-impact by one team).
- **No hard release dates** are given — the responding engineer is personally working on **non-prod support**, with a teammate covering **three additional flavors** in progress.
- **Prioritization is community/upvote-driven** — teams are encouraged to **upvote the relevant JIRA tickets** to influence what gets picked up next ("straight democracy").

### 13. Inventory Count Drop (366 → 244) — Root Cause Explained
**Question raised by Sandeep**, matching our earlier internal concern about the inventory shrinking.

- **Two likely causes identified:**
  1. Some JIRA tickets were created by LOB/PMO teams **before scope was finalized** (finalized around **August 28**) and were never updated after the change went through.
  2. Some repos were **archived**, or moved to an **app type or pipeline flavor now deemed out of scope**, and were removed accordingly.
- **Core baseline scope has not changed** since end of August — the shifts reflect individual repos falling in/out, not a scope redefinition.
- **Going forward:** The **current ETB inventory will not change further**, except if a team's **approved exclusion request** results in repos being removed (in which case the team will be notified directly).
- **Important distinction:** Post-ETB, tracking moves to **ETIP**, which **will have an ongoing, dynamically changing inventory** as new repos are created/registered — but that's out of scope for the current ETB.

### 14. Non-PAR Auto-Schedule — Still Under Review, No Date
- Still **pending JPL approval**, actively in review with the SDLC team communicating with JPL.
- **No hard date given** — multiple approval layers involved. Team continues pushing to expedite but cannot commit to a timeline.

### 15. Non-Flavor-Supported Repos — Confirmed Path
- **Confirmed directly:** for non-flavor-supported repos, **manual deployment is the only path** — matches what we'd already assumed internally.

### 16. Dashboard Clarifications — Onboarded vs. Eligible
- The main **ETB QuickSight dashboard shows eligibility**, but **does not show whether a repo is actually onboarded** to CAR auto-schedule.
- A **separate dashboard** exists specifically for auto-schedule tracking — shows which ASVs are actively onboarded, and whether each is **active or paused**. Link was dropped in the office hours chat; filterable by ASV (dashboard covers 20 ASVs total).
- **Note:** ETB compliance and CAR auto-schedule are **not the same thing** — auto-schedule is optional tooling; manual deployment can also satisfy the ETB directly.

### 17. Complete → Not Started Flip (Duplicate of Item 9, Team-Specific Case)
- Sandeep separately raised seeing a repo go from **"Complete" to "Not Started"** the following week, despite being onboarded to CAR.
- **Confirmed as the same logic-bug fix** described in Item 9 — recalculation may cause a step-back to "In Progress," or it may reflect an actually missed deployment.
- **Recommended self-check:** the **rolling window table** at the bottom of the dashboard shows exact deployment windows and next-due dates per repo.

---

## Action Items

| # | Action | Owner |
|---|--------|-------|
| 1 | Confirm the Oct 30 extension applies specifically to ETB 2440 (not ALBs) via the pinned Slack link | All teams |
| 2 | Continue weekly deployments even after hitting "Complete" status — it's an ongoing requirement, not a one-time milestone | All teams |
| 3 | Use full build + deploy where possible, rather than deploy-only, for long-term compliance health | All teams |
| 4 | Review the rolling-window table on the dashboard to confirm actual compliance status per repo after the recent logic fix | Sandeep / all teams |
| 5 | If pursuing an exception, review the shared approved-exceptions doc and submit via the EMR form (not UTEP) — only for business-critical impact | Applicable teams |
| 6 | Upvote relevant pipeline-flavor JIRA tickets (e.g., Kubernetes) to influence prioritization | Interested teams |
| 7 | Track non-prod-only components manually — auto-schedule does not currently support them | Amit / applicable teams |
| 8 | Use the separate CAR auto-schedule dashboard (filterable by ASV) to check onboarding/active-paused status, since the main ETB dashboard doesn't show this | Sandeep / team |
| 9 | Follow up in Slack (tag ETB team) on the dependency-range/hot-fix rebuild question | Zach/Varun |
| 10 | Continue monitoring for non-PAR auto-schedule approval — no committed date, still in JPL review | All teams |
| 11 | Watch for exclusion queue updates in the Slack channel — ETB team targeting first pass by end of this week | All teams |

---

## Key Takeaways
- **Biggest news: deadline extended to October 30** — an extra month of runway for all in-scope repos.
- **A logic bug in compliance calculation was just fixed** — expect some previously "Complete" repos to show as "In Progress" temporarily; this is expected and not a new problem, just corrected tracking.
- **Exceptions remain very hard to get** — only genuine business-critical risk qualifies; technical difficulty or time cost alone does not.
- **Our earlier inventory-drop question (366→244) got a direct answer:** it's due to stale JIRA tickets pre-dating the Aug 28 scope finalization, plus repos falling out of scope individually — not a moving target going forward (barring approved exclusions).
- **Non-PAR auto-schedule remains undated**, still working through JPL approval layers.
- Two useful dashboards now confirmed: the **main ETB dashboard** (eligibility + rolling-window compliance detail) and a **separate CAR auto-schedule dashboard** (onboarding/active-paused status, filterable by ASV) — worth using both going forward.
