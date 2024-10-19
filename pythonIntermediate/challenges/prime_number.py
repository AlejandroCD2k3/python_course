import math

"""
IS IT A PRIME NUMBER?
Write a program that checks whether a number is prime or not.
Once done, print the prime numbers between 1 and 100.
"""

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number))+1):
        if(number%i==0):
            return False
        
    return True
        

def print_primes_until(top_limit):
    for i in range(1, top_limit+1):
        if is_prime(i):
            print(i)

print_primes_until(100)