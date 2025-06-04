## 📌 Virtual Environment in Python
- A virtual environment (venv) is an isolated environment for Python projects. 
- It allows you to manage dependencies separately for each project, avoiding conflicts between different packages or versions.
    - Think of it as a sandbox for your Python project.
    - It uses its own installation directories and doesn’t share libraries with other environments or the global Python interpreter.

--- 
## **Importance & Usage**
**✅ Why it's important:**
    - Dependency Isolation: Keeps project dependencies separate.
    - Version Control: Avoids version conflicts across projects.
    - Cleaner Development: Reduces risk of breaking global packages.
    - Portability: Makes it easier to share projects (via requirements.txt).

**🛠️ When to use:**
    - Every time you start a new Python project.
    - When working on multiple projects with different package requirements.
    - In collaborative development to ensure consistent environments.

---

## ⚙️ 3. How to Create a Virtual Environment

**🔸 A. Using `venv` (Standard Library - Python 3.3+)**
- Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

- macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

**🔸 B. Using `virtualenv` (More features, supports older versions)**
- First install: pip install virtualenv
- Windows:

```bash
virtualenv env
.\env\Scripts\activate
```

-  macOS/Linux:
```bash
virtualenv env
source env/bin/activate
```

**🔸 C. Using conda (Anaconda/Miniconda users)**
```bash
conda create --name myenv python=3.10
conda activate myenv
```

---

##  What is PIP?
- PIP stands for "Pip Installs Packages".
- It is the default package installer for Python, used to install, upgrade, and manage Python packages from the Python Package Index (PyPI).

**Usage of PIP**
- Install packages/libraries required for your project.
- Manage versions of packages.
- Generate and install from requirements.txt.
- Works with both virtual environments and system Python.

**Most Common PIP Commands**
| **Command**                         | **Description**                               |
| ----------------------------------- | --------------------------------------------- |
| `pip install package_name`          | Install a package                             |
| `pip uninstall package_name`        | Remove a package                              |
| `pip install package==version`      | Install specific version                      |
| `pip install -r requirements.txt`   | Install packages from file                    |
| `pip freeze`                        | List installed packages (with versions)       |
| `pip list`                          | Show all installed packages                   |
| `pip show package_name`             | Display package info                          |
| `pip install --upgrade package`     | Upgrade a package                             |
| `pip search keyword` *(deprecated)* | Search for packages (not recommended anymore) |


🔹 Disable cache (no .cache/pip usage):
 - pip install requests --no-cache-dir

🔹 Reinstall a package from scratch:
 - pip install --force-reinstall flask
🔹 Use a private package index:
 - pip install mypackage --index-url https://mypackage.repo/simple

🔹 Install without dependencies:
 - pip install django --no-deps

---

### Other Popular Python Packaging Tools
| **Tool**       | **Purpose**                                                            |
| -------------- | ---------------------------------------------------------------------- |
| **conda**      | Package/environment manager (used with Anaconda)                       |
| **pipenv**     | Combines `pip` and `venv`, creates `Pipfile` for dependency management |
| **poetry**     | Modern dependency manager, uses `pyproject.toml` for packaging         |
| **virtualenv** | Used to create virtual environments (especially pre-Python 3.3)        |
| **wheel**      | Binary packaging format (`.whl` files) for faster installs             |
| **setuptools** | Used for packaging and distributing Python projects                    |
| **twine**      | Securely upload Python packages to PyPI                                |


**📌 When to Use Which Tool?**
| **Scenario**                       | **Best Tool**          |
| ---------------------------------- | ---------------------- |
| Simple package management          | `pip`                  |
| Isolated project environments      | `venv`, `virtualenv`   |
| Data science + environments        | `conda`                |
| Modern project management + builds | `poetry`               |
| Uploading to PyPI                  | `twine` + `setuptools` |

---

## 🧑‍🎓 What is Poetry?
- Poetry is a Python tool for managing dependencies, packaging, and publishing Python projects — all in one.
> It's designed to simplify and standardize Python project management, especially for production-level and open-source development.

