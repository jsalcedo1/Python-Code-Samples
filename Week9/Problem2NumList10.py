# Jaime S.
# 11/24/2021
# National Louis University
# Simple program that will print numbers 0-10 on each iteration the loop will append the current value and increase it
# by 1 & the counter will stop once it has reached a number greater than 10
l = []  # list called l
counter = 0  # counter
while counter <= 10:  # if counter is less than or equal to 10
    l.append(counter)  # will append the current value
    counter += 1  # counter increases by 1
print(l)
