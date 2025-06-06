## 🆚 Differences Between Python 2 and Python 3

| Feature                  | Python 2                                   | Python 3                                   |
|--------------------------|--------------------------------------------|--------------------------------------------|
| **Release Year**         | 2000                                       | 2008                                       |
| **Print Statement**      | `print "Hello"` (statement)                 | `print("Hello")` (function)                 |
| **Integer Division**     | Dividing integers returns integer           | Dividing integers returns float             |
| **Unicode Support**      | ASCII by default                            | Unicode by default                          |
| **`range()` Function**   | Returns list                               | Returns iterator (more memory efficient)   |
| **Error Handling**       | `except Exception, e:` syntax               | `except Exception as e:` syntax             |
| **Input Function**       | `raw_input()` for string input              | `input()` for string input                   |
| **End of Life**          | Officially deprecated since 2020            | Current and actively maintained             |

---

## 🖨️ Python Output Function: `print()`

### Syntax:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- *objects: One or more objects to print, separated by commas
- sep: String inserted between objects (default is a space ' ')
- end: String appended after the last object (default is newline '\n')
- file: A file-like object (stream) where the output is sent (default is standard output)
- flush: Whether to forcibly flush the stream (default is False)

```python
# 🔤 String
print('Hey Geeks')  # Output: Hey Geeks

# 🔢 Numeric Types
print(10)           # Integer (int)
print(10.2)         # Floating-point number (float)
print(1 + 2j)       # Complex number (complex)

# ✅ Boolean Type
print(True)         # Boolean True
print(False)        # Boolean False

# ⛔ Special Type
print(None)         # NoneType represents no value

# ----------------------------------------

# 📚 Collection Data Types

# List - Ordered, Mutable, Allows Duplicates
print([10, 20, 30, 40])  

# Tuple - Ordered, Immutable, Allows Duplicates
print(("IND", "NZ", "AUS"))  

# Set - Unordered, No Duplicates
print({"blue", "yellow", "red", "blue"})  

# Dictionary - Key-Value Pairs, Unordered (as of Python 3.6+ maintains insertion order)
print({"name": "Kumar", "course": "Python", "fee": 10.23893})
```
### 🔍 Attributes Explained with Examples
| Attribute | Description                                       | Example                                                         | Output                      |
| --------- | ------------------------------------------------- | --------------------------------------------------------------- | --------------------------- |
| `sep`     | Separator between multiple objects                | `print("apple", "banana", sep=", ")`                            | `apple, banana`             |
| `end`     | String appended at the end of print output        | `print("Hello", end="!")`                                       | `Hello!`                    |
| `file`    | Output destination (e.g., file instead of screen) | `python with open("out.txt", "w") as f: print("Hello", file=f)` | Writes "Hello" to `out.txt` |
| `flush`   | Forces flushing of the output buffer              | `print("Hello", flush=True)`                                    | Immediately outputs "Hello" |

### 💡 More Examples
```python 
# Default print
print("Hello", "World")  
# Output: Hello World

# Using sep
print("Python", "Java", "C++", sep=" | ")  
# Output: Python | Java | C++

# Using end
print("Hello", end="...")
print("World")  
# Output: Hello...World

# Writing to a file
print("Hey Hi Everyone Welcome to Python Session",file= open("welcome.txt",mode="a"))  #append mode)

# Flushing output
import time
print("Loading...", end="", flush=True)
time.sleep(2)
print("Done")

```

## Try These 
```python 

# Q1
print("Hello", "World", sep='-', end='***')
print("Python")

# Q2
print("A", "B", "C", sep='*', end='@')
print("D", "E", sep='-')

# Q3
print("Python", end='')
print("Rocks", end='!')
print("Yes")

# Q4
print("1", "2", "3", sep='', end='-')
print("4", "5", sep='')

# Q5
print("A", end='-')
print("B", end='*')
print("C", end='@')

# Q6 
print("Hi Captain America")
print() 
print()
print("Welcome 20100")

# Q7 
var = print('Hi Azure AI') 
print(var)

# Q8
print(print('Hi ChatGPT'))

```

