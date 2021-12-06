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


# ======================================================================================================================
# Game Intro
def intro():
    print(GREEN + '''
    ╔╔══════════════════════╗╗ 
    ║║▐█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▌║║ 
    ║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
    ║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║ 
    ║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║ 
    ║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
    ║║▐▌▒▒░░▒▒░░▒▒░░▒▒░░▒▒▐▌║║ 
    ║║▐▌░░▒▒░░▒▒░░▒▒░░▒▒░░▐▌║║ 
    ║║▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▌║║ 
    ╚╚══════════════════════╝╝ 
    ██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
    ██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
    ██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ 
    ██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██ 
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    ''', GREEN + '''
    ==========================''', YELLOW + '''
     𝙇𝙤𝙨𝙩 𝙞𝙣 𝙩𝙝𝙚 𝙃𝙪𝙣𝙩 𝙤𝙛 𝘿𝙚𝙨𝙥𝙖𝙞𝙧 
        ʙʏ: ᴊᴀɪᴍᴇ ꜱᴀʟᴄᴇᴅᴏ 
     ɴᴀᴛɪᴏɴᴀʟ ʟᴏᴜɪꜱ ᴜɴɪᴠᴇʀꜱɪᴛʏ''', GREEN + '''
    ==========================
    ''')

    # ======================================================================================================================
    time.sleep(a)
    print("===========================================================================================================")
    time.sleep(a)
    winsound.PlaySound("sound1", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound1 (background)
    print(YELLOW + "Introduction:")
    time.sleep(a)
    print(BLUE + "*Wakes up*")
    time.sleep(a)
    print("Wha... What happened? Where am I?")
    time.sleep(a)
    print("It's too dark to see anything...")
    time.sleep(a)
    print()
    startGame = input(YELLOW + "Would you like to start the game? (Y/N): ")
    if startGame == "n" or startGame == "N":
        print(GREEN + "Maybe next time")
        time.sleep(a)
        exit()

    elif startGame == "y" or startGame == "Y":
        main()


# ======================================================================================================================
# Intro continuation
def main():
    winsound.PlaySound("sound2", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound2 (background)
    time.sleep(a)
    print(GREEN)
    print("===========================================================================================================")
    time.sleep(a)
    print(YELLOW + "Continuation:")
    time.sleep(a)
    print(RESET + "Narrator: Everything is dark")
    time.sleep(c)
    print("Narrator: You feel around using your hands to see...")
    time.sleep(e)
    print("Narrator: The ground is cold, damp, and covered in thick vines...")
    time.sleep(f)
    print(BLUE + "You: *Walks forward*")
    time.sleep(a)
    print("You: I can't see!!")
    time.sleep(a)
    print("You: *Accidentally hits head on a rocky wall*")
    time.sleep(c)
    print("You: OUCH!!!")
    time.sleep(a)
    print(RESET + "Action: *The ground starts rumbling*")
    time.sleep(c)
    print("Action: *Water starts flooding in the area*")
    time.sleep(e)
    print(BLUE + "You: I need to get out of here...")
    time.sleep(f)
    print("You: I must be in a cave...")
    time.sleep(b)
    print("You: *Looks up and sees a bright light*")
    time.sleep(a)
    print("You: And I'm all the way down here in a the cave's hole...how did I even get here?")
    time.sleep(h)
    print('''You: *Looks down, raises foot (Notices flooding), puts foot back to the ground & then bends down...''')
    time.sleep(i)
    print("You: *touches water*")
    time.sleep(e)
    print("You: *Shakes and dries hand*")
    time.sleep(e)
    print("You: This won't take long...the cave will be flooded with water at any second...")
    time.sleep(e)
    print("You: This cave must be surrounded by swamp water...")
    time.sleep(e)
    print("You: *Walks towards a rocky wall & touches*...I can climb this...")
    time.sleep(d)
    print("You: *Climbs wall*")
    time.sleep(a)
    print(RESET + "Narrator: As you climb the wall you suddenly hear...creepy sounds")
    time.sleep(e)
    print(RED + "Creature: *GROWLS*")
    winsound.PlaySound("sound5", winsound.SND_ALIAS)  # Squeal Sound5 (not background)
    winsound.PlaySound("sound2", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound2 (background)
    time.sleep(a)
    print(BLUE + "You: OMG WHAT IS THAT?")
    time.sleep(c)
    print("You: *Sees shadow*")
    time.sleep(a)
    print("You: Who are you?...*panics*... SHOW YOURSELF!")
    time.sleep(b)
    print(RED + "Creature: *GROWLS*")
    winsound.PlaySound("sound5", winsound.SND_ALIAS)  # Squeal Sound5 (not background)
    time.sleep(a)
    print("Creature: *TURNS CHAINSAW ON*")
    winsound.PlaySound("sound3", winsound.SND_ALIAS)  # Chainsaw Sound3 (not background)
    winsound.PlaySound("sound2", winsound.SND_ALIAS | winsound.SND_ASYNC)  # Intro Sound2 (background)
    time.sleep(a)
    print(BLUE + "You: OH MY GOD WHAT IS THAT??!!")
    time.sleep(d)
    print("You: I NEED TO GET OUT OF HERE!!")
    time.sleep(a)
    print("You: *Tries to climb wall rapidly*")
    time.sleep(c)
    print("You: *Slips and falls towards the ground*")
    time.sleep(a)
    scream = 'You: "AHHHHHHHHHHHHHHHHHHHHHH!"'
    for character in scream:
        sys.stdout.write(character)
        sys.stdout.flush()
    winsound.PlaySound("sound4", winsound.SND_ALIAS)  # Scream Sound4 (not background)
    print(RESET)
    time.sleep(e)
    winsound.PlaySound(None, winsound.SND_ALIAS)  # Stops Sounds
# ======================================================================================================================


