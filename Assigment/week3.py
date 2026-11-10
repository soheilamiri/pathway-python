##### Problem 1 ######
product = lambda x, y: x * y
print(product(5, 6))
30

##### Problem 2 ######
#import math module
import math
# Define a function named circle_area that accepts the radius of as circle as an argument for calculation
def circle_area(radius):
    return math.pi * (radius ** 2)
#print the area
print(circle_area(10))

##### Problem 3 ######
# Define a function named calculator that takes three arguments:
# num1: the first number
# num2: the second number
# op: the operation to perform ('add', 'sub', 'multi', 'div')
def calculator(num1, num2, op):
# Check if the operation is addition
    if op == 'add':
        return num1 + num2
# Check if the operation is subtraction
    elif op == 'sub':
        return num1 - num2
# Check if the operation is multiplication
    elif op == 'multi':
        return num1 * num2
# Check if the operation is division
    elif op == 'div':
# Check to avoid division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Warrning: input number is wrong, Cannot divide by zero."
# Handle any unknown operation
    else:
        return "Invalid operation"
# test: divide 2 by 5 using 'div'
print(calculator(2, 5, 'div'))

##### Problem 4 ######
# Define class
class Rectangle:
    # defining object
    def __init__(self, length, width):
        # Call a descriptive method to initialize values
        self.set_dimensions(length, width)

    # A more meaningful method name to update or set dimensions
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

    # Define a method to calculate and return the area
    def area(self):
        return self.length * self.width

#test: create an instance of Rectangle with length=5 and width=10
r = Rectangle(5, 10)
# print the result
print(r.area())

##### Problem 5 ######
#code compatible with python 3.7+
from dataclasses import dataclass

# Base class using dataclass
@dataclass
class Shape:
    name: str
    length: float

    def area(self):
        return 0

# Subclass inheriting from Shape
@dataclass
class Square(Shape):
    # Automatically inherits 'name' and 'length' attributes and __init__
    def area(self):
        print("The area is:")
        return self.length * self.length

    def describe(self):
        return f"This is a: {self.name}"

# --- Run test ---
s = Square('square', 5)
print(s.area())
print(s.describe())
