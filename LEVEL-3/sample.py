class Person:
    '''
        This is Person Class create object by taking name and age
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Alice", 30)
print(p.__dict__)  # {'name': 'Alice', 'age': 30}
print(p.__class__) # <class '__main__.Person'>
print(Person.__doc__) # Prints class docstring if available

print(dict.__doc__)