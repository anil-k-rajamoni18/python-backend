# 🐍 Python Crash Course — Complete Reference Guide

---

## 📑 Table of Contents

1. [Python Fundamentals](#1-python-fundamentals)
2. [Variables & Data Types](#2-variables--data-types)
3. [Operators](#3-operators)
4. [Strings (Deep Dive)](#4-strings-deep-dive)
5. [Control Flow](#5-control-flow)
6. [Functions](#6-functions)
7. [Data Structures](#7-data-structures)
8. [List Comprehensions & Generators](#8-list-comprehensions--generators)
9. [Object-Oriented Programming (OOP)](#9-object-oriented-programming-oop)
10. [Modules & Packages](#10-modules--packages)
11. [File I/O](#11-file-io)
12. [Exception Handling](#12-exception-handling)
13. [Iterators & Decorators](#13-iterators--decorators)
14. [Context Managers](#14-context-managers)
15. [Concurrency & Parallelism](#15-concurrency--parallelism)
16. [Type Hints & Annotations](#16-type-hints--annotations)
17. [Testing](#17-testing)
18. [Project Management — pipenv](#18-project-management--pipenv)
19. [Project Management — Poetry](#19-project-management--poetry)
20. [Resolving Vulnerabilities](#20-resolving-vulnerabilities)
21. [Commands Cheat Sheet](#21-commands-cheat-sheet)
22. [Important Websites & Links](#22-important-websites--links)

---

## 1. Python Fundamentals

### What is Python?
Python is a high-level, interpreted, dynamically-typed, and garbage-collected programming language created by **Guido van Rossum** (1991). It runs on CPython (reference implementation).

### Installation
```bash
# Check version
python --version          # or python3 --version

# Interactive REPL
python3

# Run a script
python3 script.py
```

### Python Zen (PEP 20)
```python
import this   # prints The Zen of Python
```

### PEP 8 — Style Guide Highlights
- 4 spaces for indentation (never tabs)
- Max line length: 79 characters (or 88 with Black formatter)
- Blank lines: 2 between top-level definitions, 1 between methods
- Naming: `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_CASE` for constants

### Python Memory Model
- Everything is an **object** with identity (`id()`), type (`type()`), and value
- Variables are **references** (labels), not boxes
- CPython uses **reference counting** + cyclic garbage collector

```python
a = [1, 2, 3]
b = a          # b and a point to the SAME list
b.append(4)
print(a)       # [1, 2, 3, 4]  ← shared reference

b = a.copy()   # shallow copy — now independent at top level
```

---

## 2. Variables & Data Types

### Built-in Types

| Category | Types |
|----------|-------|
| Numeric | `int`, `float`, `complex` |
| Sequence | `str`, `list`, `tuple`, `range` |
| Mapping | `dict` |
| Set | `set`, `frozenset` |
| Boolean | `bool` |
| Binary | `bytes`, `bytearray`, `memoryview` |
| None | `NoneType` |

```python
# Numeric
x: int   = 42
y: float = 3.14
z: complex = 2 + 3j

# Booleans (subclass of int)
t: bool = True    # int(True) == 1
f: bool = False   # int(False) == 0

# None
val = None
print(type(val))  # <class 'NoneType'>

# Type checking
print(isinstance(x, int))      # True
print(type(x) is int)          # True

# Dynamic typing
x = 10
x = "hello"   # perfectly valid — type changes at runtime
```

### Variable Unpacking
```python
a, b, c = 1, 2, 3
first, *rest = [1, 2, 3, 4, 5]   # first=1, rest=[2,3,4,5]
*init, last = [1, 2, 3, 4, 5]    # init=[1,2,3,4], last=5

# Swap without temp
a, b = b, a
```

---

## 3. Operators

### Arithmetic
```python
print(10 + 3)    # 13  — addition
print(10 - 3)    # 7   — subtraction
print(10 * 3)    # 30  — multiplication
print(10 / 3)    # 3.333... — true division (always float)
print(10 // 3)   # 3   — floor division
print(10 % 3)    # 1   — modulo
print(2 ** 10)   # 1024 — exponentiation
```

### Comparison & Logical
```python
print(5 == 5)    # True
print(5 != 4)    # True
print(5 > 3)     # True
print(5 is 5)    # True (identity) — use == for value equality

# Logical
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Chained comparison (Pythonic!)
print(1 < 2 < 3)   # True
```

### Bitwise
```python
print(0b1010 & 0b1100)   # 8  (AND)
print(0b1010 | 0b1100)   # 14 (OR)
print(0b1010 ^ 0b1100)   # 6  (XOR)
print(~0b1010)            # -11 (NOT)
print(1 << 3)             # 8  (left shift)
print(8 >> 2)             # 2  (right shift)
```

### Walrus Operator `:=` (Python 3.8+)
```python
import re
if m := re.search(r"\d+", "abc123"):
    print(m.group())   # 123
```

---

## 4. Strings (Deep Dive)

```python
# Creation
s1 = 'single'
s2 = "double"
s3 = """triple
double"""
s4 = r"raw\nstring"        # raw string — no escape processing
s5 = b"bytes literal"      # bytes, not str

# f-strings (Python 3.6+) — preferred
name, age = "AK", 30
print(f"Hello {name}, you are {age:.2f} years old")
print(f"{2 ** 10 = }")      # 2**10 = 1024  (Python 3.8+ self-documenting)

# Common methods
s = "  Hello, World!  "
print(s.strip())            # "Hello, World!"
print(s.lower())            # "  hello, world!  "
print(s.upper())            # "  HELLO, WORLD!  "
print(s.replace("World", "Python"))
print(s.split(","))         # ['  Hello', ' World!  ']
print("Python".startswith("Py"))   # True
print("Python".endswith("on"))     # True
print(",".join(["a", "b", "c"]))   # "a,b,c"
print("hello world".title())       # "Hello World"
print("abc" * 3)                   # "abcabcabc"

# Indexing & Slicing
s = "Python"
print(s[0])      # P
print(s[-1])     # n
print(s[1:4])    # yth
print(s[::-1])   # nohtyP  (reverse)
print(s[::2])    # Pto
```

---

## 5. Control Flow

### if / elif / else
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary (conditional expression)
status = "pass" if score >= 60 else "fail"
```

### for Loops
```python
# Iterate over a sequence
for i in range(5):
    print(i)         # 0 1 2 3 4

# range(start, stop, step)
for i in range(10, 0, -2):
    print(i)         # 10 8 6 4 2

# enumerate
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# zip
names = ["Alice", "Bob"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Loop control
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
else:
    print("Loop completed")   # only if no break
```

### while Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    data = input("Enter (q to quit): ")
    if data == "q":
        break
```

### match / case (Python 3.10+ — Structural Pattern Matching)
```python
command = "quit"
match command:
    case "quit":
        print("Quitting")
    case "help":
        print("Help menu")
    case _:
        print("Unknown command")

# Match on types and structures
point = (1, 0)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

---

## 6. Functions

```python
# Basic function
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# *args and **kwargs
def variadic(*args, **kwargs):
    print(args)    # tuple of positional args
    print(kwargs)  # dict of keyword args

variadic(1, 2, 3, name="AK", lang="Python")

# Keyword-only arguments (after *)
def connect(host, *, port=8080, timeout=30):
    pass

connect("localhost", port=3000)   # OK
# connect("localhost", 3000)     # TypeError!

# Positional-only arguments (before /) — Python 3.8+
def div(a, b, /):
    return a / b

# Lambda
square = lambda x: x ** 2
print(square(5))   # 25

# Higher-order functions
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))   # [2, 4]
doubled = list(map(lambda x: x * 2, nums))           # [2, 4, 6, 8, 10]

from functools import reduce
total = reduce(lambda a, b: a + b, nums)             # 15

# Closures
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c(), c(), c())   # 1 2 3
```

---

## 7. Data Structures

### Lists
```python
lst = [1, 2, 3, 4, 5]
lst.append(6)          # add to end
lst.insert(0, 0)       # insert at index
lst.extend([7, 8])     # merge another list
lst.remove(3)          # remove first occurrence of value
popped = lst.pop()     # remove & return last
popped = lst.pop(0)    # remove & return at index
lst.sort()             # in-place sort
lst.sort(reverse=True)
sorted_lst = sorted(lst, key=lambda x: -x)
lst.reverse()
print(lst.index(2))    # first index of value
print(lst.count(2))    # occurrences
lst.clear()
```

### Tuples
```python
t = (1, 2, 3)          # immutable sequence
t = 1, 2, 3            # parentheses optional
single = (42,)         # single-element needs trailing comma
print(t[0])            # 1
a, b, c = t            # unpack

# Named tuples
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)        # 10 20
```

### Dictionaries
```python
d = {"name": "AK", "lang": "Python", "version": 3.12}
d["age"] = 30                      # add/update
print(d.get("age", 0))            # safe access with default
print(d.keys())                    # dict_keys
print(d.values())                  # dict_values
print(d.items())                   # dict_items  (k, v pairs)
d.update({"city": "Hyderabad"})   # merge
del d["version"]                   # remove key
popped = d.pop("age", None)        # remove & return

# Dictionary unpacking (merge) — Python 3.9+
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2      # {"a": 1, "b": 2}
d1 |= d2              # in-place merge

# dict comprehension
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}

# defaultdict
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")   # no KeyError

# Counter
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(3))   # [('a', 5), ('b', 2), ('r', 2)]

# OrderedDict (Python 3.7+ dicts maintain insertion order by default)
from collections import OrderedDict
od = OrderedDict()
```

### Sets
```python
s = {1, 2, 3, 4}
s.add(5)
s.discard(10)          # no error if missing
s.remove(1)            # KeyError if missing

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)           # {1, 2, 3, 4}  — union
print(a & b)           # {2, 3}        — intersection
print(a - b)           # {1}           — difference
print(a ^ b)           # {1, 4}        — symmetric difference
print(a.issubset(b))   # False
print(a.issuperset(b)) # False

# frozenset (immutable, hashable)
fs = frozenset([1, 2, 3])
```

---

## 8. List Comprehensions & Generators

### List Comprehensions
```python
# [expression for item in iterable if condition]
squares   = [x**2 for x in range(10)]
evens     = [x for x in range(20) if x % 2 == 0]
matrix    = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# Dict & set comprehensions
d = {k: v for k, v in zip("abc", [1, 2, 3])}   # {'a':1, 'b':2, 'c':3}
s = {x**2 for x in range(5)}                     # {0, 1, 4, 9, 16}
```

### Generators (lazy evaluation)
```python
# Generator expression (uses () not [])
gen = (x**2 for x in range(1_000_000))   # no memory allocated yet
print(next(gen))   # 0 — pull one value at a time

# Generator function (uses yield)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(8)])   # [0, 1, 1, 2, 3, 5, 8, 13]

# yield from (delegation)
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1, 2], [3, 4])))   # [1, 2, 3, 4]
```

### itertools — Power Tools
```python
import itertools

list(itertools.count(10, 2))                # [10, 12, 14, ...]
list(itertools.cycle("AB"))                 # ['A','B','A','B',...]
list(itertools.repeat(5, 3))               # [5, 5, 5]
list(itertools.chain([1,2], [3,4]))        # [1,2,3,4]
list(itertools.islice(range(100), 5))      # [0,1,2,3,4]
list(itertools.permutations("AB"))         # [('A','B'),('B','A')]
list(itertools.combinations("ABC", 2))     # [('A','B'),('A','C'),('B','C')]
list(itertools.product([0,1], repeat=3))   # all 3-bit combinations
list(itertools.groupby("aabbcc",           # group consecutive
     lambda x: x))
```

---

## 9. Object-Oriented Programming (OOP)

### Classes & Instances
```python
class Animal:
    # Class attribute (shared)
    kingdom = "Animalia"

    def __init__(self, name: str, sound: str):
        # Instance attributes
        self.name  = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, sound={self.sound!r})"

    def __str__(self) -> str:
        return self.name


cat = Animal("Cat", "meow")
print(cat.speak())       # Cat says meow!
print(repr(cat))         # Animal(name='Cat', sound='meow')
```

### Inheritance
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "woof")
        self.breed = breed

    def speak(self) -> str:          # override
        return f"{self.name} ({self.breed}) says {self.sound}!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


rex = Dog("Rex", "Labrador")
print(rex.speak())       # Rex (Labrador) says woof!
print(isinstance(rex, Animal))   # True — MRO works correctly
```

### Multiple Inheritance & MRO
```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C):
    pass

d = D()
print(d.method())      # B  — follows MRO: D → B → C → A
print(D.__mro__)       # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, ...)
```

### Dunder (Magic) Methods
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):         return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):         return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):        return Vector(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar):       return self.__mul__(scalar)
    def __eq__(self, other):          return self.x == other.x and self.y == other.y
    def __lt__(self, other):          return abs(self) < abs(other)
    def __abs__(self):                return (self.x**2 + self.y**2) ** 0.5
    def __len__(self):                return 2
    def __getitem__(self, idx):       return (self.x, self.y)[idx]
    def __iter__(self):               return iter((self.x, self.y))
    def __repr__(self):               return f"Vector({self.x}, {self.y})"
    def __bool__(self):               return bool(self.x or self.y)
    def __hash__(self):               return hash((self.x, self.y))
```

### Properties, Classmethods & Staticmethods
```python
class Temperature:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5/9)

    @staticmethod
    def is_boiling(celsius: float) -> bool:
        return celsius >= 100


t = Temperature.from_fahrenheit(212)
print(t.celsius)      # 100.0
print(Temperature.is_boiling(100))   # True
```

### Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float
    label: str = field(default="origin", compare=False)

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(3.0, 4.0)
p2 = Point(0.0, 0.0, label="origin")
print(p1.distance_to_origin())   # 5.0
print(p1 > p2)                   # True  (order=True compares fields in order)
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self):
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self):      return 3.14159 * self.radius ** 2
    def perimeter(self): return 2 * 3.14159 * self.radius
```

---

## 10. Modules & Packages

### Importing
```python
import os
import os.path
from os import getcwd, listdir
from os.path import join, exists
import numpy as np                 # alias
from typing import Optional, List  # type utilities

# Lazy import (avoid circular)
def get_pandas():
    import pandas as pd
    return pd
```

### Creating a Package
```
my_package/
├── __init__.py          # makes it a package; can expose public API
├── core.py
├── utils.py
└── sub/
    ├── __init__.py
    └── helpers.py
```

```python
# __init__.py
from .core import MainClass
from .utils import helper_fn
__all__ = ["MainClass", "helper_fn"]   # controls `from pkg import *`
```

### `__name__ == "__main__"` Guard
```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

### Useful Standard Library Modules
| Module | Purpose |
|--------|---------|
| `os`, `os.path` | File system operations |
| `sys` | System info, argv, path |
| `pathlib` | OOP file paths |
| `re` | Regular expressions |
| `json` | JSON encode/decode |
| `csv` | CSV read/write |
| `datetime` | Date and time |
| `math`, `cmath` | Math functions |
| `random` | Random numbers |
| `collections` | deque, Counter, defaultdict, OrderedDict |
| `itertools` | Infinite & combinatoric iterators |
| `functools` | reduce, lru_cache, partial, wraps |
| `contextlib` | contextmanager, suppress |
| `typing` | Type hints |
| `dataclasses` | @dataclass decorator |
| `abc` | Abstract base classes |
| `enum` | Enumerations |
| `logging` | Logging framework |
| `argparse` | CLI argument parsing |
| `subprocess` | Run system commands |
| `threading`, `multiprocessing` | Concurrency |
| `asyncio` | Async I/O |
| `socket` | Low-level networking |
| `http.server` | Quick HTTP server |
| `urllib`, `http.client` | HTTP requests |
| `hashlib` | SHA, MD5 hashing |
| `secrets` | Cryptographically secure random |
| `sqlite3` | SQLite database |
| `pickle` | Object serialization |
| `copy` | Shallow and deep copy |
| `pdb` | Debugger |
| `timeit` | Code benchmarking |
| `unittest` | Unit testing |
| `zipfile`, `tarfile` | Archive files |
| `shutil` | High-level file operations |
| `tempfile` | Temporary files/dirs |

---

## 11. File I/O

### Text Files
```python
from pathlib import Path

# Write
Path("output.txt").write_text("Hello, AK!\n", encoding="utf-8")

# Read whole file
content = Path("output.txt").read_text(encoding="utf-8")

# Read lines
lines = Path("output.txt").read_text().splitlines()

# Append
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Another line\n")

# Read line by line (memory-efficient)
with open("large_file.txt", encoding="utf-8") as f:
    for line in f:
        process(line.strip())
```

### Binary & JSON
```python
import json

data = {"name": "AK", "skills": ["Python", "Node.js"]}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json") as f:
    loaded = json.load(f)

# Strings
s = json.dumps(data)
d = json.loads(s)
```

### CSV
```python
import csv

# Write
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows([{"name": "AK", "age": 30}])

# Read
with open("data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

### pathlib — Modern Path Handling
```python
from pathlib import Path

p = Path("/home/user/docs")
p.mkdir(parents=True, exist_ok=True)

log = p / "app.log"           # path joining with /
print(log.suffix)             # .log
print(log.stem)               # app
print(log.parent)             # /home/user/docs
print(log.exists())           # bool

# Glob
for py_file in p.glob("**/*.py"):
    print(py_file)
```

---

## 12. Exception Handling

```python
# Basic structure
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type/Value error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
    raise   # re-raise
else:
    print("No exception!")     # runs if no exception
finally:
    print("Always runs")       # cleanup code

# Custom Exceptions
class AppError(Exception):
    """Base exception for this app."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field   = field
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    pass

# Exception Groups (Python 3.11+)
try:
    raise ExceptionGroup("network errors", [
        ConnectionError("timeout"),
        OSError("DNS failed"),
    ])
except* ConnectionError as eg:
    print("Connection issues:", eg.exceptions)
except* OSError as eg:
    print("OS issues:", eg.exceptions)

# Context (chained exceptions)
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Config parse failed") from e
```

### Exception Hierarchy
```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── OSError (IOError, FileNotFoundError, PermissionError)
    ├── RuntimeError
    │   └── RecursionError
    ├── AttributeError
    └── ImportError
        └── ModuleNotFoundError
```

---

## 13. Iterators & Decorators

### Iterators Protocol
```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(3):
    print(n)   # 3 2 1
```

### Decorators
```python
import functools
import time

# Basic decorator
def my_decorator(func):
    @functools.wraps(func)      # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print(f"Before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After  {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name): return f"Hello {name}"

# Decorator with arguments
def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"Retry {attempt}/{times}: {e}")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def fetch_data(url): ...

# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

# lru_cache (memoization)
@functools.lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

print(fib(50))   # Fast!
```

---

## 14. Context Managers

```python
# Using with statement
with open("file.txt") as f:
    data = f.read()

# Multiple context managers
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

# Creating context managers with class
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # False = don't suppress exceptions

with Timer() as t:
    sum(range(1_000_000))

# Creating with contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

with managed_resource("DB connection") as conn:
    print(f"Using {conn}")

# suppress exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    Path("nonexistent.txt").unlink()
```

---

## 15. Concurrency & Parallelism

### Threading
```python
import threading

def worker(name, delay):
    import time
    time.sleep(delay)
    print(f"Worker {name} done")

threads = [
    threading.Thread(target=worker, args=(f"T{i}", i * 0.1))
    for i in range(5)
]
for t in threads: t.start()
for t in threads: t.join()

# Thread-safe with Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
```

### Multiprocessing (bypass GIL)
```python
from multiprocessing import Pool, cpu_count

def cpu_task(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(cpu_task, [10**6] * 8)
    print(results)
```

### asyncio (async/await)
```python
import asyncio
import aiohttp   # pip install aiohttp

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, u)) for u in urls]
        results = await asyncio.gather(*tasks)
    return results

asyncio.run(main())

# asyncio event loop fundamentals
async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)   # sentinel

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None: break
        print(f"Consumed: {item}")
```

### concurrent.futures (high-level)
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# I/O bound → ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_url, url): url for url in urls}
    for future in as_completed(futures):
        url    = futures[future]
        result = future.result()

# CPU bound → ProcessPoolExecutor
with ProcessPoolExecutor() as executor:
    results = list(executor.map(heavy_computation, data_list))
```

---

## 16. Type Hints & Annotations

```python
from typing import (
    Optional, Union, List, Dict, Tuple, Set,
    Callable, Iterator, Generator, Any,
    TypeVar, Generic, Protocol, TypedDict,
    Final, ClassVar, Literal, Annotated
)
from collections.abc import Sequence, Mapping

# Basic annotations
def greet(name: str, times: int = 1) -> str:
    return (name + "\n") * times

# Optional (= Union[X, None])
def find_user(uid: int) -> Optional[str]:
    return None

# Union (Python 3.10+: use X | Y)
def parse(val: int | str) -> int:
    return int(val)

# TypeVar & Generic
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

# TypedDict
class Config(TypedDict):
    host: str
    port: int
    debug: bool

# Protocol (structural subtyping)
class Drawable(Protocol):
    def draw(self) -> None: ...

# Final
MAX_SIZE: Final = 100

# Literal
Mode = Literal["r", "w", "a", "rb", "wb"]
def open_file(path: str, mode: Mode) -> None: ...

# Annotated (metadata)
from typing import Annotated
Positive = Annotated[int, "must be > 0"]

# Python 3.12+ — type alias statement
type Vector = list[float]

# mypy — static type checker
# pip install mypy
# mypy script.py
```

---

## 17. Testing

### unittest
```python
import unittest

class TestMath(unittest.TestCase):

    def setUp(self):             # run before each test
        self.values = [1, 2, 3]

    def tearDown(self):          # run after each test
        pass

    def test_sum(self):
        self.assertEqual(sum(self.values), 6)

    def test_type(self):
        self.assertIsInstance(self.values, list)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

### pytest (preferred)
```bash
pip install pytest pytest-cov
pytest tests/              # run all tests
pytest -v                  # verbose
pytest -k "test_login"     # filter by name
pytest --cov=myapp         # coverage
```

```python
# test_example.py
import pytest

@pytest.fixture
def user_data():
    return {"name": "AK", "role": "admin"}

def test_user_name(user_data):
    assert user_data["name"] == "AK"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected

def test_raises_on_negative():
    with pytest.raises(ValueError, match="negative"):
        validate_positive(-1)

# Mocking
from unittest.mock import MagicMock, patch

def test_service(monkeypatch):
    monkeypatch.setattr("myapp.db.query", lambda q: [])
    ...

@patch("myapp.external.api_call")
def test_api(mock_call):
    mock_call.return_value = {"status": "ok"}
    result = my_function()
    mock_call.assert_called_once()
```

---

## 18. Project Management — pipenv

### What is pipenv?
`pipenv` combines `pip` and `virtualenv` into one tool. It manages `Pipfile` (human-friendly) and `Pipfile.lock` (deterministic builds).

### Installation
```bash
pip install pipenv
# or (macOS)
brew install pipenv
```

### Basic Workflow
```bash
# Create new project / virtualenv
pipenv --python 3.12

# Install a package (adds to Pipfile)
pipenv install requests

# Install dev-only dependency
pipenv install --dev pytest black mypy

# Install all dependencies (from Pipfile.lock)
pipenv install

# Install exact locked versions (CI/production)
pipenv sync

# Remove a package
pipenv uninstall requests

# Activate virtual environment shell
pipenv shell

# Run a command inside the venv without activating
pipenv run python script.py
pipenv run pytest

# Exit virtualenv shell
exit

# Show dependency graph
pipenv graph

# Generate requirements.txt from lock file
pipenv requirements > requirements.txt
pipenv requirements --dev > requirements-dev.txt

# Check for security vulnerabilities
pipenv check

# Remove the virtualenv
pipenv --rm

# Locate the virtualenv
pipenv --venv

# Where is Python?
pipenv --py
```

### Pipfile Example
```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = ">=2.31"
fastapi  = "*"
pydantic = ">=2.0"

[dev-packages]
pytest    = "*"
black     = "*"
mypy      = "*"
ruff      = "*"

[requires]
python_version = "3.12"
```

### Environment Variables with pipenv
```bash
# pipenv auto-loads .env file
echo 'DATABASE_URL=postgresql://localhost/mydb' >> .env
pipenv run python -c "import os; print(os.environ['DATABASE_URL'])"
```

---

## 19. Project Management — Poetry

### What is Poetry?
Poetry is a modern dependency manager and build tool. It uses `pyproject.toml` (PEP 517/518) and `poetry.lock` for fully reproducible environments.

### Installation
```bash
# Official installer (recommended)
curl -sSL https://install.python-poetry.org | python3 -

# Verify
poetry --version

# Update poetry itself
poetry self update
```

### Creating a Project
```bash
# New project scaffold
poetry new my-project
cd my-project

# Init in existing directory
cd existing-project
poetry init         # interactive setup
```

### Dependency Management
```bash
# Add runtime dependency
poetry add requests
poetry add "fastapi[all]"
poetry add "sqlalchemy>=2.0,<3.0"

# Add dev dependency
poetry add --group dev pytest black ruff mypy

# Add optional group (e.g. docs)
poetry add --group docs mkdocs mkdocstrings

# Install all deps (from lock file)
poetry install

# Install without dev deps (production)
poetry install --only main

# Install specific groups
poetry install --with dev,docs

# Remove a package
poetry remove requests

# Update all packages
poetry update

# Update a specific package
poetry update requests

# Lock without installing
poetry lock

# Show installed packages
poetry show
poetry show --tree    # dependency tree

# Export to requirements.txt
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements-dev.txt
```

### Virtual Environments
```bash
# Activate venv shell
poetry shell

# Run command inside venv
poetry run python script.py
poetry run pytest

# Show venv path
poetry env info --path

# List environments
poetry env list

# Remove environment
poetry env remove python3.12

# Use specific Python version
poetry env use python3.12
```

### pyproject.toml Example
```toml
[tool.poetry]
name        = "my-project"
version     = "0.1.0"
description = "Awesome Python project"
authors     = ["AK <ak@example.com>"]
readme      = "README.md"
packages    = [{include = "my_project"}]

[tool.poetry.dependencies]
python    = "^3.12"
requests  = "^2.31"
fastapi   = "^0.110"
pydantic  = "^2.6"

[tool.poetry.group.dev.dependencies]
pytest     = "^8.1"
black      = "^24.0"
mypy       = "^1.9"
ruff       = "^0.4"

[tool.poetry.scripts]
start = "my_project.main:app"

[build-system]
requires      = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 88

[tool.ruff]
select     = ["E", "W", "F", "I"]
line-length = 88

[tool.mypy]
strict = true
```

### Publishing to PyPI
```bash
# Configure PyPI token
poetry config pypi-token.pypi <your-token>

# Build sdist + wheel
poetry build

# Publish
poetry publish

# Build & publish in one step
poetry publish --build

# Publish to TestPyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi
```

### pipenv vs Poetry Comparison

| Feature | pipenv | poetry |
|---------|--------|--------|
| Config file | `Pipfile` + `.lock` | `pyproject.toml` + `poetry.lock` |
| Build & publish | ❌ | ✅ |
| Lock file | `Pipfile.lock` | `poetry.lock` |
| Dependency groups | dev only | multiple named groups |
| `.env` auto-load | ✅ | ❌ (use python-dotenv) |
| Monorepo support | ❌ | ✅ (path deps) |
| Standards compliance | Partial | PEP 517/518/621 ✅ |
| Speed | Moderate | Fast |

---

## 20. Resolving Vulnerabilities

### Tools for Scanning

#### 1. pip-audit (recommended by PyPA)
```bash
pip install pip-audit

# Audit current environment
pip-audit

# Audit a requirements file
pip-audit -r requirements.txt

# Output JSON
pip-audit --format json -o audit.json

# Fix automatically (update to safe versions)
pip-audit --fix

# Audit with pipenv
pipenv run pip-audit

# Audit with poetry
poetry run pip-audit
```

#### 2. pipenv check
```bash
pipenv check
# Uses PyUp Safety database to check for known vulnerabilities
```

#### 3. Safety
```bash
pip install safety

# Check installed packages
safety check

# Check requirements file
safety check -r requirements.txt

# JSON output
safety check --json

# Ignore a specific CVE
safety check --ignore 12345
```

#### 4. Bandit (code security linter)
```bash
pip install bandit

# Scan a file
bandit script.py

# Scan a directory recursively
bandit -r my_project/

# Specific severity level
bandit -ll my_project/   # medium and above

# Output formats
bandit -r . -f json -o bandit-report.json
bandit -r . -f html -o bandit-report.html

# Skip tests
bandit -r . --skip B101,B601
```

#### 5. Snyk (cloud-based, CI/CD ready)
```bash
npm install -g snyk
snyk auth
snyk test                          # scan current project
snyk monitor                       # continuous monitoring
snyk fix                           # auto-fix where possible
```

### Common Vulnerability Sources & Fixes

| Vulnerability | Detection | Fix |
|---------------|-----------|-----|
| Outdated dependency | `pip-audit`, `safety` | `pip install --upgrade pkg` or pin safe version |
| SQL Injection | `bandit B608` | Use parameterized queries / ORM |
| Hardcoded secrets | `bandit B105/B106` | Use env vars, `python-dotenv`, vault |
| Insecure deserialization | `bandit B301` | Avoid `pickle` on untrusted data, use JSON |
| Shell injection | `bandit B602/B603` | Use `subprocess` with list args, never `shell=True` |
| Insecure random | `bandit B311` | Use `secrets` module for security-critical randomness |
| SSL verification disabled | `bandit B501` | Never `verify=False` in requests |
| Use of `eval()` | `bandit B307` | Avoid `eval`/`exec` on untrusted input |
| Weak hashing (MD5/SHA1) | `bandit B303` | Use SHA-256 or `bcrypt`/`argon2` for passwords |

### Fixing Vulnerabilities — Step-by-Step

```bash
# Step 1: Scan
pip-audit -r requirements.txt

# Step 2: Check CVE details at https://nvd.nist.gov

# Step 3: Update to patched version
pip install "vulnerable-package>=safe.version"
# OR pin safe version in pyproject.toml / Pipfile

# Step 4: With Poetry
poetry update vulnerable-package
# Check if a version range is available:
poetry add "vulnerable-package>=safe.version"

# Step 5: With pipenv
pipenv update vulnerable-package

# Step 6: Re-audit
pip-audit

# Step 7: Add to CI pipeline (GitHub Actions example)
# .github/workflows/security.yml — see below

# Step 8: Generate lock file & commit
poetry lock
git add poetry.lock pyproject.toml
git commit -m "chore: fix security vulnerabilities"
```

### GitHub Actions Security Workflow
```yaml
name: Security Audit

on:
  push:
    branches: [main]
  schedule:
    - cron: "0 6 * * 1"    # Every Monday at 6 AM

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install pip-audit & bandit
        run: pip install pip-audit bandit

      - name: Dependency vulnerability scan
        run: pip-audit -r requirements.txt

      - name: Code security scan
        run: bandit -r src/ -ll -f json -o bandit.json

      - name: Upload Bandit report
        uses: actions/upload-artifact@v4
        with:
          name: bandit-report
          path: bandit.json
```

### Secure Coding Patterns
```python
# ✅ Use secrets for tokens/passwords
import secrets
token = secrets.token_hex(32)

# ✅ Parameterized DB queries
import sqlite3
conn = sqlite3.connect("db.sqlite3")
conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))   # safe

# ✅ Subprocess without shell=True
import subprocess
result = subprocess.run(["ls", "-la", path], capture_output=True, text=True)

# ✅ Load secrets from environment
import os
from dotenv import load_dotenv
load_dotenv()
db_url = os.environ["DATABASE_URL"]   # raises if missing — intentional

# ✅ Hash passwords with bcrypt
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt.checkpw(password.encode(), hashed)

# ✅ Safe YAML loading
import yaml
data = yaml.safe_load(stream)   # NOT yaml.load()
```

---

## 21. Commands Cheat Sheet

### Python Runtime
```bash
python3 --version                     # check version
python3 -m venv .venv                 # create virtualenv
source .venv/bin/activate             # activate (Unix)
.venv\Scripts\activate                # activate (Windows)
deactivate                            # deactivate venv
python3 -c "print('hello')"           # run inline code
python3 script.py arg1 arg2           # run script
python3 -m module_name                # run as module
python3 -i script.py                  # interactive after run
python3 -O script.py                  # optimize (removes asserts)
python3 -m pdb script.py              # debugger
python3 -m timeit "2**100"            # benchmark
python3 -m cProfile script.py         # profiler
python3 -m py_compile script.py       # syntax check
```

### pip
```bash
pip install package                   # install
pip install "package==1.2.3"          # exact version
pip install "package>=1.2,<2.0"       # version range
pip install package --upgrade         # upgrade
pip uninstall package                 # remove
pip list                              # all installed
pip list --outdated                   # show outdated
pip show package                      # package info
pip freeze > requirements.txt         # export
pip install -r requirements.txt       # install from file
pip install -e .                      # editable install (dev)
pip cache purge                       # clear pip cache
pip config list                       # show pip config
```

### pipenv
```bash
pipenv --python 3.12                  # create env
pipenv install package                # add dependency
pipenv install --dev package          # add dev dep
pipenv install                        # install all
pipenv sync                           # install from lock (exact)
pipenv shell                          # activate shell
pipenv run python script.py           # run in env
pipenv uninstall package              # remove dep
pipenv update                         # update all
pipenv graph                          # dep tree
pipenv check                          # security check
pipenv requirements                   # export requirements
pipenv --venv                         # show venv path
pipenv --rm                           # delete venv
```

### Poetry
```bash
poetry new project                    # scaffold new project
poetry init                           # init in existing dir
poetry add package                    # add dep
poetry add --group dev package        # add dev dep
poetry remove package                 # remove dep
poetry install                        # install all
poetry install --only main            # production only
poetry update                         # update all
poetry update package                 # update specific
poetry show                           # list packages
poetry show --tree                    # dep tree
poetry shell                          # activate shell
poetry run python script.py           # run in env
poetry env info                       # env info
poetry env list                       # list envs
poetry env remove python3.12          # delete env
poetry build                          # build package
poetry publish                        # publish to PyPI
poetry publish --build                # build + publish
poetry export -f requirements.txt     # export
poetry lock                           # regenerate lock
poetry check                          # validate pyproject.toml
poetry config --list                  # show config
poetry self update                    # update poetry
```

### Code Quality Tools
```bash
# Formatting
black .                               # format all files
black --check .                       # check without modifying
black --diff file.py                  # show diff

# Linting
ruff check .                          # lint
ruff check --fix .                    # auto-fix
flake8 .                              # PEP 8 checker
pylint my_module/                     # deep lint

# Type checking
mypy script.py                        # type check
mypy --strict .                       # strict mode
pyright .                             # Microsoft type checker

# Import sorting
isort .                               # sort imports
isort --check .                       # check only

# Security
bandit -r . -ll                       # code security
pip-audit                             # dep vulnerabilities
safety check                          # safety database check
```

### Testing
```bash
pytest                                # run all tests
pytest tests/test_file.py            # specific file
pytest -v                             # verbose
pytest -s                             # show print output
pytest -x                             # stop on first failure
pytest --tb=short                     # shorter tracebacks
pytest -k "login or auth"            # filter by name
pytest --cov=myapp --cov-report=html  # coverage report
pytest --lf                           # last failed only
pytest -n 4                           # parallel (pytest-xdist)
pytest --benchmark-only               # benchmarks (pytest-benchmark)
```

### Common One-liners
```bash
python3 -m http.server 8080           # quick file server
python3 -m json.tool data.json        # pretty-print JSON
python3 -m zipfile -e archive.zip .   # extract zip
python3 -c "import sys; print(sys.path)"
python3 -c "import platform; print(platform.python_implementation())"
python3 -m ensurepip --upgrade        # ensure pip available
```

---

## 22. Important Websites & Links

### 📚 Official Documentation
| Resource | URL |
|----------|-----|
| Python Official Docs | https://docs.python.org/3/ |
| Python Language Reference | https://docs.python.org/3/reference/ |
| Python Standard Library | https://docs.python.org/3/library/ |
| Python HOWTOs | https://docs.python.org/3/howto/ |
| Python Glossary | https://docs.python.org/3/glossary.html |
| What's New in Python | https://docs.python.org/3/whatsnew/ |

### 📦 Package & Dependency Management
| Resource | URL |
|----------|-----|
| PyPI (Package Index) | https://pypi.org |
| pip Documentation | https://pip.pypa.io/en/stable/ |
| pipenv Documentation | https://pipenv.pypa.io/en/latest/ |
| Poetry Documentation | https://python-poetry.org/docs/ |
| Python Packaging Guide | https://packaging.python.org/en/latest/ |
| pyproject.toml Guide | https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ |

### 🔒 Security & Vulnerability
| Resource | URL |
|----------|-----|
| pip-audit | https://github.com/pypa/pip-audit |
| Safety | https://pyup.io/safety/ |
| Bandit | https://bandit.readthedocs.io/en/latest/ |
| Snyk Python | https://snyk.io/languages/python/ |
| NVD (CVE Database) | https://nvd.nist.gov |
| OSV Database | https://osv.dev |
| OWASP Python | https://owasp.org/www-project-python-security/ |

### 🎨 Code Quality & Linting
| Resource | URL |
|----------|-----|
| Black Formatter | https://black.readthedocs.io/en/stable/ |
| Ruff Linter | https://docs.astral.sh/ruff/ |
| Flake8 | https://flake8.pycqa.org/en/latest/ |
| Pylint | https://pylint.readthedocs.io/en/stable/ |
| mypy | https://mypy.readthedocs.io/en/stable/ |
| pyright | https://github.com/microsoft/pyright |
| isort | https://pycqa.github.io/isort/ |
| PEP 8 Style Guide | https://peps.python.org/pep-0008/ |

### 🧪 Testing
| Resource | URL |
|----------|-----|
| pytest | https://docs.pytest.org/en/stable/ |
| unittest | https://docs.python.org/3/library/unittest.html |
| hypothesis (property testing) | https://hypothesis.readthedocs.io/en/latest/ |
| pytest-cov | https://pytest-cov.readthedocs.io/en/latest/ |
| tox (multi-env testing) | https://tox.wiki/en/stable/ |
| Faker (test data) | https://faker.readthedocs.io/en/master/ |

### 🌐 Web Frameworks
| Resource | URL |
|----------|-----|
| FastAPI | https://fastapi.tiangolo.com |
| Django | https://docs.djangoproject.com/en/stable/ |
| Flask | https://flask.palletsprojects.com/en/stable/ |
| Starlette | https://www.starlette.io |
| Litestar | https://litestar.dev |

### 🔢 Data & Science
| Resource | URL |
|----------|-----|
| NumPy | https://numpy.org/doc/stable/ |
| Pandas | https://pandas.pydata.org/docs/ |
| Matplotlib | https://matplotlib.org/stable/users/ |
| Scikit-learn | https://scikit-learn.org/stable/ |
| SQLAlchemy | https://docs.sqlalchemy.org/en/20/ |
| Pydantic | https://docs.pydantic.dev/latest/ |

### 🤖 GenAI & LLM (Relevant to Your Journey!)
| Resource | URL |
|----------|-----|
| LangChain | https://docs.langchain.com |
| LlamaIndex | https://docs.llamaindex.ai/en/stable/ |
| LangGraph | https://langchain-ai.github.io/langgraph/ |
| HuggingFace | https://huggingface.co/docs |
| OpenAI Python SDK | https://github.com/openai/openai-python |
| Anthropic Python SDK | https://github.com/anthropics/anthropic-sdk-python |
| ChromaDB | https://docs.trychroma.com |

### 📖 Learning Resources
| Resource | URL |
|----------|-----|
| Real Python | https://realpython.com |
| Python Cookbook (O'Reilly) | https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/ |
| PEPs (Enhancement Proposals) | https://peps.python.org |
| Python Tricks (book) | https://realpython.com/products/python-tricks-book/ |
| Talk Python Podcast | https://talkpython.fm |
| Python Weekly Newsletter | https://www.pythonweekly.com |
| Awesome Python | https://github.com/vinta/awesome-python |

### 🛠 Tools & IDEs
| Resource | URL |
|----------|-----|
| VS Code Python Extension | https://marketplace.visualstudio.com/items?itemName=ms-python.python |
| PyCharm | https://www.jetbrains.com/pycharm/ |
| Jupyter Notebook | https://jupyter.org |
| Google Colab | https://colab.research.google.com |
| Replit | https://replit.com |
| Python Tutor (visualizer) | https://pythontutor.com |

---

> 📝 **Summary:** This guide covers Python from zero to production — including all core language features, OOP, concurrency, type hints, testing, dependency management with **pipenv** and **Poetry**, security auditing, and a complete cheat sheet. Pin this as your daily driver reference!
>
> ✍️ *Tailored for full-stack developers transitioning into GenAI/LLM engineering.*

---
