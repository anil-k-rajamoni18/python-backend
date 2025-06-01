# 📚 Strings in Python?
- A **string** is a sequence of characters enclosed within quotes.
- Strings are used to store text data.
- Strings are **immutable**, meaning once created, they cannot be changed.
- They support **indexing** and **slicing** to access parts of the string.

### ✍️ Different Ways to Declare Strings
1. **Single Quotes `'...'`**
```python
name = 'Alice'
```

2. Double Quotes "..."
```python
greeting = "Hello, World!"
```

3. Triple Quotes '''...''' or """..."""
- Used for multi-line strings or docstrings.
```python
message = '''This is a
multi-line
string'''
```

**Why Different Ways?**
- Single and double quotes are mostly interchangeable and used for convenience.
- Triple quotes allow strings to span multiple lines and preserve formatting.
- Using different quotes inside strings helps avoid the need for escaping characters.
```python
quote = "She said, 'Hello!'"
```

## 🔧 Common String Methods
| Method                | Description                                 | Example                                  |
| --------------------- | ------------------------------------------- | ---------------------------------------- |
| `.lower()`            | Converts string to lowercase                | `'HELLO'.lower()` → `'hello'`            |
| `.upper()`            | Converts string to uppercase                | `'hello'.upper()` → `'HELLO'`            |
| `.strip()`            | Removes leading/trailing whitespace         | `'  hello  '.strip()` → `'hello'`        |
| `.replace(old, new)`  | Replaces substring with new substring       | `'cat'.replace('c', 'b')` → `'bat'`      |
| `.split(sep)`         | Splits string into list by separator        | `'a,b,c'.split(',')` → `['a', 'b', 'c']` |
| `.join(iterable)`     | Joins elements of iterable into a string    | `','.join(['a', 'b', 'c'])` → `'a,b,c'`  |
| `.find(sub)`          | Finds first index of substring (-1 if none) | `'hello'.find('e')` → `1`                |
| `.startswith(prefix)` | Checks if string starts with prefix         | `'hello'.startswith('he')` → `True`      |
| `.endswith(suffix)`   | Checks if string ends with suffix           | `'hello'.endswith('lo')` → `True`        |


