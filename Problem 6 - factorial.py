# Jaime S.
# 11/06/2021
# This is a program that will asks the user to input an integer and the program will simply do the math for it.
# Helpful information: Very simple program to factor a desired number.

import math                               # imports the math module


def factorial():                          # defines factorial function
    n = int(input("Enter a number"))      # asks user to enter a number
    print("Factorial of number ", math.factorial(n))   # prints the number


factorial()
