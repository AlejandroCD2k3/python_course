# SyntaxError: Code doesn't follow grammar rules of the programming language

    #print "Hello World"
    
print("Hello World")

"""
Python expects:

Lexem   Token

print   keyword
(       special_char
"       special_char
HW      string
"       special_char
)       special_char

"""

# NameError: Calling a not defined statement

    # print(name)

name = "Allison"
print(name)

# IndexError: It occurs when Python tries to access an index that is out of bounds in a data collection (like a list or tuple).

my_list = ["Python","Java","Cobol","Swift","Pearl"]
print(my_list[2])

    # print(my_list[7])

# ModuleNotFoundError/AttributeError: It occurs when we try to import a module that doesn't exist or is not specified correctly.

    # import maths

    # print(maths.sqrt(16))

import math

print(math.sqrt(16))

    # print(math.PI)    PI in uppercase doesn't exist in math module

print(math.pi)

# KeyError: It happens when we try to call a key that doesn't exist in a dictionary

my_dictionary = {"Name":"Michael", "Last name":"Jefferson", "Age":22, 1:"Python"}

    # print(my_dictionary["Pet"])

print(my_dictionary["Age"])

# TypeError: It occurs when we pass an argument of the wrong type to a function.

    # print(2+"2")

print(2+2)
print("2"+"2")

# ImportError: It occurs when we try to import a module or a specific function from a module, but it doesn't exist.

    # from math import PI

from math import pi

# ValueError: It occurs when a function receives an argument of the right type, but with an inappropriate value.

    # print(int("Hello"))   Hello can't be converted to a int

print(int("12"))

# ZeroDivisionError: We can't divide by 0!

    # print(4/0)