""" 
THE FAMOUS "FIZZ BUZZ": Write a program that prints to the console 
(using print) the numbers from 1 to 100 
(inclusive and with a line break between each print), replacing the following:

Multiples of 3 with the word "fizz."
Multiples of 5 with the word "buzz."
Multiples of both 3 and 5 with the word "fizzbuzz." 
"""

multiple_of_3 = "fizz"
multiple_of_5 = "buzz"

for i in range(1, 101):
    
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: " + multiple_of_3 + multiple_of_5)
    elif i % 3 == 0:
        print(f"{i}: " + multiple_of_3)
    elif i % 5 == 0:
        print(f"{i}: " + multiple_of_5)
    else:
        print(i)
