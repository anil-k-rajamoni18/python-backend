# 🛡️ Python Exception Handling

### ✅ What is an Exception? What is an Error?

> Error: A problem in the program that causes it to stop the execution. 
- Examples: SyntaxError, IndentationError.

> Exception: An error that occurs during runtime, which can be handled using code.

- Python uses exception handling to manage such events without crashing the program.

**🤔 Why Do Exceptions Occur?**
- Invalid user input
- File not found
- Division by zero
- Invalid operations
- Type mismatch, etc.


## 🧯 What is Exception Handling?
- Mechanism to catch and handle exceptions during runtime.
- Prevents program from crashing unexpectedly.
- Helps build robust and user-friendly applications.
- Ensures that the flow of the program doesn't break when an exception occurs.

**🚫 Without Exception Handling**
```python
x = int(input("Enter number: "))
y = int(input("Enter divisor: "))
print("Result:", x / y)  # Will crash if y = 0
```

**✅ With Exception Handling**
```python
try:
    x = int(input("Enter number: "))
    y = int(input("Enter divisor: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

---

## 🔄 try-except
- The try block is used for code that might raise an error.
- The except block handles those errors.
- A try block can have multiple except clauses, but only one will run if an exception occurs.

```python
try:
    # Risky code
except ExceptionType:
    # Handler code
```

**Example-1**

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("❌ Please enter a valid integer.")
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
```

**Example-2**
```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print("File content:", content)
except FileNotFoundError:
    print("❌ File not found.")
except PermissionError:
    print("❌ You do not have permission to open this file.")
finally:
    print("🔚 Done trying to open the file.")
```


**Example-3: Given a list, catch an IndexError if trying to access an out-of-range element.**
```python
my_list = [1, 2, 3]
try:
    print(my_list[5])
# Your except block here
```

**Example-4**
```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a number.")
```

**Example-5**
```python
try:
    x = int("abc")  
    y = "2" + 3      
except ValueError:
    print("ValueError occurred!")
except TypeError:
    print("TypeError occurred!")
```

---

## 🧱 Nested Try Blocks – When to Use?
- When you want to isolate risky sections of code inside larger blocks.
- Useful when handling multiple levels of exceptions separately.

```python
try:
    num = int(input("Enter a number: "))
    try:
        result = 10 / num
        print(result)
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero!")
except ValueError:
    print("Outer: Please enter a valid number!")
```

- **User Input + Calculation**
```python
try:
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        result = 100 / num
        print("Result:", result)
    except ValueError:
        print("That's not a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except Exception as e:
    print("🔴 An unexpected error occurred:", str(e))
```

- **File Reading & Data Conversion**
```python
try:
    file = open("data.txt", "r")
    try:
        data = file.read()
        number = int(data.strip())  # May raise ValueError
        print("Number:", number)
    except ValueError:
        print("Could not convert file content to an integer.")
    finally:
        file.close()
        print("📁 File closed.")
except FileNotFoundError:
    print("File not found.")
```
> Outer try handles file access (FileNotFoundError).
> Inner try handles data parsing (ValueError).

- **File Handling with JSON Parsing**
```python
import json

try:
    with open("config.json", "r") as f:
        try:
            config = json.load(f)
            print("✅ Config loaded:", config)
        except json.JSONDecodeError:
            print("Invalid JSON format.")
except FileNotFoundError:
    print("config.json file not found.")
```

---
## 🧩 try-except-else
- else runs if no exception occurs in try.

- `try` block: Code that might raise an exception.
- `except` block: Runs if an exception occurs.
- `else` block: Runs only if no exception was raised in the try block.
- `finally` (optional): Runs no matter what, for cleanup.

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"Good input: {value}")
```
**When to Use else:**
- To write code that should only run if try succeeded.
- Keeps your logic cleaner by separating normal code from error handling.

**Division with else**
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("❌ Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("❌ You can't divide by zero.")
else:
    print("✅ Success! Result is:", result)
```

---
## 🔚 try-finally
- finally block runs no matter what (even if there's a return or exception).
- Used for cleanup tasks (e.g., closing files, releasing resources, database connection).
```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("❌ File not found.")
else:
    print("📄 File content:")
    print(f.read())
    f.close()
```
---
## 🧭 Order of Exceptions
- Always catch specific exceptions first, then general ones.
- Python matches the first compatible except block.

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception:
    print("General error handler.")
```

---
## 👨‍💻 User Defined Exceptions
- Create custom exception classes by inheriting from Exception.

**steps**
- Create a class that extends Exception.
- Add a constructor with one parameter.
- Call the parent constructor with that parameter.

```python
class StudentNotFoundException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
```

```python
class InvalidAgeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)
```

---
## 🚨 Raising Exceptions Manually
- Use raise to trigger an exception.
- You can raise a built-in or user-defined exception, with an optional custom message.
- It's often used to enforce rules or handle custom error cases.


```python
age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
``` 

```python
username = ""
if not username:
    raise Exception("Username must not be empty")
```

```python
class CustomError(Exception):
    pass

def check_value(val):
    if val != "Python":
        raise CustomError("Only 'Python' is allowed!")

check_value("Java")  # Raises CustomError
```
---

### 📁 Hands on Question
**Develop Secure File Uploader and Processor**
A command-line tool that:
- Takes file name input from the user
- Checks file validity (existence, type, format)
- Reads data from the file
- Processes file content
- Handles all exceptions (e.g., file not found, wrong format, user errors)
- Uses try-except, else, finally, raise, custom exceptions, and nested try
