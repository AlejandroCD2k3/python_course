my_typed_variable : str = "My typed String variable"
print(type(my_typed_variable))

my_typed_variable = 5
print(type(my_typed_variable))

# ---------------------------------------------------------

another_typed_variable: int = "Another typed variable"
print(type(another_typed_variable))

# ---------------------------------------------------------

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("Michael",12))

# print(get_name_with_age(15,12)) TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ---------------------------------------------------------

from typing import List


def process_items(items: List[str]):
    for item in items:
        print(item)

process_items(["a","b","c","d","...","z"])
process_items([1,2,3,4,5])