# ======================================================================================================================
import sys
import time  # Time module

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
def ch5():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    print(YELLOW)
    print("******************************************************************************************")
    print("**                         Chapter 5: Escaping The Haunted House                         **")
    print("**  You found a key and you use it to open the backdoor, as soon as you close the door   **")
    print("**  and exit the house you can see how there are huge fences that were not there before..**")
    print("**  these fences form a zic zac...which you must pass through to leave town and find     **")
    print("**   people alive....which will eventually help find information regarding your parents  **")
    print("*******************************************************************************************")
    time.sleep(m)
    zic_zac()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def zic_zac():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Zic Zac: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                             FIND YOUR WAY THOUGH THE ZIC ZAC
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Zic Zac: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Break right...")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Walk forward....")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Break left.....")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to break right")
        time.sleep(b)
        zic_zac()
    elif firstPath == '2':
        print("Action: You've chosen to walk forward")
        time.sleep(b)
        zic_zac()
    elif firstPath == '3':
        print("Action: You've chosen to break left")
        time.sleep(b)
        break_confusion()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def break_confusion():
    # ======================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Zic Zac: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
            This is not broken keep trying...your way out.. clues what do you call someone who is (censored) handed
                                        probably you should try that direction....
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Zic Zac: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    s1 = RESET + 'Narrator:" Haha..Pretty difficult to get out from this loop?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = RESET + 'Narrator:"No one said that the final chapter was going to be this easy"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Break right")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Walk forward")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Break left")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print("Action: You've chosen to break right")
        time.sleep(a)
        break_confusion2()
    elif firstPath == '2':
        print("Action: You've chosen to walk forward")
        time.sleep(a)
        break_confusion2()
    elif firstPath == '3':
        print("Action: You've chosen to break left")
        time.sleep(a)
        break_path()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def break_confusion2():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ======================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Zic Zac Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                    This is not broken keep trying...almost there..
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Zic Zac: Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "Break right")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Walk forward")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Break left.")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    if firstPath == '1':
        print("Action: You've chosen to break right")
        time.sleep(c)
        break_path()
    elif firstPath == '2':
        print("Action: You've chosen to walk forward")
        time.sleep(c)
        break_path()
    elif firstPath == '3':
        print("Action: You've chosen to break left")
        time.sleep(c)
        break_path()
    print(GREEN)  # Space
    print("===========================================================================================================")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def break_path():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    print(YELLOW + "Zic Zac(Ending): Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *steps on a bear trap ...*")
    time.sleep(a)
    print('"You: "OMG NO...."')
    print(RED + "Creature: *hears the sound caused by it and heads over your location*")
    time.sleep(a)
    s1 = BLUE + 'You: "Please....let go of me"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(a)
    print()
    print(BLUE + "You: *Sees creature coming*")
    time.sleep(a)
    print(RED + "Creature: *turns chainsaw on*")
    time.sleep(a)
    print()
    s2 = BLUE + 'You: "YESS I\'M FREE..."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s3 = 'You: "I NEED TO RUN....AHHHHHHHHH"'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print("You: *starts running*")
    time.sleep(a)
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Zic Zac(Ending): Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                                            Where should you go now?
    ''')
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(m)
    # ==================================================================================================================
    print(YELLOW + "Zic Zac(Ending): Player Actions:")  # Player Actions
    time.sleep(a)
    print()  # Space
    print(YELLOW + "What should you do now?")
    time.sleep(a)
    print(CYAN + "Path #1:", GREEN + "RUN RIGHT ")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "RUN LEFT")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "RUN FORWARD")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    time.sleep(a)
    print(YELLOW + "Choice Selected:")  # Choices
    if firstPath == '1':
        print("Action: You've chosen run to the right")
        time.sleep(c)
        finish_line()
    elif firstPath == '2':
        print("Action: You've chosen to run to the left")
        time.sleep(c)
        finish_line()
    elif firstPath == '3':
        print("Action: You've chosen to run forward")
        time.sleep(c)
        finish_line()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def finish_line():
    # winsound.PlaySound("sound10", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound10 (background)
    # ==================================================================================================================
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Path: Continuation:")  # Continuation
    time.sleep(a)
    print()  # Space
    # Beginning of dialogues
    print(BLUE + "You: *keeps running*")
    time.sleep(a)
    s1 = 'You: "omg there is a door blocking the way... "'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    s2 = RED + 'Creature: "COME TO ME!....*turns chainsaw on*"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
    print()
    print(RESET + "Narrator: Says the creature with a creepy voice ....")
    time.sleep(a)
    s3 = BLUE + 'You: "NOOO....."'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(x)
        # winsound.PlaySound("sound7", winsound.SND_ALIAS)
    print("You: *Climbs door*")
    time.sleep(a)
    print("You: *grabs yourself from an edge & gets to other side of the wall*")
    time.sleep(a)
    print(RED + "Creature: *breaks door* ")
    time.sleep(a)
    print(RESET + "Narrator: Eventually you get to the end of labyrinth or zic zac...")
    time.sleep(a)
    print("Narrator: ... As you are running you suddenly see three alternatives of escaping...please choose wisely..")
    time.sleep(a)
    print(GREEN)  # Space
    print("===========================================================================================================")
    # ==================================================================================================================
    print(YELLOW + "Path: Scene:")  # Scene
    print()  # Space
    print(MAGENTA + '''
                             Narrator: ONCE AGAIN... Please choose your alternative wisely...
                                                 ..You've come to a dead end....
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
    print(CYAN + "Path #1:", GREEN + "Go through the manhole cover, which is slightly open")
    time.sleep(a)
    print(CYAN + "Path #2:", GREEN + "Grab a brick from the ones that are on the floor  and hit the creature with it")
    time.sleep(a)
    print(CYAN + "Path #3:", GREEN + "Wake up?..")
    time.sleep(a)
    firstPath = input(YELLOW + "Choose a path (1/2/3): ")
    print()
    print(GREEN + "---------------------------------------------------------------------------------------------------")
    print(YELLOW + "Choice Selected:")  # Choices
    time.sleep(a)
    if firstPath == '1':
        print(RESET + "Narrator: Good try, but no....")
        time.sleep(a)
        print(BLUE + "You: AHHHHHHH.....I can't swim....")
        time.sleep(a)
        print("You: *Drowns* X_X...")
        time.sleep(a)
        print(GREEN + "Action: GAME OVER")
        print()
        exit()
    elif firstPath == '2':
        print(RESET + "Narrator: You've just angered the creature....whatever..see the scene for yourself")
        time.sleep(a)
        print(RED + "*Creature: ARUGHHHHHHHHHH*")
        time.sleep(a)
        print("Creature:Exterminates you")
        time.sleep(a)
        print(GREEN + "GAME OVER")
        exit()
    elif firstPath == '3':
        print(RESET + "Narrator: IT WAS ALL A DREAM..YOU WERE DREAMING THE ENTIRE TIME....")
        time.sleep(c)
        print("Narrator: Nothing was real....you still at school detention...")
        time.sleep(c)
        print(BLUE + '"You: What a crazy dream...haha..oh look there is a dagger in my backpack.."')
        time.sleep(c)
        print(GREEN + "Action: *suspense....*end of story*")
        time.sleep(c)
        print(BLUE + "You: *Puts ghost looking mask on and costume...and grabs dagger*")
        time.sleep(c)
        print(CYAN + "Teacher: Omg what are you doing... ")
        time.sleep(c)
        print(RED + "Action: *BLOODY SCENE*....this is for what they did to me in the past *does ghosty smile*")
        time.sleep(b)
        print(BLUE + "Doctor: This young man is a threat for our community...apply the anesthesia..Mr. White...")
        time.sleep(b)
        print("Mr. White: We'll lock him down... Mr...")
        time.sleep(a)
        print(RED + "You: *heart starts beating fast*")
        time.sleep(b)
        print("You: *Closes eyes*")
        time.sleep(b)
        print("You: *Wakes up*")
        time.sleep(b)
        print('You: "NOOOOOOOOOOO..let me out of here!"')
        time.sleep(b)
        print(RESET + "Narrator: Some people believe that Ghostface will escape from the mental hospital.")
        time.sleep(b)
        print("Narrator: Someday and somehow...from the mental imprisonment...")
        time.sleep(b)
        print("Narrator: Doctors believe that he will get better... I totally doubt it...")
        time.sleep(b)
        print("Narrator: I believe that He will.. avenge those who humiliated him..and left him in the cave")
        time.sleep(b)
        s1 = YELLOW + 'Author:', RED + 'JAIME ', GREEN, '"THANKS FOR PLAYING"'
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(x)
        print()

        congrats_you_finished_the_game()
    print(GREEN)  # Space
    print("===========================================================================================================")
    time.sleep(a)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def congrats_you_finished_the_game():
    print(GREEN + '''
██████████████████████████████████▓▓██████████████████████████████████████████████████
████████████████████████████▓▓▓▓▓▓████████████████████████████████████████████████████
██████████████████████████▓▓▓▓▓▓██████████████████████████████████████████████████████
████████████████████████████▓▓████████████████████████████████████████████████████████
████████████████████▓▓████▓▓▓▓████████████████████████████████████████████████████████
██████████████████▓▓████▓▓▒▒████████████▓▓▓▓██████████████████████████████████████████
████████████████▓▓▓▓████▓▓▓▓██████▓▓▓▓▒▒░░░░░░░░▒▒▒▒▓▓████████████████████████████████
████████████████▒▒████▓▓▓▓██████████▓▓░░░░░░░░░░░░░░░░▓▓██████████████████████████████
██████████████▒▒▓▓████▓▓▓▓██████▓▓▓▓▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒████████████████████████████
████████████▒▒▒▒████▓▓▓▓██████████▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒██████████████████████████
██████████▓▓▒▒▓▓████▓▓▓▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████████████████████████
██████████▒▒▒▒████▓▓██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒████████████████████
████████▒▒░░▓▓████▓▓████▓▓██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██████▓▓██████████
████████░░▒▒▓▓████████▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██████████████████
████████░░▓▓██████████▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓████████████████
████████▒▒▓▓████████▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓████████████████
██████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒████████████▓▓██
██████▒▒▓▓▓▓████▓▓▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██████████████
██████▒▒▓▓▓▓████▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓██████████████
██████▓▓▒▒▓▓██████▓▓▓▓██░░░░░░        ░░  ░░░░░░░░▒▒▒▒░░  ░░░░░░▒▒▒▒▒▒▓▓██████████████
████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░            ░░▒▒████▓▓▒▒▒▒░░░░░░░░░░▒▒▓▓▒▒▒▒▓▓██████▓▓████
████░░▓▓▓▓▓▓██▓▓▓▓▓▓██░░░░            ░░▒▒████████░░▒▒░░░░████░░▒▒▓▓▒▒▒▒▓▓████████████
████▒▒▓▓▓▓▓▓██▓▓▓▓▓▓██░░░░          ░░░░████████▓▓░░▒▒░░▒▒████▓▓░░▓▓▒▒▒▒▓▓████████████
████▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░          ░░▒▒██████████▓▓░░░░░░████████░░▓▓▒▒▒▒▓▓████████████
██░░▓▓▓▓▓▓▓▓██▒▒▓▓██░░░░        ░░▒▒████████████▒▒░░░░░░██████▓▓▒▒▓▓▒▒▒▒▓▓██████████▓▓
▓▓░░▓▓▓▓▓▓▓▓██▒▒████░░░░      ░░░░██████████████░░▒▒░░░░████████▓▓▒▒▒▒▒▒▒▒██████████▓▓
▓▓░░▓▓▓▓▓▓▓▓██▓▓████░░░░░░░░░░░░██████████████▓▓░░▒▒░░▒▒████████▓▓▒▒▒▒▒▒▒▒██████████▓▓
▒▒▒▒▓▓▓▓▓▓▓▓██▓▓██▒▒░░░░░░░░░░▓▓██████████████▒▒░░░░░░▒▒████████▓▓▒▒▒▒▒▒▒▒████▓▓████▒▒
░░▒▒▓▓▓▓▓▓▓▓██▓▓██░░░░░░░░░░▓▓████████████████░░░░░░░░▒▒████████▓▓░░▒▒▒▒▒▒▓▓████████▒▒
░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓██░░░░  ░░▓▓████████████████▒▒  ░░░░░░░░██████████▒▒░░▒▒▒▒▓▓██▓▓████▒▒
░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░  ░░▒▒██████████████████  ░░░░░░░░░░██████████▓▓░░▒▒▒▒▓▓██▓▓████▒▒
▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░██████████████████░░░░░░  ░░▒▒░░████████████▒▒░░▒▒▓▓██▓▓████░░
▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓██░░░░░░▓▓▓▓██████████▒▒░░░░░░  ░░░░▒▒░░░░██████████▓▓▒▒░░▓▓██▓▓██▓▓  
▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░▓▓████████▒▒░░░░░░    ░░░░░░▒▒░░████████████▒▒░░▓▓██▓▓████  
▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░▒▒▒▒░░░░░░░░░░  ░░  ░░░░░░▒▒░░▒▒██████████▒▒░░▒▒██▓▓██▓▓  
▒▒▓▓▓▓▓▓▓▓▓▓▒▒██▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░    ░░░░▒▒██▒▒▓▓░░▓▓██████▒▒░░░░▒▒██████▓▓  
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██░░░░░░░░░░░░░░░░░░        ░░██░░██░░▓▓░░░░▒▒▓▓▒▒░░░░░░▓▓██████▒▒░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░░░▒▒░░░░      ░░▓▓██░░██▒▒▓▓▒▒░░░░░░░░░░░░▒▒▓▓██████▒▒░░
▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░▒▒░░░░        ░░░░░░░░▓▓░░▒▒▒▒░░░░░░░░░░░░▒▒██▓▓████    
▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓████▒▒▒▒▒▒▒▒░░░░          ░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒██▓▓████    
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒░░░░░░░░          ░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒▓▓██▓▓████    
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████░░░░░░░░░░        ░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▓▓▓▓██▓▓▓▓██▒▒    
▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓████░░░░░░░░░░░░      ░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓████▓▓████      
▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░░░░░  ░░  ░░▒▒██████▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓██      
▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓████▒▒░░░░░░░░░░░░░░░░████████████▒▒▒▒▓▓▒▒▒▒▓▓██████▓▓██████░░░░░░
▓▓▓▓██████████▓▓▓▓▓▓██████░░░░░░░░░░░░░░████████████████░░▓▓▓▓▓▓▓▓████▓▓▓▓████░░░░░░░░
▓▓▓▓██████████▓▓▓▓▓▓██████░░░░░░░░░░░░▒▒████████████████░░▓▓▓▓▓▓██████▓▓▓▓████░░░░░░░░
▓▓▓▓▓▓████████▓▓▓▓▓▓██████▒▒░░░░░░░░░░██████████████████░░▓▓▓▓████▓▓▓▓▓▓████░░░░▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████░░░░░░░░░░██████████████████░░▓▓▓▓████░░▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓████████░░░░░░░░░░██████████████████░░▓▓▓▓████░░▓▓████▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██████████░░░░░░░░░░████████████████▓▓░░▓▓▓▓██▒▒▒▒▓▓████░░▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓████████▓▓██████████░░░░░░░░░░████████████████▓▓░░▓▓████▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓████████████████████░░░░░░░░░░████████████████▓▓░░▓▓████░░▓▓████░░▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓████████▓▓██████████▒▒░░░░░░░░████████████████▓▓▒▒▓▓████▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓████▓▓░░░░░░░░▒▒██████████████▓▓▓▓████▓▓▓▓██████▒▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▒▒▒▒▒▒▓▓██████▓▓▓▓▓▓████████░░░░░░░░▒▒██████████████▒▒▓▓████▒▒▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▓▓██████▓▓██▓▓████████░░░░░░░░░░██████████████▒▒▓▓████▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▓▓██████████████████░░░░░░░░░░██████████████░░▓▓████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▒▒▒▒▒▒░░▒▒██████████████████░░░░░░░░░░████████████▓▓░░██████▓▓████▓▓▓▓▓▓▓▓▓▓▓▓██████
▓▓▓▓▒▒▒▒▒▒▒▒██████▓▓██████████░░░░░░░░░░▒▒████████████░░████▓▓████████▓▓▓▓████████████
▓▓▓▓▓▓▒▒▒▒▓▓██████████████████▒▒░░░░░░░░░░████████████░░████████████████████▓▓▓▓██████
▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓░░░░░░░░░░██████████▓▓▒▒████▓▓████████████████████▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██████████▓▓▒▒██████████░░░░░░░░████████████▒▒██████████████████████████████
▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓██▓▓██████████▒▒░░░░██████████▓▓▓▓██████████████████████████████
▓▓████▓▓▓▓▓▓██████████▓▓██████████████░░░░▒▒████████▒▒████████████████████████████████
██████████▓▓▓▓████████▓▓██████████░░░░░░░░░░████████░░████████████████████████████████
████████▓▓████▓▓██████▓▓██████████░░░░░░░░░░▒▒████▓▓░░██████████▓▓████████████████████
████████████████▓▓████▓▓██████████▒▒░░░░░░░░░░▒▒██░░████████████▓▓████████████████████
██████████████████▓▓██▓▓████████████▒▒▒▒▒▒▒▒▒▒░░░░▓▓████████████▓▓████████████████████
██████████████████████▓▓████████████▓▓▒▒▒▒▒▒▓▓▓▓████████████████▓▓████████████████████
██████████████████████▓▓██████████████████▓▓▓▓██████████████████▓▓████████████████████
██████████████████████████████████████████▓▓░░░░████████████████▓▓▓▓██████████████████
████████████████████████████████████████████░░▓▓████████████████▓▓▓▓██████████████████

                        .▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
                        ─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█
''')
    exit()
