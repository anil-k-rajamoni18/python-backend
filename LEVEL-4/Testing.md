## 🧪 Testing in Python
- Testing is the process of verifying that code works as expected under various conditions. 
- It helps catch bugs early and ensures reliability as code evolves.

**🔍 Why Do We Need Testing?**
| Reason                             | Explanation                                     |
| ---------------------------------- | ----------------------------------------------- |
| 🔒 Ensures correctness             | Prevents bugs from going unnoticed.             |
| 🧼 Maintains code quality          | Encourages clean, modular code.                 |
| 🔁 Facilitates refactoring         | Allows safe code changes over time.             |
| 🚀 Boosts confidence in deployment | Confirms features work before release.          |
| 👨‍💻 Supports collaboration       | Makes it easier for teams to contribute safely. |

**Types of Testing in Python**
| Type                    | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| **Unit Testing**        | Test individual units (functions/methods) in isolation. |
| **Integration Testing** | Test interactions between multiple components.          |
| **System Testing**      | Test the whole system end-to-end.                       |
| **Acceptance Testing**  | Validate the system against user requirements.          |
| **Regression Testing**  | Ensure new code doesn’t break existing features.        |
| **Mock Testing**        | Simulate dependencies (like databases, APIs).           |


**Python Testing Tools**
- unittest – Built-in module.
- pytest – Popular third-party framework (recommended for simplicity and power).
- mock / unittest.mock – For mocking objects.
- nose2, doctest – Other options.

### **using unittest**
```python
def add(a: int, b: int) -> int:
    return a + b
```

```python
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

if __name__ == "__main__":
    unittest.main()
```

#### **🧪 unittest Methods**
**Lifecycle Methods**
- These are used to set up and tear down resources for each test.
| Method               | Purpose                                                           |
| -------------------- | ----------------------------------------------------------------- |
| `setUp(self)`        | Runs **before** each test method. Use to initialize test objects. |
| `tearDown(self)`     | Runs **after** each test method. Use to clean up.                 |
| `setUpClass(cls)`    | Runs **once before all tests** in the class. (Class method)       |
| `tearDownClass(cls)` | Runs **once after all tests** in the class. (Class method)        |


```python
@classmethod
def setUpClass(cls): ...

@classmethod
def tearDownClass(cls): ...
```

**Assertion Methods**
- These are the core of your test cases — they compare expected vs actual results.
| Method                      | Description                              |
| --------------------------- | ---------------------------------------- |
| `assertEqual(a, b)`         | Passes if `a == b`                       |
| `assertNotEqual(a, b)`      | Passes if `a != b`                       |
| `assertTrue(x)`             | Passes if `bool(x) is True`              |
| `assertFalse(x)`            | Passes if `bool(x) is False`             |
| `assertIs(a, b)`            | Passes if `a is b`                       |
| `assertIsNot(a, b)`         | Passes if `a is not b`                   |
| `assertIsNone(x)`           | Passes if `x is None`                    |
| `assertIsNotNone(x)`        | Passes if `x is not None`                |
| `assertIn(a, b)`            | Passes if `a in b`                       |
| `assertNotIn(a, b)`         | Passes if `a not in b`                   |
| `assertIsInstance(a, b)`    | Passes if `a` is instance of `b`         |
| `assertNotIsInstance(a, b)` | Passes if `a` is **not** instance of `b` |
| `assertAlmostEqual(a, b)`   | Passes if `a ≈ b` (used for floats)      |
| `assertGreater(a, b)`       | Passes if `a > b`                        |
| `assertLess(a, b)`          | Passes if `a < b`                        |


**Exception Handling in Tests**
- Use assertRaises() to check for expected exceptions.

```python
def divide(x, y):
    return x / y

class TestDivision(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
```

**Skipping Tests**
- Sometimes you may want to skip a test conditionally.
| Decorator or Method                       | Usage                          |
| ----------------------------------------- | ------------------------------ |
| `@unittest.skip(reason)`                  | Always skip.                   |
| `@unittest.skipIf(condition, reason)`     | Skip if condition is true.     |
| `@unittest.skipUnless(condition, reason)` | Skip unless condition is true. |


