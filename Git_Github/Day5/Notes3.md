# 📘 **GitHub Actions & CI/CD Fundamentals**


---

# 🌟 **1. What is GitHub Actions?**

GitHub Actions is a **CI/CD and automation platform** that allows you to define workflows triggered by GitHub events.

### **Key Concepts:**

* **Workflow:** Automation defined in a YAML file
* **Job:** Collection of steps run on a specific runner
* **Step:** Individual task in a job (runs a script or action)
* **Action:** Reusable component that performs a task (official, community, or custom)
* **Runner:** Server executing jobs (GitHub-hosted or self-hosted)

**Industry Scenario:** Every PR triggers a workflow that runs tests, builds Docker images, and deploys staging apps.

---

# 🔹 **2. Workflow Triggers**

Workflows can be triggered by:

* **push** → commits pushed to a branch
* **pull_request** → PR opened or updated
* **schedule** → cron jobs
* **workflow_dispatch** → manual trigger
* **release** → on new release creation

Example:

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

---

# 🔹 **3. Workflow Structure**

Workflows are defined in `.github/workflows/<name>.yml`

### **Basic Example:**

```yaml
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install Dependencies
        run: npm install
      - name: Run Tests
        run: npm test
```

**Explanation:**

* `checkout` → pulls code
* `setup-node` → sets up Node.js environment
* `run` → executes shell commands

---

# 🔹 **4. Common GitHub Actions Topics**

## **4.1 Jobs & Steps**

* A workflow can have **multiple jobs** running sequentially or in parallel
* Each job can have multiple **steps**
* Jobs can depend on previous jobs using `needs`

## **4.2 Matrix Builds**

Run the same job across multiple environments

```yaml
strategy:
  matrix:
    node: [16,18]
```

Useful for testing on multiple Node versions or OSes.

## **4.3 Secrets & Environment Variables**

* Use `secrets` to store tokens, API keys, passwords
* Access in workflow:

```yaml
- run: echo ${{ secrets.MY_SECRET }}
```

## **4.4 Caching**

* Speed up builds by caching dependencies

```yaml
- name: Cache Node Modules
  uses: actions/cache@v3
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('package-lock.json') }}
```

## **4.5 Notifications**

* Slack, Teams, email notifications can be integrated via actions

---

# 🔹 **5. CI/CD Pipelines with GitHub Actions**

### **Continuous Integration (CI)**

* Run tests and lint on every PR or push
* Prevent broken code from merging

### **Continuous Deployment (CD)**

* Build Docker images
* Deploy to staging or production
* Automatic rollback on failure

### **Real-World Scenario:**

* On `main` branch push:

  1. Build backend and frontend
  2. Run tests
  3. Build Docker image
  4. Push image to container registry
  5. Deploy to Kubernetes staging cluster

---

# 🔹 **6. Advanced Topics**

## **6.1 Reusable Workflows**

* DRY workflows, reference reusable workflow across repos

```yaml
uses: org/repo/.github/workflows/ci.yml@main
```

## **6.2 Conditional Steps**

* Run steps based on conditions

```yaml
if: github.event_name == 'push'
```

## **6.3 Self-Hosted Runners**

* Use custom servers for specific workloads
* Can run on internal network for security

## **6.4 Artifacts**

* Upload build artifacts to be used in later jobs

```yaml
- uses: actions/upload-artifact@v3
  with:
    name: build
    path: ./build
```

## **6.5 Matrix & Parallelization**

* Run tests on multiple OS versions or languages concurrently
* Reduce CI time significantly

---

# 🧪 **7. Hands-On Tasks**

1. Create a workflow triggered on push to main
2. Run lint and unit tests using Node.js or Python
3. Add caching for dependencies
4. Upload build artifacts
5. Trigger a workflow manually using `workflow_dispatch`
6. Configure a secret and use it in the workflow

---

# 🏆 **8. Mini Project — Deploy a Sample App via GitHub Actions**

1. Create a sample web app (Node, Python, or static site)
2. Push code to GitHub
3. Create workflow:

   * Checkout code
   * Install dependencies
   * Run tests
   * Build project
   * Deploy to GitHub Pages or staging server
4. Add matrix strategy to run tests across multiple Node/Python versions
5. Add notifications to Slack or email

### **Outcome:**

* Your PR triggers CI tests automatically
* Successful push triggers CD deployment
* You experience **end-to-end GitHub Actions automation** like real SDE-II engineers

---

# 🎯 **Key Takeaways**

* GitHub Actions is flexible and integrates deeply with GitHub repo events
* Workflows can automate testing, deployment, and more
* Secrets, caching, matrix builds, artifacts are essential for production-grade CI/CD
* Hands-on practice helps simulate real-world engineering workflows
