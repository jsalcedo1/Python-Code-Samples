# Jaime S.
# 11/06/2021
# This program will print an approximation float/decimals for pi and will show pi as value/decimals.
# Helpful information: Simple program to show the estimate for pi & show the symbol pi as decimals
import math                                         # requests access to the math module


def estimate_pi(terms):                             # defines the term pi
    ans = 0.0                                       # ans statement will store decimals
    for k in range(terms):                          # same type of variables
        ans += (-1.0 / 3.0) ** k / (2.0 * k + 1.0)  # conversion formula
    return math.sqrt(12) * ans                      # will square root and multiply the answer


print(estimate_pi(21))                              # prints the estimate of pie
print(math.pi)                                      # prints pi as decimals
