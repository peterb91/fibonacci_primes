#!/usr/bin/python3

def fib(n):
    """ Return (n+1)th element of fibonacci sequence"""

    if not isinstance(n, int) or n < 0:
        return "Input must be not negative integer"
    elif n < 2:
        return n
    elif n > 1:
        return fib(n-2) + fib(n-1)

def is_prime_number(num):
    """Return True if num is prime and False if num is not prime or input non integer"""

    if not isinstance(num, int) or num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

##### Fibonacci Prime Numbers implementation #####

def prime_fibonacci_numbers(i):
    """Return i-element list of primes from fibonacci sequence starting from the beginning of the sequence"""
    result = []
    if not isinstance(i, int) or i < 0:
        return "Input must be not negative integer"
    if i == 0:
        return result
    for fib_num in [fib(n) for n in range(20)]:
        if is_prime_number(fib_num):
            result.append(fib_num)
        if len(result) == i:
            break
    return result

print(prime_fibonacci_numbers(0))
print(prime_fibonacci_numbers(3))
print(prime_fibonacci_numbers(4))
print(prime_fibonacci_numbers(5))
