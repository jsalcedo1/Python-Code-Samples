# Jaime S.
# 11/16/2021
# National Louis University
# This program will check if the value of 5 exists in the list. It will print "five is in the list" only if the value
# of 5 is in the list. If the value of 5 is not in the list, it will print " five is not in the list"
# Important information: A simple program that will check whether the value of 5 is in the list.
# You can modify the values that are in the list, the same as the value that you want the program to check if
# its in the list.

list = [1, 2, 3, 4, 5]           # Assigns as a list of [1, 2, 3, 4, 5] values
print('This is your list', list)
value = 5  # Value is assigned as 5 (You can change the value that you want the program to check)

if value in list:                # Will check if the value is in the list
    print(value, "Five is in the list")      # If the value is in the list then it will print "is in the list"
elif value not in list:          # Will check if the value is not in the list
    print(value, "Five does not exist in the list")  # If the value is not in the list it will print"is not in the list"

