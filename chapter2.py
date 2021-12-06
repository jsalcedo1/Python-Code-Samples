from chapter3 import ch3
# ======================================================================================================================
# Importing modules
import sys
import time
import winsound

# =============================
# Dialogue Timer: # Regular timer
a = 2
b = 2.5
c = 3
d = 3.5
e = 4
f = 4.5
g = 5
h = 6
i = 7
j = 8
k = 9
m = 10
x = 0.1  # characters
z = 5    # Chapter
# =============================
# Text Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# ==============================
# Testing Timer # Set these settings equal to 0 and add a hashtag (#) to dialogue timer
# a = 2         # (Only if you want to test this quickly & ignore the timers for each dialogue being played)
# b = 2.5
# c = 3
# d = 3.5
# e = 4
# f = 0
# g = 5
# h = 6
# i = 7
# j = 8
# k = 9
# m = 10
# x = 0.1
# z = 5




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Chapter 1: Intro
def ch2():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW)
    print("*******************************************************************************")
    print("**                Chapter 2: Accessing The Abandoned House                   **")
    print("** Luckily, the waterspout tornado made its way to the left-hand side        **")
    print("** on to another direction and away from your location. However, the heavy   **")
    print("**   thunderstorm and the heavy rain remained and couldn't let you continue  **")
    print("**                            your way home.                                 **")
    print("*******************************************************************************")
    time.sleep(m)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ======================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Scene:")  # Scene
    time.sleep(a)
    print()  # Space
    print(MAGENTA + '''
                You realize that you will not to be able to make it home, so you decide to settle down near 
                                            an abandoned old house.
    ''')
    time.sleep(a)
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print("What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Try to open the front door")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Go to the back yard and try to open the back door")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Throw a rock at the window and try to get inside")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to try to open the front door")
        time.sleep(a)
        ch2_path1()
    elif firstPath == '2':
        print("Action: You've chosen to go to the back yard and try to open the back door")
        time.sleep(a)
        ch2_path2()
    elif firstPath == '3':
        print("Action: You've chosen to throw a rock at the window and try to get inside")
        time.sleep(a)
        ch2_path3()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def ch2_path1():
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Path1: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *tries to open the front door*")
    time.sleep(a)
    s1 = '"You: It\'s locked... "'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = '"You: For god sake.. I must do something about this...I\'m getting wet.."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = '"You: I must find a better way to get inside..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path1: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                    What other ways are you thinking? ...
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path1: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Attempt to get inside using the abandoned house's backdoor")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Attempt to get inside by trying to break a window with a rock")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Do absolutely nothing...and get wet by the rain/thunderstorm")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Path1: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to attempt to get inside using the abandoned house's backdoor")
        time.sleep(d)
        ch2_path2()
    elif firstPath == '2':
        print("Action: You've chosen to attempt to get inside by trying to break a window with a rock")
        time.sleep(d)
        ch2_path3()
    elif firstPath == '3':
        print("Action: You've chosen to do absolutely nothing...and get wet by the rain/thunderstorm")
        time.sleep(d)
        print("Narrator: That's not going to get you anywhere pal, choose another choice...")
        time.sleep(d)
        ch2_path2()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_path2():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path2: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *tries to open the back door*")
    time.sleep(a)
    s1 = '"You: It\'s locked... "'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = '"You: For god sake.. I must do something about this...I\'m getting wet.."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = '"You: I must find a better way to get inside..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print(
        "===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path2: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                           What other ways are you thinking? ...
           ''')
    print(GREEN)  # Space
    print(
        "===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path2: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Attempt to get inside using the abandoned house's front door")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Attempt to get inside by trying to break a window with a rock")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Do absolutely nothing...and get wet by the rain/thunderstorm")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Path2: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to attempt to get inside using the abandoned house's front door")
        time.sleep(d)
        ch2_path1()
    elif firstPath == '2':
        print("Action: You've chosen to attempt to get inside by trying to break a window with a rock")
        time.sleep(d)
        ch2_path3()
    elif firstPath == '3':
        print("Action: You've chosen to do absolutely nothing...and get wet by the rain/thunderstorm")
        time.sleep(d)
        print("Narrator: That's not going to get you anywhere pal, choose another choice...")
        time.sleep(d)
        ch2_path2()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_path3():
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Path3: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *tries to get in by throwing a rock at a window*")
    time.sleep(a)
    s1 = '"Yes!!!I\'ve got it"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *takes lasso out from backpack*")
    time.sleep(a)
    s2 = 'You: "I knew this was going to be useful someday..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *climbs wall with lasso*")
    time.sleep(a)
    s2 = 'You: "Yes I\'m inside....what is this place?..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    ch2_sub_path()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def ch2_sub_path():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "SubPath: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    s1 = BLUE + 'You: "Everything in here is getting flooded..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "I think I will be safe as long as I walk up the stairs and stay in the second floor"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)

    # ==================================================================================================================
    print(YELLOW + "SubPath: Scene:")  # Scene
    time.sleep(a)
    print()  # Space
    print(MAGENTA + '''
            You have now broken into the house successfully. You think you are safe, but you are not.
                              Everything on the first floor is now getting flooded. 
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "SubPath: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Go upstairs")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Stay in the first floor")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Leave the abandoned house")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "SubPath: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to go upstairs")
        time.sleep(a)
        ch3()
    elif firstPath == '2':
        print("Action: You've chosen stay in the first floor")
        time.sleep(a)
        ch2_first_floor()
    elif firstPath == '3':
        print("Action: You've chosen to leave the abandoned house")
        time.sleep(a)
        ch2_leave()
    print(GREEN)  # Space
    print("===========================================================================================================")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_stairs():
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "SubPath1: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    s1 = BLUE + ' '
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "I think I will be safe as long as I walk up the stairs and stay in the second floor"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)
    # ==================================================================================================================
    print(YELLOW + "SubPath1: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
    You have now broken into the house successfully. You think you are safe, but you are not. Everything on the first 
    floor is now getting flooded. 
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "SubPath1: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Go upstairs")
    time.sleep(a)
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Stay in the first floor")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Leave the abandoned house")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "SubPath1: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to go upstairs")
        time.sleep(a)
        ch3()
    elif firstPath == '2':
        print("Action: You've chosen stay in the first floor")
        time.sleep(a)
        ch2_first_floor()
    elif firstPath == '3':
        print("Action: You've chosen to leave the abandoned house")
        time.sleep(a)
        ch2_leave
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_first_floor():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "SubPath2: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    s1 = BLUE + 'You: "I can feel the water flooding slowly coming up right on my knees...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "I shouldn\'t stay here..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "SubPath2: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
            The natural diaster's water is slowly flooding the entire house, you cannot stay in the first floor...
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "SubPath2: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Go upstairs")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Stay in the first floor")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Leave the abandoned house")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "SubPath2: Choice Selected:")  # Choices
    if firstPath == '1':
        print("Action: You've chosen to go upstairs")
        time.sleep(a)
        ch3()
    elif firstPath == '2':
        print("Action: You've chosen stay in the first floor")
        time.sleep(a)
        ch2_first_floor()
    elif firstPath == '3':
        print("Action: You've chosen to leave the abandoned house")
        time.sleep(a)
        ch2_leave()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_leave():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "SubPath3: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    s1 = BLUE + ' '
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "I think I will be safe as long as I walk up the stairs and stay in the second floor"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "SubPath3: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
            The natural diaster's water is slowly flooding the entire region, you cannot leave the house...
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "SubPath3: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Go upstairs")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Stay in the first floor")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Leave the abandoned house")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "SubPath3: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to go upstairs")
        time.sleep(a)
        ch3()
    elif firstPath == '2':
        print("Action: You've chosen stay in the first floor")
        time.sleep(a)
        ch2_first_floor()
    elif firstPath == '3':
        print("Action: You've chosen to leave the abandoned house")
        time.sleep(a)
        ch2_leave()
    print(GREEN)  # Space
    print("===========================================================================================================")