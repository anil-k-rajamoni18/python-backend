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

# 🔥 1. Git Merge vs Git Rebase — Real-Time Understanding

---

## 🟦 git merge

### 📌 What it does:
- Combines two branches
- Creates a new merge commit
- Does not rewrite history

### 🧠 When you use it:
- When you want to keep a clear history of how branches diverged
- When collaborating with multiple developers

### 📘 Example (Real-Time Scenario)

You are working on a feature branch:

```
main ----A----B
              \
               C----D (feature)
```

Your teammate updated `main`:

```
main ----A----B----E----F
```

You run:

```bash
git checkout feature
git merge main
```

New Git history:

```
main ----A----B----E----F
              \         \
               C----D----M (merge commit)
```

### ⭐ Used when:
- Team projects
- You don't want to rewrite commit history
- You want a clear and traceable timeline

---

## 🟧 git rebase

### 📌 What it does:
- Moves your branch on top of another branch
- Rewrites commit history
- Makes linear history

### 🧠 When you use it:
- When you want a clean history
- Before merging PRs
- When you're the only developer modifying the branch

### 📘 Example (Same Scenario but with rebase)

```bash
git checkout feature
git rebase main
```

Feature branch commits are "replayed" on top of `main`.

New history:

```
main ----A----B----E----F----C'----D'
```

(' means new commit IDs)

### ⭐ Used when:
- To keep history clean
- Before creating a Pull Request
- When working alone on a branch

---

## 🎯 Real-Time Analogy

| Command | Analogy |
|---------|---------|
| **merge** | "Add your pages to the existing story as a new chapter." |
| **rebase** | "Rewrite your chapter so it looks like you wrote it after the latest chapter." |

---

## ⚠️ Golden Rule (Interview Must-Say)

> 👉 **NEVER rebase on a public/shared branch**  
> Because it rewrites history → breaks teammates' workflows.

---

# 🔥 2. git revert — Safest Way to Undo (Creates a New Commit)

---

## 🟩 git revert

### 📌 What it does:
- Undoes a commit by creating a new opposite commit
- Does not change history
- Safe for shared branches like `main`

### 📘 Real-Time Example

Someone pushed a bad commit to `main`:

```
Commit 10: Removed production config by mistake
```

You want to undo it.

```bash
git revert <commit-hash>
```

Git creates a new commit:

```
Commit 11: Revert "Removed production config"
```

### ⭐ When used:
- Undo mistakes on shared branches
- Production fixes
- When you must preserve history

### 🔥 Real-Time Scenario

You deploy a bad commit to production. Instead of rewriting history:

```bash
git revert c7f190
git push origin main
```

→ CI/CD deploys a fix automatically.

---

# 🔥 3. git reset — Changes History (Dangerous)

---

## 🟥 git reset

It moves your HEAD to another commit. It overwrites history → dangerous for shared branches.

There are 3 types:

---

## 3.1️⃣ git reset --soft

**Keeps:**
- changes in staging

**Moves HEAD only.**

**Example:**  
You want to "undo" last commit but keep all files staged.

```bash
git reset --soft HEAD~1
```

---

## 3.2️⃣ git reset --mixed (default)

**Keeps:**
- changes in working directory

**Unstages them.**

```bash
git reset HEAD~1
```

---

## 3.3️⃣ git reset --hard

⚠️ **Deletes working directory changes**  
⚠️ **Irreversible without backup**

**Example:**  
You want to discard all local changes:

```bash
git reset --hard HEAD~1
```

or

```bash
git reset --hard origin/main
```

---

## 🎯 Real-Time Scenario (git reset)

You accidentally committed 100MB log files. You want to remove them without preserving changes:

```bash
git reset --hard HEAD~1
```

---

# 🔥 Summary Table (Perfect for Interviews)

| Command | Purpose | Rewrites History? | Safe for Shared Branch? | Real Use Case |
|---------|---------|-------------------|------------------------|---------------|
| **git merge** | Combine branches | ❌ No | ✅ Yes | Team merging workflows |
| **git rebase** | Linear clean history | ✅ Yes | ❌ No | Clean PR before merge |
| **git revert** | Undo a commit safely | ❌ No | ✅ Yes | Fix prod issue without breaking history |
| **git reset** | Move HEAD & modify history | ✅ Yes | ❌ No | Undo local commits |

---

# 🧪 Real-Time Hands-On Example (All Commands)

---

## Step 1 — Create a feature branch

```bash
git checkout -b feature/login
```

---

## Step 2 — Fix commits (reset)

```bash
git reset --soft HEAD~1
# rewrite commit message or modify files
```

---

## Step 3 — Clean history (rebase)

```bash
git rebase main
```

---

## Step 4 — Merge clean branch

```bash
git merge feature/login
```

---

## Step 5 — Production bug found → revert

```bash
git revert <commit-hash>
git push main
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