**✅ Why Use Poetry Instead of pip/venv?**

| Feature              | pip/venv                          | poetry                        |
| -------------------- | --------------------------------- | ----------------------------- |
| Dependency handling  | Manual                            | Automatic                     |
| Environment creation | Separate tool                     | Built-in                      |
| Lock file            | Manual (`pip freeze`)             | Automatic (`poetry.lock`)     |
| Packaging projects   | Requires `setuptools`, `setup.py` | Built-in via `pyproject.toml` |
| Publishing to PyPI   | Needs `twine`                     | Built-in                      |

#### **🚀 How to Install Poetry**

-  With the Official Installer
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
- Verify Installation:
```bash
poetry --version
```
---

### 📦 Basic Usage
- 1. Create a New Project: Creates a new project folder with structure and pyproject.toml.
```bash
poetry new myproject    
```

- 2. Add Poetry to Existing Project
```bash
cd existing_project
poetry init
```
- Interactive prompts help you set up pyproject.toml.

**📂 Working with Dependencies**
```bash
poetry add requests #  Add a Package

poetry add --dev black # poetry add --dev black

Remove a Package # poetry remove requests

````

**🛠️ Managing Environments**
```bash
poetry shell # Create/Activate Virtual Environment
```

```bash
poetry run python script.py #  Run Commands Inside Environment
```


```bash
poetry install #  Install All Dependencies (from lock file)
```

```bash
poetry update # Update poetry.lock with the latest versions
````

```bash
poetry build # Build your package
poetry publish --username __token__ --password <pypi-token> # ublish to PyPI
```

