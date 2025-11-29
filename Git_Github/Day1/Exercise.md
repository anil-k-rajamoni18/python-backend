# Day 1 — Git Hands-On Practice Questions (Real-Time Scenarios)

## 🔹 1. Install & Configure Git

### Scenario 1: Corporate vs Personal Config

Your organization requires you to use the email `dev@company.com` for all company projects, but you also contribute to open source with `osscoder@gmail.com`.

#### Tasks:
1. Set your global Git username and email to personal credentials.
2. Inside a project folder `payment-service/`, override the email with the company email.
3. Verify all configuration levels.

---

## 🔹 2. Initializing and Cloning Repositories

### Scenario 2: New Microservice Setup

You are starting a new microservice named `order-service`.

#### Tasks:
1. Create a folder `order-service`.
2. Initialize a Git repo inside it.
3. Create a file `index.js` with `console.log("Order service started")`.
4. Stage and commit the file with a meaningful message.

### Scenario 3: Cloning a Team Repository

You join a new team. They give you this repo URL: `https://github.com/company/inventory-service.git`

#### Tasks:
1. Clone the repo.
2. Move inside the cloned directory.
3. Display the latest 5 commits in oneline format.

---

## 🔹 3. File Lifecycle & Staging Area

### Scenario 4: Accidentally Added File

Inside the repo, you create 3 files:

```
server.js
notes.txt
debug.log
```

#### Tasks:
1. Stage only `server.js`.
2. Leave the other files untracked.
3. Verify using `git status`.
4. Commit the staged file.

### Scenario 5: Modified but Not Staged

You modify `server.js` by adding comments.

#### Tasks:
1. Show the file lifecycle change to modified.
2. View the differences before staging.
3. Stage and commit only this file.

---

## 🔹 4. .gitignore Hands-On

### Scenario 6: Sensitive Files

Your project generates the following files:

```
.env
temp.log
node_modules/
build/
```

#### Tasks:
1. Create a `.gitignore` to ignore all the above.
2. Verify using `git status` that Git now ignores them.
3. Confirm that tracked files (if any) are not ignored.

### Scenario 7: Ignoring Specific File Patterns

Your project generates multiple log files like:

```
debug.log
error.log
app-2024.log
```

#### Task:
Write a `.gitignore` entry that ignores all `.log` files but still tracks `keep.log`.

---

## 🔹 5. Branching Basics

### Scenario 8: Feature Development

You must create a login feature.

#### Tasks:
1. Create a new branch `feature/login`.
2. Switch to it.
3. Add a file `login.js`.
4. Commit it.
5. Switch back to `main`.
6. Delete the feature branch after merge.

### Scenario 9: Hotfix Scenario

A production issue appears!

#### Tasks:
1. Create a branch `hotfix/critical-bug`.
2. Modify a file to fix the bug.
3. Commit changes.
4. Return to main branch.

---

## 🔹 6. Viewing Commit History

### Scenario 10: Who Broke the Build?

Your CI/CD pipeline failed after merging some commits.

#### Tasks:
1. View all commit messages in oneline mode.
2. Display commit history in graph format.
3. Identify the commit hash of the second-latest commit.
4. Show details of that commit.

### Scenario 11: Release Verification

Your lead asks:
> "Before deploying Release v1.2, get me a list of all commits made this week."

#### Task:
Use Git log filters (author/date/message as needed).

---

## 📝 Additional Notes

- All scenarios are designed to simulate real-world Git usage
- Practice each scenario multiple times to build muscle memory
- Try to complete tasks without looking at documentation first
- Document any commands you find particularly useful

## 💡 Tips for Success

1. **Read the scenario carefully** before starting the tasks
2. **Verify your work** after each step using `git status` or `git log`
3. **Experiment safely** - Git is forgiving with local repositories
4. **Keep a command reference** handy for quick lookup
5. **Practice regularly** - consistency is key to mastering Git

---

## 🔗 Quick Command Reference

```bash
# Configuration
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --local user.email "work@email.com"

# Repository basics
git init
git clone <url>
git status

# Staging and committing
git add <file>
git commit -m "message"

# Branching
git branch <branch-name>
git checkout <branch-name>
git branch -d <branch-name>

# History
git log --oneline
git log --graph
git show <commit-hash>
```