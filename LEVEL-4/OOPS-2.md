## 🔷 Inheritance in Python
> Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called child/derived class) to inherit the attributes and methods from another class (called parent/base class).

- 👨‍👩‍👧 Parent-Child Relationship in classes is like Class-Subclass.
- 🔁 Inheritance lets one class reuse the properties and methods of another.
- 🏛️ Parent/Base Class = the original class
- 👶 Child/Derived Class = the class that inherits

**✨ Benefits:**
-  Inheriting = copying features from another class
- 🌍 Mimics real-world relationships
-  Reuse code without rewriting
-  Add new features easily
-  Transitive: If B inherits A, then C (inheriting B) gets A too

**Why is Inheritance Used?**
- Code Reusability: Avoid code duplication by reusing existing class functionality.
- Maintainability: Centralize changes by updating the base class.
- Extensibility: Add new features without modifying existing code.
- Polymorphism: Allows the use of a unified interface for different data types.

```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    pass

obj = Child()
obj.show()  # Output: This is the parent class
```
---

#### Overview of self and super()

**`self`**
- Refers to the instance of the class.
- Used to access instance variables and methods.
- Always the first parameter in instance methods.

```python
class Example:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)
```

**`super()`**
- Calls methods from the parent class.
- Mostly used in method overriding, especially constructors.

```python
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")
```

---

### Types of Inheritance in Python
| Type             | Description                               | Example                           |
| ---------------- | ----------------------------------------- | --------------------------------- |
| **Single**       | One child inherits from one parent        | `class B(A)`                      |
| **Multiple**     | One child inherits from multiple parents  | `class C(A, B)`                   |
| **Multilevel**   | Chain of inheritance                      | `class C(B), class B(A)`          |
| **Hierarchical** | Multiple children inherit from one parent | `class B(A), class C(A)`          |
| **Hybrid**       | Combination of more than one type         | Involves multiple/multilevel etc. |

```python
# define a superclass
class super_class:
    # attributes and method definition

# inheritance
class sub_class(super_class):
    # attributes and method of super_class
    # attributes and method of sub_class
```

#### Single Inheritance
> When a child class inherits from only one parent class
- A Vehicle class and a Car class that inherits from it.

```python
class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Car is moving")

my_car = Car()
my_car.start_engine()  # Inherited
my_car.drive()
```

```python
class Person:
    def __init__(self, dept_id, dept_name):
        print('Initializing parent class')
        self._deptId = dept_id
        self._deptName = dept_name

    def display(self):
        print(self._deptId)
        print(self._deptName)

class Employee(Person):
    def __init__(self, dept_id, dept_name, emp_name, emp_id, salary, post):
        print('Initializing child class')
        self.empName = emp_name
        self.empId = emp_id
        self.salary = salary
        self.post = post
        Person.__init__(self, dept_id, dept_name)

    def display(self):
        super().display()
        print(self.empName, self.empId, self.salary, self.post, sep='\n')

emp1 = Employee('d123', 'IT', 'Kumar', 11223096, 200000, 'Intern')
emp1.display()
```

---

####  Multiple Inheritance
> When a child class inherits from multiple parent classes,
- A GPS class and a MusicSystem class. A SmartCar inherits both.
- Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket.

```python
class GPS:
    def navigate(self):
        print("Navigating to destination")

class MusicSystem:
    def play_music(self):
        print("Playing music")

class SmartCar(GPS, MusicSystem):
    def drive(self):
        print("SmartCar is driving")

my_smartcar = SmartCar()
my_smartcar.navigate()
my_smartcar.play_music()
my_smartcar.drive()
```

```python
class ParentOne:
    def __init__(self):
        self.text1 = "Geek1"
        print("ParentOne initialized")

    def welcome(self):
        print("Welcome from ParentOne")


class ParentTwo:
    def __init__(self):
        self.text2 = "Geek2"
        print("ParentTwo initialized")

    def greet(self):
        print("Greetings from ParentTwo")


class Child(ParentOne, ParentTwo):
    def __init__(self):
        ParentOne.__init__(self)
        ParentTwo.__init__(self)
        print("Child class initialized")

    def display_texts(self):
        print(self.text1, self.text2)


obj = Child()
obj.display_texts()
obj.greet()
obj.welcome()
```