**File: pyproject.toml**
- This is the central config file in Poetry. It replaces setup.py, requirements.txt, and MANIFEST.in.

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = ""
authors = ["You <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0.0"
```

**💡 Tips & Best Practices**
- Always commit poetry.lock to version control.
- Use poetry run to ensure scripts use the correct virtual env.
- Use poetry version patch|minor|major to bump versions cleanly.
- Use in Docker with poetry export to create requirements.txt.

---

## 📦 Package in Python
- A package is a way to organize and group related modules (Python files) together into a directory structure.
    - Technically, a package is a directory with an __init__.py file.
    - It helps structure your codebase logically, especially for large projects.

**Usage and Importance**
| **Purpose**              | **Why It Matters**                                      |
| ------------------------ | ------------------------------------------------------- |
| **Code Organization**    | Break large codebases into smaller, manageable parts    |
| **Namespace Management** | Avoid name clashes by grouping related modules          |
| **Reusability**          | Share reusable logic across projects                    |
| **Distributability**     | Easily share or publish your code as libraries/packages |
| **Scalability**          | Structure projects cleanly as they grow                 |

**🧱 Basic Concepts**
| **Term**          | **Description**                                          |
| ----------------- | -------------------------------------------------------- |
| **Module**        | A single `.py` file with Python code                     |
| **Package**       | A directory containing modules and an `__init__.py` file |
| **Subpackage**    | A package inside another package                         |
| **Namespace**     | Scope that defines what names are visible                |
| **Import System** | Mechanism for loading modules and packages               |


### 🛠️ How to Create a Package
✅ Steps:
- Create a folder (your package)
- Add an __init__.py file (can be empty)
- Add modules (e.g., .py files)
- (Optional) Add subpackages and other files.

**📁 Example Structure:**
```yaml
my_package/
├── __init__.py
├── math_utils.py
├── string_utils.py
```

---

###  Understanding __init__.py, __all__, Namespaces, Imports

#### **🔸 `__init__.py`**
- Marks the directory as a package.
- Can run setup/init code or expose certain modules.
- Think of __init__.py as the front desk of your package.

```python
# my_package/__init__.py
from .math_utils import add

# importing the add function from the math_utils module into the package namespace.
```
- from .math_utils:
    - The . refers to "this package" (i.e., my_package).
    - math_utils is a module (math_utils.py) inside my_package.

- import add:
    - You're importing the add function from math_utils.py.

**Why do this?**
- It allows someone to access add directly from the package like this:
```python 
from my_package import add

# instead of
from my_package.math_utils import add
```

#### **🔸 `__all__`**
- Defines what gets imported with from package import *.
```python
__all__ = ['math_utils', 'string_utils']
```

#### 🔸 Namespaces
- Packages help prevent name conflicts.
- my_package.math_utils and my_package.string_utils keep code isolated.

#### 🔸 Relative vs Absolute Imports
| Type         | Example                                                 |
| ------------ | ------------------------------------------------------- |
| **Absolute** | `from my_package import math_utils`                     |
| **Relative** | `from . import math_utils` (relative to current module) |

> Use absolute imports for clarity in most cases.


---

### 📥 Importing Packages

**After creating a package:**
```python
from my_package import math_utils
print(math_utils.add(2, 3))
```
**Import from submodules:**
```python
from my_package.math_utils import add
```

**Inside the package (relative import):**
```python
# Inside string_utils.py
from .math_utils import add
```
---

### 📦 Distributing a Package
🔸 Steps:
- Add pyproject.toml or setup.py
- Build the package: python setup.py sdist or poetry build
- Publish to PyPI: twine upload dist/*
- Example setup.py:
```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
)
```

**✅ Best Practices**
- Always include __init__.py in packages.
- Use clear and consistent naming.
- Use absolute imports for clarity.
- Group related functionality into separate modules or subpackages.
- Document and structure your pyproject.toml or setup.py for distribution.

---
### ⚠️ Common Challenges in Python Packages

**1. Import Errors / ModuleNotFoundError**

Problem:
- ModuleNotFoundError: No module named 'x'
- Occurs when Python can't locate your package or module.

Causes:
- Package/module not in PYTHONPATH
- Misconfigured imports (wrong relative/absolute import)
- Missing __init__.py

Fixes:
- Use absolute imports
- Ensure the package is installed or accessible in the current environment
- Run scripts using python -m package.module to set the correct context

**2. Confusing Relative vs Absolute Imports**
- Problem: Using . or .. improperly in relative imports.
- Symptoms: Circular import errors, confusing import paths.
- Best Practice: Use absolute imports for clarity, and relative only within deeply nested modules.

**3. Name Conflicts**
- Problem: Module/package has the same name as a built-in or third-party library (e.g., email, random).
- Fix: Rename your module/package to something unique.

**4. Circular Imports**
Problem: Two modules import each other, leading to crashes or unexpected behavior.

Fix:
- Restructure code to avoid tight coupling
- Use late imports (inside functions) if restructuring is not feasible

---

## HandsOn Projects 
**Task Manager CLI**
- Develeop command-line project management app where users can create projects and add/view/update/delete tasks inside each project. 
- Each project stores tasks in a separate JSON file.

```python
task_manager/
│
├── main.py
├── projects/
│   └── <project_name>.json      # Dynamic JSON storage per project
│
├── core/                        # Main package
│   ├── __init__.py
│   ├── manager.py               # CLI interaction
│   └── validator.py             # Input validation functions
│
├── data/                        # Data handling package
│   ├── __init__.py
│   └── file_ops.py              # Read/write JSON
│
└── utils/
    ├── __init__.py
    └── date_tools.py            # Format/parse dates
```

**✨ Key Features:**
- Add a project
- Add tasks to a project
- View all tasks
- Mark task as completed
- Delete a task
- Data is stored in per-project JSON files


---
**Personal Expense Tracker (CLI-based)**
- Build a command-line expense tracker where users can add, view, delete, and summarize their expenses. 
- It stores data in a local CSV file and uses built-in modules like csv, datetime, and os.

```python
expense_tracker/
│
├── main.py                   # Main CLI entry point
├── data/
│   └── storage.csv           # CSV to store expenses
│
├── utils/
│   ├── __init__.py
│   ├── file_manager.py       # File handling logic
│   └── helpers.py            # Date parsing, formatting, etc.
│
└── features/
    ├── __init__.py
    ├── add_expense.py        # Function to add expense
    ├── view_expenses.py      # Function to list expenses
    └── summary.py            # Function to show summary (monthly, category-wise)
```