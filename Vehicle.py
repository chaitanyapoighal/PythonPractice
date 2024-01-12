class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (Subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (Subclass)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Call the speak method for each instance
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())
