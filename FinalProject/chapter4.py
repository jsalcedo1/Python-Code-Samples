from chapter5 import ch5 # Used to transition from one file's branch to another file's branch.
# ======================================================================================================================
import sys
import time           # Time module
# import winsound     # Sounds (Only plays files that are .wav format)

# =============================
# Dialogue Timer Settings:
# ( Remove # If you want to play the game normally with timing delay between dialogues)
# (Otherwise, leave as it is if you want to tes if every option or branch works.

# =============================
# a = 2
# b = 2.5
# c = 3
# d = 3.5
# e = 4
# f = 4.5
# g = 5
# h = 6
# i = 7
# j = 8
# k = 9
# m = 10
# x = 0.1  # Time used in characters
# z = 5    # Time used in Chapters
# =============================
# Text Colors
# These are used for each dialogue/printing statement
# =============================
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# ==============================
# Testing Timer:
# These are set to 0 for testing purposes
# ==============================

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
m = 0
x = 0 # Time used in characters
z = 0 # Time Used in chapters

# Important information:
# Each file is divided by branches.
# ((If we get furthermore into detail, each branch follows my flowchart & milestone 1)).
# Flow/Structure: Main file - Introduction - Chapter 1, Chapter 2, Chapter 3, Chapter 4, Chapter 5.
# Branch structure: Chapter, Descriptive Small Story, Player Actions/Choices, Different Paths, Following Chapter.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Chapter 1: Intro
def ch4():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW)
    print("*****************************************************************************************************")
    print("**                Chapter 4: Looking For The Backpack And Staying For A Night                      **")
    print("**     You realize that everyone in town has either left or died, you don't know what to do        **")
    print("**  you are thinking about leaving town as well but you notice that you don't have your backpack   **")
    print("**    on you, you forgot it at the abandoned house, so you decide to go inside and look for it     **")
    print("*****************************************************************************************************")
    time.sleep(m)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ======================================================================================================================
    print(GREEN)
    print("You: *gets into the house*")
    time.sleep(a)
    s1 = 'You: " I should go upstairs since that is where I left it..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *walks up the stairs*")
    time.sleep(a)
    print("You: *finds an an old man with half his body dismembered*")
    time.sleep(a)
    print("You: OMG... ARE YOU OKAY?")
    time.sleep(a)
    s1 = 'Old man: "No, I\'m not okay..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print("*coughs*")
    s2 = 'Old man: "...But take this...you will know what to do with it.."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Old man: *starts dying slowly*")
    time.sleep(a)
    s3 = 'You: "A dagger?... What am I supposed to do with this? "'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Old man: *hands dagger to you*")
    time.sleep(a)
    s3 = 'You: "sOO!!!! "'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    # winsound.PlaySound("sound7", winsound.SND_ALIAS)
    print()
    print("===========================================================================================================")
    print(YELLOW + "Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                    You suddenly hear a squealing noises and foot steps in the first floor....
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(BLUE + "You: OMG WHAT IS THAT?...")
    time.sleep(a)
    s4 = '"You: "ooops.. I shouldn\'t have screamed..."'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print("What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Hide under the bed")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Hide inside the closet")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Be a brave man and wait for it to get to the second floor...")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    if firstPath == '1':
        print("Action: You've chosen to hide under the bed")
        time.sleep(c)
        ch2_path1()
    elif firstPath == '2':
        print(RED + "Creature: *hears you opening the closet*")
        time.sleep(c)
        print("Creature *takes you out & kills you*")
        time.sleep(c)
        print(RESET + "Narrator: It's not the time to play games...you either can survive or die...")
        time.sleep(c)
        print("Narrator: I'm terminating the game... since you died.. good luck trying the game over again..")
        time.sleep(d)
        exit()
    elif firstPath == '3':
        print(RED + "Creature: *sees you*")
        time.sleep(a)
        print("Creature: *grabs you from the neck*")
        time.sleep(b)
        print("Creature: *throws you out the window")
        time.sleep(b)
        print(RESET + "Narrator: It's not the time to play games...you either can survive or die...")
        time.sleep(d)
        print("Narrator: I'm terminating the game... since you died.. good luck trying the game over again..")
        time.sleep(d)
        exit()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def ch2_path1():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Path1: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: * hides under the bed*")
    time.sleep(a)
    s1 = 'You: "hopefully he does not see me.."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(RED + "Creature: *goes upstairs to the second floor*")
    time.sleep(a)
    s2 = 'Creature: "*JAWWWNSSSSSSS*"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Creature: *puts chainsaw aside of the bed's headboard*")
    time.sleep(d)
    print("Creature: *sits on top of bed & then lays*")
    time.sleep(a)
    print("Creature: *Starts snoring*")
    time.sleep(a)
    s3 = BLUE + 'You: "this is my chance...--- (You think to yourself)"'
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
                                              What should you do now?........
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
    print(CYAN + "Path #1:", GREEN + "Reach his chainsaw and slightly slide it underneath the bed")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Slowly walk away..")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Go downstairs and try to escape through the front door...")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Path1: Choice Selected:")  # Choices
    if firstPath == '1':
        print(RESET + "Narrator: This is not the time... to do play the superman role...")
        time.sleep(c)
        print("Narrator: I'm just going to let you see it for yourself...")
        time.sleep(c)
        print(RED + "Creature: *grabs you from the hand*")
        time.sleep(c)
        print("Creature: *throws you to the floor & eats your intestines*")
        time.sleep(c)
        print(GREEN + "Action: You are dead")
        exit()
    elif firstPath == '2':
        print("Action: You've chosen to slowly walk away")
        time.sleep(b)
        ch2_path2()
    elif firstPath == '3':
        print(GREEN + "Action: You've chosen use the front door...")
        time.sleep(b)
        print(BLUE + "You: DAMN IT'S LOCKED..!")
        time.sleep(b)
        print(RESET + "Narrator:Why are you screaming..")
        time.sleep(b)
        print(RED + "Creature: *hears you & kills you*")
        time.sleep(b)
        exit()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch2_path2():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path2: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *slowly walks away*")
    time.sleep(a)
    s1 = '"You: uff..glad that ugly creature did not hear me..could have been dead.."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *slowly walks downstairs*")
    time.sleep(a)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path2: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                           What should you do now?
           ''')
    print(GREEN)  # Space
    print(
        "===========================================================================================================")
    time.sleep(m)
    choices()
    # ==================================================================================================================


def choices():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW + "Path2: Player Actions:")  # Player Actions
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Search for key")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Try using the backdoor to leave..")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Try using the front door to leave..")
    time.sleep(a)
    print(CYAN + "Path #4:", GREEN + "Go trough the the same window you broke & used to get inside the abandoned house")
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Path2: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print(GREEN + "Action: You've chosen to search for a key")
        time.sleep(d)
        ch5()
    elif firstPath == '2':
        print(RESET + "Narrator: The backdoor is locked remember?..")
        time.sleep(d)
        choices()
    elif firstPath == '3':
        print(RESET + "Narrator: The front door is locked remember? try another choice...")
        time.sleep(d)
        choices()
    elif firstPath == '4':
        print(RESET + "Narrator: Eventually you can go through the same window...")
        time.sleep(d)
        print("Narrator: Remember that you used a lasso to climb that window...therefore")
        time.sleep(d)
        print("Narrator: You eventually die...since its distance is far away from the floor ")
        time.sleep(d)
        exit()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
