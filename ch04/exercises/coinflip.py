import turtle
import random 
window=turtle.Screen()
don=turtle.Turtle()
don.shape('turtle')
don.color('blue')
def isInscreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False

while isInscreen(window, don):
    flip=random.choice['heads','tails']
    if flip == 'heads':
        don.right(90)
        don.forward(50)
    else:
        don.left(90)
        break
    don.forward(50)
    
turtle.exitonclick()