# 🐍 Python Modules
- A **module** is a Python file (`.py`) containing definitions, functions, classes, or variables that you can **reuse** in other programs.
- In real-world development, we don’t write everything from scratch. We use predefined modules to speed up development.
- Modules contain ready-made functionality we can import when needed. This approach saves time, makes code more organized, and easier to maintain.

### ✅ Why Use Modules?
- Promotes **code reuse** and **modularity**
- Helps **organize** large programs
- Avoids **rewriting common logic**
- Python comes with many **built-in** modules

### 📍 Where to Use?
- For any **repeated logic** or **utility functions**
- For **external tools** like network requests, databases, etc.
- In **larger projects** where separating functionality makes maintenance easier

--- 

### Four Ways to Import Modules in Python**

**1. Basic Import (Module Name Only)**
- Import the entire module
- Access functions using module_name.function()
```python
import math
math.gcd(12, 18)
```
**2. Import with an Alias**
- Useful for long module names
- Access functions using the alias

```python
import math as mt
mt.gcd(12, 18)
```

**3. Import Specific Functions**
- Imports only the needed functions
- Saves memory and keeps code clean
- No need to prefix with module name

```python 
from math import gcd, pi
gcd(12, 18)
```

**4. Wildcard Import `(*)`**
- Imports everything from the module
- Not recommended for large modules (can lead to naming conflicts)
```python
from math import *
gcd(12, 18)
```

---

## 🧰 Common Built-In / Standard Library Modules

### 1. `os` – Operating System Interface
- Interact with the file system
- Run shell commands
- Work with paths, directories, environment variables

```python
import os

print("Current Directory:", os.getcwd())

print("\nFiles & Folders:")
for item in os.listdir():
    print("-", item)

# Create a new directory
if not os.path.exists("logs"):
    os.mkdir("logs")
    print("\n'logs' folder created!")

# Rename a file (if it exists)
if os.path.exists("old.txt"):
    os.rename("old.txt", "new.txt")
    print("\nFile renamed from 'old.txt' to 'new.txt'")

# Show file size
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"\nSize of data.txt: {size} bytes")

```
---

### **2. `sys` – System-Specific Parameters**
- Access system-specific variables and functions
- Useful for command-line arguments and exiting programs

```python
import sys
import math

# 1. sys.argv - Command-line arguments
print("Command-line arguments (sys.argv):", sys.argv)

# 2. sys.exit - Uncomment to exit the program early
# sys.exit("Exiting program.")

# 3. sys.path - Module search paths
print("Module search paths (sys.path):", sys.path[:2])  # Show only first 2 for brevity

# 4. sys.platform - Detect OS platform
print("Platform (sys.platform):", sys.platform)

# 5. sys.version / sys.version_info - Python version
print("Python version (sys.version):", sys.version)
print("Version info (sys.version_info):", sys.version_info)

# 6. sys.stdin, sys.stdout, sys.stderr - Standard I/O streams
sys.stdout.write("Writing to standard output using sys.stdout.write\n")

# 7. sys.getsizeof - Size of an object in bytes
sample_string = "Hello, sys!"
print(f"Size of '{sample_string}' (sys.getsizeof):", sys.getsizeof(sample_string), "bytes")

# 8. sys.modules - List loaded modules
print("Is 'math' module loaded? ('math' in sys.modules):", 'math' in sys.modules)

# 9. sys.maxsize - Maximum size of a Python int
print("Maximum integer size (sys.maxsize):", sys.maxsize)

# 10. sys.exc_info - Exception information
try:
    1 / 0
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Exception info (sys.exc_info):", exc_type, exc_value)

# NOTE: To test sys.exit, uncomment the line above.
# Be aware that calling sys.exit will stop the script early.

```
---

### **3. `array` – Space-Efficient Arrays**
- The array module provides an array data structure that is more memory-efficient than regular Python lists when storing large amounts of numeric data of the same type.
- All elements must be of the same data type (unlike Python lists)
- Faster for numerical processing compared to generic lists
- Uses single-character codes to define element type (e.g., 'i' for integers)

