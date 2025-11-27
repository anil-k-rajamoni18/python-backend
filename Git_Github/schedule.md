# 🚀 5-Day Git & GitHub Basic → Advanced Mastery Plan

**Goal:** Become fully job-ready in Git, GitHub workflow, PR reviews, branching strategies, merge conflict resolution, and advanced commands.

---

## ✅ DAY 1 — Git Fundamentals (Basics to Solid Foundation)

### Topics

- Install Git, set config (global/local)
- Repository basics: init, clone, add, commit
- File lifecycle: untracked → staged → committed
- .gitignore & patterns
- Branch basics: create, switch, delete
- Viewing commit history

### Important Commands

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

### Hands-On Tasks

- Initialize a Git repo from scratch
- Track files, make commits
- Create & switch branches
- Use .gitignore for IDE files

### Mini Project

**💻 Local Portfolio Repo**  
Create a small project (even just text files) and manage full commit history.

---

## ✅ DAY 2 — Intermediate Git + GitHub Essentials

### Topics

- GitHub Remote: origin, upstream
- Push & Pull
- Fork vs Clone
- GitHub UI basics
- Issues & labels
- Markdown README editing
- SSH vs HTTPS authentication

### Important Commands

```bash
git remote add origin
git push
git pull
git fetch
git remote -v
```

### Hands-On Tasks

- Create GitHub repo
- Push local repo to GitHub
- Create issues, assign labels
- Write a professional README

### Mini Project

**🌐 Push Your Local Portfolio to GitHub**

---

## ✅ DAY 3 — Branching, Merging & Merge Conflicts (Deep Dive)

### Topics

- Git flow branching model
- Feature branches
- Fast-forward merges vs 3-way merges
- What causes merge conflicts?
- How to read conflict markers
- Resolving conflicts manually
- Git merge vs rebase (intro)
- Cherry-pick intro

### Important Commands

```bash
git merge
git merge --no-ff
git rebase
git rebase --continue
git cherry-pick
git stash
git stash pop
```

### Hands-On Tasks

- Create two branches and cause a merge conflict intentionally
- Resolve conflict and commit fix
- Try stash + applying changes
- Rebase a feature branch onto main

### Mini Project

**🔥 Conflict Resolution Simulation Project**  
You create branches featuring conflicting code. Practice: merge, conflict, resolve, rebase, cherry-pick.

---

## ✅ DAY 4 — PR Workflow, Code Reviews & GitHub Advanced

### Topics

#### Pull Request (PR) Best Practices

- Clear title & description
- Linked issues
- Small commits
- Atomic changes

#### PR review etiquette

- Approvals, re-reviews
- Using GitHub Actions for CI/CD checks
- CODEOWNERS

### Professional PR Review Rules & Suggestions

**Reviewer checklist:**

- ✔ Check code readability
- ✔ Request meaningful commit messages
- ✔ Ensure no secrets in code
- ✔ Validate folder structure
- ✔ Ensure tests pass
- ✔ Suggest improvements, not demands
- ✔ Provide examples when requesting changes
- ✔ Encourage small PRs
- ✔ Respect original author's context

**Common review suggestions:**

- "Consider renaming variable for clarity"
- "Can this logic be more modular?"
- "Add test coverage for this new method"
- "Document this function"

### Advanced GitHub Topics

- Branch Protection rules
- Required checks
- GitHub Projects & Wiki
- Releases & Tags
- GitHub CLI (gh)

### Important Commands

```bash
git tag
git push --tags
gh pr create
gh pr review
```

### Hands-On Tasks

- Create PR from feature → main
- Review your own PR from another GitHub account
- Setup branch protection rules
- Add CODEOWNERS

### Mini Project

**📝 PR Review Training Repository**  
You make multiple PRs and practice reviewing each.

---

## ✅ DAY 5 — Advanced Git Commands, Cleanup, Optimization & Full Project

### Topics

#### Advanced Git Commands

- Rebase (interactive)
- Squash & reword commits
- Commit amending
- Reflog for recovery
- Bisect for debugging
- Submodules
- Git hooks

### Advanced Commands List

```bash
git rebase -i HEAD~5
git commit --amend
git reflog
git reset --hard
git revert
git bisect start
git bisect good
git bisect bad
git submodule add
```

### Advanced Conflict Scenarios

- Rebasing + conflicts
- Cherry-pick conflicts
- Reverting conflicts
- Resolving binary file conflicts

### Hands-On Tasks

- Rewrite commit history with interactive rebase
- Recover deleted commits using reflog
- Debug code using git bisect
- Add a submodule (e.g., a UI library)

---

## 🏆 Final Real-World Project (Day 5)

### 🔥 Complete GitHub Collaboration Simulation Project

You will create a real multi-branch, multi-feature workflow:

#### Project Structure

- `main` (protected)
- `dev`
- `feature/auth`
- `feature/ui`
- `feature/database`
- `hotfix/typo-fix`

#### Project Tasks

1. Clone project
2. Add multiple features
3. Make PRs
4. Do reviews & request changes
5. Resolve conflicts across multiple branches
6. Squash commits before merge
7. Add tags for release v1.0.0
8. Write a changelog
9. Simulate bug fix on hotfix branch

---

## 🎯 After 5 Days You Will Be Able To:

- ✔ Work confidently with Git at a professional level
- ✔ Master branching, merging, rebasing, stashing
- ✔ Resolve ANY merge conflict
- ✔ Write clean PRs and perform professional reviews
- ✔ Use GitHub like a senior engineer
- ✔ Understand advanced commands & workflows
- ✔ Debug with bisect
- ✔ Recover lost commits
- ✔ Collaborate like a real dev team member