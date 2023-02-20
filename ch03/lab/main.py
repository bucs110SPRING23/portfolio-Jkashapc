import turtle #1. import modules
from random import randrange 

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

# 5. Your PART A code goes here
don.down()
mic.down()
don.forward(randrange(1,100))
mic.forward(randrange(1,100))
don.up()
mic.up()
don.goto(-100,20)
mic.goto(-100,-20)

for _ in range(0,10):
     don.forward(randrange(1,10))
     mic.forward(randrange(1,10))
don.goto(-100,20)
mic.goto(-100,-20)


window.exitonclick()

# PART B - complete part B here
import pygame
import math 

pygame.init()
screen=pygame.display.set_mode()
# screen.fill("green")
pygame.display.flip()
xpos = 100
ypos = 100
side_length = 40


for num_sides in [3,4,6,20,100,360]:
    points =[]
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle*i)
        x = xpos + side_length * math.cos(radians)
        y = ypos +side_length * math.sin(radians)
        points.append((x, y))
    pygame.draw.polygon(screen, 'green', points )
    pygame.display.flip()
    pygame.time.wait(3000)
    screen.fill('black')
    pygame.display.flip()



  




