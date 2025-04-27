# Assignment 1: Using self

class Student:
    def __init__(self, name, marks):
        self.name = name        # using self to set instance variables
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage:
student1 = Student("Muneeba", 21)
student1.display()

# Assignment 2: Using cls

class Counter:
    count = 0  # Class variable to keep track of number of objects

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()

# Assignment 3: Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand  

    def start(self):
        print(f"The {self.brand} car has started.")  

# Example usage:
my_car = Car("Toyota")

# Accessing public variable
print("Brand of the car:", my_car.brand)

# Accessing public method
my_car.start()


# Assignment 4: Class Variables and Class Methods

class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Example usage:

# Creating two instances
acc1 = Bank("Meezan")
acc2 = Bank("Nayapay")

# Display details before changing bank name
acc1.display()
acc2.display()

# Changing the bank name using class method
Bank.change_bank_name("Allied Bank")

# Display details after changing bank name
acc1.display()
acc2.display()


# Assignment 5: Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage:
result = MathUtils.add(5, 7)
print("Sum:", result)


# Assignment 6: Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger object has been created!")

    def __del__(self):
        print("Logger object has been destroyed!")

# Example usage:
logger1 = Logger()
del logger1

# Assignment 7: Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            
        self._salary = salary        
        self.__ssn = ssn             

# Example usage:
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing public variable
print("Public - Name:", emp.name)  
# Accessing protected variable
print("Protected - Salary:", emp._salary) 

# Accessing private variable
try:
    print("Private - SSN:", emp.__ssn)  
except AttributeError as e:
    print("Error accessing private variable __ssn:", e)

print("Private (via name mangling) - SSN:", emp._Employee__ssn)


#Assignment 8

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject

# Example usage
teacher1 = Teacher("Mr. Smith", "Mathematics")
print(f"Name: {teacher1.name}")
print(f"Subject: {teacher1.subject}")



#assignment 9 
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(5, 3)
print(f"Area of Rectangle: {rect.area()}")



#assignment 10
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Example usage
my_dog = Dog("Buddy", "Goldenbox")
my_dog.bark()

#ssignment 11
class Book:
    total_books = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(f"Total books: {Book.total_books}")

#assignment 12
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")


#assignment 13
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        self.engine.start()  # Using Engine's method

# Example usage
my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()

#assignment 14
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.department_name}")
        for emp in self.employees:
            print(f"- {emp.name}")

# Example usage
emp1 = Employee("Alice")
emp2 = Employee("Bob")

dept = Department("HR")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
 

 #assignment 15
 class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):  # D inherits from B and C
    pass

# Example usage
d = D()
d.show()

# Let's also check the MRO
print(D.__mro__)


#assignment 16
# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Function with decorator
@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()


#assignment17
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
person = Person("Alice")
print(person.greet())  # Output: Hello from Decorator!


#assignment18
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
product = Product(100)

# Get the price
print(product.price)  

# Set the price
product.price = 120  
print(product.price)  

# Set an invalid price
product.price = -50  

# Delete the price
del product.price  

#assignment 19
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Example usage
multiplier = Multiplier(5)

# Test with callable()
print(callable(multiplier))  # Output: True

# Call the object like a function
result = multiplier(10)
print(result)  # Output: 50


#assignment 20

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print("Age is valid.")

# Example usage with try...except
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")

#assignment 21

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # The iterator is the object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        else:
            self.current -= 1
            return self.current + 1  # Return the current number before decrementing

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)


