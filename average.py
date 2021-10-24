#!/usr/bin/env python
#Author: Jaime Salcedo
#Date: Sep, 28, 2021
#Purpose of the program:
#This program is to find the average of three values, which are entered by the user.


'''Author: Jaime Salcedo
    Date: Sep 28, 2021
    Purpose of the program:
    This is to find the average of three values, which are entered
    by the user.'''
 
round1 = int(input("Enter score for round 1: "))
round2 = int(input("Enter score for round 2: "))
round3 = int(input("Enter score for round 3: "))
average = (round1 + round2 + round3) / 3
print ("the average score is: ", average)
