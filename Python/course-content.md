# 35-Day Python Full-Stack Backend Course Content 

**Role focus:** Python Backend Engineer with React (UI) integration awareness  
**Audience:** Students with basic programming exposure (loops, variables)  
**Outcome:** Job-ready Python backend developer with strong **Advanced Python**, **OOP**, **Async**, **Frameworks**, **DB**, **Cloud**, and **AI/LLM fundamentals**

**Overall Time Commitment**
- **Daily:** 2–3h instructor-led + 2–4h practice
- **Weekly:** ~15–18 hours

**Weight Distribution**
- ✅ Python Basics & Foundations → **4 days (~10%)**
- ✅ Advanced Python → **11 days (~30%)**
- ✅ Frameworks + Database → **9 days (~25%)**
- ✅ React UI & Backend Integration → **4 days (~10%)**
- ✅ CI/CD, Docker, AWS → **4 days (~10%)**
- ✅ AI, ML, LLMs → **3 days (~10%)**
- ✅ Projects → **2 days (~5%)**

---

## 📅 DAY-WISE COURSE CONTENT

---

## 🟡 Python Basics & Foundations (Days 1–4)

---

### **Day 1 — Python In-Depth Foundations**
**Concepts (In-depth)**
- **Python Interpreter & Execution Flow**
  - CPython architecture (bytecode compilation)
  - .pyc files and __pycache__
  - Python execution lifecycle: lexical analysis → parsing → AST → bytecode → PVM
  
- **Variables & Memory Model**
  - Dynamic typing vs static typing
  - Object identity, type, and value
  - Memory allocation on heap vs stack
  - Reference counting mechanism
  - Small integer caching (-5 to 256)
  - String interning optimization
  
- **Mutable vs Immutable Types**
  - Immutable: int, float, str, tuple, frozenset, bytes
  - Mutable: list, dict, set, bytearray
  - Deep vs shallow copy (copy module)
  - Implications for function arguments
  
- **id(), reference vs value**
  - Memory address inspection
  - Variable aliasing
  - Identity vs equality operators

**Exercise**
- Write programs to compare memory IDs of different data types
- Demonstrate string interning with `is` operator
- Show list modification vs tuple immutability
- Create shallow vs deep copy scenarios

**Assignment**
- Create a comprehensive markdown document explaining:
  - Memory model with diagrams
  - 5 examples of mutable/immutable behavior
  - Performance implications of immutability
  - When to use `is` vs `==`

**Explore**
- Python is pass-by-object-reference (not pass-by-value or pass-by-reference)
- The `sys.getrefcount()` function
- dis module for bytecode inspection

**Interview Questions**
- Why are strings immutable in Python? (Thread safety, hashability, optimization)
- Difference between `==` and `is`
- Explain Python's memory management
- What happens when you do `a = b = [1,2,3]` and modify the list?
- Why can't you use a list as a dictionary key?

---

### **Day 2 — Control Flow & Functions**
**Concepts**
- **Control Flow Deep Dive**
  - if/elif/else chains and ternary operators
  - for loops with else clause
  - while loops with else clause
  - break, continue, pass keywords
  - Pattern matching with `match/case` (Python 3.10+)
  - List comprehensions vs generator expressions
  - Dictionary and set comprehensions
  
- **Functions In-Depth**
  - Function definition and calling convention
  - Positional vs keyword arguments
  - *args and **kwargs
  - Default argument pitfalls (mutable defaults)
  - Return values vs side effects
  - None as implicit return
  - First-class functions
  - Lambda functions and use cases
  - Type hints and annotations (PEP 484)
  
- **Scope & Namespace**
  - LEGB rule (Local → Enclosing → Global → Built-in)
  - global keyword
  - nonlocal keyword
  - Namespace dictionary inspection (`locals()`, `globals()`)
  - Closures and variable capture

**Exercise**
- Number utilities (prime checker, palindrome, fibonacci)
- Implement functions using different argument patterns
- Demonstrate scope issues and resolutions
- Refactor nested logic into clean functions
- Create higher-order functions (functions returning functions)

