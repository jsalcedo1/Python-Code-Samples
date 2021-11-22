# Jaime S.
# 11/16/2021
# National Louis University
# This program will check whether the sum of two inputs( Values/whole numbers) entered by the user
# are greater than, less than, or equal to 10.
# Important information: This program will only work with whole numbers, it will not work with decimals.

a = int(input("Enter value/number: "))  # User input
b = int(input("Enter another value/number: "))  # User input
c = 10  # This number can be changed. However, it is set to check 10.
if a + b > c:    # if the values a + b given by the user's input is greater than 10...
    print("Number is greater than 10")  # It will print this.
if a + b < c:    # if the values a + b given by the user's input is less than 10...
    print("Number is less than 10")  # It will print this...

if a + b == c: # If the values a + b given by the user's input is equal to 10...
    print("The number is equal to 10")  # It will print this