**Common Type Codes**
| Type Code | C Type         | Python Type | Size (bytes) |
| --------- | -------------- | ----------- | ------------ |
| `'b'`     | signed char    | int         | 1            |
| `'B'`     | unsigned char  | int         | 1            |
| `'h'`     | signed short   | int         | 2            |
| `'H'`     | unsigned short | int         | 2            |
| `'i'`     | signed int     | int         | 4            |
| `'I'`     | unsigned int   | int         | 4            |
| `'f'`     | float          | float       | 4            |
| `'d'`     | double float   | float       | 8            |


```python
import array

a = array.array('i', [1, 2, 3, 4])
print(a[0])    # Access element
```

```python
import array

# 1. Create an array of integers
arr = array.array('i', [10, 20, 30, 40])
print("Original array:", arr)

# 2. Append a new item
arr.append(50)
print("After append:", arr)

# 3. Insert an element at index 1
arr.insert(1, 15)
print("After insert at index 1:", arr)

# 4. Remove an item
arr.remove(30)
print("After removing 30:", arr)

# 5. Pop the last item
last_item = arr.pop()
print("Popped item:", last_item)
print("Array after pop:", arr)

# 6. Access by index
print("Element at index 2:", arr[2])

# 7. Convert array to list
as_list = arr.tolist()
print("Converted to list:", as_list)

# 8. Slice the array
print("Sliced array (index 1 to 3):", arr[1:4])

# 9. Iterate through the array
print("All elements:")
for item in arr:
    print(item)
```

**Bonus: Use array for Binary I/O**
```python
# Save array to a binary file
with open("data.bin", "wb") as f:
    arr.tofile(f)

# Load array from binary file
new_arr = array.array('i')  # Must use the same type code
with open("data.bin", "rb") as f:
    new_arr.fromfile(f, 5)  # Read 5 elements
print("Loaded from file:", new_arr)
```

---

### **4. `random` – Generate Random Data**
- The random module provides functions to generate pseudo-random numbers and randomly select or shuffle data
- Useful for games, testing, simulations

```python
import random

# 1. random.random() – Random float between 0.0 and 1.0
print("1. Random float (0.0 to 1.0):", random.random())

# 2. random.randint(a, b) – Random integer in range [a, b]
print("2. Random integer (10 to 20):", random.randint(10, 20))

# 3. random.uniform(a, b) – Random float in range [a, b]
print("3. Random float (1.5 to 6.5):", random.uniform(1.5, 6.5))

# 4. random.choice(seq) – Pick a single random item
colors = ['red', 'green', 'blue', 'yellow']
print("4. Random color choice:", random.choice(colors))

# 5. random.choices(population, weights=None, k=1) – Multiple choices (with replacement)
lottery_numbers = [1, 2, 3, 4, 5, 6]
print("5. Weighted choices (3 picks):", random.choices(lottery_numbers, weights=[1, 2, 1, 1, 1, 1], k=3))

# 6. random.sample(population, k) – Unique random sample (without replacement)
print("6. Random sample (3 unique numbers):", random.sample(lottery_numbers, 3))

# 7. random.shuffle(seq) – Shuffle a list in place
deck = ['A', 'K', 'Q', 'J', '10']
random.shuffle(deck)
print("7. Shuffled deck:", deck)

# 8. random.seed(a) – Set seed for reproducible results
random.seed(123)
print("8. Seeded random number (123):", random.random())

# 9. Reproducibility demo: same seed, same result
random.seed(123)
print("9. Same seed again, same result:", random.random())
```

- 🎮 Game Mechanics
```python
# Roll a dice
dice_roll = random.randint(1, 6)
print("Dice rolled:", dice_roll)
```

- 🔍 Simulations
```python 
# Simulate coin tosses
results = [random.choice(['Heads', 'Tails']) for _ in range(10)]
print("Coin toss simulation:", results)
```

- 🧪 Unit Testing with Random Data
```python
# Generate random test IDs
test_ids = ['ID' + str(random.randint(1000, 9999)) for _ in range(5)]
print("Generated test IDs:", test_ids)
```

- Weighted Lottery
```python
# 70% chance to win "Apple", 30% chance to win "Banana"
print(random.choices(['Apple', 'Banana'], weights=[70, 30], k=1))
```

