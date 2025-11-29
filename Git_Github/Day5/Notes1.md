# 📘 **Day 5 — Advanced Git Commands, Cleanup, Optimization & Full Project Simulation**

---

# 🔥 **1. Advanced Git Commands**

## **1.1 Interactive Rebase (Editing Commit History)**

Interactive rebase allows you to **edit**, **reword**, **squash**, or **remove** commits.

### Example:

```bash
git rebase -i HEAD~5
```

This opens an editor listing the last 5 commits.

### Common Actions:

* **pick** → keep the commit
* **squash** → combine commit with previous
* **reword** → update commit message
* **drop** → remove commit

### Real-World Scenario

Before merging a feature branch into `main`, developers squash multiple WIP commits into clean, readable commits.

---

## **1.2 Squash & Reword Commits**

Used to:

* Clean up messy history
* Combine small commits
* Fix incorrect commit messages

Example inside interactive rebase:

```
pick abc123 Initial login UI
squash def456 Fix button style
reword 8923ab Update login UI message
```

---

## **1.3 Commit Amending**

Fixes the last commit without creating a new one.

```bash
git commit --amend
```

Useful for:

* Updating commit message
* Adding forgotten files

**Industry Example:** A developer forgets to commit a config file—amend adds it without polluting history.

---

## **1.4 Reflog (Recover Lost Commits)**

Reflog tracks **everything** your HEAD has pointed to.

```bash
git reflog
```

Use Case:

* Recover commits lost after `reset --hard`

Example:

```bash
git checkout <reflog-hash>
```

---

## **1.5 Git Reset vs Revert**

### **Reset** (dangerous)

Moves branch pointer backwards, modifies history.

```bash
git reset --hard <commit>
```

### **Revert** (safe)

Creates a new commit that undoes a previous commit.

```bash
git revert <commit>
```

**Industry Rule:** Teams use **revert**, not **reset**, on shared branches.

---

## **1.6 Git Bisect (Debugging Tool)**

Used to find which commit introduced a bug.

### Start bisect:

```bash
git bisect start
git bisect bad
git bisect good <commit>
```

Git performs binary search through commits.

### Real Scenario:

Production bug detected — bisect helps identify the exact commit causing the issue.

---

## **1.7 Submodules**

Submodules allow you to include one Git repo inside another.

```bash
git submodule add <repo-url> libs/ui-library
```

**Real Example:** Monorepos using shared UI components as submodules.

---

## **1.8 Git Hooks**

Git hooks automate tasks.

### Located in:

```
.git/hooks/
```

### Examples:

* **pre-commit** → run tests before committing
* **pre-push** → run lint checks

**Industry Scenario:** Prevent bad code from entering main with automated hooks.

---

# ⚠️ **2. Advanced Conflict Scenarios**

## **2.1 Rebasing + Conflicts**

During rebase, Git stops at conflicting commits.

```bash
git rebase main
# fix conflict
git rebase --continue
```

---

## **2.2 Cherry‑Pick Conflicts**

Cherry-picking applies specific commits.

If conflicts occur:

```bash
git add <fixed-file>
git cherry-pick --continue
```

---

## **2.3 Reverting Conflicts**

Even reverts may conflict if code has evolved.

```bash
git revert <commit>
```

Resolve conflicts as usual.

---

## **2.4 Binary File Conflicts**

Binary files (images, PDFs, compiled output) cannot auto‑merge.

Solutions:

* Choose one version manually
* Use Git LFS (Large File Storage)

---

# 🧪 **3. Hands-On Tasks**

## **Task 1 — Rewrite Commit History With Interactive Rebase**

* Use `git rebase -i HEAD~5`
* Squash unnecessary commits
* Reword messages to be meaningful

---

## **Task 2 — Recover Deleted Commits With Reflog**

* Make changes
* Run `git reset --hard`
* Use `git reflog` to find lost commit
* Recover it using checkout/reset

---

## **Task 3 — Debug Code Using Git Bisect**

* Mark a known “good” commit
* Mark a “bad” commit
* Let Git locate the buggy commit

---

## **Task 4 — Add a Submodule**

Example:

```bash
git submodule add https://github.com/some/library.git libs/ui-components
```

---

# 🏆 **Final Real‑World Project — Complete Collaboration Simulation**

You will now simulate a real multi‑developer Git workflow.

## **Project Branch Structure**

```
main       (protected)
dev
feature/auth
feature/ui
feature/database
hotfix/typo-fix
```

---

# 🔥 **Project Tasks**

1. Clone the repository
2. Set up remotes and sync `dev`
3. Create multiple feature branches
4. Add code, push changes
5. Create Pull Requests
6. Perform review on another branch
7. Request changes & approve PRs
8. Create merge conflicts intentionally
9. Resolve conflicts across branches
10. Squash commits before merging
11. Add Git tags for release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

12. Write a professional `CHANGELOG.md`
13. Simulate a bug found in production → fix using `hotfix/typo-fix`
14. Merge hotfix back to both `main` and `dev`

---
