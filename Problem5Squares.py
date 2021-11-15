# Jaime S.
# 11/9/2021
# This is a program uses some code already provided with the intention to produce various looping squared shapes
# Helpful information: Simple program to use, you would just run it and expect to see various looping squared shapes
import turtle           # requests turtle module


def drawSquare(t, sz):  # Will define draw square as turtle and size
    for i in range(4):  # Will repeat the loop 4 times:
        t.forward(sz)   # The turtle will move forward
        t.left(90)      # The turtle will move left
        t.hideturtle()  # Will hide the turtle


wn = turtle.Screen()    # Sets up a window and its attributes

alex = turtle.Turtle()  # Creates alex
alex.color("blue")      # Adds color blue to alex

size = 20               # Square size set to 20

for i in range(5):      # Will repeat the loop 4 times
    drawSquare(alex, size)  # Draws alex's size
    size = size + 20        # Adds 20 to size
    alex.penup()            # Picks penup
    alex.goto(alex.pos() + (-10, -10))  # Sends alex to a different position
    alex.pendown()  # Puts pen down

wn.exitonclick()    # Will exit on click
