import timeit

""" 
THE FIBONACCI SEQUENCE Write a program that prints the first 50 numbers 
of the Fibonacci sequence starting from 0.

The Fibonacci series consists of a sequence of numbers in which 
the next number is always the sum of the previous two. 
0, 1, 1, 2, 3, 5, 8, 13... 
"""



def fibonacci_sequence_1(sequence_lenght):
    first_number = 0
    second_number = 1

    for i in range(sequence_lenght-1):
        
        if i < 1:
            print(f"{first_number}\n{second_number}")
        else:
            sequence = first_number + second_number

            first_number = second_number
            second_number = sequence 




def fibonacci_sequence_2(sequence_lenght):

    fibonacci_list = [0,1]

    for i in range(2, sequence_lenght):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    print(fibonacci_list)

execution_time = timeit.timeit(lambda: fibonacci_sequence_1(50), number=1)
print(f"Excecution time: {execution_time} seconds")

execution_time = timeit.timeit(lambda: fibonacci_sequence_2(50), number=1)
print(f"Excecution time: {execution_time} seconds")
