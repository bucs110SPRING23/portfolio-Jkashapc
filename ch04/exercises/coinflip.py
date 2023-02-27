import turtle
import random 
window=turtle.Screen()
don=turtle.Turtle()
don.shape(turtle)
don.color('blue')
flip=random.choice['heads','tails']
don.goto(-100,20)
don.down()
for i in flip:
    if flip is 'heads':
        don.right(90)
        don.forward(50)
    elif flip is 'tails':
        don.left(90)
        don.forward(50)
    



window.exitonclick()