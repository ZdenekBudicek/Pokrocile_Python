from turtle import Turtle, Screen

colors = ["violet", "yellow", "red", "green", "blue", "pink"]

arrow = Turtle("arrow")
arrow.pensize(3)
arrow.speed(0)

for x in range(300):
    arrow.pencolor(colors[x % 6])
    arrow.forward(x)
    arrow.left(60)

screen = Screen()
screen.exitonclick()
