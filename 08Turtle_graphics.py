# Turtle graphics
from turtle import Turtle, Screen

Tommy = Turtle()
Tommy.shape("turtle")
Tommy.color("red", "green")
Tommy.speed(1)
Tommy.forward(50)
Tommy.right(45)
Tommy.forward(50)

my_screen = Screen()
my_screen.bgcolor("yellow")
my_screen.exitonclick()
