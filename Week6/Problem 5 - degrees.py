# Jaime S.
# 11/06/2021
# This program will convert radians to degrees using the formula n x 180 / pi.
# Helpful information: Very simple program to use and convert radians to degrees.


from math import pi                          # Requests module

n = int(input("Input radians: "))            # Asks the user to input its answer in radians
print("==============================")      # Made simply to organize
print("This is the result in degrees:")      # This is the formula used to convert radians to degrees
print(n * 180 / pi)

