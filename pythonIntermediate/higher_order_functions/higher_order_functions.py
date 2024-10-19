def add_one(value):
    return value + 1

def add_five(value):
    return value + 5

def add_values_plus_one(first_value, second_value):
    return add_one(first_value + second_value)

def add_values_plus_one_alternative(first_value, second_value, f_add_one):
    return f_add_one(first_value + second_value)

print(add_values_plus_one(5,2))
print(add_values_plus_one_alternative(5,2,add_one))
print(add_values_plus_one_alternative(5,2,add_five))

# --------------------- CLOSURES ---------------------

def add_ten():

    def add(value):
        return value + 10

    return add

add_closure = add_ten()
print(add_closure(5))
print((add_ten())(5))

# --------------------- BUILT IN ---------------------

def multiply_two_times(number):
    return number*2

numbers = [2, 5, 10, 21, 3, 30]

print(list(map(multiply_two_times ,numbers)))

print(list(map(lambda number: number*2, numbers)))

#numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))

print(squares)

# --------------------- FILTER ---------------------

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))

print(list(filter(lambda number: number > 10, numbers)))

# --------------------- REDUCE ---------------------

from functools import reduce

# [2, 5, 10, 21, 3, 30]

def add_values(first_value, second_value):
    print(f"{first_value} + {second_value}")
    return first_value + second_value

print(reduce(add_values, numbers))