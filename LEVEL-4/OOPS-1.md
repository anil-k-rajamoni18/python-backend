# Object-Oriented Programming (OOP)

### **🔹 1. Functional Programming (FP)**
> Functional Programming avoids changing state and relies on pure functions—functions that return the same output for the same inputs, without side effects. It promotes efficiency, lazy evaluation, fewer bugs, and easier parallelism.

| Feature           | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| ✅ Paradigm        | Declarative — focuses on *what* to solve, not *how*.            |
| ✅ Core Idea       | Uses **pure functions**, avoids changing state or mutable data. |
| ✅ Key Concepts    | Functions, immutability, recursion, first-class functions.      |
| ✅ Python Features | `map()`, `filter()`, `reduce()`, lambda, list comprehensions    |

**Example**
```python
def add(x, y):
    return x + y
```
**Advantages:**
- Easy to test/debug (pure functions)
- Concurrency-friendly (no shared state)
- Shorter, expressive code for transformations

**Disadvantages:**
- Less intuitive for modeling complex systems (e.g., GUIs, games)
- Recursion can be less efficient in Python

### **🔸 2. Object-Oriented Programming (OOP)**
> Object-Oriented Programming organizes code using objects and classes. Objects store data (attributes) and behavior (methods), modeling real-world entities and making complex programs easier to manage.

| Feature        | Description                                               |
| -------------- | --------------------------------------------------------- |
| ✅ Paradigm     | Imperative — models real-world entities using **objects** |
| ✅ Core Idea    | Data and behavior grouped into **classes**                |
| ✅ Key Concepts | Class, object, inheritance, encapsulation, polymorphism   |

```python
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
```
**Advantages:**
- Models real-world systems naturally
- Easier to manage large, complex codebases
- Code reuse via inheritance

**Disadvantages**
- More boilerplate
- Overhead for simple tasks
- Can become rigid and tightly coupled

---

## 🔶 What is OOP in Python?
> OOP (Object-Oriented Programming) is a programming style that encapsulates data and behavior into classes and objects.

**🔑 Key Elements:**
- Class: Blueprint for an object (e.g., Car, User)
- Object: Instance of a class (e.g., my_car = Car())
- Method: Function inside a class
- Attribute: Variable inside a class

**Pros:**
- 📦 Encapsulation: Keeps data safe from outside interference
- 🔁 Reusability: Use inheritance to reuse code
- 👷‍♀️ Modularity: Split code into independent classes
- 🔍 Maintainability: Easier to locate bugs and refactor

**Cons:**
- ❗ Complexity: Overhead for small scripts or problems
- ⏳ Slower: Slightly less performant than FP for small tasks
- ⚙️ Tight coupling: Bad design can cause ripple effects

--- 

## 🧱 OOP Principles

**1. `Encapsulation`**
-  Bundling data and methods that operate on that data into one unit, while restricting direct access to some components.
- Real-life Example:
    - ATM Machine: You interact using buttons and a screen, but the internal logic (like PIN verification or cash management) is hidden from you.

    - Mobile Phone: You use an interface to make calls or send messages, but the internal workings are protected.

**2. `Abstraction`**
- Hiding complex internal implementation details and showing only the necessary features to the user.
Real-life Example:

**Real-life Example:**
    - Car Driving: You turn the key or push a button to start the engine, without needing to know how the fuel system, battery, and ignition work together.

    - TV Remote: Pressing a button changes the channel, but you don’t see how signals are processed inside.


**3. `Inheritance`**
- One class can acquire the properties and behavior (methods) of another class.

**Real-life Example:**

    - Family Hierarchy: A child inherits features from parents — like eye color or last name.

    - Vehicle Types: All vehicles (bikes, cars, trucks) inherit basic characteristics from a common vehicle category (like having wheels, engine, etc.).

**4. `Polymorphism`**
- The ability of different classes to be treated as instances of the same class through a common interface, with each responding differently.

**Real-life Example:**
    - Same Button, Different Action: In a media player, pressing the "play" button could play music, a video, or a podcast, depending on context.
    - Animal Sounds: All animals have a "make sound" action, but a dog barks, a cat meows, and a cow moos.

