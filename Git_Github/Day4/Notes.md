# 📘 **Day 4 — PR Workflow, Code Reviews & GitHub Advanced**


---

# 🔄 **1. Pull Request (PR) Best Practices**

A Pull Request is not just a merge request—it’s a communication tool for collaboration.

## **✔ Clear Title & Description**

A good PR should:

* Explain **what** the change is
* Explain **why** the change was made
* Provide context (screenshots, logs, diagrams if necessary)

### **Real Example**

**Title:** `feat(auth): add JWT refresh token mechanism`
**Description:**

* Adds refresh token endpoint
* Updates login logic
* Fixes issue #42
* Includes unit tests

---

## **✔ Link Issues**

Automatically close issues by referencing them:

```
Closes #23
Fixes #47
```

---

## **✔ Small Commits & Atomic Changes**

Atomic → Each commit should represent ONE logical change.

### Why?

* Easier review
* Easier rollback
* Better history tracking

**Industry Scenario:**
Large PRs slow down teams. Many companies enforce max PR size guidelines.

---

# 🤝 **2. PR Review Etiquette**

Professional code review is about collaboration, not criticism.

## **Approvals & Re-Reviews**

* Author pushes changes
* Reviewer re-checks only changed parts (incremental review)

## **Automated CI/CD Checks**

GitHub Actions runs:

* Linting
* Tests
* Security scans
* Build checks

Merges are allowed only when checks pass.

## **CODEOWNERS**

Automatically assigns reviewers to PRs.

Example file:

```
# All frontend changes require approval from FE team
/frontend/ @frontend-team
```

---

# 🧑‍💻 **3. Professional PR Review Rules & Suggestions**

These rules are followed by top-tier engineering teams.

## **Reviewer Checklist**

* ✔ Check code readability
* ✔ Ensure meaningful commit messages
* ✔ Confirm no secrets or API keys
* ✔ Validate file & folder structure
* ✔ Ensure tests pass
* ✔ Suggest improvements politely
* ✔ Provide examples for suggested changes
* ✔ Encourage small PRs
* ✔ Respect author's design context

---

## **Common Review Suggestions**

* "Consider renaming variable for clarity"
* "Can this logic be more modular?"
* "Add test coverage for this new method"
* "Document this function"

### Industry Insight

Good reviewers never dictate— they *suggest* and explain justification.

---

# 📦 **4. Advanced GitHub Topics**

Modern teams rely heavily on GitHub’s advanced features.

## **Branch Protection Rules**

Prevents merging without:

* Required reviewers
* CI passing
* No direct pushes to `main`

## **Required Checks**

Typical checks include:

* Unit tests
* Linting
* Build pipeline

## **GitHub Projects**

Kanban-style project management.

## **GitHub Wiki**

Long-term documentation storage.

## **Releases & Tags**

Used for versioning deployment artifacts.

```bash
git tag v1.0.0
git push --tags
```

## **GitHub CLI (gh)**

Powerful command-line tool for automation.

```bash
gh pr create
gh pr review
```

---

# 🧪 **Important Commands Summary**

```bash
git tag
git push --tags
gh pr create
gh pr review
```

---

# 🧪 **Day 4 Hands-On Tasks**

## **1. Create PR from feature → main**

* Push feature branch
* Open PR using GitHub UI or CLI

## **2. Review Your Own PR (Using Another Account)**

* Add comments
* Request changes
* Approve

## **3. Setup Branch Protection Rules**

* Require 1 reviewer
* Require CI to pass

## **4. Add CODEOWNERS**

* Add team members
* Enforce auto-review rules

---

# 📝 **Mini Project — PR Review Training Repository**

Create a repository where you:

1. Open multiple PRs
2. Add meaningful descriptions
3. Assign reviewers
4. Perform detailed reviews
5. Create releases & tags
