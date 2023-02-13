import turtle

window=turtle.Screen()
sides=input("How many sides does your desired shape have?:")
sides=int(sides)
length=input("What should the length of each side be?:")
length=int(length)


tur=turtle.Turtle()
tur.color('blue')
tur.shape('turtle')

for s in range(sides):
     tur.down
     tur.forward(length)
     tur.right(360/sides)





window.exitonclick()