---
### **5. `sqlite3` – Lightweight Embedded Database**
- The sqlite3 module lets you use SQLite, a lightweight, built-in SQL database engine. 
- It's excellent for small/local apps, prototypes, and data storage.
- No server required, and the entire database is stored in a single file.

```python

import sqlite3

# 1. Connect to (or create) a local SQLite database file
conn = sqlite3.connect("mydata.db")  # Use ":memory:" for in-RAM DB
cursor = conn.cursor()

# 2. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# 3. Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
conn.commit()

# 4. Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("All Users:")
for row in rows:
    print(row)

# 5. Update data
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()

# 6. Delete data
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()

# 7. Query again
cursor.execute("SELECT * FROM users")
print("\nAfter update/delete:")
for row in cursor.fetchall():
    print(row)

# 8. Close the connection
conn.close()
```
--- 

### **6. `hashlib` – Secure Hash Algorithms**
- hashlib provides a common interface to many secure hash and message digest algorithms. It’s part of Python’s standard library.
- Used for encryption, password hashing, file integrity

**Common Use Cases:**
| Use Case            | Example                                 |
| ------------------- | --------------------------------------- |
| Password hashing    | Store and compare hashed passwords      |
| File verification   | Check if a file was modified/corrupted  |
| Data fingerprinting | Generate consistent unique IDs          |
| Security checks     | Generate or verify cryptographic hashes |

**🔑 Supported Hash Algorithms**
| Algorithm            | Hash Length                         | Description                            |
| -------------------- | ----------------------------------- | -------------------------------------- |
| `md5`                | 128 bits                            | Fast but **not secure** for modern use |
| `sha1`               | 160 bits                            | Also outdated; use SHA-2 instead       |
| `sha256`             | 256 bits                            | Secure and widely used                 |
| `sha512`             | 512 bits                            | More secure, but longer hashes         |
| `blake2b`, `blake2s` | Fast and secure alternatives to SHA |                                        |

```python
# Hash Strings
import hashlib

# 1. Original data
text = "hello123"
encoded = text.encode()  # Convert string to bytes

# 2. Generate various hashes
md5_hash = hashlib.md5(encoded).hexdigest()
sha1_hash = hashlib.sha1(encoded).hexdigest()
sha256_hash = hashlib.sha256(encoded).hexdigest()
sha512_hash = hashlib.sha512(encoded).hexdigest()

# 3. Print the hashes
print("MD5    :", md5_hash)
print("SHA1   :", sha1_hash)
print("SHA256 :", sha256_hash)
print("SHA512 :", sha512_hash)
```

```python
# Hash a File (e.g. for file integrity)
def get_file_hash(filepath, algo='sha256'):
    hasher = hashlib.new(algo)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


print(get_file_hash("sample.py"))

```

```python

import hashlib
import os

# 1. Generate a random salt
salt = os.urandom(16)

# 2. Hash the password using PBKDF2
password = b"my_secret_password"
hashed_pw = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

# 3. Store (salt + hash) securely
print("Salt:", salt.hex())
print("Hashed password:", hashed_pw.hex())

# 4. verify 
# Pretend this is the user entering their password:
user_input = b"my_secret_password"  

# Hash the user input using the same salt and iterations
input_hash = hashlib.pbkdf2_hmac('sha256', user_input, salt, 100000)

# Check if it matches the stored hash
if input_hash == hashed_pw:
    print("✅ Password is correct")
else:
    print("❌ Password is incorrect")
```

