# Single Inheritance
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Multiple Inheritance
class Person:
    def greet(self):
        print("Hello!")

class Employee:
    def job(self):
        print("Employee job")

class Manager(Person, Employee):
    def manage(self):
        print("Managing team")

# Multilevel Inheritance
class Shape:
    def area(self):
        print("Shape area")

class Square(Shape):
    def area(self):
        print("Square area")

if __name__ == "__main__":
    # Single inheritance example
    dog = Dog()
    dog.sound()

    # Multiple inheritance example
    manager = Manager()
    manager.greet()
    manager.job()

    # Multilevel inheritance example
    square = Square()
    square.area()