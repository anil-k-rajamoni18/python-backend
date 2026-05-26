# 🐍 Python — Day 7 Master Notes

> Iterators, Generators, Decorators, Context Managers, Type Hints  
> Enhanced with internals, memory diagrams, execution flow, real-world patterns, and complete exercises

---

## Table of Contents

1. [Iterators — Deep Dive](#1-iterators--deep-dive)
2. [Generators — Iterators Made Easy](#2-generators--iterators-made-easy)
3. [Generator Expressions vs List Comprehensions](#3-generator-expressions-vs-list-comprehensions)
4. [Generator Pipelines — Composing Data Flows](#4-generator-pipelines--composing-data-flows)
5. [Decorators — Deep Dive](#5-decorators--deep-dive)
6. [Decorators with Arguments](#6-decorators-with-arguments)
7. [Stacking Decorators & Preserving Metadata](#7-stacking-decorators--preserving-metadata)
8. [Real-World Decorator Patterns](#8-real-world-decorator-patterns)
9. [Context Managers — Deep Dive](#9-context-managers--deep-dive)
10. [contextlib — The Pythonic Way](#10-contextlib--the-pythonic-way)
11. [Real-World Context Manager Patterns](#11-real-world-context-manager-patterns)
12. [Type Hints — Deep Dive](#12-type-hints--deep-dive)
13. [Advanced Type Hints](#13-advanced-type-hints)
14. [Hands-On Exercises (All Coded)](#14-hands-on-exercises-all-coded)
15. [Mini Project — Performance Monitor Tool (Full Implementation)](#15-mini-project--performance-monitor-tool-full-implementation)

---

## 1. Iterators — Deep Dive

### What Is an Iterator?

An iterator is an object that produces values one at a time, on demand. You don't get everything at once — you get one item, process it, then ask for the next. This is the foundation of how Python's `for` loop actually works under the hood.

There are two closely related concepts:

```
ITERABLE                            ITERATOR
────────────────────────────────    ──────────────────────────────────
Any object you can loop over.       The object that does the looping.
Has __iter__() which returns        Has both __iter__() and __next__().
an iterator.                        __next__() returns the next value
                                    or raises StopIteration when done.

Examples:                           Examples:
  list, tuple, str, dict            iter([1, 2, 3])
  set, range, file objects          map(), filter(), zip()
  any class with __iter__           any class with __next__()
```

A helpful mental model: an **iterable** is a book. An **iterator** is a bookmark — it remembers where you are and moves forward one page at a time.

### How `for` Loops Work Internally

Every `for` loop in Python is actually doing this:

```python
# What you write:
for item in [10, 20, 30]:
    print(item)

# What Python actually does:
_iterable = [10, 20, 30]
_iterator = iter(_iterable)       # calls _iterable.__iter__()
while True:
    try:
        item = next(_iterator)    # calls _iterator.__next__()
        print(item)
    except StopIteration:
        break
```

This is why the `for` loop works with lists, strings, files, generators, database cursors, and anything else that follows the iterator protocol.

### Manual Iterator Usage

```python
numbers = [10, 20, 30]

it = iter(numbers)        # get the iterator
print(next(it))           # 10
print(next(it))           # 20
print(next(it))           # 30
print(next(it))           # StopIteration raised

# Safe version with default — no exception
print(next(it, "done"))   # "done" — returned when exhausted
```

### Building a Custom Iterator

The iterator protocol is just two methods: `__iter__` and `__next__`. Any class that implements them can be used in a `for` loop, `zip()`, `list()`, and anywhere else Python expects an iterable.

**Example — Countdown Iterator:**

```python
class CountDown:
    """Counts down from start to 1."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self    # the iterator is the object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Use it anywhere an iterable is expected
for n in CountDown(5):
    print(n, end=" ")    # 5 4 3 2 1

print(list(CountDown(3)))    # [3, 2, 1]
print(sum(CountDown(10)))    # 55
```

**Example — Range of Squares Iterator:**

```python
class SquareRange:
    """Generates squares of integers from start to stop."""

    def __init__(self, start: int, stop: int):
        self.current = start
        self.stop    = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current ** 2
        self.current += 1
        return value

print(list(SquareRange(1, 6)))   # [1, 4, 9, 16, 25]
```

### Real-World Example — Paginated API Fetcher

APIs often return data in pages. An iterator models this perfectly — you don't fetch all pages upfront, you fetch one page, process it, then fetch the next only when needed.

```python
import requests

class PaginatedAPI:
    """
    Iterates through paginated API responses.
    Fetches each page lazily — only when requested.
    Used in: data migrations, report generation, ETL pipelines.
    """

    def __init__(self, base_url: str, per_page: int = 10):
        self.base_url  = base_url
        self.per_page  = per_page
        self.page      = 1
        self.exhausted = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.exhausted:
            raise StopIteration

        response = requests.get(
            self.base_url,
            params={"_page": self.page, "_limit": self.per_page},
            timeout=10
        )
        data = response.json()

        if not data:
            raise StopIteration

        self.page += 1
        return data

# Usage
api = PaginatedAPI("https://jsonplaceholder.typicode.com/posts")
for page_num, page_data in enumerate(api, start=1):
    print(f"Page {page_num}: {len(page_data)} records")
    if page_num >= 3:
        break   # only process 3 pages in this example
```

### Real-World Example — Streaming Sensor Data

```python
import time
import random

class TemperatureSensor:
    """
    Simulates a streaming IoT sensor.
    In production: reads from serial port, MQTT, or WebSocket.
    """

    def __init__(self, limit: int = None):
        self.count = 0
        self.limit = limit   # None = infinite stream

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit and self.count >= self.limit:
            raise StopIteration
        self.count += 1
        temperature = round(random.uniform(18.0, 35.0), 2)
        humidity    = round(random.uniform(40.0, 80.0), 1)
        return {
            "reading":     self.count,
            "temperature": temperature,
            "humidity":    humidity,
            "timestamp":   time.time()
        }

sensor = TemperatureSensor(limit=5)
for reading in sensor:
    print(f"Reading #{reading['reading']}: {reading['temperature']}°C, {reading['humidity']}%")
```

### Iterator Internals — What Happens in Memory

```
ITERABLE (list):                    ITERATOR OBJECT:
┌─────────────────────┐            ┌─────────────────────┐
│ [10, 20, 30, 40]    │  iter() →  │ pointer → index: 0  │
│ stored in memory    │            │                     │
└─────────────────────┘            │ next() → 10, idx:1  │
                                   │ next() → 20, idx:2  │
                                   │ next() → 30, idx:3  │
                                   │ next() → 40, idx:4  │
                                   │ next() → StopIter   │
                                   └─────────────────────┘

KEY INSIGHT: The full list exists in memory the whole time.
             The iterator is just a lightweight object tracking position.
             For generators (next section), values aren't stored at all.
```

### Where Iterators Are Used in Industry

| Domain | Iterator Use Case |
|--------|------------------|
| Pandas | `iterrows()`, `itertuples()` over DataFrames |
| Django/SQLAlchemy | QuerySet lazy loading from database |
| Apache Kafka | Consumer iterating over message stream |
| File Processing | Log parsers, CSV readers, ETL pipelines |
| ML Data Loading | PyTorch `DataLoader`, HuggingFace datasets |
| Networking | Socket data reading, WebSocket streams |

---

## 2. Generators — Iterators Made Easy

### What Is a Generator?

A generator is a function that uses `yield` instead of `return`. It automatically implements the full iterator protocol (`__iter__` and `__next__`) without you writing any of that boilerplate. When called, a generator function returns a **generator object** — which is a lazy iterator.

The key insight about generators: **execution is suspended at every `yield` and resumed on the next `next()` call.** The function's local variables, the call stack, and the execution position are all preserved between calls.

### How `yield` Works — The Execution Flow

```python
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n          # ← execution PAUSES here, value sent to caller
        n -= 1           # ← execution RESUMES here on next next() call
    print("Done!")

gen = countdown(3)       # function body does NOT run yet — just creates generator

print(next(gen))         # "Starting countdown from 3", then yields → 3
print(next(gen))         # resumes, n becomes 2, yields → 2
print(next(gen))         # resumes, n becomes 1, yields → 1
print(next(gen))         # resumes, "Done!" printed, StopIteration raised
```

```
EXECUTION TIMELINE:
─────────────────────────────────────────────────────────────
gen = countdown(3)    → generator object created, NO code runs
next(gen)             → enters function, runs until yield 3 → pauses
next(gen)             → resumes after yield, n=2, reaches yield 2 → pauses
next(gen)             → resumes, n=1, reaches yield 1 → pauses
next(gen)             → resumes, n=0, loop exits, "Done!" printed → StopIteration
─────────────────────────────────────────────────────────────
```

### Generator vs Iterator Class — Same Result, Far Less Code

```python
# Class-based iterator — lots of boilerplate
class CountDown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Generator — exactly equivalent, 4 lines
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Both behave identically
list(CountDown(5))  # [5, 4, 3, 2, 1]
list(countdown(5))  # [5, 4, 3, 2, 1]
```

### Memory — The Core Advantage

This is the most important practical benefit of generators:

```python
import sys

# List comprehension — generates ALL values, stores ALL in memory
squares_list = [x ** 2 for x in range(1_000_000)]
print(f"List size:      {sys.getsizeof(squares_list):>10,} bytes")  # ~8,000,056 bytes

# Generator — produces values ONE AT A TIME, stores almost nothing
squares_gen = (x ** 2 for x in range(1_000_000))
print(f"Generator size: {sys.getsizeof(squares_gen):>10,} bytes")  # ~104 bytes

# Both produce the same values when iterated
print(sum(squares_list))   # 333332833333500000
print(sum(squares_gen))    # 333332833333500000 — identical result
```

With 1 million numbers: the list uses ~8MB. The generator uses ~100 bytes. With 1 billion numbers: the list needs ~8GB RAM and your process crashes. The generator still uses ~100 bytes.

### Real-World Generators

**Streaming large file processor:**
```python
def read_logs(path: str, encoding: str = "utf-8"):
    """
    Generator that reads a log file line by line.
    Never loads the whole file into memory.
    Works on a 10GB log file exactly the same as a 10KB one.
    """
    with open(path, encoding=encoding) as f:
        for line in f:
            yield line.rstrip("\n")

def filter_errors(lines):
    """Generator pipeline step — only pass ERROR lines through."""
    for line in lines:
        if "ERROR" in line or "CRITICAL" in line:
            yield line

def parse_timestamp(lines):
    """Extract the timestamp from each log line."""
    import re
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
    for line in lines:
        match = pattern.search(line)
        ts = match.group(1) if match else "unknown"
        yield ts, line

# Composing generators into a pipeline — reads the 10GB file, uses almost no RAM
log_lines  = read_logs("server.log")
error_lines = filter_errors(log_lines)
parsed     = parse_timestamp(error_lines)

for timestamp, line in parsed:
    print(f"[{timestamp}] {line[:80]}")
```

**Infinite sequence generator:**
```python
def fibonacci():
    """
    Infinite Fibonacci sequence generator.
    Produces numbers forever — caller decides when to stop.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(n, iterable):
    """Take first n items from any iterable."""
    for i, item in enumerate(iterable):
        if i >= n:
            return
        yield item

fib = fibonacci()
first_20 = list(take(20, fib))
print(first_20)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

**Database batch fetcher:**
```python
def fetch_in_batches(query: str, batch_size: int = 500):
    """
    Generator that fetches DB rows in batches.
    Avoids loading millions of rows into memory at once.
    Standard pattern in ETL and data migration scripts.
    """
    offset = 0
    while True:
        # In real code: rows = db.execute(query + f" LIMIT {batch_size} OFFSET {offset}")
        rows = simulate_db_query(query, batch_size, offset)
        if not rows:
            return
        yield rows
        if len(rows) < batch_size:
            return    # last batch
        offset += batch_size

def simulate_db_query(query, limit, offset):
    """Simulates a DB query returning rows."""
    all_data = list(range(1, 1501))   # 1500 records total
    return all_data[offset:offset + limit]

for batch in fetch_in_batches("SELECT * FROM users", batch_size=500):
    print(f"Processing batch of {len(batch)} records: {batch[0]}..{batch[-1]}")
```

### `yield from` — Delegating to Sub-Generators

```python
def chain(*iterables):
    """Like itertools.chain — combines multiple iterables."""
    for iterable in iterables:
        yield from iterable   # delegates to each sub-iterable

result = list(chain([1, 2, 3], [4, 5], [6, 7, 8]))
# [1, 2, 3, 4, 5, 6, 7, 8]

# Recursive tree traversal with yield from
def flatten(lst):
    """Flatten arbitrarily nested lists."""
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)   # delegate recursively
        else:
            yield item

print(list(flatten([1, [2, [3, [4]], 5], 6])))
# [1, 2, 3, 4, 5, 6]
```

### Sending Values Into a Generator — Two-Way Communication

Generators can also receive values via `send()`. This turns them into coroutines — the foundation of Python's async system.

```python
def accumulator():
    """Generator that accumulates sent values and yields running total."""
    total = 0
    while True:
        value = yield total   # yield sends total out; send() pushes value in
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)             # prime the generator (advance to first yield)
acc.send(10)          # total = 10
acc.send(25)          # total = 35
acc.send(5)           # total = 40
print(acc.send(0))    # 40
```

---

## 3. Generator Expressions vs List Comprehensions

| Feature | List Comprehension `[...]` | Generator Expression `(...)` |
|---------|---------------------------|------------------------------|
| Memory | Allocates all at once | Produces one at a time |
| Speed to create | Slower (builds list) | Instant (just creates object) |
| Reusable | Yes — iterate multiple times | No — exhausted after one pass |
| Best for | Small data, reused multiple times | Large data, iterated once |
| Use with `sum/max/any/all` | Works | Works + more efficient |

```python
# When you NEED a list (reuse, indexing, len)
words = ["the", "quick", "brown", "fox"]
lengths = [len(w) for w in words]
print(lengths[0])    # needs indexing → use list

# When you just need to aggregate (don't need the list itself)
total_chars = sum(len(w) for w in words)           # generator — no list built
longest     = max(len(w) for w in words)           # generator
has_long    = any(len(w) > 4 for w in words)       # generator, stops early

# Passing a generator to a function — only one pair of parens needed
print(sum(x**2 for x in range(100)))
# NOT: sum((x**2 for x in range(100)))  ← unnecessary extra parens
```

---

## 4. Generator Pipelines — Composing Data Flows

One of the most powerful patterns in Python: chaining generators together so each one handles one transformation. Data flows through lazily — no intermediate lists built, no extra memory used.

```
raw_data → generator_1 → generator_2 → generator_3 → output

Each generator pulls from the previous only when it needs the next value.
```

```python
import csv

# Each function is a generator — one responsibility each
def read_csv(path):
    """Step 1: Read raw CSV rows."""
    with open(path, newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)

def parse_amounts(rows):
    """Step 2: Convert string amounts to float, skip bad rows."""
    for row in rows:
        try:
            row["amount"] = float(row["amount"])
            yield row
        except (ValueError, KeyError):
            pass   # skip malformed rows silently

def filter_high_value(rows, threshold=10000):
    """Step 3: Keep only high-value transactions."""
    for row in rows:
        if row["amount"] >= threshold:
            yield row

def add_gst(rows, rate=0.18):
    """Step 4: Add computed GST field."""
    for row in rows:
        row["gst"]   = round(row["amount"] * rate, 2)
        row["total"] = round(row["amount"] + row["gst"], 2)
        yield row

# Compose the pipeline — no intermediate lists, no extra memory
pipeline = add_gst(
               filter_high_value(
                   parse_amounts(
                       read_csv("transactions.csv")
                   ),
                   threshold=5000
               )
           )

for record in pipeline:
    print(f"{record['id']}: ₹{record['total']:,.2f}")
```

This pattern — popularized by Unix pipes — is used in Spark, Kafka Streams, and Python's `itertools` module.

---

## 5. Decorators — Deep Dive

### What Is a Decorator?

A decorator is a function that takes another function as input and returns a new function that adds behavior around it. The original function's code doesn't change — the decorator wraps it.

Decorators implement the **wrapper pattern** from software design. They let you apply cross-cutting concerns (logging, auth, timing, caching, validation) to many functions without touching each one individually.

### How Decorators Work — Step by Step

```python
# Step 1: A plain function
def greet():
    print("Hello!")

# Step 2: A decorator function
def logger(func):
    def wrapper(*args, **kwargs):         # ← the wrapper catches all arguments
        print(f"→ Calling {func.__name__}")
        result = func(*args, **kwargs)    # ← call the original function
        print(f"← {func.__name__} finished")
        return result                     # ← return original result
    return wrapper                        # ← return the wrapper, not calling it

# Step 3: Apply manually (what @ does under the hood)
greet = logger(greet)   # greet is now the wrapper

# Step 4: Using @ syntax — exact same thing, cleaner
@logger
def greet():
    print("Hello!")

# greet() now actually calls wrapper(), which calls original greet()
greet()
# → Calling greet
# Hello!
# ← greet finished
```

The `@logger` syntax is pure syntactic sugar. Python rewrites it to `greet = logger(greet)` before executing anything.

### `*args` and `**kwargs` — Making Decorators Universal

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
# Calling add with args=(3, 5), kwargs={}
# Returned: 8

greet("Anil", greeting="Welcome")
# Calling greet with args=('Anil',), kwargs={'greeting': 'Welcome'}
# Returned: Welcome, Anil!
```

### Timing Decorator — Real Production Use

```python
import time
import functools

def timeit(func):
    """
    Measures and logs execution time of any function.
    Used for: profiling slow DB queries, ML inference timing,
              API endpoint benchmarking.
    """
    @functools.wraps(func)   # preserves original function metadata
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()       # high-resolution timer
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        elapsed = (end - start) * 1000     # convert to milliseconds
        print(f"⏱  {func.__name__} completed in {elapsed:.2f}ms")
        return result
    return wrapper

@timeit
def sort_million_numbers():
    return sorted(range(1_000_000), reverse=True)

@timeit
def fetch_user(user_id: int):
    time.sleep(0.1)    # simulates DB query
    return {"id": user_id, "name": "Anil"}

sort_million_numbers()
# ⏱  sort_million_numbers completed in 312.45ms

fetch_user(1042)
# ⏱  fetch_user completed in 100.23ms
```

---

## 6. Decorators with Arguments

Sometimes you want to configure a decorator — pass it options like a log level, a retry count, or a role name. This requires one extra layer of nesting: a **decorator factory** that returns the actual decorator.

```
Normal decorator:
  @decorator          ← no arguments
  def func():...
  → func = decorator(func)

Parameterized decorator:
  @decorator(arg)     ← has arguments
  def func():...
  → func = decorator(arg)(func)    ← three layers
```

```python
import functools
import time

# Three-layer structure:
# 1. Outer function  → accepts decorator arguments
# 2. Middle function → accepts the function being decorated
# 3. Inner function  → the actual wrapper that runs on every call

def retry(max_attempts: int = 3, delay: float = 1.0, exceptions=(Exception,)):
    """
    Retry decorator with configurable attempts, delay, and exception types.
    Used everywhere: API calls, DB connections, file I/O, payment processing.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        print(f"❌ {func.__name__} failed after {max_attempts} attempts: {e}")
                        raise
                    wait = delay * (2 ** (attempt - 1))   # exponential backoff
                    print(f"⚠ Attempt {attempt}/{max_attempts} failed. Retrying in {wait:.1f}s...")
                    time.sleep(wait)
        return wrapper
    return decorator

import random

@retry(max_attempts=4, delay=0.5, exceptions=(ConnectionError,))
def call_payment_api(amount: float):
    """Simulates an unreliable external API."""
    if random.random() < 0.7:
        raise ConnectionError("Payment gateway timeout")
    return {"status": "success", "amount": amount}

result = call_payment_api(4999.0)
print(result)
```

**Role-based access decorator:**
```python
def require_role(*allowed_roles: str):
    """
    Authorization decorator.
    Used in Flask, FastAPI, Django to protect routes.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") not in allowed_roles:
                raise PermissionError(
                    f"Access denied. Required: {allowed_roles}, got: {user.get('role')}"
                )
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin", "superuser")
def delete_user(user, target_id: int):
    print(f"User {target_id} deleted by {user['name']}")

@require_role("admin", "hr_manager")
def view_salary_report(user):
    print(f"Salary report viewed by {user['name']}")

admin = {"name": "Anil", "role": "admin"}
guest = {"name": "Bob", "role": "viewer"}

delete_user(admin, 42)     # ✅ works
delete_user(guest, 42)     # ❌ PermissionError
```

**Validation decorator:**
```python
def validate_types(**expected_types):
    """
    Validates argument types at runtime.
    Similar to what Pydantic does for FastAPI request bodies.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig    = inspect.signature(func)
            params = list(sig.parameters.keys())
            for i, arg in enumerate(args):
                if i < len(params):
                    param_name = params[i]
                    if param_name in expected_types:
                        expected = expected_types[param_name]
                        if not isinstance(arg, expected):
                            raise TypeError(
                                f"'{param_name}' expected {expected.__name__}, "
                                f"got {type(arg).__name__}"
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int, salary=float)
def create_employee(name: str, age: int, salary: float):
    return {"name": name, "age": age, "salary": salary}

create_employee("Anil", 28, 85000.0)   # ✅
create_employee("Bob", "28", 72000.0)  # ❌ TypeError: 'age' expected int, got str
```

---

## 7. Stacking Decorators & Preserving Metadata

### Stacking Multiple Decorators

You can stack decorators — they apply bottom-up:

```python
@decorator_A
@decorator_B
@decorator_C
def func():
    pass

# Equivalent to:
func = decorator_A(decorator_B(decorator_C(func)))
# C wraps func first, B wraps that, A wraps that
```

```python
import functools
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} took {(time.perf_counter()-start)*1000:.2f}ms")
        return result
    return wrapper

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token")
        if not token or token != "valid_token_123":
            raise PermissionError("Invalid or missing auth token")
        return func(*args, **kwargs)
    return wrapper

@timeit
@log_call
@require_auth
def get_dashboard_data(user_id: int, token: str = None):
    time.sleep(0.05)   # simulates DB query
    return {"user_id": user_id, "widgets": ["sales", "users", "revenue"]}

get_dashboard_data(1042, token="valid_token_123")
```

### Preserving Function Metadata with `functools.wraps`

Without `functools.wraps`, decorators break introspection:

```python
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """This function does something important."""
    pass

print(my_function.__name__)   # "wrapper" ← wrong!
print(my_function.__doc__)    # None      ← wrong!

# ─────────────────────────────────────────────────────────────

def good_decorator(func):
    @functools.wraps(func)     # ← copies __name__, __doc__, __module__ etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function():
    """This function does something important."""
    pass

print(my_function.__name__)   # "my_function" ✅
print(my_function.__doc__)    # "This function does something important." ✅
```

Always use `@functools.wraps(func)` inside your decorators. Without it, debugging, logging, and documentation tools break.

---

## 8. Real-World Decorator Patterns

### Rate Limiter

```python
import time
import functools
from collections import defaultdict

def rate_limit(calls_per_second: float):
    """
    Limits how frequently a function can be called.
    Used in API clients, web scrapers, notification systems.
    """
    min_interval = 1.0 / calls_per_second
    last_called   = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now    = time.monotonic()
            key    = func.__name__
            elapsed = now - last_called.get(key, 0)
            if elapsed < min_interval:
                sleep_time = min_interval - elapsed
                time.sleep(sleep_time)
            last_called[key] = time.monotonic()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)   # max 2 calls per second
def send_notification(message: str):
    print(f"[{time.strftime('%H:%M:%S')}] Sending: {message}")

for msg in ["Alert 1", "Alert 2", "Alert 3", "Alert 4"]:
    send_notification(msg)
```

### Cache / Memoization

```python
import functools

def memoize(func):
    """
    Cache function results by arguments.
    Identical to @functools.lru_cache but transparent for learning.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache       # expose cache for inspection
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # instant — no redundant calls
print(fibonacci.cache)  # see what's cached

# Production: use @functools.lru_cache(maxsize=128)
```

### Decorator Summary — Industry Map

| Decorator | What It Does | Used In |
|-----------|-------------|---------|
| `@timeit` | Measures execution time | Performance profiling, APM |
| `@retry(n)` | Retries failed calls | API clients, DB connections |
| `@require_role(...)` | Checks user permissions | Web frameworks (Flask, FastAPI) |
| `@rate_limit(n)` | Limits call frequency | API clients, notification systems |
| `@memoize` / `@lru_cache` | Caches return values | Expensive computations, DB queries |
| `@validate_types(...)` | Validates argument types | Input validation, form processing |
| `@log_call` | Logs invocations | Audit logging, debugging |
| `@deprecated` | Warns on use | Library maintenance |
| `@singleton` | Enforces single instance | Service classes, config objects |

---

## 9. Context Managers — Deep Dive

### What Is a Context Manager?

A context manager is an object that manages a resource — it handles **setup** before you use the resource and **cleanup** after, even if an exception happens. The `with` statement is the syntax that triggers it.

```python
with some_context_manager() as resource:
    # use resource here
    pass
# cleanup happens here automatically — exception or not
```

The problem context managers solve: resources like files, database connections, locks, and network sockets need to be properly closed/released. Without context managers, every developer has to remember to write the cleanup code — and they don't always, especially when exceptions happen.

### The Protocol — `__enter__` and `__exit__`

```python
class FileManager:
    """
    Custom context manager for file access.
    Adds logging around open/close.
    """

    def __init__(self, path: str, mode: str = "r"):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called at the start of the with block. Returns the resource."""
        print(f"Opening {self.path}")
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file          # ← this is what 'as f' receives

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called at the end of the with block — always, even on exception.
        exc_type:  exception class if an error occurred, else None
        exc_value: exception instance, else None
        traceback: traceback object, else None
        Return True to suppress the exception, False/None to let it propagate.
        """
        print(f"Closing {self.path}")
        if self.file:
            self.file.close()

        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
            return False  # don't suppress — let exception propagate

        return True

# Usage
with FileManager("data.txt", "r") as f:
    content = f.read()
    print(content[:50])
# "Closing data.txt" always prints — even if read() threw an exception
```

### The `__exit__` Method in Detail

```python
def __exit__(self, exc_type, exc_value, traceback):
    #                  ↑           ↑          ↑
    #              The class   The actual   Stack trace
    #              of exception instance    object
    #              (None if    of the       (for logging
    #              no error)   exception    or re-raising)

    # Return False (or None): exception propagates normally
    # Return True:            exception is suppressed (swallowed)

    # Example: suppress only FileNotFoundError, let others propagate
    return exc_type is FileNotFoundError
```

### Database Transaction Context Manager

This is one of the most important real-world uses:

```python
import sqlite3

class DatabaseTransaction:
    """
    Context manager for database transactions.
    Commits on success, rolls back on any exception.
    Pattern used in: SQLAlchemy, Django ORM, FastAPI DB sessions.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn    = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("BEGIN")
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.conn.commit()
            print("✅ Transaction committed")
        else:
            self.conn.rollback()
            print(f"❌ Transaction rolled back due to: {exc_value}")
        self.conn.close()
        return False    # don't suppress the exception

# Usage
try:
    with DatabaseTransaction("app.db") as conn:
        conn.execute("INSERT INTO users VALUES (1, 'Anil', 'anil@x.com')")
        conn.execute("INSERT INTO orders VALUES (101, 1, 4999.0)")
        # If this raises, both inserts are rolled back automatically
        conn.execute("UPDATE inventory SET stock = stock - 1 WHERE id = 42")
except Exception as e:
    print(f"Operation failed: {e}")
```

### Thread Lock Context Manager

```python
import threading

lock = threading.Lock()

def update_shared_counter():
    with lock:              # acquires lock on enter, releases on exit
        # only one thread executes this block at a time
        shared_counter += 1
    # lock released here — even if exception was raised
```

---

## 10. contextlib — The Pythonic Way

Writing a full class with `__enter__` and `__exit__` is verbose. The `contextlib` module lets you create context managers from generator functions using `@contextmanager`. Much less code, same behavior.

### `@contextmanager` Decorator

```python
from contextlib import contextmanager

@contextmanager
def managed_file(path: str, mode: str = "r"):
    """
    Context manager written as a generator.
    Code BEFORE yield = __enter__ (setup)
    Code AFTER yield  = __exit__  (cleanup)
    The yield value is what 'as f' receives.
    """
    print(f"Opening {path}")
    f = open(path, mode, encoding="utf-8")
    try:
        yield f             # ← hand control to the with block
    finally:
        f.close()           # ← always runs (finally = __exit__ behavior)
        print(f"Closed {path}")

with managed_file("data.txt") as f:
    print(f.read())
```

**Timer context manager:**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str = "Block"):
    """Measure execution time of any code block."""
    start = time.perf_counter()
    try:
        yield    # no value needed — 'as' not required
    finally:
        elapsed = (time.perf_counter() - start) * 1000
        print(f"⏱ {label} completed in {elapsed:.2f}ms")

with timer("Database migration"):
    time.sleep(0.5)   # simulates long operation
# ⏱ Database migration completed in 500.12ms

with timer("ML model inference"):
    result = [x**2 for x in range(1_000_000)]
# ⏱ ML model inference completed in 84.37ms
```

**Temporary directory context manager:**
```python
from contextlib import contextmanager
import tempfile
import shutil
from pathlib import Path

@contextmanager
def temp_workspace(prefix: str = "work_"):
    """
    Creates a temporary directory for intermediate work.
    Deletes it automatically when done — even on error.
    Used in: file processing jobs, test fixtures, ML training runs.
    """
    workspace = Path(tempfile.mkdtemp(prefix=prefix))
    print(f"Created workspace: {workspace}")
    try:
        yield workspace
    finally:
        shutil.rmtree(workspace, ignore_errors=True)
        print(f"Cleaned up workspace: {workspace}")

with temp_workspace("etl_job_") as ws:
    # Write intermediate files
    (ws / "input.csv").write_text("name,age\nAnil,28\nBob,32")
    (ws / "output.json").write_text('{"processed": 2}')
    print(f"Files in workspace: {list(ws.iterdir())}")
# Directory and all files deleted automatically
```

### `contextlib.suppress` — Ignore Specific Exceptions

```python
from contextlib import suppress

# Instead of:
try:
    os.remove("temp_file.txt")
except FileNotFoundError:
    pass

# Write:
with suppress(FileNotFoundError):
    os.remove("temp_file.txt")

# Works with multiple exception types
with suppress(FileNotFoundError, PermissionError):
    shutil.rmtree("build/")
```

### `contextlib.ExitStack` — Dynamic Number of Context Managers

```python
from contextlib import ExitStack

# When you don't know how many files you'll open at compile time
def merge_files(input_paths: list, output_path: str):
    with ExitStack() as stack:
        files = [
            stack.enter_context(open(p, encoding="utf-8"))
            for p in input_paths
        ]
        out = stack.enter_context(open(output_path, "w"))
        for f in files:
            out.write(f.read())
```

---

## 11. Real-World Context Manager Patterns

### Connection Pool Simulation

```python
from contextlib import contextmanager
from queue import Queue
import threading

class ConnectionPool:
    """
    Manages a pool of reusable connections.
    Context manager ensures connections are returned to the pool.
    Pattern used by: psycopg2, SQLAlchemy, Redis py, motor.
    """

    def __init__(self, size: int = 5):
        self._pool = Queue(maxsize=size)
        for i in range(size):
            self._pool.put(f"Connection-{i+1}")

    @contextmanager
    def get_connection(self, timeout: float = 5.0):
        conn = self._pool.get(timeout=timeout)
        print(f"Acquired {conn}")
        try:
            yield conn
        finally:
            self._pool.put(conn)
            print(f"Released {conn}")

pool = ConnectionPool(size=3)

with pool.get_connection() as conn:
    print(f"Using {conn} to run query")
# Connection automatically returned to pool
```

### HTTP Session Context Manager

```python
import requests
from contextlib import contextmanager

@contextmanager
def api_session(base_url: str, token: str):
    """
    Creates an authenticated HTTP session.
    Ensures session is properly closed after use.
    """
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    })
    session.base_url = base_url

    try:
        yield session
    finally:
        session.close()

with api_session("https://api.example.com", token="mytoken123") as session:
    resp = session.get(f"{session.base_url}/users")
    users = resp.json()
```

---

## 12. Type Hints — Deep Dive

### What Are Type Hints?

Type hints are annotations that describe the expected types of function parameters and return values. Python does **not enforce them at runtime** — they're informational. But tools like `mypy`, `pyright`, `PyCharm`, and `VS Code` read them to catch bugs before runtime.

```python
# Without type hints — reader must guess what types are expected
def process(data, limit, active):
    ...

# With type hints — immediately clear
def process(data: list[dict], limit: int, active: bool) -> list[dict]:
    ...
```

### Why Type Hints Matter in Production

```
Without type hints:               With type hints:
─────────────────────────────     ──────────────────────────────────────
Bug discovered at runtime         Bug caught by IDE/mypy before running
  → user sees 500 error           → developer sees red underline

Reader must trace code            Reader understands from signature
  → slows onboarding              → fast code review

No IDE autocomplete               Full autocomplete + docs
  → slower development            → faster development

FastAPI: manual docs              FastAPI: auto-generates Swagger docs,
                                  request validation, response schemas
```

### Basic Type Hints

```python
# Variables
name: str   = "Anil"
age:  int   = 28
gpa:  float = 9.2
active: bool = True

# Function parameters and return type
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_data(records: list) -> None:   # None = no return value
    for r in records:
        print(r)
```

### Collection Types

```python
# Python 3.9+ — use built-in generics
def average(values: list[int]) -> float:
    return sum(values) / len(values)

def get_tags(post_id: int) -> set[str]:
    return {"python", "backend", "api"}

def get_config() -> dict[str, str]:
    return {"host": "localhost", "port": "5432"}

def get_coordinates() -> tuple[float, float]:
    return (17.3850, 78.4867)

# Pre-3.9 (still common in codebases)
from typing import List, Dict, Set, Tuple
def legacy(values: List[int]) -> Dict[str, int]:
    ...
```

### Optional and Union Types

```python
from typing import Optional, Union

# Optional[X] means "X or None" — same as X | None in 3.10+
def find_user(user_id: int) -> Optional[dict]:
    """Returns user dict if found, None if not found."""
    if user_id == 1:
        return {"id": 1, "name": "Anil"}
    return None   # explicit None return is documented by Optional

# Union — multiple possible types
def format_value(value: Union[int, float, str]) -> str:
    return str(value)

# Python 3.10+ shorthand — use | instead of Union
def format_value(value: int | float | str) -> str:
    return str(value)

# Optional shorthand in 3.10+
def find_user(user_id: int) -> dict | None:
    ...
```

### TypedDict — Typing Dictionary Structures

```python
from typing import TypedDict

class UserProfile(TypedDict):
    id:         int
    name:       str
    email:      str
    age:        int
    is_active:  bool

class Address(TypedDict, total=False):   # total=False = all keys optional
    street: str
    city:   str
    pincode: str

def create_user(profile: UserProfile) -> UserProfile:
    return profile

# IDE now knows exactly what keys exist and their types
user: UserProfile = {
    "id": 1,
    "name": "Anil",
    "email": "anil@company.com",
    "age": 28,
    "is_active": True
}
```

### Callable — Typing Functions as Arguments

```python
from typing import Callable

# A function that takes (int, int) and returns int
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

apply(lambda x, y: x + y, 3, 5)   # IDE knows func takes two ints

# Decorator typing
from typing import TypeVar, Callable, Any
F = TypeVar("F", bound=Callable[..., Any])

def log_call(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper   # type: ignore
```

### Generic Types and TypeVar

```python
from typing import TypeVar, Generic

T = TypeVar("T")   # placeholder for any type

def first(lst: list[T]) -> T:
    """Return first element — works for list of any type."""
    return lst[0]

first([1, 2, 3])       # returns int
first(["a", "b"])      # returns str
first([1.0, 2.0])      # returns float
```

---

## 13. Advanced Type Hints

### Protocol — Structural Typing (Duck Typing + Types)

```python
from typing import Protocol

class Serializable(Protocol):
    """Any object with a .to_dict() method satisfies this protocol."""
    def to_dict(self) -> dict: ...

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age
    def to_dict(self) -> dict:
        return {"name": self.name, "age": self.age}

class Product:
    def __init__(self, name: str, price: float):
        self.name  = name
        self.price = price
    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price}

def serialize(obj: Serializable) -> str:
    import json
    return json.dumps(obj.to_dict())

# Both work — no inheritance needed, just the right interface
serialize(User("Anil", 28))
serialize(Product("Laptop", 75000.0))
```

### Literal — Restricting to Specific Values

```python
from typing import Literal

LogLevel  = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
SortOrder = Literal["asc", "desc"]
HTTPMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

def log(message: str, level: LogLevel = "INFO") -> None:
    print(f"[{level}] {message}")

def get_users(sort: SortOrder = "asc") -> list:
    ...

log("Server started")           # ✅
log("Error!", level="ERROR")    # ✅
log("Bad", level="VERBOSE")     # ❌ mypy/pyright error — not a valid level
```

### `dataclasses` — Typed Data Classes

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Employee:
    id:         int
    name:       str
    email:      str
    department: str
    salary:     float
    skills:     list[str]         = field(default_factory=list)
    joined_at:  datetime          = field(default_factory=datetime.now)
    manager_id: Optional[int]     = None

    def annual_salary(self) -> float:
        return self.salary * 12

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

emp = Employee(
    id=1042,
    name="Anil Rajamoni",
    email="anil@company.com",
    department="Engineering",
    salary=85000.0,
    skills=["Python", "FastAPI", "PostgreSQL"]
)

print(emp.annual_salary())    # 1020000.0
print(emp)                    # nice __repr__ auto-generated
```

### Type Checking Tools — When and How

| Tool | When to Use |
|------|-------------|
| `mypy` | CLI type checker — run in CI/CD pipeline |
| `pyright` | VS Code default type checker (Pylance) |
| `pydantic` | Runtime validation — FastAPI request models |
| `beartype` | Runtime type checking decorator |
| `pytype` | Google's type inference tool |

```bash
# Install and run mypy
pip install mypy
mypy your_module.py --strict
```

---

## 14. Hands-On Exercises (All Coded)

### Exercise 1 — Custom Range Iterator

```python
class StepRange:
    """
    Like built-in range() but supports float steps.
    range(0, 1, 0.1) doesn't work — this does.
    """

    def __init__(self, start: float, stop: float, step: float = 1.0):
        if step == 0:
            raise ValueError("step cannot be zero")
        self.current = start
        self.stop    = stop
        self.step    = step

    def __iter__(self):
        return self

    def __next__(self) -> float:
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = round(self.current, 10)
        self.current += self.step
        return value

    def __repr__(self):
        return f"StepRange({self.current}, {self.stop}, {self.step})"

# Tests
print(list(StepRange(0, 1, 0.2)))     # [0.0, 0.2, 0.4, 0.6, 0.8]
print(list(StepRange(10, 0, -2)))     # [10, 8, 6, 4, 2]
print(sum(StepRange(1, 6)))           # 15.0
```

### Exercise 2 — Generator-Based Data Pipeline

```python
from typing import Iterator, Generator
import json, random

# Simulate a data source
def generate_sales(count: int) -> Generator[dict, None, None]:
    """Generates simulated sales records."""
    regions   = ["North", "South", "East", "West"]
    products  = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    for i in range(count):
        yield {
            "id":      i + 1,
            "region":  random.choice(regions),
            "product": random.choice(products),
            "amount":  round(random.uniform(500, 100000), 2),
            "refund":  random.random() < 0.1   # 10% chance of refund
        }

def exclude_refunds(records: Iterator[dict]) -> Generator[dict, None, None]:
    for r in records:
        if not r["refund"]:
            yield r

def add_tax(records: Iterator[dict], rate: float = 0.18) -> Generator[dict, None, None]:
    for r in records:
        r["tax"]   = round(r["amount"] * rate, 2)
        r["total"] = round(r["amount"] + r["tax"], 2)
        yield r

def filter_region(records: Iterator[dict], region: str) -> Generator[dict, None, None]:
    for r in records:
        if r["region"] == region:
            yield r

# Build the pipeline lazily
raw      = generate_sales(10000)
valid    = exclude_refunds(raw)
taxed    = add_tax(valid)
north    = filter_region(taxed, "North")

# Consume — nothing computed until here
north_total = sum(r["total"] for r in north)
print(f"North region total (after tax, excl. refunds): ₹{north_total:,.2f}")
```

### Exercise 3 — Decorator Suite

```python
import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s — %(message)s")
logger = logging.getLogger(__name__)

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        ms     = (time.perf_counter() - start) * 1000
        logger.info(f"⏱ {func.__name__}: {ms:.2f}ms")
        return result
    return wrapper

def log_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"❌ {func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper

def cache_result(ttl_seconds: float = 60):
    def decorator(func):
        _cache = {}

        @functools.wraps(func)
        def wrapper(*args):
            now = time.monotonic()
            if args in _cache:
                result, timestamp = _cache[args]
                if now - timestamp < ttl_seconds:
                    logger.info(f"Cache HIT: {func.__name__}{args}")
                    return result
            result = func(*args)
            _cache[args] = (result, now)
            logger.info(f"Cache MISS: {func.__name__}{args}")
            return result
        return wrapper
    return decorator

# Apply all three
@timeit
@log_errors
@cache_result(ttl_seconds=30)
def get_user_profile(user_id: int) -> dict:
    time.sleep(0.1)   # simulates DB query
    return {"id": user_id, "name": f"User_{user_id}", "role": "developer"}

# First call — cache miss, DB query
p1 = get_user_profile(42)
# Second call — cache hit, instant
p2 = get_user_profile(42)
# Different arg — cache miss
p3 = get_user_profile(99)
```

### Exercise 4 — Context Manager Suite

```python
from contextlib import contextmanager
import time, os, json
from pathlib import Path

@contextmanager
def timed_block(label: str):
    start = time.perf_counter()
    print(f"▶ Starting: {label}")
    try:
        yield
    finally:
        ms = (time.perf_counter() - start) * 1000
        print(f"◼ Finished: {label} [{ms:.2f}ms]")

@contextmanager
def atomic_write(path: str):
    """
    Write to a temp file then atomically rename.
    Prevents partial writes from corrupting existing files.
    Standard pattern for config updates and data exports.
    """
    tmp_path = path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            yield f
        os.replace(tmp_path, path)   # atomic on most OSes
        print(f"✅ Atomically written: {path}")
    except Exception:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise

@contextmanager
def managed_transaction(operations_log: list):
    """Simulates a transaction with rollback."""
    snapshot = operations_log.copy()
    try:
        yield operations_log
        print(f"✅ Transaction committed. {len(operations_log)} operations.")
    except Exception as e:
        print(f"❌ Rolling back due to: {e}")
        operations_log.clear()
        operations_log.extend(snapshot)
        raise

# Demo all three
with timed_block("JSON export"):
    data = {"users": list(range(1000)), "generated": time.time()}
    with atomic_write("output.json") as f:
        json.dump(data, f, indent=2)

ops = ["insert user 1", "insert order 101"]
try:
    with managed_transaction(ops) as log:
        log.append("insert payment 201")
        raise ValueError("Payment gateway error")   # triggers rollback
except ValueError:
    pass
print(f"Log after rollback: {ops}")   # original two items only
```

### Exercise 5 — Typed Data Model

```python
from dataclasses import dataclass, field
from typing import Optional, Literal
from datetime import datetime
import json

Priority   = Literal["low", "medium", "high", "critical"]
TaskStatus = Literal["todo", "in_progress", "review", "done", "cancelled"]

@dataclass
class Task:
    id:          str
    title:       str
    description: str
    priority:    Priority
    status:      TaskStatus         = "todo"
    assignee:    Optional[str]      = None
    tags:        list[str]          = field(default_factory=list)
    created_at:  datetime           = field(default_factory=datetime.now)
    updated_at:  Optional[datetime] = None

    def assign(self, username: str) -> "Task":
        self.assignee   = username
        self.updated_at = datetime.now()
        return self

    def move_to(self, status: TaskStatus) -> "Task":
        self.status     = status
        self.updated_at = datetime.now()
        return self

    def to_dict(self) -> dict:
        return {
            "id":          self.id,
            "title":       self.title,
            "priority":    self.priority,
            "status":      self.status,
            "assignee":    self.assignee,
            "tags":        self.tags,
            "created_at":  self.created_at.isoformat(),
        }

@dataclass
class Sprint:
    name:    str
    tasks:   list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_by_priority(self, priority: Priority) -> list[Task]:
        return [t for t in self.tasks if t.priority == priority]

    def get_by_status(self, status: TaskStatus) -> list[Task]:
        return [t for t in self.tasks if t.status == status]

    def summary(self) -> dict[str, int]:
        from collections import Counter
        return dict(Counter(t.status for t in self.tasks))

# Demo
sprint = Sprint("Sprint 42")

t1 = Task("T001", "Fix login bug",      "JWT expiry issue",     "critical")
t2 = Task("T002", "Add dark mode",      "UI enhancement",       "low")
t3 = Task("T003", "Optimize DB query",  "N+1 query on /users",  "high")

sprint.add_task(t1.assign("anil").move_to("in_progress"))
sprint.add_task(t2.assign("bob"))
sprint.add_task(t3.assign("carol").move_to("review"))

print(json.dumps([t.to_dict() for t in sprint.tasks], indent=2))
print(sprint.summary())
print("Critical tasks:", [t.title for t in sprint.get_by_priority("critical")])
```

---

## 15. Mini Project — Performance Monitor Tool (Full Implementation)

Combines generators, decorators, context managers, and type hints into a cohesive production-grade tool.

```python
"""
performance_monitor.py
─────────────────────────────────────────────────────
A production-style performance monitoring tool.
Features:
  - @monitor decorator: measures + logs function execution time
  - @retry decorator: retries failed functions with backoff
  - Timer context manager: measures any code block
  - StatsCollector: tracks and reports aggregated metrics
  - Generator-based log streamer: streams performance logs
"""

import time
import logging
import functools
import statistics
import json
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional, TypeVar, Any
from dataclasses import dataclass, field

# ─── Setup ────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)-8s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("performance.log", encoding="utf-8")
    ]
)
logger = logging.getLogger("perf_monitor")
F = TypeVar("F", bound=Callable[..., Any])

# ─── Stats Collector ──────────────────────────────────────────────────────────

@dataclass
class FunctionStats:
    name:     str
    calls:    int             = 0
    total_ms: float           = 0.0
    min_ms:   float           = float("inf")
    max_ms:   float           = 0.0
    errors:   int             = 0
    timings:  list[float]     = field(default_factory=list)

    def record(self, elapsed_ms: float, success: bool = True):
        self.calls    += 1
        self.total_ms += elapsed_ms
        self.min_ms    = min(self.min_ms, elapsed_ms)
        self.max_ms    = max(self.max_ms, elapsed_ms)
        self.timings.append(elapsed_ms)
        if not success:
            self.errors += 1

    @property
    def avg_ms(self) -> float:
        return self.total_ms / self.calls if self.calls else 0.0

    @property
    def p95_ms(self) -> float:
        if not self.timings:
            return 0.0
        sorted_t = sorted(self.timings)
        idx      = int(len(sorted_t) * 0.95)
        return sorted_t[min(idx, len(sorted_t) - 1)]

    @property
    def error_rate(self) -> float:
        return (self.errors / self.calls * 100) if self.calls else 0.0

    def to_dict(self) -> dict:
        return {
            "function":    self.name,
            "calls":       self.calls,
            "errors":      self.errors,
            "error_rate":  f"{self.error_rate:.1f}%",
            "avg_ms":      f"{self.avg_ms:.2f}",
            "min_ms":      f"{self.min_ms:.2f}",
            "max_ms":      f"{self.max_ms:.2f}",
            "p95_ms":      f"{self.p95_ms:.2f}",
        }

class StatsCollector:
    """Central registry for all function performance stats."""
    _registry: dict[str, FunctionStats] = {}

    @classmethod
    def record(cls, name: str, elapsed_ms: float, success: bool = True):
        if name not in cls._registry:
            cls._registry[name] = FunctionStats(name)
        cls._registry[name].record(elapsed_ms, success)

    @classmethod
    def report(cls) -> list[dict]:
        return [stats.to_dict() for stats in cls._registry.values()]

    @classmethod
    def print_report(cls):
        print("\n" + "═" * 70)
        print("  PERFORMANCE REPORT")
        print("═" * 70)
        print(f"  {'Function':<25} {'Calls':>6} {'Avg(ms)':>9} {'Max(ms)':>9} {'P95(ms)':>9} {'Err%':>6}")
        print("  " + "─" * 68)
        for stats in cls._registry.values():
            print(
                f"  {stats.name:<25} {stats.calls:>6} "
                f"{stats.avg_ms:>9.2f} {stats.max_ms:>9.2f} "
                f"{stats.p95_ms:>9.2f} {stats.error_rate:>5.1f}%"
            )
        print("═" * 70)

    @classmethod
    def save_report(cls, path: str = "perf_report.json"):
        Path(path).write_text(json.dumps(cls.report(), indent=2))
        logger.info(f"Report saved: {path}")

# ─── Decorators ───────────────────────────────────────────────────────────────

def monitor(func: F) -> F:
    """
    Measure and record execution time of a function.
    Logs each call and registers stats in StatsCollector.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start   = time.perf_counter()
        success = True
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            logger.error(f"❌ {func.__name__} raised {type(e).__name__}: {e}")
            raise
        finally:
            ms = (time.perf_counter() - start) * 1000
            StatsCollector.record(func.__name__, ms, success)
            status = "✅" if success else "❌"
            logger.info(f"{status} {func.__name__}: {ms:.2f}ms")
    return wrapper   # type: ignore

def retry(
    max_attempts: int = 3,
    delay: float = 0.5,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,)
):
    """Retry decorator with exponential backoff."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wait = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"💀 {func.__name__} exhausted {max_attempts} retries: {e}")
                        raise
                    logger.warning(f"⚠ {func.__name__} attempt {attempt}/{max_attempts} failed. "
                                   f"Retrying in {wait:.1f}s...")
                    time.sleep(wait)
                    wait *= backoff
        return wrapper   # type: ignore
    return decorator

# ─── Context Manager ──────────────────────────────────────────────────────────

@contextmanager
def timer(label: str, threshold_ms: float = 500):
    """
    Measure any code block. Warns if it exceeds threshold.
    """
    start = time.perf_counter()
    print(f"▶ [{label}] starting...")
    try:
        yield
    finally:
        ms = (time.perf_counter() - start) * 1000
        StatsCollector.record(f"block:{label}", ms)
        flag = "⚠ SLOW" if ms > threshold_ms else "✅"
        print(f"◼ [{label}] {ms:.2f}ms {flag}")
        logger.info(f"Block [{label}]: {ms:.2f}ms")

# ─── Generator — Log Streamer ─────────────────────────────────────────────────

def stream_performance_log(
    path: str,
    keyword: Optional[str] = None
):
    """
    Generator that streams lines from the performance log.
    Optionally filters by keyword.
    """
    log_path = Path(path)
    if not log_path.exists():
        return

    with open(log_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            if keyword is None or keyword.lower() in line.lower():
                yield line

# ─── Demo Functions ───────────────────────────────────────────────────────────

@monitor
@retry(max_attempts=3, delay=0.1, exceptions=(ConnectionError,))
def fetch_user_data(user_id: int) -> dict:
    """Simulates an API call that occasionally fails."""
    import random
    if random.random() < 0.3:   # 30% failure rate
        raise ConnectionError("Simulated connection timeout")
    time.sleep(random.uniform(0.05, 0.2))
    return {"id": user_id, "name": f"User_{user_id}", "status": "active"}

@monitor
def process_batch(records: list[int]) -> dict:
    """Simulates batch data processing."""
    time.sleep(len(records) * 0.001)
    return {"processed": len(records), "failed": 0}

@monitor
def compute_analytics(data: list[float]) -> dict:
    """Simulates heavy computation."""
    time.sleep(0.3)
    return {
        "mean":   statistics.mean(data),
        "stdev":  statistics.stdev(data),
        "median": statistics.median(data)
    }

# ─── Main Demo ────────────────────────────────────────────────────────────────

def main():
    logger.info("Performance Monitor Demo Starting")

    # 1. Test monitored + retried function
    print("\n── API Calls ──────────────────────────")
    for uid in [101, 102, 103, 104, 105]:
        try:
            result = fetch_user_data(uid)
            print(f"  User {uid}: {result['status']}")
        except ConnectionError:
            print(f"  User {uid}: FAILED after retries")

    # 2. Test context manager timer
    print("\n── Timed Blocks ───────────────────────")
    with timer("Batch Processing", threshold_ms=100):
        result = process_batch(list(range(500)))
        print(f"  Result: {result}")

    with timer("Analytics Computation", threshold_ms=100):
        import random
        data   = [random.gauss(50, 10) for _ in range(1000)]
        result = compute_analytics(data)
        print(f"  Mean: {result['mean']:.2f}, StdDev: {result['stdev']:.2f}")

    # 3. Print consolidated report
    StatsCollector.print_report()
    StatsCollector.save_report("perf_report.json")

    # 4. Stream error lines from log
    print("\n── Recent Errors in Log ───────────────")
    for line in stream_performance_log("performance.log", keyword="ERROR"):
        print(f"  {line}")

if __name__ == "__main__":
    main()
```

**Sample output:**
```
── API Calls ──────────────────────────
  User 101: active
  ⚠ fetch_user_data attempt 1/3 failed. Retrying in 0.1s...
  User 102: active
  ...

── Timed Blocks ───────────────────────
▶ [Batch Processing] starting...
◼ [Batch Processing] 500.12ms ⚠ SLOW
  Result: {'processed': 500, 'failed': 0}

══════════════════════════════════════════════════════════════════════
  PERFORMANCE REPORT
══════════════════════════════════════════════════════════════════════
  Function                  Calls   Avg(ms)   Max(ms)   P95(ms)   Err%
  ────────────────────────────────────────────────────────────────────
  fetch_user_data               5    142.31    198.44    195.12   20.0%
  process_batch                 1    500.12    500.12    500.12    0.0%
  compute_analytics             1    303.45    303.45    303.45    0.0%
  block:Batch Processing        1    500.12    500.12    500.12    0.0%
══════════════════════════════════════════════════════════════════════
```

---

## Quick Reference — Day 7 Cheat Sheet

```
ITERATORS:
  __iter__()   → return self
  __next__()   → return next value or raise StopIteration
  iter(x)      → get iterator from iterable
  next(it)     → call __next__
  next(it, d)  → return d instead of StopIteration

GENERATORS:
  yield value  → suspend, send value to caller
  yield from x → delegate to sub-iterator
  gen.send(v)  → send value in (coroutine style)
  (x for x in it)  → generator expression (lazy)

DECORATORS:
  @functools.wraps(func)  → always use inside decorators
  @decorator              → func = decorator(func)
  @decorator(arg)         → func = decorator(arg)(func)  [3 layers]

CONTEXT MANAGERS:
  __enter__()  → setup, return resource
  __exit__(exc_type, exc_val, tb) → cleanup; return True to suppress
  @contextmanager + yield  → generator-based (simpler)
  contextlib.suppress(E)   → ignore specific exceptions
  contextlib.ExitStack     → dynamic number of managers

TYPE HINTS (Python 3.10+ style):
  x: int                   variable annotation
  def f(a: int) -> str     function signature
  list[int]                generic list
  dict[str, Any]           generic dict
  int | None               optional (was Optional[int])
  int | str                union (was Union[int, str])
  Literal["a", "b"]        restrict to specific values
  TypedDict                typed dict structure
  @dataclass               auto-generate __init__, __repr__, etc.
  Protocol                 structural typing (duck typing + types)
```

| Concept | Best For | Key Benefit |
|---------|----------|-------------|
| Iterator class | Stateful, complex iteration logic | Full control |
| Generator function | Simple lazy sequences | Minimal code |
| Generator expression | One-pass aggregation | Memory efficient |
| Generator pipeline | ETL, log processing, data streams | Composable, zero-copy |
| Decorator | Cross-cutting concerns | DRY — apply once, works everywhere |
| Context manager | Resource management | Guaranteed cleanup |
| Type hints | Large codebases, APIs, teams | Early bug detection, IDE support |

---

*Notes compiled for SDE Track — Python Full Stack | Day 7*