**Example**
```python
# Real-time example demonstrating multiple string methods in one scenario


text = "  Python3.8 is AWESOME! \tLet's test string methods.\nNew line here.  "

print("Original Text:")
print(repr(text))

# 1. capitalize() - first char uppercase, rest lowercase
print("\ncapitalize():", text.capitalize())

# 2. casefold() - aggressive lowercase for case-insensitive comparison
print("casefold():", text.casefold())

# 3. center(width, fillchar) - center text with fill character
print("center(50, '*'):", text.center(50, '*'))

# 4. count(sub) - count occurrences of substring
print("count('is'):", text.count("is"))

# 5. encode(encoding) - encode to bytes
print("encode('utf-8'):", text.encode('utf-8'))

# 6. endswith(suffix) - check if ends with substring
print("endswith('here.  '):", text.endswith("here.  "))

# 7. expandtabs(tabsize) - replace tabs with spaces
print("expandtabs(4):", repr(text.expandtabs(4)))

# 8. find(sub) - first index of substring or -1
print("find('string'):", text.find("string"))

# 9. format() - format with placeholders
template = "Version: {}"
print("format():", template.format("3.8"))

# 10. format_map(mapping) - format using dict
template_map = "Hello, {name}!"
print("format_map():", template_map.format_map({'name': 'Alice'}))

# 11. index(sub) - like find but raises error if not found
print("index('AWESOME'):", text.index("AWESOME"))

# 12. isalnum() - checks if all chars are alphanumeric
print("isalnum():", text.strip().replace('.', '').replace(' ', '').isalnum())

# 13. isalpha() - checks if all chars are alphabetic
print("isalpha():", "Python".isalpha())

# 14. isascii() - checks if all chars are ASCII
print("isascii():", text.isascii())

# 15. isdecimal() - all decimal digits
print("isdecimal():", "12345".isdecimal())

# 16. isdigit() - all digits (includes superscripts)
print("isdigit():", "²³".isdigit())

# 17. isidentifier() - valid Python identifier
print("isidentifier('variable_1'):", "variable_1".isidentifier())

# 18. islower() - all lowercase
print("islower():", "hello".islower())

# 19. isnumeric() - all numeric characters (includes fractions etc.)
print("isnumeric():", "½".isnumeric())

# 20. isprintable() - all printable characters
print("isprintable():", text.isprintable())

# 21. isspace() - all whitespace
print("isspace():", " \t\n".isspace())

# 22. istitle() - string is title cased
print("istitle():", "Hello World".istitle())

# 23. isupper() - all uppercase
print("isupper():", "HELLO".isupper())

# 24. join(iterable) - join strings with this string as separator
print("join():", "-".join(["Python", "3.8", "Rocks"]))

# 25. ljust(width, fillchar) - left justify with fillchar
print("ljust(30, '.'):", "left".ljust(30, '.'))

# 26. lower() - all lowercase
print("lower():", "HELLO".lower())

# 27. lstrip() - remove leading whitespace
print("lstrip():", "   spaces".lstrip())

# 28. maketrans() & translate() - replace chars using translation table
table = str.maketrans("aeiou", "12345")
print("translate():", "translate vowels".translate(table))

# 29. partition(sep) - split into tuple (before, sep, after)
print("partition('is'):", "This is fun".partition("is"))

# 30. removeprefix(prefix) - remove prefix if present (Python 3.9+)
print("removeprefix('This '):", "This is fun".removeprefix("This "))

# 31. removesuffix(suffix) - remove suffix if present (Python 3.9+)
print("removesuffix(' fun'):", "This is fun".removesuffix(" fun"))

# 32. replace(old, new) - replace substring
print("replace('fun', 'awesome'):", "This is fun".replace("fun", "awesome"))

# 33. rfind(sub) - last index of substring or -1
print("rfind('is'):", "This is fun".rfind("is"))

# 34. rindex(sub) - like rfind but raises error if not found
print("rindex('is'):", "This is fun".rindex("is"))

# 35. rjust(width, fillchar) - right justify
print("rjust(30, '.'):", "right".rjust(30, '.'))

# 36. rpartition(sep) - like partition but splits at last occurrence
print("rpartition('is'):", "This is fun".rpartition("is"))

# 37. rsplit(sep, maxsplit) - split from right
print("rsplit(' ', 1):", "one two three".rsplit(" ", 1))

# 38. rstrip() - remove trailing whitespace
print("rstrip():", "trailing spaces   ".rstrip())

# 39. split(sep, maxsplit) - split string into list
print("split(' ', 2):", "one two three four".split(" ", 2))

# 40. splitlines(keepends) - split by lines
multi_line = "Line1\nLine2\r\nLine3"
print("splitlines():", multi_line.splitlines())

# 41. startswith(prefix) - check if starts with prefix
print("startswith('  Python'):", text.startswith("  Python"))

# 42. strip() - remove leading and trailing whitespace
print("strip():", text.strip())

# 43. swapcase() - swap uppercase to lowercase and vice versa
print("swapcase():", "Hello World".swapcase())

# 44. title() - title case each word
print("title():", "hello world from python".title())

# 45. upper() - all uppercase
print("upper():", "hello".upper())

# 46. zfill(width) - pad numeric string on left with zeros
print("zfill(10):", "42".zfill(10))

```

### Questions
#### 🚀 Hands-On Python String Questions

1. **User Input Validation:**  
   Ask the user to enter their username.  
   - Check if the username is a valid Python identifier (no spaces, starts with letter/underscore).  
   - Ensure it contains only alphanumeric characters.  
   - If valid, print "Username accepted", else print "Invalid username".

2. **Email Domain Extractor:**  
   Given an email input from the user, extract and print the domain part (after `@`).  
   Example: For `user@example.com`, output should be `example.com`.

3. **Password Strength Checker:**  
   Take a password input and check:  
   - Length is at least 8 characters.  
   - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character.  
   - Print "Strong password" if all conditions met, else "Weak password".

4. **Log File Parser:**  
   Given a multi-line string representing log entries separated by newlines,  
   - Split into individual log lines.  
   - Count how many lines start with `"ERROR"` and how many with `"WARNING"`.

5. **Text Cleaner:**  
   Given user input with inconsistent spacing and random uppercase letters,  
   - Remove extra spaces (leading, trailing, and multiple spaces between words).  
   - Convert the text to lowercase.  
   - Print the cleaned text.