---
###  7. `pathlib` – Modern Path Handling
- pathlib provides the Path class for representing and manipulating file and directory paths in an object-oriented way. 
- It works across all operating systems (Windows, macOS, Linux).
-  Included in Python 3.4+
- Safer than os.path , Less error-prone and easier to read
```python
from pathlib import Path

# 1. Create a Path object (relative)
file_path = Path("demo_folder") / "example.txt"

# 2. Create a directory (if it doesn't exist)
file_path.parent.mkdir(exist_ok=True)
print(f"Created folder: {file_path.parent}")

# 3. Write text to the file
file_path.write_text("Hello from pathlib!")
print(f"Written to file: {file_path}")

# 4. Read the file content
content = file_path.read_text()
print("File content:", content)

# 5. Check if the file and folder exist
print("File exists:", file_path.exists())
print("Is file:", file_path.is_file())
print("Is directory:", file_path.parent.is_dir())

# 6. Show file parts
print("File name:", file_path.name)
print("File suffix (extension):", file_path.suffix)
print("File stem:", file_path.stem)
print("Parent directory:", file_path.parent.resolve())

# 7. File metadata
print("File size:", file_path.stat().st_size, "bytes")

# 8. List all .txt files in the folder
print("\nText files in folder:")
for txt in file_path.parent.glob("*.txt"):
    print("-", txt.name)

# 9. Rename the file
new_file_path = file_path.with_name("renamed_example.txt")
file_path.rename(new_file_path)
print(f"\nFile renamed to: {new_file_path.name}")

# 10. Create another file and write something
extra_file = file_path.parent / "extra.txt"
extra_file.write_text("Another file.")
print("Created extra file.")

# 11. Recursively list all .txt files
print("\nAll .txt files (recursive):")
for txt in file_path.parent.rglob("*.txt"):
    print("-", txt.relative_to(file_path.parent))

# 12. Cleanup: Delete files and directory
extra_file.unlink()
new_file_path.unlink()
file_path.parent.rmdir()
print("\nCleanup complete.")

```
---
### 🔍 8. `regex` Regular Expressions
The re module allows you to use regular expressions in Python for:
- Pattern matching
- Searching and replacing
- Validating strings (e.g. emails, phone numbers)
- Splitting text by complex rules

**Common Functions in re**
| Function        | Description                         |
| --------------- | ----------------------------------- |
| `re.search()`   | Find first match anywhere in string |
| `re.match()`    | Match only from the beginning       |
| `re.findall()`  | Return all matches as a list        |
| `re.finditer()` | Return all matches as iterator      |
| `re.sub()`      | Replace patterns                    |
| `re.split()`    | Split string by regex               |
| `re.compile()`  | Compile regex for reuse             |


**Regex Patterns**
| Pattern   | Matches                      |                |        |
| --------- | ---------------------------- | -------------- | ------ |
| `\d`      | Any digit (0–9)              |                |        |
| `\w`      | Any alphanumeric + `_`       |                |        |
| `\s`      | Any whitespace               |                |        |
| `.`       | Any character except newline |                |        |
| `[abc]`   | a, b, or c                   |                |        |
| `[^abc]`  | NOT a, b, or c               |                |        |
| `a{3}`    | Exactly 3 a's                |                |        |
| `a+`      | One or more a's              |                |        |
| `a*`      | Zero or more a's             |                |        |
| `^` / `$` | Start / end of string        |                |        |
| \`        | \`                           | OR (e.g. \`cat | dog\`) |
|           |                              |                |        |

```python
import re

text = "My email is test@example.com and my phone is +1-800-555-1234."

# 1. Search for an email pattern
email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
if email_match:
    print("📧 Found email:", email_match.group())

# 2. Find all phone numbers
phones = re.findall(r"\+?\d[\d\-]{9,}", text)
print("📞 Found phone(s):", phones)

# 3. Replace email with [EMAIL]
masked_text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[EMAIL]", text)
print("🔒 Masked:", masked_text)

# 4. Split sentence by words (not just spaces)
words = re.split(r"\W+", text)
print("🪓 Split words:", words)

# 5. Validate input using match (must match entire string)
password = "P@ssw0rd123"
if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
    print("✅ Password is valid")
else:
    print("❌ Password is invalid")
```

- **Email Validator**
```python
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.fullmatch(pattern, email) is not None

print(is_valid_email("test@example.com"))  # True

```
- **Remove Extra Spaces**
```python
text = "This   has  too    many spaces"
cleaned = re.sub(r"\s+", " ", text)
print("Cleaned:", cleaned)

# Extract Hashtags from Text
text = "Loving the #Python #regex module!"
hashtags = re.findall(r"#\w+", text)
print("Hashtags:", hashtags)


