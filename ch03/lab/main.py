import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

don = turtle.Turtle() # 3.  Create two turtles
mic = turtle.Turtle()
don.color('orange')
mic.color('blue')
don.shape('turtle')
mic.shape('turtle')

don.up() # 4. Pick up the pen so we don’t get lines
mic.up()
don.goto(-100,20)
mic.goto(-100,-20)

## 5. Your PART A code goes here
don.down()
mic.down()
don.forward(randrange(1,100))
mic.forward(randrange(1,100))

# PART B - complete part B here


window.exitonclick()