6. **Invoice Formatter:**  
   You have a list of product names and their prices.  
   - Join product names into a single string separated by commas.  
   - Format the prices to 2 decimal places and join them with a dollar sign prefix (`$`).  
   - Print a formatted receipt string showing products and prices aligned neatly.

7. **URL Validator:**  
   Ask the user to enter a URL and check if it:  
   - Starts with `"http://"` or `"https://"`  
   - Ends with `".com"`, `".org"`, or `".net"`  
   Print `"Valid URL"` or `"Invalid URL"` accordingly.

8. **Sentence Capitalizer:**  
   Given a sentence input, capitalize the first letter of every word and print it.

9. **Character Frequency Counter:**  
   Take a string input and count the frequency of each character (ignore case).  
   Display the counts in descending order.

10. **Secret Message Encoder:**  
    Replace all vowels in a sentence with asterisks (`*`).  
    Print the encoded message.

---

# 📋 List in Python
- A **list** is an **ordered**, **mutable** collection of items.
- Items can be of **different data types** (int, str, float, etc.).
- Lists allow **duplicate** elements.
- Lists are **indexed**, starting at 0.
- Lists are defined using **square brackets []**.

**Syntax**
```python
my_list = [item1, item2, item3, ...]
```
**Example**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "hello", 3.14, True]
```

**🔑 Properties of Lists**
| Property          | Description                      |
| ----------------- | -------------------------------- |
| Ordered           | Maintains the order of insertion |
| Mutable           | Can change items after creation  |
| Allows Duplicates | Can store duplicate elements     |
| Indexed           | Supports indexing and slicing    |
| Heterogeneous     | Can hold mixed data types        |


**🕵️ When to Use Lists?**
- When you need an ordered collection of items.
- When you want to modify elements (add, update, remove).
- When duplicates are allowed.
- For tasks like storing user inputs, processing sequences, or managing collections.

**List Methods with Examples**

**1. append(object)**
- Adds an item to the end of the list.
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```

**2. insert(index, item)**
- Inserts an item at a specified index.
```python
numbers = [1, 2, 4]
numbers.insert(2, 3)  # insert 3 at index 2
print(numbers)        # [1, 2, 3, 4]
```

**3. extend(iterable)**
- Adds all items from an iterable (list, tuple, etc.) to the end.
```python
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]
```

**4. remove(item)**
- Removes the first occurrence of an item.
```python
colors = ["red", "green", "blue", "green"]
colors.remove("green")
print(colors)  # ['red', 'blue', 'green']
```

**5. pop([index])**
- Removes and returns the item at the given index (default last).
```python
stack = [1, 2, 3, 4]
last_item = stack.pop()
print(last_item)  # 4
print(stack)      # [1, 2, 3]
```

**6. clear()**
- Removes all items from the list.
```python
nums = [1, 2, 3]
nums.clear()
print(nums)  # []
```

**7. index(item, [start, [end]])**
- Returns the index of the first occurrence of the item.
```python
letters = ['a', 'b', 'c', 'b']
print(letters.index('b'))  # 1
```

**8. count(item)**
- Returns how many times an item appears.
```python
nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3
```

**9. sort(reverse=False)**
- Sorts the list in-place in ascending order by default.
```python
values = [3, 1, 4, 2]
values.sort()
print(values)  # [1, 2, 3, 4]

values.sort(reverse=True)
print(values)  # [4, 3, 2, 1]

```

**10. reverse()**
- Reverses the order of the list in-place.
```python
items = [1, 2, 3]
items.reverse()
print(items)  # [3, 2, 1]
```

**11. copy()**
- Returns a shallow copy of the list.
```python
original = [1, 2, 3]
new_list = original.copy()
print(new_list)  # [1, 2, 3]
```

## Summary

#### ➡️ Insertion Methods
- `append(obj)` — Adds an object at the end of the list  
- `insert(index, obj)` — Inserts an object at the specified index  
- `extend([obj1, obj2, ..., objn])` — Adds multiple objects from another iterable  

---

#### ➡️ Deletion Methods
- `pop(index=-1)` — Removes and returns the element at the given index (default last). Raises `IndexError` if index is invalid.  
- `remove(value)` — Removes the first occurrence of the value. Raises `ValueError` if the value does not exist.  

---

