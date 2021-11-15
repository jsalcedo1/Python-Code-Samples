# Jaime S.
# 11/9/2021
# This is a program that asks for user's input or number and ...
# determines whether the inserted number is within the given range of (1, 10)
# Helpful information: No additional info, just a simple and easy to use program to determine ...
# Which number is or isn't within the range of (1, 10) (The range can be modified)
def test_range(number):                                  # Defines test range as number
    if number in range(1, 10):                           # Checks if the number is within the range of (1,10)
        print(" %s is in the range" % str(number))       # If it is will print "is in range"
    else:                                                # If not then ...
        print("The number is outside the given range.")  # It will print "the number is outside the given range"


n = int(input("Enter a range: "))                        # Asks for user's input
test_range(n)                                            # Ensures it is printing the test range of the number inserted
