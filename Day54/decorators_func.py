#Add
def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2

#substract
def subtract(n1, n2):
    """Subtracts two numbers together"""
    return n1 - n2

#multiply
def multiply(n1, n2):
    """Multiplies two numbers together"""
    return n1 * n2

#divide
def divide(n1, n2):
    """Divides two numbers together"""
    return n1 / n2



#--------------------------------
#first-class objects , can be passed around an arguments e.g. int/string/float/...

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 3, 4)
# print(result)
#

#---------------------------------------------------------
#nested Function

# def outer_function():
#     print("outer function")
#     def nested_function():
#         print("nested function")
#
#     nested_function()
#
# outer_function()

#--------------------------------
# Function can be returned from other function

# def outer_function():
#     print("outer function")
#     def nested_function():
#         print("inner function")
#
#     return nested_function
#
# inner_function = outer_function()
#
# inner_function()

# ------------------------------------
"""python decorator"""
import time

def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        #do something before
        func()
        func()
        "etc func repeat"
        #do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello, world!")

@delay_decorator
def say_bye():
    print("Bye, world!")

def greeting():
    print("How are you?")

#1 methode
say_bye()
#2 methode
decorated_function = delay_decorator(greeting())
decorated_function()