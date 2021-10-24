# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")

'''
Edited by: Jaime S.
10/22/2021

Corrections:
=====================================================================================
Line 9 has 4 errors:

1. Line 9: Syntax Error: Equal sign is repeated twice ==, it should only have one = 
2. Line 9: Syntax Error: Wrong single quote ' , should have a double quote "
3. Line 9: Syntax Error: A dot . between int and input should be removed, a parenthesis should be added
4. Line 9: Syntax Error: Two closing parenthesis at the end of "origin?")) should be added
=====================================================================================
Line 11 has 1 error:

1. Line 11: Syntax Error: Missing a colon :
=====================================================================================
Line 12 has 2 errors:

1. Line 12: Syntax Error: Wrong single quote ' , should have a double quote "
2. Line 12: Syntax Error: Unnecessary spacing after print ( , the parenthesis should be close to print(
=====================================================================================
Line 13 has 1 error:

1. Line 13: Syntax Error: The symbol ampersand & is repeated , should only have one ampersand symbol &
======================================================================================
Line 14 has 1 error:

Line 14: Syntax Error: Unnecessary spacing after print (, the parenthesis should be close to print(
======================================================================================
Line 15 has 1 error:

1. Line 15: Syntax Error: Statement elseif is improperly used, the else statement should be used instead
======================================================================================
Line 16 has 1 error:

1.Line 16: Syntax Error: Unnecessary spacing after print (, the parenthesis should be close to print(
======================================================================================
'''