```

---

### 📅 9. `datetime` – Dates and Times
- The datetime module provides classes for manipulating dates, times, timestamps, and durations. It's useful for:
    - Logging timestamps
    - Scheduling
    - Age calculations
    - Time differences (durations)
    - Formatting/parsing date strings

**Core Classes in datetime**
| Class       | Description                      |
| ----------- | -------------------------------- |
| `datetime`  | Combination of date and time     |
| `date`      | Date only (year, month, day)     |
| `time`      | Time only (hour, minute, etc.)   |
| `timedelta` | Duration between two dates/times |


```python
from datetime import datetime, date, time, timedelta

# 1. Get the current date and time
now = datetime.now()
print("1. Current datetime:", now)

# 2. Current date and time separately
print("2. Current date:", now.date())
print("3. Current time:", now.time())

# 4. Create specific date and time objects
d = date(2025, 1, 1)
t = time(12, 30, 45)
dt = datetime(2025, 1, 1, 12, 30, 45)
print("4. Custom date:", d)
print("5. Custom time:", t)
print("6. Custom datetime:", dt)

# 5. timedelta – working with durations
delta = timedelta(days=5, hours=3)
future = now + delta
past = now - delta
print("7. 5 days from now:", future)
print("8. 5 days ago:", past)

# 6. Difference between two dates/times
diff = future - past
print("9. Difference between future and past:", diff)
print("10. Total days:", diff.days)
print("11. Total seconds:", diff.total_seconds())

# 7. Formatting datetime to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("12. Formatted current datetime:", formatted)

# 8. Parsing string to datetime
dt_from_str = datetime.strptime("2025-01-01 12:30:45", "%Y-%m-%d %H:%M:%S")
print("13. Parsed datetime from string:", dt_from_str)

# 9. ISO format and parsing
print("14. ISO format:", now.isoformat())
parsed_iso = datetime.fromisoformat(now.isoformat())
print("15. Parsed from ISO:", parsed_iso)

# 10. Getting weekday
print("16. Weekday (0=Monday):", now.weekday())
print("17. Weekday name:", now.strftime("%A"))
```

**Useful strftime Format Codes**
| Code | Meaning         | Example  |
| ---- | --------------- | -------- |
| `%Y` | Year (4 digits) | 2025     |
| `%m` | Month (01–12)   | 05       |
| `%d` | Day (01–31)     | 31       |
| `%H` | Hour (00–23)    | 14       |
| `%M` | Minute          | 09       |
| `%S` | Second          | 45       |
| `%A` | Weekday name    | Saturday |




**Age Calculator**
```python
from datetime import date
birth_date = date(2000, 6, 1)
today = date.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print("Age:", age)
```

**Countdown to a Date**
```python
event_date = datetime(2025, 12, 31)
days_left = event_date - datetime.now()
print("Days until event:", days_left.days)
```

**Timestamp for Logging**
```python
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Process started.")
```

---

### 🌐 10. `requests` – HTTP for Humans
- requests is a third-party Python library used to send HTTP/HTTPS requests in a simple, readable way.
- Not built-in. Install via: `pip install requests`

**Common Use Cases**
| Use Case               | Example                             |
| ---------------------- | ----------------------------------- |
| Call REST APIs         | GET/POST requests                   |
| Web scraping           | Fetch HTML content                  |
| Submit forms           | POST with data                      |
| Download files         | Save images, PDFs, JSON, etc.       |
| Handle headers/cookies | Work with authentication and tokens |


```python
import requests

# 1. Simple GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("1. Status Code:", response.status_code)
print("2. JSON Response:", response.json())

# 2. Make a POST request with data
post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
print("\n3. POST response:", post_response.json())

# 3. Custom headers
headers = {
    "User-Agent": "my-app/0.0.1"
}
res = requests.get("https://httpbin.org/headers", headers=headers)
print("\n4. Custom headers:", res.json())

# 4. Query parameters
params = {'q': 'python', 'limit': 2}
res = requests.get("https://httpbin.org/get", params=params)
print("\n5. URL with query params:", res.url)
print("6. Response with params:", res.json())

# 5. Handle timeouts and exceptions
try:
    res = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.exceptions.Timeout:
    print("\n7. Request timed out!")

# 6. Downloading a file
image_url = "https://via.placeholder.com/150"
img_res = requests.get(image_url)
with open("downloaded_image.png", "wb") as f:
    f.write(img_res.content)