```python
@unittest.skip("Not implemented yet")
def test_feature(self):
    ...
```

**SubTests (Loop Testing)**
- Test multiple cases in one method without stopping at first failure.
```python
def test_multiple(self):
    for a, b in [(1, 1), (2, 2), (3, 3)]:
        with self.subTest(a=a, b=b):
            self.assertEqual(a, b)
```

**Example: Bank Account System**

- bank.py
```python
# bank.py

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
```

-  test_bank.py
```python
# test_bank.py

import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("=== Setting up BankAccount Test Class ===")

    def setUp(self):
        self.acc = BankAccount("Alice", 1000)

    def tearDown(self):
        del self.acc

    @classmethod
    def tearDownClass(cls):
        print("=== Done testing BankAccount ===")

    def test_initial_balance(self):
        self.assertEqual(self.acc.get_balance(), 1000)

    def test_deposit(self):
        self.acc.deposit(500)
        self.assertEqual(self.acc.get_balance(), 1500)

    def test_withdraw(self):
        self.acc.withdraw(300)
        self.assertEqual(self.acc.get_balance(), 700)

    def test_withdraw_exception(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(5000)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-50)

    def test_types(self):
        self.assertIsInstance(self.acc.owner, str)
        self.assertIsInstance(self.acc.balance, float)

    def test_subtest_balances(self):
        for amount in [100, 200, 300]:
            with self.subTest(amount=amount):
                self.acc.deposit(amount)
                self.assertTrue(self.acc.get_balance() >= 1000 + amount)

    @unittest.skip("Feature under development")
    def test_transfer(self):
        # Placeholder for future test
        pass

if __name__ == "__main__":
    unittest.main()

```

---
### pytest

A third-party testing framework that supports:
- Simple unit tests
- Fixtures for setup/teardown
- Assertions without boilerplate
- Parametrization, mocking, plugins, and more

**Why Use pytest?**
| Feature         | Benefit                             |
| --------------- | ----------------------------------- |
| 🧼 Clean Syntax | Just use `assert`                   |
| ⚡ Fast          | Minimal boilerplate                 |
| 🔄 Flexible     | Fixtures, plugins, parametrize      |
| 📈 Scalable     | Works for small scripts to big apps |




**📦 Install pytest**
```python
pip install pytest
```

**Running Tests**
```python
pytest test_file.py
```
- Auto-discovers files starting with test_ or ending in _test.py.
- Auto-discovers functions and classes prefixed with test.

**Example**
- calculator.py
```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```
- test_calculator.py
```python
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)
```

**🔄 Pytest Assertion Methods**
- No need to use assertEqual or assertTrue—just use Python’s assert keyword:

| `unittest`               | `pytest`                  |
| ------------------------ | ------------------------- |
| `self.assertEqual(a, b)` | `assert a == b`           |
| `self.assertTrue(x)`     | `assert x`                |
| `self.assertRaises(...)` | `with pytest.raises(...)` |


**Pytest Fixtures (like setUp/tearDown)**
- Fixtures provide reusable test data or setup logic.
- You can use them in any test just by passing the name.

```python
import pytest
from calculator import add

@pytest.fixture
def sample_data():
    return (5, 3)

def test_add_with_fixture(sample_data):
    a, b = sample_data
    assert add(a, b) == 8
```

**Parametrized Tests**
- Helps test multiple input combinations with minimal code.
```python
import pytest
from calculator import add

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_param(a, b, result):
    assert add(a, b) == result
```

**Skipping and Expected Failures**
```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_feature_x():
    ...

@pytest.mark.xfail(reason="Known bug")
def test_broken_logic():
    assert 1 == 2
```
---
### 🧪 Pytest Commands
| Command                     | Description                                      |
| --------------------------- | ------------------------------------------------ |
| `pytest`                    | Run all tests in current directory (recursively) |
| `pytest file.py`            | Run tests in a specific file                     |
| `pytest file.py::test_func` | Run a specific test function                     |
| `pytest dir/`               | Run all tests in a specific directory            |

