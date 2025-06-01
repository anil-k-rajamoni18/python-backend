# 📘 Python Functions

---

## Types of Programming Paradigms

- Programming paradigms are approaches to solving problems using programming languages. 
- They influence how developers design and organize their code.

### 1. **Imperative Paradigm**
- Describes *how* a program operates.
- Uses statements that change a program’s state.
- **Examples**: C, Python, Java

### 2. **Declarative Paradigm**
- Describes *what* the program should accomplish.
- Focuses on the result, not the process.
- **Examples**: SQL, HTML

### 3. **Procedural Paradigm**
- Subset of imperative.
- Based on procedure calls.
- Focuses on step-by-step instructions.

### 4. **Object-Oriented Paradigm (OOP)**
- Based on *objects* (instances of classes).
- Emphasizes encapsulation, inheritance, polymorphism.
- **Examples**: Java, Python, C++

### 5. **Functional Paradigm**
- Based on mathematical functions.
- Avoids changing-state and mutable data.


---

## What is Functional Programming?

Functional Programming (FP) is a paradigm where programs are constructed by applying and composing functions.

### 🔑 Key Concepts:
- **Pure Functions**: No side effects.
- **Immutability**: Data does not change.
- **First-class Functions**: Functions are treated like variables.
- **Higher-order Functions**: Functions that take or return other functions.
- **Recursion**: Looping through recursion instead of iteration.

---

## 🧩 Functions in Python

- A function is a structured block of code that executes only when it is called.

> Simply put, it’s like placing a group of related lines of code inside a container for reuse and better organization.
- ✅ Purpose: Designed to perform a specific task.
- 🎯 Abstraction: Functions serve as a level of abstraction, hiding implementation details.
- 📥 Inputs: They accept input in the form of parameters or arguments.
- 📤 Outputs: In Python, functions can return a result using the return statement.
- ⚠️ If no value is explicitly returned, the function returns None by default.

> A function helps break down complex problems into smaller, manageable parts. It promotes modularity and code reuse.

- In Python, functions are defined using the `def` keyword.


**📌 Syntax**:
```python
def function_name(parameters):
    # code block
    return result
```
**Example**
```python
def greet(name):
    return f"Hello, {name}!"
```

**🔄 Two Phases of Working with Functions**
1. Declaration (Definition)
    - This is where the function is created using the def keyword. You define the function's name, parameters, and the block of code it should execute.

2. Invocation (Calling)
    - This is when the function is actually executed by using its name followed by parentheses, optionally passing arguments.

> ⚠️ A function must be defined before it is called, otherwise Python will raise an error



**💡 Need of Functions**
- 📦 Modularity – Organize code into blocks.
- 🔁 Reusability – Write once, use many times.
- 🧹 Clean Code – Makes code readable and manageable.
- 🔍 Testing – Easier to test smaller blocks of code.

**👍 Advantages**
- Reduces redundancy
- Increases maintainability
- Helps in debugging and testing

**👎 Disadvantages**
- Overhead of function calls in some cases
- Poorly designed functions can lead to complexity
- Too many small functions can make flow hard to follow

---

**Example-1**

**❌ Without Function**
```python
c1 = 0
f1 = (c1 * 9/5) + 32
print(f"Fahrenheit: {f1}")

c2 = 25
f2 = (c2 * 9/5) + 32
print(f"Fahrenheit: {f2}")

c3 = 100
f3 = (c3 * 9/5) + 32
print(f"Fahrenheit: {f3}")
```

- 🔻 Drawbacks:
    - Code repetition
    - Harder to update or maintain
    - Less readable

**✅ With Function**
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures = [0, 25, 100]

for temp in temperatures:
    print(f"Fahrenheit: {celsius_to_fahrenheit(temp)}")
```
- ✔️ Benefits:
    - DRY principle (Don't Repeat Yourself)
    - Easy to modify logic in one place
    - Reusable for any temperature value
---

**Example-2**
- Validating if names are not empty and contain only alphabets
```python
# ❌ Without Function
name1 = "Alice"
if name1 and name1.isalpha():
    print(f"{name1} is a valid name.")
else:
    print("Invalid name")

name2 = "Bob123"
if name2 and name2.isalpha():
    print(f"{name2} is a valid name.")
else:
    print("Invalid name")

name3 = ""
if name3 and name3.isalpha():
    print(f"{name3} is a valid name.")