print("\n8. Image downloaded: downloaded_image.png")

# 7. Status code checking
if response.ok:
    print("9. The GET request was successful.")
else:
    print("9. Request failed with status:", response.status_code)
```

**📄 Response Object**
| Property       | Description                   |
| -------------- | ----------------------------- |
| `.status_code` | HTTP status (e.g. 200, 404)   |
| `.text`        | Response as plain text (HTML) |
| `.json()`      | Parses JSON into Python dict  |
| `.content`     | Raw bytes (for files/images)  |
| `.url`         | Final URL after redirects     |
| `.headers`     | Response headers (dict)       |



**Authenticated Requests**
```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('username', 'token'))
print("Authenticated user data:", response.json())

```

---

### 🧰 11. `collections` – Advanced Data Structures
- collections is a built-in Python module that provides alternative container datatypes designed for specific use cases, such as counting, ordering, fast insertion/removal, and readable tuple-like objects.

**✅ Key Data Structures in collections**
| Class         | Description                                           |
| ------------- | ----------------------------------------------------- |
| `namedtuple`  | Tuple with named fields (like a lightweight object)   |
| `deque`       | Double-ended queue (fast appends/pops from both ends) |
| `Counter`     | Counts frequency of items                             |
| `defaultdict` | Dict with default values                              |
| `OrderedDict` | (In Python <3.7) Dict that remembers insertion order  |
| `ChainMap`    | Combines multiple dicts into one view                 |


```python
from collections import namedtuple, deque, Counter, defaultdict, ChainMap

# 1. namedtuple – Tuple with named fields
Person = namedtuple("Person", ["name", "age"])
p1 = Person("Alice", 30)
print("1. namedtuple:", p1.name, p1.age)

# 2. deque – Fast appends and pops from both ends
dq = deque(["a", "b", "c"])
dq.append("d")
dq.appendleft("z")
dq.pop()
dq.popleft()
print("2. deque after operations:", dq)

# 3. Counter – Count frequencies
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print("3. Counter (word frequencies):", word_count)
print("Most common:", word_count.most_common(2))

# 4. defaultdict – Automatically handles missing keys
dd = defaultdict(int)  # Default value is 0
dd["apples"] += 1
dd["oranges"] += 2
print("4. defaultdict:", dict(dd))

# 5. ChainMap – Combine multiple dicts into one view
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined = ChainMap(dict1, dict2)
print("5. ChainMap view:", dict(combined))
print("Value for 'b':", combined["b"])  # From dict1, takes first occurrence
```

**🔹 namedtuple**
- Immutable and readable like a class but faster.
- Ideal for structured, lightweight records.
```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
pt = Point(10, 20)
print(pt.x, pt.y)
```

**🔹 deque**
- O(1) complexity for both ends.
- Perfect for implementing queues and stacks.

```python
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
```

**🔹 Counter**
- Automatically counts items in a list, string, or iterable.
- Has helpful methods like .most_common() and arithmetic support.

```python
from collections import Counter
c = Counter("hello world")
print(c)  # Count each character
```

**🔹 defaultdict**
- Avoids KeyError by providing default values automatically.
```python
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
```

**🔹 ChainMap**
- Useful for combining configs, overriding scopes, layered dictionaries.
```python
from collections import ChainMap
cm = ChainMap({'a': 1}, {'a': 2, 'b': 3})
print(cm['a'])  # 1 (from first dict)
```

- **Simple Task Queue Processor (using deque)**
```python
from collections import deque

# Create a queue of tasks
task_queue = deque(["Email User", "Generate Report", "Backup Database"])

# Process tasks
while task_queue:
    current_task = task_queue.popleft()
    print(f"✅ Processing task: {current_task}")
```

- **Word Frequency Counter (using Counter)**
```python
from collections import Counter
import re

text = """
Python is great for data science. Python is also widely used in web development, scripting, and automation.
"""

# Clean and split text into words
words = re.findall(r'\w+', text.lower())

# Count word frequencies
word_counts = Counter(words)

# Get top 3 most common words
print("🔢 Most common words:", word_counts.most_common(3))
```