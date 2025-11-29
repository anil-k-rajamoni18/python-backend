# 📘 How to Do PR / Code Review Like an SDE-II

---

## ✅ 1. Mindset of an SDE-II Reviewer

An SDE-II isn't just checking syntax—they evaluate:

* ✔️ Code Quality
* ✔️ Design & Architecture
* ✔️ Performance impact
* ✔️ Security & privacy concerns
* ✔️ Maintainability
* ✔️ Risk of regressions
* ✔️ Alignment with team standards
* ✔️ Future-proofing & scalability

**They review code as if they own the system, not just the PR.**

---

## 🔥 2. Before Reviewing a PR

### ✓ Understand Context

Read the PR description:

* What problem is being solved?
* Is there a ticket linked? (Jira, Azure Boards, GitHub Issue)
* Does the solution match the acceptance criteria?

### ✓ Run the Branch (if applicable)

For UI, APIs, backend services:

* Run app locally
* Test new endpoints
* Verify feature flow

### ✓ Check PR Size

**Ideal PR size: 200–500 lines**

If > 1,000 lines:
* Ask contributor to split PR
* Large PRs hide bugs and make review ineffective

---

## 🧠 3. SDE-II PR Review Checklist

### 3.1 Code Correctness & Logic

**Ask: Does the code do what it's supposed to do?**

* Edge cases covered?
* Null safety?
* Error handling?
* Proper status codes for APIs?
* Race conditions?
* Thread safety issues?

### 3.2 Architecture & Design

SDE-II reviews design, not just code.

#### Checklist:

* Does the implementation follow the existing architecture?
* Is code placed in the right module/layer?
* Are abstractions meaningful?
* Is duplication minimized?
* Is SOLID respected?

**Common SDE-II remark:**
> "This logic belongs in a service layer, not the controller."

### 3.3 Performance Review

**Consider:**

* Will this scale with 10x traffic?
* Are we doing inefficient DB calls?
* Are loops nested unnecessarily?
* Can caching help?

#### Examples:

* Replace for loops with batched operations
* Avoid N+1 queries
* Avoid loading unnecessary data

### 3.4 Security Review

**Check for:**

* SQL injection
* Input validation
* Hardcoded secrets
* Logging sensitive data
* Authentication & authorization checks

SDE-II often catches these subtle issues.

### 3.5 Maintainability

**Ask:**

* Is the code readable?
* Are names meaningful?
* Is complexity low?
* Are comments explaining non-obvious logic?
* Are unit tests provided?

### 3.6 Test Coverage

High-quality PRs include:

* Unit tests
* Integration tests
* Negative scenario tests
* Edge cases

**Reject PRs with poor coverage or missing tests.**

### 3.7 Consistency

Does the code follow:

* Coding standards
* Naming conventions
* Logging patterns
* Folder structure
* API response format conventions

### 3.8 Documentation

**Check:**

* Updated README (if needed)
* API docs updated
* Inline comments for complex logic
* Migrations documented

---

## ⚠️ 4. Common PR Smells (Red Flags)

| Red Flag | Issue |
|----------|-------|
| 🚨 **Very Large PR** | Hard to review; increases bug risk |
| 🚨 **Duplicate Code** | Indicates poor abstraction |
| 🚨 **Unnecessary dependencies** | Slows builds and increases attack surface |
| 🚨 **Over-engineering** | Too complex for the requirement |
| 🚨 **Hardcoded values** | Leading cause of bugs |
| 🚨 **Missing tests** | Non-negotiable for quality code |
| 🚨 **Silent catch blocks** | Criminal offense in engineering 😄 |

---

## ⭐ 5. How SDE-II Should Comment on PRs

### ✓ Be specific

❌ **Bad:**
> "This is wrong."

✔️ **Good:**
> "This API returns 200 even when the DB update fails. Consider returning 400 or 500 to match consistency with other handlers."

### ✓ Be constructive