---

## **1.`Class`**
- A class is a blueprint or template for creating objects.
- It defines the structure and behavior (attributes and methods) of objects.
- Created using the class keyword in Python.
- Class names should be singular and follow PascalCase (e.g., Student, CarModel).

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand      # private attribute
        self.__model = model      # private attribute

    def display_info(self):       # public method
        print(f"Car: {self.__brand} {self.__model}")
````
## **2. `Object`**
- An object is a real-world instance created from a class.
- It has state (attributes) and behavior (methods).
- Attributes represent data (state), while methods define functionality (behavior).
- Objects can’t exist without a class.
- Attributes are usually private; methods are public.
- Objects expose data through methods.

```python
# Creating an object (instance of the Car class)
my_car = Car("Toyota", "Corolla")

my_car.display_info()
```

**Basic Class Declaration**
```python
class MyClass:
    pass
```
- A simple empty class using the class keyword.
- pass is used when no properties or methods are defined yet.


#### 🔹 Instance Variables
- Belong to an object (instance) of a class.
- Each object has its own copy.
- Defined using self.variable_name inside methods (usually __init__).

```python
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

print(s1.name)  
print(s2.name)  
```
- Values are unique per object.
- Modified through the object: s1.name = "Alicia"

#### 🔹 Class Variables
- Shared across all objects of a class.
- Defined outside any method, usually at the top of the class body.
- Accessed using the class name or object reference.

```python
class Student:
    school_name = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name         # instance variable

s1 = Student("Ram")
s2 = Student("Krishna")

print(s1.school_name)  
print(s2.school_name)  
```
- Same for all instances unless modified.
- Can be accessed or modified using ClassName.variable (recommended).

----
| Feature           | Instance Variable           | Class Variable                |
| ----------------- | --------------------------- | ----------------------------- |
| Scope             | Specific to an object       | Shared across all objects     |
| Declaration       | Inside methods using `self` | Inside class, outside methods |
| Memory Allocation | Per object                  | One copy for entire class     |
| Access            | `object.var_name`           | `ClassName.var_name`          |

---

## Constructor (`__init()__`)
- A constructor is a special method used to initialize objects.
- In Python, the constructor method is named __init__().
- It's called automatically when an object is created.

**Purpose of __init__()**
- Used to initialize the object’s state (assign values to instance variables).
- Sets up the initial values when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Max", 25)
print(p1.name)  
```

**🤔 What is self?**
- self refers to the current object (instance) of the class.
- It is used to access instance variables and methods within the class.
> Think of self as a reference to "this object".

### 🧩 Types of Constructors
- Python supports mainly one constructor per class (__init__), but conceptually we can think of these types:
| Type                          | Description                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| **Default Constructor**       | No parameters except `self`. Used when no arguments are passed.                                  |
| **Parameterized Constructor** | Takes arguments to initialize instance variables.                                                |
| **Constructor Overloading**   | Not directly supported in Python, but can be handled using default values or `*args`/`**kwargs`. |

**Default Constructor**
```python
class Demo:
    def __init__(self):
        print("Default constructor")

d = Demo()
```

**Parameterized Constructor**
```python
class Demo:
    def __init__(self, x):
        self.x = x

d = Demo(10)
```

**Simulating Constructor Overloading**
```python
class Demo:
    def __init__(self, x=None):
        if x:
            self.x = x
        else:
            self.x = 0
```

**Examples**

```python
class Fruits:
    favourite = "Apple"

    def __init__(self):
        self.favourite = "Orange"

    def show(self):
        print(self.favourite)

obj = Fruits()
obj.show()
print(Fruits.favourite)
```

```python
class Person1():
   
    def __init__(self,surname,age): # param
        self.c=surname
        self.d=age
        
    def __init__(self): # non-param
        print("Hey HI!!")
             
    def __init__(self,name): # param
        self.a=name      
        
    def __init__(self,fullname,year,place): # param
        """
        constructor
        """
        self.x=fullname
        self.y=year
        self.z=place


