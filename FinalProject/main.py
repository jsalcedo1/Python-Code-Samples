
# ======================================================================================================================
# Importing Modules:
from Introduction import intro # Imports introduction to the main file.
from chapter1 import ch1 # Brings ch1 branch from chapter 1 file

# ======================================================================================================================
# Game Starts Here:
intro()
if __name__ == '__main__':  # Reads source files and defines as global variables
    ch1()  # Takes player to chapter 1 (this function is commonly used in every branch)
# ======================================================================================================================



