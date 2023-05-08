from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)

# Generování a nastavení objektu
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(0)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def circle(gap):
    for number in range(int(360 / gap)):
        tommy.pencolor(color())
        tommy.circle(80)
        tommy.left(gap)


circle(10)

my_screen = Screen()
my_screen.exitonclick()
