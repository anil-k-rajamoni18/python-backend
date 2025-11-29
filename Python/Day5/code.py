class Animal:
    def speak(self):
        return "Unknown sound"

class Dog(Animal):
    def speak(self):
        # Overriding the parent method
        return "Bark"
    

d = Dog()
print(d.speak())
print(Dog.mro())