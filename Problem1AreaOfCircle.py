# Jaime S.
# 11/9/2021
# This program asks for user's input or circle's radius and gives the output of the circle's area
# Helpful Information: No additional info, just a simple and easy program to use & calculate the area of a circle
import math                     # requests math module


def area_of_circle(r):          # Defines the area of a circle as radius
    area = (r ** 2) * math.pi   # Formula used to calculate its area
    return area                 # exits function and runs the rest of the code


radius = int(input("Enter circle's radius: "))                 # Asks user to type the circle's radius
print("The area of your circle is:", area_of_circle(radius))   # Displays the user's area of a circle


