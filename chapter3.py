from chapter4 import ch4
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
z = 5  # Chapter
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
def ch3():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW)
    print("*********************************************************************************************************")
    print("**                                Chapter 3: Catastrophe                                               **")
    print("**    You stayed at the haunted house to sleep in the second floor, now that the natural disaster      **")
    print("**      is gone and now that the weather is at a stabilized stage you have the opportunity             **")
    print("** to go home and see for yourself that everyone in town has evacuated the area including your parents **")
    print("**    you don't know for sure if they are dead or still alive...you must figure it out yourself....    **")
    print("*********************************************************************************************************")
    time.sleep(m)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ======================================================================================================================
    print(GREEN)
    # Beginning of dialogues
    print(BLUE + "You: *Wakes up*")
    time.sleep(a)
    print("You: *Heads towards home*")
    time.sleep(a)
    print("You: *Searches around the house*")
    time.sleep(a)
    s1 = 'You: "I can\'t believe there is no one in here..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(a)
    print()
    print("You: *Exits house*")
    time.sleep(a)
    print("You: *Looks around neighborhood*")
    time.sleep(b)
    s2 = 'You: "Everyone in town must be dead...all I can see is dead bodies...that\'s is crazy..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = 'You: "I must leave town and see if anyone else in other regions are alive..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s4 = 'You: "I totally doubt it..but let\'s see how this goes.."'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
            After hours and hours of searching, you weren't able to find people alive...but maybe if you
        look into the places that you have not yet looked into...you could probably find someone alive there
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Player Actions:")  # Player Actions
    print()  # Space
    print("Where should you look now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Church, maybe you will find people in church")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Home, maybe you haven't searched very well...")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Alleys, maybe there could be someone alive")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    time.sleep(a)
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to search for people alive in church")
        time.sleep(a)
        ch3_church()
    elif firstPath == '2':
        print("Action: You've chosen to search for people alive at home")
        time.sleep(a)
        ch3_home()
    elif firstPath == '3':
        print("Action: You've chosen to search for people alive in the alleys of your neighborhood")
        time.sleep(a)
        ch3_alleys()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def ch3_church():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path1: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *looks for people alive in church*")
    time.sleep(a)
    s1 = 'You: "There is no one alive... "'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = '"You: Maybe I should try searching people alive in places I have not yet searched in"'
    for character in s2:
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
    print(YELLOW + "Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print("Where should you look now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Church, again...maybe you searched for very well")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Home, maybe you haven't searched very well...")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Alleys, maybe there could be someone alive")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    time.sleep(a)
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Path1: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to search again for people alive in church")
        time.sleep(c)
        ch3_church()
    elif firstPath == '2':
        print("Action: You've chosen to search for people alive at home")
        time.sleep(c)
        ch3_home()
    elif firstPath == '3':
        print("Action: You've chosen to search for people alive in the alleys of your neighborhood")
        time.sleep(e)
        ch3_alleys()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch3_home():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path2: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *Looks for people at home again*")
    time.sleep(a)
    s1 = 'You: "What am I even doing...just wasting my time.. I already searched here..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You: "This place is not even big for me to have to search here again...what am I doing?"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = '"You: There must be somewhere else better to look for..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(GREEN)  # Space
    print("===========================================================================================================")
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
    print("Where should you look now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Church, maybe you will find people in church")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Home, again...maybe you haven't searched very well...")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Alleys, maybe there could be someone alive")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    time.sleep(a)
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Path2: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to search for people alive in church")
        time.sleep(d)
        ch3_church()
    elif firstPath == '2':
        print("Action: You've chosen to search for people alive at home again")
        time.sleep(d)
        ch3_home()
    elif firstPath == '3':
        print("Action: You've chosen to search for people alive in the alleys of your neighborhood")
        time.sleep(d)
        ch3_alleys()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch3_alleys():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path3: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *Looks for people in the alleys*")
    time.sleep(a)
    s1 = 'You: "There is no one in here...wait a minute..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *Sees shadow*")
    time.sleep(a)
    s2 = 'You: Omg...you again.... '
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = '"You: NO NO NO ...you are imaginary... you do not supposed to be real!...."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *Runs away*")
    time.sleep(a)
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path2: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                                   You've ran away....
             ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Path2: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print("Where are you going to go now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Doesn't matter as long as it is away from that creature")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "I will not run, I'll rather stay...the creature is imaginary..")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Find a safer place...")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    time.sleep(a)
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Path2: Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to go anywhere away from that creature ")
        time.sleep(a)
        ch3_sub_path()
    elif firstPath == '2':
        print("Action: You've chosen not to run since you think the creature is imaginary")
        time.sleep(a)
        ch3_sub_path2()
    elif firstPath == '3':
        print("Action: You've chosen to find a safer place")
        time.sleep(a)
        ch4()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def ch3_sub_path():
    winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    s1 = BLUE + 'You: "I could not choose any better....*sarcasm*"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = 'You:" what a great decision I have made...not sure if that was what I thought it was..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = 'You:" Anyway I\'m away from that thing..."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s4 = 'You: "Oh NO! I have lost myself..."'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s5 = 'You: "And my backpack???...are you serious...I have to go find it before I leave town"'
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("===========================================================================================================")
    time.sleep(a)
    # ==================================================================================================================
    print(YELLOW + "SubPath: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print("What can you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Try to go back using the same direction")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Run further away...")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Path2: Choice Selected:")  # Choices
    if firstPath == '1':
        print("Narrator: Great Choice....")
        time.sleep(c)
        ch4()
    elif firstPath == '2':
        print("Narrator: Are you serious?...try that again...")
        time.sleep(c)
        ch3_sub_path()
    elif firstPath == '3':
        print("Narrator: You must be kidding right...try that again..")
        time.sleep(c)
        ch3_sub_path()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def ch3_sub_path2():
    s1 = 'You: "Lol an imaginary creature...obviously nothing will happen to me?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = BLUE + 'You:" OMG NOOOOOOOOOOOOOOOOOOOOOOOO!!!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
        winsound.PlaySound("sound7", winsound.SND_ALIAS)
    print()
    winsound.PlaySound("sound7", winsound.SND_ALIAS)  # plays sound not background
    print(RED + "Creature: *Growls*")
    winsound.PlaySound("sound5", winsound.SND_ALIAS)  # plays sound not background
    time.sleep(a)
    print(RED + "Creature: MUAHAHAH")
    time.sleep(a)
    print(RED + "Creature: *Takes chainsaw out & kills you*")
    time.sleep(a)
    print(BLUE + "You: Please no....X_X ....ugh...*dies*")
    time.sleep(a)
    s3 = RESET + 'Narrator: GREAT JOB...YOU FOOL... you just killed yourself..'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s4 = "Narrator: I'm going to terminate the game since you are dead hopefully you make better decisions next time.."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("Good luck...")
    time.sleep(a)
    exit()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