```python
class ParentA:
    def __init__(self):
        self.message = "Message from ParentA"
        print("ParentA initialized")


class ParentB:
    def __init__(self):
        self.message = "Message from ParentB"
        print("ParentB initialized")


class Child(ParentB, ParentA):
    pass


obj = Child()
print(obj.message)
```

```python
class Mi:
    def __init__(self, ram, processor):
        print("Initializing Mi")
        self.ram = ram
        self.processor = processor
        self.model_name = "Mi"

    def mobile_description(self):
        print(self.model_name)
        print(f"RAM: {self.ram}\nProcessor: {self.processor}\n")

    def hello_mi(self):
        print("Hi, I am mi AI assistant tool...")

    def welcome(self):
        print("Welcome to Mi")


class OnePlus:
    def __init__(self, ram, processor):
        print("Initializing OnePlus")
        self.ram = ram
        self.processor = processor
        self.model_name = "OnePlus"

    def mobile_description(self):
        print(self.model_name)
        print(f"RAM: {self.ram}\nProcessor: {self.processor}\n")

    def print_greet(self):
        print("Hey, hi there!")

    def welcome(self):
        print("Welcome to OnePlus")


class NewMobile(Mi, OnePlus):
    pass


# Creating an object of NewMobile
ob = NewMobile("8GB", "SnapD")

# Calling methods
ob.mobile_description()
ob.print_greet()
ob.hello_mi()
ob.welcome()
```

---
#### Multilevel Inheritance
> When a child class inherits from multiple parent classes
- Device → Phone → Smartphone

```python
class Device:
    def power_on(self):
        print("Device powered on")

class Phone(Device):
    def call(self):
        print("Calling someone...")

class Smartphone(Phone):
    def browse_internet(self):
        print("Browsing the internet")

my_phone = Smartphone()
my_phone.power_on()       # From Device
my_phone.call()           # From Phone
my_phone.browse_internet() # From Smartphone
```

----

#### Hierarchical Inheritance
> More than one derived classes are created from a single base.
- A Account base class. Two subclasses: SavingsAccount and CurrentAccount.

```python
class Account:
    def account_info(self):
        print("General account information")

class SavingsAccount(Account):
    def interest_rate(self):
        print("Savings account interest: 4%")

class CurrentAccount(Account):
    def overdraft(self):
        print("Overdraft limit is $500")

savings = SavingsAccount()
current = CurrentAccount()

savings.account_info()
savings.interest_rate()

current.account_info()
current.overdraft()
```

---
#### Hybrid Inheritance
- Combination of Multiple and Multilevel Inheritance
```python
class Engine:
    def engine_type(self):
        print("Petrol engine")

class Vehicle(Engine):
    def wheels(self):
        print("Has 4 wheels")

class GPS:
    def navigation(self):
        print("GPS enabled")

class SmartVehicle(Vehicle, GPS):
    def features(self):
        print("Smart features included")

sv = SmartVehicle()
sv.engine_type()  # From Engine
sv.wheels()       # From Vehicle
sv.navigation()   # From GPS
sv.features()     # Own method
```
 
----
### Realtime examples 

**Single Inheritance**
> Base Class: User  

> Derived Class: Customer

```python
A general User class contains login and logout functionality. The Customer class inherits these features and adds shopping cart operations.
```

**Multiple Inheritance**
```python
Class A: Camera
Class B: Phone
Derived Class: CameraPhone

Scenario:
A CameraPhone needs features from both Camera (like capture, zoom) and Phone (call, text).
```

**Multilevel Inheritance**
```python
Base Class: Animal
Intermediate Class: Mammal
Derived Class: Dog

Scenario:
Animal defines basic behaviors, Mammal adds warm-blooded behavior, and Dog adds barking and loyalty behavior.
```

