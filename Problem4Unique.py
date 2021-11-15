# Jaime S.
# 11/9/2021
# This is a program that will take the list (1,3,3,3,6,2,3,5) and will provide a new list.
# Helpful information: No additional information, you could simply run the code and expect to see the new list.
def unique_list(list):  # Defines unique list as list
    x = []  # Variable x is assigned as list
    for a in list:  # Uses a loop to determine numbers within a list
        if a not in x:   # if the number is not within the list it will...
            x.append(a)  # Add a single existing item to the list
    return x    # exits function and runs the rest of the code


print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))  # Prints the new modified list


