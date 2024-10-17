# ------------------- WHILE -------------------

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Optional
    print("My condition is greater or equal to 10")

# ------------------- FOR -------------------

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

#------

for element in my_list:
    print(element)
    if(element > 40):
        break
else:
    print("Bucle has finalized")

#------

for digit in range (0,10):
    print(digit)