**Hierarchical Inheritance**
```python
Base Class: Employee
Derived Classes: Manager, Developer, Designer

Scenario:
Employee has basic methods like clock_in() and get_salary(), while Manager has assign_task(), Developer has write_code(), and Designer has create_mockup().
```

**Hybrid Inheritance**
```python
Base Class 1: Person
Base Class 2: Skills
Intermediate Class: Employee(Person)
Derived Class: Engineer(Employee, Skills)

Scenario:
An Engineer needs to inherit both identity info (Person) and technical abilities (Skills) while also having general Employee behaviors like attendance and salary calculation.
```

---
## 🔍 Encapsulation in Python
> Encapsulation means hiding an object’s internal data and only exposing what’s necessary through methods. 
- It bundles data and functions together in a class and restricts direct access to protect the object’s state.
- Encapsulation bundles data (attributes) and methods (functions) that operate on that data into a single unit — a class.
- It restricts direct access to some of the object's components, which means internal representation of an object is hidden from the outside.
- This protects object integrity by preventing external code from modifying internal states unexpectedly.

**🔹 Why use it?**
- 🛡️ Protects data from accidental changes
- 🔐 Controls access via getters/setters
- 🔧 Makes maintenance easier
- 🔒 Secures sensitive information

**🔹 How is Encapsulation Implemented in Python?**
> Python uses naming conventions to indicate the intended level of access:

| Access Modifier | Prefix        | Meaning                          | Accessibility              |
| --------------- | ------------- | -------------------------------- | -------------------------- |
| Public          | No underscore | Accessible everywhere            | Accessible from outside    |
| Protected       | Single `_`    | Intended for internal use only   | Accessible but discouraged |
| Private         | Double `__`   | Name mangling for limited access | Not accessible directly    |


**🔹 Example**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public attribute
        self.__balance = balance      # Private attribute (encapsulated)
    
    # Getter method to access balance
    def get_balance(self):
        return self.__balance
    
    # Setter method to update balance with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Usage
account = BankAccount("Ram", 1000)
print(account.owner)           # Access public attribute
print(account.get_balance())   # Access private attribute via getter

