### Methods in Python
- Methods are functions defined inside a class that operate on instances or the class itself.
- They define behaviors for the objects created from the class.

**Types of Methods in Python**
> Python primarily supports three types of methods inside classes:


| Method Type         | Description                                                                                               | How to Define                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Instance Method** | Works with an instance (object) of the class. Can access and modify object state.                         | First parameter is always `self` (the instance)                       |
| **Class Method**    | Works with the class itself, not instances. Can access/modify class state shared across instances.        | Use decorator `@classmethod` and first parameter is `cls` (the class) |
| **Static Method**   | Does not access instance or class data. Behaves like a regular function but lives in the class namespace. | Use decorator `@staticmethod` and no `self` or `cls` parameter        |

**🔹 Instance Method**
- Most common method type.
- Has access to instance attributes via self.
- Can modify object state or call other instance methods.
```python
class Person:
    def __init__(self, name):
        self.name = name  # instance variable

    def greet(self):
        print(f"Hello, my name is {self.name}")


p = Person("Ram")
p.greet()  

```

**🔹 Class Method**
- Bound to the class, not the instance.
- Can access/modify class variables shared by all instances.
- Marked with @classmethod decorator.
- Takes cls as the first parameter (refers to the class itself).

```python
class Person:
    species = "Homo sapiens"  # class variable

    @classmethod
    def species_info(cls):
        print(f"We are all {cls.species}")


Person.species_info()  # Called on the class itself
```

**Example: Alternative Constructor**
```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)  # Create instance using cls()
```


**🔹 Static Method**
- No access to self or cls.
- Utility functions related to the class but independent of instance/class state.
- Marked with @staticmethod decorator.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

result = Math.add(5, 7)  
```

**Class Methods vs Static Methods: When to Use?**
| Aspect                 | Class Method (`@classmethod`)                                                                      | Static Method (`@staticmethod`)                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Access to Class**    | Yes — receives class (`cls`) as first argument                                                     | No — does NOT receive `cls` or `self`                                                 |
| **Access to Instance** | No — cannot access instance (`self`) directly                                                      | No — cannot access instance (`self`)                                                  |
| **Typical Use Case**   | Methods that need to know or modify **class state**, or are alternative constructors               | Utility/helper functions related to the class but independent of instance/class state |
                                                                                 

**When to Use**
- We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.



---

## Type Hints (Type Annotations) in Python
- Type hints (or type annotations) are a way to explicitly specify the expected data types of variables, function parameters, and return values in Python code.
- Introduced in PEP 484 (Python 3.5+).
- Syntax uses a colon (:) for parameters and -> for return types.

**Why Use Type Hints?**
| Benefit                     | Explanation                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| **Improved Readability**    | Makes code easier to understand by clearly stating what types are expected. |
| **Early Error Detection**   | Static type checkers (e.g., `mypy`) can catch type errors before runtime.   |
| **Better IDE Support**      | Enhanced autocompletion, code navigation, and refactoring in editors.       |
| **Documentation**           | Serves as inline documentation for other developers.                        |
| **Facilitates Maintenance** | Easier to maintain and extend large codebases with clear contracts.         |

**syntax**
```python
	variable: type
    def func(param: type) -> type:
        pass
```

**Basic Types:**
```python
int: Integer values.
float: Floating-point numbers.
str: Strings.
bool: Boolean values (True or False).
list: Lists of a specific type (e.g., list[int]).
tuple: Tuples of specific types (e.g., tuple[str, int]).
dict: Dictionaries with specific key and value types (e.g., dict[str, int]).
None: Represents the absence of a value.
```

**Advanced Types (from the typing module):**
```python
Any: Represents any type, used when the type is unknown or can vary.
Union: Allows a variable to be one of several types (e.g., Union[int, float]).
Optional: Indicates that a variable can be either a specific type or None (e.g., Optional[str]).
Callable: Represents a function with specific parameter and return types.
TypeVar: Used for generic types.
NoReturn: Indicates that a function never returns (e.g., raises an exception).
```

### Examples
**Function Parameter and Return Type Annotations**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```
**Variable Annotations**
```python
age: int = 30
name: str
```

**Using typing Module**
- Provides complex types like Union, Tuple, Callable, TypeVar, Generic.
```python
from typing import List, Dict, Tuple, Optional, Union, Any, Callable, Literal, TypeAlias
```

