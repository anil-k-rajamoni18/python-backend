# 📘 Functional Programming in Python
Functional Programming (FP) is a programming paradigm where programs are constructed by applying and composing functions. It emphasizes:

* Immutability: Data is not changed.
* Pure functions: Same input always returns the same output, no side effects.
* First-class functions: Functions are treated like variables.
* Higher-order functions: Functions can take other functions as arguments or return them.

**Usage of Functional Programming**
Functional programming is useful for:
- Data processing (e.g., filtering, transforming large data sets).
- Parallelism and concurrency (pure functions reduce side-effect risks).
- Cleaner, shorter code using declarative logic.

## Methods/Tools 

####  1. lambda functions (Anonymous Functions)
- A small anonymous function, usually one-liner.
- `lambda` keyword is used to define an anonymous function in Python.
- syntax: 
```python
lambda arguments: expression
```

```python
square = lambda x: x**2
print(square(5))  # Output: 25
```

**regular function**
```python
def addition(a,b):
    return a+b

addition(11,22)
print(type(addition))
```

**lambda**
```python
add = lambda a,b:a+b

print(type(add))

print(add(11,22))
```
> Use Case: Quick, throwaway functions for use in map(), filter(), etc.

---
#### 🔹 2. map() — Transform Each Item
- Applies a function to each item in an iterable. Each item is passed as an argument to the function.
- It returns a map object, which can be converted to other data types like a list or tuple to display the results.
- Syntax:
```python
map(function, iterable)
```

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]
```

**Convert list of strings to integers**
```python
str_numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # Output: [1, 2, 3, 4]
```

**Capitalize first letter of each word**
```python
words = ['apple', 'banana', 'cherry']
capitalized = list(map(str.capitalize, words))
print(capitalized)  # Output: ['Apple', 'Banana', 'Cherry']
```
**Add two lists element-wise**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)  # Output: [5, 7, 9]
```

**Flatten a list of lists using map and sum**
```python
list_of_lists = [[1, 2], [3, 4], [5, 6]]

# map sum with an empty list flattens the list of lists
flattened = sum(map(list, list_of_lists), [])
print(flattened)
```

**Processing CSV lines into structured data**
```python
csv_lines = [
    "John,25,Engineer",
    "Jane,30,Doctor",
    "Doe,22,Artist"
]

def parse_line(line):
    # complete the body
    pass

people = list(map(parse_line, csv_lines)) # dictionary
print(people)
```

**Element-wise multiplication of multiple lists**
```python
list1 = [2, 3, 4]
list2 = [5, 6, 7]
list3 = [8, 9, 10]

product = # complete missing part
print(product)
# Output: [80, 162, 280]
```

---
#### 🔹 3. filter() — Filter Items
- Filters items from an iterable based on a condition (returns only items for which the function returns True).
- The result is a filter object, which can be converted to a list or other collection.
- Syntax:
```python
filter(function, iterable)
```

- **Example**
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
````

**Filter even numbers from a list**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]
```
**Filter out empty strings**
```python
strings = ["apple", "", "banana", "", "cherry", ""]
non_empty = list(filter(<>, strings))
print(non_empty)  # Output: ['apple', 'banana', 'cherry']
```

**Filter names starting with a vowel**
```python
names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Ian", "Charlie"]

def starts_with_vowel(name):
    # Complete the code

vowel_names = list(filter(starts_with_vowel, names))
print(vowel_names)  # Output: ['Alice', 'Eve', 'Oscar', 'Uma', 'Ian']
```

**Filter numbers greater than a threshold**
```python
numbers = [10, 15, 20, 25, 30, 35]

def greater_than_20(x):
    return x > 20

filtered = # complete
print(filtered)  # Output: [25, 30, 35]
```

**Filter dictionaries based on key value**
```python
students = [
    {"name": "John", "grade": 75},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 65},
]

passed = # complete
print(passed)
# Output: [{'name': 'John', 'grade': 75}, {'name': 'Jane', 'grade': 85}]
```

**Filter out prime numbers (more complex condition)**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 20))
primes = list(filter(is_prime, numbers))
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

----
#### `reduce()` (from functools)
- reduce() is a function from the functools module.
- It applies a binary function cumulatively to the items of an iterable.
- The result is a single accumulated value.

**Syntax**
```python
from functools import reduce
reduce(function, iterable[, initializer])
```

- function: A binary function that takes two arguments.
- iterable: A sequence (like list or tuple).
- initializer (optional): Starting value for the accumulator.

**Example – Sum a List**
```python
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)  
```

**How it works:**
```python

