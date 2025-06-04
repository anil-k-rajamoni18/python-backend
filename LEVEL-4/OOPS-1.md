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


**3. Inheritance**
- One class can acquire the properties and behavior (methods) of another class.

**Real-life Example:**

    - Family Hierarchy: A child inherits features from parents — like eye color or last name.

    - Vehicle Types: All vehicles (bikes, cars, trucks) inherit basic characteristics from a common vehicle category (like having wheels, engine, etc.).

**4. Polymorphism**
- The ability of different classes to be treated as instances of the same class through a common interface, with each responding differently.

**Real-life Example:**
    - Same Button, Different Action: In a media player, pressing the "play" button could play music, a video, or a podcast, depending on context.
    - Animal Sounds: All animals have a "make sound" action, but a dog barks, a cat meows, and a cow moos.


