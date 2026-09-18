
## Current Status

**Overall repo landscape:**
- **354 total repos** identified as in-scope for ETB 2440.
- **115 repos onboarded to CAR auto-schedule** so far (up from the earlier count of 83).
- Roughly **~240 repos remain outside CAR coverage** — these require manual weekly deployment until automated onboarding is possible.

**Onboarding progress (of the 115 onboarded):**

| ASV | Total | Complete | In Progress | Not Started |
|---|---|---|---|---|
| ASVPROMETHEUSFINANCIALCORE | 69 | 16 | 3 | 50 |
| ASVPROMETHEUSFINANCIALCOREBANK | 15 | 0 | 1 | 14 |
| ASVPROMETHEUSFINANCIALCORECARD | 24 | 2 | 1 | 21 |
| ASVPROMETHEUSFINANCIALCOREINTERNAL | 7 | — | — | Non-PAR, out of scope |

- **26 of the 115 onboarded repos haven't had a scan run yet** — actual compliance status for these is unknown.

**Progress on non-CAR-eligible items:**
- Non-PAR auto-schedule support is actively being built (JPL changes in progress); soft target is **end of month**, pending JPL team approval — not guaranteed.
- **7 new pipeline flavors** (COTS multi/single-region, static content, data processing, container, AWS, Kubernetes) are tested and ready, pending a DevNav Hub release expected imminently.
- **Library packages have a temporary ETB exclusion** confirmed via the official exclusions list — relevant if any of our repos fall into that flavor.
- A **catch-all exclusion request for Windows/COTS applications** (raised by other teams, not confirmed as applicable to us yet) is being escalated to leadership, with precedent from Citrix/AWS Workspaces exclusions — worth evaluating if any of our repos fit this profile.

## Blockers

1. **Majority of onboarded repos are still "Not Started"** — CORE alone has 50 of 69 not started; this is the single biggest driver of low overall progress.
2. **~240 repos have no automated path** (non-PAR or unsupported flavor) — require manual weekly deployment, estimated at ~20 hrs/week team effort.
3. **No exception available** for flavor/PAR limitations — confirmed directly by the ETB team; only genuine technical/business blockers qualify (and lower change frequency actually works against an exception, not for it).
4. **26 onboarded repos haven't been scanned**, so real compliance status is unverified.
5. **Pipeline reliability risk:** ~35% build success rate; unstable/aborted builds don't count toward compliance even when the underlying work completes — some pipelines need config fixes to report "successful" correctly.
6. **No weekend deployment window in CAR** — only Mon/Wed/Fri; no committed ETA for a fix (backlog item, prioritized by upvotes).
7. **30-day successful prod release is a prerequisite** for CAR auto-schedule pickup — some "not started" repos may be blocked here rather than by lack of effort; worth auditing.
8. **Trex-related pause (Sept 8–15)** temporarily halted all releases — now resolved, but may explain recent gaps in build history.
9. **Full ETB intent goes beyond CAR onboarding** — source repos also need manual build+deploy, not just deployment-layer repos, since pipelines are chained end-to-end.
