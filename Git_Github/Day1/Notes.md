# **Day 1 — Git Fundamentals (Basics to Solid Foundation)**



---

# 🚀 **1. Installing Git & Configuring It**

## **Why Install Git?**

Git is the most widely used version control system in modern software teams. It helps teams collaborate, track changes, manage releases, and maintain clean code history.

## **Installation**

* **Windows** → Install via Git for Windows
* **Mac** → `brew install git`
* **Linux** → `sudo apt-get install git` or distro equivalent

## **Git Configuration Levels**

| Level      | Scope             | Location         |
| ---------- | ----------------- | ---------------- |
| **System** | All users & repos | `/etc/gitconfig` |
| **Global** | Current user      | `~/.gitconfig`   |
| **Local**  | Specific repo     | `.git/config`    |

### **Common Config Commands**

```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
git config --global core.editor "code --wait"
```

### **Real-Time Example**

When working in a corporate setting, your Git global config uses your company email. But if you contribute to open-source projects, you may override with a **local** config using your personal email.

---

# 📂 **2. Repository Basics (init, clone, add, commit)**

## **What Is a Repository?**

A Git repo is a directory with version control enabled.

### **Create a New Local Repo**

```bash
git init
```

**Industry Scenario:** You are working on a new microservice. Before starting coding, initialize a repo to track every change.

### **Clone an Existing Repo**

```bash
git clone https://github.com/example/project.git
```

**Real-World Scenario:** On your first day at a company, your tech lead gives you a repo link to get started.

### **Add Files to Staging**

```bash
git add file.txt
git add .
```

### **Commit Files**

```bash
git commit -m "Added login feature"
```

**Industry Example:** Commit messages follow standards (Conventional Commits), example:

```
feat(auth): add JWT login validation
```

---

# 🔄 **3. Git File Lifecycle**

Understanding file lifecycle is a core Git skill.

| State         | Meaning               |
| ------------- | --------------------- |
| **Untracked** | File not yet in Git   |
| **Staged**    | File added to index   |
| **Committed** | Saved to repo history |

### Workflow Example

1. You create `app.js` → **untracked**
2. Run `git add app.js` → **staged**
3. Run `git commit -m "Add app entry point"` → **committed**

**Industry Scenario:** Before raising a Pull Request, developers ensure only the required files move from untracked → staged → committed.

---

# 🙈 **4. .gitignore & Patterns**

## **Purpose of .gitignore**

To prevent unnecessary files from being pushed to a repo.

### **Common Example Patterns**

```
node_modules/
.env
*.log
dist/
```

### **Real-Time Scenario**

In a Node.js microservice:

* `node_modules/` is huge and should not be versioned
* `.env` contains secrets
* Logs and build outputs do not belong in Git

---

# 🌿 **5. Branch Basics**

## **Why Branch?**

Allows developers to work on features independently without affecting main code.

### **Create a Branch**

```bash
git branch feature/login
```

### **Switch Branch**

```bash
git switch feature/login
```

### **Delete Branch**

```bash
git branch -d feature/login
```

### **Industry Scenario**

When working in a CI/CD pipeline:

* Developers create **feature branches**
* Branches go through PR review
* When merged into `main`, a new build/deployment is triggered

---

# 🕒 **6. Viewing Commit History**

## **Useful Log Commands**

```bash
git log
git log --oneline
git log --graph --decorate --all
```

### **Real-Time Example**

Before deploying a release, DevOps engineers check commit logs to understand which features or bug fixes are included.

---

# 🧪 **Important Commands Summary**

```bash
git init
git clone
git add
git commit -m
git status
git log --oneline
git branch
git switch
```

---

# 🎯 **Conclusion**

Day 1 covers all foundational concepts required for effective Git usage. With these, you can confidently create repos, track changes, manage branches, and collaborate with a team.

Continue practicing by creating a demo project and performing full Git workflows.

---

# 🧪 **Hands-On Tasks**

## **1. Initialize a Git Repo From Scratch**

* Create a new folder: `mkdir my-git-demo && cd my-git-demo`
* Initialize Git → `git init`
* Create a file and commit it.

**Real Example:** When starting a new internal tool or automation script, engineers begin with a fresh repo.

## **2. Track Files & Make Commits**

* Create `readme.md`
* Track: `git add readme.md`
* Commit: `git commit -m "Initial project setup"`

**Industry Scenario:** Every commit should represent a meaningful change—useful during audits, code reviews, and deployments.

## **3. Create & Switch Branches**

```bash
git branch feature/about
git switch feature/about
```

**Real-Time Scenario:** Frontend teams create branches for UI components, backend teams for microservice enhancements.

## **4. Use .gitignore for IDE Files**

Typical IDE files to ignore:

```
.vscode/
.idea/
*.iml
target/
```

**Industry Example:** Accidental commits of IDE files cause merge conflicts in team environments.

---

# 🧩 **Mini Project: Local Portfolio Repo**

Create a simple portfolio project locally:

## **Steps:**

1. Create repo folder: `mkdir my-portfolio && cd my-portfolio`

2. Run `git init`

3. Add files:

   * `about.txt`
   * `projects.txt`
   * `contact.txt`

4. Track and commit in stages:

   ```bash
   git add about.txt
   git commit -m "Add about section"

   git add projects.txt
   git commit -m "Add projects list"

   git add contact.txt
   git commit -m "Add contact information"
   ```

5. Create branches:

   * `git branch feature/ui`
   * `git switch feature/ui`

6. Make changes & commit.

