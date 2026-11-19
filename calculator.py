"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Divided by zero")
    return b / a

def logarithm(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithms require positive integers")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def hypotenuse(a,b):
    return (a**2 + b**2)**0.5

def square_root(a):
    if a < 0:
        raise ValueError("Square root must be positive")
    return a**0.5
