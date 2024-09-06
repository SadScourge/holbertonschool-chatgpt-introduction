#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculates the factorial of a given non-negative integer using recursion.

	Parameters:
	n (int): A non-negative integer whose factorial is to be calculated.

	Returns:
	int: The factorial of the given integer n.
		 If n is 0, returns 1 since the factorial of 0 is defined as 1.
		 For n > 0, returns n multiplied by the factorial of (n-1).
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Retrieves the first command-line argument, converts it to an integer,
# calculates its factorial, and prints the result.
f = factorial(int(sys.argv[1]))
print(f)