#### ➡️ Popular Methods
- `reverse()` — Reverses the list in place  
- `count(value)` — Counts how many times a value appears  
- `index(value)` — Returns the index of the first occurrence of a value  
- `sort()` — Sorts the list in ascending order by default  
- `clear()` — Removes all elements from the list  
- `copy()` — Creates a shallow copy of the list  

---

#### ⚠️ Observations
- With `insert()`, even if the index is positive or negative but out of range, Python still inserts the item (at start or end).  
- `pop()` without an argument removes the last item by default.  
- You **cannot** pop from an empty list — this raises an error.  
- `remove()` throws a `ValueError` if the specified element is not found.  
- Using `sort(reverse=True)` sorts the list in descending order.  
- The `copy()` method creates a new list object with a different memory address from the original.  

--- 
**Realtime example: Managing a To-Do List App**

```python
# Scenario: Managing a To-Do List App

tasks = ["Buy groceries", "Call Alice", "Finish report"]

# 1. append() - Add a new task at the end
tasks.append("Walk the dog")
print("After append:", tasks)

# 2. insert() - Add an urgent task at position 1
tasks.insert(1, "Pay bills")
print("After insert:", tasks)

# 3. extend() - Add multiple new tasks from another list
tasks.extend(["Schedule meeting", "Email Bob"])
print("After extend:", tasks)

# 4. remove() - Remove a completed task by name
tasks.remove("Call Alice")
print("After remove:", tasks)

# 5. pop() - Remove and get the last task (mark done)
done_task = tasks.pop()
print("Popped task:", done_task)
print("After pop:", tasks)

# 6. clear() - Clear all tasks (commented to keep list for next steps)
# tasks.clear()
# print("After clear:", tasks)

# 7. index() - Find position of a task
pos = tasks.index("Pay bills")
print("Index of 'Pay bills':", pos)

# 8. count() - Count how many times 'Buy groceries' appears
tasks.append("Buy groceries")
count = tasks.count("Buy groceries")
print("Count of 'Buy groceries':", count)

# 9. sort() - Sort tasks alphabetically
tasks.sort()
print("After sort:", tasks)

# 10. reverse() - Reverse task order (e.g. show newest first)
tasks.reverse()
print("After reverse:", tasks)

# 11. copy() - Create a backup of tasks
backup_tasks = tasks.copy()
print("Backup tasks:", backup_tasks)

```
---
### 📝 Hands-on Questions

1. **Shopping Cart Manager**  
   Create a list representing a shopping cart with some items.  
   - Add 3 new items using different list methods (`append`, `insert`, `extend`).  
   - Remove one item by name.  
   - Print the final cart sorted alphabetically.

2. **Student Scores**  
   Given a list of student scores `[85, 92, 78, 90, 88]`:  
   - Add a new score to the list.  
   - Find the highest and lowest scores by sorting the list.  
   - Remove the lowest score using `pop()` and print the updated list.

3. **Duplicate Task Checker**  
   You have a to-do list with some duplicate tasks:  
   `tasks = ["email", "call", "email", "meeting", "call"]`  
   - Count how many times `"email"` appears.  
   - Remove the first occurrence of `"call"`.  
   - Print the updated list.

4. **Reverse Order Playlist**  
   Create a list of your favorite songs.  
   - Print the playlist in the original order.  
   - Reverse the playlist order using a list method and print again.  
   - Create a copy of the reversed playlist and print it.

5. **Index Finder**  
   You have a list of cities:  
   `cities = ["New York", "London", "Paris", "Tokyo", "Delhi"]`  
   - Find and print the index of `"Tokyo"`.  
   - Insert a new city `"Berlin"` at index 2.  
   - Print the updated list.

---

# 📌 Tuple
- A **tuple** is an **immutable** ordered collection of elements.
- Elements can be of **different data types**.
- Once created, **tuple elements cannot be changed** (no addition, deletion, or modification).

**Syntax**
```python
# Creating a tuple
my_tuple = (1, 2, 3)

# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)

# Single element tuple (note the comma)
single_element = (5,)
```

**🔑 Properties of Tuples**
- Ordered: Elements maintain their position.
- Immutable: Elements cannot be modified after creation.
- Allows duplicates: Multiple identical elements are allowed.
- Can contain heterogeneous data types.

**🕵️‍♂️ When to Use Tuples?**
- When you want to store a collection of fixed data.
- When you want to ensure data integrity (no accidental changes).
- For keys in dictionaries (tuples are hashable, lists are not).
- When you want to return multiple values from a function.
- Slightly faster and more memory-efficient than lists.

