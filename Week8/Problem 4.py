# Jaime S.
# 11/16/2021
# National Louis University
# This program will take a year as a parameter and will return true if the year is leap year, it will return false
# Important information: This program should work because we want the year to be divisible with 4.
# %4 will need to be true for the output to be bool True. We have to take into account that the year that is divisible
# with 4 can be divided to 400.  If the year is divisible to 100 but not to 400 bool is False.

year = int(input('Enter year to check if it is leap year.'))  # User input
if year % 4 == 0 and year % 100 != 0:  # Checks if it is
    leap = "is a leap year"  # Will print this if it is a leap year
elif year % 100 == 0 and year % 400 == 0:  # Checks else if
    leap = "is a leap year"  # will print this if it is a leap year
else:  # Checks If is not
    leap = "is not a leap year"  # Will print this if is not a leap year

print(" the year you entered " + leap)  # prints text + leap
