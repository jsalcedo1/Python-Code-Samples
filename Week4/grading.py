# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 89.5:
    letter_grade = "A"
elif avg >= 80 and avg < 89.5:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")

"""
Edited by: Jaime S.
10/22/2021

Corrections: 
==========================================================
Line 24 has 2 errors

Line 24: Syntax Error: Missing an integer int, an integer int should be added
Line 24: Syntax Error: Missing a parenthesis (, a parenthesis ( should be added
==========================================================
Line 26 has 2 errors

Line 26: Syntax Error: Wrong interpretation, exam_3 should be written in letters exam_three
Line 26: Syntax Error: Wrong interpretation, str should be removed, and an integer int should be added
============================================================
Line 28 has 2 errors

Line 28: Syntax Error: Missing a comma , , a comma should be added , 
Line 28: Syntax Error: Missing a comma , , a comma should be added ,
============================================================
Line 30 has 1 error

Line 30: Syntax Error: Missing a letter S, the letter S should be added to grade
============================================================
Line 33 has 1 error

Line 33: Syntax Error: Missing letter S,  letter S should be added to grade
============================================================
Line 35 has 1 error 

Line 35: Logic Error:  Giving wrong grade I changed 90 to 89.5
============================================================
Line 37 has 2 error

Line 37: Syntax Error: Missing a colon :, a colon should be added :
Line 37: Logic Error:  Giving wrong grade I changed 90 to 89.5
============================================================
Line 40: Syntax Error: Wrong single quote ' , a double quote  " should be added instead 
============================================================
Line 43 has 1 error

Line 43: Syntax Error: Wrongly expressed elseif statement, else statement should be added instead
=============================================================
Line 46 has 1 error

Line 46: Syntax Error: Missing letter S,  letter S should be added to grade
==============================================================
Line 53 has 2 errorS

Line 53: Syntax Error: Missing an underscore _ , an underscore should be added to letter_grade
Line 53: Syntax Error: I changed "is" to "=="
==============================================================
Line 54 has 2 errors

Line 54: Missing an open parenthesis ( after print, a parenthesis should be added after print(
Line 54: Missing a closing parenthesis ), a parenthesis should be added after failing.")
==============================================================
Line 55 has 2 errors

Line 55: Missing an open parenthesis ( after print, a parenthesis should be added after print(
Line 54: Missing a closing parenthesis ), a parenthesis should be added after passing.")
===============================================================
"""
