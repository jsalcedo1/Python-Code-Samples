#!/usr/bin/env python
#Author: Jaime Salcedo
#Date: Sep, 28, 2021
#Purpose of the program:
#This program is to convert Kilometers Per Hour(KMPH) into Miles Per Hour (MPH), which are entered by the user.

'''Author: Jaime Salcedo
    Date: Sep 28, 2021
    Purpose of the program:
    This is to convert Kilometers Per Hour(KPH) into
    Miles Per Hour(MPH), which are entered by the user.'''

kmh = int(input("Enter km/h: "))
mph =  0.6214 * kmh
print("Speed:", kmh, "KM/H = ", mph, "MPH")
