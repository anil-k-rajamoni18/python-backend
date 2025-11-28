
# 🟦 1. Functions, Arguments & Return Values

## ✔ What is a Function?

A block of reusable code that performs a specific task.

```python
def greet():
    print("Hello!")
```

## Why Functions Matter in Real Software?

- Promote reusability
- Improve maintainability
- Support modularity
- Allow testing individual components

## ✔ Types of Arguments

### 1. Positional Arguments

```python
def add(a, b):
    return a + b
```

### 2. Keyword Arguments

```python
add(b=5, a=2)
```

### 3. Default Arguments

```python
def greet(name="Guest"):
    print("Hello", name)
```

### 4. Variable-Length Arguments

**`*args`** → multiple positional values

```python
def total(*nums):
    return sum(nums)
```

**`**kwargs`** → multiple key-value values

```python
def printer(**info):
    print(info)
```

## ✔ Return Values

A function may:
- return one value
- return multiple values (as tuple)
- return nothing (None)

```python
def stats(nums):
    return max(nums), min(nums), sum(nums)
```

---

## 🔥 Real-Time / Industry Examples

### 🌐 1. API Helper Functions

```python
def fetch_user(id):
    response = requests.get(f"/users/{id}")
    return response.json()
```

### 📊 2. ML Feature Extraction

```python
def normalize(value, max_v):
    return value / max_v
```

### 🔧 3. DevOps Utilities

```python
def run_shell(cmd):
    return subprocess.getoutput(cmd)
```

---

## ⭐ BEST PRACTICES

- ✔ Functions should do one thing only
- ✔ Add docstrings
- ✔ Do not mutate arguments unless needed
- ✔ Keep functions short and readable

---

# 🟩 2. Lambda, Map, Filter, Reduce

These make your code concise, functional-style, and expressive.

## 🟦 Lambda Function

Anonymous functions (no name).

```python
square = lambda x: x * x
```

**Used heavily in:**
- ETL transformations
- Feature engineering
- Data filtering

---

## 🟨 map() — Apply a Function to All Items

```python
nums = [1,2,3]
doubles = list(map(lambda x: x*2, nums))
```

**Industry Example:**

Convert API response prices to floats:

```python
clean_prices = list(map(float, raw_prices))
```

---

## 🟧 filter() — Keep Items That Match Condition

```python
evens = list(filter(lambda x: x%2 == 0, nums))
```

**Industry Example:**

Get only failed logs:

```python
errors = list(filter(lambda log: "ERROR" in log, logs))
```

---

## 🟥 reduce() — Reduce Sequence to a Single Value

**Requires:**
```python
from functools import reduce
```

```python
total = reduce(lambda a,b: a+b, nums)
```

**Industry Example:**

Compute total size of files downloaded:

```python
total_size = reduce(lambda a,b: a+b["size"], files, 0)
```

---

# 🟦 3. Error Handling — try/except/else/finally

Proper error handling is essential for APIs, production apps, ML pipelines, and CI/CD workflows.

## ✔ Basic Structure

```python
try:
    risky_code
except SomeError:
    handle_error
else:
    runs_if_no_error
finally:
    always_runs
```

---

## 🟥 Types of Exceptions

| Exception | When It Occurs |
|-----------|----------------|
| `ValueError` | wrong type/format |
| `KeyError` | accessing missing dict key |
| `IndexError` | wrong list index |
| `ZeroDivisionError` | division by zero |
| `FileNotFoundError` | file missing |
| `TypeError` | incompatible types |

---

## 🔥 Real-Time / Industry Examples

### 🧵 1. API Error Wrapping

```python
try:
    data = requests.get(url).json()
except Exception:
    return {"error": "API failed"}
```

### 💾 2. File Handling

```python
try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Missing config file!")
```

### 🤖 3. ML Pipeline

```python
try:
    model.fit(X, y)
except ValueError:
    print("Bad input shape")
```

---

# 🟪 4. Custom Exceptions

Used when basic exceptions aren't enough.

```python
class InvalidAgeError(Exception):
    pass

def register(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")
```

## When Used in Industry?

- API validation errors
- Internal business rule violations
- Workflow failures
- Data validation in ML pipelines

---

# 🧪 HANDS-ON EXERCISES

## 1. Higher-Order Functions Practice

Write a function:

```python
apply_twice(func, value)
```

**Example:**

```python
apply_twice(lambda x: x+3, 5)
# Output → 11
```

---

## 2. Convert a List of Names to Uppercase

**Use:**
- `map()`
- `lambda`

---

## 3. Filter All Even Numbers

**Using:**
- `filter()`
- `lambda`

---

## 4. Create a Safe Division Function

```python
def safe_div(a, b):
   # return "Invalid" if division fails
```

**Must handle:**
- `ZeroDivisionError`
- `TypeError`

---

## 5. Error-Safe Input Loop

Ask for an integer:

```python
while True:
    try:
        age = int(input())
        break
    except:
        print("Invalid number, try again")
```

---

## 6. Write a Custom Exception

Create `WeakPasswordError`:

**Rules:**
- must contain upper/lowercase
- minimum 8 chars
- must contain digit

---

# 🧩 Mini Project — Contact Book CLI (Overview)

## ✔ Features

- Add contact
- Search contact
- Delete contact
- Save data in JSON
- Load data on startup
- Error-safe input
- Proper exception handling

---

## ✔ Data Structure (contacts.json)

```json
{
  "contacts": [
    {"name": "John", "phone": "12345", "email": "john@gmail.com"},
    {"name": "Sara", "phone": "54321", "email": "sara@gmail.com"}
  ]
}
```

---

## ✔ Core functions (industry-style)

```python
def load_contacts()
def save_contacts()
def add_contact()
def search_contact()
def delete_contact()
```

---

## Error Handling Required

- File missing → create new file
- Duplicate contact name → warn
- Invalid phone format
- Missing keys

---

## Optional Enhancements

- ✔ Edit contact
- ✔ Export to CSV
- ✔ Import from CSV
- ✔ Validate email format using regex