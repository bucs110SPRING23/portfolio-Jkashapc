import turtle
import random 
window=turtle.Screen()
def in_screen (window, t):
    
don=turtle.Turtle()
don.shape('turtle')
don.color('blue')
don.speed(0)
dist=10
angle=90
in_screen=True
while in_screen:
    flip=random.randrange(0,2)
    if flip:
        don.right(angle)
    else:
        don.left(angle)
    don.forward(dist)

    donx=don.xcor()
    dony=don.ycor()
    xrange=window.window_width()/2
    yrange=window.window_height()/2
    don.color(random.choice(colors))

    if abs(donx)>xrange or abs(dony)>yrange:
        in_screen=False


   
turtle.exitonclick()