currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)

'''
Edited by: Jaime S.
10/22/2021

Corrections: 
============================================================================================
Line 2 has 1 error

Line 2:Syntax Error: Missing a closing parenthesis ), a closing parenthesis should be added after wait")

=============================================================================================
Line 4 has 2 errors

Line 4: Syntax Error: Wrong usage of underscores and wrong interpretation, 
(current_time_int) should not end with int and should not have underscores instead it should
be expressed as (currentTimeStr)
=============================================================================================
Line 5 has 2 errors

Line 5: Syntax Error: Wrong usage of underscores and wrong interpretation, (wait_time_int)
should not end with int and should not have underscores instead it should be expressed as (waitTimeStr)
=============================================================================================
Line 8 has 1 error

Line 8: Wrong usage of underscores, the underscores should be removed
=============================================================================================
'''
