# Jaime S.
# 11/06/2021
# This program will select a random week day from the list and will show it.
# Helpful information: Very simple program to use to generate a random day from the week.
import random    # requests access to the random module

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # list of days within a week

print(random.choice(days))    # selects and prints a random day