else:
    print("Invalid name")

# ************************************ #

# ✅ With Function
def is_valid_name(name):
    return name.isalpha() and len(name) > 0

names = ["Alice", "Bob123", ""]

for name in names:
    if is_valid_name(name):
        print(f"{name} is a valid name.")
    else:
        print("Invalid name")

```



### **🧪 Types of Functions**
**1. Built-in Functions**
- Provided by Python.
- Examples: print(), len(), type()

**2. User-defined Functions**
- Created by the programmer using def.

**3. Lambda Functions**
- Anonymous one-liner functions.
- Syntax: lambda arguments: expression
```python
add = lambda x, y: x + y
```

**4. Recursive Functions**
- A function that calls itself.
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

**5.Higher-order Functions**
- Takes one or more functions as arguments.
- Examples: map(), filter(), reduce()

---

## 🔢 Inputs to Functions
- Functions can receive data from the caller through **parameters**.
- Data to the functions is passed as arguments.
- Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
> A parameter is the variable listed inside the parentheses in the function definition.
> An argument is the value that is sent to the function when it is called.

```python
def greet(name): # params
    print(f"Hello, {name}!")

greet("Alice")  # args

# 👆 Here, "Alice" is the input (argument) passed to the function.
```

### Types of Arguments in Python
- Python supports multiple ways to pass arguments to functions.

**1. Positional Arguments**
- Arguments passed based on their position.
```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

**2. Keyword Arguments**
- Arguments passed with parameter names.
```python
def student_info(name, age):
    print(f"{name} is {age} years old.")

student_info(age=20, name="Ravi")
```
> 🟢 Advantage: Order doesn’t matter when using keywords.

**3. Default Arguments**
- You can set default values for parameters.
```python
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()           # Output: Welcome, Guest!
greet("Meera")    # Output: Welcome, Meera!
```
- Non-default arguments cannot follow default arguments in a function definition.
- **❌ Invalid:** 
```python
def greet(name="Guest", age):
    print(name, age)
```

- **✅ Correct:**
```python
def greet(age, name="Guest"):
    print(name, age)
```
> 🔑 Reason: Once you start assigning default values, all subsequent parameters must also have default values.

**4. Variable-length Arguments**

- a. **args (Non-keyworded)**
    - Used to pass a variable number of positional arguments.
    - Use *parameter to accept an unknown number of positional arguments — they are received as a tuple inside the function.

    ```python
    def total_marks(*marks):
        return sum(marks)

    print(total_marks(80, 90, 85))  # Output: 255

    ```

- b. **kwargs (Keyworded)**
    - Used to pass a variable number of keyword arguments.
    - They are received as a dictionary inside the function.

    ```python
        def print_details(**details):
            for key, value in details.items():
                print(f"{key}: {value}")

        print_details(name="Anu", age=23, city="Delhi")

    ```

---
## 🔄 Returning Values from a Function
- Functions can return single or multiple values using the return keyword.
- By default ,it returns None type

```python
def get_user():
    name = "Kiran"
    age = 30
    email = "kiran@example.com"
    return name, age, email

n, a, e = get_user()
print(f"Name: {n}, Age: {a}, Email: {e}")
```

- Python functions can return multiple values as a tuple, even if not explicitly mentioned.

```python
def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

result = calculate(10, 5)
print(result)           # Output: (15, 5, 50)
a, s, m = calculate(10, 5)
print(f"Add: {a}, Sub: {s}, Mul: {m}")
```

```python
def analyze_list(data):
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)
    return minimum, maximum, average

nums = [10, 20, 30, 40]
low, high, avg = analyze_list(nums)
print(f"Min: {low}, Max: {high}, Avg: {avg}"
```

**Swapping Values**
```python
def swap(a, b):
    return b, a

x, y = swap(5, 10)
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 5
```

---
## 🎯 Pass by Reference vs Pass by Value in Python
- Python’s variables are references to objects. The behavior depends on mutability.

**📌 Immutable Types (Pass-by-Value-like)**
```python
def modify_value(x):
    x = x + 5
    print("Inside Function:", x)

num = 10
modify_value(num)
print("Outside Function:", num)  # Output: 10
```
>  Here, num is not changed outside because integers are immutable.
> Integers are immutable. A new value is created inside the function, the original remains unchanged.

