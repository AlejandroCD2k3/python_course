number_one= 5
number_two = 1
number_two = "1"

"""
if type(number_two) == int:
    print(number_one+number_two)
else:
    print("Didn't comply")
"""

try:
    print(number_one + number_two)
except TypeError as error:
    print("A error has ben produced")
    print(error)
except Exception as exception:
    print("There's a exception")
    print(exception)
else:
    print("Excecution continues normally")
finally:
    print("Execution still going")
