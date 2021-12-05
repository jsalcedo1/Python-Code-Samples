# Jaime S.
# 11/24/2021
# National Louis University
# Simple program  that will print a counter of 0 to 50, it will print it by 10's.
count = 0  # counter set to 0
tens = []  # tens is assigned as a list
while count < 51:  # installs a counter of 0 to 50
    if count % 10 == 0:  # if divisible by 10
        tens.append(count)  # appends the count by 10's
    count += 1
print("Tens:", tens)  # shows results