**Assignment**
- Build a feature-rich CLI calculator with:
  - Basic operations (+, -, *, /, //, %, **)
  - Scientific functions (sin, cos, sqrt using math module)
  - Memory storage functionality
  - History tracking
  - Error handling for invalid inputs
  - Type hints for all functions

**Explore**
- Python call stack visualization (using traceback)
- functools module (partial, reduce, lru_cache)
- Recursion depth limits (sys.getrecursionlimit())
- Tail call optimization (Python doesn't have it)

**Interview Questions**
- What is recursion? Pros/cons? (Stack overflow risk, base case importance)
- Explain the pitfall of mutable default arguments
- What is a closure? Provide a use case
- Difference between `*args` and `**kwargs`
- How does Python resolve variable names? (LEGB)
- When should you use lambda vs def?

---

### **Day 3 — Data Structures**
**Concepts**
- **Core Data Structures**
  - **Lists**
    - Dynamic arrays internally
    - append, extend, insert, remove, pop operations
    - Slicing and stride (start:stop:step)
    - List methods: sort, reverse, count, index
    - Nested lists and matrix operations
    
  - **Tuples**
    - Immutable sequences
    - Packing and unpacking
    - Named tuples (collections.namedtuple)
    - Use cases: function multiple returns, dictionary keys
    
  - **Sets**
    - Hash table implementation
    - Set operations: union, intersection, difference, symmetric_difference
    - frozenset for immutable sets
    - Set comprehensions
    
  - **Dictionaries**
    - Hash table/hash map implementation
    - Key requirements (hashable, immutable)
    - Dictionary methods: get, setdefault, update, pop, popitem
    - Dictionary views (keys(), values(), items())
    - Dictionary comprehensions
    - OrderedDict vs regular dict (Python 3.7+ preserves insertion order)
    - defaultdict and Counter (collections module)
    - ChainMap for multiple dictionaries
    
- **Time Complexity Analysis**
  - Big O notation basics
  - List operations: O(1) append, O(n) insert, O(n) search
  - Dict operations: O(1) average case for get/set
  - Set operations: O(1) average for membership testing
  - Understanding amortized complexity

- **Space Complexity**
  - Memory overhead of different structures
  - When to optimize for space vs time

**Exercise**
- CRUD operations on dictionary-based student records
- Implement set operations for data filtering
- Performance comparison: list vs set for membership testing
- Create complex nested data structures
- Use Counter for frequency analysis
- Implement a simple cache using dict

**Assignment**
- Student management system (in-memory) with:
  - Add, update, delete, search students
  - Store: name, ID, grades (list), courses (set)
  - Calculate GPA, find top performers
  - Filter students by criteria
  - Data validation (unique IDs, grade ranges)
  - Bonus: Implement using classes with dict storage

**Explore**
- When to use set vs list (uniqueness, membership testing)
- collections module: deque, defaultdict, Counter, OrderedDict
- heapq module for priority queues
- Performance testing with timeit module
- Memory profiling basics

**Interview Questions**
- Why is dict lookup O(1)? (Hash table mechanism)
- Explain hash collisions and resolution
- When would you use a tuple instead of a list?
- Difference between list and deque
- How does a set ensure uniqueness?
- What makes an object hashable?
- Compare list.sort() vs sorted() function

---

### **Day 4 — Modules, Packages & Virtual Environments**
**Concepts**
- **Import System Deep Dive**
  - Module search path (sys.path)
  - import vs from...import
  - Circular imports and how to avoid them
  - `__init__.py` and package initialization
  - Relative vs absolute imports
  - `__all__` for controlling exports
  - Lazy imports and performance
  
- **`__name__ == "__main__"` Pattern**
  - Script vs module execution
  - Entry point best practices
  - Command-line argument parsing (argparse, sys.argv)
  
- **Virtual Environments**
  - Why isolation matters
  - venv creation and activation
  - pip and package management
  - requirements.txt and freeze
  - Development vs production dependencies
  - pip install -e for editable installs
  - Dependency resolution and version conflicts
  
- **Package Structure Best Practices**
  - Organizing modules into packages
  - setup.py and pyproject.toml basics
  - Creating distributable packages
  - src layout pattern
  - Configuration files (.env, config.py)

**Exercise**
- Convert previous student management project into proper package structure:
  ```
  student_manager/
  ├── student_manager/
  │   ├── __init__.py
  │   ├── models.py
  │   ├── operations.py
  │   └── utils.py
  ├── tests/
  ├── README.md
  ├── requirements.txt
  └── setup.py
  ```
- Demonstrate different import styles
- Handle circular import scenarios

**Assignment**
- Restructure previous project with:
  - Clean package hierarchy
  - Separate concerns (models, business logic, utilities)
  - Virtual environment setup
  - requirements.txt with specific versions
  - README with installation and usage instructions
  - CLI interface using argparse
  - Configuration file for settings

**Explore**
- PYTHONPATH environment variable
- importlib for dynamic imports
- Namespace packages
- Entry points for console scripts
- Poetry and modern dependency management
- pip-tools for dependency pinning

**Interview Questions**
- Difference between module and package
- Explain the module search algorithm
- How to resolve circular imports
- Why use virtual environments?
- Difference between pip freeze and pip list
- What is `__init__.py` for?
- Explain relative imports with examples

---

## 🔵 Advanced Python (Days 5–15)

---

### **Day 5 — OOP Fundamentals**
**Concepts**
- **Object-Oriented Programming Paradigm**
  - Principles: Encapsulation, Abstraction, Inheritance, Polymorphism
  - Class vs Object (blueprint vs instance)
  - Class definition syntax
  
- **Constructors and Initialization**
  - `__init__` method (constructor)
  - `__new__` method (rare use cases)
  - Constructor overloading alternatives
  - Initialization parameter validation
  
- **Instance vs Class Variables**
  - Instance attributes (self.variable)
  - Class attributes (shared across instances)
  - When modifications affect all instances
  - Shadowing class variables
  
- **Methods**
  - Instance methods (self)
  - Class methods (@classmethod, cls)
  - Static methods (@staticmethod)
  - When to use each type
  - Method resolution order basics

- **Self Parameter**
  - Why Python requires explicit self
  - Calling conventions internally
  - self vs cls vs no prefix

**Exercise**
- Implement BankAccount class with:
  - Instance variables: account_number, balance, owner
  - Class variable: bank_name, interest_rate
  - Methods: deposit, withdraw, get_balance
  - Class method: create_savings_account
  - Static method: validate_account_number
- Create multiple instances and observe shared vs instance state

**Assignment**
- Extend BankAccount with:
  - Transaction history (list of transactions)
  - Withdraw with balance validation
  - Display account summary
  - Calculate interest earned
  - Implement minimum balance checking
  - Add timestamp to transactions (datetime module)
  - Create different account types using class methods

**Explore**
- Object lifecycle (`__init__`, `__del__`)
- Object identity with id()
- isinstance() and type() checking
- Private name mangling (`__variable`)
- Property decorators preview

**Interview Questions**
- Why use OOP in backend systems? (Modularity, reusability, maintenance)
- Difference between class and instance variables
- When to use @classmethod vs @staticmethod?
- Explain the self parameter
- What is `__init__` vs `__new__`?
- How is OOP different from procedural programming?

---

### **Day 6 — Inheritance & Polymorphism**
**Concepts**
- **Inheritance Fundamentals**
  - Parent/Base/Super class
  - Child/Derived/Sub class
  - `class Child(Parent):` syntax
  - super() function and its importance
  - Accessing parent methods
  - Constructor inheritance and overriding
  
- **Method Overriding**
  - Redefining parent methods
  - Extending vs replacing behavior
  - super() for calling parent implementation
  - Override best practices
  
- **Polymorphism**
  - Same interface, different implementations
  - Duck typing in Python
  - Method overriding as polymorphism
  - Runtime polymorphism
  - Operator overloading preview
  
- **Types of Inheritance**
  - Single inheritance
  - Multiple inheritance
  - Multilevel inheritance
  - Hierarchical inheritance
  - Hybrid inheritance
  
- **Method Resolution Order (MRO)**
  - C3 linearization algorithm
  - `__mro__` attribute
  - `ClassName.mro()` method
  - Understanding complex inheritance chains

**Exercise**
- Create Account hierarchy:
  ```
  Account (base)
  ├── SavingsAccount
  ├── CurrentAccount
  └── FixedDepositAccount
  ```
- Implement specific behaviors:
  - SavingsAccount: interest calculation, withdrawal limits
  - CurrentAccount: overdraft facility, no interest
  - FixedDepositAccount: lock-in period, higher interest
- Demonstrate polymorphic behavior (same method, different logic)

**Assignment**
- Banking system with inheritance:
  - Base Account class with common methods
  - At least 3 derived account types
  - Override withdraw method with specific rules
  - Implement calculate_interest differently for each
  - Add account-specific features
  - Create account factory method
  - Test polymorphism with list of different account types

**Explore**
- Multiple inheritance and diamond problem
- Mixins pattern
- Abstract base classes preview
- Composition vs inheritance
- Liskov Substitution Principle

**Interview Questions**
- Explain the diamond problem and how Python solves it (MRO, C3 linearization)
- When to use inheritance vs composition?
- What is polymorphism? Provide backend examples
- How does super() work in multiple inheritance?
- Difference between overriding and overloading
- What is the Liskov Substitution Principle?

---

### **Day 7 — Encapsulation & Abstraction**
**Concepts**
- **Encapsulation Deep Dive**
  - Data hiding and access control
  - Public attributes (no prefix)
  - Protected attributes (single underscore `_variable`)
  - Private attributes (double underscore `__variable`)
  - Name mangling mechanism (`_ClassName__variable`)
  - Getter and setter methods
  
- **Property Decorators**
  - `@property` for getter
  - `@attribute.setter` for setter
  - `@attribute.deleter` for deletion
  - Computed properties
  - Validation in setters
  - Read-only properties
  - Property vs direct attribute access
  
- **Abstraction with ABC**
  - abc module (Abstract Base Classes)
  - `ABC` class and `@abstractmethod`
  - Abstract properties
  - Forcing subclass implementation
  - Cannot instantiate abstract classes
  - Multiple abstract methods
  - Concrete methods in abstract classes
  
- **Interfaces vs Abstract Classes**
  - Interface concept in Python (informal protocols)
  - Protocol classes (PEP 544)
  - When to use ABCs vs duck typing
  - Designing for contracts

**Exercise**
- Create secure BankAccount with:
  - Private `__balance` attribute
  - Property for reading balance
  - Setter with validation (non-negative)
  - Private `__pin` for security
  - Methods requiring PIN verification
- Demonstrate name mangling behavior
- Create abstract Payment class with:
  - Abstract method: process_payment
  - Abstract property: payment_type
  - Concrete method: log_transaction

**Assignment**
- Payment system with abstraction:
  - Abstract Payment base class
  - Concrete classes: CreditCard, DebitCard, UPI, NetBanking
  - Each implements process_payment differently
  - Use properties for encapsulation
  - Validation logic in setters
  - Cannot create Payment object directly
  - Factory pattern for creating payment instances
  - Security features using private attributes

**Explore**
- Interface vs abstract class differences
- When encapsulation actually matters (APIs, libraries)
- descriptor protocol (`__get__`, `__set__`)
- typing.Protocol for structural subtyping

**Interview Questions**
- Does Python support true encapsulation? (No, conventions only)
- Explain name mangling with example
- When to use @property vs direct attributes?
- Difference between abstract class and interface
- Why use ABC instead of regular inheritance?
- What is the purpose of `@abstractmethod`?
- Can an abstract class have concrete methods?

---

### **Day 8 — Magic Methods & Dataclasses**
**Concepts**
- **Dunder/Magic Methods**
  - String representation:
    - `__str__`: user-friendly string (str(), print())
    - `__repr__`: developer-friendly, unambiguous representation
    - Best practices for both
  
  - Comparison operators:
    - `__eq__`: equality (==)
    - `__lt__`, `__le__`, `__gt__`, `__ge__`: ordering
    - @functools.total_ordering decorator
  
  - Arithmetic operators:
    - `__add__`, `__sub__`, `__mul__`, `__truediv__`
    - Right-hand versions: `__radd__`, etc.
    - In-place versions: `__iadd__`, etc.
  
  - Container methods:
    - `__len__`: len() function
    - `__getitem__`: indexing and slicing
    - `__setitem__`: assignment by index
    - `__delitem__`: deletion by index
    - `__contains__`: 'in' operator
    - `__iter__`: iteration support
  
  - Context managers:
    - `__enter__` and `__exit__`
    - with statement support
  
  - Callable objects:
    - `__call__`: making instances callable
  
  - Attribute access:
    - `__getattr__`, `__setattr__`, `__delattr__`

- **Dataclasses (Python 3.7+)**
  - `@dataclass` decorator
  - Automatic `__init__` generation
  - Automatic `__repr__` generation
  - Automatic `__eq__` generation
  - Field types and default values
  - field() for advanced options
  - Immutable dataclasses (frozen=True)
  - Post-init processing (`__post_init__`)
  - Ordering (order=True)
  - Comparison with namedtuple
  - asdict() and astuple() helpers

**Exercise**
- Create Order class with magic methods:
  - `__str__` and `__repr__`
  - `__eq__` for equality comparison
  - `__lt__` for sorting by total
  - `__len__` for number of items
  - `__getitem__` for accessing items
  - Arithmetic for combining orders
- Create Vector class demonstrating arithmetic operations
- Implement custom context manager for database connection simulation

**Assignment**
- Refactor previous models using dataclasses:
  - Convert at least 2 classes to dataclasses
  - Use type hints for all fields
  - Implement custom `__post_init__` validation
  - Create frozen dataclass for immutable config
  - Implement comparison methods
  - Use field() with default_factory for mutable defaults
  - Create example showing dataclass advantages over regular class

**Explore**
- `__slots__` for memory optimization
- Attribute performance implications
- functools.total_ordering
- More magic methods (`__hash__`, `__bool__`, `__format__`)

**Interview Questions**
- What's the benefit of dataclass? (Less boilerplate, type safety, automatic methods)
- Difference between `__str__` and `__repr__`?
- When to implement `__eq__`?
- What is `__slots__` and when to use it?
- How do magic methods enable operator overloading?
- Explain context managers and their magic methods

---

### **Day 9 — Exceptions & Logging**
**Concepts**
- **Exception Handling Deep Dive**
  - Exception hierarchy in Python
  - try/except/else/finally structure
  - Catching specific vs general exceptions
  - Multiple except blocks
  - Exception chaining (raise...from)
  - Re-raising exceptions
  - Exception groups (Python 3.11+)
  
- **Custom Exceptions**
  - Inheriting from Exception
  - Custom error messages
  - Adding custom attributes
  - When to create custom exceptions
  - Exception naming conventions
  - Building exception hierarchies
  
- **Best Practices**
  - Never catch Exception blindly
  - Specific exceptions first
  - Resource cleanup with finally
  - Context managers for automatic cleanup
  - EAFP vs LBYL (Easier to Ask Forgiveness vs Look Before You Leap)
  
- **Logging Module**
  - Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Logger hierarchy and propagation
  - Handlers (StreamHandler, FileHandler, RotatingFileHandler)
  - Formatters for log messages
  - Configuration methods:
    - basicConfig for simple setup
    - dictConfig for complex setup
    - File-based configuration
  - Logger naming conventions (\_\_name\_\_)
  - Logging best practices for production
  - Structured logging concepts
  - Log rotation and management

**Exercise**
- Create robust error-handling layer:
  - Custom exceptions: InvalidAccountError, InsufficientFundsError
  - Try/except around all user inputs
  - Proper exception messages
  - Resource cleanup scenarios
- Implement logging in previous project:
  - Different log levels for different scenarios
  - File handler with rotation
  - Custom formatter with timestamp
  - Logger per module

**Assignment**
- Add comprehensive error handling and logging:
  - Custom exception hierarchy (minimum 3 exceptions)
  - Validation with appropriate exceptions
  - Logging configuration file
  - Different log levels used appropriately
  - File logging with rotation (max 5MB, 3 backups)
  - Structured log messages with context
  - Exception logging with traceback
  - Separate debug and production logging configs

**Explore**
- Logging levels and when to use each
- traceback module for debugging
- warnings module
- structlog for structured logging
- Sentry integration preview

**Interview Questions**
- Why not use print() in production? (No persistence, levels, filtering, performance)
- Explain exception hierarchy in Python
- When to create custom exceptions?
- Difference between ERROR and CRITICAL logging levels?
- What is EAFP principle?
- How does finally block work with return statements?
- Best practices for exception handling in APIs

---

### **Day 10 — Iterators & Generators**
**Concepts**
- **Iterator Protocol**
  - Iterable vs Iterator
  - `__iter__()` method (returns iterator)
  - `__next__()` method (returns next item or raises StopIteration)
  - iter() and next() built-in functions
  - Creating custom iterators
  - Iterator state management
  - When iterators are exhausted
  
- **Generators**
  - Generator functions with yield
  - yield vs return
  - Generator expressions (genexp)
  - Generator state preservation
  - send(), throw(), close() methods
  - Infinite generators
  - Generator pipelines
  
- **Memory Efficiency**
  - Lazy evaluation concept
  - Generator vs list memory comparison
  - When to use generators (large datasets, streams)
  - itertools module:
    - count, cycle, repeat
    - chain, zip_longest
    - islice, takewhile, dropwhile
    - accumulate, groupby
    - combinations, permutations
  
- **Coroutines Preview**
  - Bidirectional generators
  - send() for pushing values
  - Connection to async programming

**Exercise**
- Implement custom range iterator from scratch
- Create Fibonacci generator (infinite)
- File reader generator (line by line)
- Log file parser using generators
- Chain multiple generators together
- Memory comparison: generator vs list for large dataset

**Assignment**
- File processing with generators:
  - CSV file reader (generator-based)
  - Filter rows based on criteria
  - Transform data lazily
  - Calculate aggregations without loading full file
  - Handle large files (100MB+) efficiently
  - Implement generator pipeline:
    - read → filter → transform → aggregate
  - Compare memory usage with list-based approach
  - Bonus: Process multiple files with itertools.chain

**Explore**
- Memory profiling (memory_profiler)
- yield from syntax
- Generator-based coroutines (pre-async/await)
- more_itertools library

**Interview Questions**
- Generator vs list: when to use which?
- Explain iterator protocol with example
- How do generators save memory?
- What happens when you iterate a generator twice?
- Difference between yield and return?
- Explain lazy evaluation
- What is the purpose of itertools module?

---

### **Day 11 — Decorators**
**Concepts**
- **Decorator Fundamentals**
  - Functions as first-class objects
  - Closures review
  - Wrapper function pattern
  - @ syntax sugar
  - Multiple decorators stacking
  - Order of decorator application
  
- **Function Decorators**
  - Basic decorator structure
  - Preserving function metadata (functools.wraps)
  - Decorators with arguments
  - Parameterized decorators
  - *args and **kwargs in wrappers
  
- **Real-World Use Cases**
  - Timing/profiling decorator
  - Logging decorator
  - Authentication/authorization decorator
  - Caching/memoization (@lru_cache)
  - Retry logic decorator
  - Rate limiting decorator
  - Validation decorator
  - Deprecation warnings
  
- **Class Decorators**
  - Decorating classes
  - Method decorators
  - Property decorators review
  - classmethod and staticmethod as decorators
  
- **Advanced Patterns**
  - Decorator classes (\_\_call\_\_)
  - Decorator factories
  - Stacking decorators properly
  - Preserving signatures

**Exercise**
- Implement timing decorator:
  ```python
  @timing
  def slow_function():
      time.sleep(1)
  ```
- Create logging decorator with level parameter
- Implement authentication simulator:
  ```python
  @require_auth
  def protected_endpoint():
      return "Secret data"
  ```
- Build retry decorator with max attempts
- Memoization decorator for expensive calculations

**Assignment**
- Create decorator library:
  - @timer: execution time logging
  - @retry(max_attempts=3, delay=1): retry on failure
  - @validate_types: runtime type checking
  - @cache: simple memoization
  - @rate_limit(calls=5, period=60): rate limiting
  - @log_calls: log function calls with arguments
  - Demonstrate all decorators with examples
  - Handle decorator stacking
  - Preserve function metadata properly

**Explore**
- functools module (wraps, lru_cache, cache)
- Class decorators vs metaclasses
- Descriptor protocol
- Property as decorator implementation

**Interview Questions**
- How do decorators work internally? (Closures, function replacement)
- Explain functools.wraps purpose
- Difference between @decorator and @decorator()
- How to create decorator with parameters?
- When to use class vs function decorator?
- What is @lru_cache and when to use it?
- Order of execution with multiple decorators?

---

### **Day 12 — Async Python (Core)**
**Concepts**
- **Asynchronous Programming Fundamentals**
  - Sync vs async execution model
  - Concurrency vs parallelism
  - Why async in Python (I/O bound tasks)
  - Event loop architecture
  
- **async/await Syntax**
  - async def for coroutine functions
  - await keyword for awaiting coroutines
  - Coroutine objects
  - Running async code from sync code
  
- **Event Loop**
  - asyncio.run() for running coroutines
  - asyncio.create_task() for concurrent tasks
  - asyncio.gather() for multiple awaits
  - asyncio.wait() with conditions
  - Event loop lifecycle
  - Policy and custom event loops
  
- **Async Patterns**
  - Concurrent API calls
  - Task cancellation
  - Timeouts (asyncio.wait_for)
  - Semaphores for limiting concurrency
  - Async context managers
  - Async iterators and generators
  
- **Common Libraries**
  - aiohttp for async HTTP
  - aiofiles for async file I/O
  - asyncpg for async PostgreSQL
  - httpx for modern async HTTP

**Exercise**
- Basic async function execution
- Concurrent API calls simulation:
  ```python
  async def fetch_data(url):
      # Simulate API call
      await asyncio.sleep(1)
      return f"Data from {url}"
  
  urls = [f"http://api.example.com/{i}" for i in range(10)]
  results = await asyncio.gather(*[fetch_data(url) for url in urls])
  ```
- Compare sync vs async execution time
- Implement task cancellation
- Use semaphore for rate limiting

**Assignment**
- Async file downloader:
  - Download multiple files concurrently
  - Use aiohttp for HTTP requests
  - Limit concurrent downloads (semaphore)
  - Progress tracking per file
  - Timeout handling
  - Error handling per download
  - Aggregate statistics (total time, success/failure count)
  - Compare performance: sync vs async
  - Bonus: Implement retry logic for failed downloads

**Explore**
- asyncio.gather vs asyncio.as_completed
- async with for context managers
- async for for iterations
- Event, Queue, Lock in asyncio
- Bridging sync and async code

**Interview Questions**
- Async vs threading: when to use what? (I/O vs CPU bound)
- Explain event loop mechanism
- What is a coroutine?
- Difference between concurrent and parallel?
- How does await work?
- When NOT to use async?
- Explain asyncio.gather vs asyncio.wait

---

### **Day 13 — Threading & Multiprocessing**
**Concepts**
- **Threading Fundamentals**
  - Thread creation (threading.Thread)
  - Thread lifecycle (start, join, is_alive)
  - Daemon threads
  - Thread pools (concurrent.futures.ThreadPoolExecutor)
  - Thread synchronization:
    - Lock for mutual exclusion
    - RLock (reentrant lock)
    - Semaphore for limiting access
    - Event for signaling
    - Condition for complex coordination
  
- **Global Interpreter Lock (GIL)**
  - What is GIL and why it exists
  - GIL implications for threading
  - Reference counting protection
  - When GIL is released (I/O operations)
  - GIL impact on CPU-bound vs I/O-bound tasks
  
- **Multiprocessing**
  - Process vs Thread
  - multiprocessing.Process
  - Process pools (ProcessPoolExecutor)
  - Inter-process communication:
    - Queue for data exchange
    - Pipe for bidirectional communication
    - Value and Array for shared memory
    - Manager for complex shared objects
  - Process synchronization (Lock, Semaphore in multiprocessing)
  
- **CPU-bound vs I/O-bound**
  - Identifying task types
  - Choosing the right concurrency model:
    - Threading for I/O-bound
    - Multiprocessing for CPU-bound
    - Async for high-concurrency I/O
  - Hybrid approaches
  
- **concurrent.futures**
  - Unified interface for threads and processes
  - ThreadPoolExecutor
  - ProcessPoolExecutor
  - submit() vs map()
  - Future objects and result handling
  - as_completed() for processing results

**Exercise**
- Threading example: concurrent downloads
- Multiprocessing example: parallel computation
- Race condition demonstration with and without locks
- Thread pool for I/O tasks
- Process pool for CPU tasks
- Compare performance: sequential vs threaded vs multiprocessing


**Assignment**
- Benchmark suite comparing concurrency models:
  - Task 1 (I/O-bound): API calls
    - Sequential implementation
    - Threading implementation
    - Async implementation
    - Measure and compare execution time
  
  - Task 2 (CPU-bound): Prime number calculation
    - Sequential implementation
    - Threading implementation (show GIL impact)
    - Multiprocessing implementation
    - Measure and compare execution time
  
  - Analysis document:
    - Performance graphs
    - When to use each approach
    - Resource utilization comparison
    - GIL impact demonstration

**Explore**
- Race conditions and deadlocks
- Thread-safe data structures (queue.Queue)
- weakref for avoiding circular references in threads
- subprocess module for external processes
- joblib for parallel computing

**Interview Questions**
- Why does Python have GIL? (CPython implementation, memory management)
- When does GIL become a bottleneck?
- Threading vs multiprocessing: use cases
- How to share data between processes?
- What is a race condition? How to prevent it?
- Explain deadlock with example
- When to use ThreadPoolExecutor vs ProcessPoolExecutor?

---

### **Day 14 — Memory Management & Garbage Collection**
**Concepts**
- **Memory Management Architecture**
  - Python's memory allocation (pymalloc)
  - Private heap for objects
  - Memory pools and arenas
  - Object allocation strategies
  - Memory overhead per object
  
- **Reference Counting**
  - Primary garbage collection mechanism
  - sys.getrefcount() inspection
  - Reference increment/decrement
  - Immediate deallocation when count reaches 0
  - Advantages and limitations
  
- **Cyclic Garbage Collector**
  - Detecting reference cycles
  - Generational garbage collection (0, 1, 2)
  - gc module interface:
    - gc.collect() manual collection
    - gc.get_count() for generation counts
    - gc.get_threshold() and gc.set_threshold()
    - gc.disable() and gc.enable()
  - Collection frequency and triggers
  
- **Memory Leaks**
  - Common causes in Python:
    - Circular references
    - Unclosed files/connections
    - Global variables
    - Cache without eviction
    - Event handlers not removed
  - Detection techniques
  - Prevention strategies
  
- **Weak References**
  - weakref module
  - WeakValueDictionary and WeakKeyDictionary
  - Use cases (caches, observer pattern)
  - Preventing circular references
  
- **Memory Profiling**
  - memory_profiler tool
  - Line-by-line memory usage
  - tracemalloc module
  - objgraph for reference visualization
  - Memory snapshots and comparison

**Exercise**
- Circular reference demonstration:
  ```python
  class Node:
      def __init__(self):
          self.ref = None
  
  a = Node()
  b = Node()
  a.ref = b
  b.ref = a  # Circular reference
  ```
- Memory leak simulation
- Weak reference examples
- Profile memory usage of different data structures
- Compare memory: list vs tuple vs array

**Assignment**
- Memory analysis project:
  - Create program with memory leak (circular references)
  - Use gc module to detect cycles
  - Implement fixes using weakref
  - Profile memory usage with memory_profiler
  - Document findings:
    - Before and after memory usage
    - GC behavior analysis
    - Best practices learned
  - Create cheat sheet:
    - When to use gc.collect()
    - How to prevent memory leaks
    - Tools for memory debugging

**Explore**
- `__del__` method and finalization
- Context managers for resource management
- sys.getsizeof() for object size
- Resource tracking with tracemalloc
- Memory-efficient data structures

**Interview Questions**
- How does Python free memory? (Reference counting + GC)
- Explain generational garbage collection
- What causes memory leaks in Python?
- When would reference counting fail? (Circular references)
- What is weakref and when to use it?
- How to detect memory leaks in production?
- Difference between gc.collect() and automatic GC?

---

### **Day 15 — Advanced Python Review + Mini Project**

**Morning: Comprehensive Review**
- OOP principles recap with real-world examples
- Async patterns and when to use them
- Memory management best practices
- Decorator patterns in production code
- Exception handling strategies

**Mini Project: CLI-based Library Management System**

**Requirements:**
- **OOP Implementation:**
  - Base class: LibraryItem (books, magazines, DVDs)
  - Derived classes with specific attributes
  - Member class with borrowing history
  - Librarian class with admin privileges
  
- **Advanced Python Features:**
  - Decorators: @require_login, @admin_only, @log_action
  - Generators: Lazy loading of large catalogs
  - Context managers: Database transaction simulation
  - Custom exceptions: ItemNotFound, MemberLimitExceeded
  - Properties: Validation for member age, item status
  
- **Functionality:**
  - Add/remove items from catalog
  - Member registration and management
  - Borrow/return system with due dates
  - Search functionality (by title, author, genre)
  - Late fee calculation
  - Popular items report
  - Member borrowing history
  
- **Data Structures:**
  - Dictionaries for fast lookups
  - Sets for unique items tracking
  - Dataclasses for item representation
  
- **Error Handling:**
  - Custom exception hierarchy
  - Comprehensive logging
  - Input validation
  
- **CLI Interface:**
  - argparse for command-line arguments
  - Interactive menu system
  - Rich output formatting (optional: use rich library)

**Deliverable:**
- GitHub repository with:
  - Clean project structure
  - Comprehensive README
  - requirements.txt
  - Unit tests (preview for later)
  - Example usage documentation
  - Code comments explaining advanced patterns used

**Evaluation Criteria:**
- Proper OOP design
- Effective use of advanced Python features
- Clean code and organization
- Error handling completeness
- Documentation quality

---

## 🟣 Frameworks & Database (Days 16–24)

---

### **Day 16 — Web Basics + Flask Introduction**

**Concepts**

- **HTTP Protocol Deep Dive**
  - Request/Response cycle
  - HTTP methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
  - Status codes families (1xx, 2xx, 3xx, 4xx, 5xx)
  - Important status codes: 200, 201, 400, 401, 403, 404, 500
  - Headers (Content-Type, Authorization, Accept, etc.)
  - Request body formats (JSON, form data, multipart)
  - Query parameters vs path parameters vs body
  
- **REST API Principles**
  - Resource-based architecture
  - Statelessness
  - URI design best practices
  - HTTP methods semantic usage
  - HATEOAS concept
  - API versioning strategies
  
- **Flask Framework Fundamentals**
  - WSGI (Web Server Gateway Interface)
  - Flask application factory pattern
  - Application and request contexts
  - Routing and URL building
  - Request object (request.args, request.json, request.form)
  - Response object and make_response
  - jsonify for JSON responses
  - Flask development server vs production
  
- **Flask Core Concepts**
  - Route decorators and URL rules
  - Variable rules in URLs (<int:id>, <string:name>)
  - HTTP method specification (methods=['GET', 'POST'])
  - Request data access
  - Template rendering basics (for UI context)
  - Static files handling

**Exercise**
```bash
# Setup Flask project
mkdir flask_api && cd flask_api
python -m venv venv
source venv/bin/activate
pip install flask

# Create app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    return jsonify({"id": user_id, "name": "John"})

flask --app app run
```

- Create endpoints for basic CRUD operations
- Handle different HTTP methods
- Access query parameters and JSON body
- Return appropriate status codes

**Assignment**
- Simple CRUD API for TODO items:
  - GET /api/todos - List all todos
  - GET /api/todos/<id> - Get specific todo
  - POST /api/todos - Create new todo
  - PUT /api/todos/<id> - Update todo
  - DELETE /api/todos/<id> - Delete todo
  - In-memory storage (list/dict)
  - Proper HTTP status codes
  - JSON request/response
  - Input validation
  - Error handling with appropriate responses

**Explore**
- Flask extensions ecosystem
- Jinja2 template engine basics
- Flask shell for testing
- CORS basics

**Interview Questions**
- Explain REST principles
- What is WSGI and why is it important?
- Difference between PUT and PATCH?
- When to use 201 vs 200 status code?
- How does Flask routing work?
- What is the request context in Flask?

---

### **Day 17 — Flask Advanced Patterns**

**Concepts**

- **Application Structure**
  - Blueprints for modular applications
  - Application factory pattern
  - Configuration management (config.py)
  - Environment-based configs (dev, test, prod)
  
- **Blueprints Deep Dive**
  - Creating blueprints
  - Registering blueprints
  - Blueprint URL prefixes
  - Blueprint templates and static files
  - Organizing large applications
  
- **Request Lifecycle**
  - before_request hooks
  - after_request hooks
  - teardown_request
  - Error handlers (@app.errorhandler)
  - Custom decorators for routes
  
- **Middleware and Hooks**
  - Custom middleware patterns
  - Request preprocessing
  - Response postprocessing
  - Global error handling
  
- **Advanced Routing**
  - URL converters
  - Custom URL converters
  - url_for() for URL generation
  - Redirect and url_for patterns
  
- **Request Handling**
  - File uploads (request.files)
  - Form data processing
  - JSON validation
  - Request parsing utilities

**Exercise**
- Restructure previous TODO API with blueprints:
  ```
  app/
  ├── __init__.py (app factory)
  ├── api/
  │   ├── __init__.py
  │   ├── todos.py (blueprint)
  │   └── users.py (blueprint)
  ├── models/
  ├── config.py
  └── run.py
  ```

- Implement middleware for:
  - Request logging
  - Authentication check
  - Response timing

**Assignment**
- Modular Flask application:
  - Multiple blueprints (at least 3 resources)
  - Application factory pattern
  - Configuration for dev/test/prod
  - Custom error handlers (404, 500, etc.)
  - Request/response logging middleware
  - Input validation decorator
  - CORS handling
  - Health check endpoint
  - API documentation endpoint (manual)

**Explore**
- Flask-CORS extension
- Flask-Limiter for rate limiting
- Request ID tracking
- Custom Werkzeug converters

**Interview Questions**
- What are Flask blueprints and why use them?
- Explain application factory pattern benefits
- How to handle errors globally in Flask?
- What happens in before_request vs after_request?
- How to structure a large Flask application?

---

### **Day 18 — FastAPI Fundamentals**

**Concepts**

- **FastAPI Introduction**
  - ASGI (Asynchronous Server Gateway Interface)
  - Why FastAPI (performance, async, type hints)
  - Automatic API documentation (Swagger/OpenAPI)
  - FastAPI vs Flask comparison
  
- **Pydantic Models**
  - BaseModel for request/response
  - Type validation and coercion
  - Field validators
  - Custom validation
  - Model configuration
  - Schema generation
  - Nested models
  
- **Path Operations**
  - Decorator-based routing
  - Path parameters with types
  - Query parameters with defaults
  - Request body with Pydantic
  - Response models
  - Status codes in decorators
  - Tags and summary for documentation
  
- **Async in FastAPI**
  - async def vs def route handlers
  - When to use async
  - await in route handlers
  - Background tasks
  
- **Automatic Documentation**
  - /docs (Swagger UI)
  - /redoc (ReDoc)
  - OpenAPI schema generation
  - Customizing documentation

**Exercise**
```bash
pip install fastapi uvicorn[standard] pydantic

# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/", status_code=201)
async def create_item(item: Item):
    return item

uvicorn main:app --reload
```

- Access http://localhost:8000/docs
- Test API using Swagger UI
- Create CRUD endpoints with Pydantic models

**Assignment**
- FastAPI CRUD application:
  - Resource: Products
  - Pydantic models for request/response
  - All CRUD operations
  - Async route handlers
  - Query parameters for filtering/pagination
  - Response models for different scenarios
  - Proper status codes
  - Validation errors handling
  - API documentation with descriptions

**Explore**
- FastAPI middleware
- Dependencies system preview
- Form data handling
- File uploads in FastAPI

**Interview Questions**
- Flask vs FastAPI: when to use which?
- What is Pydantic and why use it?
- Explain ASGI vs WSGI
- How does FastAPI generate documentation?
- When to use async def in FastAPI?

---

### **Day 19 — Dependency Injection & Configuration**

**Concepts**

- **Dependency Injection in FastAPI**
  - Depends() function
  - Function dependencies
  - Class dependencies
  - Dependency chains
  - Sub-dependencies
  - Dependencies with yield (cleanup)
  - Global dependencies
  - Override dependencies for testing
  
- **Common Dependencies**
  - Database session management
  - Authentication verification
  - Pagination parameters
  - Header validation
  - Query parameter parsing
  
- **Configuration Management**
  - Environment variables
  - .env files and python-dotenv
  - Pydantic Settings
  - Configuration validation
  - Secret management
  - Multiple environments (dev, staging, prod)
  
- **Application Settings**
  - BaseSettings class
  - Nested configuration
  - Config from files vs environment
  - Runtime configuration access
  
- **Security Configuration**
  - API keys
  - Database credentials
  - Third-party service credentials
  - Never commit secrets

**Exercise**
```python
from fastapi import Depends, FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My API"
    database_url: str
    secret_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()

# Dependency example
async def get_db():
    db = "database_connection"
    try:
        yield db
    finally:
        print("Closing DB")

@app.get("/items/")
async def read_items(db = Depends(get_db)):
    return {"db": db}
```

- Create common dependencies
- Implement pagination dependency
- Setup environment-based configuration

**Assignment**
- Configuration-driven FastAPI app:
  - Pydantic Settings for config
  - Environment-specific configs (.env.dev, .env.prod)
  - Dependencies for:
    - Database session (simulation)
    - Authentication (token check)
    - Rate limiting
    - Pagination (page, size)
  - Reuse dependencies across routes
  - Settings validation
  - Config documentation
  - Example showing dependency override for testing

**Explore**
- Secrets management (AWS Secrets Manager, Vault)
- dotenv vs environment variables
- 12-factor app methodology
- Configuration schema validation

**Interview Questions**
- What is dependency injection and its benefits?
- How does FastAPI's Depends() work?
- Why use Pydantic Settings for configuration?
- How to manage secrets securely?
- How to test code with dependencies?

---

### **Day 20 — PostgreSQL & SQL Deep Dive**

**Concepts**

- **Relational Database Fundamentals**
  - ACID properties (Atomicity, Consistency, Isolation, Durability)
  - Tables, rows, columns
  - Primary keys and foreign keys
  - Constraints (NOT NULL, UNIQUE, CHECK, DEFAULT)
  - Data types in PostgreSQL
  
- **SQL Core Operations**
  - DDL (Data Definition Language):
    - CREATE TABLE with constraints
    - ALTER TABLE (add/modify/drop columns)
    - DROP TABLE
    - TRUNCATE vs DELETE
  
  - DML (Data Manipulation Language):
    - INSERT with multiple rows
    - SELECT with WHERE, ORDER BY, LIMIT
    - UPDATE with conditions
    - DELETE with conditions
  
  - DQL (Data Query Language):
    - SELECT clause anatomy
    - WHERE conditions (AND, OR, NOT, IN, BETWEEN, LIKE)
    - Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
    - GROUP BY and HAVING
    - ORDER BY ASC/DESC
    - LIMIT and OFFSET for pagination
  
- **Joins Deep Dive**
  - INNER JOIN
  - LEFT JOIN (LEFT OUTER JOIN)
  - RIGHT JOIN (RIGHT OUTER JOIN)
  - FULL OUTER JOIN
  - CROSS JOIN
  - Self joins
  - Multiple table joins
  
- **Indexes**
  - What are indexes and why use them
  - B-tree index (default)
  - Index on single vs multiple columns
  - Unique indexes
  - When indexes help (WHERE, JOIN, ORDER BY)
  - Index overhead on writes
  - EXPLAIN for query analysis
  
- **Transactions**
  - BEGIN/COMMIT/ROLLBACK
  - Transaction isolation levels
  - Concurrent access issues
  - Deadlocks
  
- **Schema Design Best Practices**
  - Normalization (1NF, 2NF, 3NF)
  - When to denormalize
  - Naming conventions
  - Data types selection
  - NULL handling

**Exercise**
```sql
-- Setup database
CREATE DATABASE library_db;

-- Tables with relationships
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT REFERENCES authors(id),
    published_year INT,
    price DECIMAL(10, 2),
    stock INT DEFAULT 0
);

CREATE INDEX idx_books_author ON books(author_id);
CREATE INDEX idx_books_year ON books(published_year);

-- Complex queries
SELECT a.name, COUNT(b.id) as book_count
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.id, a.name
HAVING COUNT(b.id) > 2;
```

- Write queries for various scenarios
- Practice all types of joins
- Analyze query performance with EXPLAIN

**Assignment**
- E-commerce database schema:
  - Tables: users, products, categories, orders, order_items
  - Proper relationships and foreign keys
  - Appropriate indexes
  - Constraints for data integrity
  - Write SQL for:
    - User registration
    - Product catalog with categories
    - Order placement (transactions)
    - Order history for user
    - Product search with filters
    - Sales report (aggregations, joins)
    - Top selling products
  - Include EXPLAIN output for complex queries
  - Document normalization decisions

**Explore**
- PostgreSQL-specific features (JSONB, arrays)
- Full-text search
- Window functions
- CTEs (Common Table Expressions)
- Views and materialized views

**Interview Questions**
- Explain ACID properties with examples
- When to use indexes and potential downsides?
- Difference between INNER JOIN and LEFT JOIN?
- What is normalization and why is it important?
- How to optimize slow queries?
- Explain transaction isolation levels
- What is the N+1 query problem?

---

### **Day 21 — SQLAlchemy ORM**

**Concepts**

- **ORM Fundamentals**
  - Object-Relational Mapping concept
  - ORM vs raw SQL trade-offs
  - SQLAlchemy architecture
  - Core vs ORM layers
  
- **Engine and Session**
  - create_engine() configuration
  - Connection pooling
  - Session lifecycle
  - sessionmaker factory
  - Scoped sessions
  - Session best practices
  
- **Declarative Models**
  - Base class setup
  - Column types and options
  - Primary keys and autoincrement
  - Nullable and default values
  - Unique and index constraints
  - Custom column names
  
- **Relationships**
  - One-to-Many (relationship, ForeignKey)
  - Many-to-One (backref, back_populates)
  - One-to-One (uselist=False)
  - Many-to-Many (association tables)
  - Lazy loading strategies (select, joined, subquery)
  - Cascade operations
  
- **Querying**
  - session.query() basics
  - Filtering (filter, filter_by)
  - Ordering and limiting
  - Joins with ORM
  - Eager loading (joinedload, selectinload)
  - Aggregations
  - Exists and count
  
- **CRUD Operations**
  - Create: session.add()
  - Read: session.query()
  - Update: modify and commit
  - Delete: session.delete()
  - Bulk operations
  - session.commit() and session.rollback()

**Exercise**
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

engine = create_engine('postgresql://user:pass@localhost/dbname')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# CRUD examples
new_user = User(username="john")
session.add(new_user)
session.commit()

users = session.query(User).filter_by(username="john").all()
```

- Create complete model hierarchy
- Practice all relationship types
- Compare lazy vs eager loading performance

**Assignment**
- Blog system with SQLAlchemy:
  - Models:
    - User (id, username, email, password_hash, created_at)
    - Post (id, title, content, user_id, created_at, updated_at)
    - Comment (id, content, post_id, user_id, created_at)
    - Tag (id, name)
    - PostTag (association table)
  - Relationships:
    - User → Posts (one-to-many)
    - Post → Comments (one-to-many)
    - Post ↔ Tags (many-to-many)
  - Functionality:
    - Create users, posts, comments, tags
    - Get all posts by user (with eager loading)
    - Get post with comments and author
    - Search posts by tag
    - Update and delete operations
  - Compare N+1 query problem with and without eager loading

**Explore**
- Hybrid properties
- Association proxies
- Event system
- Query optimization
- Connection pooling tuning

**Interview Questions**
- Benefits and drawbacks of ORMs?
- Explain lazy loading vs eager loading
- What is the N+1 problem and how to solve it?
- How do SQLAlchemy sessions work?
- Difference between backref and back_populates?
- When to use Core vs ORM in SQLAlchemy?

---

### **Day 22 — Alembic & Database Migrations**

**Concepts**

- **Database Migrations**
  - Why migrations are necessary
  - Version control for database schema
  - Migration workflow in teams
  - Development vs production migrations
  
- **Alembic Fundamentals**
  - Alembic architecture
  - Migration environment setup
  - alembic.ini configuration
  - env.py customization
  
- **Migration Operations**
  - Autogenerate migrations
  - Manual migrations
  - Upgrade and downgrade
  - Revision history
  - Branching and merging
  
- **Common Migration Tasks**
  - Adding/removing columns
  - Changing column types
  - Adding/removing indexes
  - Data migrations
  - Adding/removing tables
  - Modifying constraints
  
- **Best Practices**
  - Always review autogenerated migrations
  - Test migrations before production
  - Write reversible migrations
  - Data migration strategies
  - Handling production data safely

**Exercise**
```bash
# Install Alembic
pip install alembic

# Initialize Alembic
alembic init migrations

# Configure alembic.ini
sqlalchemy.url = postgresql://user:pass@localhost/dbname

# Create first migration
alembic revision --autogenerate -m "create users table"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1

# Check current version
alembic current

# View history
alembic history
```

- Create migrations for schema changes
- Test upgrade and downgrade
- Handle data migration scenario

**Assignment**
- Migration workflow project:
  - Setup Alembic for existing project
  - Initial migration capturing current schema
  - Create migrations for:
    - Adding new table (categories)
    - Adding column to existing table (user.bio)
    - Creating index (email index)
    - Data migration (populate default categories)
    - Removing column (deprecated field)
  - Test full upgrade path
  - Test downgrade for each migration
  - Document migration strategy
  - Create migration checklist for team

**Explore**
- Branching and merging migrations
- Offline migration generation
- Custom migration templates
- Testing migrations
- Continuous deployment with migrations

**Interview Questions**
- Why use database migrations?
- How does Alembic detect schema changes?
- What is migration downgrade and when is it used?
- How to handle data migrations safely?
- Migration strategy for production deployments?
- What happens if autogenerate misses changes?

---

### **Day 23 — Authentication & Authorization (JWT)**

**Concepts**

- **Authentication vs Authorization**
  - Authentication (AuthN): Who are you?
  - Authorization (AuthZ): What can you do?
  - Relationship between the two
  
- **Password Security**
  - Never store plain-text passwords
  - Password hashing (bcrypt, Argon2)
  - Salt and pepper
  - Work factor/cost parameter
  - Password policies
  
- **JWT (JSON Web Tokens)**
  - JWT structure (Header.Payload.Signature)
  - Signing algorithms (HS256, RS256)
  - Claims (iss, sub, exp, iat, etc.)
  - Access tokens vs refresh tokens
  - Token expiration strategies
  - Token revocation challenges
  
- **OAuth 2.0 Basics**
  - Authorization code flow
  - Client credentials flow
  - Implicit flow
  - Access tokens and scopes
  
- **Implementation in FastAPI**
  - OAuth2PasswordBearer
  - OAuth2PasswordRequestForm
  - Security dependencies
  - Token generation
  - Token verification
  - Protected routes
  
- **Security Best Practices**
  - HTTPS only for production
  - Secure token storage (client-side)
  - Token expiration
  - Refresh token rotation
  - CSRF protection
  - Rate limiting login attempts

**Exercise**
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
        return username
    except JWTError:
        raise HTTPException(status_code=401)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verify user and password
    # Generate and return token
    pass

@app.get("/users/me")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
```

- Implement complete auth flow
- Test with different users and roles

**Assignment**
- Full authentication system:
  - User registration with password hashing
  - Login with JWT token generation
  - Token verification dependency
  - Protected endpoints
  - User roles (user, admin)
  - Role-based access control
  - Refresh token implementation
  - Logout (token blacklist simulation)
  - Password reset flow (email simulation)
  - Security headers middleware

**Explore**
- OAuth 2.0 with external providers
- Session-based vs token-based auth
- Multi-factor authentication
- API key authentication
- RBAC (Role-Based Access Control) patterns

**Interview Questions**
- Explain JWT structure and how it works
- Authentication vs authorization difference?
- Why hash passwords instead of encrypting?
- What are refresh tokens and why use them?
- How to implement logout with JWT?
- What is OAuth 2.0 and when to use it?
- Security risks with JWT and mitigations?

---

### **Day 24 — API Testing with pytest**

**Concepts**

- **Testing Pyramid**
  - Unit tests (functions, classes)
  - Integration tests (database, external APIs)
  - End-to-end tests (full request flow)
  - Test coverage goals
  
- **pytest Fundamentals**
  - Test discovery (test_*.py, *_test.py)
  - Test functions and classes
  - Assertions (assert statements)
  - Test markers (@pytest.mark)
  - Skipping tests
  - Parametrized tests
  
- **Fixtures**
  - Setup and teardown
  - Fixture scope (function, class, module, session)
  - Fixture dependencies
  - yield fixtures for cleanup
  - conftest.py for shared fixtures
  
- **Testing FastAPI**
  - TestClient from starlette
  - Overriding dependencies
  - Testing with test database
  - Mocking external services
  - Testing authentication
  
- **Database Testing**
  - Test database setup
  - Fixture for database session
  - Rollback after each test
  - Factory pattern for test data
  - SQLite in-memory for speed
  
- **Code Coverage**
  - pytest-cov plugin
  - Coverage reports
  - Coverage goals (80%+)
  - Excluding files from coverage
  
- **Best Practices**
  - AAA pattern (Arrange, Act, Assert)
  - One assertion per test (guideline)
  - Descriptive test names
  - Independent tests
  - Fast test execution

**Exercise**
```python
# test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# With fixtures
import pytest

@pytest.fixture
def test_user():
    return {"username": "testuser", "password": "testpass"}

def test_create_user(test_user):
    response = client.post("/users/", json=test_user)
    assert response.status_code == 201
    assert response.json()["username"] == test_user["username"]
```

**Parametrized test**
```python
@pytest.mark.parametrize("endpoint,expected_status", [
("/", 200),
("/users", 200),
("/nonexistent", 404),
])
def test_endpoints(endpoint, expected_status):
    response = client.get(endpoint)
    assert response.status_code == expected_status
```
- Write tests for all CRUD operations
- Test authentication flow
- Test error cases

**Assignment**
- Comprehensive test suite:
  - Test configuration for separate test database
  - Fixtures:
    - Database session (with rollback)
    - Test client
    - Authenticated user
    - Test data factories
  - Tests for:
    - User registration (success and failure cases)
    - Login (valid/invalid credentials)
    - Protected endpoint access (with/without token)
    - CRUD operations (all methods)
    - Input validation
    - Error responses
    - Edge cases
  - Parametrized tests for multiple scenarios
  - Achieve 80%+ code coverage
  - Coverage report in HTML format

**Explore**
- pytest plugins (pytest-asyncio, pytest-xdist)
- Mocking with unittest.mock or pytest-mock
- Test factories (factory_boy)
- Continuous testing
- TDD (Test-Driven Development)

**Interview Questions**
- Why write tests for APIs?
- Explain test pyramid concept
- What are pytest fixtures and their scopes?
- How to test database operations without affecting production?
- What is code coverage and what's a good target?
- How to test authentication in APIs?
- Difference between unit and integration tests?

---

## 🟢 React UI & Backend Integration (Days 25–28)

---

### **Day 25 — React Overview & Fundamentals**

**Concepts**

- **React Basics for Backend Developers**
  - Component-based architecture
  - Virtual DOM concept
  - JSX syntax basics
  - React vs vanilla JavaScript
  
- **Components**
  - Functional components
  - Component composition
  - Props (properties)
  - Children prop
  - Component reusability
  
- **State Management**
  - useState hook
  - State immutability
  - Lifting state up
  - State vs props
  
- **Hooks**
  - useState for local state
  - useEffect for side effects
  - useEffect dependency array
  - Cleanup in useEffect
  - Custom hooks basics
  
- **Event Handling**
  - onClick, onChange, onSubmit
  - Event object
  - Preventing default behavior
  - Event handlers with parameters
  
- **Conditional Rendering**
  - if/else in JSX
  - Ternary operators
  - && for conditional display
  
- **Lists and Keys**
  - Rendering arrays with map()
  - Key prop importance
  - List item components

**Exercise**
```jsx
// Basic component
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

// Todo list component
function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  
  const addTodo = () => {
    setTodos([...todos, { id: Date.now(), text: input }]);
    setInput('');
  };
  
  return (
    <div>
      <input 
        value={input} 
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={addTodo}>Add</button>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>{todo.text}</li>
        ))}
      </ul>
    </div>
  );
}
```

- Build simple interactive components
- Practice state management
- Handle user input

**Assignment**
- React fundamentals project:
  - Todo app with:
    - Add todo functionality
    - Mark as complete (toggle)
    - Delete todo
    - Filter (all/active/completed)
    - Todo count
  - Use multiple components:
    - TodoList
    - TodoItem
    - TodoForm
    - TodoFilter
  - Props passing between components
  - State management best practices
  - Clean component structure

**Explore**
- React Developer Tools
- Component lifecycle (with hooks)
- Form handling patterns
- Controlled vs uncontrolled components

**Interview Questions (Backend Context)**
- How does React differ from traditional web pages?
- What are components and why use them?
- Explain useState hook
- What is the virtual DOM?
- Why do lists need keys?

---

### **Day 26 — React + Backend API Integration**

**Concepts**

- **HTTP Requests from React**
  - fetch API
  - axios library
  - HTTP methods in frontend context
  - Handling responses
  - Error handling
  
- **useEffect for Data Fetching**
  - Fetching on component mount
  - Dependency array usage
  - Cleanup functions
  - Avoiding infinite loops
  
- **Async State Management**
  - Loading states
  - Error states
  - Success states
  - Optimistic updates
  
- **CORS (Cross-Origin Resource Sharing)**
  - What is CORS and why it exists
  - Same-origin policy
  - CORS headers:
    - Access-Control-Allow-Origin
    - Access-Control-Allow-Methods
    - Access-Control-Allow-Headers
  - Preflight requests (OPTIONS)
  - FastAPI CORS middleware
  - Development vs production CORS
  
- **API Integration Patterns**
  - Base URL configuration
  - API client abstraction
  - Request/response interceptors
  - Centralized error handling

**Exercise**
```jsx
// Fetch data from API
import { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetch('http://localhost:8000/api/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

// Using axios
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

function createUser(userData) {
  return api.post('/users', userData);
}
```

- Connect React app to FastAPI backend
- Setup CORS in FastAPI
- Handle loading and error states

**Assignment**
- Full-stack CRUD application:
  - Backend: FastAPI with products API
  - Frontend: React product management
  - Features:
    - List all products (GET)
    - Add new product (POST with form)
    - Update product (PUT)
    - Delete product (DELETE with confirmation)
  - Loading indicators
  - Error handling and display
  - Form validation
  - Success notifications
  - Environment-based API URL
  - API client service layer
  - CORS properly configured

**Explore**
- React Query for server state
- SWR for data fetching
- Axios interceptors
- Request cancellation

**Interview Questions**
- What is CORS and why does it matter?
- How to handle API errors in React?
- Why use useEffect for data fetching?
- fetch vs axios comparison?
- Best practices for API integration?

---

### **Day 27 — Authentication Integration**

**Concepts**

- **Frontend Authentication Flow**
  - Login form submission
  - Token reception and storage
  - Token inclusion in requests
  - Token expiration handling
  - Logout functionality
  
- **Token Storage**
  - localStorage vs sessionStorage
  - Cookie-based storage
  - Security considerations
  - XSS and CSRF risks
  
- **Protected Routes**
  - Route guards
  - Redirect to login
  - Conditional rendering
  - React Router integration
  
- **Auth Context**
  - Context API for global auth state
  - Auth provider pattern
  - useContext for accessing auth
  - Centralized auth logic
  
- **Authenticated Requests**
  - Authorization header
  - Bearer token format
  - Axios interceptors for auto-inclusion
  - Handling 401 responses

**Exercise**
```jsx
// Auth context
import { createContext, useState, useContext } from 'react';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  
  const login = async (credentials) => {
    const response = await fetch('http://localhost:8000/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(credentials),
    });
    const data = await response.json();
    setToken(data.access_token);
    localStorage.setItem('token', data.access_token);
  };
  
  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
  };
  
  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);

// Protected component
function ProtectedPage() {
  const { token } = useAuth();
  const [data, setData] = useState(null);
  
  useEffect(() => {
    fetch('http://localhost:8000/protected', {
      headers: { 'Authorization': `Bearer ${token}` },
    })
      .then(res => res.json())
      .then(setData);
  }, [token]);
  
  return <div>{data?.message}</div>;
}
```

- Implement login/logout UI
- Store and use JWT tokens
- Protect routes based on auth state

**Assignment**
- Authenticated React application:
  - Backend: FastAPI with JWT auth
  - Frontend features:
    - Login form
    - Registration form
    - Auth context provider
    - Token storage (localStorage)
    - Axios interceptor for auth header
    - Protected routes (redirect if not authenticated)
    - Logout functionality
    - Token expiration handling (refresh or redirect)
    - User profile page (requires auth)
    - Role-based UI (show/hide based on permissions)
  - Error handling for auth failures
  - Loading states during auth operations

**Explore**
- Refresh token implementation
- OAuth social login
- Session management
- Secure cookie storage

**Interview Questions**
- How to store tokens securely in frontend?
- What is token-based authentication flow?
- How to handle token expiration?
- XSS and CSRF: what are they and how to prevent?
- Why use Context API for auth?

---

### **Day 28 — Full Stack Integration & Deployment Prep**

**Concepts**

- **Full Stack Architecture**
  - Frontend and backend separation
  - API as contract between layers
  - Development vs production setup
  - Proxy configuration
  
- **Environment Configuration**
  - React environment variables (.env)
  - REACT_APP_ prefix
  - Build-time vs runtime config
  - Backend environment config
  
- **Error Handling Across Stack**
  - API error responses
  - Frontend error display
  - User-friendly error messages
  - Error logging
  
- **Production Considerations**
  - Build process (npm run build)
  - Serving React build from backend
  - Static file serving
  - API and frontend on same domain
  
- **Full Request Flow**
  - User interaction → Event handler
  - HTTP request → Backend
  - Database query → Response
  - State update → UI render

**Exercise**
- Build complete feature end-to-end:
  - Backend endpoint
  - Database model
  - Frontend component
  - API integration
  - Error handling
  - Loading states

**Assignment**
- Full-stack mini application:
  - **Project: Task Management System**
  - Backend (FastAPI):
    - Task CRUD API
    - User authentication
    - Task assignment to users
    - PostgreSQL database
    - Alembic migrations
    - pytest tests
  
  - Frontend (React):
    - Login/Register pages
    - Task list with filtering
    - Create/edit task forms
    - Task assignment UI
    - User profile
    - Responsive design (basic)
  
  - Integration:
    - Authentication flow
    - CRUD operations
    - Error handling
    - Loading indicators
    - Success feedback
  
  - Deployment prep:
    - Environment config for dev/prod
    - Build scripts
    - README with setup instructions
    - Docker Compose for local development

**Deliverable:**
- GitHub repository with:
  - Backend and frontend code
  - Database schema
  - API documentation
  - Setup instructions
  - Demo video or screenshots

**Explore**
- WebSockets for real-time features
- Server-Sent Events (SSE)
- GraphQL as alternative to REST
- State management (Redux, Zustand)

**Interview Questions**
- Explain full request/response cycle
- How to structure full-stack projects?
- Development vs production configurations?
- How to serve React app from backend?
- Security considerations in full-stack apps?

---

## 🟠 CI/CD, Docker & AWS (Days 29–32)

---

### **Day 29 — Docker Fundamentals**

**Concepts**

- **Containerization Basics**
  - What are containers and why use them
  - Containers vs Virtual Machines
  - Docker architecture (client, daemon, registry)
  - Images vs containers
  - Docker registry and Docker Hub
  
- **Docker Images**
  - Dockerfile syntax and best practices
  - Base images (python:3.11-slim, etc.)
  - Layers and layer caching
  - .dockerignore file
  - Multi-stage builds
  - Image tags and versioning
  
- **Docker Containers**
  - Running containers
  - Port mapping (-p)
  - Volume mounting (-v)
  - Environment variables (-e)
  - Container lifecycle
  - Container logs and debugging
  
- **Dockerfile Best Practices**
  - Minimize layers
  - Order instructions for cache efficiency
  - Use specific base image versions
  - Don't run as root
  - Clean up in same layer
  - Use .dockerignore

**Exercise**
```dockerfile
# Dockerfile for FastAPI app
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Non-root user
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
```bash
# Build image
docker build -t my-api:latest .

# Run container
docker run -d -p 8000:8000 --name api-container my-api:latest

# View logs
docker logs api-container

# Execute command in container
docker exec -it api-container bash

# Stop and remove
docker stop api-container
docker rm api-container
```

- Containerize FastAPI application
- Test container locally
- Optimize Dockerfile

**Assignment**
- Docker containerization project:
  - Dockerfile for FastAPI backend
  - Multi-stage build (if applicable)
  - Environment variable configuration
  - Health check instruction
  - .dockerignore file
  - Build and run locally
  - Document:
    - Build instructions
    - Run instructions
    - Environment variables
    - Port mappings
  - Optimize image size (compare before/after)
  - Include database connection handling

**Explore**
- Docker volumes for persistence
- Docker networks
- Container registries (ECR, GCR)
- Image scanning for vulnerabilities

**Interview Questions**
- Containers vs VMs: explain difference
- What is a Docker layer?
- How to optimize Docker image size?
- Explain multi-stage builds
- Why use .dockerignore?
- How to debug a container?

---

### **Day 30 — Docker Compose**

**Concepts**

- **Docker Compose Overview**
  - Orchestrating multiple containers
  - docker-compose.yml syntax
  - Services, networks, volumes
  - Version differences (v3 most common)
  
- **Service Definition**
  - Image vs build
  - Environment variables
  - Port mappings
  - Volume mounts
  - Depends_on for service dependencies
  - Health checks
  - Restart policies
  
- **Networking**
  - Default network creation
  - Custom networks
  - Service discovery by name
  - Port exposure
  
- **Volumes**
  - Named volumes vs bind mounts
  - Persistent data storage
  - Sharing volumes between services
  
- **Common Patterns**
  - App + database stack
  - Development environment
  - Environment-specific overrides
  - Secrets management

**Exercise**
```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/mydb
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./app:/app  # For development hot-reload

volumes:
  postgres_data:
```
```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f api

# Stop all services
docker compose down

# Remove with volumes
docker compose down -v
```

- Create multi-container setup
- Test service communication
- Manage development environment

**Assignment**
- Complete development environment:
  - Services:
    - FastAPI backend
    - PostgreSQL database
    - Redis (for caching/sessions)
    - Optional: nginx as reverse proxy
  - docker-compose.yml features:
    - Health checks for all services
    - Named volumes for persistence
    - Environment file (.env) usage
    - Development overrides (docker-compose.dev.yml)
  - Test:
    - Start entire stack with one command
    - Verify service communication
    - Database migrations on startup
    - Hot-reload for development
  - Documentation:
    - Setup guide
    - Service descriptions
    - Useful commands cheat sheet

**Explore**
- docker-compose override files
- Scaling services
- Compose in production (Docker Swarm, Kubernetes)
- Traefik for routing

**Interview Questions**
- Why use Docker Compose?
- Explain depends_on and service_healthy
- How do services communicate in Compose?
- Volumes vs bind mounts: when to use which?
- How to handle secrets in Compose?

---

### **Day 31 — AWS Core Services**

**Concepts**

- **AWS Overview**
  - Cloud computing basics
  - AWS global infrastructure
  - Regions and Availability Zones
  - AWS Free Tier
  
- **IAM (Identity and Access Management)**
  - Users, groups, roles
  - Policies and permissions
  - Least privilege principle
  - Access keys vs console access
  - MFA (Multi-Factor Authentication)
  
- **EC2 (Elastic Compute Cloud)**
  - Virtual servers in cloud
  - Instance types and families
  - AMIs (Amazon Machine Images)
  - Security groups (firewall)
  - Key pairs for SSH
  - Elastic IP addresses
  
- **S3 (Simple Storage Service)**
  - Object storage basics
  - Buckets and objects
  - Storage classes
  - Bucket policies and ACLs
  - Pre-signed URLs
  - S3 as static website host
  
- **RDS (Relational Database Service)**
  - Managed database service
  - PostgreSQL on RDS
  - Backups and snapshots
  - Multi-AZ for high availability
  - Security groups for database
  
- **VPC (Virtual Private Cloud)**
  - Private networks in AWS
  - Subnets (public and private)
  - Internet Gateway
  - Security groups vs NACLs

**Exercise (Hands-on)**
```python
# S3 file upload with boto3
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
    except ClientError as e:
        print(f"Error: {e}")
        return False
    return True

# Generate pre-signed URL
def create_presigned_url(bucket_name, object_name, expiration=3600):
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        return url
    except ClientError as e:
        print(f"Error: {e}")
        return None
```

- Create AWS account (Free Tier)
- Setup IAM user with appropriate permissions
- Create S3 bucket and upload files
- Launch EC2 instance and SSH into it

**Assignment**
- AWS infrastructure setup:
  - IAM:
    - Create user with programmatic access
    - Create appropriate policies
    - Setup MFA
  - S3:
    - Create bucket for file storage
    - Upload files via boto3
    - Implement pre-signed URLs
    - Set bucket policies
  - EC2:
    - Launch t2.micro instance
    - Configure security group (SSH, HTTP)
    - Install Docker on EC2
    - Deploy containerized app
  - Document:
    - Architecture diagram
    - Security best practices followed
    - Cost estimation

**Explore**
- CloudWatch for monitoring
- Application Load Balancer
- Route 53 for DNS
- CloudFormation for infrastructure as code
- AWS CLI

**Interview Questions**
- What is IAM and why is it important?
- EC2 vs on-premise servers benefits?
- When to use S3 vs EBS?
- Explain AWS security groups
- What is a VPC?
- S3 storage classes and use cases?

---

### **Day 32 — CI/CD & Deployment**

**Concepts**

- **CI/CD Fundamentals**
  - Continuous Integration (CI)
  - Continuous Deployment (CD)
  - Benefits of automation
  - CI/CD pipeline stages
  
- **GitHub Actions**
  - Workflows and events
  - Jobs and steps
  - Runners (GitHub-hosted vs self-hosted)
  - Secrets management
  - Environment variables
  - Matrix builds
  
- **CI Pipeline**
  - Code checkout
  - Dependency installation
  - Linting and formatting
  - Running tests
  - Code coverage
  - Building artifacts
  
- **CD Pipeline**
  - Building Docker images
  - Pushing to registry
  - Deploying to environments
  - Deployment strategies (blue-green, rolling)
  
- **Deployment Targets**
  - EC2 deployment
  - ECS (Elastic Container Service)
  - Docker Compose on server
  - Automated deployment scripts

**Exercise**
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run linter
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Run tests
      run: |
        pytest --cov=./ --cov-report=xml
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost/test_db
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: docker build -t my-app:${{ github.sha }} .
    
    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
    
    - name: Push to Docker Hub
      run: |
        docker tag my-app:${{ github.sha }} username/my-app:latest
        docker push username/my-app:latest
```

- Setup GitHub Actions workflow
- Automate testing and building
- Deploy to staging environment

**Assignment**
- Complete CI/CD pipeline:
  - CI Pipeline:
    - Trigger on push and PR
    - Run linting (flake8/black)
    - Run tests with coverage
    - Build Docker image
    - Security scanning (optional: Trivy)
  
  - CD Pipeline:
    - Push Docker image to Docker Hub/ECR
    - Deploy to EC2 instance
    - Health check after deployment
    - Rollback on failure
  
  - Environments:
    - Staging (auto-deploy on develop branch)
    - Production (manual approval or main branch)
  
  - Documentation:
    - Pipeline architecture
    - Deployment process
    - Rollback procedure
    - Monitoring setup

**Explore**
- GitLab CI/CD
- Jenkins
- ArgoCD for Kubernetes
- Terraform for infrastructure as code
- Monitoring with Prometheus/Grafana

**Interview Questions**
- What is CI/CD and why is it important?
- Explain a typical CI/CD pipeline
- How to handle secrets in CI/CD?
- Deployment strategies: blue-green vs rolling?
- How to rollback a failed deployment?
- GitHub Actions vs Jenkins comparison?

---

## 🔴 AI, ML & LLMs (Days 33–35)

---

### **Day 33 — Machine Learning Basics with scikit-learn**

**Concepts**

- **Machine Learning Overview**
  - Supervised vs unsupervised vs reinforcement learning
  - Classification vs regression
  - Training, validation, test sets
  - Overfitting and underfitting
  - Model evaluation metrics
  
- **Data Preprocessing**
  - Feature scaling (StandardScaler, MinMaxScaler)
  - Handling missing values
  - Encoding categorical variables
  - Train-test split
  
- **scikit-learn Basics**
  - Estimator API (fit, predict)
  - Pipeline for workflow
  - Cross-validation
  - Grid search for hyperparameters
  
- **Common Algorithms**
  - Linear Regression
  - Logistic Regression
  - Decision Trees
  - Random Forest
  - K-Nearest Neighbors
  
- **Model Evaluation**
  - Accuracy, precision, recall, F1-score
  - Confusion matrix
  - ROC curve and AUC
  - Mean Squared Error (MSE) for regression

**Exercise**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

- Train classification model
- Train regression model
- Evaluate and compare models

**Assignment**
- ML model development:
  - Dataset: Choose from sklearn.datasets or kaggle
  - Tasks:
    - Data exploration (pandas, matplotlib)
    - Preprocessing pipeline
    - Train multiple models
    - Compare performance
    - Hyperparameter tuning
    - Save best model (joblib/pickle)
  - API integration:
    - Create FastAPI endpoint for predictions
    - Load trained model
    - Accept input, return prediction
    - Input validation with Pydantic
  - Documentation:
    - Model selection rationale
    - Performance metrics
    - API usage examples

**Explore**
- Feature engineering
- Ensemble methods
- Model interpretability (SHAP)
- MLflow for experiment tracking

**Interview Questions**
- Explain overfitting and how to prevent it
- What is cross-validation?
- Precision vs recall: when to optimize for which?
- How to handle imbalanced datasets?
- Explain random forest algorithm
- How to deploy ML models in production?

---

### **Day 34 — Large Language Models & Transformers**

**Concepts**

- **LLM Fundamentals**
  - What are Large Language Models
  - Transformer architecture (high-level)
  - Pre-training and fine-tuning
  - Prompt engineering basics
  - Token limits and context windows
  
- **Hugging Face Ecosystem**
  - Transformers library
  - Model Hub
  - Pipeline API for quick inference
  - AutoModel and AutoTokenizer
  - Popular models (BERT, GPT, T5)
  
- **Text Generation**
  - Completion vs chat models
  - Temperature and sampling parameters
  - Top-k and top-p sampling
  - Controlling generation
  
- **Text Classification**
  - Sentiment analysis
  - Zero-shot classification
  - Named Entity Recognition
  
- **API-based LLMs**
  - OpenAI API
  - Anthropic Claude API
  - API keys and authentication
  - Rate limiting
  - Cost considerations

**Exercise**
```python
from transformers import pipeline

# Sentiment analysis
classifier = pipeline("sentiment-analysis")
result = classifier("I love this product!")
print(result)

# Text generation
generator = pipeline("text-generation", model="gpt2")
result = generator("Once upon a time", max_length=50)
print(result[0]['generated_text'])

# Question answering
qa = pipeline("question-answering")
context = "Python is a programming language."
question = "What is Python?"
result = qa(question=question, context=context)
print(result)

# Using OpenAI API
import openai

openai.api_key = "your-key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain Python in one sentence"}
    ]
)
print(response.choices[0].message['content'])
```