#### ⚙️Methods
- Tuples have only two built-in methods:
Returns the number of times x appears in the tuple.

**1. count(x)**
- Returns the number of times x appears in the tuple.
```python
t = (1, 2, 3, 2, 2)
print(t.count(2))  # Output: 3
```

**2. index(x[, start[, end]])**
- Returns the first index of x in the tuple.
- Raises ValueError if x is not found.
```python
t = (10, 20, 30, 40, 20)
print(t.index(20))     # Output: 1
print(t.index(20, 2))  # Start searching from index 2, Output: 4
```

#### **Real-Time Examples**
**Example 1: Storing Coordinates (Immutable Data)**
```python
coordinates = (10.0, 20.0)
print("X:", coordinates[0])
print("Y:", coordinates[1])
```

**Example 2: Returning Multiple Values from a Function**
```python
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([4, 1, 7, 9])
print("Min:", result[0], "Max:", result[1])
```

**Example 3: Using Tuple as Dictionary Key**
```python
location = {}
location[(40.7128, -74.0060)] = "New York"
print(location)
```

### 🚫 Tuple vs List
| Feature    | Tuple                    | List                     |
| ---------- | ------------------------ | ------------------------ |
| Mutability | Immutable                | Mutable                  |
| Syntax     | `(1, 2, 3)`              | `[1, 2, 3]`              |
| Methods    | `count()`, `index()`     | Many (append, remove...) |
| Use Case   | Fixed data, keys in dict | Dynamic data collection  |


---
# 🔹 Set in Python

A **set** is an unordered, mutable collection of unique elements.

- **Unordered**: Items do not maintain insertion order.
- **Mutable**: Can add or remove items.
- **Unique**: No duplicate elements allowed.

**🛠️ Syntax:**
```python
my_set = {1, 2, 3}

# Or using constructor:
my_set = set([1, 2, 3])
````

**✅ When to Use Sets?**
- When you need to store unique items.
- For efficient membership tests (x in set is faster than in lists).
- When you need to perform set operations (union, intersection, etc.).


**Properties of Sets:**
| Property      | Description                  |
| ------------- | ---------------------------- |
| Unordered     | No indexing or slicing       |
| Mutable       | Can change after creation    |
| Iterable      | Can be looped through        |
| No duplicates | Each item must be unique     |
| Mixed types   | Supports multiple data types |

### Methods

**1. `add()`**
- Adds an item to the set.

```python
fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'mango'}
```

**2. `update()`**
- Adds multiple items (from iterable) to the set.
```python
fruits.update(["cherry", "orange"])
```

**3. `remove()`**
- Removes a specific item (raises error if not found).
```python
fruits.remove("banana")
```

**4. `discard()`**
- Removes a specific item (no error if not found).
```python
fruits.discard("pineapple")  # No error
```

**5. `pop()`**
- Removes and returns a random item.
```python
item = fruits.pop()
print("Removed:", item)
```

**6. clear()**
- Removes all items from the set.
```python
fruits.clear()
```
**7. `copy()`**
- Returns a shallow copy of the set.
```python
new_set = fruits.copy()
```

**8. `union()`**
- Combines two sets (returns a new set).
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
```
**9. `intersection()`**
- Returns common elements in both sets.
```python
print(a.intersection(b))  # {3}
```

**10. `difference()`**
- Returns elements in a not in b.
```python
print(a.difference(b))  # {1, 2}
```

**11. `symmetric_difference()`**
- Returns elements not common in both.
```python
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
```

**12. `isdisjoint()`**
- Checks if two sets have no elements in common.
```python
print(a.isdisjoint({6, 7}))  # True
```

**13. `issubset()` / `issuperset()`**
- Check subset or superset relationship.
```python
x = {1, 2}
y = {1, 2, 3}
print(x.issubset(y))   # True
print(y.issuperset(x)) # True
```

**Common Use cases**
- Removing duplicates from a list:
```python
names = ["Alice", "Bob", "Alice"]
unique_names = set(names)
```
- Fast lookup:
```python
blacklist = {"spam", "bot", "banned"}
if user_input in blacklist:
    print("Blocked")
```

