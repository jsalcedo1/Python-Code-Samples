# Jaime S.
# 11/06/2021
# This program will print 10 random integers.
# Helpful information: Very simple program to use to generate 10 random whole numbers.

import random                                     # requests access to the random module

for i in range(10):                              # will repeat over the sequence/order of 10 integers
    print(random.randrange(25, 35), end=' ')     # 10 integers within range of 25 & 35, end is a space between them.

