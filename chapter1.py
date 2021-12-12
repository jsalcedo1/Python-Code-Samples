from chapter2 import ch2 # Used to transition from one file's branch to another file's branch.
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
x = 0  # Time used in characters
z = 0  # Time Used in chapters

# Important information:
# Each file is divided by branches.
# ((If we get furthermore into detail, each branch follows my flowchart & milestone 1)).
# Flow/Structure: Main file - Introduction - Chapter 1, Chapter 2, Chapter 3, Chapter 4, Chapter 5.
# Branch structure: Chapter, Descriptive Small Story, Player Actions/Choices, Different Paths, Following Chapter.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Chapter 1: Intro
def ch1():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW)
    print("*****************************************************************")
    print("**                 Chapter 1: Dreaming at school               **")
    print("** It was a dark and cold night with a heavy thunderstorm and  **")
    print("** mighty thunder rays, causing the ground to flood.           **")
    print("*****************************************************************")
    time.sleep(m)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ======================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *Wakes up*")
    time.sleep(a)
    s1 = 'You: "I must have been dreaming...what a stupid dream...."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "A creature in a cave with a chainsaw??....I must be kidding"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print(" *laughs*")
    time.sleep(a)
    print("You: All I can remember is falling asleep during detention --- (You think to yourself)")
    time.sleep(a)
    s3 = 'You: "I need to leave school and get home early...my mom is going to get mad at me..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Narrator: You suddenly hear heavy storm and strong wind sounds")
    time.sleep(a)
    s4 = '''You: "Oh my god, everything has been flooded...AND A WATERSPOUT TORNADO IS SLOWLY COMING TOWARDS 
THIS DIRECTION!!"'''
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")

    # ==================================================================================================================
    print(YELLOW + "Scene:")  # Scene
    time.sleep(a)
    print()  # Space
    print(MAGENTA + '''
              You realize that you have to get home to avoid being drowned or killed by the flooding caused by 
              the waterspout tornado; the entire region nearby your school is starting to flood. 
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print("What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "RUN")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "WALK")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "CROUCH & SCREAM")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    if firstPath == '1':
        print("Action: You've chosen to run")
        time.sleep(g)
        path1()
    elif firstPath == '2':
        print("Action: You've chosen to walk")
        time.sleep(g)
        path2()
    elif firstPath == '3':
        print("You've chosen to crouch & scream")
        time.sleep(g)
        path3()
    print()  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def path1():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *runs* ")
    time.sleep(a)
    print("You: *Inhales*")
    time.sleep(a)
    print("You: *Exhales*")
    time.sleep(a)
    s1 = 'You: "I can do this"...*exits school*'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Narrator: As you were exiting school..you suddenly feel that someone grabs your leg....")
    time.sleep(a)
    s2 = 'You: "AH!.. What is this?...Who are you?... Let go of me.. *looks down to the ground*'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = 'Creepy old man: "Yes, I am grabbing your leg kind sir and not letting go of it...."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                     The old man looks suspicious, and seems to be hiding something behind his back...
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Kick him")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Help him get up")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Run away")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print('YOU: "*Kicks him and walks away*"')
        time.sleep(b)
        path2()
    elif firstPath == '2':
        print("Action: You've chosen to help him get up")
        time.sleep(b)
        s1 = BLUE + 'Old man: "Thank you for helping me...LOOK...WHAT IS THAT?!"'
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(x)
        print()
        s2 = 'You: "WHAT IS WHAT?"'
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(x)
        print()
        print("You: *gets knocked down in the ground and dies*")
        time.sleep(b)
        print(GREEN + "Action: GAME OVER")
        time.sleep(b)
        exit()
    elif firstPath == '3':
        print("Action: You've chosen to run away")
        time.sleep(b)
        path2()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def path2():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *walks* ")
    time.sleep(a)
    s1 = 'You: "This is not bad at all..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Narrator: You suddenly feel that the waterspout tornado elevates you to the air...")
    time.sleep(d)
    s2 = 'You: "OMG...AHHHHHHHHHHHHHHHHHHHHHH!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
    In front of you, there is a rocky cliff you can fasten on to. In the back of you, there is a tree with branches, 
    which you can also fasten on to. In your surroundings, there are objects flying, which you can also fasten on to.
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Fasten on to the rocky cliff, in front of you")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Fasten on to the tree's branches, in the back of you")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Fasten on to the nearest objects flying, surrounding you")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to fasten on to the rocky cliff, in front of you")
        time.sleep(d)
        print(RESET + '''Narrator: Good decision you've managed to resit to the natural disaster...however you will need 
to run and find somewhere safe to settle...the tornado keeps going back and forth...it might return...''')
        time.sleep(g)
        ch2()
    elif firstPath == '2':
        print("Action: You've chosen to fasten on to the tree's branches, in the back of you")
        time.sleep(e)
        print(RESET + '''Narrator: Good decision you've managed to resit to the natural disaster...however you will need 
to run and find somewhere safe to settle...the tornado keeps going back and forth...it might return...''')
        time.sleep(g)
        ch2()
    elif firstPath == '3':
        print(RESET + '''Narrator: Good decision you've managed to resit to the natural disaster...however you will need 
to run and find somewhere safe to settle...the tornado keeps going back and forth...it might return...''')
        time.sleep(g)
        ch2()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def path3():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *Crouches & screams* ")
    time.sleep(a)
    s1 = 'You: " SOMEBODY HELP!!"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Narrator: Sadly, nobody is able to hear you...")
    time.sleep(b)
    s2 = 'You: "OMG...*gets you angered* There is no one?!!...."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
    Your scream was extremely loud and dramatic enough to anger a pack of wolves, which were hanging around outside 
                                                from your school. 
                Suddenly....The wolves start getting inside your school and start looking for you....
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Scream even more, until the wolves get scared and leave the school facility")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Run away from school, until you reach a safe zone")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Stay still, until the wolves leave")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    if firstPath == '1':
        print(RESET + "Narrator: Wrong decision...you think they will get scared?")
        time.sleep(d)
        print("Narrator: You must be joking...")
        time.sleep(b)
        print(RED + "*Wolves bite you until you are dead*")
        time.sleep(b)
        print(GREEN + "GAME OVER")
        time.sleep(a)
        exit()
    elif firstPath == '2':
        print("Action: You've chosen to Run away from school, until you reach a safe zone")
        time.sleep(d)
        ch2()
    elif firstPath == '3':
        print(RESET + "Narrator: Wrong decision...you must be kidding right?")
        time.sleep(a)
        print("Narrator: These wolves are not going to leave until they see you dead...I'll just let the scene play..")
        time.sleep(e)
        print(RED + "*Wolves bite you until you are dead*")
        time.sleep(d)
        print(GREEN + "Action: GAME OVER")
        time.sleep(a)
        exit()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


