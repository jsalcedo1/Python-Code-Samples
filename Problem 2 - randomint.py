# Jaime S.
# 11/06/2021
# This is a program will print a random odd integer between 0 and 100.
# Helpful information: Very simple program to use to generate a random odd whole number.
import random                               # requests access to the random module

num = 0                                     # associates the name number with 0
while num % 2 == 0:                         # it will print an odd integer no matter what
    num = random.randrange(0, 100)          # range between 0 and 100

print(num)                                  # will print a random odd integer





