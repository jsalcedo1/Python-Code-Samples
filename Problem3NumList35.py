# Jaime S.
# 11/24/2021
# National Louis University
# Simple program that will ask the user input and then will append each number entered to a list and add it together.
# It will stop if the numbers entered are greater than 100.
l = []

while sum(l) < 100:
    n = int(input("Please choose a number: "))
    l.append(n)
print(l)
