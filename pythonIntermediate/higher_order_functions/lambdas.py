add_values = lambda first_value, second_value: first_value + second_value

print(add_values(2,5))

#-----------------------------------------------------

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))

print(squares)