#### Scenario: 🛒 Online Shopping Cart System
```python
# Initialize the Cart
cart = {"laptop", "headphones", "mouse"}
print("Initial Cart:", cart)

# Add a New Item (add())
cart.add("keyboard")
print("After adding keyboard:", cart)


# Add Multiple Items (update())
cart.update(["webcam", "usb hub", "mouse"])  # 'mouse' is a duplicate
print("After bulk update:", cart)


# Remove an Unavailable Item (remove())
cart.remove("usb hub")  # Out of stock
print("After removing 'usb hub':", cart)


# Discard an Item Safely (discard())
cart.discard("microphone")  # Safe, no error even if item doesn’t exist
print("After trying to discard 'microphone':", cart)

# Remove a Random Item (pop())
removed_item = cart.pop()
print("Removed (random):", removed_item)
print("Cart after pop:", cart)

# Clear the Entire Cart (clear())
cart.clear()
print("Cart after clear():", cart)

# Copy Wishlist (copy())
wishlist = {"tablet", "headphones", "monitor"}
saved_cart = wishlist.copy()
print("Copied Wishlist:", saved_cart)

# Combine Two Carts (union())
friend_cart = {"phone", "tablet", "laptop"}
combined_cart = wishlist.union(friend_cart)
print("Combined Cart:", combined_cart)

# Find Common Items (intersection())
common_items = wishlist.intersection(friend_cart)
print("Common Items:", common_items)

# Wishlist Items Not in Friend’s Cart (difference())
exclusive_wishlist = wishlist.difference(friend_cart)
print("Unique to Wishlist:", exclusive_wishlist)

# Items Unique in Each (symmetric_difference())
non_common_items = wishlist.symmetric_difference(friend_cart)
print("Items unique to each cart:", non_common_items)


# Check Disjoint Sets (isdisjoint())
banned_items = {"knife", "fireworks"}
print("Is Wishlist safe?", wishlist.isdisjoint(banned_items))  # True

# Subset and Superset Checks
wishlist = {"tablet", "monitor"}
cart = {"tablet", "monitor", "mouse"}

print("Wishlist ⊆ Cart?", wishlist.issubset(cart))      # True
print("Cart ⊇ Wishlist?", cart.issuperset(wishlist))    # True
```
---

### 📝 Hands-on Questions

1. Unique Words in a Sentence
    - Ask the user to enter a sentence and print the set of unique words.

2. Common Hobbies Checker
    - Create two sets of hobbies from two users. Print:
        - Common hobbies
        - All hobbies combined
        - Hobbies unique to user1

3. Duplicate Remover
    - Write a function that takes a list and returns a new list with duplicates removed using a set.

4. Vowel Checker
    - Ask for a sentence and print which vowels appear in it using sets.

5. Symmetric Difference App
    - Take two sets of names: students who attended Day 1 and Day 2.
    - Print names of students who attended only one of the two days.


---

# 📘 Dictionary (`dict`)
- A **dictionary** is a built-in data type in Python used to store **key-value** pairs.  
- It is **unordered (before Python 3.7)**, **mutable**, and **indexed by keys** (not by position).


**Syntax**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```
- Keys are unique and immutable (strings, numbers, tuples).
- Values can be of any data type.

**🧾 Properties**
- 🔑 Key-value structure
- ✅ Keys must be unique and immutable
- 🔄 Mutable (can change, add, remove items)
- 🚫 No duplicate keys allowed
- 🔀 Maintains insertion order (Python 3.7+)

**When to Use**
- When you want to associate one piece of data with another (e.g., a name with an age).
- For fast lookup and retrieval using keys.
- To model structured data (e.g., user profile, config settings).

### 🛠️ Methods

**1. `dict()` constructor**
```python
person = dict(name="John", age=30)
print(person)
```
**2. `keys()`, `values()`, `items()`**
```python
user = {"name": "Ravi", "city": "Delhi", "age": 28}