Step 1: (1 + 2) = 3  
Step 2: (3 + 3) = 6  
Step 3: (6 + 4) = 10  
```

**🔁 With an Initializer**
```python
nums = [1, 2, 3]
result = reduce(lambda x, y: x + y, nums, 10)
print(result)  
```

**🔢 Multiply All Numbers**
```python
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  
```

**🔤 Find the Longest Word**
```python
words = ["cat", "elephant", "tiger", "hippopotamus"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)  
```

**📚 Concatenate Strings**
```python
words = ["Functional", "Programming", "in", "Python"]
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)
```

----

### 🔄 itertools – Functional Iteration Toolkit
- itertools provides fast, memory-efficient tools for working with iterators. 
- These are often used in functional programming for pipelines, infinite sequences, and combinatorics.

**1. `count(start=0, step=1)` – Infinite counter**`

```python
from itertools import count

for i in count(10, 2):
    print(i)
    if i > 20:
        break
```

**2. `cycle(iterable)` – Infinite loop over iterable**
```python
from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))
```

**3. `repeat(elem, n)` – Repeat an element n times (or forever)**
```python
from itertools import repeat

list(repeat("hello", 3))  
```

**4. `product(iterable, repeat=n)` – Cartesian product**
```python
from itertools import product

list(product([1, 2], repeat=2))  
```

**5. `permutations(iterable, r=None)` – All possible orderings**
```python
from itertools import permutations

list(permutations(['A', 'B', 'C'], 2)) 
```

**6. `combinations(iterable, r)` – All possible subsets of length r**
```python
from itertools import combinations

list(combinations([1, 2, 3], 2))  
```

**7. groupby(iterable, key=...) – Group consecutive items by a key**
```python
from itertools import groupby

data = "aaabbcaaa"
grouped = [(k, list(g)) for k, g in groupby(data)]
# [('a', ['a', 'a', 'a']), ('b', ['b', 'b']), ('c', ['c']), ('a', ['a', 'a', 'a'])]
```
----

#### 🛠️ functools – Tools for Functional Programming
- functools provides higher-order functions, memoization, partial function application, and more.

**1. `partial(func, *args, **kwargs)` – Pre-fill some function arguments**
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5)) 
```

**2. `lru_cache(maxsize=128)` – Memoization for function results**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Much faster with caching
```

**3. `cached_property` – Caches result of property method**
```python
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Calculating area...")
        return 3.1415 * self.radius ** 2

c = Circle(10)
print(c.area)  # Calculates
print(c.area)  # Uses cached value
```

**4. `singledispatch` – Function overloading based on argument type**
```python
from functools import singledispatch

@singledispatch
def greet(arg):
    print("Hello, unknown!")

@greet.register(str)
def _(arg):
    print(f"Hello, {arg}!")

@greet.register(int)
def _(arg):
    print(f"You gave the number {arg}.")

greet("Alice")  # Hello, Alice!
greet(42)       # You gave the number 42.
```

---
### 🔥 Functional-Style Coding Problems
**1. Find the Sum of Even Numbers in a List**
- Use: filter + reduce 

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
even_sum = reduce(lambda x, y: x + y, filter(lambda n: n % 2 == 0, nums))
print(even_sum)  # Output: 12
```

**2. Flatten a Nested List**
```python
from functools import reduce

nested = [[1, 2], [3, 4], [5]]
flattened = reduce(lambda x, y: x + y, nested)
print(flattened)  # Output: [1, 2, 3, 4, 5]
```

**Count Frequency of Elements**
```python
from functools import reduce

data = ['a', 'b', 'a', 'c', 'b', 'a']
freq = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, data, {})
print(freq)  # {'a': 3, 'b': 2, 'c': 1}
```

**Generate All Permutations of a String**
```python
from itertools import permutations

s = "abc"
perms = list(map(lambda x: ''.join(x), permutations(s)))
print(perms)
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
**Get Running Total (Prefix Sum)**
```python
from itertools import accumulate

nums = [1, 2, 3, 4]
running_total = list(accumulate(nums))
print(running_total)  # [1, 3, 6, 10]
```

**Filter Palindromes from a List**
```python
words = ["madam", "racecar", "apple", "noon"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)  # ['madam', 'racecar', 'noon']
```

**Find the Maximum Using reduce**
```python
from functools import reduce

nums = [4, 2, 9, 1, 7]
maximum = reduce(lambda x, y: x if x > y else y, nums)
print(maximum)  # Output: 9
```

**Remove Duplicates and Keep Order**
```python
from functools import reduce

items = [1, 2, 3, 1, 2, 4]
unique = reduce(lambda acc, x: acc + [x] if x not in acc else acc, items, [])
print(unique)  # [1, 2, 3, 4]
```