```python

def modify_string(s):
    s = s.upper()
    print("Inside function:", s)

name = "hello"
modify_string(name)
print("Outside function:", name)  # Output: "hello"

# 🧠 Strings are immutable, so any change creates a new string.
```


*8📌 Mutable Types (Pass-by-Reference-like)**
```python
def modify_list(lst):
    lst.append(100)
    print("Inside Function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside Function:", my_list)  # Output: [1, 2, 3, 100]
```
>  Lists are mutable, so the change is reflected outside the function.

```python
def add_entry(d):
    d["new_key"] = "new_value"
    print("Inside function:", d)

info = {"name": "Sam"}
add_entry(info)
print("Outside function:", info)  # Output includes "new_key"
```

**How to Prevent Changes (Copying)**
- If you want to avoid modifying the original object, pass a copy:
```python
def safe_update(lst):
    lst.append(999)
    print("Inside function:", lst)

original = [1, 2, 3]
safe_update(original.copy())
print("Outside function:", original)  # Output: [1, 2, 3]
```

**🔹 Shallow Copy**
- A shallow copy creates a new object, but does not create copies of nested objects inside the original. 
- Instead, it copies references to those nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99

print(original)  # [[99, 2], [3, 4]] — original is affected!

# ✅ shallow is a new outer list
# ❌ Inner lists are shared, not copied
```

**🔹 Deep Copy**
- A deep copy creates a new object and recursively copies all nested objects. 
- So the copy is entirely independent of the original.
```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print(original)  # [[1, 2], [3, 4]] — original is untouched

# ✅ deep is a new outer list
# ✅ Inner lists are also new copies
```

- Use copy.copy() for shallow copy
- Use copy.deepcopy() for deep copy

```python
org = [1,2,3]
dup = org.copy()  # create shallow copy 

print(id(org), id(dup)) # memory addr of outer objects
print(id(org[0]), id(dup[0])) # memory addr of inner objects

# update inner object 
dup[0] = 100

print(org, dup)
print(id(org[0]), id(dup[0]))
```

> 🔑Shallow copy matters only when mutating nested or mutable objects, not when reassigning elements.



**Summary Table**
| Data Type      | Behavior               | Mutable? | Affects Original? |
| -------------- | ---------------------- | -------- | ----------------- |
| `int`, `float` | Pass-by-value-like     | ❌        | ❌                 |
| `str`, `tuple` | Pass-by-value-like     | ❌        | ❌                 |
| `list`, `dict` | Pass-by-reference-like | ✅        | ✅                 |

---

## 🔍 Variable Scopes in Functions

**📌 What is Scope?**
- Scope refers to the **visibility** and **lifetime** of variables — where they can be accessed or modified.

**Python Scope Levels:**
- **Local**: Inside the current function
- **Enclosing**: In enclosing (outer) functions (for nested functions)
- **Global**: Declared at the top level of the script/module
- **Built-in**: Predefined names in Python (like `print`, `len`, etc.)

📦 Known as **LEGB Rule** — Local → Enclosing → Global → Built-in

**Example-1**
```python
def show_local():
    x = 10  # Local to this function
    print("Inside function:", x)

show_local()
# print(x)  # ❌ NameError: x is not defined (outside the function)
```


**Example-2**
```python
x = 50  # Global variable

def print_global():
    print("Inside function:", x)

print_global()
print("Outside function:", x)
```

**Exaample-3**
```python
def outer():
    message = "Hello from outer!"

    def inner():
        print(message)  # Enclosing scope

    inner()

outer()
```

**Example-4**
```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

**Example-5:  Shadowing Global with Local**
```python
x = "Global"

def test():
    x = "Local"  # This shadows the global x
    print("Inside function:", x)

test()
print("Outside function:", x)
```

**Example 7: Using nonlocal in Nested Functions**
```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Inner count:", count)

    inner()
    inner()

outer()
```


**Example 8: Modifying Global Variables**
```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```
> ⚠️ Use global with caution — it can make debugging harder.

---

## 🔁 Nested Functions
- A function defined inside another function is called a nested function (or inner function).
- ✅ Use Case: Useful for encapsulation, closures, and code modularity.

**Example-1: Basic Nested Function**
```python
def outer():
    def inner():
        print("Hello from the inner function!")
    inner()

outer()
```

**Example-2: Encapsulation: Helper Function Hidden Inside**
```python
def calculate_area(radius):
    def square(n):
        return n * n
    area = 3.14159 * square(radius)
    return area

print(calculate_area(5))  # Output: 78.53975

```

