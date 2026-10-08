# Minutes of Meeting: Office Hours, ETB 2440

**Date:** October 7
**Session:** ETB 2440 Office Hours
**Hosts / ETB and CAR team:** Joe, Talyne, Akash
**Attendees who raised questions:** Sandeep (PFC), Charlie, Noah, Brian, plus one or two other app team representatives (names unclear in audio)

---

## Summary (TL;DR)

- **The ETB dashboard (QuickSight) is the only source of truth.** Any spreadsheet or JIRA inventory is static and outdated. The dashboard refreshes daily between 6 and 8 AM.
- **Library package, SOD, Platform and Config repos can drop out of scope.** Library package has a temporary exclusion. Platform, SOD and Config app types are permanently out of scope, but only if the app type is set correctly through One-Pipeline support.
- **"Unmanaged" pipeline flavor repos are still in scope** and need weekly manual deployment unless their app type or flavor qualifies them for exclusion.
- **No exception path for "rarely updated" components** such as Herschel-type, library, infra or smart ops repos. If it is in scope, it needs a weekly deployment.
- **Non-prod auto-schedule:** the code is written, the approval request went to the SDLC and SLT teams on October 6. Now waiting on approvals and testing. No date.
- **Blue/green provision and destroy pipelines** may not count as deployments. The ETB team is checking the SQL behind the dashboard and will get back to the requester.
- **If an infra repo is retagged to Platform, running a non-infra pipeline on that component flips it back to Application.**

---

## Key Discussion Points

### 1. Exclusions: Library Package, SOD, Platform, Config

**Raised by:** a team with a repo flagged in scope that they believed was a library package.

- Two separate exclusion mechanisms exist:
  - **Library package pipeline flavor:** a **temporary** exclusion. These will be brought back into scope later when tracking moves to ETIP.
  - **Artemis / Blade Runner app type = Platform, SOD or Config:** these are filtered out of scope **permanently**, since they contain no application code that can be refreshed.
- The repo in question showed an **unmanaged** pipeline flavor on DevNav Hub (shown as customer managed), so it did not qualify as a library package. Its app type needs to be changed to SOD.
- App type changes go through the **One-Pipeline (OPL) support team**.
- Once the app type or flavor is corrected, the repo **drops out of scope automatically on the next dashboard refresh**. No exception form is needed.
- **Caution:** if the repo actually contains application code, the app type will flip back to Application the next time the pipeline runs.

### 2. Unmanaged Pipeline Flavor Repos (Sandeep)

- Some in-scope repos show an **unmanaged** flavor. **Unmanaged is still in scope**, so weekly manual deployment applies.
- For repos showing as out of scope or unregistered in the dashboard, no action is needed.
- To find out how a repo should be handled, **look up each component on DevNav Hub** and check its flavor and app type.
- One example shown was a library package in pre-production, covered by the temporary exclusion. These are also **not eligible for auto-schedule**.

### 3. Inventory Mismatch: ETB JIRA Sheet vs Dashboard (Sandeep)

- Sandeep's inventory from the ETB JIRA ticket showed **224 in scope**. The QuickSight dashboard showed **203 in scope, 64 complete**.
- **Explanation:**
  - The JIRA sheet and any downloaded spreadsheets are **static**, pulled at the start of the ETB, and many LOB copies were never updated.
  - The team made **two to three data improvements** to ETB scope, the last one in **mid-September**, which changed scope for some ASVs.
  - Anything downloaded earlier uses outdated data and outdated inclusion parameters.
- **Direction given:** QuickSight is the **only source of truth**. No other document or inventory from the ETB is kept up to date.
- Dashboard refresh window: **between 6 AM and 8 AM daily.**

### 4. Tracking Completed / In Progress / Not Started Counts (Sandeep)

- Sandeep asked whether there is a quicker way to see counts by status, instead of checking repos one by one.
- **Answer:** there is **no filter for compliance streak status** on the dashboard.
- **Workaround suggested:** download the data by ASV and summarize it yourself (using Claude if needed).

### 5. Herschel-Type Components: Exclusion Without Formal Exception

- **Answer: No.** This does not qualify.
- Non-prod environments are in scope. Repos that rarely update (smart ops, library, info repos and similar) are also in scope.
- **Rule: if a repo is in scope, it needs the weekly deployment.**

### 6. Non-Prod Auto-Schedule: JPL Approval Status

- Update: the request **went out to the SDLC and SLT teams on October 6**.
- The code is already written. What remains is **approvals and testing**.
- No committed date.

### 7. Infra Repo Retagging: Caveat on Flipping Back (Sandeep)

- Concern raised: after changing app type from Application to Platform, will it revert?
- **Answer (Akash):** app type is **tied to the pipeline flavor**. If one component is used with different flavors (for example an infrastructure flavor and a serverless flavor), and the serverless pipeline runs, the **app type switches back to Application**.
- Practical takeaway: only retag components that are truly infra only.

### 8. Archived Repos Still Showing In Scope

- A team decommissioning components had archived most repos and cleaned up non-prod resources, but still saw them in the scope list.
- **Answer:** archiving a repo moves it **out of scope**, and this is reflected in the dashboard. The static sheet is what is showing stale data. The dashboard link was shared in chat.

