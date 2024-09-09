#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # This line was missing
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
except ValueError as e:
    print(e)
    sys.exit(1)

f = factorial(number)
print(f)