p = Person1('Alice', 45)
print(p)
```

```
Create a class Election with the following:

🔹 Attributes:
name, city, election_id, have_voter_card, age

🔹 Method:
Check if the person is eligible to vote based on:

Age ≥ 18

Has voter card (True)

election_id is a 10-character alphanumeric (A–Z, 0–9)

✅ If eligible → print "Allowed to vote"
❌ Else → print "Not allowed to vote"

```

---

### 🔐 Access Modifiers
> Python control access modifications which are used to restrict access to the variables and methods of the class.
- To control the visibility and accessibility of class members (attributes and methods).
- To protect data from unauthorized access or accidental modification.
- To encapsulate the internal details and expose only what is necessary.
- To help maintain data integrity and security.

**🔹 Types of Access Modifiers**
| Modifier      | Description                          | Python Syntax          |
| ------------- | ------------------------------------ | ---------------------- |
| **Public**    | Accessible from anywhere             | No underscore prefix   |
| **Protected** | Accessible within class & subclasses | Single underscore `_`  |
| **Private**   | Accessible only within the class     | Double underscore `__` |


**1. Public Members**
```python
class Car:
    def __init__(self):
        self.brand = "Toyota"  # Public attribute

    def drive(self):
        print("Driving")
```

**2. Protected Members**
```python
class Car:
    def __init__(self):
        self._model = "Corolla"  # Protected attribute

class Sedan(Car):
    def show_model(self):
        print(self._model)  # Accessible in subclass
```
- Conventionally treated as "internal use"
- Accessible in class and subclasses, but not recommended outside.


**3. Private Members**
```python
class Car:
    def __init__(self):
        self.__engine_number = "12345"  # Private attribute

    def get_engine_number(self):
        return self.__engine_number

car = Car()
print(car.get_engine_number()) 
print(car.__engine_number)      
```

- Name mangling hides the attribute: internally stored as _Car__engine_number
- Not directly accessible outside the class.

---

### ✨ Special Methods (Magic Methods / Dunder Methods)
- Special methods in Python start and end with double underscores (e.g., __init__, __str__, __repr__).
- They define behavior for built-in operations and functions.
- Let you customize how objects behave with operators, functions, or built-in syntax.

**🔹 Common Special Methods**
| Method     | Purpose                                              | Example Use                           |
| ---------- | ---------------------------------------------------- | ------------------------------------- |
| `__init__` | Constructor — initialize object attributes           | `obj = ClassName()`                   |
| `__str__`  | String representation for **print()** and `str()`    | `print(obj)` shows user-friendly info |
| `__repr__` | Official string representation, mainly for debugging | `repr(obj)` or in console output      |
| `__len__`  | Returns length of the object                         | `len(obj)`                            |
| `__eq__`   | Defines behavior for equality operator `==`          | `obj1 == obj2`                        |
| `__add__`  | Defines behavior for addition operator `+`           | `obj1 + obj2`                         |


**`__str__`**
- Used by the print() function to get a human-readable string representation of an object.
- Should return a string describing the object in a friendly way.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

p = Person("Alice", 30)
print(p)  
```

**__add__**
-  Defines the behavior of the + operator for objects.
- Allows you to customize how two objects are added together.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls p1.__add__(p2)

print(p3)  # Output: (6, 8)
```

**__eq__**
- Defines the behavior of the equality operator ==.
- Allows you to customize how two objects are compared for equality.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

**Difference Between __str__ and __repr__**
- __str__: For end-users, readable and informal.
- __repr__: For developers, unambiguous and often includes details to recreate the object.

```python
def __repr__(self):
    return f"Person(name={self.name!r}, age={self.age!r})"
```

**🔹 Special Attributes**
- __dict__: Dictionary containing all attributes of an object.
- __class__: Reference to the object's class.
- __doc__: Docstring of the class or method.

```python
print(p.__dict__)  # {'name': 'Alice', 'age': 30}
print(p.__class__) # <class '__main__.Person'>
print(Person.__doc__) # Prints class docstring if available
```