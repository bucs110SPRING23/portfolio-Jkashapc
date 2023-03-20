import turtle

def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_ellipse(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(width/2, 90)
    turtle.circle(height/2, 90)
    turtle.left(90)
    turtle.end_fill()

turtle.speed(0)
turtle.bgcolor('pink')

draw_circle(80, 'pink')

turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()
draw_ellipse(30, 60, 'pink')

turtle.penup()
turtle.goto(50, 150)
turtle.pendown()
draw_ellipse(30, 60, 'pink')

turtle.penup()
turtle.goto(-25, 120)
turtle.pendown()
draw_circle(10, 'white')

turtle.penup()
turtle.goto(25, 120)
turtle.pendown()
draw_circle(10, 'white')

turtle.penup()
turtle.goto(-20, 115)
turtle.pendown()
draw_circle(5, 'black')

turtle.penup()
turtle.goto(30, 115)
turtle.pendown()
draw_circle(5, 'black')

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
draw_circle(20, 'black')

turtle.penup()
turtle.goto(-30, 60)
turtle.pendown()
turtle.right(45)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
draw_circle(120, 'pink')

turtle.penup()
turtle.goto(-60, -110)
turtle.pendown()
draw_ellipse(20, 50, 'pink')

turtle.penup()
turtle.goto(60, -110)
turtle.pendown()
draw_ellipse(20, 50, 'pink')

turtle.penup()
turtle.goto(-45, -160)
turtle.pendown()
draw_ellipse(20, 50, 'pink')

turtle.penup()
turtle.goto(45, -160)
turtle.pendown()
draw_ellipse(20, 50, 'pink')

turtle.hideturtle()
turtle.done()