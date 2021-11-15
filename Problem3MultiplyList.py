# Jaime S.
# 11/9/2021
# This is a program that will multiply all values in the list using the transversal method
# Helpful information: No additional info, just a simple and easy to use program to multiply all values
# you put on the list in this case (5,2,7,-1)
def multiplyList(list):  # Defines multiply list as list
    multiple_number = 1  # By default it should be set to 1 if you want to multiply all numbers as a sequence(1 by 1)
    for x in list:    # Repeats the multiplication for all numbers on the list
        multiple_number = multiple_number * x  # Does the math for you (multiplication)
    return multiple_number  # Exits function and runs the rest of the code


# Executable code
List = [5, 2, 7, -1]  # List of given numbers (these can be modified manually)
print(multiplyList(List))  # Will print the total of the numbers multiplied in the list
