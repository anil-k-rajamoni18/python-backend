# 📘 **Day 3 — Branching, Merging & Merge Conflicts (Deep Dive)**

---

# 🌿 **1. Git Flow Branching Model**

Git Flow is a structured branching model ideal for medium to large teams.

## **Primary Branches**

* **main/master** → Production-ready code
* **develop** → Integration branch for ongoing work

## **Supporting Branches**

| Branch Type  | Purpose                                    |
| ------------ | ------------------------------------------ |
| **feature/** | Build new features without affecting main  |
| **release/** | Prepare for release cycles                 |
| **hotfix/**  | Quick fixes applied directly to production |

### **Real-World Example**

A banking application team uses Git Flow to manage multiple squads working on features like KYC, Payments, and Statements simultaneously.

---

# 🧩 **2. Feature Branches**

Feature branches allow isolated development.

### **Naming Conventions**

```
feature/user-auth
feature/add-to-cart
feature/ui-refresh
```

### **Industry Scenario**

Backend engineers develop a new `/orders` API on a dedicated branch so the main codebase stays stable.

---

# 🔀 **3. Fast-Forward Merges vs 3-Way Merges**

## **Fast-Forward Merge**

Used when `main` has not diverged.

```bash
git merge feature/user-auth
```

Main pointer simply moves forward.

## **3-Way Merge**

Used when both branches have new commits.

```bash
git merge feature/user-auth --no-ff
```

Creates a merge commit.

### **Industry Scenario**

Teams prefer **`--no-ff` merges** for traceability—helps in PR reviews and production debugging.

---

# ⚠️ **4. What Causes Merge Conflicts?**

Conflicts occur when Git cannot automatically combine changes.

### **Common Causes**

* Same lines modified in both branches
* File edited in one branch and deleted in another
* Overlapping structural changes

### **Real Example**

Two developers update the same function in `invoiceService.js`—Git cannot guess which change is correct.

---

# 📝 **5. Understanding Conflict Markers**

When conflicts occur, Git marks the file like this:

```
<<<<<<< HEAD
code from your current branch
=======
code from the branch being merged
>>>>>>> feature/user-auth
```

### **Sections Explained**

* **HEAD:** Your current branch
* **Lower section:** Incoming branch changes

---

# 🔧 **6. Resolving Conflicts Manually**

### Steps:

1. Open the conflicted file
2. Decide which changes to keep
3. Remove conflict markers
4. Stage the fixed file:

```bash
git add <file>
```

5. Complete merge:

```bash
git commit
```

### **Industry Scenario**

During release crunch time, merge conflicts are frequent—engineers must resolve them cleanly to avoid breaking builds.

---

# 🔄 **7. Git Merge vs Rebase (Intro)**

## **Merge**

* Keeps history intact
* Creates a merge commit
* Good for collaborative teams

## **Rebase**

* Rewrites history
* Creates a clean, linear commit timeline

### Example

```bash
git rebase main
```

### **Industry Use**

Rebase is used before creating a Pull Request to clean up commit history.

---

# 🍒 **8. Cherry-Pick Intro**

Cherry-picking lets you copy *specific commits* from another branch.

```bash
git cherry-pick <commit-hash>
```

### **Use Case**

A critical bug fix done on a feature branch needs to be applied to the release branch immediately.

---

# 📦 **9. Stash (Saving Temporary Work)**

Stash lets you save uncommitted changes without committing them.

```bash
git stash
```

Retrieve stashed changes:

```bash
git stash pop
```

### **Real Scenario**

You're in the middle of coding but must switch branches to hotfix a production issue.

---

# 🧪 **Important Commands Summary**

```bash
git merge
git merge --no-ff
git rebase
git rebase --continue
git cherry-pick
git stash
git stash pop
```

---

# 🧪 **Day 3 Hands-On Tasks**

## **1. Create Two Branches & Cause a Merge Conflict Intentionally**

* Create `feature/A` and `feature/B`
* Modify the same line in both branches
* Merge one into `main`, then merge the second → conflict expected

## **2. Resolve the Conflict & Commit the Fix**

* Edit conflict markers
* Stage changes
* Commit the merge resolution

## **3. Try Stash + Apply Changes**

* Make changes without committing
* Run `git stash`
* Switch branch
* Run `git stash pop`

## **4. Rebase a Feature Branch Onto Main**

```bash
git switch feature/A
git rebase main
```

Resolve any conflicts and continue:

```bash
git rebase --continue
```

---

# 🔥 **Mini Project — Conflict Resolution Simulation**

Create a simulation repo to practice:

### **Tasks:**

1. Create multiple branches with intentionally conflicting code
2. Perform merges and resolve conflicts
3. Use rebase to clean commit history
4. Cherry-pick selected commits across branches
5. Use stash to manage temporary work