**🔍 Verbosity & Output Control**

| Command              | Description                               |      |                          |
| -------------------- | ----------------------------------------- | ---- | ------------------------ |
| `pytest -v`          | Verbose output (shows each test name)     |      |                          |
| `pytest -q`          | Quiet mode (minimal output)               |      |                          |
| `pytest -s`          | Show `print()` output from test functions |      |                          |
| `pytest --maxfail=3` | Stop after 3 test failures                |      |                          |


**Debugging**
| Command                     | Description                              |
| --------------------------- | ---------------------------------------- |
| `pytest --pdb`              | Enter Python debugger on test failure    |
| `pytest --trace`            | Start debugger at the start of each test |
| `pytest --disable-warnings` | Suppress warnings output                 |


**Code Coverage (with pytest-cov)**
- Run with coverage:
```python
pytest --cov=your_module test_file.py

pytest --cov=your_module tests/


# --cov=your_module: the name of the Python module/package you want coverage info for.
# tests/: folder containing your test files.
```
| Command             | Description                     |
| ------------------- | ------------------------------- |
| `--cov-report=term` | Show coverage in terminal       |
| `--cov-report=html` | Generate HTML report            |
| `--cov-report=xml`  | Generate XML (CI/CD compatible) |


---

### Mocking with pytest + unittest.mock
- we can use unittest.mock with pytest to fake external dependencies.


**Most Used Methods in unittest.mock**
| Method                         | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `@patch()`                     | Replace real object/function with a mock     |
| `MagicMock()`                  | Create mock objects with flexible behavior   |
| `mock.return_value`            | Set the value a mock returns                 |
| `mock.side_effect`             | Simulate exceptions or dynamic return values |
| `mock.assert_called_once()`    | Ensure function was called once              |
| `mock.assert_called_with(...)` | Check parameters of function call            |



**Example-1: Mocking API Call**
```python
# weather.py

import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()

# test_weather.py

from unittest.mock import patch
from weather import get_weather

@patch("weather.requests.get")
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"temp": "22C"}
    
    result = get_weather("London")
    
    assert result["temp"] == "22C"
    mock_get.assert_called_once_with("https://api.weather.com/London")


```

**Example-2: Mocking a Class Method**
```python
# bank.py

class Bank:
    def get_balance(self, account_id):
        # Imagine a real DB call here
        return 1000


#  test_bank.py 
from unittest.mock import MagicMock
from bank import Bank

def test_get_balance_mock():
    mock_bank = Bank()
    mock_bank.get_balance = MagicMock(return_value=500)

    assert mock_bank.get_balance("123") == 500
    mock_bank.get_balance.assert_called_once_with("123")

```

**Example-3: Mocking a Function**
```python
# email_utils.py
def send_email(to, message):
    print(f"Sending email to {to}: {message}")
    return True


# test_email_utils.py
from unittest.mock import patch
from email_utils import send_email

@patch("email_utils.send_email")
def test_send_email(mock_send):
    mock_send.return_value = True
    assert send_email("user@example.com", "Hello") == True
    mock_send.assert_called_once_with("user@example.com", "Hello")

```

**Example-4: Using side_effect for Exception**
```python
from calculator import divide
from unittest.mock import patch

@patch("calculator.divide")
def test_divide_side_effect(mock_divide):
    mock_divide.side_effect = ValueError("Invalid")
    with pytest.raises(ValueError):
        divide(5, 0)
```

**Example-5: Mocking time or OS libraries**
```python
from unittest.mock import patch
import time

@patch("time.sleep", return_value=None)
def test_sleep_mock(mock_sleep):
    time.sleep(5)  # Won’t actually sleep
    mock_sleep.assert_called_once_with(5)
```

---

#### 🧾 Project: User Authentication System
```
Functionality:
    - Register user
    - Authenticate user
    - Store credentials in memory

📁 Project Structure
auth_project/
├── auth.py               # Auth logic with SQLite + hashing
├── test_auth.py          # Unit tests using pytest
├── users.db              # SQLite DB (generated at runtime)
└── requirements.txt      # Dependencies

```