❌ **Bad:**
> "Why did you write it like this?"

✔️ **Good:**
> "We can simplify this logic using a guard clause which improves readability."

### ✓ Provide alternatives

> "Instead of manually parsing JSON, you can use the built-in serializer."

### ✓ Ask leading questions

> "What happens when this list is empty? Does the function still behave correctly?"

### ✓ Suggest improvements, avoid commanding

> "Could we rename `x` to `userId` for clarity?"

---

## 🤖 6. PR Review Structure You Should Follow

### 1. Overview comment

Summarize your review:
* What you tested
* Major improvements needed
* Overall quality

### 2. Inline comments

Add comments to:
* Logic mistakes
* Naming suggestions
* Performance improvements
* Security vulnerabilities

### 3. Optional Suggestions

Use "nit:" for minor things

* `nit: spacing`
* `nit: variable naming`

### 4. Approval or Request Changes

* **Approve**
* **Comment** (non-blocking)
* **Request changes** (blocking)

---

## 🏭 7. Real-World Scenarios (SDE-II Level)

### Scenario 1 — API Endpoint PR

**Checks:**
* Does endpoint validate inputs?
* Are error messages consistent?
* Is the service layer doing too much?
* Are we leaking sensitive info in logs?

### Scenario 2 — Database Query PR

**Checks:**
* Query optimization
* Index usage
* Transaction safety
* Deadlock risk
* Is the query idempotent?

### Scenario 3 — UI + Backend Integration

**SDE-II ensures:**
* UI sends correct payload
* Backend validates payload
* Error handling matches UI requirements
* The API is backward compatible

### Scenario 4 — Refactoring PR

**Evaluate:**
* Are abstractions better now?
* Did refactoring break existing flow?
* Are tests updated accordingly?

---

## 🧪 8. Checklist Summary (SDE-II Quality)

### ❗ Mandatory

* ✔ Code correctness
* ✔ Tests included
* ✔ No performance bottlenecks
* ✔ No security issues
* ✔ No broken architecture
* ✔ Code readable and maintainable
* ✔ Consistent with standards

### ⭐ Optional (Good to have)

* ✔ Better naming
* ✔ Improved comments
* ✔ Minor stylistic improvements
* ✔ Better separation of concerns

---

## 🎯 Final Advice: How to Behave as a High-Performing Reviewer

1. **Review PRs within 24 hours**
2. **Do not nitpick early** — look at architecture first
3. **Always ask for tests**
4. **Keep tone friendly and professional**
5. **Focus on long-term maintainability**, not personal preferences
6. **Aim for fewer, higher-quality comments** instead of 100 nitpicks

**Remember:** Your goal is **team velocity + code quality**, not showing intelligence.

---

## 📋 Quick Reference Card

```markdown
Before Review:
├── Read PR description & linked tickets
├── Check PR size (ideal: 200-500 lines)
└── Run the branch locally

During Review:
├── Code correctness & logic
├── Architecture & design
├── Performance implications
├── Security concerns
├── Maintainability
├── Test coverage
├── Consistency with standards
└── Documentation updates

After Review:
├── Provide overview comment
├── Add inline comments
├── Mark as: Approve / Comment / Request Changes
└── Follow up on requested changes
```

---

## 💡 Pro Tips

* **Start with the big picture** before diving into details
* **Understand the "why"** before critiquing the "how"
* **Be a mentor**, not a gatekeeper
* **Praise good work** when you see it
* **Learn from every PR** you review
* **Document patterns** for future reference
* **Balance perfectionism** with shipping velocity

---

## 🚀 Level Up Your Reviews

As you gain experience:

1. **Build a mental model** of the entire system
2. **Anticipate future changes** and their impact
3. **Think about observability** and debugging
4. **Consider the user experience** end-to-end
5. **Mentor junior developers** through your reviews
6. **Share knowledge** in your comments
7. **Create reusable patterns** the team can follow

Remember: **Great code reviews make great engineers!**