**Example-3: Nested Function Accessing Outer Variable**
```python
def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Aisha"))

```

**Example-5: Using Nested Functions to Avoid Repetition**
```python
def operate(x, y, op):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b

    if op == "add":
        return add(x, y)
    elif op == "subtract":
        return subtract(x, y)

print(operate(10, 5, "add"))       # Output: 15
print(operate(10, 5, "subtract"))  # Output: 5
```

**Example-6**
```python
def greet(name):
    def format_name(n):
        return n.capitalize()
    print("Hello,", format_name(name))

greet("john")  # Output: Hello, John
```

---

## 📦 Function Closures
A closure is a function that remembers the environment in which it was created — even after the outer function has finished executing.

**Key Properties:**
- Nested function
- Outer function returns inner function
- Inner function retains access to outer function’s variables

**Example-1**
```python
def outer(msg):
    def inner():
        print("Message:", msg)
    return inner

my_func = outer("Hello Closure!")
my_func()  # Output: Message: Hello Closure!
```
> Even though outer() has finished, inner() still has access to msg.

**Example-2: Real-Time Example: Logging**
```python
def logger(prefix):
    def log_message(msg):
        print(f"[{prefix}] {msg}")
    return log_message

info_logger = logger("INFO")
info_logger("Server started")  # Output: [INFO] Server started

```

**Example-3: Closure with Parameters**
```python
def power(exp):
    def calculate(base):
        return base ** exp
    return calculate

square = power(2)
cube = power(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
```

**Example-4: Closure for Creating Counters**
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # Output: 1
print(c())  # Output: 2
print(c())  # Output: 3
```

**Example-5: Nested Functions for Decorators**
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_hello():
    print("Hello!")

decorated = decorator(say_hello)
decorated()
```

**Example-6: Closure to Remember Function Calls**
```python
def tracker():
    calls = []
    def log_call(func):
        def wrapper(*args, **kwargs):
            calls.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper
    def get_calls():
        return calls
    return log_call, get_calls

log_call, get_calls = tracker()

@log_call
def foo():
    print("foo called")

@log_call
def bar():
    print("bar called")

foo()
bar()
foo()

print(get_calls())  # Output: ['foo', 'bar', 'foo']
```

**Example-7: Closure with Mutable Objects**
```python
def append_to_list():
    items = []
    def add(item):
        items.append(item)
        return items
    return add

adder = append_to_list()
print(adder(1))  # Output: [1]
print(adder(2))  # Output: [1, 2]
print(adder(3))  # Output: [1, 2, 3]
```

---

## 🔁 Recursion
- Recursion is when a function calls itself to solve smaller instances of the same problem.

**📌 Rules for Recursion:**
- Base Case – when to stop
- Recursive Case – function calling itself

**Example-1: Factorial**
```python
def factorial(n):
    if n == 0:
        return 1  # Base case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```


**Example-2: Fibonacci**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5
```

**Example-3: String Reversal Using Recursion**
```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"
```


**⚠️ Recursion vs Iteration**
| Feature     | Recursion                 | Iteration               |
| ----------- | ------------------------- | ----------------------- |
| Concept     | Function calls itself     | Uses loops              |
| Performance | Slower (stack overhead)   | Faster                  |
| Readability | Cleaner for tree problems | Better for simple loops |
| Risk        | Can cause stack overflow  | No such risk            |

**Best Practices for Recursion**
| Tip                          | Description                              |
| ---------------------------- | ---------------------------------------- |
| Use base case                | To stop the recursion                    |
| Avoid excessive depth        | Can cause `RecursionError`               |
| Prefer iteration when simple | It's usually more efficient              |
| Use memoization              | To optimize recursive solutions like Fib |


### More Questions On Recursion
1. Sum of Natural Numbers
2. String Reversal Using Recursion
3. Check Palindrome Recursively
4. Binary Search Using Recursion
5. Flatten Nested List (Recursive)
6. Greatest Common Divisor (GCD) — Euclid’s Algorithm

## Hands On Questions 

Project: ✅ Mini Online Store Simulation
- Use all concepts together:
    - Product functions (basic)
    - Cart and checkout using various function types
    - Variable scope for inventory
    - Closures for coupons/discounts
    - Recursion to explore product categories