print(user.keys())    # dict_keys(['name', 'city', 'age'])
print(user.values())  # dict_values(['Ravi', 'Delhi', 28])
print(user.items())   # dict_items([('name', 'Ravi'), ('city', 'Delhi'), ('age', 28)])
```

**3. get(key, default)**
```python
print(user.get("name"))         # Ravi
print(user.get("email", "N/A")) # N/A
```

**4. update() – add or modify entries**
```python
user.update({"city": "Mumbai", "email": "ravi@example.com"})
print(user)
```

**5. pop(key) – remove a key and return value**
```python
age = user.pop("age")
print(age)      # 28
print(user)
```

**6. popitem() – removes and returns the last item**
```python
last_item = user.popitem()
print(last_item)
```

**7. clear() – removes all items**
```python
user.clear()
print(user)  # {}
```

**8. copy() – returns a shallow copy**
```python
user_copy = user.copy()
```

**9. setdefault() – returns value if key exists, else sets with default**
```python
prefs = {"theme": "dark"}
prefs.setdefault("font", "Arial")
print(prefs)
```

**10. fromkeys() – create dict from keys with same default value**
```python
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)
print(default_scores)
```

**✅ Summary Table**
| Operation      | Method                          | Description               |
| -------------- | ------------------------------- | ------------------------- |
| Access value   | `dict[key]`                     | Direct access             |
| Safe access    | `get()`                         | Avoids KeyError           |
| Add/Update     | `update()`                      | Add or modify entries     |
| Delete         | `pop()`, `popitem()`            | Remove by key / last item |
| Inspect        | `keys()`, `values()`, `items()` | Retrieve info             |
| Copy           | `copy()`                        | Shallow copy              |
| Create default | `setdefault()`                  | Get or set default        |
| Bulk create    | `fromkeys()`                    | Create from list of keys  |

--- 

### 📝 Hands-on Questions

1. **Create a dictionary** called `car` with the following keys and values:  
   - `brand`: `"Toyota"`
   - `model`: `"Corolla"`
   - `year`: `2020`

- Print only the **keys**, **values**, and **items** of the `car` dictionary.
- Use the `get()` method to safely access the value of the key `"color"` from the `car` dictionary, with default `"Unknown"`.
- Add a new key `"color"` with value `"Red"` using the `update()` method.
- Remove the `"model"` key from the dictionary using `pop()`.


2. **Student Marks Analysis:**  
    - Create a dictionary of students and their marks.  
    - Find the student(s) with the highest and lowest marks.
	
3. **Login System:**  
    - Create a dictionary with usernames as keys and passwords as values.  
    - Ask for input and validate if the login is successful.
	
4. **Word Counter:**  
    - Accept a sentence from user input. Create a dictionary to count the frequency of each word.
	

5. **Character Frequency:**  
   - Create a dictionary that counts how many times each character appears in a string (case-insensitive).


   ---


## 📦 Other Collection Data Types (from collections module)

**1. namedtuple**
- Like a tuple, but with named fields.
- Useful for creating lightweight, readable data objects.
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(p1.x, p1.y)  # 10 20

# Example-2
Student = namedtuple('Student', ['name', 'roll', 'grade'])

s1 = Student('Asha', 101, 'A')
print(s1.name)  # Asha
print(s1.grade)  # A

# Example-3
Rectangle = namedtuple('Rectangle', ['length', 'width'])

r = Rectangle(10, 5)
area = r.length * r.width
print(f"Area: {area}")  # Area: 50


```

**2. deque (Double-Ended Queue)**
- A list-like container with fast appends and pops from both ends.
- More efficient than list for queue operations.

```python
from collections import deque

q = deque([1, 2, 3])
q.appendleft(0)
q.append(4)
print(q)  # deque([0, 1, 2, 3, 4])
```

**3. Counter**
- A dictionary subclass for counting hashable items.
```python
from collections import Counter

text = "banana"
count = Counter(text)
print(count)  # {'a': 3, 'b': 1, 'n': 2}
```

**4. OrderedDict (Python < 3.7)**
- Like dict but remembers insertion order (before Python 3.7).
- In Python 3.7+, normal dict maintains insertion order by default.
```python
from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
print(od)
```

**5. defaultdict**
- Like a dict but with a default value for missing keys.
```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1
print(dd['a'])  # 1
print(dd['b'])  # 0 (no KeyError)
```

**Summary**
| Collection    | Description                          | Use Case Example                         |
| ------------- | ------------------------------------ | ---------------------------------------- |
| `namedtuple`  | Tuple with named fields              | Coordinate points, records               |
| `deque`       | Fast queue operations from both ends | Task scheduling, sliding window          |
| `Counter`     | Count frequency of elements          | Word frequency, item count               |
| `OrderedDict` | Dict with preserved insertion order  | Custom serialization, ordered configs    |
| `defaultdict` | Dict with default value for new keys | Grouping, counting, mapping with default |
