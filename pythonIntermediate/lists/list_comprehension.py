# It's a way to make lists quickly, sometimes based on lists that already exist

my_original_list = [35, 24, 62, 52, 30, 30, 17]
another_original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "...", 99]

my_list = [i for i in my_original_list]
another_list = [i for i in range(100)]

print(my_list)

print(another_original_list)
print(another_list)

another_list = [i+1 for i in range(10)]

print(another_list)

another_list = [i*2 for i in range(10)]

print(another_list)

def add_five(number):
    return number+5

another_list = [ add_five(i) for i in range(10)]

print(another_list)