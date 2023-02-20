from turtle import Turtle
from random import randrange

window = turtle.Screen()
window.bgcolor('lightblue')

don= Turtle()   
mic= Turtle()
don.color('red')
mic.color('black')
don.shape('turtle')
mic.shape('turtle')

don.up()
mic.up()
don.goto(-100,20)
mic.goto(-100,-20)

don.down()
mic.down()
don.forward(randrange(1,100))
mic.forward(randrange(1,100))



window.exitonclick()