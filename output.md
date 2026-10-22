# Minutes of Meeting: Office Hours, ETB 2440

**Date:** October 21
**Session:** ETB 2440 Office Hours (two recording parts, combined here)
**ETB / CAR team:** Joe, Akash, Talyne (director and program POC), Adriana (data team expert, joined mid-session)
**Teams who raised questions:** Mark Clark and team, Zach Olson, Sridevi (28 repos), Rachel (OSDI platform team), Brian, Mitchell, Umar, and others (names as heard in the audio, some spellings unclear)

---

## Summary (TL;DR)

- **The dashboard data is correct, but confusing.** Freeze padding from TRex and enterprise change freezes made the deployment windows very long (window A reached about 24 days). Teams that deployed regularly still show In Progress.
- **Complete status is deferred, not lost.** The windows started rolling again on October 21. Repos move to Complete once they have a deployment in each window.
- **The key action is the "next valid deployment due" date** on the rolling window view. A successful deployment by that date (for many teams, October 27) is what restores compliance.
- **Some repos may still show wrong data.** The data team is fixing specific issues. Teams should screenshot their dashboards and report repos that look wrong by Friday.
- **The ETB will likely close red on October 31.** The program team expects overall completion around 70% at best, then a path to green, with weekly reporting continuing.
- **Composite-application repos with multiple artifacts are skipped by CAR.** They need manual deployment until a fix is built. CAR onboarding itself is optional for the ETB.

---

## Key Points (2-3 liners)

**The dashboard is correct, but the windows look odd.** Freeze padding from TRex and change freezes stretched window A to about 24 days, so many teams that deploy regularly still show In Progress. Windows started rolling again on October 21.

**The next valid deployment due date is the action to watch.** A successful deployment by that date, October 27 for many repos, restores compliance. A second deployment within seven days holds it through October 31.

**Some data issues are being fixed.** Teams should screenshot their dashboards and post repo names that look wrong by Friday, tagging the host.

**Expect the ETB to close below 100% on October 31.** The ETB team thinks completion may reach about 70%, then a path to green with weekly reporting. On October 31, download the rolling window view as a record of deployment dates.

**Composite-application repos with multiple artifacts are skipped by CAR.** They need manual deployment until a fix is built. CAR onboarding is optional for the ETB.

---

## Key Discussion Points

### 1. Is It Safe to Plan for Compliance on October 31?

**Question:** If a repo has a deployment in the 7 days before October 31 (October 24 to 31) and another within 7 days before that (October 17 to 23), is that a fair way to judge compliance?

**Answer:** Yes, with the caveat that freeze padding has added days to some windows, which is what confuses many teams.
- The data team was notified and is looking into adjustments. No ETA was given.
- The host is not the data owner. The dashboard query is more than 1,000 lines long.

### 2. How Freeze Padding Works

- When a freeze is active, **the clock stops**. A team is not penalized for days it could not deploy, so those days are added to the window.
- The padding was applied to **everyone equally**, with no per-team logic. Some teams did not need it, and for them it worked against the intent.
- **Window naming is reversed from intuition:** window A is the **most recent** window and window B is the **earlier** one.
- **Why windows kept growing day by day:** a day of padding was added each day until the freeze ended (the TRex period plus enterprise freezes). The freeze ended October 20, and the windows began rolling on October 21.
- Talyne and Adriana confirmed: **there is no bug.** Window A is currently up to about **24 days**, made up of about 17 days of freeze padding on top of the normal period.
- The compliant status is **deferred** for the number of padding days in a team's cycle. Teams in Progress will become Complete.
- A window cannot be extended. It is a rolling seven-day window, which is longer only where freeze padding applies.

### 3. The Three Compliance Checks (from Adriana)

A repo is compliant when it has:
1. A deployment in **window A**.
2. A deployment in **window B** (the seven days before window A, which currently has no freeze padding).
3. **No gap longer than seven days** between window A and window B, with freeze padding applied where relevant.

The third check exists because deploying on day one and again on day thirteen would otherwise count as two windows.

### 4. Next Valid Deployment Due Date

- A column on the rolling window view shows the **next valid deployment due date**, based on the most recent deployment plus any freeze padding.
- **Example given:** if the due date is October 27, a successful deployment on that day restores compliance. Missing it risks going back to Not Complete.
- A **future freezes** column, on the far right of the rolling details section, shows upcoming padding that applies to a team.
- Teams that deploy by their due date twice before the 30th should be compliant (confirmed in the Q&A).
- A deployment from October 1 would roll into window B on October 22, and a new deployment made on October 21 sits in window A, which makes the repo compliant.