### 9. CAR Auto-Schedule Retry and Failure Behavior

- If a scheduled build fails, auto-schedule **retries on the next available train** (Monday to Thursday at 9 AM, 1 PM and 4 PM). It keeps retrying until the issue is fixed.
- **No failure notification exists yet.** Slack alerts currently only confirm that a build triggered, not that it failed or succeeded. This is being worked on, so teams need to keep checking the status page.
- Auto-schedule starts attempting a redeploy at the **6.5 day mark** so there is buffer before the 7 day compliance window. Triggering more often than that causes more issues than it solves.
- **Custom scheduling is not available** but is in progress.

### 10. Version Increments and Config Changes

- Auto-schedule **does not make changes on a team's behalf**. It either redeploys the last successful prod artifact or runs a full build.
- If a repo needs a stack version incremented before deploy (for example a CDK stack), the team has to handle that, for example with a **pre-hook inside the pipeline**.

### 11. Blue/Green Provision and Destroy Pipelines (Brian)

- **Situation:** a vendor product cannot use the managed blue/green deployment. The team runs separate blue and green repos. Week one is a **provision** pipeline, week two is a **destroy** pipeline, and they alternate. About five or six repo pairs follow this pattern.
- **Question:** does the destroy pipeline count as a deployment for ETB?
- **Response:**
  - The ETB team looks at specific pipeline stages (publish to artifactory, deploy stage), plus a successful Artemis release and a closed change order.
  - A "delete stack" stage likely **will not** count as a weekly refresh, but this was **not confirmed**.
  - The ETB team will check the **SQL query behind the dashboard** and get back to the team.
  - If destroys do not count, the options are: (1) **provision and destroy in the same week** per repo, which doubles the work, or (2) an **exception request**, which requires a strong business critical case such as impact to a very large number of customers.
- The team said they would rather not file an exception if they can avoid it, but believes there is an argument for one.

### 12. Other Q&A

- **ETB vs CAR eligibility:** the ETB does not require CAR auto-schedule. Manual deployments and other CD practices count. Whether a repo is eligible for auto-schedule is not relevant to ETB scope.
- **Onboarding option on DevNav Hub:** if the option to onboard is shown, the flavor is supported.
- **Part approval and commit classification (Charlie):** the decision matrix on the auto-schedule documentation decides approval. Bot-only commits (for example CodeGenie) with a full build go to production without approval. Human commits require manual PAR approval.
- **Auto-PAR vs auto-schedule (Noah):** these are separate initiatives. Auto-schedule's own commit classification logic works whether or not a team opts into auto-PAR. Questions on auto-PAR should go to the auto-PAR onboarding channel.
- **Freeze periods:** auto-schedule pauses during freezes, and the ETB follows the same schedule, so freeze periods are not counted against teams.
- **Full build vs redeploy (Python flavors):** either option can be used, depending on commits. Full build runs all pipeline stages.
- **No code changes:** if a repo has no new commits, auto-schedule still kicks off at about 6.5 days, rebuilds and redeploys the last version (if full build is chosen), and the repo stays compliant for ETB.
- **QA-only merges to main (Noah):** a human commit to main will stop at the PAR stage. Best practice is to only merge to main what is ready for prod, or use feature flags. If it is not deployed within 7 days, the repo falls out of compliance.

---

## Action Items

| # | Action | Owner |
|---|--------|-------|
| 1 | Use the QuickSight dashboard as the only source for scope and status. Stop relying on JIRA or downloaded inventory sheets | All teams, Sandeep |
| 2 | Look up each in-scope repo on DevNav Hub to confirm flavor and app type (library package, SOD, Platform, Config, unmanaged) | Sandeep and repo teams |
| 3 | For repos that qualify, work with One-Pipeline support to change app type to SOD or Platform. Only for components with no application code | Sandeep, with OPL |
| 4 | Download dashboard data by ASV and summarize Completed, In Progress and Not Started counts (no built-in filter) | Sandeep |
| 5 | Plan for weekly deployment of Herschel-type and other low-change components. No exclusion route exists | Affected teams |
| 6 | Check SQL logic behind the dashboard on whether a destroy pipeline counts as a deployment, then reply to the blue/green team | ETB team (Akash) |
| 7 | Blue/green team to decide between provision and destroy in the same week, or a business critical exception request | Brian and team |
| 8 | Monitor non-prod auto-schedule approval, now with SDLC and SLT | All teams |
| 9 | Do not assume Slack alerts confirm success. Check the auto-schedule status page for failures | Teams on auto-schedule |

---

## Key Takeaways for Our Team

- **Our infra repo retagging plan is consistent with what was said today**, with one important caveat: if a component runs a non-infra pipeline, the app type flips back to Application.
- **The inventory drop we were asking about earlier (366 to 244, and now 224 vs 203) is a data freshness issue**, not a real change. The dashboard is the number to report to leadership.
- **Non-prod auto-schedule is still pending approvals**, so manual deployment remains the plan for those repos.
- **No leniency for components that "rarely change"**, which matters for any repo of that type in our inventory.

---
*Note: Some speaker names and a few words are unclear in the transcripts (for example "Talyne" appears under several spellings), and the two uploaded files overlap in the final section. Please verify details before wider distribution.*