# Trying to access private attribute directly will fail
# print(account.__balance)     # AttributeError

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)         # Invalid withdrawal
```

**Name Mangling**
- Private attributes like __balance are internally renamed by Python to _ClassName__balance to avoid name clashes.
- This makes direct access difficult but not impossible (discouraged though).
```python
print(account._BankAccount__balance)  # Works but not recommended
```

### 🔹 What is @property?
- @property allows you to define methods that behave like attributes.
- It lets you control access to private attributes with getter, setter, and deleter methods without changing how you access the attribute.
- This improves code readability and keeps the interface clean.


```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected attribute (single underscore)
    
    @property
    def balance(self):
        """Getter method to access the balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """Setter method to update balance with validation."""
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self._balance = amount
            print(f"Balance updated to: ${self._balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Usage
account = BankAccount("Bob", 1000)
print(account.owner)        # Public attribute
print(account.balance)      # Access balance via @property (getter)

account.deposit(200)
account.withdraw(500)

# Using setter to update balance (not typical but allowed)
account.balance = 1500
print(account.balance)

# Trying to set negative balance (will trigger validation)
account.balance = -100
```

**🔹 How It Works**
- balance method decorated with @property acts as a getter.
- balance method decorated with @balance.setter acts as a setter.
- Accessing account.balance calls the getter internally.
- Assigning account.balance = value calls the setter internally.
- The private attribute _balance is protected by convention (single underscore).


---

## 🔑 Abstraction 
- Abstraction is one of the key principles of Object-Oriented Programming (OOP)
- It means hiding complex implementation details and showing only the essential features of an object.
- In Python, abstraction is achieved using:
    - Abstract Base Classes (ABCs)
    - The abc module (abstract base class)
    - @abstractmethod decorator

**Why Use Abstraction?**
- To hide unnecessary implementation logic
- To define a blueprint for derived classes
- To enforce a certain structure in child classes

**Example-1:**
```
Different payment methods (credit card, PayPal, UPI, etc.) should all support a pay() method, but the internal implementation will vary. 
As a developer, you only want to interact with the pay() method, without worrying about how each method works internally.
```

```python
from abc import ABC, abstractmethod

# Abstract class
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class 1
class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

# Concrete class 2
class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Concrete class 3
class UPIPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Processing UPI payment of ${amount}")

# Real-time usage
def make_payment(processor: PaymentProcessor, amount):
    processor.pay(amount)

# Driver code
payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment3 = UPIPayment()

make_payment(payment1, 150)
make_payment(payment2, 75)
make_payment(payment3, 50)
```

**Example-2**
```
When you use an ATM, you perform actions like:
    - withdraw_money()
    - check_balance()

You don’t care about how it connects to the bank server, verifies your PIN, or deducts balance — you only see simple options. 
This is abstraction.
```

```python
from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw_money(self, amount):
        pass

# Concrete class
class HDFCBankATM(ATM):
    def __init__(self):
        self._balance = 5000

    def check_balance(self):
        print(f"Your balance is ₹{self._balance}")

    def withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("Insufficient balance!")

class ICICIBankATM(ATM):
    def __init__(self):
        self._balance = 3000

    def check_balance(self):
        print(f"Your balance is ₹{self._balance}")

    def withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("Insufficient balance!")

# Function to interact with any ATM
def perform_transaction(atm: ATM):
    atm.check_balance()
    atm.withdraw_money(1000)

# Driver code
atm1 = HDFCBankATM()
atm2 = ICICIBankATM()

perform_transaction(atm1)
perform_transaction(atm2)
```

---
## 🧠 Polymorphism
- Polymorphism means "many forms" — it allows objects of different classes to be treated as objects of a common super class. 
- In Python, this means different classes can define the same method name with different behavior.

**🔑 Why Use Polymorphism?**
- Promotes flexibility and reusability
- Supports code generalization
- Makes systems extensible and maintainable

**✅ Types of Polymorphism in Python**
| Type                       | Description                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **Duck Typing**            | If an object behaves like a duck, treat it like a duck.                                    |
| **Operator Overloading**   | Same operator behaves differently for different types.                                     |
| **Method Overriding**      | Subclass provides a specific implementation of a method already defined in its superclass. |
| **Function Overloading**\* | Not natively supported; can be simulated.                                                  |

> *Python doesn’t support function overloading like C++/Java but can be mimicked using default args or *args.

**🔸 Example 1: Duck Typing (Real-World: File Reader)**
```python
class PDFReader:
    def read(self):
        print("Reading PDF file...")

class WordReader:
    def read(self):
        print("Reading Word document...")

def open_file(reader):
    reader.read()  # Polymorphic behavior

# Real-time usage
pdf = PDFReader()
doc = WordReader()

open_file(pdf)
open_file(doc)  
```

**🐥 Why Is It Called Duck Typing**

- The term duck typing comes from the phrase:

> “If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.”

- In programming — especially in Python — it means:

> "If an object has the methods and behaviors we expect, we can use it without caring about its actual class/type."

- ✅ Duck Typing = Behavior Over Type

**🔍 Example Without Duck Typing**
```python
def start_engine(vehicle):
    if isinstance(vehicle, Car):
        vehicle.start()
    elif isinstance(vehicle, Bike):
        vehicle.start()
```

**Example With Duck Typing**
```python
def start_engine(vehicle):
    vehicle.start()  
```

**🔧 Real-World Analogy**
- Imagine you're plugging in a USB device:
    - You don’t care if it’s a mouse, keyboard, or pen drive.
    - As long as it supports the USB protocol (same interface), it just works.
- That’s duck typing — you're trusting the interface, not checking the identity.

---

**🔸 Example 2: Method Overriding**
```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Real-time usage
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.make_sound()  # Polymorphic call
```
> ✔ Different objects use the same method name but with different implementations.


**🔸 Example 3: Operator Overloading**
```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

result = c1 + c2  # Same '+' operator behaves differently
print(result)
```


**🔸 Example 4: Polymorphism with Abstract Classes**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
```

**Example 5:**
```
🎯 Scenario:
Your chatbot needs to respond to different user intents, such as:
    Greeting
    Weather inquiry
    Booking request
    Goodbye

Each intent has different logic, but your system should treat them in a polymorphic way — by calling the same method (e.g., handle()).

```

```python
# Base Intent class
class Intent:
    def handle(self, message):
        raise NotImplementedError("Subclasses must implement this method")

# Concrete Intent 1
class GreetIntent(Intent):
    def handle(self, message):
        return "Hello! How can I assist you today?"

# Concrete Intent 2
class WeatherIntent(Intent):
    def handle(self, message):
        return "Sure, let me check the weather for your location."

# Concrete Intent 3
class BookingIntent(Intent):
    def handle(self, message):
        return "I'd be happy to help you book an appointment. Please provide the date."

# Concrete Intent 4
class GoodbyeIntent(Intent):
    def handle(self, message):
        return "Goodbye! Have a great day!"

# Polymorphic intent processor
def process_intent(intent: Intent, message: str):
    response = intent.handle(message)
    print(f"Bot: {response}")

# Simulating chatbot messages
intents = [GreetIntent(), WeatherIntent(), BookingIntent(), GoodbyeIntent()]
messages = ["Hi", "What's the weather?", "Book a flight", "Bye"]

for intent, msg in zip(intents, messages):
    print(f"User: {msg}")
    process_intent(intent, msg)
    print()
```

--- 
## 🧠 Operator Overloading
- Operator Overloading means giving custom behavior to standard operators (+, -, *, ==, etc.) for user-defined classes.

- In Python, you can redefine what these operators do using special methods (also called magic methods or dunder methods, e.g., __add__, __eq__).


**Overloading + for a Custom Class**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2
print(result)
```

**🔧 Common Operator Overloading Methods in Python**
| Operator | Method                 | Example    |
| -------- | ---------------------- | ---------- |
| `+`      | `__add__(self, other)` | `a + b`    |
| `-`      | `__sub__()`            | `a - b`    |
| `*`      | `__mul__()`            | `a * b`    |
| `/`      | `__truediv__()`        | `a / b`    |
| `==`     | `__eq__()`             | `a == b`   |
| `<`      | `__lt__()`             | `a < b`    |
| `>`      | `__gt__()`             | `a > b`    |
| `[]`     | `__getitem__()`        | `obj[key]` |
| `len()`  | `__len__()`            | `len(obj)` |


**⚠️ Note**
Operator overloading should be:
   - Intuitive (do what the operator normally means)
   - Consistent (don’t confuse users)

- Example of bad overloading:
```python
def __add__(self, other):
    return self.name + str(other.age)  # Confusing!
```
---
## Method Resolution Order (MRO) in Python
- MRO (Method Resolution Order) defines the order in which Python looks for methods in a hierarchy of classes (especially in multiple inheritance).
- It determines which method is called when you invoke a method on an instance.
- Ensures consistent and predictable method lookup.

**Why is MRO important?**
- In single inheritance, method lookup is straightforward (parent → grandparent).
- In multiple inheritance, multiple parents can have the same method name — MRO decides which parent's method runs.
- Helps avoid ambiguity and the “diamond problem.”

**How Python computes MRO?**
- Python uses C3 Linearization Algorithm (also called C3 superclass linearization) to compute MRO.
- MRO lists classes in the order they are checked when looking for a method.

**Checking MRO in Python**
- Use the special attribute or method:
```python
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())
# or
print(C.__mro__)
```

**Example of MRO in Multiple Inheritance**
```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()
print(D.mro())
```

> object is the root of all classes in Python; always last in MRO.