### 5. Teams Showing In Progress Despite Regular Releases

Several teams showed the same pattern:
- **Zach Olson:** window A end date kept moving to the current day. Explained by the freezes (an enterprise freeze from October 16 to 20, and TRex). Teams were asked to screenshot dates today and tomorrow, and the data team will check if it keeps moving.
- **Sridevi (28 repos, HydraCache example):** the latest window B release was September 23, and the earliest window A release was October 5, so the gap was more than seven days. The team was in TRex and had enterprise pipeline issues in that period. The host believes the window B column and streak display are partly wrong, and will send the repos to the data team.
- **Teams with deployments in both windows but a red X:** the data team is working on an active issue. One build on October 1 should roll to window B within a day or two.
- **Brian's team and Mitchell's JetStore component:** same freeze padding effect. A recovery pattern was established, but window A is too long to show it. Another release by October 27 completes it.
- **Vulnerability-blocked components:** the same October 27 due date applies, because of the enterprise freezes.

### 6. Can Teams Submit Their Own Evidence Instead of the Dashboard?

- Teams can pull pipeline metrics data showing deployments in the last 14 days. The dashboard applies extra logic, mainly freeze padding, that teams cannot replicate.
- The host will pass the feedback to the director and data team, including the request to simplify the metric.
- There is **no forecast of future windows** on the dashboard.

### 7. Reporting on October 31 and After

- On October 31, teams can **download the QuickSight rolling window view**, which shows all deployment dates. The host will also download it and share it with the channel, so teams have a reference of deployment dates at the ETB due date.
- The ETB status is **whatever it is on October 31.**
- Talyne expects the program to be **red, possibly around 70%**. Reporting would continue weekly in the ETB and ETIP forums, with a **path to green** established, and then the ETB reporting stops.
- Tracking moves to an ETIP metric as business as usual. Controls and **UTEPs** will exist for exceptions.
- These challenges are being shared up through the program's leadership.
- A **short explainer** on freeze windows will be shared for teams to reuse with their own leadership.

### 8. Composite-Application Repos Skipped by CAR (Rachel, OSDI Platform)

- Some repos were skipped with the message that the release has **three application-typed artifacts, but exactly one was expected.**
- Cause (Akash): the Artemis API returns more than one artifact of the same type, so CAR does not know what to redeploy. It is not an easy fix and is being investigated.
- **Workaround:** manual deployments until it is fixed, particularly for composite applications with CFD or CDK.
- **CAR onboarding is optional for the ETB.** A team does not need auto-schedule to meet the deployment requirement.
- Akash will DM the JIRA ticket to track the fix. **Inner-source contributions** to auto-schedule are also possible.

### 9. Other Notes

- A post in the channel suggested deploying all repos once between October 16 and 22 and again between October 23 and 28. The hosts agreed the idea is consistent with the due date logic, subject to each repo's own due date.
- Anyone seeing windows keep growing should screenshot it, post in the channel and tag the host. Cases collected by Friday will go to the data team.

---

## Action Items

| # | Action | Owner |
|---|--------|-------|
| 1 | Check the "next valid deployment due" date for every repo and deploy successfully by it | All teams |
| 2 | Deploy again within seven days to hold the streak through October 31 | All teams |
| 3 | Screenshot dashboard windows today and tomorrow as a record | All teams |
| 4 | If a repo still looks wrong by Friday, post in the channel and tag the host with the repo names | Affected teams |
| 5 | Send the repo names with suspected window B or streak issues to the data team | Host, Talyne |
| 6 | Download the QuickSight rolling window view on October 31, and share the host's download in the channel | All teams, host |
| 7 | Share a short explainer on freeze windows | ETB team |
| 8 | DM the JIRA ticket on composite-application skips to Rachel | Akash |
| 9 | Plan manual deployments for composite-application repos that CAR skips | Affected teams |
| 10 | Pass feedback on simplifying the window metric to the director and data team | Host, Talyne |

---
*Note: Some names and numbers were unclear in the audio, and the first recording was cut at about 30 minutes before the second began. Please verify details before wider distribution.*