**List and Nested Lists**
```python
def total(numbers: List[int]) -> int:
    return sum(numbers)

def matrix_sum(matrix: List[List[int]]) -> int:
    return sum(sum(row) for row in matrix)
```

**Dictionary**
```python
def count_words(texts: List[str]) -> Dict[str, int]:
    count = {}
    for word in texts:
        count[word] = count.get(word, 0) + 1
    return count
```

**Tuple**
```python
def get_position() -> Tuple[int, int]:
    return (10, 20)

coordinates: Tuple[float, float, float] = (1.0, 2.5, 3.1)
```

**Optional**
```python
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

**Any**
```python
def print_item(item: Any) -> None:
    print(item)
```

**Callable (Functions as Parameters)**
```python
def apply_operation(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

# Example usage:
def add(x: int, y: int) -> int:
    return x + y

result = apply_operation(5, 3, add)  # returns 8
```

**Literal (Specific Allowed Values)**
```python
from typing import Literal

def get_status(code: Literal["success", "error", "pending"]) -> str:
    return f"Status: {code}"
```

**Type Alias**
```python
Vector: TypeAlias = List[float]

def scale(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]
```

**Custom Classes with Type Hints**
```python
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

def discount(product: Product) -> float:
    return product.price * 0.9
```

**Nested Complex Structures**

```python
def process_data(data: List[Dict[str, Union[int, List[str]]]]) -> None:
    for record in data:
        print(record)
```

**🔹 TypeVar**
- Generics allow you to write code that works with different data types while maintaining type safety.
- You define type placeholders using TypeVar, which are filled in when the class/function is used.

```python
from typing import TypeVar

T = TypeVar('T')  
```
> T can be replaced by any type: int, str, List, or even user-defined classes.

```python
from typing import TypeVar

T = TypeVar('T')

def get_first(items: list[T]) -> T:
    return items[0]


print(get_first([1, 2, 3]))         # int
print(get_first(["a", "b", "c"]))   # str
```

**Generic Class**

- 🔑 Why Use Generics?
| Benefit              | Description                                          |
| -------------------- | ---------------------------------------------------- |
| ✅ Type Safety        | Prevents type errors at compile-time (via tools).    |
| ✅ Code Reuse         | Write once, work with any type.                      |
| ✅ Better Tooling     | IDEs can infer return types and provide suggestions. |
| ✅ Cleaner Interfaces | No need to hardcode types or return `Any`.           |


```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get(self) -> T:
        return self.content


int_box = Box[int](10)
str_box = Box[str]("hello")

print(int_box.get())  # 10
print(str_box.get())  # hello
```

**Bounded TypeVar**
- Limit T to subclasses of a certain class/interface.

```python
from typing import TypeVar

class Animal:
    def speak(self) -> str:
        pass

TAnimal = TypeVar('TAnimal', bound=Animal)

def make_speak(animal: TAnimal) -> str:
    return animal.speak()
```

**Custom API Wrapper Using Generics**
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class APIResponse(Generic[T]):
    def __init__(self, data: T, status: int):
        self.data = data
        self.status = status

    def is_success(self) -> bool:
        return 200 <= self.status < 300

user_data: dict = {"id": 1, "name": "Ram"}
response = APIResponse[dict](user_data, 200)

print(response.is_success())  
print(response.data["name"])  
```

---
## HandsOn Projects 
```
1. Student Management System
Concepts Used:
    Class and Object creation
    Inheritance (e.g., Undergraduate, Postgraduate)
    Encapsulation for private student data
    File/database interaction (optional)

Features:
    Add/edit/delete student records
    Assign courses and grades
    Generate transcripts
    Search/filter students


2. 🏦 Banking System
Concepts Used:
    Abstraction for transactions
    Inheritance (SavingsAccount, CurrentAccount)
    Polymorphism (withdrawal rules differ)
    Exception handling

Features:
    Deposit, withdraw, transfer
    Interest calculation (using class/staticmethod)
    Account statements
    Login system (admin/user)

3. Task/ToDo Management CLI App
Concepts Used:
    OOP Design Patterns (like Factory or Singleton for TaskManager)
    Data encapsulation
    Optional file or DB storage

Features:
    Add/edit/delete tasks
    Categorize and prioritize tasks
    Reminders
    CLI interface



```