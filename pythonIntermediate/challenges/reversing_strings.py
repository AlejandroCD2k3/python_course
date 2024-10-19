"""
REVERSING STRINGS
Create a program that reverses the order of a text string 
without using built-in language functions that do it automatically.
- If we pass "Hello world" to it, it would return "dlrow olleH"
"""

def reverse_string(string):
    reversed_string = ""

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string

print(reverse_string("Hello"))