---
## 💬 Comments in Python

- Comments are **non-executable** lines in a program that are ignored by the interpreter. 
- They help developers understand code logic, improve readability, and allow temporary disabling of code.
- Any text starting with hash(#) in Python is a comment.


### 🔹 Types of Comments:

#### 1. **Single-line Comment**
- Begins with a `#`
- Useful for short explanations

```python
# This line prints a greeting
print("Hello, World!")
```

#### 2. Multi-line Comment / Docstring
- Enclosed in triple quotes: ''' ''' or """ """
- Often used for documentation or large explanations

```python 
'''
This program calculates the area
of a circle using radius input
'''
print("Circle Area Calculator")
```
> 🔔 Note: Technically, Python treats triple-quoted strings as string literals, not actual comments, unless used as docstrings.

### 🧠 When to Use:
| Type        | When to Use                             |
| ----------- | --------------------------------------- |
| Single-line | Quick inline notes, small blocks        |
| Multi-line  | Documentation, large block descriptions |


---

## 📦 Variables in Python
- Variables are named storage locations that hold data values during program execution.
- A variable refers to a memory address in which data is stored

**🧠 Why Do We Need Them?**
- Store values that can change
- Improve code readability and manageability
- Reuse values without hardcoding

**💾 Where Are They Stored?**
- In RAM (main memory)
- Python stores references to the memory address of the value (everything in Python is an object)

### 📏 Rules for Defining Variables:
- Must start with a letter (A-Z, a-z) or underscore (_)
- Cannot start with a digit (0-9)
- Can contain letters, digits, and underscores
- Cannot use Python keywords
- Case-sensitive (Name ≠ name)
- No special characters (@, $, %, - not allowed)

> A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended

**✅ Valid Variable Names:**
```python 

firstname = "John"
lastname = "Doe"
age = 30
country = "USA"
city = "New York"

first_name = "Alice"
last_name = "Smith"
capital_city = "Paris"

_if = True  # Using underscore to avoid keyword conflict

year_2021 = 2021
year2021 = 2021
current_year_2021 = 2021
birth_year = 1995

num1 = 10
num2 = 20

# Output example
print(f"{first_name} {last_name} lives in {capital_city}, {country}.")
print(f"Born in {birth_year}, current age is {age}.")
```

**❌ Invalid Variable Names:**
```python 
first-name = "John"     # Hyphen is not allowed
first@name = "Alice"    # Special characters like @ not allowed
first$name = "Sam"      # $ symbol is not allowed
num-1 = 5               # Hyphen not allowed; treated as subtraction
1num = 10               # Cannot start with a digit
if = "condition"        # 'if' is a reserved keyword
True = "yes"            # 'True' is a boolean keyword, not a variable name

```
### ☕ Java vs Python: Variable Declaration
| Feature           | Python                        | Java                             |
| ----------------- | ----------------------------- | -------------------------------- |
| Declaration       | `x = 5`                       | `int x = 5;`                     |
| Type System       | Dynamically Typed             | Statically Typed                 |
| Type Required?    | ❌ No                          | ✅ Yes                            |
| Semicolons Needed | ❌ No                          | ✅ Yes                            |
| Memory Model      | Reference to Object (dynamic) | Strongly typed memory allocation |

> 📝 Python is easier for beginners because it reduces verbosity and automates type inference.


---
## 🗝️ Python Keywords
- Keywords are reserved words in Python that have predefined meanings and are used to define the syntax and structure of the language.

*🧠 Why Are They Important?**
- Cannot be used as variable names or identifiers
- Ensure that the language syntax is not broken

**🧾 Common Python Keywords:**
```python 
False, True, None, and, or, not, if, elif, else,
for, while, break, continue, return, def, class,
import, from, as, global, nonlocal, try, except,
finally, with, lambda, yield, assert, pass, del, raise
```

**To get all keywords:**
```python 
import keyword
print(keyword.kwlist)
```

---

## 🎨 Styling Conventions in Python
- Python follows PEP 8 – the official style guide for Python code.

**✨ Naming Styles:**
| Style          | Example         | Usage                             |
| -------------- | --------------- | --------------------------------- |
| `snake_case`   | `user_name`     | ✅ Functions, variables (Pythonic) |
| `PascalCase`   | `UserProfile`   | ✅ Class names                     |
| `camelCase`    | `userName`      | ❌ Avoid in Python, used in Java   |
| `UPPER_CASE`   | `MAX_LIMIT`     | ✅ Constants                       |
| `_private_var` | `_hidden_value` | ✅ Private/internal use            |

**🧠 When to Use Which:**
- snake_case → for variables and functions
- PascalCase → for class names
- UPPERCASE → for constants
- Leading underscore (_) → for private/internal use
- Double underscores (__) → name mangling for class-private members

---

## 💻 What Are Data Types?

In Python, **data types** define the type of value a variable can hold. 
- Python is **dynamically typed**, which means you don't need to declare the type explicitly—it is inferred at runtime.

---

## 📦 Built-in Data Types in Python

Python has the following built-in data types:

1. **Numbers**
2. **Strings**
3. **Booleans**
4. **Complex Numbers**
5. **Collections** (List, Tuple, Set, Dictionary)

---

## 🔢 1. Number Types

### ➤ Integer (`int`)

- Whole numbers (positive or negative) without decimals.
```python
age = 25
year = 2024
```
- In Python, you can represent integers in binary, octal, and hexadecimal formats using specific prefixes:

**🧮 Binary, Octal, Hexadecimal in Integers**

| Number System | Prefix     | Usage in Code          | Conversion Function | Example                      |
|---------------|------------|-----------------------|---------------------|------------------------------|
| **Binary**    | `0b` or `0B` | Used to define binary literals | `bin()`             | `num = 0b1010` (decimal 10)  |
| **Octal**     | `0o` or `0O` | Used to define octal literals  | `oct()`             | `num = 0o12` (decimal 10)    |
| **Hexadecimal** | `0x` or `0X` | Used to define hex literals    | `hex()`             | `num = 0xA` (decimal 10)     |

```python 
# Binary
binary_num = 0b1010
print("Binary:", binary_num)  # Output: 10

# Octal
octal_num = 0o12
print("Octal:", octal_num)    # Output: 10

# Hexadecimal
hex_num = 0xA
print("Hexadecimal:", hex_num)  # Output: 10
```

```python 
# bin() examples 
#  Convert a positive integer to binary
num = 10
binary_str = bin(num)
print(binary_str)  # Output: '0b1010'

# Convert zero to binary
num_zero = 0
print(bin(num_zero))  # Output: '0b0'

# Convert a negative integer to binary
num_neg = -15
print(bin(num_neg))   # Output: '-0b1111'

# Using bin() inside a print statement directly
print(bin(255))      # Output: '0b11111111'


# oct() examples

# Convert a positive integer to octal
num = 10
oct_str = oct(num)
print(oct_str)  # Output: '0o12'

# Convert zero to octal
num_zero = 0
print(oct(num_zero))  # Output: '0o0'

# Convert a negative integer to octal
num_neg = -15
print(oct(num_neg))   # Output: '-0o17'

# Using oct() directly inside print
print(oct(255))       # Output: '0o377'


# hex() examples

# Convert a positive integer to hexadecimal
num = 10
hex_str = hex(num)
print(hex_str)  # Output: '0xa'

# Convert zero to hexadecimal
num_zero = 0
print(hex(num_zero))  # Output: '0x0'

# Convert a negative integer to hexadecimal
num_neg = -15
print(hex(num_neg))   # Output: '-0xf'

# Using hex() directly inside print
print(hex(255))       # Output: '0xff'

```
- Prefixes (0b, 0o, 0x) tell Python the base of the integer literal.
- Functions bin(), oct(), and hex() convert an integer to a string in binary, octal, or hexadecimal format respectively.

### ➤ Float (float)
- Decimal or floating-point numbers.
```python 
price = 99.99
temperature = -12.5
```
**e means "times ten raised to the power of".**

```python
# Using 'e' in float to represent numbers in scientific notation

# 1.23 × 10^3  (which is 1230.0)
num1 = 1.23e3
print(num1)   # Output: 1230.0

# 4.56 × 10^-4 (which is 0.000456)
num2 = 4.56e-4
print(num2)   # Output: 0.000456

# Another example: 7.89 × 10^0 = 7.89
num3 = 7.89e0
print(num3)   # Output: 7.89
```

### ➤ Complex (complex)
- Numbers with a real and imaginary part.
- Used in scientific and engineering applications.
- real number is optional and imaginary part is mandatory

```python
z = 2 + 3j
print(z.real)  # 2.0
print(z.imag)  # 3.0

a = 7j # 0+7j
print(a.real) # 0.0
print(a.imag) # 7.0

x = 4 + 5j
y = complex(2, 3)

```

---
## 🔤 2. String (str)
- A sequence of characters(letters , symbols,numbers) enclosed in quotes.
- Strings in Python can be represented using three types of quotes:
    - Single quotes — e.g., 'a', 'hello'
    - Double quotes — e.g., "Hello World"
    - Triple quotes — used for multi-line strings or docstrings, e.g., '''This is a multi-line string'''

```python 
name = "Alice"
message = 'Welcome to Python!'

# It's a good movie

# print('It's a good movie') # Error 

print("It's a good movie")
print('It\'s a good movie')

# python is "oops" lang

print("python is \"oops\" language")
print(""""python is "oops" language""")


```

- Indexed
- Immutable

```python
print(name[0])  # Output: A
```

---

## 🔁 3. Boolean (bool)
- Represents one of two values: True or False.

```python
is_active = True
is_logged_in = False
```
Useful in: Conditions, Loops, Comparisons

---
## 📚 5. Collections
**📋 List (list)**
- Ordered, indexed, and mutable collection of items.
```python 
fruits = ["apple", "banana", "cherry"]
fruits[0] = "mango"
```
> Real-time use: Shopping cart items, user tags, search history.

**📦 Tuple (tuple)**
- Ordered, indexed, and immutable collection.
```python
dimensions = (1920, 1080)
```
> Use when data should not be changed: screen sizes, coordinates, configuration values.

**🧮 Set (set)**
- Unordered, non-indexed, and unique elements.
```python
colors = {"red", "blue", "green", "red"}
print(colors)  # {'blue', 'green', 'red'}
```
> Great for removing duplicates, finding unique entries.

**📖 Dictionary (dict)**
- Ordered, key-value pairs, and mutable.

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # John
```

- ✅ Key-based indexing
- ✅ Mutable
> Used in APIs, configs, data records, user profiles.

### 🧮 Indexed vs Non-Indexed Types
| Data Type | Indexed?   | Mutable? | Ordered? |
| --------- | ---------- | -------- | -------- |
| `str`     | ✅          | ❌        | ✅        |
| `list`    | ✅          | ✅        | ✅        |
| `tuple`   | ✅          | ❌        | ✅        |
| `set`     | ❌          | ✅        | ❌        |
| `dict`    | ✅ (by key) | ✅        | ✅ (3.7+) |


**📝 Real-Time Examples**
- List: Shopping cart → ["item1", "item2", "item3"]
- Tuple: Coordinate system → (x, y)
- Set: Unique visitors → {user1, user2, user3}
- Dictionary: User profile → {"username": "john", "email": "john@example.com"}

---

## ⌨️ Input Function

- The `input()` function in Python is used to take input from the user during program execution. 
- It reads a line of text entered by the user and returns it as a **string**.

**Syntax**

```python
variable = input("Prompt")
```

### 🧰 Usage with Different Data Types
- Since input() always returns a string, you often need to convert the input to other data types using type casting functions like int(), float(), or bool().

```python
# Taking string input (default behavior)
name = input("Enter your name: ")
print("Hello,", name)

# Taking integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Taking float input
price = float(input("Enter the price: "))
print("Price entered:", price)

# Taking boolean input (requires custom handling)
response = input("Are you a student? (yes/no): ").lower()
is_student = True if response == 'yes' else False
print("Student status:", is_student)
```
### Try These 
```python

# Q1 
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

print(num1 + num2)

# Q2
x = input("Enter a number: ")
print(x + 5)

# Q3
print('10' + 10) # str + int
print(5 + '4') # int + str

# Q4 - What will this print if the user types 10.5?
num = int(input("Enter a number: "))
print(num)

# Q5 
How to take multiple inputs in one line and store them as integers in a list?

# Q6 
flag = bool(input("Enter True or False: "))
print(flag)

# Q7 
How do you handle blank input from the user (i.e., user just presses Enter)?
```

---

## 🔎 Built-in Functions in Python

<img src="https://i.sstatic.net/O0eOZ.png" alt="drawing" width="800"/>

### 1.a `type()`
- Returns the **type** of an object.
- Useful to check the data type of a variable or value.

```python
print(type(10))         # <class 'int'>
print(type("Hello"))    # <class 'str'>
```
### 1.b  `id()`
- It helps to check if two variables reference the same object.
- The returned value is typically the memory address where the object is stored (implementation-dependent).
```python
id(object)

a = 10
b = 10
print(id(a))  # e.g., 140704045672464
print(id(b))  # same as id(a) because of interning small integers

c = [1, 2, 3]
d = [1, 2, 3]
print(id(c))  # different IDs because different objects
print(id(d))
```

### 2. dir()
- Lists all attributes and methods of an object.
- Helpful to explore what you can do with an object.
```python
print(dir([]))  # Lists methods available for list objects
```

### 3. help()
- Displays the documentation/help for a module, function, class, or object.
- Great for understanding usage and parameters.
```python
help(str)  # Shows help for string type and its methods
```

### 4. ord()
- Returns the Unicode code point (integer) of a given character.
```python
print(ord('A'))  # Output: 65
print(ord('z'))  # Output: 122
```

### 5. chr()
Converts an integer Unicode code point back to its character.
```python
print(chr(65))   # Output: 'A'
print(chr(122))  # Output: 'z'
```

## 🔢 Data Type Conversion Functions and Usage
**1. int()**
- Converts a value to an integer.
- Can convert strings representing whole numbers or floats (by truncation).
```python
print(int("123"))     # 123
print(int(12.99))     # 12

print(int("107A"))  # Error
```

**2. float()**
- Converts a value to a floating-point number.
```python
print(float("12.34"))  # 12.34
print(float(10))       # 10.0

print(float("107.2A")) # Error
```

**3. str()**
Converts any value to a string.
```python
print(str(100))       # '100'
print(str(12.34))     # '12.34'
```

**4. complex()**
Creates a complex number from two numbers or strings.
```python
print(complex(2, 3))          # (2+3j)
print(complex("4+5j"))        # (4+5j)
```

**5. bool()**
- Converts a value to Boolean (True or False).
- Values like 0, "", None, [] convert to False. Others convert to True.
```python
print(bool(0))        # False
print(bool(123))      # True
print(bool(""))       # False
print(bool("hello"))  # True
```

**6. list()**
- Converts iterable to a list (ordered, mutable).
```python
print(list("hello"))    # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))  # [1, 2, 3]
```
**7. tuple()**
- Converts iterable to a tuple (ordered, immutable).
```python
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple("abc"))      # ('a', 'b', 'c')
```
**8. set()**
- Converts iterable to a set (unordered, unique elements).
```python
print(set([1, 2, 2, 3]))  # {1, 2, 3}
print(set("hello"))        # {'h', 'e', 'l', 'o'}
```

**9.dict()**
- Creates a dictionary (key-value pairs).
- Can convert a list of tuples (pairs) to dictionary.
```python
print(dict([("name", "Alice"), ("age", 25)]))  # {'name': 'Alice', 'age': 25}
```


### Hands-On 

**Q1**
- Declare 5 real-world variables by taking input from the keyboard,then print each variable’s value, its data type, and its memory ID.

**Q2**
-  Use dir() to list all the methods available for a string variable "hello".

**Q3**
- Create a dictionary from a list of key-value pairs: [("name", "Alice"), ("age", 30), ("city", "NY")] using dict()
